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
class RobotHandler():
    def __init__(self, args, logger, bstack11111llll1_opy_, bstack11111ll1ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack11111llll1_opy_ = bstack11111llll1_opy_
        self.bstack11111ll1ll_opy_ = bstack11111ll1ll_opy_
    @staticmethod
    def version():
        import robot
        return robot.__version__
    @staticmethod
    def bstack111l1lllll_opy_(bstack111111lll1_opy_):
        bstack111111ll11_opy_ = []
        if bstack111111lll1_opy_:
            tokens = str(os.path.basename(bstack111111lll1_opy_)).split(bstack1l1ll_opy_ (u"ࠣࡡࠥႅ"))
            camelcase_name = bstack1l1ll_opy_ (u"ࠤࠣࠦႆ").join(t.title() for t in tokens)
            suite_name, bstack111111ll1l_opy_ = os.path.splitext(camelcase_name)
            bstack111111ll11_opy_.append(suite_name)
        return bstack111111ll11_opy_
    @staticmethod
    def bstack111111llll_opy_(typename):
        if bstack1l1ll_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨႇ") in typename:
            return bstack1l1ll_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧႈ")
        return bstack1l1ll_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨႉ")