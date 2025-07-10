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
import time
from bstack_utils.bstack11ll11l11l1_opy_ import bstack11ll11l1l1l_opy_
from bstack_utils.constants import bstack11l1lll1l1l_opy_
from bstack_utils.helper import get_host_info
class bstack111l1ll1l11_opy_:
    bstack1l1ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡉࡣࡱࡨࡱ࡫ࡳࠡࡶࡨࡷࡹࠦ࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡸ࡭ࠦࡴࡩࡧࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡶࡩࡷࡼࡥࡳ࠰ࠍࠤࠥࠦࠠࠣࠤࠥ῍")
    def __init__(self, config, logger):
        bstack1l1ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡩ࡯࡯ࡨ࡬࡫࠿ࠦࡤࡪࡥࡷ࠰ࠥࡺࡥࡴࡶࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡧࡴࡴࡦࡪࡩࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡣࡸࡺࡲࡢࡶࡨ࡫ࡾࡀࠠࡴࡶࡵ࠰ࠥࡺࡥࡴࡶࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡹࡴࡳࡣࡷࡩ࡬ࡿࠠ࡯ࡣࡰࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ῎")
        self.config = config
        self.logger = logger
        self.bstack1llllll1lll1_opy_ = bstack1l1ll_opy_ (u"ࠤࡷࡩࡸࡺ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠵ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡱ࡮࡬ࡸ࠲ࡺࡥࡴࡶࡶࠦ῏")
        self.bstack1llllll1l11l_opy_ = None
        self.bstack1llllll1ll11_opy_ = 60
        self.bstack1llllll1ll1l_opy_ = 5
        self.bstack1llllll11lll_opy_ = 0
    def bstack111l1l1ll11_opy_(self, test_files, orchestration_strategy):
        bstack1l1ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡊࡰ࡬ࡸ࡮ࡧࡴࡦࡵࠣࡸ࡭࡫ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡸࡥࡲࡷࡨࡷࡹࠦࡡ࡯ࡦࠣࡷࡹࡵࡲࡦࡵࠣࡸ࡭࡫ࠠࡳࡧࡶࡴࡴࡴࡳࡦࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡵࡵ࡬࡭࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥῐ")
        self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡠࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴ࡟ࠣࡍࡳ࡯ࡴࡪࡣࡷ࡭ࡳ࡭ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡽࡩࡵࡪࠣࡷࡹࡸࡡࡵࡧࡪࡽ࠿ࠦࡻࡾࠤῑ").format(orchestration_strategy))
        try:
            payload = {
                bstack1l1ll_opy_ (u"ࠧࡺࡥࡴࡶࡶࠦῒ"): [{bstack1l1ll_opy_ (u"ࠨࡦࡪ࡮ࡨࡔࡦࡺࡨࠣΐ"): f} for f in test_files],
                bstack1l1ll_opy_ (u"ࠢࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡓࡵࡴࡤࡸࡪ࡭ࡹࠣ῔"): orchestration_strategy,
                bstack1l1ll_opy_ (u"ࠣࡰࡲࡨࡪࡏ࡮ࡥࡧࡻࠦ῕"): int(os.environ.get(bstack1l1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡐࡒࡈࡊࡥࡉࡏࡆࡈ࡜ࠧῖ")) or bstack1l1ll_opy_ (u"ࠥ࠴ࠧῗ")),
                bstack1l1ll_opy_ (u"ࠦࡹࡵࡴࡢ࡮ࡑࡳࡩ࡫ࡳࠣῘ"): int(os.environ.get(bstack1l1ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡕࡔࡂࡎࡢࡒࡔࡊࡅࡠࡅࡒ࡙ࡓ࡚ࠢῙ")) or bstack1l1ll_opy_ (u"ࠨ࠱ࠣῚ")),
                bstack1l1ll_opy_ (u"ࠢࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠧΊ"): self.config.get(bstack1l1ll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭῜"), bstack1l1ll_opy_ (u"ࠩࠪ῝")),
                bstack1l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠨ῞"): self.config.get(bstack1l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ῟"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡖࡺࡴࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥῠ"): os.environ.get(bstack1l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬῡ"), None),
                bstack1l1ll_opy_ (u"ࠢࡩࡱࡶࡸࡎࡴࡦࡰࠤῢ"): get_host_info(),
            }
            self.logger.debug(bstack1l1ll_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡔࡧࡱࡨ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷ࠿ࠦࡻࡾࠤΰ").format(payload))
            response = bstack11ll11l1l1l_opy_.bstack1111111l1l1_opy_(self.bstack1llllll1lll1_opy_, payload)
            if response:
                self.bstack1llllll1l11l_opy_ = self._1llllll1l111_opy_(response)
                self.logger.debug(bstack1l1ll_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡕࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧῤ").format(self.bstack1llllll1l11l_opy_))
            else:
                self.logger.error(bstack1l1ll_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡭ࡥࡵࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠰ࠥῥ"))
        except Exception as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠦࡠࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡳࡪࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹ࠺࠻ࠢࡾࢁࠧῦ").format(e))
    def _1llllll1l111_opy_(self, response):
        bstack1l1ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡶࡴࡩࡥࡴࡵࡨࡷࠥࡺࡨࡦࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡂࡒࡌࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠦࡡ࡯ࡦࠣࡩࡽࡺࡲࡢࡥࡷࡷࠥࡸࡥ࡭ࡧࡹࡥࡳࡺࠠࡧ࡫ࡨࡰࡩࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧῧ")
        bstack1ll1l1ll1l_opy_ = {}
        bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢῨ")] = response.get(bstack1l1ll_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣῩ"), self.bstack1llllll1ll11_opy_)
        bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡋࡱࡸࡪࡸࡶࡢ࡮ࠥῪ")] = response.get(bstack1l1ll_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡌࡲࡹ࡫ࡲࡷࡣ࡯ࠦΎ"), self.bstack1llllll1ll1l_opy_)
        bstack1llllll1l1ll_opy_ = response.get(bstack1l1ll_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡘࡶࡱࠨῬ"))
        bstack1llllll11l11_opy_ = response.get(bstack1l1ll_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸ࡚ࡸ࡬ࠣ῭"))
        if bstack1llllll1l1ll_opy_:
            bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸ࡚ࡸ࡬ࠣ΅")] = bstack1llllll1l1ll_opy_.split(bstack11l1lll1l1l_opy_ + bstack1l1ll_opy_ (u"ࠨ࠯ࠣ`"))[1] if bstack11l1lll1l1l_opy_ + bstack1l1ll_opy_ (u"ࠢ࠰ࠤ῰") in bstack1llllll1l1ll_opy_ else bstack1llllll1l1ll_opy_
        else:
            bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦ῱")] = None
        if bstack1llllll11l11_opy_:
            bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡘࡶࡱࠨῲ")] = bstack1llllll11l11_opy_.split(bstack11l1lll1l1l_opy_ + bstack1l1ll_opy_ (u"ࠥ࠳ࠧῳ"))[1] if bstack11l1lll1l1l_opy_ + bstack1l1ll_opy_ (u"ࠦ࠴ࠨῴ") in bstack1llllll11l11_opy_ else bstack1llllll11l11_opy_
        else:
            bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹ࡛ࡲ࡭ࠤ῵")] = None
        if (
            response.get(bstack1l1ll_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢῶ")) is None or
            response.get(bstack1l1ll_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡊࡰࡷࡩࡷࡼࡡ࡭ࠤῷ")) is None or
            response.get(bstack1l1ll_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡗࡵࡰࠧῸ")) is None or
            response.get(bstack1l1ll_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡗࡵࡰࠧΌ")) is None
        ):
            self.logger.debug(bstack1l1ll_opy_ (u"ࠥ࡟ࡵࡸ࡯ࡤࡧࡶࡷࡤࡹࡰ࡭࡫ࡷࡣࡹ࡫ࡳࡵࡵࡢࡶࡪࡹࡰࡰࡰࡶࡩࡢࠦࡒࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡰࡸࡰࡱࠦࡶࡢ࡮ࡸࡩ࠭ࡹࠩࠡࡨࡲࡶࠥࡹ࡯࡮ࡧࠣࡥࡹࡺࡲࡪࡤࡸࡸࡪࡹࠠࡪࡰࠣࡷࡵࡲࡩࡵࠢࡷࡩࡸࡺࡳࠡࡃࡓࡍࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠢῺ"))
        return bstack1ll1l1ll1l_opy_
    def bstack111l1ll1l1l_opy_(self):
        if not self.bstack1llllll1l11l_opy_:
            self.logger.error(bstack1l1ll_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡔ࡯ࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡧࡥࡹࡧࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠱ࠦΏ"))
            return None
        bstack1llllll1l1l1_opy_ = None
        test_files = []
        bstack1llllll11l1l_opy_ = int(time.time() * 1000) # bstack1llllll1llll_opy_ sec
        bstack1lllllll1111_opy_ = int(self.bstack1llllll1l11l_opy_.get(bstack1l1ll_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࡏ࡮ࡵࡧࡵࡺࡦࡲࠢῼ"), self.bstack1llllll1ll1l_opy_))
        bstack1llllll11ll1_opy_ = int(self.bstack1llllll1l11l_opy_.get(bstack1l1ll_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢ´"), self.bstack1llllll1ll11_opy_)) * 1000
        bstack1llllll11l11_opy_ = self.bstack1llllll1l11l_opy_.get(bstack1l1ll_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦ῾"), None)
        bstack1llllll1l1ll_opy_ = self.bstack1llllll1l11l_opy_.get(bstack1l1ll_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦ῿"), None)
        if bstack1llllll1l1ll_opy_ is None and bstack1llllll11l11_opy_ is None:
            return None
        try:
            while bstack1llllll1l1ll_opy_ and (time.time() * 1000 - bstack1llllll11l1l_opy_) < bstack1llllll11ll1_opy_:
                response = bstack11ll11l1l1l_opy_.bstack111111l11l1_opy_(bstack1llllll1l1ll_opy_, {})
                if response and response.get(bstack1l1ll_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣ ")):
                    bstack1llllll1l1l1_opy_ = response.get(bstack1l1ll_opy_ (u"ࠥࡸࡪࡹࡴࡴࠤ "))
                self.bstack1llllll11lll_opy_ += 1
                if bstack1llllll1l1l1_opy_:
                    break
                time.sleep(bstack1lllllll1111_opy_)
                self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡌࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡰࡴࡧࡩࡷ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡧࡴࡲࡱࠥࡸࡥࡴࡷ࡯ࡸ࡛ࠥࡒࡍࠢࡤࡪࡹ࡫ࡲࠡࡹࡤ࡭ࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡻࡾࠢࡶࡩࡨࡵ࡮ࡥࡵ࠱ࠦ ").format(bstack1lllllll1111_opy_))
            if bstack1llllll11l11_opy_ and not bstack1llllll1l1l1_opy_:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡡࡧࡦࡶࡒࡶࡩ࡫ࡲࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡢࠦࡆࡦࡶࡦ࡬࡮ࡴࡧࠡࡱࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࡳࠡࡨࡵࡳࡲࠦࡴࡪ࡯ࡨࡳࡺࡺࠠࡖࡔࡏࠦ "))
                response = bstack11ll11l1l1l_opy_.bstack111111l11l1_opy_(bstack1llllll11l11_opy_, {})
                if response and response.get(bstack1l1ll_opy_ (u"ࠨࡴࡦࡵࡷࡷࠧ ")):
                    bstack1llllll1l1l1_opy_ = response.get(bstack1l1ll_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨ "))
            if bstack1llllll1l1l1_opy_ and len(bstack1llllll1l1l1_opy_) > 0:
                for bstack111ll11l1l_opy_ in bstack1llllll1l1l1_opy_:
                    file_path = bstack111ll11l1l_opy_.get(bstack1l1ll_opy_ (u"ࠣࡨ࡬ࡰࡪࡖࡡࡵࡪࠥ "))
                    if file_path:
                        test_files.append(file_path)
            if not bstack1llllll1l1l1_opy_:
                return None
            self.logger.debug(bstack1l1ll_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡓࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡴࡨࡧࡪ࡯ࡶࡦࡦ࠽ࠤࢀࢃࠢ ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠽ࠤࢀࢃࠢ ").format(e))
            return None
    def bstack111l1ll11l1_opy_(self):
        bstack1l1ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦࡣࡰࡷࡱࡸࠥࡵࡦࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡁࡑࡋࠣࡧࡦࡲ࡬ࡴࠢࡰࡥࡩ࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ ")
        return self.bstack1llllll11lll_opy_