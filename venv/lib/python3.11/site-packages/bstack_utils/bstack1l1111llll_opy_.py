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
import logging
import datetime
import threading
from bstack_utils.helper import bstack11ll1ll1lll_opy_, bstack1ll11llll_opy_, get_host_info, bstack11l11l1l1ll_opy_, \
 bstack1ll1ll111l_opy_, bstack11ll1ll11_opy_, bstack111l111ll1_opy_, bstack11l11l11ll1_opy_, bstack1lllll1l11_opy_
import bstack_utils.accessibility as bstack111111l1l_opy_
from bstack_utils.bstack111llll111_opy_ import bstack11ll1llll1_opy_
from bstack_utils.percy import bstack1lll1l11_opy_
from bstack_utils.config import Config
bstack11l1lll1_opy_ = Config.bstack11ll11ll1_opy_()
logger = logging.getLogger(__name__)
percy = bstack1lll1l11_opy_()
@bstack111l111ll1_opy_(class_method=False)
def bstack1lllll1lll11_opy_(bs_config, bstack11lll11lll_opy_):
  try:
    data = {
        bstack1l1ll_opy_ (u"࠭ࡦࡰࡴࡰࡥࡹ࠭ℇ"): bstack1l1ll_opy_ (u"ࠧ࡫ࡵࡲࡲࠬ℈"),
        bstack1l1ll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡡࡱࡥࡲ࡫ࠧ℉"): bs_config.get(bstack1l1ll_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧℊ"), bstack1l1ll_opy_ (u"ࠪࠫℋ")),
        bstack1l1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩℌ"): bs_config.get(bstack1l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨℍ"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack1l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩℎ"): bs_config.get(bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩℏ")),
        bstack1l1ll_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ℐ"): bs_config.get(bstack1l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬℑ"), bstack1l1ll_opy_ (u"ࠪࠫℒ")),
        bstack1l1ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨℓ"): bstack1lllll1l11_opy_(),
        bstack1l1ll_opy_ (u"ࠬࡺࡡࡨࡵࠪ℔"): bstack11l11l1l1ll_opy_(bs_config),
        bstack1l1ll_opy_ (u"࠭ࡨࡰࡵࡷࡣ࡮ࡴࡦࡰࠩℕ"): get_host_info(),
        bstack1l1ll_opy_ (u"ࠧࡤ࡫ࡢ࡭ࡳ࡬࡯ࠨ№"): bstack1ll11llll_opy_(),
        bstack1l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡳࡷࡱࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ℗"): os.environ.get(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨ℘")),
        bstack1l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࡡࡵࡩࡷࡻ࡮ࠨℙ"): os.environ.get(bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠩℚ"), False),
        bstack1l1ll_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡥࡣࡰࡰࡷࡶࡴࡲࠧℛ"): bstack11ll1ll1lll_opy_(),
        bstack1l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ℜ"): bstack1llll1llllll_opy_(bs_config),
        bstack1l1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡨࡪࡺࡡࡪ࡮ࡶࠫℝ"): bstack1lllll11l111_opy_(bstack11lll11lll_opy_),
        bstack1l1ll_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭℞"): bstack1lllll111111_opy_(bs_config, bstack11lll11lll_opy_.get(bstack1l1ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪ℟"), bstack1l1ll_opy_ (u"ࠪࠫ℠"))),
        bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭℡"): bstack1ll1ll111l_opy_(bs_config),
    }
    return data
  except Exception as error:
    logger.error(bstack1l1ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡥࡾࡲ࡯ࡢࡦࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࠣࡿࢂࠨ™").format(str(error)))
    return None
def bstack1lllll11l111_opy_(framework):
  return {
    bstack1l1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭℣"): framework.get(bstack1l1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠨℤ"), bstack1l1ll_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ℥")),
    bstack1l1ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬΩ"): framework.get(bstack1l1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ℧")),
    bstack1l1ll_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨℨ"): framework.get(bstack1l1ll_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ℩")),
    bstack1l1ll_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨK"): bstack1l1ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧÅ"),
    bstack1l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨℬ"): framework.get(bstack1l1ll_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩℭ"))
  }
def bstack11l11l1l1l_opy_(bs_config, framework):
  bstack1l1l11l1_opy_ = False
  bstack1l111l1lll_opy_ = False
  bstack1lllll1111ll_opy_ = False
  if bstack1l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ℮") in bs_config:
    bstack1lllll1111ll_opy_ = True
  elif bstack1l1ll_opy_ (u"ࠫࡦࡶࡰࠨℯ") in bs_config:
    bstack1l1l11l1_opy_ = True
  else:
    bstack1l111l1lll_opy_ = True
  bstack11l1ll11l_opy_ = {
    bstack1l1ll_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬℰ"): bstack11ll1llll1_opy_.bstack1lllll11111l_opy_(bs_config, framework),
    bstack1l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ℱ"): bstack111111l1l_opy_.bstack1llllll11_opy_(bs_config),
    bstack1l1ll_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭Ⅎ"): bs_config.get(bstack1l1ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧℳ"), False),
    bstack1l1ll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫℴ"): bstack1l111l1lll_opy_,
    bstack1l1ll_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩℵ"): bstack1l1l11l1_opy_,
    bstack1l1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨℶ"): bstack1lllll1111ll_opy_
  }
  return bstack11l1ll11l_opy_
