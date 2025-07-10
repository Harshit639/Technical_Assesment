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
import traceback
from typing import Dict, Tuple, Callable, Type, List, Any
from urllib.parse import urlparse
from browserstack_sdk.sdk_cli.bstack1llllllll1l_opy_ import (
    bstack11111111l1_opy_,
    bstack1llll1ll1l1_opy_,
    bstack1lllll1lll1_opy_,
    bstack1llll1lllll_opy_,
)
import copy
from datetime import datetime, timezone, timedelta
from bstack_utils.bstack11l1l111l_opy_ import bstack1llll11l1l1_opy_
from bstack_utils.constants import EVENTS
class bstack1lll11lll1l_opy_(bstack11111111l1_opy_):
    bstack1l11l1l111l_opy_ = bstack1l1ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠢᕩ")
    NAME = bstack1l1ll_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥᕪ")
    bstack1l1l11l111l_opy_ = bstack1l1ll_opy_ (u"ࠤ࡫ࡹࡧࡥࡵࡳ࡮ࠥᕫ")
    bstack1l1l11l1l1l_opy_ = bstack1l1ll_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠥᕬ")
    bstack11lllll1111_opy_ = bstack1l1ll_opy_ (u"ࠦ࡮ࡴࡰࡶࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠤᕭ")
    bstack1l1l11l1lll_opy_ = bstack1l1ll_opy_ (u"ࠧࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠦᕮ")
    bstack1l11l1ll11l_opy_ = bstack1l1ll_opy_ (u"ࠨࡩࡴࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡪࡸࡦࠧᕯ")
    bstack11llll1l111_opy_ = bstack1l1ll_opy_ (u"ࠢࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠦᕰ")
    bstack11lllll111l_opy_ = bstack1l1ll_opy_ (u"ࠣࡧࡱࡨࡪࡪ࡟ࡢࡶࠥᕱ")
    bstack1ll111l111l_opy_ = bstack1l1ll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࠥᕲ")
    bstack1l11ll1llll_opy_ = bstack1l1ll_opy_ (u"ࠥࡲࡪࡽࡳࡦࡵࡶ࡭ࡴࡴࠢᕳ")
    bstack11llll1ll1l_opy_ = bstack1l1ll_opy_ (u"ࠦ࡬࡫ࡴࠣᕴ")
    bstack1l1ll111111_opy_ = bstack1l1ll_opy_ (u"ࠧࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠤᕵ")
    bstack1l11l11ll1l_opy_ = bstack1l1ll_opy_ (u"ࠨࡷ࠴ࡥࡨࡼࡪࡩࡵࡵࡧࡶࡧࡷ࡯ࡰࡵࠤᕶ")
    bstack1l11l1l11l1_opy_ = bstack1l1ll_opy_ (u"ࠢࡸ࠵ࡦࡩࡽ࡫ࡣࡶࡶࡨࡷࡨࡸࡩࡱࡶࡤࡷࡾࡴࡣࠣᕷ")
    bstack11llll1lll1_opy_ = bstack1l1ll_opy_ (u"ࠣࡳࡸ࡭ࡹࠨᕸ")
    bstack11llll1l11l_opy_: Dict[str, List[Callable]] = dict()
    bstack1l11lllll11_opy_: str
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lll1l11l11_opy_: Any
    bstack1l11l1l1111_opy_: Dict
    def __init__(
        self,
        bstack1l11lllll11_opy_: str,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        bstack1lll1l11l11_opy_: Dict[str, Any],
        methods=[bstack1l1ll_opy_ (u"ࠤࡢࡣ࡮ࡴࡩࡵࡡࡢࠦᕹ"), bstack1l1ll_opy_ (u"ࠥࡷࡹࡧࡲࡵࡡࡶࡩࡸࡹࡩࡰࡰࠥᕺ"), bstack1l1ll_opy_ (u"ࠦࡪࡾࡥࡤࡷࡷࡩࠧᕻ"), bstack1l1ll_opy_ (u"ࠧࡷࡵࡪࡶࠥᕼ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.bstack1l11lllll11_opy_ = bstack1l11lllll11_opy_
        self.platform_index = platform_index
        self.bstack1llllll11l1_opy_(methods)
        self.bstack1lll1l11l11_opy_ = bstack1lll1l11l11_opy_
    @staticmethod
    def session_id(target: object, strict=True):
        return bstack11111111l1_opy_.get_data(bstack1lll11lll1l_opy_.bstack1l1l11l1l1l_opy_, target, strict)
    @staticmethod
    def hub_url(target: object, strict=True):
        return bstack11111111l1_opy_.get_data(bstack1lll11lll1l_opy_.bstack1l1l11l111l_opy_, target, strict)
    @staticmethod
    def bstack11llll1ll11_opy_(target: object, strict=True):
        return bstack11111111l1_opy_.get_data(bstack1lll11lll1l_opy_.bstack11lllll1111_opy_, target, strict)
    @staticmethod
    def capabilities(target: object, strict=True):
        return bstack11111111l1_opy_.get_data(bstack1lll11lll1l_opy_.bstack1l1l11l1lll_opy_, target, strict)
    @staticmethod
    def bstack1l1llll1ll1_opy_(instance: bstack1llll1ll1l1_opy_) -> bool:
        return bstack11111111l1_opy_.bstack1lllll111ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1l11l1ll11l_opy_, False)
    @staticmethod
    def bstack1ll1l11l111_opy_(instance: bstack1llll1ll1l1_opy_, default_value=None):
        return bstack11111111l1_opy_.bstack1lllll111ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1l1l11l111l_opy_, default_value)
    @staticmethod
    def bstack1ll11ll11ll_opy_(instance: bstack1llll1ll1l1_opy_, default_value=None):
        return bstack11111111l1_opy_.bstack1lllll111ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1l1l11l1lll_opy_, default_value)
    @staticmethod
    def bstack1ll11111l1l_opy_(hub_url: str, bstack11llll1l1l1_opy_=bstack1l1ll_opy_ (u"ࠨ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠥᕽ")):
        try:
            bstack11llll1llll_opy_ = str(urlparse(hub_url).netloc) if hub_url else None
            return bstack11llll1llll_opy_.endswith(bstack11llll1l1l1_opy_)
        except:
            pass
        return False
    @staticmethod
    def bstack1ll1l111ll1_opy_(method_name: str):
        return method_name == bstack1l1ll_opy_ (u"ࠢࡦࡺࡨࡧࡺࡺࡥࠣᕾ")
    @staticmethod
    def bstack1ll111ll1ll_opy_(method_name: str, *args):
        return (
            bstack1lll11lll1l_opy_.bstack1ll1l111ll1_opy_(method_name)
            and bstack1lll11lll1l_opy_.bstack1l11ll111l1_opy_(*args) == bstack1lll11lll1l_opy_.bstack1l11ll1llll_opy_
        )
    @staticmethod
    def bstack1ll1l111lll_opy_(method_name: str, *args):
        if not bstack1lll11lll1l_opy_.bstack1ll1l111ll1_opy_(method_name):
            return False
        if not bstack1lll11lll1l_opy_.bstack1l11l11ll1l_opy_ in bstack1lll11lll1l_opy_.bstack1l11ll111l1_opy_(*args):
            return False
        bstack1ll11111ll1_opy_ = bstack1lll11lll1l_opy_.bstack1ll111111l1_opy_(*args)
        return bstack1ll11111ll1_opy_ and bstack1l1ll_opy_ (u"ࠣࡵࡦࡶ࡮ࡶࡴࠣᕿ") in bstack1ll11111ll1_opy_ and bstack1l1ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥᖀ") in bstack1ll11111ll1_opy_[bstack1l1ll_opy_ (u"ࠥࡷࡨࡸࡩࡱࡶࠥᖁ")]
    @staticmethod
    def bstack1ll11ll1l1l_opy_(method_name: str, *args):
        if not bstack1lll11lll1l_opy_.bstack1ll1l111ll1_opy_(method_name):
            return False
        if not bstack1lll11lll1l_opy_.bstack1l11l11ll1l_opy_ in bstack1lll11lll1l_opy_.bstack1l11ll111l1_opy_(*args):
            return False
        bstack1ll11111ll1_opy_ = bstack1lll11lll1l_opy_.bstack1ll111111l1_opy_(*args)
        return (
            bstack1ll11111ll1_opy_
            and bstack1l1ll_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦᖂ") in bstack1ll11111ll1_opy_
            and bstack1l1ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡦࡶ࡮ࡶࡴࠣᖃ") in bstack1ll11111ll1_opy_[bstack1l1ll_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࠨᖄ")]
        )
    @staticmethod
    def bstack1l11ll111l1_opy_(*args):
        return str(bstack1lll11lll1l_opy_.bstack1ll11ll1111_opy_(*args)).lower()
    @staticmethod
    def bstack1ll11ll1111_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1ll111111l1_opy_(*args):
        return args[1] if len(args) > 1 and isinstance(args[1], dict) else None
    @staticmethod
    def bstack11ll1l1l1l_opy_(driver):
        command_executor = getattr(driver, bstack1l1ll_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠥᖅ"), None)
        if not command_executor:
            return None
        hub_url = str(command_executor) if isinstance(command_executor, (str, bytes)) else None
        hub_url = str(command_executor._url) if not hub_url and getattr(command_executor, bstack1l1ll_opy_ (u"ࠣࡡࡸࡶࡱࠨᖆ"), None) else None
        if not hub_url:
            client_config = getattr(command_executor, bstack1l1ll_opy_ (u"ࠤࡢࡧࡱ࡯ࡥ࡯ࡶࡢࡧࡴࡴࡦࡪࡩࠥᖇ"), None)
            if not client_config:
                return None
            hub_url = getattr(client_config, bstack1l1ll_opy_ (u"ࠥࡶࡪࡳ࡯ࡵࡧࡢࡷࡪࡸࡶࡦࡴࡢࡥࡩࡪࡲࠣᖈ"), None)
        return hub_url
    def bstack1l11ll111ll_opy_(self, instance, driver, hub_url: str):
        result = False
        if not hub_url:
            return result
        command_executor = getattr(driver, bstack1l1ll_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠢᖉ"), None)
        if command_executor:
            if isinstance(command_executor, (str, bytes)):
                setattr(driver, bstack1l1ll_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠣᖊ"), hub_url)
                result = True
            elif hasattr(command_executor, bstack1l1ll_opy_ (u"ࠨ࡟ࡶࡴ࡯ࠦᖋ")):
                setattr(command_executor, bstack1l1ll_opy_ (u"ࠢࡠࡷࡵࡰࠧᖌ"), hub_url)
                result = True
        if result:
            self.bstack1l11lllll11_opy_ = hub_url
            bstack1lll11lll1l_opy_.bstack1lllll1l111_opy_(instance, bstack1lll11lll1l_opy_.bstack1l1l11l111l_opy_, hub_url)
            bstack1lll11lll1l_opy_.bstack1lllll1l111_opy_(
                instance, bstack1lll11lll1l_opy_.bstack1l11l1ll11l_opy_, bstack1lll11lll1l_opy_.bstack1ll11111l1l_opy_(hub_url)
            )
        return result
    @staticmethod
    def bstack1l11l11l1l1_opy_(bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_]):
        return bstack1l1ll_opy_ (u"ࠣ࠼ࠥᖍ").join((bstack1lllll1lll1_opy_(bstack1llllllll11_opy_[0]).name, bstack1llll1lllll_opy_(bstack1llllllll11_opy_[1]).name))
    @staticmethod
    def bstack1ll111ll111_opy_(bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_], callback: Callable):
        bstack1l11l11lll1_opy_ = bstack1lll11lll1l_opy_.bstack1l11l11l1l1_opy_(bstack1llllllll11_opy_)
        if not bstack1l11l11lll1_opy_ in bstack1lll11lll1l_opy_.bstack11llll1l11l_opy_:
            bstack1lll11lll1l_opy_.bstack11llll1l11l_opy_[bstack1l11l11lll1_opy_] = []
        bstack1lll11lll1l_opy_.bstack11llll1l11l_opy_[bstack1l11l11lll1_opy_].append(callback)
    def bstack1llll1l1lll_opy_(self, instance: bstack1llll1ll1l1_opy_, method_name: str, bstack1lllllll111_opy_: timedelta, *args, **kwargs):
        if not instance or method_name in (bstack1l1ll_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࠤᖎ")):
            return
        cmd = args[0] if method_name == bstack1l1ll_opy_ (u"ࠥࡩࡽ࡫ࡣࡶࡶࡨࠦᖏ") and args and type(args) in [list, tuple] and isinstance(args[0], str) else None
        bstack11llll1l1ll_opy_ = bstack1l1ll_opy_ (u"ࠦ࠿ࠨᖐ").join(map(str, filter(None, [method_name, cmd])))
        instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶ࠿ࠨᖑ") + bstack11llll1l1ll_opy_, bstack1lllllll111_opy_)
    def bstack1lllll1llll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable[..., Any]:
        instance, method_name = exec
        bstack1lllllll1l1_opy_, bstack1l11l11l1ll_opy_ = bstack1llllllll11_opy_
        bstack1l11l11lll1_opy_ = bstack1lll11lll1l_opy_.bstack1l11l11l1l1_opy_(bstack1llllllll11_opy_)
        self.logger.debug(bstack1l1ll_opy_ (u"ࠨ࡯࡯ࡡ࡫ࡳࡴࡱ࠺ࠡ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࡃࡻ࡮ࡧࡷ࡬ࡴࡪ࡟࡯ࡣࡰࡩࢂࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨᖒ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠢࠣᖓ"))
        if bstack1lllllll1l1_opy_ == bstack1lllll1lll1_opy_.QUIT:
            if bstack1l11l11l1ll_opy_ == bstack1llll1lllll_opy_.PRE:
                bstack1ll1l11l11l_opy_ = bstack1llll11l1l1_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack11111ll1_opy_.value)
                bstack11111111l1_opy_.bstack1lllll1l111_opy_(instance, EVENTS.bstack11111ll1_opy_.value, bstack1ll1l11l11l_opy_)
                self.logger.debug(bstack1l1ll_opy_ (u"ࠣ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡀࡿࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࡁࢀࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࢁࠥ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࢁࠧᖔ").format(instance, method_name, bstack1lllllll1l1_opy_, bstack1l11l11l1ll_opy_))
        if bstack1lllllll1l1_opy_ == bstack1lllll1lll1_opy_.bstack1llllll111l_opy_:
            if bstack1l11l11l1ll_opy_ == bstack1llll1lllll_opy_.POST and not bstack1lll11lll1l_opy_.bstack1l1l11l1l1l_opy_ in instance.data:
                session_id = getattr(target, bstack1l1ll_opy_ (u"ࠤࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠨᖕ"), None)
                if session_id:
                    instance.data[bstack1lll11lll1l_opy_.bstack1l1l11l1l1l_opy_] = session_id
        elif (
            bstack1lllllll1l1_opy_ == bstack1lllll1lll1_opy_.bstack1lllll11l1l_opy_
            and bstack1lll11lll1l_opy_.bstack1l11ll111l1_opy_(*args) == bstack1lll11lll1l_opy_.bstack1l11ll1llll_opy_
        ):
            if bstack1l11l11l1ll_opy_ == bstack1llll1lllll_opy_.PRE:
                hub_url = bstack1lll11lll1l_opy_.bstack11ll1l1l1l_opy_(target)
                if hub_url:
                    instance.data.update(
                        {
                            bstack1lll11lll1l_opy_.bstack1l1l11l111l_opy_: hub_url,
                            bstack1lll11lll1l_opy_.bstack1l11l1ll11l_opy_: bstack1lll11lll1l_opy_.bstack1ll11111l1l_opy_(hub_url),
                            bstack1lll11lll1l_opy_.bstack1ll111l111l_opy_: int(
                                os.environ.get(bstack1l1ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠥᖖ"), str(self.platform_index))
                            ),
                        }
                    )
                bstack1ll11111ll1_opy_ = bstack1lll11lll1l_opy_.bstack1ll111111l1_opy_(*args)
                bstack11llll1ll11_opy_ = bstack1ll11111ll1_opy_.get(bstack1l1ll_opy_ (u"ࠦࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠥᖗ"), None) if bstack1ll11111ll1_opy_ else None
                if isinstance(bstack11llll1ll11_opy_, dict):
                    instance.data[bstack1lll11lll1l_opy_.bstack11lllll1111_opy_] = copy.deepcopy(bstack11llll1ll11_opy_)
                    instance.data[bstack1lll11lll1l_opy_.bstack1l1l11l1lll_opy_] = bstack11llll1ll11_opy_
            elif bstack1l11l11l1ll_opy_ == bstack1llll1lllll_opy_.POST:
                if isinstance(result, dict):
                    framework_session_id = result.get(bstack1l1ll_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࠦᖘ"), dict()).get(bstack1l1ll_opy_ (u"ࠨࡳࡦࡵࡶ࡭ࡴࡴࡉࡥࠤᖙ"), None)
                    if framework_session_id:
                        instance.data.update(
                            {
                                bstack1lll11lll1l_opy_.bstack1l1l11l1l1l_opy_: framework_session_id,
                                bstack1lll11lll1l_opy_.bstack11llll1l111_opy_: datetime.now(tz=timezone.utc),
                            }
                        )
        elif (
            bstack1lllllll1l1_opy_ == bstack1lllll1lll1_opy_.bstack1lllll11l1l_opy_
            and bstack1lll11lll1l_opy_.bstack1l11ll111l1_opy_(*args) == bstack1lll11lll1l_opy_.bstack11llll1lll1_opy_
            and bstack1l11l11l1ll_opy_ == bstack1llll1lllll_opy_.POST
        ):
            instance.data[bstack1lll11lll1l_opy_.bstack11lllll111l_opy_] = datetime.now(tz=timezone.utc)
        if bstack1l11l11lll1_opy_ in bstack1lll11lll1l_opy_.bstack11llll1l11l_opy_:
            bstack1l11l1l11ll_opy_ = None
            for callback in bstack1lll11lll1l_opy_.bstack11llll1l11l_opy_[bstack1l11l11lll1_opy_]:
                try:
                    bstack1l11l11ll11_opy_ = callback(self, target, exec, bstack1llllllll11_opy_, result, *args, **kwargs)
                    if bstack1l11l1l11ll_opy_ == None:
                        bstack1l11l1l11ll_opy_ = bstack1l11l11ll11_opy_
                except Exception as e:
                    self.logger.error(bstack1l1ll_opy_ (u"ࠢࡦࡴࡵࡳࡷࠦࡩ࡯ࡸࡲ࡯࡮ࡴࡧࠡࡥࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࠧᖚ") + str(e) + bstack1l1ll_opy_ (u"ࠣࠤᖛ"))
                    traceback.print_exc()
            if bstack1lllllll1l1_opy_ == bstack1lllll1lll1_opy_.QUIT:
                if bstack1l11l11l1ll_opy_ == bstack1llll1lllll_opy_.POST:
                    bstack1ll1l11l11l_opy_ = bstack11111111l1_opy_.bstack1lllll111ll_opy_(instance, EVENTS.bstack11111ll1_opy_.value)
                    if bstack1ll1l11l11l_opy_!=None:
                        bstack1llll11l1l1_opy_.end(EVENTS.bstack11111ll1_opy_.value, bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᖜ"), bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᖝ"), True, None)
            if bstack1l11l11l1ll_opy_ == bstack1llll1lllll_opy_.PRE and callable(bstack1l11l1l11ll_opy_):
                return bstack1l11l1l11ll_opy_
            elif bstack1l11l11l1ll_opy_ == bstack1llll1lllll_opy_.POST and bstack1l11l1l11ll_opy_:
                return bstack1l11l1l11ll_opy_
    def bstack1llllll1l11_opy_(
        self, method_name, previous_state: bstack1lllll1lll1_opy_, *args, **kwargs
    ) -> bstack1lllll1lll1_opy_:
        if method_name == bstack1l1ll_opy_ (u"ࠦࡤࡥࡩ࡯࡫ࡷࡣࡤࠨᖞ") or method_name == bstack1l1ll_opy_ (u"ࠧࡹࡴࡢࡴࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠧᖟ"):
            return bstack1lllll1lll1_opy_.bstack1llllll111l_opy_
        if method_name == bstack1l1ll_opy_ (u"ࠨࡱࡶ࡫ࡷࠦᖠ"):
            return bstack1lllll1lll1_opy_.QUIT
        if method_name == bstack1l1ll_opy_ (u"ࠢࡦࡺࡨࡧࡺࡺࡥࠣᖡ"):
            if previous_state != bstack1lllll1lll1_opy_.NONE:
                bstack1ll1l1111ll_opy_ = bstack1lll11lll1l_opy_.bstack1l11ll111l1_opy_(*args)
                if bstack1ll1l1111ll_opy_ == bstack1lll11lll1l_opy_.bstack1l11ll1llll_opy_:
                    return bstack1lllll1lll1_opy_.bstack1llllll111l_opy_
            return bstack1lllll1lll1_opy_.bstack1lllll11l1l_opy_
        return bstack1lllll1lll1_opy_.NONE