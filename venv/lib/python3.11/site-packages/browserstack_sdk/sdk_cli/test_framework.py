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
import os
import threading
import traceback
from typing import Dict, List, Any, Callable, Tuple, Union
import abc
from datetime import datetime, timezone
from dataclasses import dataclass
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import bstack111111l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lllll1l1l1_opy_ import bstack1lllll1111l_opy_, bstack1111111l11_opy_
class bstack1lll1111lll_opy_(Enum):
    PRE = 0
    POST = 1
    def __repr__(self) -> str:
        return bstack1l1ll_opy_ (u"ࠣࡖࡨࡷࡹࡎ࡯ࡰ࡭ࡖࡸࡦࡺࡥ࠯ࡽࢀࠦᖢ").format(self.name)
class bstack1llll11ll11_opy_(Enum):
    NONE = 0
    BEFORE_ALL = 1
    LOG = 2
    SETUP_FIXTURE = 3
    INIT_TEST = 4
    BEFORE_EACH = 5
    AFTER_EACH = 6
    TEST = 7
    STEP = 8
    LOG_REPORT = 9
    AFTER_ALL = 10
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
    def __repr__(self) -> str:
        return bstack1l1ll_opy_ (u"ࠤࡗࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡕࡷࡥࡹ࡫࠮ࡼࡿࠥᖣ").format(self.name)
class bstack1lll1ll1111_opy_(bstack1lllll1111l_opy_):
    bstack1ll1l111111_opy_: List[str]
    bstack1l111l1ll1l_opy_: Dict[str, str]
    state: bstack1llll11ll11_opy_
    bstack1lllll1l1ll_opy_: datetime
    bstack1llllll1lll_opy_: datetime
    def __init__(
        self,
        context: bstack1111111l11_opy_,
        bstack1ll1l111111_opy_: List[str],
        bstack1l111l1ll1l_opy_: Dict[str, str],
        state=bstack1llll11ll11_opy_.NONE,
    ):
        super().__init__(context)
        self.bstack1ll1l111111_opy_ = bstack1ll1l111111_opy_
        self.bstack1l111l1ll1l_opy_ = bstack1l111l1ll1l_opy_
        self.state = state
        self.bstack1lllll1l1ll_opy_ = datetime.now(tz=timezone.utc)
        self.bstack1llllll1lll_opy_ = datetime.now(tz=timezone.utc)
    def bstack1lllll1l111_opy_(self, bstack1lllll1ll11_opy_: bstack1llll11ll11_opy_):
        bstack1llllll1l1l_opy_ = bstack1llll11ll11_opy_(bstack1lllll1ll11_opy_).name
        if not bstack1llllll1l1l_opy_:
            return False
        if bstack1lllll1ll11_opy_ == self.state:
            return False
        self.state = bstack1lllll1ll11_opy_
        self.bstack1llllll1lll_opy_ = datetime.now(tz=timezone.utc)
        return True
@dataclass
class bstack1l111lll1ll_opy_:
    test_framework_name: str
    test_framework_version: str
    platform_index: int
@dataclass
class bstack1llll11llll_opy_:
    kind: str
    message: str
    level: Union[None, str] = None
    timestamp: Union[None, datetime] = datetime.now(tz=timezone.utc)
    fileName: str = None
    bstack1l1l1ll1l11_opy_: int = None
    bstack1l1lll11l1l_opy_: str = None
    bstack1l1l1l1_opy_: str = None
    bstack1l1l1llll1_opy_: str = None
    bstack1l1l1ll1lll_opy_: str = None
    bstack1l1111l111l_opy_: str = None
