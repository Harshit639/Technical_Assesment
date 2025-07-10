# coding: UTF-8
import sys
bstack1111l1l_opy_ = sys.version_info [0] == 2
bstack1l1l_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l1ll_opy_ (bstack1llll11_opy_):
    global bstack1l11111_opy_
    bstack11l11l_opy_ = ord (bstack1llll11_opy_ [-1])
    bstack11l11ll_opy_ = bstack1llll11_opy_ [:-1]
    bstack111ll1l_opy_ = bstack11l11l_opy_ % len (bstack11l11ll_opy_)
    bstack1l1l11l_opy_ = bstack11l11ll_opy_ [:bstack111ll1l_opy_] + bstack11l11ll_opy_ [bstack111ll1l_opy_:]
    if bstack1111l1l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l_opy_ - (bstack1l1l1l_opy_ + bstack11l11l_opy_) % bstack1llllll1_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1l1l11l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack1l1l_opy_ - (bstack1l1l1l_opy_ + bstack11l11l_opy_) % bstack1llllll1_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1l1l11l_opy_)])
    return eval (bstack1ll1_opy_)
import os
from datetime import datetime, timezone
from uuid import uuid4
from typing import Dict, List, Any, Tuple
from browserstack_sdk.sdk_cli.bstack1lllll1l1l1_opy_ import bstack1lllll1111l_opy_
from browserstack_sdk.sdk_cli.utils.bstack11l1lll11l_opy_ import bstack1l1111111ll_opy_
from pathlib import Path
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.test_framework import (
    TestFramework,
    bstack1llll11ll11_opy_,
    bstack1lll1ll1111_opy_,
    bstack1lll1111lll_opy_,
    bstack1l111lll1ll_opy_,
    bstack1llll11llll_opy_,
)
import traceback
from bstack_utils.helper import bstack1l1ll1l11ll_opy_
from bstack_utils.bstack11l1l111l_opy_ import bstack1llll11l1l1_opy_
from bstack_utils.constants import EVENTS
from browserstack_sdk.sdk_cli.utils.bstack1ll1llllll1_opy_ import bstack1ll1l1ll11l_opy_
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import bstack111111l1ll_opy_
bstack1l1ll1lll1l_opy_ = bstack1l1ll1l11ll_opy_()
bstack1l1lll11l11_opy_ = bstack1l1ll_opy_ (u"ࠣࡗࡳࡰࡴࡧࡤࡦࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹ࠭ࠣᐚ")
bstack11llllll11l_opy_ = bstack1l1ll_opy_ (u"ࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰࠧᐛ")
bstack1l1111l1ll1_opy_ = bstack1l1ll_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠤᐜ")
bstack1l111lll11l_opy_ = 1.0
_1l1ll111lll_opy_ = set()
class PytestBDDFramework(TestFramework):
    bstack1l111l1llll_opy_ = bstack1l1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩ࡭ࡽࡺࡵࡳࡧࡶࠦᐝ")
    bstack1l111ll1l1l_opy_ = bstack1l1ll_opy_ (u"ࠧࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࡡࡶࡸࡦࡸࡴࡦࡦࠥᐞ")
    bstack11llllll1ll_opy_ = bstack1l1ll_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡵࡢࡪ࡮ࡴࡩࡴࡪࡨࡨࠧᐟ")
    bstack1l1111ll11l_opy_ = bstack1l1ll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡰࡦࡹࡴࡠࡵࡷࡥࡷࡺࡥࡥࠤᐠ")
    bstack1l111111ll1_opy_ = bstack1l1ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡱࡧࡳࡵࡡࡩ࡭ࡳ࡯ࡳࡩࡧࡧࠦᐡ")
    bstack1l1111lllll_opy_: bool
    bstack111111l11l_opy_: bstack111111l1ll_opy_  = None
    bstack1l111lllll1_opy_ = [
        bstack1llll11ll11_opy_.BEFORE_ALL,
        bstack1llll11ll11_opy_.AFTER_ALL,
        bstack1llll11ll11_opy_.BEFORE_EACH,
        bstack1llll11ll11_opy_.AFTER_EACH,
    ]
    def __init__(
        self,
        bstack1l111l1ll1l_opy_: Dict[str, str],
        bstack1ll1l111111_opy_: List[str]=[bstack1l1ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨᐢ")],
        bstack111111l11l_opy_: bstack111111l1ll_opy_ = None,
        bstack1lll1ll111l_opy_=None
    ):
        super().__init__(bstack1ll1l111111_opy_, bstack1l111l1ll1l_opy_, bstack111111l11l_opy_)
        self.bstack1l1111lllll_opy_ = any(bstack1l1ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠢᐣ") in item.lower() for item in bstack1ll1l111111_opy_)
        self.bstack1lll1ll111l_opy_ = bstack1lll1ll111l_opy_
    def track_event(
        self,
        context: bstack1l111lll1ll_opy_,
        test_framework_state: bstack1llll11ll11_opy_,
        test_hook_state: bstack1lll1111lll_opy_,
        *args,
        **kwargs,
    ):
        super().track_event(self, context, test_framework_state, test_hook_state, *args, **kwargs)
        if test_framework_state == bstack1llll11ll11_opy_.TEST or test_framework_state in PytestBDDFramework.bstack1l111lllll1_opy_:
            bstack1l1111111ll_opy_(test_framework_state, test_hook_state)
        if test_framework_state == bstack1llll11ll11_opy_.NONE:
            self.logger.warning(bstack1l1ll_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨࡨࠥࡩࡡ࡭࡮ࡥࡥࡨࡱࠠࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫࠽ࡼࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨࡁࠧᐤ") + str(test_hook_state) + bstack1l1ll_opy_ (u"ࠧࠨᐥ"))
            return
        if not self.bstack1l1111lllll_opy_:
            self.logger.warning(bstack1l1ll_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥࡻ࡮ࡴࡷࡳࡴࡴࡸࡴࡦࡦࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡃࠢᐦ") + str(str(self.bstack1ll1l111111_opy_)) + bstack1l1ll_opy_ (u"ࠢࠣᐧ"))
            return
        if not isinstance(args, tuple) or len(args) == 0:
            self.logger.warning(bstack1l1ll_opy_ (u"ࠣࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰࡨࡼࡵ࡫ࡣࡵࡧࡧࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᐨ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠤࠥᐩ"))
            return
        instance = self.__1l111l11ll1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        if not instance:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡸࡷࡧࡣ࡬ࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡥࡷ࡭ࡳ࠾ࠤᐪ") + str(args) + bstack1l1ll_opy_ (u"ࠦࠧᐫ"))
            return
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1l111lllll1_opy_ and test_hook_state == bstack1lll1111lll_opy_.PRE:
                bstack1ll1l11l11l_opy_ = bstack1llll11l1l1_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack1ll111111_opy_.value)
                name = str(EVENTS.bstack1ll111111_opy_.name)+bstack1l1ll_opy_ (u"ࠧࡀࠢᐬ")+str(test_framework_state.name)
                TestFramework.bstack1l111l11111_opy_(instance, name, bstack1ll1l11l11l_opy_)
        except Exception as e:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮࡯ࡰ࡭ࠣࡩࡷࡸ࡯ࡳࠢࡳࡶࡪࡀࠠࡼࡿࠥᐭ").format(e))
        try:
            if test_framework_state == bstack1llll11ll11_opy_.TEST:
                if not TestFramework.bstack1lllllllll1_opy_(instance, TestFramework.bstack1l111l111ll_opy_) and test_hook_state == bstack1lll1111lll_opy_.PRE:
                    if not (len(args) >= 3):
                        return
                    test = PytestBDDFramework.__1l111llll11_opy_(args)
                    if test:
                        instance.data.update(test)
                        self.logger.debug(bstack1l1ll_opy_ (u"ࠢ࡭ࡱࡤࡨࡪࡪࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢᐮ") + str(test_hook_state) + bstack1l1ll_opy_ (u"ࠣࠤᐯ"))
                if test_hook_state == bstack1lll1111lll_opy_.PRE and not TestFramework.bstack1lllllllll1_opy_(instance, TestFramework.bstack1l1lll111ll_opy_):
                    TestFramework.bstack1lllll1l111_opy_(instance, TestFramework.bstack1l1lll111ll_opy_, datetime.now(tz=timezone.utc))
                    PytestBDDFramework.__1l111l1ll11_opy_(instance, args)
                    self.logger.debug(bstack1l1ll_opy_ (u"ࠤࡶࡩࡹࠦࡴࡦࡵࡷ࠱ࡸࡺࡡࡳࡶࠣࡪࡴࡸࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢᐰ") + str(test_hook_state) + bstack1l1ll_opy_ (u"ࠥࠦᐱ"))
                elif test_hook_state == bstack1lll1111lll_opy_.POST and not TestFramework.bstack1lllllllll1_opy_(instance, TestFramework.bstack1l1ll1ll1ll_opy_):
                    TestFramework.bstack1lllll1l111_opy_(instance, TestFramework.bstack1l1ll1ll1ll_opy_, datetime.now(tz=timezone.utc))
                    self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡸ࡫ࡴࠡࡶࡨࡷࡹ࠳ࡥ࡯ࡦࠣࡪࡴࡸࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࡸࡥࡧࠪࠬࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢᐲ") + str(test_hook_state) + bstack1l1ll_opy_ (u"ࠧࠨᐳ"))
            elif test_framework_state == bstack1llll11ll11_opy_.STEP:
                if test_hook_state == bstack1lll1111lll_opy_.PRE:
                    PytestBDDFramework.__1l11111llll_opy_(instance, args)
                elif test_hook_state == bstack1lll1111lll_opy_.POST:
                    PytestBDDFramework.__1l11l111l11_opy_(instance, args)
            elif test_framework_state == bstack1llll11ll11_opy_.LOG and test_hook_state == bstack1lll1111lll_opy_.POST:
                PytestBDDFramework.__1l111l11l1l_opy_(instance, *args)
            elif test_framework_state == bstack1llll11ll11_opy_.LOG_REPORT and test_hook_state == bstack1lll1111lll_opy_.POST:
                self.__1l11l111ll1_opy_(instance, *args)
                self.__1l111ll1111_opy_(instance)
            elif test_framework_state in PytestBDDFramework.bstack1l111lllll1_opy_:
                self.__1l11111l11l_opy_(instance, test_framework_state, test_hook_state, *args)
            self.logger.debug(bstack1l1ll_opy_ (u"ࠨࡴࡳࡣࡦ࡯ࡤ࡫ࡶࡦࡰࡷ࠾ࠥ࡮ࡡ࡯ࡦ࡯ࡩࡩࠦࡥࡷࡧࡱࡸࡂࢁࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࠢᐴ") + str(instance.ref()) + bstack1l1ll_opy_ (u"ࠢࠣᐵ"))
        except Exception as e:
            self.logger.error(e)
            traceback.print_exc()
        self.bstack1l111l1l1l1_opy_(instance, (test_framework_state, test_hook_state), *args, **kwargs)
        try:
            if instance!= None and test_framework_state in PytestBDDFramework.bstack1l111lllll1_opy_ and test_hook_state == bstack1lll1111lll_opy_.POST:
                name = str(EVENTS.bstack1ll111111_opy_.name)+bstack1l1ll_opy_ (u"ࠣ࠼ࠥᐶ")+str(test_framework_state.name)
                bstack1ll1l11l11l_opy_ = TestFramework.bstack1l111ll1lll_opy_(instance, name)
                bstack1llll11l1l1_opy_.end(EVENTS.bstack1ll111111_opy_.value, bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᐷ"), bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᐸ"), True, None, test_framework_state.name)
        except Exception as e:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣ࡬ࡴࡵ࡫ࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᐹ").format(e))
    def bstack1l1l1lll1ll_opy_(self):
        return self.bstack1l1111lllll_opy_
    def __1l111111l11_opy_(self, *args):
        if len(args) > 2 and callable(getattr(args[2], bstack1l1ll_opy_ (u"ࠧ࡭ࡥࡵࡡࡵࡩࡸࡻ࡬ࡵࠤᐺ"), None)):
            rep = args[2].get_result()
            if rep:
                return TestFramework.bstack1l1ll11111l_opy_(rep, [bstack1l1ll_opy_ (u"ࠨࡷࡩࡧࡱࠦᐻ"), bstack1l1ll_opy_ (u"ࠢࡰࡷࡷࡧࡴࡳࡥࠣᐼ"), bstack1l1ll_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣᐽ"), bstack1l1ll_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤᐾ"), bstack1l1ll_opy_ (u"ࠥࡷࡰ࡯ࡰࡱࡧࡧࠦᐿ"), bstack1l1ll_opy_ (u"ࠦࡱࡵ࡮ࡨࡴࡨࡴࡷࡺࡥࡹࡶࠥᑀ")])
        return None
    def __1l11l111ll1_opy_(self, instance: bstack1lll1ll1111_opy_, *args):
        result = self.__1l111111l11_opy_(*args)
        if not result:
            return
        failure = None
        bstack111111llll_opy_ = None
        if result.get(bstack1l1ll_opy_ (u"ࠧࡵࡵࡵࡥࡲࡱࡪࠨᑁ"), None) == bstack1l1ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨᑂ") and len(args) > 1 and getattr(args[1], bstack1l1ll_opy_ (u"ࠢࡦࡺࡦ࡭ࡳ࡬࡯ࠣᑃ"), None) is not None:
            failure = [{bstack1l1ll_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᑄ"): [args[1].excinfo.exconly(), result.get(bstack1l1ll_opy_ (u"ࠤ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠣᑅ"), None)]}]
            bstack111111llll_opy_ = bstack1l1ll_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࡋࡲࡳࡱࡵࠦᑆ") if bstack1l1ll_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢᑇ") in getattr(args[1].excinfo, bstack1l1ll_opy_ (u"ࠧࡺࡹࡱࡧࡱࡥࡲ࡫ࠢᑈ"), bstack1l1ll_opy_ (u"ࠨࠢᑉ")) else bstack1l1ll_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣᑊ")
        bstack1l11111lll1_opy_ = result.get(bstack1l1ll_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤᑋ"), TestFramework.bstack1l11l1111l1_opy_)
        if bstack1l11111lll1_opy_ != TestFramework.bstack1l11l1111l1_opy_:
            TestFramework.bstack1lllll1l111_opy_(instance, TestFramework.bstack1l1lll11111_opy_, datetime.now(tz=timezone.utc))
        TestFramework.bstack1l11111ll1l_opy_(instance, {
            TestFramework.bstack1l1l11111l1_opy_: failure,
            TestFramework.bstack1l111l111l1_opy_: bstack111111llll_opy_,
            TestFramework.bstack1l1l111l1ll_opy_: bstack1l11111lll1_opy_,
        })
    def __1l111l11ll1_opy_(
        self,
        context: bstack1l111lll1ll_opy_,
        test_framework_state: bstack1llll11ll11_opy_,
        test_hook_state: bstack1lll1111lll_opy_,
        *args,
        **kwargs,
    ):
        instance = None
        if test_framework_state == bstack1llll11ll11_opy_.SETUP_FIXTURE:
            instance = self.__1l1111llll1_opy_(context, test_framework_state, test_hook_state, *args, **kwargs)
        else:
            target = None # bstack1l1111ll1l1_opy_ bstack1l1111ll111_opy_ this to be bstack1l1ll_opy_ (u"ࠤࡱࡳࡩ࡫ࡩࡥࠤᑌ")
            if test_framework_state == bstack1llll11ll11_opy_.INIT_TEST:
                target = args[0] if isinstance(args[0], str) else None
                if target:
                    self.__1l1111lll1l_opy_(context, test_framework_state, target, *args)
            elif test_framework_state == bstack1llll11ll11_opy_.LOG:
                nodeid = getattr(getattr(args[0], bstack1l1ll_opy_ (u"ࠥࡲࡴࡪࡥࠣᑍ"), None), bstack1l1ll_opy_ (u"ࠦࡳࡵࡤࡦ࡫ࡧࠦᑎ"), None) if args else None
                if isinstance(nodeid, str):
                    target = nodeid
            elif getattr(args[0], bstack1l1ll_opy_ (u"ࠧࡴ࡯ࡥࡧࠥᑏ"), None):
                target = args[0].node.nodeid
            elif getattr(args[0], bstack1l1ll_opy_ (u"ࠨ࡮ࡰࡦࡨ࡭ࡩࠨᑐ"), None):
                target = args[0].nodeid
            instance = TestFramework.bstack1lllll1l11l_opy_(target) if target else None
        return instance
    def __1l11111l11l_opy_(
        self,
        instance: bstack1lll1ll1111_opy_,
        test_framework_state: bstack1llll11ll11_opy_,
        test_hook_state: bstack1lll1111lll_opy_,
        *args,
    ):
        key = test_framework_state.name
        bstack1l1111111l1_opy_ = TestFramework.bstack1lllll111ll_opy_(instance, PytestBDDFramework.bstack1l111ll1l1l_opy_, {})
        if not key in bstack1l1111111l1_opy_:
            bstack1l1111111l1_opy_[key] = []
        bstack1l111lll111_opy_ = TestFramework.bstack1lllll111ll_opy_(instance, PytestBDDFramework.bstack11llllll1ll_opy_, {})
        if not key in bstack1l111lll111_opy_:
            bstack1l111lll111_opy_[key] = []
        bstack1l11l111lll_opy_ = {
            PytestBDDFramework.bstack1l111ll1l1l_opy_: bstack1l1111111l1_opy_,
            PytestBDDFramework.bstack11llllll1ll_opy_: bstack1l111lll111_opy_,
        }
        if test_hook_state == bstack1lll1111lll_opy_.PRE:
            hook_name = args[1] if len(args) > 1 else None
            hook = {
                bstack1l1ll_opy_ (u"ࠢ࡬ࡧࡼࠦᑑ"): key,
                TestFramework.bstack1l111ll11l1_opy_: uuid4().__str__(),
                TestFramework.bstack1l111l11l11_opy_: TestFramework.bstack1l111llllll_opy_,
                TestFramework.bstack1l11l1111ll_opy_: datetime.now(tz=timezone.utc),
                TestFramework.bstack1l1111ll1ll_opy_: [],
                TestFramework.bstack1l1111l1l11_opy_: hook_name,
                TestFramework.bstack11lllllll11_opy_: bstack1ll1l1ll11l_opy_.bstack11lllllll1l_opy_()
            }
            bstack1l1111111l1_opy_[key].append(hook)
            bstack1l11l111lll_opy_[PytestBDDFramework.bstack1l1111ll11l_opy_] = key
        elif test_hook_state == bstack1lll1111lll_opy_.POST:
            bstack1l111l1l111_opy_ = bstack1l1111111l1_opy_.get(key, [])
            hook = bstack1l111l1l111_opy_.pop() if bstack1l111l1l111_opy_ else None
            if hook:
                result = self.__1l111111l11_opy_(*args)
                if result:
                    bstack1l11111l1l1_opy_ = result.get(bstack1l1ll_opy_ (u"ࠣࡱࡸࡸࡨࡵ࡭ࡦࠤᑒ"), TestFramework.bstack1l111llllll_opy_)
                    if bstack1l11111l1l1_opy_ != TestFramework.bstack1l111llllll_opy_:
                        hook[TestFramework.bstack1l111l11l11_opy_] = bstack1l11111l1l1_opy_
                hook[TestFramework.bstack1l111l1lll1_opy_] = datetime.now(tz=timezone.utc)
                hook[TestFramework.bstack11lllllll11_opy_] = bstack1ll1l1ll11l_opy_.bstack11lllllll1l_opy_()
                self.bstack1l111llll1l_opy_(hook)
                logs = hook.get(TestFramework.bstack11lllllllll_opy_, [])
                self.bstack1l1ll1l1l1l_opy_(instance, logs)
                bstack1l111lll111_opy_[key].append(hook)
                bstack1l11l111lll_opy_[PytestBDDFramework.bstack1l111111ll1_opy_] = key
        TestFramework.bstack1l11111ll1l_opy_(instance, bstack1l11l111lll_opy_)
        self.logger.debug(bstack1l1ll_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡪࡲࡳࡰࡥࡥࡷࡧࡱࡸ࠿ࠦࡴࡦࡵࡷࡣ࡭ࡵ࡯࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽ࡮ࡩࡾࢃ࠮ࡼࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࢀࠤ࡭ࡵ࡯࡬ࡵࡢࡷࡹࡧࡲࡵࡧࡧࡁࢀ࡮࡯ࡰ࡭ࡶࡣࡸࡺࡡࡳࡶࡨࡨࢂࠦࡨࡰࡱ࡮ࡷࡤ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࠽ࠣᑓ") + str(bstack1l111lll111_opy_) + bstack1l1ll_opy_ (u"ࠥࠦᑔ"))
    def __1l1111llll1_opy_(
        self,
        context: bstack1l111lll1ll_opy_,
        test_framework_state: bstack1llll11ll11_opy_,
        test_hook_state: bstack1lll1111lll_opy_,
        *args,
        **kwargs,
    ):
        fixturedef = TestFramework.bstack1l1ll11111l_opy_(args[0], [bstack1l1ll_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥᑕ"), bstack1l1ll_opy_ (u"ࠧࡧࡲࡨࡰࡤࡱࡪࠨᑖ"), bstack1l1ll_opy_ (u"ࠨࡰࡢࡴࡤࡱࡸࠨᑗ"), bstack1l1ll_opy_ (u"ࠢࡪࡦࡶࠦᑘ"), bstack1l1ll_opy_ (u"ࠣࡷࡱ࡭ࡹࡺࡥࡴࡶࠥᑙ"), bstack1l1ll_opy_ (u"ࠤࡥࡥࡸ࡫ࡩࡥࠤᑚ")]) if len(args) > 0 else {}
        request = args[1] if len(args) > 1 else None
        scenario = args[2] if len(args) == 3 else None
        scope = request.scope if hasattr(request, bstack1l1ll_opy_ (u"ࠥࡷࡨࡵࡰࡦࠤᑛ")) else fixturedef.get(bstack1l1ll_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥᑜ"), None)
        fixturename = request.fixturename if hasattr(request, bstack1l1ll_opy_ (u"ࠧ࡬ࡩࡹࡶࡸࡶࡪࡴࡡ࡮ࡧࠥᑝ")) else None
        node = request.node if hasattr(request, bstack1l1ll_opy_ (u"ࠨ࡮ࡰࡦࡨࠦᑞ")) else None
        target = request.node.nodeid if hasattr(node, bstack1l1ll_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᑟ")) else None
        baseid = fixturedef.get(bstack1l1ll_opy_ (u"ࠣࡤࡤࡷࡪ࡯ࡤࠣᑠ"), None) or bstack1l1ll_opy_ (u"ࠤࠥᑡ")
        if (not target or len(baseid) > 0) and hasattr(request, bstack1l1ll_opy_ (u"ࠥࡣࡵࡿࡦࡶࡰࡦ࡭ࡹ࡫࡭ࠣᑢ")):
            target = PytestBDDFramework.__1l1111l11ll_opy_(request._pyfuncitem.location) if hasattr(request._pyfuncitem, bstack1l1ll_opy_ (u"ࠦࡱࡵࡣࡢࡶ࡬ࡳࡳࠨᑣ")) else None
            if target and not TestFramework.bstack1lllll1l11l_opy_(target):
                self.__1l1111lll1l_opy_(context, test_framework_state, target, (target, request._pyfuncitem.location))
                node = request._pyfuncitem
                self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡺࡲࡢࡥ࡮ࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࡫ࡶࡦࡰࡷ࠾ࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱࠠࡵࡣࡵ࡫ࡪࡺ࠽ࡼࡶࡤࡶ࡬࡫ࡴࡾࠢࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫࠽ࡼࡨ࡬ࡼࡹࡻࡲࡦࡰࡤࡱࡪࢃࠠ࡯ࡱࡧࡩࡂࢁ࡮ࡰࡦࡨࢁࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࠢᑤ") + str(test_hook_state) + bstack1l1ll_opy_ (u"ࠨࠢᑥ"))
        if not fixturedef or not scope or not target:
            self.logger.warning(bstack1l1ll_opy_ (u"ࠢࡵࡴࡤࡧࡰࡥࡦࡪࡺࡷࡹࡷ࡫࡟ࡦࡸࡨࡲࡹࡀࠠࡶࡰ࡫ࡥࡳࡪ࡬ࡦࡦࠣࡩࡻ࡫࡮ࡵ࠿ࡾࡸࡪࡹࡴࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸࡺࡡࡵࡧࢀ࠲ࢀࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦࡦࡨࡪࡂࢁࡦࡪࡺࡷࡹࡷ࡫ࡤࡦࡨࢀࠤࡸࡩ࡯ࡱࡧࡀࡿࡸࡩ࡯ࡱࡧࢀࠤࡹࡧࡲࡨࡧࡷࡁࠧᑦ") + str(target) + bstack1l1ll_opy_ (u"ࠣࠤᑧ"))
            return None
        instance = TestFramework.bstack1lllll1l11l_opy_(target)
        if not instance:
            self.logger.warning(bstack1l1ll_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡨ࡬ࡼࡹࡻࡲࡦࡡࡨࡺࡪࡴࡴ࠻ࠢࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࠥ࡫ࡶࡦࡰࡷࡁࢀࡺࡥࡴࡶࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂ࠴ࡻࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࡿࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡤࡤࡷࡪ࡯ࡤ࠾ࡽࡥࡥࡸ࡫ࡩࡥࡿࠣࡸࡦࡸࡧࡦࡶࡀࠦᑨ") + str(target) + bstack1l1ll_opy_ (u"ࠥࠦᑩ"))
            return None
        bstack1l111111l1l_opy_ = TestFramework.bstack1lllll111ll_opy_(instance, PytestBDDFramework.bstack1l111l1llll_opy_, {})
        if os.getenv(bstack1l1ll_opy_ (u"ࠦࡘࡊࡋࡠࡅࡏࡍࡤࡌࡌࡂࡉࡢࡊࡎ࡞ࡔࡖࡔࡈࡗࠧᑪ"), bstack1l1ll_opy_ (u"ࠧ࠷ࠢᑫ")) == bstack1l1ll_opy_ (u"ࠨ࠱ࠣᑬ"):
            bstack1l11111l111_opy_ = bstack1l1ll_opy_ (u"ࠢ࠻ࠤᑭ").join((scope, fixturename))
            bstack1l1111l11l1_opy_ = datetime.now(tz=timezone.utc)
            bstack1l11111111l_opy_ = {
                bstack1l1ll_opy_ (u"ࠣ࡭ࡨࡽࠧᑮ"): bstack1l11111l111_opy_,
                bstack1l1ll_opy_ (u"ࠤࡷࡥ࡬ࡹࠢᑯ"): PytestBDDFramework.__1l11l111111_opy_(request.node, scenario),
                bstack1l1ll_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨࠦᑰ"): fixturedef,
                bstack1l1ll_opy_ (u"ࠦࡸࡩ࡯ࡱࡧࠥᑱ"): scope,
                bstack1l1ll_opy_ (u"ࠧࡺࡹࡱࡧࠥᑲ"): None,
            }
            try:
                if test_hook_state == bstack1lll1111lll_opy_.POST and callable(getattr(args[-1], bstack1l1ll_opy_ (u"ࠨࡧࡦࡶࡢࡶࡪࡹࡵ࡭ࡶࠥᑳ"), None)):
                    bstack1l11111111l_opy_[bstack1l1ll_opy_ (u"ࠢࡵࡻࡳࡩࠧᑴ")] = TestFramework.bstack1l1lll11lll_opy_(args[-1].get_result())
            except Exception as e:
                pass
            if test_hook_state == bstack1lll1111lll_opy_.PRE:
                bstack1l11111111l_opy_[bstack1l1ll_opy_ (u"ࠣࡷࡸ࡭ࡩࠨᑵ")] = uuid4().__str__()
                bstack1l11111111l_opy_[PytestBDDFramework.bstack1l11l1111ll_opy_] = bstack1l1111l11l1_opy_
            elif test_hook_state == bstack1lll1111lll_opy_.POST:
                bstack1l11111111l_opy_[PytestBDDFramework.bstack1l111l1lll1_opy_] = bstack1l1111l11l1_opy_
            if bstack1l11111l111_opy_ in bstack1l111111l1l_opy_:
                bstack1l111111l1l_opy_[bstack1l11111l111_opy_].update(bstack1l11111111l_opy_)
                self.logger.debug(bstack1l1ll_opy_ (u"ࠤࡸࡴࡩࡧࡴࡦࡦࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦ࠿ࠥᑶ") + str(bstack1l111111l1l_opy_[bstack1l11111l111_opy_]) + bstack1l1ll_opy_ (u"ࠥࠦᑷ"))
            else:
                bstack1l111111l1l_opy_[bstack1l11111l111_opy_] = bstack1l11111111l_opy_
                self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡸࡧࡶࡦࡦࠣࡪ࡮ࡾࡴࡶࡴࡨࡲࡦࡳࡥ࠾ࡽࡩ࡭ࡽࡺࡵࡳࡧࡱࡥࡲ࡫ࡽࠡࡵࡦࡳࡵ࡫࠽ࡼࡵࡦࡳࡵ࡫ࡽࠡࡨ࡬ࡼࡹࡻࡲࡦ࠿ࡾࡸࡪࡹࡴࡠࡨ࡬ࡼࡹࡻࡲࡦࡿࠣࡸࡷࡧࡣ࡬ࡧࡧࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࡃࠢᑸ") + str(len(bstack1l111111l1l_opy_)) + bstack1l1ll_opy_ (u"ࠧࠨᑹ"))
        TestFramework.bstack1lllll1l111_opy_(instance, PytestBDDFramework.bstack1l111l1llll_opy_, bstack1l111111l1l_opy_)
        self.logger.debug(bstack1l1ll_opy_ (u"ࠨࡳࡢࡸࡨࡨࠥ࡬ࡩࡹࡶࡸࡶࡪࡹ࠽ࡼ࡮ࡨࡲ࠭ࡺࡲࡢࡥ࡮ࡩࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠪࡿࠣ࡭ࡳࡹࡴࡢࡰࡦࡩࡂࠨᑺ") + str(instance.ref()) + bstack1l1ll_opy_ (u"ࠢࠣᑻ"))
        return instance
    def __1l1111lll1l_opy_(
        self,
        context: bstack1l111lll1ll_opy_,
        test_framework_state: bstack1llll11ll11_opy_,
        target: Any,
        *args,
    ):
        ctx = bstack1lllll1111l_opy_.create_context(target)
        ob = bstack1lll1ll1111_opy_(ctx, self.bstack1ll1l111111_opy_, self.bstack1l111l1ll1l_opy_, test_framework_state)
        TestFramework.bstack1l11111ll1l_opy_(ob, {
            TestFramework.bstack1ll11llll11_opy_: context.test_framework_name,
            TestFramework.bstack1l1ll1ll11l_opy_: context.test_framework_version,
            TestFramework.bstack1l111l11lll_opy_: [],
            PytestBDDFramework.bstack1l111l1llll_opy_: {},
            PytestBDDFramework.bstack11llllll1ll_opy_: {},
            PytestBDDFramework.bstack1l111ll1l1l_opy_: {},
        })
        if len(args) > 1 and isinstance(args[1], tuple):
            TestFramework.bstack1lllll1l111_opy_(ob, TestFramework.bstack1l11l11111l_opy_, str(args[1][0]))
        if context.platform_index >= 0:
            TestFramework.bstack1lllll1l111_opy_(ob, TestFramework.bstack1ll111l111l_opy_, context.platform_index)
        TestFramework.bstack1llllllllll_opy_[ctx.id] = ob
        self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡵࡤࡺࡪࡪࠠࡪࡰࡶࡸࡦࡴࡣࡦࠢࡦࡸࡽ࠴ࡩࡥ࠿ࡾࡧࡹࡾ࠮ࡪࡦࢀࠤࡹࡧࡲࡨࡧࡷࡁࢀࡺࡡࡳࡩࡨࡸࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡹ࠽ࠣᑼ") + str(TestFramework.bstack1llllllllll_opy_.keys()) + bstack1l1ll_opy_ (u"ࠤࠥᑽ"))
        return ob
    @staticmethod
    def __1l111l1ll11_opy_(instance, args):
        request, feature, scenario = args
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1l1ll_opy_ (u"ࠪ࡭ࡩ࠭ᑾ"): id(step),
                bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡸࡵࠩᑿ"): step.name,
                bstack1l1ll_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭ᒀ"): step.keyword,
            })
        meta = {
            bstack1l1ll_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧᒁ"): {
                bstack1l1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᒂ"): feature.name,
                bstack1l1ll_opy_ (u"ࠨࡲࡤࡸ࡭࠭ᒃ"): feature.filename,
                bstack1l1ll_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧᒄ"): feature.description
            },
            bstack1l1ll_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬᒅ"): {
                bstack1l1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᒆ"): scenario.name
            },
            bstack1l1ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᒇ"): steps,
            bstack1l1ll_opy_ (u"࠭ࡥࡹࡣࡰࡴࡱ࡫ࡳࠨᒈ"): PytestBDDFramework.__1l11l111l1l_opy_(request.node)
        }
        instance.data.update(
            {
                TestFramework.bstack1l11l11l11l_opy_: meta
            }
        )
    def bstack1l111llll1l_opy_(self, hook: Dict[str, Any]) -> None:
        bstack1l1ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕࡸ࡯ࡤࡧࡶࡷࡪࡹࠠࡵࡪࡨࠤࡍࡵ࡯࡬ࡎࡨࡺࡪࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥࡹࡩ࡮࡫࡯ࡥࡷࠦࡴࡰࠢࡷ࡬ࡪࠦࡊࡢࡸࡤࠤ࡮ࡳࡰ࡭ࡧࡰࡩࡳࡺࡡࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡕࡪ࡬ࡷࠥࡳࡥࡵࡪࡲࡨ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡈ࡮ࡥࡤ࡭ࡶࠤࡹ࡮ࡥࠡࡊࡲࡳࡰࡒࡥࡷࡧ࡯ࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡪࡰࡶ࡭ࡩ࡫ࠠࡿ࠱࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠱ࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡇࡱࡵࠤࡪࡧࡣࡩࠢࡩ࡭ࡱ࡫ࠠࡪࡰࠣ࡬ࡴࡵ࡫ࡠ࡮ࡨࡺࡪࡲ࡟ࡧ࡫࡯ࡩࡸ࠲ࠠࡳࡧࡳࡰࡦࡩࡥࡴࠢࠥࡘࡪࡹࡴࡍࡧࡹࡩࡱࠨࠠࡸ࡫ࡷ࡬ࠥࠨࡈࡰࡱ࡮ࡐࡪࡼࡥ࡭ࠤࠣ࡭ࡳࠦࡩࡵࡵࠣࡴࡦࡺࡨ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡊࡨࠣࡥࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡴࡩࡧࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࡭ࡢࡶࡦ࡬ࡪࡹࠠࡢࠢࡰࡳࡩ࡯ࡦࡪࡧࡧࠤ࡭ࡵ࡯࡬࠯࡯ࡩࡻ࡫࡬ࠡࡨ࡬ࡰࡪ࠲ࠠࡪࡶࠣࡧࡷ࡫ࡡࡵࡧࡶࠤࡦࠦࡌࡰࡩࡈࡲࡹࡸࡹࠡࡱࡥ࡮ࡪࡩࡴࠡࡹ࡬ࡸ࡭ࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡨࡪࡺࡡࡪ࡮ࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡗ࡮ࡳࡩ࡭ࡣࡵࡰࡾ࠲ࠠࡪࡶࠣࡴࡷࡵࡣࡦࡵࡶࡩࡸࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡ࡮ࡲࡧࡦࡺࡥࡥࠢ࡬ࡲࠥࡎ࡯ࡰ࡭ࡏࡩࡻ࡫࡬࠰ࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡣࡻࠣࡶࡪࡶ࡬ࡢࡥ࡬ࡲ࡬ࠦࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦࠥࡽࡩࡵࡪࠣࠦࡍࡵ࡯࡬ࡎࡨࡺࡪࡲ࠯ࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࡌࡴࡵ࡫ࡆࡸࡨࡲࡹࠨ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡔࡩࡧࠣࡧࡷ࡫ࡡࡵࡧࡧࠤࡑࡵࡧࡆࡰࡷࡶࡾࠦ࡯ࡣ࡬ࡨࡧࡹࡹࠠࡢࡴࡨࠤࡦࡪࡤࡦࡦࠣࡸࡴࠦࡴࡩࡧࠣ࡬ࡴࡵ࡫ࠨࡵࠣࠦࡱࡵࡧࡴࠤࠣࡰ࡮ࡹࡴ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡩࡱࡲ࡯࠿ࠦࡔࡩࡧࠣࡩࡻ࡫࡮ࡵࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶࡾࠦࡣࡰࡰࡷࡥ࡮ࡴࡩ࡯ࡩࠣࡩࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡲ࡯ࡨࡵࠣࡥࡳࡪࠠࡩࡱࡲ࡯ࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡫ࡳࡴࡱ࡟࡭ࡧࡹࡩࡱࡥࡦࡪ࡮ࡨࡷ࠿ࠦࡌࡪࡵࡷࠤࡴ࡬ࠠࡑࡣࡷ࡬ࠥࡵࡢ࡫ࡧࡦࡸࡸࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠤࡲࡵ࡮ࡪࡶࡲࡶ࡮ࡴࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡣࡷ࡬ࡰࡩࡥ࡬ࡦࡸࡨࡰࡤ࡬ࡩ࡭ࡧࡶ࠾ࠥࡒࡩࡴࡶࠣࡳ࡫ࠦࡐࡢࡶ࡫ࠤࡴࡨࡪࡦࡥࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡸ࡭࡫ࠠࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠤࡲࡵ࡮ࡪࡶࡲࡶ࡮ࡴࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᒉ")
        global _1l1ll111lll_opy_
        platform_index = os.environ[bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨᒊ")]
        bstack1l1l1l1llll_opy_ = os.path.join(bstack1l1ll1lll1l_opy_, (bstack1l1lll11l11_opy_ + str(platform_index)), bstack11llllll11l_opy_)
        if not os.path.exists(bstack1l1l1l1llll_opy_) or not os.path.isdir(bstack1l1l1l1llll_opy_):
            return
        logs = hook.get(bstack1l1ll_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᒋ"), [])
        with os.scandir(bstack1l1l1l1llll_opy_) as entries:
            for entry in entries:
                abs_path = os.path.abspath(entry.path)
                if abs_path in _1l1ll111lll_opy_:
                    self.logger.info(bstack1l1ll_opy_ (u"ࠥࡔࡦࡺࡨࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥࢁࡽࠣᒌ").format(abs_path))
                    continue
                if entry.is_file():
                    try:
                        timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                    except Exception:
                        timestamp = bstack1l1ll_opy_ (u"ࠦࠧᒍ")
                    log_entry = bstack1llll11llll_opy_(
                        kind=bstack1l1ll_opy_ (u"࡚ࠧࡅࡔࡖࡢࡅ࡙࡚ࡁࡄࡊࡐࡉࡓ࡚ࠢᒎ"),
                        message=bstack1l1ll_opy_ (u"ࠨࠢᒏ"),
                        level=bstack1l1ll_opy_ (u"ࠢࠣᒐ"),
                        timestamp=timestamp,
                        fileName=entry.name,
                        bstack1l1l1ll1l11_opy_=entry.stat().st_size,
                        bstack1l1lll11l1l_opy_=bstack1l1ll_opy_ (u"ࠣࡏࡄࡒ࡚ࡇࡌࡠࡗࡓࡐࡔࡇࡄࠣᒑ"),
                        bstack1l1l1l1_opy_=os.path.abspath(entry.path),
                        bstack1l1111l111l_opy_=hook.get(TestFramework.bstack1l111ll11l1_opy_)
                    )
                    logs.append(log_entry)
                    _1l1ll111lll_opy_.add(abs_path)
        platform_index = os.environ[bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩᒒ")]
        bstack1l1111l1l1l_opy_ = os.path.join(bstack1l1ll1lll1l_opy_, (bstack1l1lll11l11_opy_ + str(platform_index)), bstack11llllll11l_opy_, bstack1l1111l1ll1_opy_)
        if not os.path.exists(bstack1l1111l1l1l_opy_) or not os.path.isdir(bstack1l1111l1l1l_opy_):
            self.logger.info(bstack1l1ll_opy_ (u"ࠥࡒࡴࠦࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࡋࡳࡴࡱࡅࡷࡧࡱࡸࠥࡧࡴࡵࡣࡦ࡬ࡲ࡫࡮ࡵࡵࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡦࡰࡷࡱࡨࠥࡧࡴ࠻ࠢࡾࢁࠧᒓ").format(bstack1l1111l1l1l_opy_))
        else:
            self.logger.info(bstack1l1ll_opy_ (u"ࠦࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࡍࡵ࡯࡬ࡇࡹࡩࡳࡺࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࡀࠠࡼࡿࠥᒔ").format(bstack1l1111l1l1l_opy_))
            with os.scandir(bstack1l1111l1l1l_opy_) as entries:
                for entry in entries:
                    abs_path = os.path.abspath(entry.path)
                    if abs_path in _1l1ll111lll_opy_:
                        self.logger.info(bstack1l1ll_opy_ (u"ࠧࡖࡡࡵࡪࠣࡥࡱࡸࡥࡢࡦࡼࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡼࡿࠥᒕ").format(abs_path))
                        continue
                    if entry.is_file():
                        try:
                            timestamp = datetime.fromtimestamp(entry.stat().st_mtime, tz=timezone.utc).isoformat()
                        except Exception:
                            timestamp = bstack1l1ll_opy_ (u"ࠨࠢᒖ")
                        log_entry = bstack1llll11llll_opy_(
                            kind=bstack1l1ll_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤᒗ"),
                            message=bstack1l1ll_opy_ (u"ࠣࠤᒘ"),
                            level=bstack1l1ll_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨᒙ"),
                            timestamp=timestamp,
                            fileName=entry.name,
                            bstack1l1l1ll1l11_opy_=entry.stat().st_size,
                            bstack1l1lll11l1l_opy_=bstack1l1ll_opy_ (u"ࠥࡑࡆࡔࡕࡂࡎࡢ࡙ࡕࡒࡏࡂࡆࠥᒚ"),
                            bstack1l1l1l1_opy_=os.path.abspath(entry.path),
                            bstack1l1l1ll1lll_opy_=hook.get(TestFramework.bstack1l111ll11l1_opy_)
                        )
                        logs.append(log_entry)
                        _1l1ll111lll_opy_.add(abs_path)
        hook[bstack1l1ll_opy_ (u"ࠦࡱࡵࡧࡴࠤᒛ")] = logs
    def bstack1l1ll1l1l1l_opy_(
        self,
        bstack1l1ll111l1l_opy_: bstack1lll1ll1111_opy_,
        entries: List[bstack1llll11llll_opy_],
    ):
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = os.environ.get(bstack1l1ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤ࡙ࡅࡔࡕࡌࡓࡓࡥࡉࡅࠤᒜ"))
        req.platform_index = TestFramework.bstack1lllll111ll_opy_(bstack1l1ll111l1l_opy_, TestFramework.bstack1ll111l111l_opy_)
        req.execution_context.hash = str(bstack1l1ll111l1l_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1l1ll111l1l_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1l1ll111l1l_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.bstack1lllll111ll_opy_(bstack1l1ll111l1l_opy_, TestFramework.bstack1ll11llll11_opy_)
            log_entry.test_framework_version = TestFramework.bstack1lllll111ll_opy_(bstack1l1ll111l1l_opy_, TestFramework.bstack1l1ll1ll11l_opy_)
            log_entry.uuid = entry.bstack1l1111l111l_opy_
            log_entry.test_framework_state = bstack1l1ll111l1l_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l1ll_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧᒝ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            log_entry.level = bstack1l1ll_opy_ (u"ࠢࠣᒞ")
            if entry.kind == bstack1l1ll_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥᒟ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1l1ll1l11_opy_
                log_entry.file_path = entry.bstack1l1l1l1_opy_
        def bstack1l1ll1111l1_opy_():
            bstack11l1l1111_opy_ = datetime.now()
            try:
                self.bstack1lll1ll111l_opy_.LogCreatedEvent(req)
                bstack1l1ll111l1l_opy_.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠨᒠ"), datetime.now() - bstack11l1l1111_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l1ll_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡻࡾࠤᒡ").format(str(e)))
                traceback.print_exc()
        self.bstack111111l11l_opy_.enqueue(bstack1l1ll1111l1_opy_)
    def __1l111ll1111_opy_(self, instance) -> None:
        bstack1l1ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡎࡲࡥࡩࡹࠠࡤࡷࡶࡸࡴࡳࠠࡵࡣࡪࡷࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡧࡪࡸࡨࡲࠥࡺࡥࡴࡶࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇࡷ࡫ࡡࡵࡧࡶࠤࡦࠦࡤࡪࡥࡷࠤࡨࡵ࡮ࡵࡣ࡬ࡲ࡮ࡴࡧࠡࡶࡨࡷࡹࠦ࡬ࡦࡸࡨࡰࠥࡩࡵࡴࡶࡲࡱࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࡦࠣࡪࡷࡵ࡭ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡹࡸࡺ࡯࡮ࡖࡤ࡫ࡒࡧ࡮ࡢࡩࡨࡶࠥࡧ࡮ࡥࠢࡸࡴࡩࡧࡴࡦࡵࠣࡸ࡭࡫ࠠࡪࡰࡶࡸࡦࡴࡣࡦࠢࡶࡸࡦࡺࡥࠡࡷࡶ࡭ࡳ࡭ࠠࡴࡧࡷࡣࡸࡺࡡࡵࡧࡢࡩࡳࡺࡲࡪࡧࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᒢ")
        bstack1l11l111lll_opy_ = {bstack1l1ll_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱࡤࡳࡥࡵࡣࡧࡥࡹࡧࠢᒣ"): bstack1ll1l1ll11l_opy_.bstack11lllllll1l_opy_()}
        TestFramework.bstack1l11111ll1l_opy_(instance, bstack1l11l111lll_opy_)
    @staticmethod
    def __1l11111llll_opy_(instance, args):
        request, bstack1l111ll1l11_opy_ = args
        bstack1l1111l1111_opy_ = id(bstack1l111ll1l11_opy_)
        bstack1l1111l1lll_opy_ = instance.data[TestFramework.bstack1l11l11l11l_opy_]
        step = next(filter(lambda st: st[bstack1l1ll_opy_ (u"࠭ࡩࡥࠩᒤ")] == bstack1l1111l1111_opy_, bstack1l1111l1lll_opy_[bstack1l1ll_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᒥ")]), None)
        step.update({
            bstack1l1ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᒦ"): datetime.now(tz=timezone.utc)
        })
        index = next((i for i, st in enumerate(bstack1l1111l1lll_opy_[bstack1l1ll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᒧ")]) if st[bstack1l1ll_opy_ (u"ࠪ࡭ࡩ࠭ᒨ")] == step[bstack1l1ll_opy_ (u"ࠫ࡮ࡪࠧᒩ")]), None)
        if index is not None:
            bstack1l1111l1lll_opy_[bstack1l1ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᒪ")][index] = step
        instance.data[TestFramework.bstack1l11l11l11l_opy_] = bstack1l1111l1lll_opy_
    @staticmethod
    def __1l11l111l11_opy_(instance, args):
        bstack1l1ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡭࡫࡮ࠡ࡮ࡨࡲࠥࡧࡲࡨࡵࠣ࡭ࡸࠦ࠲࠭ࠢ࡬ࡸࠥࡹࡩࡨࡰ࡬ࡪ࡮࡫ࡳࠡࡶ࡫ࡩࡷ࡫ࠠࡪࡵࠣࡲࡴࠦࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡢࡴࡪࡷࠥࡧࡲࡦࠢ࠰ࠤࡠࡸࡥࡲࡷࡨࡷࡹ࠲ࠠࡴࡶࡨࡴࡢࠐࠠࠡࠢࠣࠤࠥࠦࠠࡪࡨࠣࡥࡷ࡭ࡳࠡࡣࡵࡩࠥ࠹ࠠࡵࡪࡨࡲࠥࡺࡨࡦࠢ࡯ࡥࡸࡺࠠࡷࡣ࡯ࡹࡪࠦࡩࡴࠢࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᒫ")
        bstack1l111ll1ll1_opy_ = datetime.now(tz=timezone.utc)
        request = args[0]
        bstack1l111ll1l11_opy_ = args[1]
        bstack1l1111l1111_opy_ = id(bstack1l111ll1l11_opy_)
        bstack1l1111l1lll_opy_ = instance.data[TestFramework.bstack1l11l11l11l_opy_]
        step = None
        if bstack1l1111l1111_opy_ is not None and bstack1l1111l1lll_opy_.get(bstack1l1ll_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ᒬ")):
            step = next(filter(lambda st: st[bstack1l1ll_opy_ (u"ࠨ࡫ࡧࠫᒭ")] == bstack1l1111l1111_opy_, bstack1l1111l1lll_opy_[bstack1l1ll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᒮ")]), None)
            step.update({
                bstack1l1ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᒯ"): bstack1l111ll1ll1_opy_,
            })
        if len(args) > 2:
            exception = args[2]
            step.update({
                bstack1l1ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᒰ"): bstack1l1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᒱ"),
                bstack1l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧᒲ"): str(exception)
            })
        else:
            if step is not None:
                step.update({
                    bstack1l1ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᒳ"): bstack1l1ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᒴ"),
                })
        index = next((i for i, st in enumerate(bstack1l1111l1lll_opy_[bstack1l1ll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨᒵ")]) if st[bstack1l1ll_opy_ (u"ࠪ࡭ࡩ࠭ᒶ")] == step[bstack1l1ll_opy_ (u"ࠫ࡮ࡪࠧᒷ")]), None)
        if index is not None:
            bstack1l1111l1lll_opy_[bstack1l1ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫᒸ")][index] = step
        instance.data[TestFramework.bstack1l11l11l11l_opy_] = bstack1l1111l1lll_opy_
    @staticmethod
    def __1l11l111l1l_opy_(node):
        try:
            examples = []
            if hasattr(node, bstack1l1ll_opy_ (u"࠭ࡣࡢ࡮࡯ࡷࡵ࡫ࡣࠨᒹ")):
                examples = list(node.callspec.params[bstack1l1ll_opy_ (u"ࠧࡠࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤ࡫ࡸࡢ࡯ࡳࡰࡪ࠭ᒺ")].values())
            return examples
        except:
            return []
    def bstack1l1lll1l111_opy_(self, instance: bstack1lll1ll1111_opy_, bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_]):
        bstack1l111l1111l_opy_ = (
            PytestBDDFramework.bstack1l1111ll11l_opy_
            if bstack1llllllll11_opy_[1] == bstack1lll1111lll_opy_.PRE
            else PytestBDDFramework.bstack1l111111ll1_opy_
        )
        hook = PytestBDDFramework.bstack1l111lll1l1_opy_(instance, bstack1l111l1111l_opy_)
        entries = hook.get(TestFramework.bstack1l1111ll1ll_opy_, []) if isinstance(hook, dict) else []
        entries.extend(TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1l111l11lll_opy_, []))
        return entries
    def bstack1l1ll11lll1_opy_(self, instance: bstack1lll1ll1111_opy_, bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_]):
        bstack1l111l1111l_opy_ = (
            PytestBDDFramework.bstack1l1111ll11l_opy_
            if bstack1llllllll11_opy_[1] == bstack1lll1111lll_opy_.PRE
            else PytestBDDFramework.bstack1l111111ll1_opy_
        )
        PytestBDDFramework.bstack1l11111ll11_opy_(instance, bstack1l111l1111l_opy_)
        TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1l111l11lll_opy_, []).clear()
    @staticmethod
    def bstack1l111lll1l1_opy_(instance: bstack1lll1ll1111_opy_, bstack1l111l1111l_opy_: str):
        bstack11llllll1l1_opy_ = (
            PytestBDDFramework.bstack11llllll1ll_opy_
            if bstack1l111l1111l_opy_ == PytestBDDFramework.bstack1l111111ll1_opy_
            else PytestBDDFramework.bstack1l111ll1l1l_opy_
        )
        bstack1l111111lll_opy_ = TestFramework.bstack1lllll111ll_opy_(instance, bstack1l111l1111l_opy_, None)
        bstack1l11l11l111_opy_ = TestFramework.bstack1lllll111ll_opy_(instance, bstack11llllll1l1_opy_, None) if bstack1l111111lll_opy_ else None
        return (
            bstack1l11l11l111_opy_[bstack1l111111lll_opy_][-1]
            if isinstance(bstack1l11l11l111_opy_, dict) and len(bstack1l11l11l111_opy_.get(bstack1l111111lll_opy_, [])) > 0
            else None
        )
    @staticmethod
    def bstack1l11111ll11_opy_(instance: bstack1lll1ll1111_opy_, bstack1l111l1111l_opy_: str):
        hook = PytestBDDFramework.bstack1l111lll1l1_opy_(instance, bstack1l111l1111l_opy_)
        if isinstance(hook, dict):
            hook.get(TestFramework.bstack1l1111ll1ll_opy_, []).clear()
    @staticmethod
    def __1l111l11l1l_opy_(instance: bstack1lll1ll1111_opy_, *args):
        if len(args) < 2 or not callable(getattr(args[1], bstack1l1ll_opy_ (u"ࠣࡩࡨࡸࡤࡸࡥࡤࡱࡵࡨࡸࠨᒻ"), None)):
            return
        if os.getenv(bstack1l1ll_opy_ (u"ࠤࡖࡈࡐࡥࡃࡍࡋࡢࡊࡑࡇࡇࡠࡎࡒࡋࡘࠨᒼ"), bstack1l1ll_opy_ (u"ࠥ࠵ࠧᒽ")) != bstack1l1ll_opy_ (u"ࠦ࠶ࠨᒾ"):
            PytestBDDFramework.logger.warning(bstack1l1ll_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵ࡭ࡳ࡭ࠠࡤࡣࡳࡰࡴ࡭ࠢᒿ"))
            return
        bstack1l111ll111l_opy_ = {
            bstack1l1ll_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧᓀ"): (PytestBDDFramework.bstack1l1111ll11l_opy_, PytestBDDFramework.bstack1l111ll1l1l_opy_),
            bstack1l1ll_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤᓁ"): (PytestBDDFramework.bstack1l111111ll1_opy_, PytestBDDFramework.bstack11llllll1ll_opy_),
        }
        for when in (bstack1l1ll_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢᓂ"), bstack1l1ll_opy_ (u"ࠤࡦࡥࡱࡲࠢᓃ"), bstack1l1ll_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧᓄ")):
            bstack11llllllll1_opy_ = args[1].get_records(when)
            if not bstack11llllllll1_opy_:
                continue
            records = [
                bstack1llll11llll_opy_(
                    kind=TestFramework.bstack1l1llll1111_opy_,
                    message=r.message,
                    level=r.levelname if hasattr(r, bstack1l1ll_opy_ (u"ࠦࡱ࡫ࡶࡦ࡮ࡱࡥࡲ࡫ࠢᓅ")) and r.levelname else None,
                    timestamp=(
                        datetime.fromtimestamp(r.created, tz=timezone.utc)
                        if hasattr(r, bstack1l1ll_opy_ (u"ࠧࡩࡲࡦࡣࡷࡩࡩࠨᓆ")) and r.created
                        else None
                    ),
                )
                for r in bstack11llllllll1_opy_
                if isinstance(getattr(r, bstack1l1ll_opy_ (u"ࠨ࡭ࡦࡵࡶࡥ࡬࡫ࠢᓇ"), None), str) and r.message.strip()
            ]
            if not records:
                continue
            bstack1l111l1l1ll_opy_, bstack11llllll1l1_opy_ = bstack1l111ll111l_opy_.get(when, (None, None))
            bstack1l11111l1ll_opy_ = TestFramework.bstack1lllll111ll_opy_(instance, bstack1l111l1l1ll_opy_, None) if bstack1l111l1l1ll_opy_ else None
            bstack1l11l11l111_opy_ = TestFramework.bstack1lllll111ll_opy_(instance, bstack11llllll1l1_opy_, None) if bstack1l11111l1ll_opy_ else None
            if isinstance(bstack1l11l11l111_opy_, dict) and len(bstack1l11l11l111_opy_.get(bstack1l11111l1ll_opy_, [])) > 0:
                hook = bstack1l11l11l111_opy_[bstack1l11111l1ll_opy_][-1]
                if isinstance(hook, dict) and TestFramework.bstack1l1111ll1ll_opy_ in hook:
                    hook[TestFramework.bstack1l1111ll1ll_opy_].extend(records)
                    continue
            logs = TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1l111l11lll_opy_, [])
            logs.extend(records)
    @staticmethod
    def __1l111llll11_opy_(args) -> Dict[str, Any]:
        request, feature, scenario = args
        bstack111ll11l_opy_ = request.node.nodeid
        test_name = PytestBDDFramework.__1l111111111_opy_(request.node, scenario)
        bstack1l111l1l11l_opy_ = feature.filename
        if not bstack111ll11l_opy_ or not test_name or not bstack1l111l1l11l_opy_:
            return None
        code = None
        return {
            TestFramework.bstack1ll11l111l1_opy_: uuid4().__str__(),
            TestFramework.bstack1l111l111ll_opy_: bstack111ll11l_opy_,
            TestFramework.bstack1ll111l11ll_opy_: test_name,
            TestFramework.bstack1l1l1l1l111_opy_: bstack111ll11l_opy_,
            TestFramework.bstack1l1111lll11_opy_: bstack1l111l1l11l_opy_,
            TestFramework.bstack1l111ll11ll_opy_: PytestBDDFramework.__1l11l111111_opy_(feature, scenario),
            TestFramework.bstack11llllll111_opy_: code,
            TestFramework.bstack1l1l111l1ll_opy_: TestFramework.bstack1l11l1111l1_opy_,
            TestFramework.bstack1l11l1ll1ll_opy_: test_name
        }
    @staticmethod
    def __1l111111111_opy_(node, scenario):
        if hasattr(node, bstack1l1ll_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩᓈ")):
            parts = node.nodeid.rsplit(bstack1l1ll_opy_ (u"ࠣ࡝ࠥᓉ"))
            params = parts[-1]
            return bstack1l1ll_opy_ (u"ࠤࡾࢁࠥࡡࡻࡾࠤᓊ").format(scenario.name, params)
        return scenario.name
    @staticmethod
    def __1l11l111111_opy_(feature, scenario) -> List[str]:
        return (list(feature.tags) if hasattr(feature, bstack1l1ll_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᓋ")) else []) + (list(scenario.tags) if hasattr(scenario, bstack1l1ll_opy_ (u"ࠫࡹࡧࡧࡴࠩᓌ")) else [])
    @staticmethod
    def __1l1111l11ll_opy_(location):
        return bstack1l1ll_opy_ (u"ࠧࡀ࠺ࠣᓍ").join(filter(lambda x: isinstance(x, str), location))