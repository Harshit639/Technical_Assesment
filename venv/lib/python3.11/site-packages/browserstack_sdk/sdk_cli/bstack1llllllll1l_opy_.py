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
from enum import Enum
from typing import Dict, Tuple, Callable, Type, List, Any
import abc
from datetime import datetime, timezone, timedelta
from browserstack_sdk.sdk_cli.bstack1lllll1l1l1_opy_ import bstack1lllll1111l_opy_, bstack1111111l11_opy_
import os
import threading
class bstack1llll1lllll_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1l1ll_opy_ (u"ࠢࡉࡱࡲ࡯ࡘࡺࡡࡵࡧ࠱ࡿࢂࠨႋ").format(self.name)
class bstack1lllll1lll1_opy_(Enum):
    NONE = 0
    bstack1llllll111l_opy_ = 1
    bstack1lllll11ll1_opy_ = 3
    bstack1lllll11l1l_opy_ = 4
    bstack1llll1ll11l_opy_ = 5
    QUIT = 6
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __repr__(self) -> str:
        return bstack1l1ll_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡓࡵࡣࡷࡩ࠳ࢁࡽࠣႌ").format(self.name)
class bstack1llll1ll1l1_opy_(bstack1lllll1111l_opy_):
    framework_name: str
    framework_version: str
    state: bstack1lllll1lll1_opy_
    previous_state: bstack1lllll1lll1_opy_
    bstack1lllll1l1ll_opy_: datetime
    bstack1llllll1lll_opy_: datetime
    def __init__(
        self,
        context: bstack1111111l11_opy_,
        framework_name: str,
        framework_version: str,
        state=bstack1lllll1lll1_opy_.NONE,
    ):
        super().__init__(context)
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.state = state
        self.previous_state = bstack1lllll1lll1_opy_.NONE
        self.bstack1lllll1l1ll_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1llllll1lll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1lllll1l111_opy_(self, bstack1lllll1ll11_opy_: bstack1lllll1lll1_opy_):
        bstack1llllll1l1l_opy_ = bstack1lllll1lll1_opy_(bstack1lllll1ll11_opy_).name
        if not bstack1llllll1l1l_opy_:
            return False
        if bstack1lllll1ll11_opy_ == self.state:
            return False
        if self.state == bstack1lllll1lll1_opy_.bstack1lllll11ll1_opy_: # bstack1llll1lll11_opy_ bstack111111111l_opy_ for bstack1llllll11ll_opy_ in bstack1llllll1ll1_opy_, it bstack1llll1llll1_opy_ bstack1lllll11111_opy_ bstack1111111l1l_opy_ times bstack1llll1ll1ll_opy_ a new state
            return True
        if (
            bstack1lllll1ll11_opy_ == bstack1lllll1lll1_opy_.NONE
            or (self.state != bstack1lllll1lll1_opy_.NONE and bstack1lllll1ll11_opy_ == bstack1lllll1lll1_opy_.bstack1llllll111l_opy_)
            or (self.state < bstack1lllll1lll1_opy_.bstack1llllll111l_opy_ and bstack1lllll1ll11_opy_ == bstack1lllll1lll1_opy_.bstack1lllll11l1l_opy_)
            or (self.state < bstack1lllll1lll1_opy_.bstack1llllll111l_opy_ and bstack1lllll1ll11_opy_ == bstack1lllll1lll1_opy_.QUIT)
        ):
            raise ValueError(bstack1l1ll_opy_ (u"ࠤ࡬ࡲࡻࡧ࡬ࡪࡦࠣࡷࡹࡧࡴࡦࠢࡷࡶࡦࡴࡳࡪࡶ࡬ࡳࡳࡀႍࠠࠣ") + str(self.state) + bstack1l1ll_opy_ (u"ࠥࠤࡂࡄࠠࠣႎ") + str(bstack1lllll1ll11_opy_))
        self.previous_state = self.state
        self.state = bstack1lllll1ll11_opy_
        self.bstack1llllll1lll_opy_ = datetime.now(tz=timezone.utc)
        return True
