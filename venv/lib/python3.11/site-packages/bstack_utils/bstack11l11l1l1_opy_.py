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
import threading
import logging
import bstack_utils.accessibility as bstack111111l1l_opy_
from bstack_utils.helper import bstack11ll1ll11_opy_
logger = logging.getLogger(__name__)
def bstack111l1l1l_opy_(bstack1lllll11_opy_):
  return True if bstack1lllll11_opy_ in threading.current_thread().__dict__.keys() else False
def bstack1l1ll1l1ll_opy_(context, *args):
    tags = getattr(args[0], bstack1l1ll_opy_ (u"ࠧࡵࡣࡪࡷࠬᝨ"), [])
    bstack11l1ll111l_opy_ = bstack111111l1l_opy_.bstack1lllll1111_opy_(tags)
    threading.current_thread().isA11yTest = bstack11l1ll111l_opy_
    try:
      bstack1ll1l1llll_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1l1l_opy_(bstack1l1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧᝩ")) else context.browser
      if bstack1ll1l1llll_opy_ and bstack1ll1l1llll_opy_.session_id and bstack11l1ll111l_opy_ and bstack11ll1ll11_opy_(
              threading.current_thread(), bstack1l1ll_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᝪ"), None):
          threading.current_thread().isA11yTest = bstack111111l1l_opy_.bstack1l1ll1llll_opy_(bstack1ll1l1llll_opy_, bstack11l1ll111l_opy_)
    except Exception as e:
       logger.debug(bstack1l1ll_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡧ࠱࠲ࡻࠣ࡭ࡳࠦࡢࡦࡪࡤࡺࡪࡀࠠࡼࡿࠪᝫ").format(str(e)))
def bstack1l1l11l1l_opy_(bstack1ll1l1llll_opy_):
    if bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨᝬ"), None) and bstack11ll1ll11_opy_(
      threading.current_thread(), bstack1l1ll_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ᝭"), None) and not bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡣࡸࡺ࡯ࡱࠩᝮ"), False):
      threading.current_thread().a11y_stop = True
      bstack111111l1l_opy_.bstack1lll1llll1_opy_(bstack1ll1l1llll_opy_, name=bstack1l1ll_opy_ (u"ࠢࠣᝯ"), path=bstack1l1ll_opy_ (u"ࠣࠤᝰ"))