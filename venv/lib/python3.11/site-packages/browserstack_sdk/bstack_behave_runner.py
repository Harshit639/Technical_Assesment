import os
from behave.runner import Runner, Context
from behave.step_registry import registry as the_step_registry
class BehaveRunner(Runner):
    def run_model(self, features=None):
        if not self.context:
            self.context = Context(self)
        if self.step_registry is None:
            self.step_registry = the_step_registry
        if features is None:
            features = self.features
        context = self.context
        self.hook_failures = 0
        self.setup_capture()
        self.run_hook("before_all", context)
        run_feature = not self.aborted
        failed_count = 0
        undefined_steps_initial_size = len(self.undefined_steps)
        for feature in features:
            feature_failed_count = 0
            if run_feature:
                try:
                    self.feature = feature
                    for formatter in self.formatters:
                        formatter.uri(feature.filename)
                    while feature_failed_count <= int(self.config.userdata.get("retries", 0)):
                        failed = feature.run(self)
                        if not failed:
                            break
                        feature_failed_count += 1
                    if failed:
                        failed_count += 1
                        if self.config.stop or self.aborted:
                            run_feature = False
                except KeyboardInterrupt:
                    self.abort(reason="KeyboardInterrupt")
                    failed_count += 1
                    run_feature = False
            for reporter in self.config.reporters:
                reporter.feature(feature)
        cleanups_failed = False
        self.run_hook("after_all", self.context)
        try:
            self.context._do_cleanups()  # Without dropping the last context layer.
        except Exception:
            cleanups_failed = True
        if self.aborted:
            print("\nABORTED: By user.")
        for formatter in self.formatters:
            formatter.close()
        for reporter in self.config.reporters:
            reporter.end()
        failed = (
            (failed_count > 0)
            or self.aborted
            or (self.hook_failures > 0)
            or (len(self.undefined_steps) > undefined_steps_initial_size)
            or cleanups_failed
        )
        return failed
