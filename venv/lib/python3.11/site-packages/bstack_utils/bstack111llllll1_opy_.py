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
import tempfile
import math
from bstack_utils import bstack1l1111111_opy_
from bstack_utils.constants import bstack111l1111l_opy_
bstack111l11lll11_opy_ = bstack1l1ll_opy_ (u"ࠧࡸࡥࡵࡴࡼࡘࡪࡹࡴࡴࡑࡱࡊࡦ࡯࡬ࡶࡴࡨ᷽ࠦ")
bstack111l11l1l11_opy_ = bstack1l1ll_opy_ (u"ࠨࡡࡣࡱࡵࡸࡇࡻࡩ࡭ࡦࡒࡲࡋࡧࡩ࡭ࡷࡵࡩࠧ᷾")
bstack111l111ll11_opy_ = bstack1l1ll_opy_ (u"ࠢࡳࡷࡱࡔࡷ࡫ࡶࡪࡱࡸࡷࡱࡿࡆࡢ࡫࡯ࡩࡩࡌࡩࡳࡵࡷ᷿ࠦ")
bstack111l111llll_opy_ = bstack1l1ll_opy_ (u"ࠣࡴࡨࡶࡺࡴࡐࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡉࡥ࡮ࡲࡥࡥࠤḀ")
bstack111l1l1111l_opy_ = bstack1l1ll_opy_ (u"ࠤࡶ࡯࡮ࡶࡆ࡭ࡣ࡮ࡽࡦࡴࡤࡇࡣ࡬ࡰࡪࡪࠢḁ")
bstack111l1l111l1_opy_ = {
    bstack111l11lll11_opy_,
    bstack111l11l1l11_opy_,
    bstack111l111ll11_opy_,
    bstack111l111llll_opy_,
    bstack111l1l1111l_opy_,
}
bstack111l11l1111_opy_ = {bstack1l1ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪḂ")}
logger = bstack1l1111111_opy_.get_logger(__name__, bstack111l1111l_opy_)
class bstack111l11ll11l_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack111l11l1l1l_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack1ll1l111l1_opy_:
    _1ll1l1ll1ll_opy_ = None
    def __init__(self, config):
        self.bstack111l11llll1_opy_ = False
        self.bstack111l11l11ll_opy_ = False
        self.bstack111l11ll1l1_opy_ = False
        self.bstack111l11lllll_opy_ = bstack111l11ll11l_opy_()
        opts = config.get(bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨḃ"), {})
        self.__111l1l11l1l_opy_(opts.get(bstack111l111ll11_opy_, False))
        self.__111l11l11l1_opy_(opts.get(bstack111l111llll_opy_, False))
        self.__111l11lll1l_opy_(opts.get(bstack111l1l1111l_opy_, False))
    @classmethod
    def bstack11ll11ll1_opy_(cls, config=None):
        if cls._1ll1l1ll1ll_opy_ is None and config is not None:
            cls._1ll1l1ll1ll_opy_ = bstack1ll1l111l1_opy_(config)
        return cls._1ll1l1ll1ll_opy_
    @staticmethod
    def bstack1l1ll1l1l_opy_(config: dict) -> bool:
        bstack111l1l1l111_opy_ = config.get(bstack1l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩḄ"), {}).get(bstack111l11lll11_opy_, {})
        return bstack111l1l1l111_opy_.get(bstack1l1ll_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧḅ"), False)
    @staticmethod
    def bstack1l1ll1ll1_opy_(config: dict) -> int:
        bstack111l1l1l111_opy_ = config.get(bstack1l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫḆ"), {}).get(bstack111l11lll11_opy_, {})
        retries = 0
        if bstack1ll1l111l1_opy_.bstack1l1ll1l1l_opy_(config):
            retries = bstack111l1l1l111_opy_.get(bstack1l1ll_opy_ (u"ࠨ࡯ࡤࡼࡗ࡫ࡴࡳ࡫ࡨࡷࠬḇ"), 1)
        return retries
    @staticmethod
    def bstack1l1l1ll11l_opy_(config: dict) -> dict:
        bstack111l1l111ll_opy_ = config.get(bstack1l1ll_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭Ḉ"), {})
        return {
            key: value for key, value in bstack111l1l111ll_opy_.items() if key in bstack111l1l111l1_opy_
        }
    @staticmethod
    def bstack111l111ll1l_opy_():
        bstack1l1ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡪࡨࡧࡰࠦࡩࡧࠢࡷ࡬ࡪࠦࡡࡣࡱࡵࡸࠥࡨࡵࡪ࡮ࡧࠤ࡫࡯࡬ࡦࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢḉ")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack1l1ll_opy_ (u"ࠦࡦࡨ࡯ࡳࡶࡢࡦࡺ࡯࡬ࡥࡡࡾࢁࠧḊ").format(os.getenv(bstack1l1ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥḋ")))))
    @staticmethod
    def bstack111l1l11111_opy_(test_name: str):
        bstack1l1ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇ࡭࡫ࡣ࡬ࠢ࡬ࡪࠥࡺࡨࡦࠢࡤࡦࡴࡸࡴࠡࡤࡸ࡭ࡱࡪࠠࡧ࡫࡯ࡩࠥ࡫ࡸࡪࡵࡷࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥḌ")
        bstack111l11l1lll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࡥࡻࡾ࠰ࡷࡼࡹࠨḍ").format(os.getenv(bstack1l1ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨḎ"))))
        with open(bstack111l11l1lll_opy_, bstack1l1ll_opy_ (u"ࠩࡤࠫḏ")) as file:
            file.write(bstack1l1ll_opy_ (u"ࠥࡿࢂࡢ࡮ࠣḐ").format(test_name))
    @staticmethod
    def bstack111l11ll111_opy_(framework: str) -> bool:
       return framework.lower() in bstack111l11l1111_opy_
    @staticmethod
    def bstack11l1l1ll11l_opy_(config: dict) -> bool:
        bstack111l1l11l11_opy_ = config.get(bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨḑ"), {}).get(bstack111l11l1l11_opy_, {})
        return bstack111l1l11l11_opy_.get(bstack1l1ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭Ḓ"), False)
    @staticmethod
    def bstack11l1l1lll1l_opy_(config: dict, bstack11l1l11llll_opy_: int = 0) -> int:
        bstack1l1ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡋࡪࡺࠠࡵࡪࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤ࠭ࠢࡺ࡬࡮ࡩࡨࠡࡥࡤࡲࠥࡨࡥࠡࡣࡱࠤࡦࡨࡳࡰ࡮ࡸࡸࡪࠦ࡮ࡶ࡯ࡥࡩࡷࠦ࡯ࡳࠢࡤࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡤࡱࡱࡪ࡮࡭ࠠࠩࡦ࡬ࡧࡹ࠯࠺ࠡࡖ࡫ࡩࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡲࡸࡦࡲ࡟ࡵࡧࡶࡸࡸࠦࠨࡪࡰࡷ࠭࠿ࠦࡔࡩࡧࠣࡸࡴࡺࡡ࡭ࠢࡱࡹࡲࡨࡥࡳࠢࡲࡪࠥࡺࡥࡴࡶࡶࠤ࠭ࡸࡥࡲࡷ࡬ࡶࡪࡪࠠࡧࡱࡵࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥ࠮ࡤࡤࡷࡪࡪࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦࡶ࠭࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡪࡰࡷ࠾࡚ࠥࡨࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦḓ")
        bstack111l1l11l11_opy_ = config.get(bstack1l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫḔ"), {}).get(bstack1l1ll_opy_ (u"ࠨࡣࡥࡳࡷࡺࡂࡶ࡫࡯ࡨࡔࡴࡆࡢ࡫࡯ࡹࡷ࡫ࠧḕ"), {})
        bstack111l1l11lll_opy_ = 0
        bstack111l111lll1_opy_ = 0
        if bstack1ll1l111l1_opy_.bstack11l1l1ll11l_opy_(config):
            bstack111l111lll1_opy_ = bstack111l1l11l11_opy_.get(bstack1l1ll_opy_ (u"ࠩࡰࡥࡽࡌࡡࡪ࡮ࡸࡶࡪࡹࠧḖ"), 5)
            if isinstance(bstack111l111lll1_opy_, str) and bstack111l111lll1_opy_.endswith(bstack1l1ll_opy_ (u"ࠪࠩࠬḗ")):
                try:
                    percentage = int(bstack111l111lll1_opy_.strip(bstack1l1ll_opy_ (u"ࠫࠪ࠭Ḙ")))
                    if bstack11l1l11llll_opy_ > 0:
                        bstack111l1l11lll_opy_ = math.ceil((percentage * bstack11l1l11llll_opy_) / 100)
                    else:
                        raise ValueError(bstack1l1ll_opy_ (u"࡚ࠧ࡯ࡵࡣ࡯ࠤࡹ࡫ࡳࡵࡵࠣࡱࡺࡹࡴࠡࡤࡨࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡦࡰࡴࠣࡴࡪࡸࡣࡦࡰࡷࡥ࡬࡫࠭ࡣࡣࡶࡩࡩࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥࡵ࠱ࠦḙ"))
                except ValueError as e:
                    raise ValueError(bstack1l1ll_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡱࡧࡵࡧࡪࡴࡴࡢࡩࡨࠤࡻࡧ࡬ࡶࡧࠣࡪࡴࡸࠠ࡮ࡣࡻࡊࡦ࡯࡬ࡶࡴࡨࡷ࠿ࠦࡻࡾࠤḚ").format(bstack111l111lll1_opy_)) from e
            else:
                bstack111l1l11lll_opy_ = int(bstack111l111lll1_opy_)
        logger.info(bstack1l1ll_opy_ (u"ࠢࡎࡣࡻࠤ࡫ࡧࡩ࡭ࡷࡵࡩࡸࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥࠢࡶࡩࡹࠦࡴࡰ࠼ࠣࡿࢂࠦࠨࡧࡴࡲࡱࠥࡩ࡯࡯ࡨ࡬࡫࠿ࠦࡻࡾࠫࠥḛ").format(bstack111l1l11lll_opy_, bstack111l111lll1_opy_))
        return bstack111l1l11lll_opy_
    def bstack111l11ll1ll_opy_(self):
        return self.bstack111l11llll1_opy_
    def __111l1l11l1l_opy_(self, value):
        self.bstack111l11llll1_opy_ = bool(value)
        self.__111l11l1ll1_opy_()
    def bstack111l11l111l_opy_(self):
        return self.bstack111l11l11ll_opy_
    def __111l11l11l1_opy_(self, value):
        self.bstack111l11l11ll_opy_ = bool(value)
        self.__111l11l1ll1_opy_()
    def bstack111l1l11ll1_opy_(self):
        return self.bstack111l11ll1l1_opy_
    def __111l11lll1l_opy_(self, value):
        self.bstack111l11ll1l1_opy_ = bool(value)
        self.__111l11l1ll1_opy_()
    def __111l11l1ll1_opy_(self):
        if self.bstack111l11llll1_opy_:
            self.bstack111l11l11ll_opy_ = False
            self.bstack111l11ll1l1_opy_ = False
            self.bstack111l11lllll_opy_.enable(bstack111l111ll11_opy_)
        elif self.bstack111l11l11ll_opy_:
            self.bstack111l11llll1_opy_ = False
            self.bstack111l11ll1l1_opy_ = False
            self.bstack111l11lllll_opy_.enable(bstack111l111llll_opy_)
        elif self.bstack111l11ll1l1_opy_:
            self.bstack111l11llll1_opy_ = False
            self.bstack111l11l11ll_opy_ = False
            self.bstack111l11lllll_opy_.enable(bstack111l1l1111l_opy_)
        else:
            self.bstack111l11lllll_opy_.disable()
    def bstack11ll1l11l_opy_(self):
        return self.bstack111l11lllll_opy_.bstack111l11l1l1l_opy_()
    def bstack1ll111l11l_opy_(self):
        if self.bstack111l11lllll_opy_.bstack111l11l1l1l_opy_():
            return self.bstack111l11lllll_opy_.get_name()
        return None