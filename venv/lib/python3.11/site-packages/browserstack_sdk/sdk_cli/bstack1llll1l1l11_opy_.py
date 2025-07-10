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
from browserstack_sdk.sdk_cli.bstack1ll1lllllll_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1llllllll1l_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llll1lllll_opy_,
    bstack1llll1ll1l1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll11lll1l_opy_
from typing import Tuple, Callable, Any
import grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1ll1lllllll_opy_ import bstack1llll11lll1_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import traceback
import os
import time
class bstack1ll1ll1111l_opy_(bstack1llll11lll1_opy_):
    bstack1ll111ll11l_opy_ = False
    def __init__(self):
        super().__init__()
        bstack1lll11lll1l_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.bstack1lllll11l1l_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1ll1111l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1ll1111l1ll_opy_(
        self,
        f: bstack1lll11lll1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        hub_url = f.hub_url(driver)
        if f.bstack1ll11111l1l_opy_(hub_url):
            if not bstack1ll1ll1111l_opy_.bstack1ll111ll11l_opy_:
                self.logger.warning(bstack1l1ll_opy_ (u"ࠤ࡯ࡳࡨࡧ࡬ࠡࡵࡨࡰ࡫࠳ࡨࡦࡣ࡯ࠤ࡫ࡲ࡯ࡸࠢࡧ࡭ࡸࡧࡢ࡭ࡧࡧࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡪࡰࡩࡶࡦࠦࡳࡦࡵࡶ࡭ࡴࡴࡳࠡࡪࡸࡦࡤࡻࡲ࡭࠿ࠥሜ") + str(hub_url) + bstack1l1ll_opy_ (u"ࠥࠦም"))
                bstack1ll1ll1111l_opy_.bstack1ll111ll11l_opy_ = True
            return
        bstack1ll1l1111ll_opy_ = f.bstack1ll11ll1111_opy_(*args)
        bstack1ll11111ll1_opy_ = f.bstack1ll111111l1_opy_(*args)
        if bstack1ll1l1111ll_opy_ and bstack1ll1l1111ll_opy_.lower() == bstack1l1ll_opy_ (u"ࠦ࡫࡯࡮ࡥࡧ࡯ࡩࡲ࡫࡮ࡵࠤሞ") and bstack1ll11111ll1_opy_:
            framework_session_id = f.session_id(driver)
            locator_type, locator_value = bstack1ll11111ll1_opy_.get(bstack1l1ll_opy_ (u"ࠧࡻࡳࡪࡰࡪࠦሟ"), None), bstack1ll11111ll1_opy_.get(bstack1l1ll_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧሠ"), None)
            if not framework_session_id or not locator_type or not locator_value:
                self.logger.warning(bstack1l1ll_opy_ (u"ࠢࡼࡥࡲࡱࡲࡧ࡮ࡥࡡࡱࡥࡲ࡫ࡽ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠣࡳࡷࠦࡡࡳࡩࡶ࠲ࡺࡹࡩ࡯ࡩࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡴࡸࠠࡢࡴࡪࡷ࠳ࡼࡡ࡭ࡷࡨࡁࠧሡ") + str(locator_value) + bstack1l1ll_opy_ (u"ࠣࠤሢ"))
                return
            def bstack1lllll1ll1l_opy_(driver, bstack1ll1111l11l_opy_, *args, **kwargs):
                from selenium.common.exceptions import NoSuchElementException
                try:
                    result = bstack1ll1111l11l_opy_(driver, *args, **kwargs)
                    response = self.bstack1ll11111l11_opy_(
                        framework_session_id=framework_session_id,
                        is_success=True,
                        locator_type=locator_type,
                        locator_value=locator_value,
                    )
                    if response and response.execute_script:
                        driver.execute_script(response.execute_script)
                        self.logger.info(bstack1l1ll_opy_ (u"ࠤࡶࡹࡨࡩࡥࡴࡵ࠰ࡷࡨࡸࡩࡱࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࠧሣ") + str(locator_value) + bstack1l1ll_opy_ (u"ࠥࠦሤ"))
                    else:
                        self.logger.warning(bstack1l1ll_opy_ (u"ࠦࡸࡻࡣࡤࡧࡶࡷ࠲ࡴ࡯࠮ࡵࡦࡶ࡮ࡶࡴ࠻ࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥ࠾ࡽ࡯ࡳࡨࡧࡴࡰࡴࡢࡸࡾࡶࡥࡾࠢ࡯ࡳࡨࡧࡴࡰࡴࡢࡺࡦࡲࡵࡦ࠿ࡾࡰࡴࡩࡡࡵࡱࡵࡣࡻࡧ࡬ࡶࡧࢀࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡃࠢሥ") + str(response) + bstack1l1ll_opy_ (u"ࠧࠨሦ"))
                    return result
                except NoSuchElementException as e:
                    locator = (locator_type, locator_value)
                    return self.__1ll1111l1l1_opy_(
                        driver, bstack1ll1111l11l_opy_, e, framework_session_id, locator, *args, **kwargs
                    )
            bstack1lllll1ll1l_opy_.__name__ = bstack1ll1l1111ll_opy_
            return bstack1lllll1ll1l_opy_
    def __1ll1111l1l1_opy_(
        self,
        driver,
        bstack1ll1111l11l_opy_: Callable,
        exception,
        framework_session_id: str,
        locator: Tuple[str, str],
        *args,
        **kwargs,
    ):
        try:
            locator_type, locator_value = locator
            response = self.bstack1ll11111l11_opy_(
                framework_session_id=framework_session_id,
                is_success=False,
                locator_type=locator_type,
                locator_value=locator_value,
            )
            if response and response.execute_script:
                driver.execute_script(response.execute_script)
                self.logger.info(bstack1l1ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡶࡵ࡭࡬࡭ࡥࡳࡧࡧ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࠨሧ") + str(locator_value) + bstack1l1ll_opy_ (u"ࠢࠣረ"))
                bstack1ll11111lll_opy_ = self.bstack1ll111111ll_opy_(
                    framework_session_id=framework_session_id,
                    locator_type=locator_type,
                )
                self.logger.info(bstack1l1ll_opy_ (u"ࠣࡨࡤ࡭ࡱࡻࡲࡦ࠯࡫ࡩࡦࡲࡩ࡯ࡩ࠰ࡶࡪࡹࡵ࡭ࡶ࠽ࠤࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࡀࡿࡱࡵࡣࡢࡶࡲࡶࡤࡺࡹࡱࡧࢀࠤࡱࡵࡣࡢࡶࡲࡶࡤࡼࡡ࡭ࡷࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࢂࠦࡨࡦࡣ࡯࡭ࡳ࡭࡟ࡳࡧࡶࡹࡱࡺ࠽ࠣሩ") + str(bstack1ll11111lll_opy_) + bstack1l1ll_opy_ (u"ࠤࠥሪ"))
                if bstack1ll11111lll_opy_.success and args and len(args) > 1:
                    args[1].update(
                        {
                            bstack1l1ll_opy_ (u"ࠥࡹࡸ࡯࡮ࡨࠤራ"): bstack1ll11111lll_opy_.locator_type,
                            bstack1l1ll_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࠥሬ"): bstack1ll11111lll_opy_.locator_value,
                        }
                    )
                    return bstack1ll1111l11l_opy_(driver, *args, **kwargs)
                elif os.environ.get(bstack1l1ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡏ࡟ࡅࡇࡅ࡙ࡌࠨር"), False):
                    self.logger.info(bstack1llll1l1l1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡹࡷ࡫࠭ࡩࡧࡤࡰ࡮ࡴࡧ࠮ࡴࡨࡷࡺࡲࡴ࠮࡯࡬ࡷࡸ࡯࡮ࡨ࠼ࠣࡷࡱ࡫ࡥࡱࠪ࠶࠴࠮ࠦ࡬ࡦࡶࡷ࡭ࡳ࡭ࠠࡺࡱࡸࠤ࡮ࡴࡳࡱࡧࡦࡸࠥࡺࡨࡦࠢࡥࡶࡴࡽࡳࡦࡴࠣࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࠦ࡬ࡰࡩࡶࠦሮ"))
                    time.sleep(300)
            else:
                self.logger.warning(bstack1l1ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡺࡸࡥ࠮ࡰࡲ࠱ࡸࡩࡲࡪࡲࡷ࠾ࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࡁࢀࡲ࡯ࡤࡣࡷࡳࡷࡥࡴࡺࡲࡨࢁࠥࡲ࡯ࡤࡣࡷࡳࡷࡥࡶࡢ࡮ࡸࡩࡂࢁ࡬ࡰࡥࡤࡸࡴࡸ࡟ࡷࡣ࡯ࡹࡪࢃࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠿ࠥሯ") + str(response) + bstack1l1ll_opy_ (u"ࠣࠤሰ"))
        except Exception as err:
            self.logger.warning(bstack1l1ll_opy_ (u"ࠤࡩࡥ࡮ࡲࡵࡳࡧ࠰࡬ࡪࡧ࡬ࡪࡰࡪ࠱ࡷ࡫ࡳࡶ࡮ࡷ࠾ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࠨሱ") + str(err) + bstack1l1ll_opy_ (u"ࠥࠦሲ"))
        raise exception
    @measure(event_name=EVENTS.bstack1ll1111111l_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def bstack1ll11111l11_opy_(
        self,
        framework_session_id: str,
        is_success: bool,
        locator_type: str,
        locator_value: str,
        platform_index=bstack1l1ll_opy_ (u"ࠦ࠵ࠨሳ"),
    ):
        self.bstack1ll1111ll11_opy_()
        req = structs.AISelfHealStepRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.is_success = is_success
        req.test_name = bstack1l1ll_opy_ (u"ࠧࠨሴ")
        req.locator_type = locator_type
        req.locator_value = locator_value
        try:
            r = self.bstack1lll1ll111l_opy_.AISelfHealStep(req)
            self.logger.info(bstack1l1ll_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣስ") + str(r) + bstack1l1ll_opy_ (u"ࠢࠣሶ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨሷ") + str(e) + bstack1l1ll_opy_ (u"ࠤࠥሸ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1ll1111l111_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def bstack1ll111111ll_opy_(self, framework_session_id: str, locator_type: str, platform_index=bstack1l1ll_opy_ (u"ࠥ࠴ࠧሹ")):
        self.bstack1ll1111ll11_opy_()
        req = structs.AISelfHealGetRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_session_id = framework_session_id
        req.locator_type = locator_type
        try:
            r = self.bstack1lll1ll111l_opy_.AISelfHealGetResult(req)
            self.logger.info(bstack1l1ll_opy_ (u"ࠦࡷ࡫ࡣࡦ࡫ࡹࡩࡩࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨሺ") + str(r) + bstack1l1ll_opy_ (u"ࠧࠨሻ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠨࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦሼ") + str(e) + bstack1l1ll_opy_ (u"ࠢࠣሽ"))
            traceback.print_exc()
            raise e