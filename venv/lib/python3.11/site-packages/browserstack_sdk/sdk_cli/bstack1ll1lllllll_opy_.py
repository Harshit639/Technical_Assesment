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
import logging
import abc
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import bstack111111l1ll_opy_
class bstack1llll11lll1_opy_(abc.ABC):
    bin_session_id: str
    bstack111111l11l_opy_: bstack111111l1ll_opy_
    def __init__(self):
        self.bstack1lll1ll111l_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack111111l11l_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1llll11l1ll_opy_(self):
        return (self.bstack1lll1ll111l_opy_ != None and self.bin_session_id != None and self.bstack111111l11l_opy_ != None)
    def configure(self, bstack1lll1ll111l_opy_, config, bin_session_id: str, bstack111111l11l_opy_: bstack111111l1ll_opy_):
        self.bstack1lll1ll111l_opy_ = bstack1lll1ll111l_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack111111l11l_opy_ = bstack111111l11l_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡧࡧࠤࡲࡵࡤࡶ࡮ࡨࠤࢀࡹࡥ࡭ࡨ࠱ࡣࡤࡩ࡬ࡢࡵࡶࡣࡤ࠴࡟ࡠࡰࡤࡱࡪࡥ࡟ࡾ࠼ࠣࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࡁࠧሾ") + str(self.bin_session_id) + bstack1l1ll_opy_ (u"ࠤࠥሿ"))
    def bstack1ll1111ll11_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1l1ll_opy_ (u"ࠥࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠤࡨࡧ࡮࡯ࡱࡷࠤࡧ࡫ࠠࡏࡱࡱࡩࠧቀ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False