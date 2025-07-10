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
import json
import os
import grpc
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1ll1lllllll_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1llllllll1l_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llll1lllll_opy_,
    bstack1llll1ll1l1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll11lll1l_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1l1ll111_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
import threading
import os
from bstack_utils.bstack11l1l111l_opy_ import bstack1llll11l1l1_opy_
class bstack1llll1l111l_opy_(bstack1llll11lll1_opy_):
    bstack1l11lll11l1_opy_ = bstack1l1ll_opy_ (u"ࠣࡴࡨ࡫࡮ࡹࡴࡦࡴࡢ࡭ࡳ࡯ࡴࠣፖ")
    bstack1l11ll11ll1_opy_ = bstack1l1ll_opy_ (u"ࠤࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶࠥፗ")
    bstack1l11lll1lll_opy_ = bstack1l1ll_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲࠥፘ")
    def __init__(self, bstack1lll11ll1l1_opy_):
        super().__init__()
        bstack1lll11lll1l_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.bstack1llllll111l_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1l11llll1ll_opy_)
        bstack1lll11lll1l_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.bstack1lllll11l1l_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1ll1111l1ll_opy_)
        bstack1lll11lll1l_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.bstack1lllll11l1l_opy_, bstack1llll1lllll_opy_.POST), self.bstack1l11lll1l11_opy_)
        bstack1lll11lll1l_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.bstack1lllll11l1l_opy_, bstack1llll1lllll_opy_.POST), self.bstack1l11ll1ll11_opy_)
        bstack1lll11lll1l_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.QUIT, bstack1llll1lllll_opy_.POST), self.bstack1l11ll1l1ll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11llll1ll_opy_(
        self,
        f: bstack1lll11lll1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1ll_opy_ (u"ࠦࡤࡥࡩ࡯࡫ࡷࡣࡤࠨፙ"):
            return
        def wrapped(driver, init, *args, **kwargs):
            url = None
            try:
                if isinstance(kwargs.get(bstack1l1ll_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣፚ")), str):
                    url = kwargs.get(bstack1l1ll_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠤ፛"))
                elif hasattr(kwargs.get(bstack1l1ll_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥ፜")), bstack1l1ll_opy_ (u"ࠨࡡࡦࡰ࡮࡫࡮ࡵࡡࡦࡳࡳ࡬ࡩࡨࠩ፝")):
                    url = kwargs.get(bstack1l1ll_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠧ፞"))._client_config.remote_server_addr
                else:
                    url = kwargs.get(bstack1l1ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷࠨ፟"))._url
            except Exception as e:
                url = bstack1l1ll_opy_ (u"ࠫࠬ፠")
                self.logger.error(bstack1l1ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡺࡸ࡬ࠡࡨࡵࡳࡲࠦࡤࡳ࡫ࡹࡩࡷࡀࠠࡼࡿࠥ፡").format(e))
            self.logger.info(bstack1l1ll_opy_ (u"ࠨࡒࡦ࡯ࡲࡸࡪࠦࡓࡦࡴࡹࡩࡷࠦࡁࡥࡦࡵࡩࡸࡹࠠࡣࡧ࡬ࡲ࡬ࠦࡰࡢࡵࡶࡩࡩࠦࡡࡴࠢ࠽ࠤࢀࢃࠢ።").format(str(url)))
            self.bstack1l11ll1lll1_opy_(instance, url, f, kwargs)
            self.logger.info(bstack1l1ll_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠮ࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࡽࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࢀ࠾ࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧ፣").format(method_name=method_name, platform_index=f.platform_index, args=args, kwargs=kwargs))
            threading.current_thread().bstackSessionDriver = driver
            return init(driver, *args, **kwargs)
        return wrapped
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
        instance, method_name = exec
        if f.bstack1lllll111ll_opy_(instance, bstack1llll1l111l_opy_.bstack1l11lll11l1_opy_, False):
            return
        if not f.bstack1lllllllll1_opy_(instance, bstack1lll11lll1l_opy_.bstack1ll111l111l_opy_):
            return
        platform_index = f.bstack1lllll111ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1ll111l111l_opy_)
        if f.bstack1ll111ll1ll_opy_(method_name, *args) and len(args) > 1:
            bstack11l1l1111_opy_ = datetime.now()
            hub_url = bstack1lll11lll1l_opy_.hub_url(driver)
            self.logger.warning(bstack1l1ll_opy_ (u"ࠣࡪࡸࡦࡤࡻࡲ࡭࠿ࠥ፤") + str(hub_url) + bstack1l1ll_opy_ (u"ࠤࠥ፥"))
            bstack1l11ll11l1l_opy_ = args[1][bstack1l1ll_opy_ (u"ࠥࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤ፦")] if isinstance(args[1], dict) and bstack1l1ll_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥ፧") in args[1] else None
            bstack1l11lll1l1l_opy_ = bstack1l1ll_opy_ (u"ࠧࡧ࡬ࡸࡣࡼࡷࡒࡧࡴࡤࡪࠥ፨")
            if isinstance(bstack1l11ll11l1l_opy_, dict):
                bstack11l1l1111_opy_ = datetime.now()
                r = self.bstack1l11ll1111l_opy_(
                    instance.ref(),
                    platform_index,
                    f.framework_name,
                    f.framework_version,
                    hub_url
                )
                instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡩ࡯࡫ࡷࠦ፩"), datetime.now() - bstack11l1l1111_opy_)
                try:
                    if not r.success:
                        self.logger.info(bstack1l1ll_opy_ (u"ࠢࡴࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭࠺ࠡࠤ፪") + str(r) + bstack1l1ll_opy_ (u"ࠣࠤ፫"))
                        return
                    if r.hub_url:
                        f.bstack1l11ll111ll_opy_(instance, driver, r.hub_url)
                        f.bstack1lllll1l111_opy_(instance, bstack1llll1l111l_opy_.bstack1l11lll11l1_opy_, True)
                except Exception as e:
                    self.logger.error(bstack1l1ll_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣ፬"), e)
    def bstack1l11lll1l11_opy_(
        self,
        f: bstack1lll11lll1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
            session_id = bstack1lll11lll1l_opy_.session_id(driver)
            if session_id:
                bstack1l11llll1l1_opy_ = bstack1l1ll_opy_ (u"ࠥࡿࢂࡀࡳࡵࡣࡵࡸࠧ፭").format(session_id)
                bstack1llll11l1l1_opy_.mark(bstack1l11llll1l1_opy_)
    def bstack1l11ll1ll11_opy_(
        self,
        f: bstack1lll11lll1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.bstack1lllll111ll_opy_(instance, bstack1llll1l111l_opy_.bstack1l11ll11ll1_opy_, False):
            return
        ref = instance.ref()
        hub_url = bstack1lll11lll1l_opy_.hub_url(driver)
        if not hub_url:
            self.logger.warning(bstack1l1ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡨࡶࡤࡢࡹࡷࡲ࠽ࠣ፮") + str(hub_url) + bstack1l1ll_opy_ (u"ࠧࠨ፯"))
            return
        framework_session_id = bstack1lll11lll1l_opy_.session_id(driver)
        if not framework_session_id:
            self.logger.warning(bstack1l1ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤ࠾ࠤ፰") + str(framework_session_id) + bstack1l1ll_opy_ (u"ࠢࠣ፱"))
            return
        if bstack1lll11lll1l_opy_.bstack1l11ll111l1_opy_(*args) == bstack1lll11lll1l_opy_.bstack1l11ll1llll_opy_:
            bstack1l11lll1ll1_opy_ = bstack1l1ll_opy_ (u"ࠣࡽࢀ࠾ࡪࡴࡤࠣ፲").format(framework_session_id)
            bstack1l11llll1l1_opy_ = bstack1l1ll_opy_ (u"ࠤࡾࢁ࠿ࡹࡴࡢࡴࡷࠦ፳").format(framework_session_id)
            bstack1llll11l1l1_opy_.end(
                label=bstack1l1ll_opy_ (u"ࠥࡷࡩࡱ࠺ࡥࡴ࡬ࡺࡪࡸ࠺ࡱࡱࡶࡸ࠲࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡢࡶ࡬ࡳࡳࠨ፴"),
                start=bstack1l11llll1l1_opy_,
                end=bstack1l11lll1ll1_opy_,
                status=True,
                failure=None
            )
            bstack11l1l1111_opy_ = datetime.now()
            r = self.bstack1l11lll11ll_opy_(
                ref,
                f.bstack1lllll111ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1ll111l111l_opy_, 0),
                f.framework_name,
                f.framework_version,
                framework_session_id,
                hub_url,
            )
            instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠦ࡬ࡸࡰࡤ࠼ࡵࡩ࡬࡯ࡳࡵࡧࡵࡣࡸࡺࡡࡳࡶࠥ፵"), datetime.now() - bstack11l1l1111_opy_)
            f.bstack1lllll1l111_opy_(instance, bstack1llll1l111l_opy_.bstack1l11ll11ll1_opy_, r.success)
    def bstack1l11ll1l1ll_opy_(
        self,
        f: bstack1lll11lll1l_opy_,
        driver: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance = exec[0]
        if f.bstack1lllll111ll_opy_(instance, bstack1llll1l111l_opy_.bstack1l11lll1lll_opy_, False):
            return
        ref = instance.ref()
        framework_session_id = bstack1lll11lll1l_opy_.session_id(driver)
        hub_url = bstack1lll11lll1l_opy_.hub_url(driver)
        bstack11l1l1111_opy_ = datetime.now()
        r = self.bstack1l11lll111l_opy_(
            ref,
            f.bstack1lllll111ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1ll111l111l_opy_, 0),
            f.framework_name,
            f.framework_version,
            framework_session_id,
            hub_url,
        )
        instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠧ࡭ࡲࡱࡥ࠽ࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲࠥ፶"), datetime.now() - bstack11l1l1111_opy_)
        f.bstack1lllll1l111_opy_(instance, bstack1llll1l111l_opy_.bstack1l11lll1lll_opy_, r.success)
    @measure(event_name=EVENTS.bstack1l1l1111l_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def bstack1l1l11l1l11_opy_(self, platform_index: int, url: str, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        req.hub_url = url
        self.logger.debug(bstack1l1ll_opy_ (u"ࠨࡲࡦࡩ࡬ࡷࡹ࡫ࡲࡠࡹࡨࡦࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࠼ࠣࠦ፷") + str(req) + bstack1l1ll_opy_ (u"ࠢࠣ፸"))
        try:
            r = self.bstack1lll1ll111l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡴࡨࡧࡪ࡯ࡶࡦࡦࠣࡪࡷࡵ࡭ࠡࡵࡨࡶࡻ࡫ࡲ࠻ࠢࡶࡹࡨࡩࡥࡴࡵࡀࠦ፹") + str(r.success) + bstack1l1ll_opy_ (u"ࠤࠥ፺"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠥࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣ፻") + str(e) + bstack1l1ll_opy_ (u"ࠦࠧ፼"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l11ll1ll1l_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def bstack1l11ll1111l_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str
    ):
        self.bstack1ll1111ll11_opy_()
        req = structs.AutomationFrameworkInitRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡪࡰ࡬ࡸ࠿ࠦࠢ፽") + str(req) + bstack1l1ll_opy_ (u"ࠨࠢ፾"))
        try:
            r = self.bstack1lll1ll111l_opy_.AutomationFrameworkInit(req)
            if not r.success:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࡵࡸࡧࡨ࡫ࡳࡴ࠿ࠥ፿") + str(r.success) + bstack1l1ll_opy_ (u"ࠣࠤᎀ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢᎁ") + str(e) + bstack1l1ll_opy_ (u"ࠥࠦᎂ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l11ll1l1l1_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def bstack1l11lll11ll_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1ll1111ll11_opy_()
        req = structs.AutomationFrameworkStartRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡷ࡫ࡧࡪࡵࡷࡩࡷࡥࡳࡵࡣࡵࡸ࠿ࠦࠢᎃ") + str(req) + bstack1l1ll_opy_ (u"ࠧࠨᎄ"))
        try:
            r = self.bstack1lll1ll111l_opy_.AutomationFrameworkStart(req)
            if not r.success:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠨࡲࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡨࡵࡳࡲࠦࡳࡦࡴࡹࡩࡷࡀࠠࠣᎅ") + str(r) + bstack1l1ll_opy_ (u"ࠢࠣᎆ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠣࡴࡳࡧ࠲࡫ࡲࡳࡱࡵ࠾ࠥࠨᎇ") + str(e) + bstack1l1ll_opy_ (u"ࠤࠥᎈ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1l11llll11l_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def bstack1l11lll111l_opy_(
        self,
        ref: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        framework_session_id: str,
        hub_url: str,
    ):
        self.bstack1ll1111ll11_opy_()
        req = structs.AutomationFrameworkStopRequest()
        req.ref = ref
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.framework_session_id = framework_session_id
        req.hub_url = hub_url
        self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡶࡪ࡭ࡩࡴࡶࡨࡶࡤࡹࡴࡰࡲ࠽ࠤࠧᎉ") + str(req) + bstack1l1ll_opy_ (u"ࠦࠧᎊ"))
        try:
            r = self.bstack1lll1ll111l_opy_.AutomationFrameworkStop(req)
            if not r.success:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᎋ") + str(r) + bstack1l1ll_opy_ (u"ࠨࠢᎌ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᎍ") + str(e) + bstack1l1ll_opy_ (u"ࠣࠤᎎ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack11l1ll1lll_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def bstack1l11ll1lll1_opy_(self, instance: bstack1llll1ll1l1_opy_, url: str, f: bstack1lll11lll1l_opy_, kwargs):
        bstack1l11ll1l111_opy_ = version.parse(f.framework_version)
        bstack1l11ll11l11_opy_ = kwargs.get(bstack1l1ll_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥᎏ"))
        bstack1l11ll1l11l_opy_ = kwargs.get(bstack1l1ll_opy_ (u"ࠥࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥ᎐"))
        bstack1l1l11l1111_opy_ = {}
        bstack1l11lll1111_opy_ = {}
        bstack1l11llll111_opy_ = None
        bstack1l11ll11lll_opy_ = {}
        if bstack1l11ll1l11l_opy_ is not None or bstack1l11ll11l11_opy_ is not None: # check top level caps
            if bstack1l11ll1l11l_opy_ is not None:
                bstack1l11ll11lll_opy_[bstack1l1ll_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ᎑")] = bstack1l11ll1l11l_opy_
            if bstack1l11ll11l11_opy_ is not None and callable(getattr(bstack1l11ll11l11_opy_, bstack1l1ll_opy_ (u"ࠧࡺ࡯ࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢ᎒"))):
                bstack1l11ll11lll_opy_[bstack1l1ll_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹ࡟ࡢࡵࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ᎓")] = bstack1l11ll11l11_opy_.to_capabilities()
        response = self.bstack1l1l11l1l11_opy_(f.platform_index, url, instance.ref(), json.dumps(bstack1l11ll11lll_opy_).encode(bstack1l1ll_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨ᎔")))
        if response is not None and response.capabilities:
            bstack1l1l11l1111_opy_ = json.loads(response.capabilities.decode(bstack1l1ll_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢ᎕")))
            if not bstack1l1l11l1111_opy_: # empty caps bstack1l1l11lll1l_opy_ bstack1l1l11ll111_opy_ bstack1l1l11lll11_opy_ bstack1lll1l1l11l_opy_ or error in processing
                return
            bstack1l11llll111_opy_ = f.bstack1lll1l11l11_opy_[bstack1l1ll_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࡢࡪࡷࡵ࡭ࡠࡥࡤࡴࡸࠨ᎖")](bstack1l1l11l1111_opy_)
        if bstack1l11ll11l11_opy_ is not None and bstack1l11ll1l111_opy_ >= version.parse(bstack1l1ll_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ᎗")):
            bstack1l11lll1111_opy_ = None
        if (
                not bstack1l11ll11l11_opy_ and not bstack1l11ll1l11l_opy_
        ) or (
                bstack1l11ll1l111_opy_ < version.parse(bstack1l1ll_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ᎘"))
        ):
            bstack1l11lll1111_opy_ = {}
            bstack1l11lll1111_opy_.update(bstack1l1l11l1111_opy_)
        self.logger.info(bstack1l1ll111_opy_)
        if os.environ.get(bstack1l1ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠣ᎙")).lower().__eq__(bstack1l1ll_opy_ (u"ࠨࡴࡳࡷࡨࠦ᎚")):
            kwargs.update(
                {
                    bstack1l1ll_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥ᎛"): f.bstack1l11lllll11_opy_,
                }
            )
        if bstack1l11ll1l111_opy_ >= version.parse(bstack1l1ll_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨ᎜")):
            if bstack1l11ll1l11l_opy_ is not None:
                del kwargs[bstack1l1ll_opy_ (u"ࠤࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤ᎝")]
            kwargs.update(
                {
                    bstack1l1ll_opy_ (u"ࠥࡳࡵࡺࡩࡰࡰࡶࠦ᎞"): bstack1l11llll111_opy_,
                    bstack1l1ll_opy_ (u"ࠦࡰ࡫ࡥࡱࡡࡤࡰ࡮ࡼࡥࠣ᎟"): True,
                    bstack1l1ll_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡢࡨࡪࡺࡥࡤࡶࡲࡶࠧᎠ"): None,
                }
            )
        elif bstack1l11ll1l111_opy_ >= version.parse(bstack1l1ll_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬᎡ")):
            kwargs.update(
                {
                    bstack1l1ll_opy_ (u"ࠢࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠢᎢ"): bstack1l11lll1111_opy_,
                    bstack1l1ll_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤᎣ"): bstack1l11llll111_opy_,
                    bstack1l1ll_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨᎤ"): True,
                    bstack1l1ll_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥᎥ"): None,
                }
            )
        elif bstack1l11ll1l111_opy_ >= version.parse(bstack1l1ll_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫᎦ")):
            kwargs.update(
                {
                    bstack1l1ll_opy_ (u"ࠧࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᎧ"): bstack1l11lll1111_opy_,
                    bstack1l1ll_opy_ (u"ࠨ࡫ࡦࡧࡳࡣࡦࡲࡩࡷࡧࠥᎨ"): True,
                    bstack1l1ll_opy_ (u"ࠢࡧ࡫࡯ࡩࡤࡪࡥࡵࡧࡦࡸࡴࡸࠢᎩ"): None,
                }
            )
        else:
            kwargs.update(
                {
                    bstack1l1ll_opy_ (u"ࠣࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠣᎪ"): bstack1l11lll1111_opy_,
                    bstack1l1ll_opy_ (u"ࠤ࡮ࡩࡪࡶ࡟ࡢ࡮࡬ࡺࡪࠨᎫ"): True,
                    bstack1l1ll_opy_ (u"ࠥࡪ࡮ࡲࡥࡠࡦࡨࡸࡪࡩࡴࡰࡴࠥᎬ"): None,
                }
            )