class TestFramework(abc.ABC):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    bstack1ll11l111l1_opy_ = bstack1l1ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡷࡸ࡭ࡩࠨᖤ")
    bstack1l111l111ll_opy_ = bstack1l1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡ࡬ࡨࠧᖥ")
    bstack1ll111l11ll_opy_ = bstack1l1ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡲࡦࡳࡥࠣᖦ")
    bstack1l1111lll11_opy_ = bstack1l1ll_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡡࡳࡥࡹ࡮ࠢᖧ")
    bstack1l111ll11ll_opy_ = bstack1l1ll_opy_ (u"ࠢࡵࡧࡶࡸࡤࡺࡡࡨࡵࠥᖨ")
    bstack1l1l111l1ll_opy_ = bstack1l1ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡦࡵࡸࡰࡹࠨᖩ")
    bstack1l1lll11111_opy_ = bstack1l1ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡧࡶࡹࡱࡺ࡟ࡢࡶࠥᖪ")
    bstack1l1lll111ll_opy_ = bstack1l1ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠧᖫ")
    bstack1l1ll1ll1ll_opy_ = bstack1l1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡨࡲࡩ࡫ࡤࡠࡣࡷࠦᖬ")
    bstack1l11l11111l_opy_ = bstack1l1ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡰࡴࡩࡡࡵ࡫ࡲࡲࠧᖭ")
    bstack1ll11llll11_opy_ = bstack1l1ll_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࠧᖮ")
    bstack1l1ll1ll11l_opy_ = bstack1l1ll_opy_ (u"ࠢࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠤᖯ")
    bstack11llllll111_opy_ = bstack1l1ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡣࡰࡦࡨࠦᖰ")
    bstack1l1l1l1l111_opy_ = bstack1l1ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡧࡵࡹࡳࡥ࡮ࡢ࡯ࡨࠦᖱ")
    bstack1ll111l111l_opy_ = bstack1l1ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࠦᖲ")
    bstack1l1l11111l1_opy_ = bstack1l1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡩࡥ࡮ࡲࡵࡳࡧࠥᖳ")
    bstack1l111l111l1_opy_ = bstack1l1ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠤᖴ")
    bstack1l111l11lll_opy_ = bstack1l1ll_opy_ (u"ࠨࡴࡦࡵࡷࡣࡱࡵࡧࡴࠤᖵ")
    bstack1l11l11l11l_opy_ = bstack1l1ll_opy_ (u"ࠢࡵࡧࡶࡸࡤࡳࡥࡵࡣࠥᖶ")
    bstack11lllll1l11_opy_ = bstack1l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡳࡤࡱࡳࡩࡸ࠭ᖷ")
    bstack1l11l1ll1ll_opy_ = bstack1l1ll_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡴࡡ࡮ࡧࠥᖸ")
    bstack1l11l1111ll_opy_ = bstack1l1ll_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹࠨᖹ")
    bstack1l111l1lll1_opy_ = bstack1l1ll_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡩࡳࡪࡥࡥࡡࡤࡸࠧᖺ")
    bstack1l111ll11l1_opy_ = bstack1l1ll_opy_ (u"ࠧ࡮࡯ࡰ࡭ࡢ࡭ࡩࠨᖻ")
    bstack1l111l11l11_opy_ = bstack1l1ll_opy_ (u"ࠨࡨࡰࡱ࡮ࡣࡷ࡫ࡳࡶ࡮ࡷࠦᖼ")
    bstack1l1111ll1ll_opy_ = bstack1l1ll_opy_ (u"ࠢࡩࡱࡲ࡯ࡤࡲ࡯ࡨࡵࠥᖽ")
    bstack1l1111l1l11_opy_ = bstack1l1ll_opy_ (u"ࠣࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠦᖾ")
    bstack11lllllllll_opy_ = bstack1l1ll_opy_ (u"ࠤ࡯ࡳ࡬ࡹࠢᖿ")
    bstack11lllllll11_opy_ = bstack1l1ll_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡢࡱࡪࡺࡡࡥࡣࡷࡥࠧᗀ")
    bstack1l11l1111l1_opy_ = bstack1l1ll_opy_ (u"ࠦࡵ࡫࡮ࡥ࡫ࡱ࡫ࠧᗁ")
    bstack1l111llllll_opy_ = bstack1l1ll_opy_ (u"ࠧࡶࡥ࡯ࡦ࡬ࡲ࡬ࠨᗂ")
    bstack1l1l1ll111l_opy_ = bstack1l1ll_opy_ (u"ࠨࡔࡆࡕࡗࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࠣᗃ")
    bstack1l1llll1111_opy_ = bstack1l1ll_opy_ (u"ࠢࡕࡇࡖࡘࡤࡒࡏࡈࠤᗄ")
    bstack1l1lll1llll_opy_ = bstack1l1ll_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥᗅ")
    bstack1llllllllll_opy_: Dict[str, bstack1lll1ll1111_opy_] = dict()
    bstack11llll1l11l_opy_: Dict[str, List[Callable]] = dict()
    bstack1ll1l111111_opy_: List[str]
    bstack1l111l1ll1l_opy_: Dict[str, str]
    def __init__(
        self,
        bstack1ll1l111111_opy_: List[str],
        bstack1l111l1ll1l_opy_: Dict[str, str],
        bstack111111l11l_opy_: bstack111111l1ll_opy_
    ):
        self.bstack1ll1l111111_opy_ = bstack1ll1l111111_opy_
        self.bstack1l111l1ll1l_opy_ = bstack1l111l1ll1l_opy_
        self.bstack111111l11l_opy_ = bstack111111l11l_opy_
    def track_event(
        self,
        context: bstack1l111lll1ll_opy_,
        test_framework_state: bstack1llll11ll11_opy_,
        test_hook_state: bstack1lll1111lll_opy_,
        *args,
        **kwargs,
    ):
        self.logger.debug(bstack1l1ll_opy_ (u"ࠤࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺ࠺ࠡࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠾ࡽࢀࠤࡹ࡫ࡳࡵࡡ࡫ࡳࡴࡱ࡟ࡴࡶࡤࡸࡪࡃࡻࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࢂࠨᗆ").format(test_framework_state,test_hook_state,args,kwargs))
    def bstack1l111l1l1l1_opy_(
        self,
        instance: bstack1lll1ll1111_opy_,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        *args,
        **kwargs,
    ):
        bstack1l11l11lll1_opy_ = TestFramework.bstack1l11l11l1l1_opy_(bstack1llllllll11_opy_)
        if not bstack1l11l11lll1_opy_ in TestFramework.bstack11llll1l11l_opy_:
            return
        self.logger.debug(bstack1l1ll_opy_ (u"ࠥ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࢁࡽࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࡶࠦᗇ").format(len(TestFramework.bstack11llll1l11l_opy_[bstack1l11l11lll1_opy_])))
        for callback in TestFramework.bstack11llll1l11l_opy_[bstack1l11l11lll1_opy_]:
            try:
                callback(self, instance, bstack1llllllll11_opy_, *args, **kwargs)
            except Exception as e:
                self.logger.error(bstack1l1ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠣ࡭ࡳࡼ࡯࡬࡫ࡱ࡫ࠥࡩࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠦᗈ").format(e))
                traceback.print_exc()
    @abc.abstractmethod
    def bstack1l1l1lll1ll_opy_(self):
        return
    @abc.abstractmethod
    def bstack1l1lll1l111_opy_(self, instance, bstack1llllllll11_opy_):
        return
    @abc.abstractmethod
    def bstack1l1ll11lll1_opy_(self, instance, bstack1llllllll11_opy_):
        return
    @staticmethod
    def bstack1lllll1l11l_opy_(target: object, strict=True):
        if target is None:
            return None
        ctx = bstack1lllll1111l_opy_.create_context(target)
        instance = TestFramework.bstack1llllllllll_opy_.get(ctx.id, None)
        if instance and instance.bstack1lllllll11l_opy_(target):
            return instance
        return instance if instance and not strict else None
    @staticmethod
    def bstack1l1lll1l1ll_opy_(reverse=True) -> List[bstack1lll1ll1111_opy_]:
        thread_id = threading.get_ident()
        process_id = os.getpid()
        return sorted(
            filter(
                lambda t: t.context.thread_id == thread_id
                and t.context.process_id == process_id,
                TestFramework.bstack1llllllllll_opy_.values(),
            ),
            key=lambda t: t.bstack1lllll1l1ll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllll11l11_opy_(ctx: bstack1111111l11_opy_, reverse=True) -> List[bstack1lll1ll1111_opy_]:
        return sorted(
            filter(
                lambda t: t.context.thread_id == ctx.thread_id
                and t.context.process_id == ctx.process_id,
                TestFramework.bstack1llllllllll_opy_.values(),
            ),
            key=lambda t: t.bstack1lllll1l1ll_opy_,
            reverse=reverse,
        )
    @staticmethod
    def bstack1lllllllll1_opy_(instance: bstack1lll1ll1111_opy_, key: str):
        return instance and key in instance.data
    @staticmethod
    def bstack1lllll111ll_opy_(instance: bstack1lll1ll1111_opy_, key: str, default_value=None):
        return instance.data.get(key, default_value) if instance else default_value
    @staticmethod
    def bstack1lllll1l111_opy_(instance: bstack1lll1ll1111_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1l1ll_opy_ (u"ࠧࡹࡥࡵࡡࡶࡸࡦࡺࡥ࠻ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡁࢀࢃࠠ࡬ࡧࡼࡁࢀࢃࠠࡷࡣ࡯ࡹࡪࡃࡻࡾࠤᗉ").format(instance.ref(),key,value))
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1l11111ll1l_opy_(instance: bstack1lll1ll1111_opy_, entries: Dict[str, Any]):
        TestFramework.logger.debug(bstack1l1ll_opy_ (u"ࠨࡳࡦࡶࡢࡷࡹࡧࡴࡦࡡࡨࡲࡹࡸࡩࡦࡵ࠽ࠤ࡮ࡴࡳࡵࡣࡱࡧࡪࡃࡻࡾࠢࡨࡲࡹࡸࡩࡦࡵࡀࡿࢂࠨᗊ").format(instance.ref(),entries,))
        instance.data.update(entries)
        return True
    @staticmethod
    def bstack11llll11lll_opy_(instance: bstack1llll11ll11_opy_, key: str, value: Any):
        TestFramework.logger.debug(bstack1l1ll_opy_ (u"ࠢࡶࡲࡧࡥࡹ࡫࡟ࡴࡶࡤࡸࡪࡀࠠࡪࡰࡶࡸࡦࡴࡣࡦ࠿ࡾࢁࠥࡱࡥࡺ࠿ࡾࢁࠥࡼࡡ࡭ࡷࡨࡁࢀࢃࠢᗋ").format(instance.ref(),key,value))
        instance.data.update(key, value)
        return True
    @staticmethod
    def get_data(key: str, target: object, strict=True, default_value=None):
        instance = TestFramework.bstack1lllll1l11l_opy_(target, strict)
        return TestFramework.bstack1lllll111ll_opy_(instance, key, default_value)
    @staticmethod
    def set_data(key: str, value: Any, target: object, strict=True):
        instance = TestFramework.bstack1lllll1l11l_opy_(target, strict)
        if not instance:
            return False
        instance.data[key] = value
        return True
    @staticmethod
    def bstack1l111l11111_opy_(instance: bstack1lll1ll1111_opy_, key: str, value: object):
        if instance == None:
            return
        instance.data[key] = value
    @staticmethod
    def bstack1l111ll1lll_opy_(instance: bstack1lll1ll1111_opy_, key: str):
        return instance.data[key]
    @staticmethod
    def bstack1l11l11l1l1_opy_(bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_]):
        return bstack1l1ll_opy_ (u"ࠣ࠼ࠥᗌ").join((bstack1llll11ll11_opy_(bstack1llllllll11_opy_[0]).name, bstack1lll1111lll_opy_(bstack1llllllll11_opy_[1]).name))
    @staticmethod
    def bstack1ll111ll111_opy_(bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_], callback: Callable):
        bstack1l11l11lll1_opy_ = TestFramework.bstack1l11l11l1l1_opy_(bstack1llllllll11_opy_)
        TestFramework.logger.debug(bstack1l1ll_opy_ (u"ࠤࡶࡩࡹࡥࡨࡰࡱ࡮ࡣࡨࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡩࡱࡲ࡯ࡤࡸࡥࡨ࡫ࡶࡸࡷࡿ࡟࡬ࡧࡼࡁࢀࢃࠢᗍ").format(bstack1l11l11lll1_opy_))
        if not bstack1l11l11lll1_opy_ in TestFramework.bstack11llll1l11l_opy_:
            TestFramework.bstack11llll1l11l_opy_[bstack1l11l11lll1_opy_] = []
        TestFramework.bstack11llll1l11l_opy_[bstack1l11l11lll1_opy_].append(callback)
    @staticmethod
    def bstack1l1lll11lll_opy_(o):
        klass = o.__class__
        module = klass.__module__
        if module == bstack1l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡵ࡫ࡱࡷࠧᗎ"):
            return klass.__qualname__
        return module + bstack1l1ll_opy_ (u"ࠦ࠳ࠨᗏ") + klass.__qualname__
    @staticmethod
    def bstack1l1ll11111l_opy_(obj, keys, default_value=None):
        return {k: getattr(obj, k, default_value) for k in keys}