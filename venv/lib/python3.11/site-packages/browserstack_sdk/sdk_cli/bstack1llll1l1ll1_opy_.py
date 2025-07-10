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
from datetime import datetime, timezone
import os
from pathlib import Path
from typing import Any, Tuple, Callable, List
from browserstack_sdk.sdk_cli.bstack1llllllll1l_opy_ import bstack1llll1ll1l1_opy_, bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lllllll_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll1ll1_opy_ import bstack1llll111lll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll11lll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11ll11_opy_, bstack1lll1ll1111_opy_, bstack1lll1111lll_opy_, bstack1llll11llll_opy_
from json import dumps, JSONEncoder
import grpc
from browserstack_sdk import sdk_pb2 as structs
import sys
import traceback
import time
import json
from bstack_utils.helper import bstack1l1ll1111ll_opy_, bstack1l1ll1l11ll_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
bstack1l1ll11l1l1_opy_ = [bstack1l1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ቏"), bstack1l1ll_opy_ (u"ࠧࡶࡡࡳࡧࡱࡸࠧቐ"), bstack1l1ll_opy_ (u"ࠨࡣࡰࡰࡩ࡭࡬ࠨቑ"), bstack1l1ll_opy_ (u"ࠢࡴࡧࡶࡷ࡮ࡵ࡮ࠣቒ"), bstack1l1ll_opy_ (u"ࠣࡲࡤࡸ࡭ࠨቓ")]
bstack1l1ll1lll1l_opy_ = bstack1l1ll1l11ll_opy_()
bstack1l1lll11l11_opy_ = bstack1l1ll_opy_ (u"ࠤࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠮ࠤቔ")
bstack1l1ll1l1ll1_opy_ = {
    bstack1l1ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶ࠱ࡴࡾࡺࡨࡰࡰ࠱ࡍࡹ࡫࡭ࠣቕ"): bstack1l1ll11l1l1_opy_,
    bstack1l1ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡵࡿࡴࡩࡱࡱ࠲ࡕࡧࡣ࡬ࡣࡪࡩࠧቖ"): bstack1l1ll11l1l1_opy_,
    bstack1l1ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡶࡹࡵࡪࡲࡲ࠳ࡓ࡯ࡥࡷ࡯ࡩࠧ቗"): bstack1l1ll11l1l1_opy_,
    bstack1l1ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠴ࡰࡺࡶ࡫ࡳࡳ࠴ࡃ࡭ࡣࡶࡷࠧቘ"): bstack1l1ll11l1l1_opy_,
    bstack1l1ll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࠮ࡱࡻࡷ࡬ࡴࡴ࠮ࡇࡷࡱࡧࡹ࡯࡯࡯ࠤ቙"): bstack1l1ll11l1l1_opy_
    + [
        bstack1l1ll_opy_ (u"ࠣࡱࡵ࡭࡬࡯࡮ࡢ࡮ࡱࡥࡲ࡫ࠢቚ"),
        bstack1l1ll_opy_ (u"ࠤ࡮ࡩࡾࡽ࡯ࡳࡦࡶࠦቛ"),
        bstack1l1ll_opy_ (u"ࠥࡪ࡮ࡾࡴࡶࡴࡨ࡭ࡳ࡬࡯ࠣቜ"),
        bstack1l1ll_opy_ (u"ࠦࡰ࡫ࡹࡸࡱࡵࡨࡸࠨቝ"),
        bstack1l1ll_opy_ (u"ࠧࡩࡡ࡭࡮ࡶࡴࡪࡩࠢ቞"),
        bstack1l1ll_opy_ (u"ࠨࡣࡢ࡮࡯ࡳࡧࡰࠢ቟"),
        bstack1l1ll_opy_ (u"ࠢࡴࡶࡤࡶࡹࠨበ"),
        bstack1l1ll_opy_ (u"ࠣࡵࡷࡳࡵࠨቡ"),
        bstack1l1ll_opy_ (u"ࠤࡧࡹࡷࡧࡴࡪࡱࡱࠦቢ"),
        bstack1l1ll_opy_ (u"ࠥࡻ࡭࡫࡮ࠣባ"),
    ],
    bstack1l1ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠲ࡲࡧࡩ࡯࠰ࡖࡩࡸࡹࡩࡰࡰࠥቤ"): [bstack1l1ll_opy_ (u"ࠧࡹࡴࡢࡴࡷࡴࡦࡺࡨࠣብ"), bstack1l1ll_opy_ (u"ࠨࡴࡦࡵࡷࡷ࡫ࡧࡩ࡭ࡧࡧࠦቦ"), bstack1l1ll_opy_ (u"ࠢࡵࡧࡶࡸࡸࡩ࡯࡭࡮ࡨࡧࡹ࡫ࡤࠣቧ"), bstack1l1ll_opy_ (u"ࠣ࡫ࡷࡩࡲࡹࠢቨ")],
    bstack1l1ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡦࡳࡳ࡬ࡩࡨ࠰ࡆࡳࡳ࡬ࡩࡨࠤቩ"): [bstack1l1ll_opy_ (u"ࠥ࡭ࡳࡼ࡯ࡤࡣࡷ࡭ࡴࡴ࡟ࡱࡣࡵࡥࡲࡹࠢቪ"), bstack1l1ll_opy_ (u"ࠦࡦࡸࡧࡴࠤቫ")],
    bstack1l1ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳࡬ࡩࡹࡶࡸࡶࡪࡹ࠮ࡇ࡫ࡻࡸࡺࡸࡥࡅࡧࡩࠦቬ"): [bstack1l1ll_opy_ (u"ࠨࡳࡤࡱࡳࡩࠧቭ"), bstack1l1ll_opy_ (u"ࠢࡢࡴࡪࡲࡦࡳࡥࠣቮ"), bstack1l1ll_opy_ (u"ࠣࡨࡸࡲࡨࠨቯ"), bstack1l1ll_opy_ (u"ࠤࡳࡥࡷࡧ࡭ࡴࠤተ"), bstack1l1ll_opy_ (u"ࠥࡹࡳ࡯ࡴࡵࡧࡶࡸࠧቱ"), bstack1l1ll_opy_ (u"ࠦ࡮ࡪࡳࠣቲ")],
    bstack1l1ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳࡬ࡩࡹࡶࡸࡶࡪࡹ࠮ࡔࡷࡥࡖࡪࡷࡵࡦࡵࡷࠦታ"): [bstack1l1ll_opy_ (u"ࠨࡦࡪࡺࡷࡹࡷ࡫࡮ࡢ࡯ࡨࠦቴ"), bstack1l1ll_opy_ (u"ࠢࡱࡣࡵࡥࡲࠨት"), bstack1l1ll_opy_ (u"ࠣࡲࡤࡶࡦࡳ࡟ࡪࡰࡧࡩࡽࠨቶ")],
    bstack1l1ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠰ࡵࡹࡳࡴࡥࡳ࠰ࡆࡥࡱࡲࡉ࡯ࡨࡲࠦቷ"): [bstack1l1ll_opy_ (u"ࠥࡻ࡭࡫࡮ࠣቸ"), bstack1l1ll_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷࠦቹ")],
    bstack1l1ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠳ࡳࡡࡳ࡭࠱ࡷࡹࡸࡵࡤࡶࡸࡶࡪࡹ࠮ࡏࡱࡧࡩࡐ࡫ࡹࡸࡱࡵࡨࡸࠨቺ"): [bstack1l1ll_opy_ (u"ࠨ࡮ࡰࡦࡨࠦቻ"), bstack1l1ll_opy_ (u"ࠢࡱࡣࡵࡩࡳࡺࠢቼ")],
    bstack1l1ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴ࠯࡯ࡤࡶࡰ࠴ࡳࡵࡴࡸࡧࡹࡻࡲࡦࡵ࠱ࡑࡦࡸ࡫ࠣች"): [bstack1l1ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢቾ"), bstack1l1ll_opy_ (u"ࠥࡥࡷ࡭ࡳࠣቿ"), bstack1l1ll_opy_ (u"ࠦࡰࡽࡡࡳࡩࡶࠦኀ")],
}
_1l1ll111lll_opy_ = set()
class bstack1lll1l1l1l1_opy_(bstack1llll11lll1_opy_):
    bstack1l1ll1l1111_opy_ = bstack1l1ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡨࡪ࡬ࡥࡳࡴࡨࡨࠧኁ")
    bstack1l1ll1l1l11_opy_ = bstack1l1ll_opy_ (u"ࠨࡉࡏࡈࡒࠦኂ")
    bstack1l1lll1ll11_opy_ = bstack1l1ll_opy_ (u"ࠢࡆࡔࡕࡓࡗࠨኃ")
    bstack1l1ll1lll11_opy_: Callable
    bstack1l1lll1lll1_opy_: Callable
    def __init__(self, bstack1ll1llll111_opy_, bstack1lll111ll1l_opy_):
        super().__init__()
        self.bstack1ll11lll11l_opy_ = bstack1lll111ll1l_opy_
        if os.getenv(bstack1l1ll_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡐ࠳࠴࡝ࠧኄ"), bstack1l1ll_opy_ (u"ࠤ࠴ࠦኅ")) != bstack1l1ll_opy_ (u"ࠥ࠵ࠧኆ") or not self.is_enabled():
            self.logger.warning(bstack1l1ll_opy_ (u"ࠦࠧኇ") + str(self.__class__.__name__) + bstack1l1ll_opy_ (u"ࠧࠦࡤࡪࡵࡤࡦࡱ࡫ࡤࠣኈ"))
            return
        TestFramework.bstack1ll111ll111_opy_((bstack1llll11ll11_opy_.TEST, bstack1lll1111lll_opy_.PRE), self.bstack1ll11l1111l_opy_)
        TestFramework.bstack1ll111ll111_opy_((bstack1llll11ll11_opy_.TEST, bstack1lll1111lll_opy_.POST), self.bstack1ll11l11lll_opy_)
        for event in bstack1llll11ll11_opy_:
            for state in bstack1lll1111lll_opy_:
                TestFramework.bstack1ll111ll111_opy_((event, state), self.bstack1l1lll1ll1l_opy_)
        bstack1ll1llll111_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.bstack1lllll11l1l_opy_, bstack1llll1lllll_opy_.POST), self.bstack1l1l1lllll1_opy_)
        self.bstack1l1ll1lll11_opy_ = sys.stdout.write
        sys.stdout.write = self.bstack1l1ll111ll1_opy_(bstack1lll1l1l1l1_opy_.bstack1l1ll1l1l11_opy_, self.bstack1l1ll1lll11_opy_)
        self.bstack1l1lll1lll1_opy_ = sys.stderr.write
        sys.stderr.write = self.bstack1l1ll111ll1_opy_(bstack1lll1l1l1l1_opy_.bstack1l1lll1ll11_opy_, self.bstack1l1lll1lll1_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l1lll1ll1l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll1111_opy_,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        *args,
        **kwargs,
    ):
        if f.bstack1l1l1lll1ll_opy_() and instance:
            bstack1l1l1ll11ll_opy_ = datetime.now()
            test_framework_state, test_hook_state = bstack1llllllll11_opy_
            if test_framework_state == bstack1llll11ll11_opy_.SETUP_FIXTURE:
                return
            elif test_framework_state == bstack1llll11ll11_opy_.LOG:
                bstack11l1l1111_opy_ = datetime.now()
                entries = f.bstack1l1lll1l111_opy_(instance, bstack1llllllll11_opy_)
                if entries:
                    self.bstack1l1ll1l1l1l_opy_(instance, entries)
                    instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡ࡯ࡳ࡬ࡥࡣࡳࡧࡤࡸࡪࡪ࡟ࡦࡸࡨࡲࡹࠨ኉"), datetime.now() - bstack11l1l1111_opy_)
                    f.bstack1l1ll11lll1_opy_(instance, bstack1llllllll11_opy_)
                instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠢࡰ࠳࠴ࡽ࠿ࡵ࡮ࡠࡣ࡯ࡰࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵࡵࠥኊ"), datetime.now() - bstack1l1l1ll11ll_opy_)
                return # bstack1l1ll1llll1_opy_ not send this event with the bstack1l1ll11l11l_opy_ bstack1l1lll1l11l_opy_
            elif (
                test_framework_state == bstack1llll11ll11_opy_.TEST
                and test_hook_state == bstack1lll1111lll_opy_.POST
                and not f.bstack1lllllllll1_opy_(instance, TestFramework.bstack1l1lll11111_opy_)
            ):
                self.logger.warning(bstack1l1ll_opy_ (u"ࠣࡦࡵࡳࡵࡶࡩ࡯ࡩࠣࡨࡺ࡫ࠠࡵࡱࠣࡰࡦࡩ࡫ࠡࡱࡩࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࠨኋ") + str(TestFramework.bstack1lllllllll1_opy_(instance, TestFramework.bstack1l1lll11111_opy_)) + bstack1l1ll_opy_ (u"ࠤࠥኌ"))
                f.bstack1lllll1l111_opy_(instance, bstack1lll1l1l1l1_opy_.bstack1l1ll1l1111_opy_, True)
                return # bstack1l1ll1llll1_opy_ not send this event bstack1l1ll11l111_opy_ bstack1l1l1ll1111_opy_
            elif (
                f.bstack1lllll111ll_opy_(instance, bstack1lll1l1l1l1_opy_.bstack1l1ll1l1111_opy_, False)
                and test_framework_state == bstack1llll11ll11_opy_.LOG_REPORT
                and test_hook_state == bstack1lll1111lll_opy_.POST
                and f.bstack1lllllllll1_opy_(instance, TestFramework.bstack1l1lll11111_opy_)
            ):
                self.logger.warning(bstack1l1ll_opy_ (u"ࠥ࡭ࡳࡰࡥࡤࡶ࡬ࡲ࡬ࠦࡔࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡙ࡴࡢࡶࡨ࠲࡙ࡋࡓࡕ࠮ࠣࡘࡪࡹࡴࡉࡱࡲ࡯ࡘࡺࡡࡵࡧ࠱ࡔࡔ࡙ࡔࠡࠤኍ") + str(TestFramework.bstack1lllllllll1_opy_(instance, TestFramework.bstack1l1lll11111_opy_)) + bstack1l1ll_opy_ (u"ࠦࠧ኎"))
                self.bstack1l1lll1ll1l_opy_(f, instance, (bstack1llll11ll11_opy_.TEST, bstack1lll1111lll_opy_.POST), *args, **kwargs)
            bstack11l1l1111_opy_ = datetime.now()
            data = instance.data.copy()
            bstack1l1llll11l1_opy_ = sorted(
                filter(lambda x: x.get(bstack1l1ll_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠣ኏"), None), data.pop(bstack1l1ll_opy_ (u"ࠨࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡸࠨነ"), {}).values()),
                key=lambda x: x[bstack1l1ll_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠥኑ")],
            )
            if bstack1llll111lll_opy_.bstack1l1l1llllll_opy_ in data:
                data.pop(bstack1llll111lll_opy_.bstack1l1l1llllll_opy_)
            data.update({bstack1l1ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡦࡪࡺࡷࡹࡷ࡫ࡳࠣኒ"): bstack1l1llll11l1_opy_})
            instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠤ࡭ࡷࡴࡴ࠺ࡵࡧࡶࡸࡤ࡬ࡩࡹࡶࡸࡶࡪࡹࠢና"), datetime.now() - bstack11l1l1111_opy_)
            bstack11l1l1111_opy_ = datetime.now()
            event_json = dumps(data, cls=bstack1l1lll111l1_opy_)
            instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠥ࡮ࡸࡵ࡮࠻ࡱࡱࡣࡦࡲ࡬ࡠࡶࡨࡷࡹࡥࡥࡷࡧࡱࡸࡸࠨኔ"), datetime.now() - bstack11l1l1111_opy_)
            self.bstack1l1lll1l11l_opy_(instance, bstack1llllllll11_opy_, event_json=event_json)
            instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠦࡴ࠷࠱ࡺ࠼ࡲࡲࡤࡧ࡬࡭ࡡࡷࡩࡸࡺ࡟ࡦࡸࡨࡲࡹࡹࠢን"), datetime.now() - bstack1l1l1ll11ll_opy_)
    def bstack1ll11l1111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll1111_opy_,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        *args,
        **kwargs,
    ):
        from bstack_utils.bstack11l1l111l_opy_ import bstack1llll11l1l1_opy_
        bstack1ll1l11l11l_opy_ = bstack1llll11l1l1_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack1l111lll1_opy_.value)
        self.bstack1ll11lll11l_opy_.bstack1l1ll1l11l1_opy_(instance, f, bstack1llllllll11_opy_, *args, **kwargs)
        bstack1llll11l1l1_opy_.end(EVENTS.bstack1l111lll1_opy_.value, bstack1ll1l11l11l_opy_ + bstack1l1ll_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧኖ"), bstack1ll1l11l11l_opy_ + bstack1l1ll_opy_ (u"ࠨ࠺ࡦࡰࡧࠦኗ"), status=True, failure=None, test_name=None)
    def bstack1ll11l11lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll1111_opy_,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        *args,
        **kwargs,
    ):
        req = self.bstack1ll11lll11l_opy_.bstack1l1ll1ll111_opy_(instance, f, bstack1llllllll11_opy_, *args, **kwargs)
        self.bstack1l1l1ll1ll1_opy_(f, instance, req)
    @measure(event_name=EVENTS.bstack1l1ll1l1lll_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def bstack1l1l1ll1ll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll1111_opy_,
        req: structs.TestSessionEventRequest
    ):
        if not req:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠢࡔ࡭࡬ࡴࡵ࡯࡮ࡨࠢࡗࡩࡸࡺࡓࡦࡵࡶ࡭ࡴࡴࡅࡷࡧࡱࡸࠥ࡭ࡒࡑࡅࠣࡧࡦࡲ࡬࠻ࠢࡑࡳࠥࡼࡡ࡭࡫ࡧࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡪࡡࡵࡣࠥኘ"))
            return
        bstack11l1l1111_opy_ = datetime.now()
        try:
            r = self.bstack1lll1ll111l_opy_.TestSessionEvent(req)
            instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡹ࡫ࡳࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡩࡻ࡫࡮ࡵࠤኙ"), datetime.now() - bstack11l1l1111_opy_)
            f.bstack1lllll1l111_opy_(instance, self.bstack1ll11lll11l_opy_.bstack1l1lll11ll1_opy_, r.success)
            if not r.success:
                self.logger.info(bstack1l1ll_opy_ (u"ࠤࡵࡩࡨ࡫ࡩࡷࡧࡧࠤ࡫ࡸ࡯࡮ࠢࡶࡩࡷࡼࡥࡳ࠼ࠣࠦኚ") + str(r) + bstack1l1ll_opy_ (u"ࠥࠦኛ"))
        except grpc.RpcError as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤኜ") + str(e) + bstack1l1ll_opy_ (u"ࠧࠨኝ"))
            traceback.print_exc()
            raise e
    def bstack1l1l1lllll1_opy_(
        self,
        f: bstack1lll11lll1l_opy_,
        _driver: object,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        _1l1l1lll11l_opy_: Tuple[bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_],
        result: Any,
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if not bstack1lll11lll1l_opy_.bstack1ll1l111ll1_opy_(method_name):
            return
        if f.bstack1ll11ll1111_opy_(*args) == bstack1lll11lll1l_opy_.bstack1l1ll111111_opy_:
            bstack1l1l1ll11ll_opy_ = datetime.now()
            screenshot = result.get(bstack1l1ll_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࠧኞ"), None) if isinstance(result, dict) else None
            if not isinstance(screenshot, str) or len(screenshot) <= 0:
                self.logger.warning(bstack1l1ll_opy_ (u"ࠢࡪࡰࡹࡥࡱ࡯ࡤࠡࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠥ࡯࡭ࡢࡩࡨࠤࡧࡧࡳࡦ࠸࠷ࠤࡸࡺࡲࠣኟ"))
                return
            bstack1l1ll111l1l_opy_ = self.bstack1l1l1llll1l_opy_(instance)
            if bstack1l1ll111l1l_opy_:
                entry = bstack1llll11llll_opy_(TestFramework.bstack1l1l1ll111l_opy_, screenshot)
                self.bstack1l1ll1l1l1l_opy_(bstack1l1ll111l1l_opy_, [entry])
                instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠣࡱ࠴࠵ࡾࡀ࡯࡯ࡡࡤࡪࡹ࡫ࡲࡠࡧࡻࡩࡨࡻࡴࡦࠤአ"), datetime.now() - bstack1l1l1ll11ll_opy_)
            else:
                self.logger.warning(bstack1l1ll_opy_ (u"ࠤࡸࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡵࡱ࡮ࡴࡥࠡࡶࡨࡷࡹࠦࡦࡰࡴࠣࡻ࡭࡯ࡣࡩࠢࡷ࡬࡮ࡹࠠࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠤࡼࡧࡳࠡࡶࡤ࡯ࡪࡴࠠࡣࡻࠣࡨࡷ࡯ࡶࡦࡴࡀࠤࢀࢃࠢኡ").format(instance.ref()))
        event = {}
        bstack1l1ll111l1l_opy_ = self.bstack1l1l1llll1l_opy_(instance)
        if bstack1l1ll111l1l_opy_:
            self.bstack1l1ll11ll1l_opy_(event, bstack1l1ll111l1l_opy_)
            if event.get(bstack1l1ll_opy_ (u"ࠥࡰࡴ࡭ࡳࠣኢ")):
                self.bstack1l1ll1l1l1l_opy_(bstack1l1ll111l1l_opy_, event[bstack1l1ll_opy_ (u"ࠦࡱࡵࡧࡴࠤኣ")])
            else:
                self.logger.debug(bstack1l1ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤࡱࡵࡧࡴࠢࡩࡳࡷࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡩࡻ࡫࡮ࡵࠤኤ"))
    @measure(event_name=EVENTS.bstack1l1ll1lllll_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def bstack1l1ll1l1l1l_opy_(
        self,
        bstack1l1ll111l1l_opy_: bstack1lll1ll1111_opy_,
        entries: List[bstack1llll11llll_opy_],
    ):
        self.bstack1ll1111ll11_opy_()
        req = structs.LogCreatedEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack1lllll111ll_opy_(bstack1l1ll111l1l_opy_, TestFramework.bstack1ll111l111l_opy_)
        req.execution_context.hash = str(bstack1l1ll111l1l_opy_.context.hash)
        req.execution_context.thread_id = str(bstack1l1ll111l1l_opy_.context.thread_id)
        req.execution_context.process_id = str(bstack1l1ll111l1l_opy_.context.process_id)
        for entry in entries:
            log_entry = req.logs.add()
            log_entry.test_framework_name = TestFramework.bstack1lllll111ll_opy_(bstack1l1ll111l1l_opy_, TestFramework.bstack1ll11llll11_opy_)
            log_entry.test_framework_version = TestFramework.bstack1lllll111ll_opy_(bstack1l1ll111l1l_opy_, TestFramework.bstack1l1ll1ll11l_opy_)
            log_entry.uuid = TestFramework.bstack1lllll111ll_opy_(bstack1l1ll111l1l_opy_, TestFramework.bstack1ll11l111l1_opy_)
            log_entry.test_framework_state = bstack1l1ll111l1l_opy_.state.name
            log_entry.message = entry.message.encode(bstack1l1ll_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧእ"))
            log_entry.kind = entry.kind
            log_entry.timestamp = (
                entry.timestamp.isoformat()
                if isinstance(entry.timestamp, datetime)
                else datetime.now(tz=timezone.utc).isoformat()
            )
            if isinstance(entry.level, str) and len(entry.level.strip()) > 0:
                log_entry.level = entry.level.strip()
            if entry.kind == bstack1l1ll_opy_ (u"ࠢࡕࡇࡖࡘࡤࡇࡔࡕࡃࡆࡌࡒࡋࡎࡕࠤኦ"):
                log_entry.file_name = entry.fileName
                log_entry.file_size = entry.bstack1l1l1ll1l11_opy_
                log_entry.file_path = entry.bstack1l1l1l1_opy_
        def bstack1l1ll1111l1_opy_():
            bstack11l1l1111_opy_ = datetime.now()
            try:
                self.bstack1lll1ll111l_opy_.LogCreatedEvent(req)
                if entry.kind == TestFramework.bstack1l1l1ll111l_opy_:
                    bstack1l1ll111l1l_opy_.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠣࡩࡵࡴࡨࡀࡳࡦࡰࡧࡣࡱࡵࡧࡠࡥࡵࡩࡦࡺࡥࡥࡡࡨࡺࡪࡴࡴࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠧኧ"), datetime.now() - bstack11l1l1111_opy_)
                elif entry.kind == TestFramework.bstack1l1lll1llll_opy_:
                    bstack1l1ll111l1l_opy_.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡧࡱࡨࡤࡲ࡯ࡨࡡࡦࡶࡪࡧࡴࡦࡦࡢࡩࡻ࡫࡮ࡵࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠨከ"), datetime.now() - bstack11l1l1111_opy_)
                else:
                    bstack1l1ll111l1l_opy_.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡵࡨࡲࡩࡥ࡬ࡰࡩࡢࡧࡷ࡫ࡡࡵࡧࡧࡣࡪࡼࡥ࡯ࡶࡢࡰࡴ࡭ࠢኩ"), datetime.now() - bstack11l1l1111_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l1ll_opy_ (u"ࠦࡷࡶࡣ࠮ࡧࡵࡶࡴࡸ࠺ࠡࠤኪ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack111111l11l_opy_.enqueue(bstack1l1ll1111l1_opy_)
    @measure(event_name=EVENTS.bstack1l1ll111l11_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def bstack1l1lll1l11l_opy_(
        self,
        instance: bstack1lll1ll1111_opy_,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        event_json=None,
    ):
        self.bstack1ll1111ll11_opy_()
        req = structs.TestFrameworkEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1ll111l111l_opy_)
        req.test_framework_name = TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1ll11llll11_opy_)
        req.test_framework_version = TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1l1ll1ll11l_opy_)
        req.test_framework_state = bstack1llllllll11_opy_[0].name
        req.test_hook_state = bstack1llllllll11_opy_[1].name
        started_at = TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1l1lll111ll_opy_, None)
        if started_at:
            req.started_at = started_at.isoformat()
        ended_at = TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1l1ll1ll1ll_opy_, None)
        if ended_at:
            req.ended_at = ended_at.isoformat()
        req.uuid = instance.ref()
        req.event_json = (event_json if event_json else dumps(instance.data, cls=bstack1l1lll111l1_opy_)).encode(bstack1l1ll_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦካ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        def bstack1l1ll1111l1_opy_():
            bstack11l1l1111_opy_ = datetime.now()
            try:
                self.bstack1lll1ll111l_opy_.TestFrameworkEvent(req)
                instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸ࡫࡮ࡥࡡࡷࡩࡸࡺ࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡩࡻ࡫࡮ࡵࠤኬ"), datetime.now() - bstack11l1l1111_opy_)
            except grpc.RpcError as e:
                self.log_error(bstack1l1ll_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧክ") + str(e))
                traceback.print_exc()
                raise e
        self.bstack111111l11l_opy_.enqueue(bstack1l1ll1111l1_opy_)
    def bstack1l1l1llll1l_opy_(self, instance: bstack1llll1ll1l1_opy_):
        bstack1l1l1ll11l1_opy_ = TestFramework.bstack1lllll11l11_opy_(instance.context)
        for t in bstack1l1l1ll11l1_opy_:
            bstack1l1ll1ll1l1_opy_ = TestFramework.bstack1lllll111ll_opy_(t, bstack1llll111lll_opy_.bstack1l1l1llllll_opy_, [])
            if any(instance is d[1] for d in bstack1l1ll1ll1l1_opy_):
                return t
    def bstack1l1llll111l_opy_(self, message):
        self.bstack1l1ll1lll11_opy_(message + bstack1l1ll_opy_ (u"ࠣ࡞ࡱࠦኮ"))
    def log_error(self, message):
        self.bstack1l1lll1lll1_opy_(message + bstack1l1ll_opy_ (u"ࠤ࡟ࡲࠧኯ"))
    def bstack1l1ll111ll1_opy_(self, level, original_func):
        def bstack1l1l1lll1l1_opy_(*args):
            return_value = original_func(*args)
            if not args or not isinstance(args[0], str) or not args[0].strip():
                return return_value
            message = args[0].strip()
            bstack1l1l1ll11l1_opy_ = TestFramework.bstack1l1lll1l1ll_opy_()
            if not bstack1l1l1ll11l1_opy_:
                return return_value
            bstack1l1ll111l1l_opy_ = next(
                (
                    instance
                    for instance in bstack1l1l1ll11l1_opy_
                    if TestFramework.bstack1lllllllll1_opy_(instance, TestFramework.bstack1ll11l111l1_opy_)
                ),
                None,
            )
            if not bstack1l1ll111l1l_opy_:
                return
            entry = bstack1llll11llll_opy_(TestFramework.bstack1l1llll1111_opy_, message, level)
            self.bstack1l1ll1l1l1l_opy_(bstack1l1ll111l1l_opy_, [entry])
            return return_value
        return bstack1l1l1lll1l1_opy_
    def bstack1l1ll11ll1l_opy_(self, event: dict, instance=None) -> None:
        global _1l1ll111lll_opy_
        levels = [bstack1l1ll_opy_ (u"ࠥࡘࡪࡹࡴࡍࡧࡹࡩࡱࠨኰ"), bstack1l1ll_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣ኱")]
        bstack1l1ll11ll11_opy_ = bstack1l1ll_opy_ (u"ࠧࠨኲ")
        if instance is not None:
            try:
                bstack1l1ll11ll11_opy_ = TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1ll11l111l1_opy_)
            except Exception as e:
                self.logger.warning(bstack1l1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡵࡶ࡫ࡧࠤ࡫ࡸ࡯࡮ࠢ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠦኳ").format(e))
        bstack1l1lll1111l_opy_ = []
        try:
            for level in levels:
                platform_index = os.environ[bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧኴ")]
                bstack1l1l1l1llll_opy_ = os.path.join(bstack1l1ll1lll1l_opy_, (bstack1l1lll11l11_opy_ + str(platform_index)), level)
                if not os.path.isdir(bstack1l1l1l1llll_opy_):
                    self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡳࡵࡴࠡࡲࡵࡩࡸ࡫࡮ࡵࠢࡩࡳࡷࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡘࡪࡹࡴࠡࡣࡱࡨࠥࡈࡵࡪ࡮ࡧࠤࡱ࡫ࡶࡦ࡮ࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡽࢀࠦኵ").format(bstack1l1l1l1llll_opy_))
                    continue
                file_names = os.listdir(bstack1l1l1l1llll_opy_)
                for file_name in file_names:
                    file_path = os.path.join(bstack1l1l1l1llll_opy_, file_name)
                    abs_path = os.path.abspath(file_path)
                    if abs_path in _1l1ll111lll_opy_:
                        self.logger.info(bstack1l1ll_opy_ (u"ࠤࡓࡥࡹ࡮ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤࢀࢃࠢ኶").format(abs_path))
                        continue
                    if os.path.isfile(file_path):
                        try:
                            bstack1l1lll1l1l1_opy_ = os.path.getmtime(file_path)
                            timestamp = datetime.fromtimestamp(bstack1l1lll1l1l1_opy_, tz=timezone.utc).isoformat()
                            file_size = os.path.getsize(file_path)
                            if level == bstack1l1ll_opy_ (u"ࠥࡘࡪࡹࡴࡍࡧࡹࡩࡱࠨ኷"):
                                entry = bstack1llll11llll_opy_(
                                    kind=bstack1l1ll_opy_ (u"࡙ࠦࡋࡓࡕࡡࡄࡘ࡙ࡇࡃࡉࡏࡈࡒ࡙ࠨኸ"),
                                    message=bstack1l1ll_opy_ (u"ࠧࠨኹ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1l1l1ll1l11_opy_=file_size,
                                    bstack1l1lll11l1l_opy_=bstack1l1ll_opy_ (u"ࠨࡍࡂࡐࡘࡅࡑࡥࡕࡑࡎࡒࡅࡉࠨኺ"),
                                    bstack1l1l1l1_opy_=os.path.abspath(file_path),
                                    bstack1l1l1llll1_opy_=bstack1l1ll11ll11_opy_
                                )
                            elif level == bstack1l1ll_opy_ (u"ࠢࡃࡷ࡬ࡰࡩࡒࡥࡷࡧ࡯ࠦኻ"):
                                entry = bstack1llll11llll_opy_(
                                    kind=bstack1l1ll_opy_ (u"ࠣࡖࡈࡗ࡙ࡥࡁࡕࡖࡄࡇࡍࡓࡅࡏࡖࠥኼ"),
                                    message=bstack1l1ll_opy_ (u"ࠤࠥኽ"),
                                    level=level,
                                    timestamp=timestamp,
                                    fileName=file_name,
                                    bstack1l1l1ll1l11_opy_=file_size,
                                    bstack1l1lll11l1l_opy_=bstack1l1ll_opy_ (u"ࠥࡑࡆࡔࡕࡂࡎࡢ࡙ࡕࡒࡏࡂࡆࠥኾ"),
                                    bstack1l1l1l1_opy_=os.path.abspath(file_path),
                                    bstack1l1l1ll1lll_opy_=bstack1l1ll11ll11_opy_
                                )
                            bstack1l1lll1111l_opy_.append(entry)
                            _1l1ll111lll_opy_.add(abs_path)
                        except Exception as bstack1l1ll11llll_opy_:
                            self.logger.error(bstack1l1ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡳࡣ࡬ࡷࡪࡪࠠࡸࡪࡨࡲࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࡹࠠࡼࡿࠥ኿").format(bstack1l1ll11llll_opy_))
        except Exception as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡴࡤ࡭ࡸ࡫ࡤࠡࡹ࡫ࡩࡳࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡥࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳࠡࡽࢀࠦዀ").format(e))
        event[bstack1l1ll_opy_ (u"ࠨ࡬ࡰࡩࡶࠦ዁")] = bstack1l1lll1111l_opy_
class bstack1l1lll111l1_opy_(JSONEncoder):
    def __init__(self, **kwargs):
        self.bstack1l1l1ll1l1l_opy_ = set()
        kwargs[bstack1l1ll_opy_ (u"ࠢࡴ࡭࡬ࡴࡰ࡫ࡹࡴࠤዂ")] = True
        super().__init__(**kwargs)
    def default(self, obj):
        return bstack1l1l1lll111_opy_(obj, self.bstack1l1l1ll1l1l_opy_)
def bstack1l1l1llll11_opy_(obj):
    return isinstance(obj, (str, int, float, bool, type(None)))
def bstack1l1l1lll111_opy_(obj, bstack1l1l1ll1l1l_opy_=None, max_depth=3):
    if bstack1l1l1ll1l1l_opy_ is None:
        bstack1l1l1ll1l1l_opy_ = set()
    if id(obj) in bstack1l1l1ll1l1l_opy_ or max_depth <= 0:
        return None
    max_depth -= 1
    bstack1l1l1ll1l1l_opy_.add(id(obj))
    if isinstance(obj, datetime):
        return obj.isoformat()
    bstack1l1ll1l111l_opy_ = TestFramework.bstack1l1lll11lll_opy_(obj)
    bstack1l1ll11l1ll_opy_ = next((k.lower() in bstack1l1ll1l111l_opy_.lower() for k in bstack1l1ll1l1ll1_opy_.keys()), None)
    if bstack1l1ll11l1ll_opy_:
        obj = TestFramework.bstack1l1ll11111l_opy_(obj, bstack1l1ll1l1ll1_opy_[bstack1l1ll11l1ll_opy_])
    if not isinstance(obj, dict):
        keys = []
        if hasattr(obj, bstack1l1ll_opy_ (u"ࠣࡡࡢࡷࡱࡵࡴࡴࡡࡢࠦዃ")):
            keys = getattr(obj, bstack1l1ll_opy_ (u"ࠤࡢࡣࡸࡲ࡯ࡵࡵࡢࡣࠧዄ"), [])
        elif hasattr(obj, bstack1l1ll_opy_ (u"ࠥࡣࡤࡪࡩࡤࡶࡢࡣࠧዅ")):
            keys = getattr(obj, bstack1l1ll_opy_ (u"ࠦࡤࡥࡤࡪࡥࡷࡣࡤࠨ዆"), {}).keys()
        else:
            keys = dir(obj)
        obj = {k: getattr(obj, k, None) for k in keys if not str(k).startswith(bstack1l1ll_opy_ (u"ࠧࡥࠢ዇"))}
        if not obj and bstack1l1ll1l111l_opy_ == bstack1l1ll_opy_ (u"ࠨࡰࡢࡶ࡫ࡰ࡮ࡨ࠮ࡑࡱࡶ࡭ࡽࡖࡡࡵࡪࠥወ"):
            obj = {bstack1l1ll_opy_ (u"ࠢࡱࡣࡷ࡬ࠧዉ"): str(obj)}
    result = {}
    for key, value in obj.items():
        if not bstack1l1l1llll11_opy_(key) or str(key).startswith(bstack1l1ll_opy_ (u"ࠣࡡࠥዊ")):
            continue
        if value is not None and bstack1l1l1llll11_opy_(value):
            result[key] = value
        elif isinstance(value, dict):
            r = bstack1l1l1lll111_opy_(value, bstack1l1l1ll1l1l_opy_, max_depth)
            if r is not None:
                result[key] = r
        elif isinstance(value, (list, tuple, set, frozenset)):
            result[key] = list(filter(None, [bstack1l1l1lll111_opy_(o, bstack1l1l1ll1l1l_opy_, max_depth) for o in value]))
    return result or None