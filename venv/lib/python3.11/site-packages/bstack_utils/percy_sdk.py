import os
from percy import percy_screenshot
from bstack_utils.constants import STAGE, EVENTS
from bstack_utils.measure import measure
class PercySDK:
  @classmethod
  def screenshot(cls,driver, name, **kwargs):
    percy_screenshot(driver, name, **kwargs)
