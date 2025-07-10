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
class bstack1l11ll111_opy_:
    def __init__(self, handler):
        self._1111111l111_opy_ = None
        self.handler = handler
        self._1111111l11l_opy_ = self.bstack11111111ll1_opy_()
        self.patch()
    def patch(self):
        self._1111111l111_opy_ = self._1111111l11l_opy_.execute
        self._1111111l11l_opy_.execute = self.bstack11111111lll_opy_()
    def bstack11111111lll_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1l1ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࠤ὘"), driver_command, None, this, args)
            response = self._1111111l111_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1l1ll_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࠤὙ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._1111111l11l_opy_.execute = self._1111111l111_opy_
    @staticmethod
    def bstack11111111ll1_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver