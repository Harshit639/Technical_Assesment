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
from typing import Dict, List, Any, Callable, Tuple, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1ll1lllllll_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1llllllll1l_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llll1lllll_opy_,
    bstack1llll1ll1l1_opy_,
)
from bstack_utils.helper import  bstack11ll1ll11_opy_
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll11lll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11ll11_opy_, bstack1lll1ll1111_opy_, bstack1lll1111lll_opy_, bstack1llll11llll_opy_
from typing import Tuple, Any
import threading
from bstack_utils.bstack1l11111l1l_opy_ import bstack1l111ll11l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll1ll1_opy_ import bstack1llll111lll_opy_
from bstack_utils.percy import bstack1lll1l11_opy_
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.constants import *
import re
class bstack1llll1111l1_opy_(bstack1llll11lll1_opy_):
    def __init__(self, bstack1l1l1l1ll11_opy_: Dict[str, str]):
        super().__init__()
        self.bstack1l1l1l1ll11_opy_ = bstack1l1l1l1ll11_opy_
        self.percy = bstack1lll1l11_opy_()
        self.bstack1l11111l_opy_ = bstack1l111ll11l_opy_()
        self.bstack1l1l1l111l1_opy_()
        bstack1lll11lll1l_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.bstack1lllll11l1l_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1l1l1l11l11_opy_)
        TestFramework.bstack1ll111ll111_opy_((bstack1llll11ll11_opy_.TEST, bstack1lll1111lll_opy_.POST), self.bstack1ll11l11lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l1l1llll1l_opy_(self, instance: bstack1llll1ll1l1_opy_, driver: object):
        bstack1l1l1ll11l1_opy_ = TestFramework.bstack1lllll11l11_opy_(instance.context)
        for t in bstack1l1l1ll11l1_opy_:
            bstack1l1ll1ll1l1_opy_ = TestFramework.bstack1lllll111ll_opy_(t, bstack1llll111lll_opy_.bstack1l1l1llllll_opy_, [])
            if any(instance is d[1] for d in bstack1l1ll1ll1l1_opy_) or instance == driver:
                return t
    def bstack1l1l1l11l11_opy_(
        self,
        f: bstack1lll11lll1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        try:
            instance, method_name = exec
            if not bstack1lll11lll1l_opy_.bstack1ll1l111ll1_opy_(method_name):
                return
            platform_index = f.bstack1lllll111ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1ll111l111l_opy_, 0)
            bstack1l1ll111l1l_opy_ = self.bstack1l1l1llll1l_opy_(instance, driver)
            bstack1l1l1l111ll_opy_ = TestFramework.bstack1lllll111ll_opy_(bstack1l1ll111l1l_opy_, TestFramework.bstack1l1l1l1l111_opy_, None)
            if not bstack1l1l1l111ll_opy_:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠤࡲࡲࡤࡶࡲࡦࡡࡨࡼࡪࡩࡵࡵࡧ࠽ࠤࡷ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡢࡵࠣࡷࡪࡹࡳࡪࡱࡱࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡾ࡫ࡴࠡࡵࡷࡥࡷࡺࡥࡥࠤዋ"))
                return
            driver_command = f.bstack1ll11ll1111_opy_(*args)
            for command in bstack1llllllll_opy_:
                if command == driver_command:
                    self.bstack1llll1ll_opy_(driver, platform_index)
            bstack11l111l11_opy_ = self.percy.bstack11ll1ll1l_opy_()
            if driver_command in bstack1l11l11ll_opy_[bstack11l111l11_opy_]:
                self.bstack1l11111l_opy_.bstack11llll1l1l_opy_(bstack1l1l1l111ll_opy_, driver_command)
        except Exception as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠥࡳࡳࡥࡰࡳࡧࡢࡩࡽ࡫ࡣࡶࡶࡨ࠾ࠥ࡫ࡲࡳࡱࡵࠦዌ"), e)
    def bstack1ll11l11lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll1111_opy_,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack11l1l111l_opy_ import bstack1llll11l1l1_opy_
        bstack1l1ll1ll1l1_opy_ = f.bstack1lllll111ll_opy_(instance, bstack1llll111lll_opy_.bstack1l1l1llllll_opy_, [])
        if not bstack1l1ll1ll1l1_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡴࡴ࡟ࡢࡨࡷࡩࡷࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨው") + str(kwargs) + bstack1l1ll_opy_ (u"ࠧࠨዎ"))
            return
        if len(bstack1l1ll1ll1l1_opy_) > 1:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣዏ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠢࠣዐ"))
        bstack1l1l1l1l1ll_opy_, bstack1l1l1l1lll1_opy_ = bstack1l1ll1ll1l1_opy_[0]
        driver = bstack1l1l1l1l1ll_opy_()
        if not driver:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࠥࡪࡲࡪࡸࡨࡶࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤዑ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠤࠥዒ"))
            return
        bstack1l1l1l11ll1_opy_ = {
            TestFramework.bstack1ll111l11ll_opy_: bstack1l1ll_opy_ (u"ࠥࡸࡪࡹࡴࠡࡰࡤࡱࡪࠨዓ"),
            TestFramework.bstack1ll11l111l1_opy_: bstack1l1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࠢࡸࡹ࡮ࡪࠢዔ"),
            TestFramework.bstack1l1l1l1l111_opy_: bstack1l1ll_opy_ (u"ࠧࡺࡥࡴࡶࠣࡶࡪࡸࡵ࡯ࠢࡱࡥࡲ࡫ࠢዕ")
        }
        bstack1l1l1l1l1l1_opy_ = { key: f.bstack1lllll111ll_opy_(instance, key) for key in bstack1l1l1l11ll1_opy_ }
        bstack1l1l1l1l11l_opy_ = [key for key, value in bstack1l1l1l1l1l1_opy_.items() if not value]
        if bstack1l1l1l1l11l_opy_:
            for key in bstack1l1l1l1l11l_opy_:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠨ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡶࡨࡷࡹࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠤዖ") + str(key) + bstack1l1ll_opy_ (u"ࠢࠣ዗"))
            return
        platform_index = f.bstack1lllll111ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1ll111l111l_opy_, 0)
        if self.bstack1l1l1l1ll11_opy_.percy_capture_mode == bstack1l1ll_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥዘ"):
            bstack111l1l11_opy_ = bstack1l1l1l1l1l1_opy_.get(TestFramework.bstack1l1l1l1l111_opy_) + bstack1l1ll_opy_ (u"ࠤ࠰ࡸࡪࡹࡴࡤࡣࡶࡩࠧዙ")
            bstack1ll1l11l11l_opy_ = bstack1llll11l1l1_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack1l1l1l11l1l_opy_.value)
            PercySDK.screenshot(
                driver,
                bstack111l1l11_opy_,
                bstack1l111l11l1_opy_=bstack1l1l1l1l1l1_opy_[TestFramework.bstack1ll111l11ll_opy_],
                bstack11l11l11_opy_=bstack1l1l1l1l1l1_opy_[TestFramework.bstack1ll11l111l1_opy_],
                bstack1l1l11ll11_opy_=platform_index
            )
            bstack1llll11l1l1_opy_.end(EVENTS.bstack1l1l1l11l1l_opy_.value, bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥዚ"), bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠦ࠿࡫࡮ࡥࠤዛ"), True, None, None, None, None, test_name=bstack111l1l11_opy_)
    def bstack1llll1ll_opy_(self, driver, platform_index):
        if self.bstack1l11111l_opy_.bstack11ll11l1_opy_() is True or self.bstack1l11111l_opy_.capturing() is True:
            return
        self.bstack1l11111l_opy_.bstack1111l111_opy_()
        while not self.bstack1l11111l_opy_.bstack11ll11l1_opy_():
            bstack1l1l1l111ll_opy_ = self.bstack1l11111l_opy_.bstack11l111ll1_opy_()
            self.bstack1ll1ll1l11_opy_(driver, bstack1l1l1l111ll_opy_, platform_index)
        self.bstack1l11111l_opy_.bstack1lll1ll1l1_opy_()
    def bstack1ll1ll1l11_opy_(self, driver, bstack1llll11l_opy_, platform_index, test=None):
        from bstack_utils.bstack11l1l111l_opy_ import bstack1llll11l1l1_opy_
        bstack1ll1l11l11l_opy_ = bstack1llll11l1l1_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack11l11ll111_opy_.value)
        if test != None:
            bstack1l111l11l1_opy_ = getattr(test, bstack1l1ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪዜ"), None)
            bstack11l11l11_opy_ = getattr(test, bstack1l1ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫዝ"), None)
            PercySDK.screenshot(driver, bstack1llll11l_opy_, bstack1l111l11l1_opy_=bstack1l111l11l1_opy_, bstack11l11l11_opy_=bstack11l11l11_opy_, bstack1l1l11ll11_opy_=platform_index)
        else:
            PercySDK.screenshot(driver, bstack1llll11l_opy_)
        bstack1llll11l1l1_opy_.end(EVENTS.bstack11l11ll111_opy_.value, bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢዞ"), bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠣ࠼ࡨࡲࡩࠨዟ"), True, None, None, None, None, test_name=bstack1llll11l_opy_)
    def bstack1l1l1l111l1_opy_(self):
        os.environ[bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧዠ")] = str(self.bstack1l1l1l1ll11_opy_.success)
        os.environ[bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࡠࡅࡄࡔ࡙࡛ࡒࡆࡡࡐࡓࡉࡋࠧዡ")] = str(self.bstack1l1l1l1ll11_opy_.percy_capture_mode)
        self.percy.bstack1l1l1l11lll_opy_(self.bstack1l1l1l1ll11_opy_.is_percy_auto_enabled)
        self.percy.bstack1l1l1l1ll1l_opy_(self.bstack1l1l1l1ll11_opy_.percy_build_id)