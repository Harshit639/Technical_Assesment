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
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack11ll11lllll_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11lll111l1l_opy_ as bstack11ll1ll1111_opy_, EVENTS
from bstack_utils.bstack11111lll_opy_ import bstack11111lll_opy_
from bstack_utils.helper import bstack1lllll1l11_opy_, bstack1111ll1l1l_opy_, bstack1ll1ll111l_opy_, bstack11ll1l111ll_opy_, \
  bstack11ll1llllll_opy_, bstack1ll11llll_opy_, get_host_info, bstack11ll1ll1lll_opy_, bstack1ll1l1l1l1_opy_, bstack111l111ll1_opy_, bstack11ll1l1l111_opy_, bstack11lll1111ll_opy_, bstack11ll1ll11_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack1l1111111_opy_ import get_logger
from bstack_utils.bstack11l1l111l_opy_ import bstack1llll11l1l1_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack11l1l111l_opy_ = bstack1llll11l1l1_opy_()
@bstack111l111ll1_opy_(class_method=False)
def _11ll1ll11l1_opy_(driver, bstack11111lll1l_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1l1ll_opy_ (u"ࠫࡴࡹ࡟࡯ࡣࡰࡩࠬᘇ"): caps.get(bstack1l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫᘈ"), None),
        bstack1l1ll_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪᘉ"): bstack11111lll1l_opy_.get(bstack1l1ll_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪᘊ"), None),
        bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡱࡥࡲ࡫ࠧᘋ"): caps.get(bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᘌ"), None),
        bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᘍ"): caps.get(bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᘎ"), None)
    }
  except Exception as error:
    logger.debug(bstack1l1ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡦࡨࡸࡦ࡯࡬ࡴࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࠦ࠺ࠡࠩᘏ") + str(error))
  return response
def on():
    if os.environ.get(bstack1l1ll_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫᘐ"), None) is None or os.environ[bstack1l1ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬᘑ")] == bstack1l1ll_opy_ (u"ࠣࡰࡸࡰࡱࠨᘒ"):
        return False
    return True
