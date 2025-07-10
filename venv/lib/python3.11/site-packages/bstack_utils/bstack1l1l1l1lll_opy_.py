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
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack111l1l1lll1_opy_ import bstack111l1ll1l11_opy_
from bstack_utils.bstack111llllll1_opy_ import bstack1ll1l111l1_opy_
from bstack_utils.helper import bstack1ll1l11l_opy_
class bstack11ll1l1ll1_opy_:
    _1ll1l1ll1ll_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack111l1l1l11l_opy_ = bstack111l1ll1l11_opy_(self.config, logger)
        self.bstack111llllll1_opy_ = bstack1ll1l111l1_opy_.bstack11ll11ll1_opy_(config=self.config)
        self.bstack111l1ll11ll_opy_ = {}
        self.bstack1111l1l1ll_opy_ = False
        self.bstack111l1l1ll1l_opy_ = (
            self.__111l1ll1111_opy_()
            and self.bstack111llllll1_opy_ is not None
            and self.bstack111llllll1_opy_.bstack11ll1l11l_opy_()
            and config.get(bstack1l1ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᷢ"), None) is not None
            and config.get(bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᷣ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack11ll11ll1_opy_(cls, config, logger):
        if cls._1ll1l1ll1ll_opy_ is None and config is not None:
            cls._1ll1l1ll1ll_opy_ = bstack11ll1l1ll1_opy_(config, logger)
        return cls._1ll1l1ll1ll_opy_
    def bstack11ll1l11l_opy_(self):
        bstack1l1ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡊ࡯ࠡࡰࡲࡸࠥࡧࡰࡱ࡮ࡼࠤࡹ࡫ࡳࡵࠢࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡼ࡮ࡥ࡯࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡑ࠴࠵ࡾࠦࡩࡴࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡕࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡪࡵࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠦࡩࡴࠢࡑࡳࡳ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᷤ")
        return self.bstack111l1l1ll1l_opy_ and self.bstack111l1l1llll_opy_()
    def bstack111l1l1llll_opy_(self):
        return self.config.get(bstack1l1ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬᷥ"), None) in bstack11l1lll1l11_opy_
    def __111l1ll1111_opy_(self):
        bstack11ll1111ll1_opy_ = False
        for fw in bstack11l1ll11l11_opy_:
            if fw in self.config.get(bstack1l1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ᷦ"), bstack1l1ll_opy_ (u"ࠫࠬᷧ")):
                bstack11ll1111ll1_opy_ = True
        return bstack1ll1l11l_opy_(self.config.get(bstack1l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩᷨ"), bstack11ll1111ll1_opy_))
    def bstack111l1ll111l_opy_(self):
        return (not self.bstack11ll1l11l_opy_() and
                self.bstack111llllll1_opy_ is not None and self.bstack111llllll1_opy_.bstack11ll1l11l_opy_())
    def bstack111l1l1l1l1_opy_(self):
        if not self.bstack111l1ll111l_opy_():
            return
        if self.config.get(bstack1l1ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᷩ"), None) is None or self.config.get(bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᷪ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack1l1ll_opy_ (u"ࠣࡖࡨࡷࡹࠦࡒࡦࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡧࡦࡴࠧࡵࠢࡺࡳࡷࡱࠠࡢࡵࠣࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠦ࡯ࡳࠢࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠠࡪࡵࠣࡲࡺࡲ࡬࠯ࠢࡓࡰࡪࡧࡳࡦࠢࡶࡩࡹࠦࡡࠡࡰࡲࡲ࠲ࡴࡵ࡭࡮ࠣࡺࡦࡲࡵࡦ࠰ࠥᷫ"))
        if not self.__111l1ll1111_opy_():
            self.logger.info(bstack1l1ll_opy_ (u"ࠤࡗࡩࡸࡺࠠࡓࡧࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡨࡧ࡮ࠨࡶࠣࡻࡴࡸ࡫ࠡࡣࡶࠤࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠡ࡫ࡶࠤࡩ࡯ࡳࡢࡤ࡯ࡩࡩ࠴ࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡦࡰࡤࡦࡱ࡫ࠠࡪࡶࠣࡪࡷࡵ࡭ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠤ࡫࡯࡬ࡦ࠰ࠥᷬ"))
    def bstack111l1l1l1ll_opy_(self):
        return self.bstack1111l1l1ll_opy_
    def bstack1111l1llll_opy_(self, bstack111l1ll1ll1_opy_):
        self.bstack1111l1l1ll_opy_ = bstack111l1ll1ll1_opy_
        self.bstack1111ll1111_opy_(bstack1l1ll_opy_ (u"ࠥࡥࡵࡶ࡬ࡪࡧࡧࠦᷭ"), bstack111l1ll1ll1_opy_)
    def bstack11111l11l1_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡠࡸࡥࡰࡴࡧࡩࡷࡥࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࡠࠤࡓࡵࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡦࡰࡴࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫࠳ࠨᷮ"))
                return None
            orchestration_strategy = None
            if self.bstack111llllll1_opy_ is not None:
                orchestration_strategy = self.bstack111llllll1_opy_.bstack1ll111l11l_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack1l1ll_opy_ (u"ࠧࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡴࡳࡣࡷࡩ࡬ࡿࠠࡪࡵࠣࡒࡴࡴࡥ࠯ࠢࡆࡥࡳࡴ࡯ࡵࠢࡳࡶࡴࡩࡥࡦࡦࠣࡻ࡮ࡺࡨࠡࡶࡨࡷࡹࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴ࠮ࠣᷯ"))
                return None
            self.logger.info(bstack1l1ll_opy_ (u"ࠨࡒࡦࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡸ࡫ࡷ࡬ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡴࡳࡣࡷࡩ࡬ࡿ࠺ࠡࡽࢀࠦᷰ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack1l1ll_opy_ (u"ࠢࡖࡵ࡬ࡲ࡬ࠦࡃࡍࡋࠣࡪࡱࡵࡷࠡࡨࡲࡶࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥᷱ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy)
            else:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡗࡶ࡭ࡳ࡭ࠠࡴࡦ࡮ࠤ࡫ࡲ࡯ࡸࠢࡩࡳࡷࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦᷲ"))
                self.bstack111l1l1l11l_opy_.bstack111l1l1ll11_opy_(test_files, orchestration_strategy)
                ordered_test_files = self.bstack111l1l1l11l_opy_.bstack111l1ll1l1l_opy_()
            if not ordered_test_files:
                return None
            self.bstack1111ll1111_opy_(bstack1l1ll_opy_ (u"ࠤࡸࡴࡱࡵࡡࡥࡧࡧࡘࡪࡹࡴࡇ࡫࡯ࡩࡸࡉ࡯ࡶࡰࡷࠦᷳ"), len(test_files))
            self.bstack1111ll1111_opy_(bstack1l1ll_opy_ (u"ࠥࡲࡴࡪࡥࡊࡰࡧࡩࡽࠨᷴ"), int(os.environ.get(bstack1l1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡒࡔࡊࡅࡠࡋࡑࡈࡊ࡞ࠢ᷵")) or bstack1l1ll_opy_ (u"ࠧ࠶ࠢ᷶")))
            self.bstack1111ll1111_opy_(bstack1l1ll_opy_ (u"ࠨࡴࡰࡶࡤࡰࡓࡵࡤࡦࡵ᷷ࠥ"), int(os.environ.get(bstack1l1ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖ᷸ࠥ")) or bstack1l1ll_opy_ (u"ࠣ࠳᷹ࠥ")))
            self.bstack1111ll1111_opy_(bstack1l1ll_opy_ (u"ࠤࡧࡳࡼࡴ࡬ࡰࡣࡧࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳࡄࡱࡸࡲࡹࠨ᷺"), len(ordered_test_files))
            self.bstack1111ll1111_opy_(bstack1l1ll_opy_ (u"ࠥࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹࡁࡑࡋࡆࡥࡱࡲࡃࡰࡷࡱࡸࠧ᷻"), self.bstack111l1l1l11l_opy_.bstack111l1ll11l1_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡠࡸࡥࡰࡴࡧࡩࡷࡥࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࡠࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦ࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣ࡭ࡣࡶࡷࡪࡹ࠺ࠡࡽࢀࠦ᷼").format(e))
        return None
    def bstack1111ll1111_opy_(self, key, value):
        self.bstack111l1ll11ll_opy_[key] = value
    def bstack1ll11ll1l1_opy_(self):
        return self.bstack111l1ll11ll_opy_