class bstack11111111l1_opy_(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1llllllllll_opy_: Dict[str, bstack1llll1ll1l1_opy_] = dict()
    framework_name: str
    framework_version: str
    classes: List[Type]
    def __init__(
        self,
        framework_name: str,
        framework_version: str,
        classes: List[Type],
    ):
        self.framework_name = framework_name
        self.framework_version = framework_version
        self.classes = classes
    @abc.abstractmethod
    def bstack1llll1l1lll_opy_(self, instance: bstack1llll1ll1l1_opy_, method_name: str, bstack1lllllll111_opy_: timedelta, *args, **kwargs):
        return
    @abc.abstractmethod
    def bstack1llllll1l11_opy_(
        self, method_name, previous_state: bstack1lllll1lll1_opy_, *args, **kwargs
    ) -> bstack1lllll1lll1_opy_:
        return
    @abc.abstractmethod
    def bstack1lllll1llll_opy_(
        self,
        target: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        bstack1llllllll11_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ) -> Callable:
        return
    def bstack1llllll11l1_opy_(self, bstack11111111ll_opy_: List[str]):
        for clazz in self.classes:
            for method_name in bstack11111111ll_opy_:
                bstack1lllll11lll_opy_ = getattr(clazz, method_name, None)
                if not callable(bstack1lllll11lll_opy_):
                    self.logger.warning(bstack1l1ll_opy_ (u"ࠦࡺࡴࡰࡢࡶࡦ࡬ࡪࡪࠠ࡮ࡧࡷ࡬ࡴࡪ࠺ࠡࠤႏ") + str(method_name) + bstack1l1ll_opy_ (u"ࠧࠨ႐"))
                    continue
                bstack1lllllll1l1_opy_ = self.bstack1llllll1l11_opy_(
                    method_name, previous_state=bstack1lllll1lll1_opy_.NONE
                )
                bstack1llllll1111_opy_ = self.bstack1llll1ll111_opy_(
                    method_name,
                    (bstack1lllllll1l1_opy_ if bstack1lllllll1l1_opy_ else bstack1lllll1lll1_opy_.NONE),
                    bstack1lllll11lll_opy_,
                )
                if not callable(bstack1llllll1111_opy_):
                    self.logger.warning(bstack1l1ll_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࠦ࡮ࡰࡶࠣࡴࡦࡺࡣࡩࡧࡧ࠾ࠥࢁ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࢁࠥ࠮ࡻࡴࡧ࡯ࡪ࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࢃ࠺ࠡࠤ႑") + str(self.framework_version) + bstack1l1ll_opy_ (u"ࠢࠪࠤ႒"))
                    continue
                setattr(clazz, method_name, bstack1llllll1111_opy_)
    def bstack1llll1ll111_opy_(
        self,
        method_name: str,
        bstack1lllllll1l1_opy_: bstack1lllll1lll1_opy_,
        bstack1lllll11lll_opy_: Callable,
    ):
        def wrapped(target, *args, **kwargs):
            bstack11l1l1111_opy_ = datetime.now()
            (bstack1lllllll1l1_opy_,) = wrapped.__vars__
            bstack1lllllll1l1_opy_ = (
                bstack1lllllll1l1_opy_
                if bstack1lllllll1l1_opy_ and bstack1lllllll1l1_opy_ != bstack1lllll1lll1_opy_.NONE
                else self.bstack1llllll1l11_opy_(method_name, previous_state=bstack1lllllll1l1_opy_, *args, **kwargs)
            )
            if bstack1lllllll1l1_opy_ == bstack1lllll1lll1_opy_.bstack1llllll111l_opy_:
                ctx = bstack1lllll1111l_opy_.create_context(self.bstack1111111111_opy_(target))
                if not self.bstack1lllllll1ll_opy_() or ctx.id not in bstack11111111l1_opy_.bstack1llllllllll_opy_:
                    bstack11111111l1_opy_.bstack1llllllllll_opy_[ctx.id] = bstack1llll1ll1l1_opy_(
                        ctx, self.framework_name, self.framework_version, bstack1lllllll1l1_opy_
                    )
                self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡹࡵࡥࡵࡶࡥࡥࠢࡰࡩࡹ࡮࡯ࡥࠢࡦࡶࡪࡧࡴࡦࡦ࠽ࠤࢀࡺࡡࡳࡩࡨࡸ࠳ࡥ࡟ࡤ࡮ࡤࡷࡸࡥ࡟ࡾࠢࡰࡩࡹ࡮࡯ࡥࡡࡱࡥࡲ࡫࠽ࡼ࡯ࡨࡸ࡭ࡵࡤࡠࡰࡤࡱࡪࢃࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡷࡹࡧࡴࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࢂࠦࡣࡵࡺࡀࡿࡨࡺࡸ࠯࡫ࡧࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤ႓") + str(bstack11111111l1_opy_.bstack1llllllllll_opy_.keys()) + bstack1l1ll_opy_ (u"ࠤࠥ႔"))
            else:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡻࡷࡧࡰࡱࡧࡧࠤࡲ࡫ࡴࡩࡱࡧࠤ࡮ࡴࡶࡰ࡭ࡨࡨ࠿ࠦࡻࡵࡣࡵ࡫ࡪࡺ࠮ࡠࡡࡦࡰࡦࡹࡳࡠࡡࢀࠤࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦ࠿ࡾࡱࡪࡺࡨࡰࡦࡢࡲࡦࡳࡥࡾࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡹࡴࡢࡶࡨࡁࢀ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࡽࠡ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡶࡁࠧ႕") + str(bstack11111111l1_opy_.bstack1llllllllll_opy_.keys()) + bstack1l1ll_opy_ (u"ࠦࠧ႖"))
            instance = bstack11111111l1_opy_.bstack1lllll1l11l_opy_(self.bstack1111111111_opy_(target))
            if bstack1lllllll1l1_opy_ == bstack1lllll1lll1_opy_.NONE or not instance:
                ctx = bstack1lllll1111l_opy_.create_context(self.bstack1111111111_opy_(target))
                self.logger.warning(bstack1l1ll_opy_ (u"ࠧࡽࡲࡢࡲࡳࡩࡩࠦ࡭ࡦࡶ࡫ࡳࡩࠦࡵ࡯ࡶࡵࡥࡨࡱࡥࡥ࠼ࠣࡿࡲ࡫ࡴࡩࡱࡧࡣࡳࡧ࡭ࡦࡿࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡳࡵࡣࡷࡩࡂࢁࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥࡾࠢࡦࡸࡽࡃࡻࡤࡶࡻࢁࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳ࠾ࠤ႗") + str(bstack11111111l1_opy_.bstack1llllllllll_opy_.keys()) + bstack1l1ll_opy_ (u"ࠨࠢ႘"))
                return bstack1lllll11lll_opy_(target, *args, **kwargs)
            bstack1lllll1ll1l_opy_ = self.bstack1lllll1llll_opy_(
                target,
                (instance, method_name),
                (bstack1lllllll1l1_opy_, bstack1llll1lllll_opy_.PRE),
                None,
                *args,
                **kwargs,
            )
            if instance.bstack1lllll1l111_opy_(bstack1lllllll1l1_opy_):
                self.logger.debug(bstack1l1ll_opy_ (u"ࠢࡢࡲࡳࡰ࡮࡫ࡤࠡࡵࡷࡥࡹ࡫࠭ࡵࡴࡤࡲࡸ࡯ࡴࡪࡱࡱ࠾ࠥࢁࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࡲࡵࡩࡻ࡯࡯ࡶࡵࡢࡷࡹࡧࡴࡦࡿࠣࡁࡃࠦࡻࡪࡰࡶࡸࡦࡴࡣࡦ࠰ࡶࡸࡦࡺࡥࡾࠢࠫࡿࡹࡿࡰࡦࠪࡷࡥࡷ࡭ࡥࡵࠫࢀ࠲ࢀࡳࡥࡵࡪࡲࡨࡤࡴࡡ࡮ࡧࢀࠤࢀࡧࡲࡨࡵࢀ࠭ࠥࡡࠢ႙") + str(instance.ref()) + bstack1l1ll_opy_ (u"ࠣ࡟ࠥႚ"))
            result = (
                bstack1lllll1ll1l_opy_(target, bstack1lllll11lll_opy_, *args, **kwargs)
                if callable(bstack1lllll1ll1l_opy_)
                else bstack1lllll11lll_opy_(target, *args, **kwargs)
            )
            bstack1lllll111l1_opy_ = self.bstack1lllll1llll_opy_(
                target,
                (instance, method_name),
                (bstack1lllllll1l1_opy_, bstack1llll1lllll_opy_.POST),
                result,
                *args,
                **kwargs,
            )
            self.bstack1llll1l1lll_opy_(instance, method_name, datetime.now() - bstack11l1l1111_opy_, *args, **kwargs)
            return bstack1lllll111l1_opy_ if bstack1lllll111l1_opy_ else result
        wrapped.__name__ = method_name
        wrapped.__vars__ = (bstack1lllllll1l1_opy_,)
        return wrapped
    @staticmethod
    def bstack1lllll1l11l_opy_(target: object, strict=True):
        ctx = bstack1lllll1111l_opy_.create_context(target)
        instance = bstack11111111l1_opy_.bstack1llllllllll_opy_.get(ctx.id, None)
        if instance and instance.bstack1lllllll11l_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1lllll11l11_opy_(
        ctx: bstack1111111l11_opy_, state: bstack1lllll1lll1_opy_, reverse=True
    ) -> List[bstack1llll1ll1l1_opy_]:
        return sorted(
            filter(
                lambda t: t.state == state
                and t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                bstack11111111l1_opy_.bstack1llllllllll_opy_.values(),
            ),
            key=lambda t: t.bstack1lllll1l1ll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllllllll1_opy_(instance: bstack1llll1ll1l1_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def bstack1lllll111ll_opy_(instance: bstack1llll1ll1l1_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1lllll1l111_opy_(instance: bstack1llll1ll1l1_opy_, key: str, value: Any) -> bool:
        instance.data[key] = value
        bstack11111111l1_opy_.logger.debug(bstack1l1ll_opy_ (u"ࠤࡶࡩࡹࡥࡳࡵࡣࡷࡩ࠿ࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠾ࡽ࡬ࡲࡸࡺࡡ࡯ࡥࡨ࠲ࡷ࡫ࡦࠩࠫࢀࠤࡰ࡫ࡹ࠾ࡽ࡮ࡩࡾࢃࠠࡷࡣ࡯ࡹࡪࡃࠢႛ") + str(value) + bstack1l1ll_opy_ (u"ࠥࠦႜ"))
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = bstack11111111l1_opy_.bstack1lllll1l11l_opy_(target, strict)
        return bstack11111111l1_opy_.bstack1lllll111ll_opy_(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = bstack11111111l1_opy_.bstack1lllll1l11l_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    def bstack1lllllll1ll_opy_(self):
        return self.framework_name == bstack1l1ll_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨႝ")
    def bstack1111111111_opy_(self, target):
        return target if not self.bstack1lllllll1ll_opy_() else self.bstack1llll1lll1l_opy_()
    @staticmethod
    def bstack1llll1lll1l_opy_():
        return str(os.getpid()) + str(threading.get_ident())