def bstack1llllll11_opy_(config):
  return config.get(bstack1l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᘓ"), False) or any([p.get(bstack1l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᘔ"), False) == True for p in config.get(bstack1l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᘕ"), [])])
def bstack1l1ll11l11_opy_(config, bstack1ll1l1111l_opy_):
  try:
    bstack11ll1ll11ll_opy_ = config.get(bstack1l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᘖ"), False)
    if int(bstack1ll1l1111l_opy_) < len(config.get(bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᘗ"), [])) and config[bstack1l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪᘘ")][bstack1ll1l1111l_opy_]:
      bstack11lll111l11_opy_ = config[bstack1l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᘙ")][bstack1ll1l1111l_opy_].get(bstack1l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᘚ"), None)
    else:
      bstack11lll111l11_opy_ = config.get(bstack1l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪᘛ"), None)
    if bstack11lll111l11_opy_ != None:
      bstack11ll1ll11ll_opy_ = bstack11lll111l11_opy_
    bstack11ll1l11lll_opy_ = os.getenv(bstack1l1ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩᘜ")) is not None and len(os.getenv(bstack1l1ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪᘝ"))) > 0 and os.getenv(bstack1l1ll_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫᘞ")) != bstack1l1ll_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬᘟ")
    return bstack11ll1ll11ll_opy_ and bstack11ll1l11lll_opy_
  except Exception as error:
    logger.debug(bstack1l1ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡷࡧࡵ࡭࡫ࡿࡩ࡯ࡩࠣࡸ࡭࡫ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶࠥࡀࠠࠨᘠ") + str(error))
  return False
def bstack1lllll1111_opy_(test_tags):
  bstack1ll1111llll_opy_ = os.getenv(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪᘡ"))
  if bstack1ll1111llll_opy_ is None:
    return True
  bstack1ll1111llll_opy_ = json.loads(bstack1ll1111llll_opy_)
  try:
    include_tags = bstack1ll1111llll_opy_[bstack1l1ll_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᘢ")] if bstack1l1ll_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᘣ") in bstack1ll1111llll_opy_ and isinstance(bstack1ll1111llll_opy_[bstack1l1ll_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᘤ")], list) else []
    exclude_tags = bstack1ll1111llll_opy_[bstack1l1ll_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᘥ")] if bstack1l1ll_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᘦ") in bstack1ll1111llll_opy_ and isinstance(bstack1ll1111llll_opy_[bstack1l1ll_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᘧ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1l1ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡷࡣ࡯࡭ࡩࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡧࡱࡵࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡧ࡫ࡦࡰࡴࡨࠤࡸࡩࡡ࡯ࡰ࡬ࡲ࡬࠴ࠠࡆࡴࡵࡳࡷࠦ࠺ࠡࠤᘨ") + str(error))
  return False
def bstack11ll1l1ll1l_opy_(config, bstack11lll11111l_opy_, bstack11lll11l11l_opy_, bstack11ll1ll1ll1_opy_):
  bstack11ll1llll11_opy_ = bstack11ll1l111ll_opy_(config)
  bstack11ll1lll111_opy_ = bstack11ll1llllll_opy_(config)
  if bstack11ll1llll11_opy_ is None or bstack11ll1lll111_opy_ is None:
    logger.error(bstack1l1ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡸࡵ࡯ࠢࡩࡳࡷࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠼ࠣࡑ࡮ࡹࡳࡪࡰࡪࠤࡦࡻࡴࡩࡧࡱࡸ࡮ࡩࡡࡵ࡫ࡲࡲࠥࡺ࡯࡬ࡧࡱࠫᘩ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬᘪ"), bstack1l1ll_opy_ (u"ࠬࢁࡽࠨᘫ")))
    data = {
        bstack1l1ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᘬ"): config[bstack1l1ll_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᘭ")],
        bstack1l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᘮ"): config.get(bstack1l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᘯ"), os.path.basename(os.getcwd())),
        bstack1l1ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡖ࡬ࡱࡪ࠭ᘰ"): bstack1lllll1l11_opy_(),
        bstack1l1ll_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩᘱ"): config.get(bstack1l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡈࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨᘲ"), bstack1l1ll_opy_ (u"࠭ࠧᘳ")),
        bstack1l1ll_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧᘴ"): {
            bstack1l1ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡒࡦࡳࡥࠨᘵ"): bstack11lll11111l_opy_,
            bstack1l1ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬᘶ"): bstack11lll11l11l_opy_,
            bstack1l1ll_opy_ (u"ࠪࡷࡩࡱࡖࡦࡴࡶ࡭ࡴࡴࠧᘷ"): __version__,
            bstack1l1ll_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭ᘸ"): bstack1l1ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬᘹ"),
            bstack1l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ᘺ"): bstack1l1ll_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩᘻ"),
            bstack1l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨᘼ"): bstack11ll1ll1ll1_opy_
        },
        bstack1l1ll_opy_ (u"ࠩࡶࡩࡹࡺࡩ࡯ࡩࡶࠫᘽ"): settings,
        bstack1l1ll_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࡇࡴࡴࡴࡳࡱ࡯ࠫᘾ"): bstack11ll1ll1lll_opy_(),
        bstack1l1ll_opy_ (u"ࠫࡨ࡯ࡉ࡯ࡨࡲࠫᘿ"): bstack1ll11llll_opy_(),
        bstack1l1ll_opy_ (u"ࠬ࡮࡯ࡴࡶࡌࡲ࡫ࡵࠧᙀ"): get_host_info(),
        bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᙁ"): bstack1ll1ll111l_opy_(config)
    }
    headers = {
        bstack1l1ll_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭ᙂ"): bstack1l1ll_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫᙃ"),
    }
    config = {
        bstack1l1ll_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᙄ"): (bstack11ll1llll11_opy_, bstack11ll1lll111_opy_),
        bstack1l1ll_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫᙅ"): headers
    }
    response = bstack1ll1l1l1l1_opy_(bstack1l1ll_opy_ (u"ࠫࡕࡕࡓࡕࠩᙆ"), bstack11ll1ll1111_opy_ + bstack1l1ll_opy_ (u"ࠬ࠵ࡶ࠳࠱ࡷࡩࡸࡺ࡟ࡳࡷࡱࡷࠬᙇ"), data, config)
    bstack11ll1l11ll1_opy_ = response.json()
    if bstack11ll1l11ll1_opy_[bstack1l1ll_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧᙈ")]:
      parsed = json.loads(os.getenv(bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨᙉ"), bstack1l1ll_opy_ (u"ࠨࡽࢀࠫᙊ")))
      parsed[bstack1l1ll_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᙋ")] = bstack11ll1l11ll1_opy_[bstack1l1ll_opy_ (u"ࠪࡨࡦࡺࡡࠨᙌ")][bstack1l1ll_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᙍ")]
      os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ᙎ")] = json.dumps(parsed)
      bstack11111lll_opy_.bstack1111l1ll1_opy_(bstack11ll1l11ll1_opy_[bstack1l1ll_opy_ (u"࠭ࡤࡢࡶࡤࠫᙏ")][bstack1l1ll_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨᙐ")])
      bstack11111lll_opy_.bstack11ll1ll111l_opy_(bstack11ll1l11ll1_opy_[bstack1l1ll_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᙑ")][bstack1l1ll_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࠫᙒ")])
      bstack11111lll_opy_.store()
      return bstack11ll1l11ll1_opy_[bstack1l1ll_opy_ (u"ࠪࡨࡦࡺࡡࠨᙓ")][bstack1l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡘࡴࡱࡥ࡯ࠩᙔ")], bstack11ll1l11ll1_opy_[bstack1l1ll_opy_ (u"ࠬࡪࡡࡵࡣࠪᙕ")][bstack1l1ll_opy_ (u"࠭ࡩࡥࠩᙖ")]
    else:
      logger.error(bstack1l1ll_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡵࡹࡳࡴࡩ࡯ࡩࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࠨᙗ") + bstack11ll1l11ll1_opy_[bstack1l1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᙘ")])
      if bstack11ll1l11ll1_opy_[bstack1l1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᙙ")] == bstack1l1ll_opy_ (u"ࠪࡍࡳࡼࡡ࡭࡫ࡧࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤࡵࡧࡳࡴࡧࡧ࠲ࠬᙚ"):
        for bstack11ll1l11l1l_opy_ in bstack11ll1l11ll1_opy_[bstack1l1ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫᙛ")]:
          logger.error(bstack11ll1l11l1l_opy_[bstack1l1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᙜ")])
      return None, None
  except Exception as error:
    logger.error(bstack1l1ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡴࡸࡲࠥ࡬࡯ࡳࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠿ࠦࠢᙝ") +  str(error))
    return None, None
def bstack11lll11l111_opy_():
  if os.getenv(bstack1l1ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬᙞ")) is None:
    return {
        bstack1l1ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᙟ"): bstack1l1ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᙠ"),
        bstack1l1ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᙡ"): bstack1l1ll_opy_ (u"ࠫࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲࠥ࡮ࡡࡥࠢࡩࡥ࡮ࡲࡥࡥ࠰ࠪᙢ")
    }
  data = {bstack1l1ll_opy_ (u"ࠬ࡫࡮ࡥࡖ࡬ࡱࡪ࠭ᙣ"): bstack1lllll1l11_opy_()}
  headers = {
      bstack1l1ll_opy_ (u"࠭ࡁࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭ᙤ"): bstack1l1ll_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࠨᙥ") + os.getenv(bstack1l1ll_opy_ (u"ࠣࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙ࠨᙦ")),
      bstack1l1ll_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨᙧ"): bstack1l1ll_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ᙨ")
  }
  response = bstack1ll1l1l1l1_opy_(bstack1l1ll_opy_ (u"ࠫࡕ࡛ࡔࠨᙩ"), bstack11ll1ll1111_opy_ + bstack1l1ll_opy_ (u"ࠬ࠵ࡴࡦࡵࡷࡣࡷࡻ࡮ࡴ࠱ࡶࡸࡴࡶࠧᙪ"), data, { bstack1l1ll_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧᙫ"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1l1ll_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡘࡪࡹࡴࠡࡔࡸࡲࠥࡳࡡࡳ࡭ࡨࡨࠥࡧࡳࠡࡥࡲࡱࡵࡲࡥࡵࡧࡧࠤࡦࡺࠠࠣᙬ") + bstack1111ll1l1l_opy_().isoformat() + bstack1l1ll_opy_ (u"ࠨ࡜ࠪ᙭"))
      return {bstack1l1ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ᙮"): bstack1l1ll_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫᙯ"), bstack1l1ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᙰ"): bstack1l1ll_opy_ (u"ࠬ࠭ᙱ")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1l1ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢࡦࡳࡲࡶ࡬ࡦࡶ࡬ࡳࡳࠦ࡯ࡧࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࡚ࠥࡥࡴࡶࠣࡖࡺࡴ࠺ࠡࠤᙲ") + str(error))
    return {
        bstack1l1ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᙳ"): bstack1l1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᙴ"),
        bstack1l1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᙵ"): str(error)
    }
def bstack11ll1l11111_opy_(bstack11lll1111l1_opy_):
    return re.match(bstack1l1ll_opy_ (u"ࡵࠫࡣࡢࡤࠬࠪ࡟࠲ࡡࡪࠫࠪࡁࠧࠫᙶ"), bstack11lll1111l1_opy_.strip()) is not None
def bstack1ll1llllll_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack11ll1ll1l1l_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack11ll1ll1l1l_opy_ = desired_capabilities
        else:
          bstack11ll1ll1l1l_opy_ = {}
        bstack1ll11l1l1ll_opy_ = (bstack11ll1ll1l1l_opy_.get(bstack1l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪᙷ"), bstack1l1ll_opy_ (u"ࠬ࠭ᙸ")).lower() or caps.get(bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠬᙹ"), bstack1l1ll_opy_ (u"ࠧࠨᙺ")).lower())
        if bstack1ll11l1l1ll_opy_ == bstack1l1ll_opy_ (u"ࠨ࡫ࡲࡷࠬᙻ"):
            return True
        if bstack1ll11l1l1ll_opy_ == bstack1l1ll_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࠪᙼ"):
            bstack1ll11l1llll_opy_ = str(float(caps.get(bstack1l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᙽ")) or bstack11ll1ll1l1l_opy_.get(bstack1l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᙾ"), {}).get(bstack1l1ll_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨᙿ"),bstack1l1ll_opy_ (u"࠭ࠧ "))))
            if bstack1ll11l1l1ll_opy_ == bstack1l1ll_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࠨᚁ") and int(bstack1ll11l1llll_opy_.split(bstack1l1ll_opy_ (u"ࠨ࠰ࠪᚂ"))[0]) < float(bstack11lll111ll1_opy_):
                logger.warning(str(bstack11ll1l1ll11_opy_))
                return False
            return True
        bstack1ll111l11l1_opy_ = caps.get(bstack1l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᚃ"), {}).get(bstack1l1ll_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧᚄ"), caps.get(bstack1l1ll_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫᚅ"), bstack1l1ll_opy_ (u"ࠬ࠭ᚆ")))
        if bstack1ll111l11l1_opy_:
            logger.warning(bstack1l1ll_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡄࡦࡵ࡮ࡸࡴࡶࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥᚇ"))
            return False
        browser = caps.get(bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᚈ"), bstack1l1ll_opy_ (u"ࠨࠩᚉ")).lower() or bstack11ll1ll1l1l_opy_.get(bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᚊ"), bstack1l1ll_opy_ (u"ࠪࠫᚋ")).lower()
        if browser != bstack1l1ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫᚌ"):
            logger.warning(bstack1l1ll_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣᚍ"))
            return False
        browser_version = caps.get(bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᚎ")) or caps.get(bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᚏ")) or bstack11ll1ll1l1l_opy_.get(bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᚐ")) or bstack11ll1ll1l1l_opy_.get(bstack1l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᚑ"), {}).get(bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫᚒ")) or bstack11ll1ll1l1l_opy_.get(bstack1l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᚓ"), {}).get(bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᚔ"))
        bstack1ll11l1ll11_opy_ = bstack11ll11lllll_opy_.bstack1ll11ll1ll1_opy_
        bstack11ll1l1lll1_opy_ = False
        if config is not None:
          bstack11ll1l1lll1_opy_ = bstack1l1ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪᚕ") in config and str(config[bstack1l1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫᚖ")]).lower() != bstack1l1ll_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧᚗ")
        if os.environ.get(bstack1l1ll_opy_ (u"ࠩࡌࡗࡤࡔࡏࡏࡡࡅࡗ࡙ࡇࡃࡌࡡࡌࡒࡋࡘࡁࡠࡃ࠴࠵࡞ࡥࡓࡆࡕࡖࡍࡔࡔࠧᚘ"), bstack1l1ll_opy_ (u"ࠪࠫᚙ")).lower() == bstack1l1ll_opy_ (u"ࠫࡹࡸࡵࡦࠩᚚ") or bstack11ll1l1lll1_opy_:
          bstack1ll11l1ll11_opy_ = bstack11ll11lllll_opy_.bstack1ll1111ll1l_opy_
        if browser_version and browser_version != bstack1l1ll_opy_ (u"ࠬࡲࡡࡵࡧࡶࡸࠬ᚛") and int(browser_version.split(bstack1l1ll_opy_ (u"࠭࠮ࠨ᚜"))[0]) <= bstack1ll11l1ll11_opy_:
          logger.warning(bstack1llll1l1l1l_opy_ (u"ࠧࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡪࡶࡪࡧࡴࡦࡴࠣࡸ࡭ࡧ࡮ࠡࡽࡰ࡭ࡳࡥࡡ࠲࠳ࡼࡣࡸࡻࡰࡱࡱࡵࡸࡪࡪ࡟ࡤࡪࡵࡳࡲ࡫࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࡾ࠰ࠪ᚝"))
          return False
        if not options:
          bstack1ll111l1ll1_opy_ = caps.get(bstack1l1ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭᚞")) or bstack11ll1ll1l1l_opy_.get(bstack1l1ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ᚟"), {})
          if bstack1l1ll_opy_ (u"ࠪ࠱࠲࡮ࡥࡢࡦ࡯ࡩࡸࡹࠧᚠ") in bstack1ll111l1ll1_opy_.get(bstack1l1ll_opy_ (u"ࠫࡦࡸࡧࡴࠩᚡ"), []):
              logger.warning(bstack1l1ll_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠ࡯ࡱࡷࠤࡷࡻ࡮ࠡࡱࡱࠤࡱ࡫ࡧࡢࡥࡼࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲࡙ࠥࡷࡪࡶࡦ࡬ࠥࡺ࡯ࠡࡰࡨࡻࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩࠥࡵࡲࠡࡣࡹࡳ࡮ࡪࠠࡶࡵ࡬ࡲ࡬ࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠢᚢ"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack1l1ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡼࡡ࡭࡫ࡧࡥࡹ࡫ࠠࡢ࠳࠴ࡽࠥࡹࡵࡱࡲࡲࡶࡹࠦ࠺ࠣᚣ") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1llll11l11l_opy_ = config.get(bstack1l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᚤ"), {})
    bstack1llll11l11l_opy_[bstack1l1ll_opy_ (u"ࠨࡣࡸࡸ࡭࡚࡯࡬ࡧࡱࠫᚥ")] = os.getenv(bstack1l1ll_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧᚦ"))
    bstack11lll111111_opy_ = json.loads(os.getenv(bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫᚧ"), bstack1l1ll_opy_ (u"ࠫࢀࢃࠧᚨ"))).get(bstack1l1ll_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ᚩ"))
    if not config[bstack1l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨᚪ")].get(bstack1l1ll_opy_ (u"ࠢࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪࠨᚫ")):
      if bstack1l1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᚬ") in caps:
        caps[bstack1l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᚭ")][bstack1l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᚮ")] = bstack1llll11l11l_opy_
        caps[bstack1l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᚯ")][bstack1l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬᚰ")][bstack1l1ll_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᚱ")] = bstack11lll111111_opy_
      else:
        caps[bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᚲ")] = bstack1llll11l11l_opy_
        caps[bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᚳ")][bstack1l1ll_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪᚴ")] = bstack11lll111111_opy_
  except Exception as error:
    logger.debug(bstack1l1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ࠰ࠣࡉࡷࡸ࡯ࡳ࠼ࠣࠦᚵ") +  str(error))
def bstack1l1ll1llll_opy_(driver, bstack11ll1l111l1_opy_):
  try:
    setattr(driver, bstack1l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫᚶ"), True)
    session = driver.session_id
    if session:
      bstack11ll1l1l11l_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack11ll1l1l11l_opy_ = False
      bstack11ll1l1l11l_opy_ = url.scheme in [bstack1l1ll_opy_ (u"ࠧ࡮ࡴࡵࡲࠥᚷ"), bstack1l1ll_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧᚸ")]
      if bstack11ll1l1l11l_opy_:
        if bstack11ll1l111l1_opy_:
          logger.info(bstack1l1ll_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡦࡰࡴࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡭ࡧࡳࠡࡵࡷࡥࡷࡺࡥࡥ࠰ࠣࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡥࡩ࡬࡯࡮ࠡ࡯ࡲࡱࡪࡴࡴࡢࡴ࡬ࡰࡾ࠴ࠢᚹ"))
      return bstack11ll1l111l1_opy_
  except Exception as e:
    logger.error(bstack1l1ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡶࡤࡶࡹ࡯࡮ࡨࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡤࡣࡱࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦ࠼ࠣࠦᚺ") + str(e))
    return False
def bstack1lll1llll1_opy_(driver, name, path):
  try:
    bstack1ll11ll11l1_opy_ = {
        bstack1l1ll_opy_ (u"ࠩࡷ࡬࡙࡫ࡳࡵࡔࡸࡲ࡚ࡻࡩࡥࠩᚻ"): threading.current_thread().current_test_uuid,
        bstack1l1ll_opy_ (u"ࠪࡸ࡭ࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨᚼ"): os.environ.get(bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᚽ"), bstack1l1ll_opy_ (u"ࠬ࠭ᚾ")),
        bstack1l1ll_opy_ (u"࠭ࡴࡩࡌࡺࡸ࡙ࡵ࡫ࡦࡰࠪᚿ"): os.environ.get(bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫᛀ"), bstack1l1ll_opy_ (u"ࠨࠩᛁ"))
    }
    bstack1ll1l11l11l_opy_ = bstack11l1l111l_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack111ll1ll_opy_.value)
    logger.debug(bstack1l1ll_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤࡸࡧࡶࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠬᛂ"))
    try:
      if (bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪᛃ"), None) and bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ᛄ"), None)):
        scripts = {bstack1l1ll_opy_ (u"ࠬࡹࡣࡢࡰࠪᛅ"): bstack11111lll_opy_.perform_scan}
        bstack11ll1l1l1l1_opy_ = json.loads(scripts[bstack1l1ll_opy_ (u"ࠨࡳࡤࡣࡱࠦᛆ")].replace(bstack1l1ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࠥᛇ"), bstack1l1ll_opy_ (u"ࠣࠤᛈ")))
        bstack11ll1l1l1l1_opy_[bstack1l1ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᛉ")][bstack1l1ll_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪᛊ")] = None
        scripts[bstack1l1ll_opy_ (u"ࠦࡸࡩࡡ࡯ࠤᛋ")] = bstack1l1ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣᛌ") + json.dumps(bstack11ll1l1l1l1_opy_)
        bstack11111lll_opy_.bstack1111l1ll1_opy_(scripts)
        bstack11111lll_opy_.store()
        logger.debug(driver.execute_script(bstack11111lll_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11111lll_opy_.perform_scan, {bstack1l1ll_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࠨᛍ"): name}))
      bstack11l1l111l_opy_.end(EVENTS.bstack111ll1ll_opy_.value, bstack1ll1l11l11l_opy_ + bstack1l1ll_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᛎ"), bstack1ll1l11l11l_opy_ + bstack1l1ll_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᛏ"), True, None)
    except Exception as error:
      bstack11l1l111l_opy_.end(EVENTS.bstack111ll1ll_opy_.value, bstack1ll1l11l11l_opy_ + bstack1l1ll_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᛐ"), bstack1ll1l11l11l_opy_ + bstack1l1ll_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᛑ"), False, str(error))
    bstack1ll1l11l11l_opy_ = bstack11l1l111l_opy_.bstack11ll1l11l11_opy_(EVENTS.bstack1ll111lll1l_opy_.value)
    bstack11l1l111l_opy_.mark(bstack1ll1l11l11l_opy_ + bstack1l1ll_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᛒ"))
    try:
      if (bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬᛓ"), None) and bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᛔ"), None)):
        scripts = {bstack1l1ll_opy_ (u"ࠧࡴࡥࡤࡲࠬᛕ"): bstack11111lll_opy_.perform_scan}
        bstack11ll1l1l1l1_opy_ = json.loads(scripts[bstack1l1ll_opy_ (u"ࠣࡵࡦࡥࡳࠨᛖ")].replace(bstack1l1ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࠧᛗ"), bstack1l1ll_opy_ (u"ࠥࠦᛘ")))
        bstack11ll1l1l1l1_opy_[bstack1l1ll_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᛙ")][bstack1l1ll_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࠬᛚ")] = None
        scripts[bstack1l1ll_opy_ (u"ࠨࡳࡤࡣࡱࠦᛛ")] = bstack1l1ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࠥᛜ") + json.dumps(bstack11ll1l1l1l1_opy_)
        bstack11111lll_opy_.bstack1111l1ll1_opy_(scripts)
        bstack11111lll_opy_.store()
        logger.debug(driver.execute_script(bstack11111lll_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11111lll_opy_.bstack11ll1lllll1_opy_, bstack1ll11ll11l1_opy_))
      bstack11l1l111l_opy_.end(bstack1ll1l11l11l_opy_, bstack1ll1l11l11l_opy_ + bstack1l1ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᛝ"), bstack1ll1l11l11l_opy_ + bstack1l1ll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᛞ"),True, None)
    except Exception as error:
      bstack11l1l111l_opy_.end(bstack1ll1l11l11l_opy_, bstack1ll1l11l11l_opy_ + bstack1l1ll_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᛟ"), bstack1ll1l11l11l_opy_ + bstack1l1ll_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᛠ"),False, str(error))
    logger.info(bstack1l1ll_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡸ࡭࡯ࡳࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠣᛡ"))
  except Exception as bstack1ll111ll1l1_opy_:
    logger.error(bstack1l1ll_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡤࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡦࡪࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡩࡳࡷࠦࡴࡩࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࡀࠠࠣᛢ") + str(path) + bstack1l1ll_opy_ (u"ࠢࠡࡇࡵࡶࡴࡸࠠ࠻ࠤᛣ") + str(bstack1ll111ll1l1_opy_))
def bstack11ll1llll1l_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack1l1ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢᛤ")) and str(caps.get(bstack1l1ll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣᛥ"))).lower() == bstack1l1ll_opy_ (u"ࠥࡥࡳࡪࡲࡰ࡫ࡧࠦᛦ"):
        bstack1ll11l1llll_opy_ = caps.get(bstack1l1ll_opy_ (u"ࠦࡦࡶࡰࡪࡷࡰ࠾ࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨᛧ")) or caps.get(bstack1l1ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢᛨ"))
        if bstack1ll11l1llll_opy_ and int(str(bstack1ll11l1llll_opy_)) < bstack11lll111ll1_opy_:
            return False
    return True
def bstack1ll1ll111_opy_(config):
  if bstack1l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ᛩ") in config:
        return config[bstack1l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧᛪ")]
  for platform in config.get(bstack1l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ᛫"), []):
      if bstack1l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ᛬") in platform:
          return platform[bstack1l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ᛭")]
  return None
def bstack11l111111l_opy_(bstack11l1lllll1_opy_):
  try:
    browser_name = bstack11l1lllll1_opy_[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡴࡡ࡮ࡧࠪᛮ")]
    browser_version = bstack11l1lllll1_opy_[bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᛯ")]
    chrome_options = bstack11l1lllll1_opy_[bstack1l1ll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡥ࡯ࡱࡶ࡬ࡳࡳࡹࠧᛰ")]
    try:
        bstack11ll1lll1l1_opy_ = int(browser_version.split(bstack1l1ll_opy_ (u"ࠧ࠯ࠩᛱ"))[0])
    except ValueError as e:
        logger.error(bstack1l1ll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡣࡰࡰࡹࡩࡷࡺࡩ࡯ࡩࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠧᛲ") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack1l1ll_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩᛳ")):
        logger.warning(bstack1l1ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨᛴ"))
        return False
    if bstack11ll1lll1l1_opy_ < bstack11ll11lllll_opy_.bstack1ll1111ll1l_opy_:
        logger.warning(bstack1llll1l1l1l_opy_ (u"ࠫࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡴࡨࡵࡺ࡯ࡲࡦࡵࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡺࡪࡸࡳࡪࡱࡱࠤࢀࡉࡏࡏࡕࡗࡅࡓ࡚ࡓ࠯ࡏࡌࡒࡎࡓࡕࡎࡡࡑࡓࡓࡥࡂࡔࡖࡄࡇࡐࡥࡉࡏࡈࡕࡅࡤࡇ࠱࠲࡛ࡢࡗ࡚ࡖࡐࡐࡔࡗࡉࡉࡥࡃࡉࡔࡒࡑࡊࡥࡖࡆࡔࡖࡍࡔࡔࡽࠡࡱࡵࠤ࡭࡯ࡧࡩࡧࡵ࠲ࠬᛵ"))
        return False
    if chrome_options and any(bstack1l1ll_opy_ (u"ࠬ࠳࠭ࡩࡧࡤࡨࡱ࡫ࡳࡴࠩᛶ") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack1l1ll_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡰࡲࡸࠥࡸࡵ࡯ࠢࡲࡲࠥࡲࡥࡨࡣࡦࡽࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠦࡓࡸ࡫ࡷࡧ࡭ࠦࡴࡰࠢࡱࡩࡼࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪࠦ࡯ࡳࠢࡤࡺࡴ࡯ࡤࠡࡷࡶ࡭ࡳ࡭ࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠣᛷ"))
        return False
    return True
  except Exception as e:
    logger.error(bstack1l1ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡦ࡬ࡪࡩ࡫ࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡳࡶࡲࡳࡳࡷࡺࠠࡧࡱࡵࠤࡱࡵࡣࡢ࡮ࠣࡇ࡭ࡸ࡯࡮ࡧ࠽ࠤࠧᛸ") + str(e))
    return False
def bstack1l1l11l1ll_opy_(bstack11111lll1_opy_, config):
    try:
      bstack1ll1l11111l_opy_ = bstack1l1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ᛹") in config and config[bstack1l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ᛺")] == True
      bstack11ll1l1lll1_opy_ = bstack1l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ᛻") in config and str(config[bstack1l1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ᛼")]).lower() != bstack1l1ll_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ᛽")
      if not (bstack1ll1l11111l_opy_ and (not bstack1ll1ll111l_opy_(config) or bstack11ll1l1lll1_opy_)):
        return bstack11111lll1_opy_
      bstack11ll1l1l1ll_opy_ = bstack11111lll_opy_.bstack11ll1lll1ll_opy_
      if bstack11ll1l1l1ll_opy_ is None:
        logger.debug(bstack1l1ll_opy_ (u"ࠨࡇࡰࡱࡪࡰࡪࠦࡣࡩࡴࡲࡱࡪࠦ࡯ࡱࡶ࡬ࡳࡳࡹࠠࡢࡴࡨࠤࡓࡵ࡮ࡦࠤ᛾"))
        return bstack11111lll1_opy_
      bstack11ll1lll11l_opy_ = int(str(bstack11lll1111ll_opy_()).split(bstack1l1ll_opy_ (u"ࠧ࠯ࠩ᛿"))[0])
      logger.debug(bstack1l1ll_opy_ (u"ࠣࡕࡨࡰࡪࡴࡩࡶ࡯ࠣࡺࡪࡸࡳࡪࡱࡱࠤࡩ࡫ࡴࡦࡥࡷࡩࡩࡀࠠࠣᜀ") + str(bstack11ll1lll11l_opy_) + bstack1l1ll_opy_ (u"ࠤࠥᜁ"))
      if bstack11ll1lll11l_opy_ == 3 and isinstance(bstack11111lll1_opy_, dict) and bstack1l1ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪᜂ") in bstack11111lll1_opy_ and bstack11ll1l1l1ll_opy_ is not None:
        if bstack1l1ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᜃ") not in bstack11111lll1_opy_[bstack1l1ll_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬᜄ")]:
          bstack11111lll1_opy_[bstack1l1ll_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ᜅ")][bstack1l1ll_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬᜆ")] = {}
        if bstack1l1ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ᜇ") in bstack11ll1l1l1ll_opy_:
          if bstack1l1ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧᜈ") not in bstack11111lll1_opy_[bstack1l1ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪᜉ")][bstack1l1ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᜊ")]:
            bstack11111lll1_opy_[bstack1l1ll_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬᜋ")][bstack1l1ll_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᜌ")][bstack1l1ll_opy_ (u"ࠧࡢࡴࡪࡷࠬᜍ")] = []
          for arg in bstack11ll1l1l1ll_opy_[bstack1l1ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ᜎ")]:
            if arg not in bstack11111lll1_opy_[bstack1l1ll_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩᜏ")][bstack1l1ll_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᜐ")][bstack1l1ll_opy_ (u"ࠫࡦࡸࡧࡴࠩᜑ")]:
              bstack11111lll1_opy_[bstack1l1ll_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬᜒ")][bstack1l1ll_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᜓ")][bstack1l1ll_opy_ (u"ࠧࡢࡴࡪࡷ᜔ࠬ")].append(arg)
        if bstack1l1ll_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷ᜕ࠬ") in bstack11ll1l1l1ll_opy_:
          if bstack1l1ll_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭᜖") not in bstack11111lll1_opy_[bstack1l1ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ᜗")][bstack1l1ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᜘")]:
            bstack11111lll1_opy_[bstack1l1ll_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ᜙")][bstack1l1ll_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ᜚")][bstack1l1ll_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ᜛")] = []
          for ext in bstack11ll1l1l1ll_opy_[bstack1l1ll_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ᜜")]:
            if ext not in bstack11111lll1_opy_[bstack1l1ll_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ᜝")][bstack1l1ll_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ᜞")][bstack1l1ll_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨᜟ")]:
              bstack11111lll1_opy_[bstack1l1ll_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬᜠ")][bstack1l1ll_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᜡ")][bstack1l1ll_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫᜢ")].append(ext)
        if bstack1l1ll_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧᜣ") in bstack11ll1l1l1ll_opy_:
          if bstack1l1ll_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨᜤ") not in bstack11111lll1_opy_[bstack1l1ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪᜥ")][bstack1l1ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩᜦ")]:
            bstack11111lll1_opy_[bstack1l1ll_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬᜧ")][bstack1l1ll_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫᜨ")][bstack1l1ll_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ᜩ")] = {}
          bstack11ll1l1l111_opy_(bstack11111lll1_opy_[bstack1l1ll_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨᜪ")][bstack1l1ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᜫ")][bstack1l1ll_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩᜬ")],
                    bstack11ll1l1l1ll_opy_[bstack1l1ll_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪᜭ")])
        os.environ[bstack1l1ll_opy_ (u"ࠬࡏࡓࡠࡐࡒࡒࡤࡈࡓࡕࡃࡆࡏࡤࡏࡎࡇࡔࡄࡣࡆ࠷࠱࡚ࡡࡖࡉࡘ࡙ࡉࡐࡐࠪᜮ")] = bstack1l1ll_opy_ (u"࠭ࡴࡳࡷࡨࠫᜯ")
        return bstack11111lll1_opy_
      else:
        chrome_options = None
        if isinstance(bstack11111lll1_opy_, ChromeOptions):
          chrome_options = bstack11111lll1_opy_
        elif isinstance(bstack11111lll1_opy_, dict):
          for value in bstack11111lll1_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack11111lll1_opy_, dict):
            bstack11111lll1_opy_[bstack1l1ll_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨᜰ")] = chrome_options
          else:
            bstack11111lll1_opy_ = chrome_options
        if bstack11ll1l1l1ll_opy_ is not None:
          if bstack1l1ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ᜱ") in bstack11ll1l1l1ll_opy_:
                bstack11ll1ll1l11_opy_ = chrome_options.arguments or []
                new_args = bstack11ll1l1l1ll_opy_[bstack1l1ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧᜲ")]
                for arg in new_args:
                    if arg not in bstack11ll1ll1l11_opy_:
                        chrome_options.add_argument(arg)
          if bstack1l1ll_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧᜳ") in bstack11ll1l1l1ll_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack1l1ll_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ᜴"), [])
                bstack11lll111lll_opy_ = bstack11ll1l1l1ll_opy_[bstack1l1ll_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ᜵")]
                for extension in bstack11lll111lll_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack1l1ll_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ᜶") in bstack11ll1l1l1ll_opy_:
                bstack11ll1l1111l_opy_ = chrome_options.experimental_options.get(bstack1l1ll_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭᜷"), {})
                bstack11ll1l1llll_opy_ = bstack11ll1l1l1ll_opy_[bstack1l1ll_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ᜸")]
                bstack11ll1l1l111_opy_(bstack11ll1l1111l_opy_, bstack11ll1l1llll_opy_)
                chrome_options.add_experimental_option(bstack1l1ll_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ᜹"), bstack11ll1l1111l_opy_)
        os.environ[bstack1l1ll_opy_ (u"ࠪࡍࡘࡥࡎࡐࡐࡢࡆࡘ࡚ࡁࡄࡍࡢࡍࡓࡌࡒࡂࡡࡄ࠵࠶࡟࡟ࡔࡇࡖࡗࡎࡕࡎࠨ᜺")] = bstack1l1ll_opy_ (u"ࠫࡹࡸࡵࡦࠩ᜻")
        return bstack11111lll1_opy_
    except Exception as e:
      logger.error(bstack1l1ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡥࡩࡪࡩ࡯ࡩࠣࡲࡴࡴ࠭ࡃࡕࠣ࡭ࡳ࡬ࡲࡢࠢࡤ࠵࠶ࡿࠠࡤࡪࡵࡳࡲ࡫ࠠࡰࡲࡷ࡭ࡴࡴࡳ࠻ࠢࠥ᜼") + str(e))
      return bstack11111lll1_opy_