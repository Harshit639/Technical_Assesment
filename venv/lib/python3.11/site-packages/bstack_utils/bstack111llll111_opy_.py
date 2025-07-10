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
import threading
from bstack_utils.helper import bstack1ll1l11l_opy_
from bstack_utils.constants import bstack11l1ll11l11_opy_, EVENTS, STAGE
from bstack_utils.bstack1l1111111_opy_ import get_logger
logger = get_logger(__name__)
class bstack11ll1llll1_opy_:
    bstack111111l1ll1_opy_ = None
    @classmethod
    def bstack1l111ll1l_opy_(cls):
        if cls.on() and os.getenv(bstack1l1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠢ⅐")):
            logger.info(
                bstack1l1ll_opy_ (u"࡚ࠪ࡮ࡹࡩࡵࠢ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾࠢࡷࡳࠥࡼࡩࡦࡹࠣࡦࡺ࡯࡬ࡥࠢࡵࡩࡵࡵࡲࡵ࠮ࠣ࡭ࡳࡹࡩࡨࡪࡷࡷ࠱ࠦࡡ࡯ࡦࠣࡱࡦࡴࡹࠡ࡯ࡲࡶࡪࠦࡤࡦࡤࡸ࡫࡬࡯࡮ࡨࠢ࡬ࡲ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴࠠࡢ࡮࡯ࠤࡦࡺࠠࡰࡰࡨࠤࡵࡲࡡࡤࡧࠤࡠࡳ࠭⅑").format(os.getenv(bstack1l1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤ⅒"))))
    @classmethod
    def on(cls):
        if os.environ.get(bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ⅓"), None) is None or os.environ[bstack1l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪ⅔")] == bstack1l1ll_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ⅕"):
            return False
        return True
    @classmethod
    def bstack1lllll11111l_opy_(cls, bs_config, framework=bstack1l1ll_opy_ (u"ࠣࠤ⅖")):
        bstack11ll1111ll1_opy_ = False
        for fw in bstack11l1ll11l11_opy_:
            if fw in framework:
                bstack11ll1111ll1_opy_ = True
        return bstack1ll1l11l_opy_(bs_config.get(bstack1l1ll_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭⅗"), bstack11ll1111ll1_opy_))
    @classmethod
    def bstack1llll1ll1lll_opy_(cls, framework):
        return framework in bstack11l1ll11l11_opy_
    @classmethod
    def bstack1lllll1ll11l_opy_(cls, bs_config, framework):
        return cls.bstack1lllll11111l_opy_(bs_config, framework) is True and cls.bstack1llll1ll1lll_opy_(framework)
    @staticmethod
    def current_hook_uuid():
        return getattr(threading.current_thread(), bstack1l1ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ⅘"), None)
    @staticmethod
    def bstack111lll11l1_opy_():
        if getattr(threading.current_thread(), bstack1l1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨ⅙"), None):
            return {
                bstack1l1ll_opy_ (u"ࠬࡺࡹࡱࡧࠪ⅚"): bstack1l1ll_opy_ (u"࠭ࡴࡦࡵࡷࠫ⅛"),
                bstack1l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⅜"): getattr(threading.current_thread(), bstack1l1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ⅝"), None)
            }
        if getattr(threading.current_thread(), bstack1l1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭⅞"), None):
            return {
                bstack1l1ll_opy_ (u"ࠪࡸࡾࡶࡥࠨ⅟"): bstack1l1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩⅠ"),
                bstack1l1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬⅡ"): getattr(threading.current_thread(), bstack1l1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪⅢ"), None)
            }
        return None
    @staticmethod
    def bstack1llll1lll11l_opy_(func):
        def wrap(*args, **kwargs):
            if bstack11ll1llll1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack111l1lllll_opy_(test, hook_name=None):
        bstack1llll1lll1ll_opy_ = test.parent
        if hook_name in [bstack1l1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬⅣ"), bstack1l1ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠩⅤ"), bstack1l1ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨⅥ"), bstack1l1ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬⅦ")]:
            bstack1llll1lll1ll_opy_ = test
        scope = []
        while bstack1llll1lll1ll_opy_ is not None:
            scope.append(bstack1llll1lll1ll_opy_.name)
            bstack1llll1lll1ll_opy_ = bstack1llll1lll1ll_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack1llll1lll1l1_opy_(hook_type):
        if hook_type == bstack1l1ll_opy_ (u"ࠦࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠤⅧ"):
            return bstack1l1ll_opy_ (u"࡙ࠧࡥࡵࡷࡳࠤ࡭ࡵ࡯࡬ࠤⅨ")
        elif hook_type == bstack1l1ll_opy_ (u"ࠨࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠥⅩ"):
            return bstack1l1ll_opy_ (u"ࠢࡕࡧࡤࡶࡩࡵࡷ࡯ࠢ࡫ࡳࡴࡱࠢⅪ")
    @staticmethod
    def bstack1llll1lll111_opy_(bstack11ll11l11l_opy_):
        try:
            if not bstack11ll1llll1_opy_.on():
                return bstack11ll11l11l_opy_
            if os.environ.get(bstack1l1ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࠨⅫ"), None) == bstack1l1ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢⅬ"):
                tests = os.environ.get(bstack1l1ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠢⅭ"), None)
                if tests is None or tests == bstack1l1ll_opy_ (u"ࠦࡳࡻ࡬࡭ࠤⅮ"):
                    return bstack11ll11l11l_opy_
                bstack11ll11l11l_opy_ = tests.split(bstack1l1ll_opy_ (u"ࠬ࠲ࠧⅯ"))
                return bstack11ll11l11l_opy_
        except Exception as exc:
            logger.debug(bstack1l1ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡸࡥࡳࡷࡱࠤ࡭ࡧ࡮ࡥ࡮ࡨࡶ࠿ࠦࠢⅰ") + str(str(exc)) + bstack1l1ll_opy_ (u"ࠢࠣⅱ"))
        return bstack11ll11l11l_opy_