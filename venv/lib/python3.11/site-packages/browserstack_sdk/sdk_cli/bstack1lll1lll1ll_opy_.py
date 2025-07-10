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
import copy
import asyncio
import threading
from browserstack_sdk import sdk_pb2 as structs
from packaging import version
import traceback
from browserstack_sdk.sdk_cli.bstack1ll1lllllll_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1llllllll1l_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llll1lllll_opy_,
    bstack1llll1ll1l1_opy_,
)
from bstack_utils.constants import *
from typing import Any, List, Union, Dict
from pathlib import Path
from browserstack_sdk.sdk_cli.bstack1ll1lll1l1l_opy_ import bstack1ll1lllll11_opy_
from datetime import datetime
from typing import Tuple, Any
from bstack_utils.messages import bstack1l1ll111_opy_
from bstack_utils.helper import bstack1l1ll1111ll_opy_
import threading
import os
import urllib.parse
class bstack1llll1111ll_opy_(bstack1llll11lll1_opy_):
    def __init__(self, bstack1lll111ll1l_opy_):
        super().__init__()
        bstack1ll1lllll11_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.bstack1llllll111l_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1l1l1l11111_opy_)
        bstack1ll1lllll11_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.bstack1llllll111l_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1l1l11l11l1_opy_)
        bstack1ll1lllll11_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.bstack1lllll11ll1_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1l1l111llll_opy_)
        bstack1ll1lllll11_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.bstack1lllll11l1l_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1l1l11llll1_opy_)
        bstack1ll1lllll11_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.bstack1llllll111l_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1l1l11ll1l1_opy_)
        bstack1ll1lllll11_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.QUIT, bstack1llll1lllll_opy_.PRE), self.on_close)
        self.bstack1lll111ll1l_opy_ = bstack1lll111ll1l_opy_
    def is_enabled(self) -> bool:
        return True
    def bstack1l1l1l11111_opy_(
        self,
        f: bstack1ll1lllll11_opy_,
        bstack1l1l1l1111l_opy_: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1ll_opy_ (u"ࠦࡱࡧࡵ࡯ࡥ࡫ࠦዢ"):
            return
        if not bstack1l1ll1111ll_opy_():
            self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡘࡥࡵࡷࡵࡲ࡮ࡴࡧࠡ࡫ࡱࠤࡱࡧࡵ࡯ࡥ࡫ࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤዣ"))
            return
        def wrapped(bstack1l1l1l1111l_opy_, launch, *args, **kwargs):
            response = self.bstack1l1l11l1l11_opy_(f.platform_index, instance.ref(), json.dumps({bstack1l1ll_opy_ (u"࠭ࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬዤ"): True}).encode(bstack1l1ll_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨዥ")))
            if response is not None and response.capabilities:
                if not bstack1l1ll1111ll_opy_():
                    browser = launch(bstack1l1l1l1111l_opy_)
                    return browser
                bstack1l1l11l1111_opy_ = json.loads(response.capabilities.decode(bstack1l1ll_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢዦ")))
                if not bstack1l1l11l1111_opy_: # empty caps bstack1l1l11lll1l_opy_ bstack1l1l11ll111_opy_ bstack1l1l11lll11_opy_ bstack1lll1l1l11l_opy_ or error in processing
                    return
                bstack1l1l11ll11l_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1l1l11l1111_opy_))
                f.bstack1lllll1l111_opy_(instance, bstack1ll1lllll11_opy_.bstack1l1l11l111l_opy_, bstack1l1l11ll11l_opy_)
                f.bstack1lllll1l111_opy_(instance, bstack1ll1lllll11_opy_.bstack1l1l11l1lll_opy_, bstack1l1l11l1111_opy_)
                browser = bstack1l1l1l1111l_opy_.connect(bstack1l1l11ll11l_opy_)
                return browser
        return wrapped
    def bstack1l1l111llll_opy_(
        self,
        f: bstack1ll1lllll11_opy_,
        Connection: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1ll_opy_ (u"ࠤࡧ࡭ࡸࡶࡡࡵࡥ࡫ࠦዧ"):
            self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢࡧ࡭ࡸࡶࡡࡵࡥ࡫ࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤየ"))
            return
        if not bstack1l1ll1111ll_opy_():
            return
        def wrapped(Connection, dispatch, *args, **kwargs):
            data = args[0]
            try:
                if args and args[0].get(bstack1l1ll_opy_ (u"ࠫࡵࡧࡲࡢ࡯ࡶࠫዩ"), {}).get(bstack1l1ll_opy_ (u"ࠬࡨࡳࡑࡣࡵࡥࡲࡹࠧዪ")):
                    bstack1l1l11l11ll_opy_ = args[0][bstack1l1ll_opy_ (u"ࠨࡰࡢࡴࡤࡱࡸࠨያ")][bstack1l1ll_opy_ (u"ࠢࡣࡵࡓࡥࡷࡧ࡭ࡴࠤዬ")]
                    session_id = bstack1l1l11l11ll_opy_.get(bstack1l1ll_opy_ (u"ࠣࡵࡨࡷࡸ࡯࡯࡯ࡋࡧࠦይ"))
                    f.bstack1lllll1l111_opy_(instance, bstack1ll1lllll11_opy_.bstack1l1l11l1l1l_opy_, session_id)
            except Exception as e:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡦ࡬ࡷࡵࡧࡴࡤࡪࠣࡱࡪࡺࡨࡰࡦ࠽ࠤࠧዮ"), e)
            dispatch(Connection, *args)
        return wrapped
    def bstack1l1l11ll1l1_opy_(
        self,
        f: bstack1ll1lllll11_opy_,
        bstack1l1l1l1111l_opy_: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1ll_opy_ (u"ࠥࡧࡴࡴ࡮ࡦࡥࡷࠦዯ"):
            return
        if not bstack1l1ll1111ll_opy_():
            self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡗ࡫ࡴࡶࡴࡱ࡭ࡳ࡭ࠠࡪࡰࠣࡧࡴࡴ࡮ࡦࡥࡷࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤደ"))
            return
        def wrapped(bstack1l1l1l1111l_opy_, connect, *args, **kwargs):
            response = self.bstack1l1l11l1l11_opy_(f.platform_index, instance.ref(), json.dumps({bstack1l1ll_opy_ (u"ࠬ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫዱ"): True}).encode(bstack1l1ll_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧዲ")))
            if response is not None and response.capabilities:
                bstack1l1l11l1111_opy_ = json.loads(response.capabilities.decode(bstack1l1ll_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨዳ")))
                if not bstack1l1l11l1111_opy_:
                    return
                bstack1l1l11ll11l_opy_ = PLAYWRIGHT_HUB_URL + urllib.parse.quote(json.dumps(bstack1l1l11l1111_opy_))
                if bstack1l1l11l1111_opy_.get(bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧዴ")):
                    browser = bstack1l1l1l1111l_opy_.bstack1l1l11ll1ll_opy_(bstack1l1l11ll11l_opy_)
                    return browser
                else:
                    args = list(args)
                    args[0] = bstack1l1l11ll11l_opy_
                    return connect(bstack1l1l1l1111l_opy_, *args, **kwargs)
        return wrapped
    def bstack1l1l11l11l1_opy_(
        self,
        f: bstack1ll1lllll11_opy_,
        bstack1l1lllllll1_opy_: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1ll_opy_ (u"ࠤࡱࡩࡼࡥࡰࡢࡩࡨࠦድ"):
            return
        if not bstack1l1ll1111ll_opy_():
            self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡖࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡩ࡯ࠢࡱࡩࡼࡥࡰࡢࡩࡨࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤዶ"))
            return
        def wrapped(bstack1l1lllllll1_opy_, bstack1l1l11l1ll1_opy_, *args, **kwargs):
            contexts = bstack1l1lllllll1_opy_.browser.contexts
            if contexts:
                for context in contexts:
                    if context.pages:
                        for page in context.pages:
                                if bstack1l1ll_opy_ (u"ࠦࡦࡨ࡯ࡶࡶ࠽ࡦࡱࡧ࡮࡬ࠤዷ") in page.url:
                                    return page
                    else:
                        return bstack1l1l11l1ll1_opy_(bstack1l1lllllll1_opy_)
        return wrapped
    def bstack1l1l11l1l11_opy_(self, platform_index: int, ref, user_input_params: bytes):
        req = structs.DriverInitRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.user_input_params = user_input_params
        req.ref = ref
        self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡸࡥࡨ࡫ࡶࡸࡪࡸ࡟ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳ࡯ࡴ࠻ࠢࠥዸ") + str(req) + bstack1l1ll_opy_ (u"ࠨࠢዹ"))
        try:
            r = self.bstack1lll1ll111l_opy_.DriverInit(req)
            if not r.success:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠢࡳࡧࡦࡩ࡮ࡼࡥࡥࠢࡩࡶࡴࡳࠠࡴࡧࡵࡺࡪࡸ࠺ࠡࡵࡸࡧࡨ࡫ࡳࡴ࠿ࠥዺ") + str(r.success) + bstack1l1ll_opy_ (u"ࠣࠤዻ"))
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢዼ") + str(e) + bstack1l1ll_opy_ (u"ࠥࠦዽ"))
            traceback.print_exc()
            raise e
    def bstack1l1l11llll1_opy_(
        self,
        f: bstack1ll1lllll11_opy_,
        Connection: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1ll_opy_ (u"ࠦࡤࡹࡥ࡯ࡦࡢࡱࡪࡹࡳࡢࡩࡨࡣࡹࡵ࡟ࡴࡧࡵࡺࡪࡸࠢዾ"):
            return
        if not bstack1l1ll1111ll_opy_():
            return
        def wrapped(Connection, bstack1l1l11lllll_opy_, *args, **kwargs):
            return bstack1l1l11lllll_opy_(Connection, *args, **kwargs)
        return wrapped
    def on_close(
        self,
        f: bstack1ll1lllll11_opy_,
        bstack1l1l1l1111l_opy_: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if method_name != bstack1l1ll_opy_ (u"ࠧࡩ࡬ࡰࡵࡨࠦዿ"):
            return
        if not bstack1l1ll1111ll_opy_():
            self.logger.debug(bstack1l1ll_opy_ (u"ࠨࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡩ࡬ࡰࡵࡨࠤࡲ࡫ࡴࡩࡱࡧ࠰ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠤጀ"))
            return
        def wrapped(Connection, close, *args, **kwargs):
            return close(Connection)
        return wrapped