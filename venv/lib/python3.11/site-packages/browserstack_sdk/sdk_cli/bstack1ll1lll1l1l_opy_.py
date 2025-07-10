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
class bstack1ll1lllll11_opy_(bstack11111111l1_opy_):
    bstack1l11l1l111l_opy_ = bstack1l1ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠥ᐀")
    bstack1l1l11l1l1l_opy_ = bstack1l1ll_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠦᐁ")
    bstack1l1l11l111l_opy_ = bstack1l1ll_opy_ (u"ࠧ࡮ࡵࡣࡡࡸࡶࡱࠨᐂ")
    bstack1l1l11l1lll_opy_ = bstack1l1ll_opy_ (u"ࠨࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠧᐃ")
    bstack1l11l11ll1l_opy_ = bstack1l1ll_opy_ (u"ࠢࡸ࠵ࡦࡩࡽ࡫ࡣࡶࡶࡨࡷࡨࡸࡩࡱࡶࠥᐄ")
    bstack1l11l1l11l1_opy_ = bstack1l1ll_opy_ (u"ࠣࡹ࠶ࡧࡪࡾࡥࡤࡷࡷࡩࡸࡩࡲࡪࡲࡷࡥࡸࡿ࡮ࡤࠤᐅ")
    NAME = bstack1l1ll_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨᐆ")
    bstack1l11l11llll_opy_: Dict[str, List[Callable]] = dict()
    platform_index: int
    options: Any
    desired_capabilities: Any
    bstack1lll1l11l11_opy_: Any
    bstack1l11l1l1111_opy_: Dict
    def __init__(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
        methods=[bstack1l1ll_opy_ (u"ࠥࡰࡦࡻ࡮ࡤࡪࠥᐇ"), bstack1l1ll_opy_ (u"ࠦࡨࡵ࡮࡯ࡧࡦࡸࠧᐈ"), bstack1l1ll_opy_ (u"ࠧࡴࡥࡸࡡࡳࡥ࡬࡫ࠢᐉ"), bstack1l1ll_opy_ (u"ࠨࡣ࡭ࡱࡶࡩࠧᐊ"), bstack1l1ll_opy_ (u"ࠢࡥ࡫ࡶࡴࡦࡺࡣࡩࠤᐋ")],
    ):
        super().__init__(
            framework_name,
            framework_version,
            classes,
        )
        self.platform_index = platform_index
        self.bstack1llllll11l1_opy_(methods)
    def bstack1llll1l1lll_opy_(self, instance: bstack1llll1ll1l1_opy_, method_name: str, bstack1lllllll111_opy_: timedelta, *args, **kwargs):
        pass
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
        bstack1l11l11lll1_opy_ = bstack1ll1lllll11_opy_.bstack1l11l11l1l1_opy_(bstack1llllllll11_opy_)
        if bstack1l11l11lll1_opy_ in bstack1ll1lllll11_opy_.bstack1l11l11llll_opy_:
            bstack1l11l1l11ll_opy_ = None
            for callback in bstack1ll1lllll11_opy_.bstack1l11l11llll_opy_[bstack1l11l11lll1_opy_]:
                try:
                    bstack1l11l11ll11_opy_ = callback(self, target, exec, bstack1llllllll11_opy_, result, *args, **kwargs)
                    if bstack1l11l1l11ll_opy_ == None:
                        bstack1l11l1l11ll_opy_ = bstack1l11l11ll11_opy_
                except Exception as e:
                    self.logger.error(bstack1l1ll_opy_ (u"ࠣࡧࡵࡶࡴࡸࠠࡪࡰࡹࡳࡰ࡯࡮ࡨࠢࡦࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࠨᐌ") + str(e) + bstack1l1ll_opy_ (u"ࠤࠥᐍ"))
                    traceback.print_exc()
            if bstack1l11l11l1ll_opy_ == bstack1llll1lllll_opy_.PRE and callable(bstack1l11l1l11ll_opy_):
                return bstack1l11l1l11ll_opy_
            elif bstack1l11l11l1ll_opy_ == bstack1llll1lllll_opy_.POST and bstack1l11l1l11ll_opy_:
                return bstack1l11l1l11ll_opy_
    def bstack1llllll1l11_opy_(
        self, method_name, previous_state: bstack1lllll1lll1_opy_, *args, **kwargs
    ) -> bstack1lllll1lll1_opy_:
        if method_name == bstack1l1ll_opy_ (u"ࠪࡰࡦࡻ࡮ࡤࡪࠪᐎ") or method_name == bstack1l1ll_opy_ (u"ࠫࡨࡵ࡮࡯ࡧࡦࡸࠬᐏ") or method_name == bstack1l1ll_opy_ (u"ࠬࡴࡥࡸࡡࡳࡥ࡬࡫ࠧᐐ"):
            return bstack1lllll1lll1_opy_.bstack1llllll111l_opy_
        if method_name == bstack1l1ll_opy_ (u"࠭ࡤࡪࡵࡳࡥࡹࡩࡨࠨᐑ"):
            return bstack1lllll1lll1_opy_.bstack1lllll11ll1_opy_
        if method_name == bstack1l1ll_opy_ (u"ࠧࡤ࡮ࡲࡷࡪ࠭ᐒ"):
            return bstack1lllll1lll1_opy_.QUIT
        return bstack1lllll1lll1_opy_.NONE
    @staticmethod
    def bstack1l11l11l1l1_opy_(bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_]):
        return bstack1l1ll_opy_ (u"ࠣ࠼ࠥᐓ").join((bstack1lllll1lll1_opy_(bstack1llllllll11_opy_[0]).name, bstack1llll1lllll_opy_(bstack1llllllll11_opy_[1]).name))
    @staticmethod
    def bstack1ll111ll111_opy_(bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_], callback: Callable):
        bstack1l11l11lll1_opy_ = bstack1ll1lllll11_opy_.bstack1l11l11l1l1_opy_(bstack1llllllll11_opy_)
        if not bstack1l11l11lll1_opy_ in bstack1ll1lllll11_opy_.bstack1l11l11llll_opy_:
            bstack1ll1lllll11_opy_.bstack1l11l11llll_opy_[bstack1l11l11lll1_opy_] = []
        bstack1ll1lllll11_opy_.bstack1l11l11llll_opy_[bstack1l11l11lll1_opy_].append(callback)
    @staticmethod
    def bstack1ll1l111ll1_opy_(method_name: str):
        return True
    @staticmethod
    def bstack1ll111ll1ll_opy_(method_name: str, *args) -> bool:
        return True
    @staticmethod
    def bstack1ll11ll11ll_opy_(instance: bstack1llll1ll1l1_opy_, default_value=None):
        return bstack11111111l1_opy_.bstack1lllll111ll_opy_(instance, bstack1ll1lllll11_opy_.bstack1l1l11l1lll_opy_, default_value)
    @staticmethod
    def bstack1l1llll1ll1_opy_(instance: bstack1llll1ll1l1_opy_) -> bool:
        return True
    @staticmethod
    def bstack1ll1l11l111_opy_(instance: bstack1llll1ll1l1_opy_, default_value=None):
        return bstack11111111l1_opy_.bstack1lllll111ll_opy_(instance, bstack1ll1lllll11_opy_.bstack1l1l11l111l_opy_, default_value)
    @staticmethod
    def bstack1ll11ll1111_opy_(*args):
        return args[0] if args and type(args) in [list, tuple] and isinstance(args[0], str) else None
    @staticmethod
    def bstack1ll1l111lll_opy_(method_name: str, *args):
        if not bstack1ll1lllll11_opy_.bstack1ll1l111ll1_opy_(method_name):
            return False
        if not bstack1ll1lllll11_opy_.bstack1l11l11ll1l_opy_ in bstack1ll1lllll11_opy_.bstack1l11ll111l1_opy_(*args):
            return False
        bstack1ll11111ll1_opy_ = bstack1ll1lllll11_opy_.bstack1ll111111l1_opy_(*args)
        return bstack1ll11111ll1_opy_ and bstack1l1ll_opy_ (u"ࠤࡶࡧࡷ࡯ࡰࡵࠤᐔ") in bstack1ll11111ll1_opy_ and bstack1l1ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵࠦᐕ") in bstack1ll11111ll1_opy_[bstack1l1ll_opy_ (u"ࠦࡸࡩࡲࡪࡲࡷࠦᐖ")]
    @staticmethod
    def bstack1ll11ll1l1l_opy_(method_name: str, *args):
        if not bstack1ll1lllll11_opy_.bstack1ll1l111ll1_opy_(method_name):
            return False
        if not bstack1ll1lllll11_opy_.bstack1l11l11ll1l_opy_ in bstack1ll1lllll11_opy_.bstack1l11ll111l1_opy_(*args):
            return False
        bstack1ll11111ll1_opy_ = bstack1ll1lllll11_opy_.bstack1ll111111l1_opy_(*args)
        return (
            bstack1ll11111ll1_opy_
            and bstack1l1ll_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࠧᐗ") in bstack1ll11111ll1_opy_
            and bstack1l1ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡧࡷ࡯ࡰࡵࠤᐘ") in bstack1ll11111ll1_opy_[bstack1l1ll_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࠢᐙ")]
        )
    @staticmethod
    def bstack1l11ll111l1_opy_(*args):
        return str(bstack1ll1lllll11_opy_.bstack1ll11ll1111_opy_(*args)).lower()