@bstack111l111ll1_opy_(class_method=False)
def bstack1llll1llllll_opy_(bs_config):
  try:
    bstack1llll1llll11_opy_ = json.loads(os.getenv(bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ℷ"), bstack1l1ll_opy_ (u"࠭ࡻࡾࠩℸ")))
    bstack1llll1llll11_opy_ = bstack1lllll111l11_opy_(bs_config, bstack1llll1llll11_opy_)
    return {
        bstack1l1ll_opy_ (u"ࠧࡴࡧࡷࡸ࡮ࡴࡧࡴࠩℹ"): bstack1llll1llll11_opy_
    }
  except Exception as error:
    logger.error(bstack1l1ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥ࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡶࡩࡹࡺࡩ࡯ࡩࡶࠤ࡫ࡵࡲࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࠤࢀࢃࠢ℺").format(str(error)))
    return {}
def bstack1lllll111l11_opy_(bs_config, bstack1llll1llll11_opy_):
  if ((bstack1l1ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭℻") in bs_config or not bstack1ll1ll111l_opy_(bs_config)) and bstack111111l1l_opy_.bstack1llllll11_opy_(bs_config)):
    bstack1llll1llll11_opy_[bstack1l1ll_opy_ (u"ࠥ࡭ࡳࡩ࡬ࡶࡦࡨࡉࡳࡩ࡯ࡥࡧࡧࡉࡽࡺࡥ࡯ࡵ࡬ࡳࡳࠨℼ")] = True
  return bstack1llll1llll11_opy_
def bstack1llllll111ll_opy_(array, bstack1llll1lllll1_opy_, bstack1lllll1111l1_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll1lllll1_opy_]
    result[key] = o[bstack1lllll1111l1_opy_]
  return result
def bstack1lllll11lll1_opy_(bstack1llll11lll_opy_=bstack1l1ll_opy_ (u"ࠫࠬℽ")):
  bstack1llll1llll1l_opy_ = bstack111111l1l_opy_.on()
  bstack1lllll111l1l_opy_ = bstack11ll1llll1_opy_.on()
  bstack1lllll111lll_opy_ = percy.bstack1111ll1ll_opy_()
  if bstack1lllll111lll_opy_ and not bstack1lllll111l1l_opy_ and not bstack1llll1llll1l_opy_:
    return bstack1llll11lll_opy_ not in [bstack1l1ll_opy_ (u"ࠬࡉࡂࡕࡕࡨࡷࡸ࡯࡯࡯ࡅࡵࡩࡦࡺࡥࡥࠩℾ"), bstack1l1ll_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪℿ")]
  elif bstack1llll1llll1l_opy_ and not bstack1lllll111l1l_opy_:
    return bstack1llll11lll_opy_ not in [bstack1l1ll_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ⅀"), bstack1l1ll_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⅁"), bstack1l1ll_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭⅂")]
  return bstack1llll1llll1l_opy_ or bstack1lllll111l1l_opy_ or bstack1lllll111lll_opy_
@bstack111l111ll1_opy_(class_method=False)
def bstack1llllll111l1_opy_(bstack1llll11lll_opy_, test=None):
  bstack1lllll111ll1_opy_ = bstack111111l1l_opy_.on()
  if not bstack1lllll111ll1_opy_ or bstack1llll11lll_opy_ not in [bstack1l1ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ⅃")] or test == None:
    return None
  return {
    bstack1l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⅄"): bstack1lllll111ll1_opy_ and bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫⅅ"), None) == True and bstack111111l1l_opy_.bstack1lllll1111_opy_(test[bstack1l1ll_opy_ (u"࠭ࡴࡢࡩࡶࠫⅆ")])
  }
def bstack1lllll111111_opy_(bs_config, framework):
  bstack1l1l11l1_opy_ = False
  bstack1l111l1lll_opy_ = False
  bstack1lllll1111ll_opy_ = False
  if bstack1l1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫⅇ") in bs_config:
    bstack1lllll1111ll_opy_ = True
  elif bstack1l1ll_opy_ (u"ࠨࡣࡳࡴࠬⅈ") in bs_config:
    bstack1l1l11l1_opy_ = True
  else:
    bstack1l111l1lll_opy_ = True
  bstack11l1ll11l_opy_ = {
    bstack1l1ll_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩⅉ"): bstack11ll1llll1_opy_.bstack1lllll11111l_opy_(bs_config, framework),
    bstack1l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⅊"): bstack111111l1l_opy_.bstack1ll1ll111_opy_(bs_config),
    bstack1l1ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ⅋"): bs_config.get(bstack1l1ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ⅌"), False),
    bstack1l1ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ⅍"): bstack1l111l1lll_opy_,
    bstack1l1ll_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ⅎ"): bstack1l1l11l1_opy_,
    bstack1l1ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬ⅏"): bstack1lllll1111ll_opy_
  }
  return bstack11l1ll11l_opy_