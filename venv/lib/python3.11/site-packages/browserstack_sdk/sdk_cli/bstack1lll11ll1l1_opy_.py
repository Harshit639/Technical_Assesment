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
from datetime import datetime
import os
import threading
from browserstack_sdk.sdk_cli.bstack1llllllll1l_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llll1lllll_opy_,
    bstack11111111l1_opy_,
    bstack1llll1ll1l1_opy_,
)
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll11lll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11ll11_opy_, bstack1lll1111lll_opy_, bstack1lll1ll1111_opy_
from typing import Tuple, Dict, Any, List, Union
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack1ll1lllllll_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll1ll1_opy_ import bstack1llll111lll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11ll_opy_ import bstack1ll1ll111ll_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll1l1l_opy_ import bstack1ll1lllll11_opy_
from bstack_utils.helper import bstack1ll1l111l1l_opy_
from bstack_utils.measure import measure
from bstack_utils.constants import *
from bstack_utils.bstack11l1l111l_opy_ import bstack1llll11l1l1_opy_
import grpc
import traceback
import json
class bstack1ll1l1l1ll1_opy_(bstack1llll11lll1_opy_):
    bstack1ll111ll11l_opy_ = False
    bstack1ll111l1l11_opy_ = bstack1l1ll_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲࠣᅵ")
    bstack1ll11ll1l11_opy_ = bstack1l1ll_opy_ (u"ࠦࡷ࡫࡭ࡰࡶࡨ࠲ࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸࠢᅶ")
    bstack1ll11lll1ll_opy_ = bstack1l1ll_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡤ࡯࡮ࡪࡶࠥᅷ")
    bstack1ll11l1l1l1_opy_ = bstack1l1ll_opy_ (u"ࠨࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡩࡴࡡࡶࡧࡦࡴ࡮ࡪࡰࡪࠦᅸ")
    bstack1ll11lll1l1_opy_ = bstack1l1ll_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࡟ࡩࡣࡶࡣࡺࡸ࡬ࠣᅹ")
    scripts: Dict[str, Dict[str, str]]
    commands: Dict[str, Dict[str, Dict[str, List[str]]]]
    def __init__(self, bstack1ll1llll111_opy_, bstack1lll111ll1l_opy_):
        super().__init__()
        self.scripts = dict()
        self.commands = dict()
        self.accessibility = False
        self.bstack1ll11l1lll1_opy_ = False
        self.bstack1ll111lllll_opy_ = dict()
        if not self.is_enabled():
            return
        self.bstack1ll11lll11l_opy_ = bstack1lll111ll1l_opy_
        bstack1ll1llll111_opy_.bstack1ll111ll111_opy_((bstack1lllll1lll1_opy_.bstack1lllll11l1l_opy_, bstack1llll1lllll_opy_.PRE), self.bstack1ll11lllll1_opy_)
        TestFramework.bstack1ll111ll111_opy_((bstack1llll11ll11_opy_.TEST, bstack1lll1111lll_opy_.PRE), self.bstack1ll11l1111l_opy_)
        TestFramework.bstack1ll111ll111_opy_((bstack1llll11ll11_opy_.TEST, bstack1lll1111lll_opy_.POST), self.bstack1ll11l11lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1ll11l1111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll1111_opy_,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1ll1l111l11_opy_(instance, args)
        test_framework = f.bstack1lllll111ll_opy_(instance, TestFramework.bstack1ll11llll11_opy_)
        if self.bstack1ll11l1lll1_opy_:
            self.bstack1ll111lllll_opy_[bstack1l1ll_opy_ (u"ࠣࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠣᅺ")] = f.bstack1lllll111ll_opy_(instance, TestFramework.bstack1ll11l111l1_opy_)
        if bstack1l1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩ࠭ᅻ") in instance.bstack1ll1l111111_opy_:
            platform_index = f.bstack1lllll111ll_opy_(instance, TestFramework.bstack1ll111l111l_opy_)
            self.accessibility = self.bstack1ll1l11111l_opy_(tags, self.config[bstack1l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᅼ")][platform_index])
        else:
            capabilities = self.bstack1ll11lll11l_opy_.bstack1ll1l11l1l1_opy_(f, instance, bstack1llllllll11_opy_, *args, **kwargs)
            if not capabilities:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦ࡮ࡰࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠡࡨࡲࡹࡳࡪࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦᅽ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠧࠨᅾ"))
                return
            self.accessibility = self.bstack1ll1l11111l_opy_(tags, capabilities)
        if self.bstack1ll11lll11l_opy_.pages and self.bstack1ll11lll11l_opy_.pages.values():
            bstack1ll111llll1_opy_ = list(self.bstack1ll11lll11l_opy_.pages.values())
            if bstack1ll111llll1_opy_ and isinstance(bstack1ll111llll1_opy_[0], (list, tuple)) and bstack1ll111llll1_opy_[0]:
                bstack1ll11l11l1l_opy_ = bstack1ll111llll1_opy_[0][0]
                if callable(bstack1ll11l11l1l_opy_):
                    page = bstack1ll11l11l1l_opy_()
                    def bstack11l1l11l1_opy_():
                        self.get_accessibility_results(page, bstack1l1ll_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥᅿ"))
                    def bstack1ll1l1111l1_opy_():
                        self.get_accessibility_results_summary(page, bstack1l1ll_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦᆀ"))
                    setattr(page, bstack1l1ll_opy_ (u"ࠣࡩࡨࡸࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡖࡪࡹࡵ࡭ࡶࡶࠦᆁ"), bstack11l1l11l1_opy_)
                    setattr(page, bstack1l1ll_opy_ (u"ࠤࡪࡩࡹࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡗ࡫ࡳࡶ࡮ࡷࡗࡺࡳ࡭ࡢࡴࡼࠦᆂ"), bstack1ll1l1111l1_opy_)
        self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡷ࡭ࡵࡵ࡭ࡦࠣࡶࡺࡴࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡷࡣ࡯ࡹࡪࡃࠢᆃ") + str(self.accessibility) + bstack1l1ll_opy_ (u"ࠦࠧᆄ"))
    def bstack1ll11lllll1_opy_(
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
            bstack11l1l1111_opy_ = datetime.now()
            self.bstack1ll1l11ll11_opy_(f, exec, *args, **kwargs)
            instance, method_name = exec
            instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠧࡧ࠱࠲ࡻ࠽࡭ࡳ࡯ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡥࡲࡲ࡫࡯ࡧࠣᆅ"), datetime.now() - bstack11l1l1111_opy_)
            if (
                not f.bstack1ll1l111ll1_opy_(method_name)
                or f.bstack1ll1l111lll_opy_(method_name, *args)
                or f.bstack1ll11ll1l1l_opy_(method_name, *args)
            ):
                return
            if not f.bstack1lllll111ll_opy_(instance, bstack1ll1l1l1ll1_opy_.bstack1ll11lll1ll_opy_, False):
                if not bstack1ll1l1l1ll1_opy_.bstack1ll111ll11l_opy_:
                    self.logger.warning(bstack1l1ll_opy_ (u"ࠨ࡛ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࠤᆆ") + str(f.platform_index) + bstack1l1ll_opy_ (u"ࠢ࡞ࠢࡤ࠵࠶ࡿࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࠦࡨࡢࡸࡨࠤࡳࡵࡴࠡࡤࡨࡩࡳࠦࡳࡦࡶࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡹࡥࡴࡵ࡬ࡳࡳࠨᆇ"))
                    bstack1ll1l1l1ll1_opy_.bstack1ll111ll11l_opy_ = True
                return
            bstack1ll11l1l111_opy_ = self.scripts.get(f.framework_name, {})
            if not bstack1ll11l1l111_opy_:
                platform_index = f.bstack1lllll111ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1ll111l111l_opy_, 0)
                self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡰࡲࠤࡦ࠷࠱ࡺࠢࡶࡧࡷ࡯ࡰࡵࡵࠣࡪࡴࡸࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸ࠾ࡽࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࢀࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨᆈ") + str(f.framework_name) + bstack1l1ll_opy_ (u"ࠤࠥᆉ"))
                return
            bstack1ll1l1111ll_opy_ = f.bstack1ll11ll1111_opy_(*args)
            if not bstack1ll1l1111ll_opy_:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡱ࡮ࡹࡳࡪࡰࡪࠤࡨࡵ࡭࡮ࡣࡱࡨࡤࡴࡡ࡮ࡧࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦ࡭ࡦࡶ࡫ࡳࡩࡥ࡮ࡢ࡯ࡨࡁࠧᆊ") + str(method_name) + bstack1l1ll_opy_ (u"ࠦࠧᆋ"))
                return
            bstack1ll11l11l11_opy_ = f.bstack1lllll111ll_opy_(instance, bstack1ll1l1l1ll1_opy_.bstack1ll11lll1l1_opy_, False)
            if bstack1ll1l1111ll_opy_ == bstack1l1ll_opy_ (u"ࠧ࡭ࡥࡵࠤᆌ") and not bstack1ll11l11l11_opy_:
                f.bstack1lllll1l111_opy_(instance, bstack1ll1l1l1ll1_opy_.bstack1ll11lll1l1_opy_, True)
                bstack1ll11l11l11_opy_ = True
            if not bstack1ll11l11l11_opy_ and not self.bstack1ll11l1lll1_opy_:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠨ࡮ࡰࠢࡘࡖࡑࠦ࡬ࡰࡣࡧࡩࡩࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨ࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࡁࠧᆍ") + str(bstack1ll1l1111ll_opy_) + bstack1l1ll_opy_ (u"ࠢࠣᆎ"))
                return
            scripts_to_run = self.commands.get(f.framework_name, {}).get(method_name, {}).get(bstack1ll1l1111ll_opy_, [])
            if not scripts_to_run:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡰࡲࠤࡦ࠷࠱ࡺࠢࡶࡧࡷ࡯ࡰࡵࡵࠣࡪࡴࡸࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥ࠾ࡽࡩ࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࢂࠦࡣࡰ࡯ࡰࡥࡳࡪ࡟࡯ࡣࡰࡩࡂࠨᆏ") + str(bstack1ll1l1111ll_opy_) + bstack1l1ll_opy_ (u"ࠤࠥᆐ"))
                return
            self.logger.info(bstack1l1ll_opy_ (u"ࠥࡶࡺࡴ࡮ࡪࡰࡪࠤࢀࡲࡥ࡯ࠪࡶࡧࡷ࡯ࡰࡵࡵࡢࡸࡴࡥࡲࡶࡰࠬࢁࠥࡹࡣࡳ࡫ࡳࡸࡸࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫࠽ࡼࡨ࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡩ࡯࡮࡯ࡤࡲࡩࡥ࡮ࡢ࡯ࡨࡁࠧᆑ") + str(bstack1ll1l1111ll_opy_) + bstack1l1ll_opy_ (u"ࠦࠧᆒ"))
            scripts = [(s, bstack1ll11l1l111_opy_[s]) for s in scripts_to_run if s in bstack1ll11l1l111_opy_]
            for script_name, bstack1ll1111lll1_opy_ in scripts:
                try:
                    bstack11l1l1111_opy_ = datetime.now()
                    if script_name == bstack1l1ll_opy_ (u"ࠧࡹࡣࡢࡰࠥᆓ"):
                        result = self.perform_scan(driver, method=bstack1ll1l1111ll_opy_, framework_name=f.framework_name)
                    instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠨࡡ࠲࠳ࡼ࠾ࠧᆔ") + script_name, datetime.now() - bstack11l1l1111_opy_)
                    if isinstance(result, dict) and not result.get(bstack1l1ll_opy_ (u"ࠢࡴࡷࡦࡧࡪࡹࡳࠣᆕ"), True):
                        self.logger.warning(bstack1l1ll_opy_ (u"ࠣࡵ࡮࡭ࡵࠦࡥࡹࡧࡦࡹࡹ࡯࡮ࡨࠢࡵࡩࡲࡧࡩ࡯࡫ࡱ࡫ࠥࡹࡣࡳ࡫ࡳࡸࡸࡀࠠࠣᆖ") + str(result) + bstack1l1ll_opy_ (u"ࠤࠥᆗ"))
                        break
                except Exception as e:
                    self.logger.error(bstack1l1ll_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠢࡨࡼࡪࡩࡵࡵ࡫ࡱ࡫ࠥࡹࡣࡳ࡫ࡳࡸࡂࢁࡳࡤࡴ࡬ࡴࡹࡥ࡮ࡢ࡯ࡨࢁࠥ࡫ࡲࡳࡱࡵࡁࠧᆘ") + str(e) + bstack1l1ll_opy_ (u"ࠦࠧᆙ"))
        except Exception as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡧࡻࡩࡨࡻࡴࡦࠢࡨࡶࡷࡵࡲ࠾ࠤᆚ") + str(e) + bstack1l1ll_opy_ (u"ࠨࠢᆛ"))
    def bstack1ll11l11lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll1111_opy_,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        *args,
        **kwargs,
    ):
        tags = self._1ll1l111l11_opy_(instance, args)
        capabilities = self.bstack1ll11lll11l_opy_.bstack1ll1l11l1l1_opy_(f, instance, bstack1llllllll11_opy_, *args, **kwargs)
        self.accessibility = self.bstack1ll1l11111l_opy_(tags, capabilities)
        if not self.accessibility:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠢࡰࡰࡢࡥ࡫ࡺࡥࡳࡡࡷࡩࡸࡺ࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡩࡳࡧࡢ࡭ࡧࡧࠦᆜ"))
            return
        driver = self.bstack1ll11lll11l_opy_.bstack1ll11ll111l_opy_(f, instance, bstack1llllllll11_opy_, *args, **kwargs)
        test_name = f.bstack1lllll111ll_opy_(instance, TestFramework.bstack1ll111l11ll_opy_)
        if not test_name:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡱࡱࡣࡦ࡬ࡴࡦࡴࡢࡸࡪࡹࡴ࠻ࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡰࡤࡱࡪࠨᆝ"))
            return
        test_uuid = f.bstack1lllll111ll_opy_(instance, TestFramework.bstack1ll11l111l1_opy_)
        if not test_uuid:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠤࡲࡲࡤࡧࡦࡵࡧࡵࡣࡹ࡫ࡳࡵ࠼ࠣࡱ࡮ࡹࡳࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡸࡹ࡮ࡪࠢᆞ"))
            return
        if isinstance(self.bstack1ll11lll11l_opy_, bstack1ll1ll111ll_opy_):
            framework_name = bstack1l1ll_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᆟ")
        else:
            framework_name = bstack1l1ll_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ᆠ")
        self.bstack1lll1llll1_opy_(driver, test_name, framework_name, test_uuid)
    def perform_scan(self, driver: object, method: Union[None, str], framework_name: str):
        bstack1ll1l11l11l_opy_ = bstack1llll11l1l1_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack111ll1ll_opy_.value)
        if not self.accessibility:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡶࡥࡳࡨࡲࡶࡲࡥࡳࡤࡣࡱ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࠨᆡ"))
            return
        bstack11l1l1111_opy_ = datetime.now()
        bstack1ll1111lll1_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1ll_opy_ (u"ࠨࡳࡤࡣࡱࠦᆢ"), None)
        if not bstack1ll1111lll1_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠢࡱࡧࡵࡪࡴࡸ࡭ࡠࡵࡦࡥࡳࡀࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࠩࡶࡧࡦࡴࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᆣ") + str(framework_name) + bstack1l1ll_opy_ (u"ࠣࠢࠥᆤ"))
            return
        if self.bstack1ll11l1lll1_opy_:
            arg = dict()
            arg[bstack1l1ll_opy_ (u"ࠤࡰࡩࡹ࡮࡯ࡥࠤᆥ")] = method if method else bstack1l1ll_opy_ (u"ࠥࠦᆦ")
            arg[bstack1l1ll_opy_ (u"ࠦࡹ࡮ࡔࡦࡵࡷࡖࡺࡴࡕࡶ࡫ࡧࠦᆧ")] = self.bstack1ll111lllll_opy_[bstack1l1ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠧᆨ")]
            arg[bstack1l1ll_opy_ (u"ࠨࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠦᆩ")] = self.bstack1ll111lllll_opy_[bstack1l1ll_opy_ (u"ࠢࡵࡧࡶࡸ࡭ࡻࡢࡠࡤࡸ࡭ࡱࡪ࡟ࡶࡷ࡬ࡨࠧᆪ")]
            arg[bstack1l1ll_opy_ (u"ࠣࡣࡸࡸ࡭ࡎࡥࡢࡦࡨࡶࠧᆫ")] = self.bstack1ll111lllll_opy_[bstack1l1ll_opy_ (u"ࠤࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡖࡲ࡯ࡪࡴࠢᆬ")]
            arg[bstack1l1ll_opy_ (u"ࠥࡸ࡭ࡐࡷࡵࡖࡲ࡯ࡪࡴࠢᆭ")] = self.bstack1ll111lllll_opy_[bstack1l1ll_opy_ (u"ࠦࡹ࡮࡟࡫ࡹࡷࡣࡹࡵ࡫ࡦࡰࠥᆮ")]
            arg[bstack1l1ll_opy_ (u"ࠧࡹࡣࡢࡰࡗ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠧᆯ")] = str(int(datetime.now().timestamp() * 1000))
            bstack1ll11l11111_opy_ = bstack1ll1111lll1_opy_ % json.dumps(arg)
            driver.execute_script(bstack1ll11l11111_opy_)
            return
        instance = bstack11111111l1_opy_.bstack1lllll1l11l_opy_(driver)
        if instance:
            if not bstack11111111l1_opy_.bstack1lllll111ll_opy_(instance, bstack1ll1l1l1ll1_opy_.bstack1ll11l1l1l1_opy_, False):
                bstack11111111l1_opy_.bstack1lllll1l111_opy_(instance, bstack1ll1l1l1ll1_opy_.bstack1ll11l1l1l1_opy_, True)
            else:
                self.logger.info(bstack1l1ll_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡪࡰࠣࡴࡷࡵࡧࡳࡧࡶࡷࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࡻࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࡾࠢࡰࡩࡹ࡮࡯ࡥ࠿ࠥᆰ") + str(method) + bstack1l1ll_opy_ (u"ࠢࠣᆱ"))
                return
        self.logger.info(bstack1l1ll_opy_ (u"ࠣࡲࡨࡶ࡫ࡵࡲ࡮ࡡࡶࡧࡦࡴ࠺ࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦ࠿ࡾࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࢁࠥࡳࡥࡵࡪࡲࡨࡂࠨᆲ") + str(method) + bstack1l1ll_opy_ (u"ࠤࠥᆳ"))
        if framework_name == bstack1l1ll_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᆴ"):
            result = self.bstack1ll11lll11l_opy_.bstack1ll11llll1l_opy_(driver, bstack1ll1111lll1_opy_)
        else:
            result = driver.execute_async_script(bstack1ll1111lll1_opy_, {bstack1l1ll_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࠦᆵ"): method if method else bstack1l1ll_opy_ (u"ࠧࠨᆶ")})
        bstack1llll11l1l1_opy_.end(EVENTS.bstack111ll1ll_opy_.value, bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᆷ"), bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᆸ"), True, None, command=method)
        if instance:
            bstack11111111l1_opy_.bstack1lllll1l111_opy_(instance, bstack1ll1l1l1ll1_opy_.bstack1ll11l1l1l1_opy_, False)
            instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠣࡣ࠴࠵ࡾࡀࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲࠧᆹ"), datetime.now() - bstack11l1l1111_opy_)
        return result
        def bstack1ll111l1l1l_opy_(self, driver: object, framework_name, bstack11lll1l1_opy_: str):
            self.bstack1ll1111ll11_opy_()
            req = structs.AccessibilityResultRequest()
            req.bin_session_id = self.bin_session_id
            req.bstack1ll11l11ll1_opy_ = self.bstack1ll111lllll_opy_[bstack1l1ll_opy_ (u"ࠤࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠤᆺ")]
            req.bstack11lll1l1_opy_ = bstack11lll1l1_opy_
            req.session_id = self.bin_session_id
            try:
                r = self.bstack1lll1ll111l_opy_.AccessibilityResult(req)
                if not r.success:
                    self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥ࡬ࡲࡰ࡯ࠣࡷࡪࡸࡶࡦࡴ࠽ࠤࠧᆻ") + str(r) + bstack1l1ll_opy_ (u"ࠦࠧᆼ"))
                else:
                    bstack1ll11l111ll_opy_ = json.loads(r.bstack1ll11llllll_opy_.decode(bstack1l1ll_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᆽ")))
                    if bstack11lll1l1_opy_ == bstack1l1ll_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠪᆾ"):
                        return bstack1ll11l111ll_opy_.get(bstack1l1ll_opy_ (u"ࠢࡥࡣࡷࡥࠧᆿ"), [])
                    else:
                        return bstack1ll11l111ll_opy_.get(bstack1l1ll_opy_ (u"ࠣࡦࡤࡸࡦࠨᇀ"), {})
            except grpc.RpcError as e:
                self.logger.error(bstack1l1ll_opy_ (u"ࠤࡵࡴࡨ࠳ࡥࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡧࡦࡶࡢࡥࡵࡶ࡟ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ࡟ࡳࡧࡶࡹࡱࡺࠠࡧࡴࡲࡱࠥࡩ࡬ࡪ࠼ࠣࠦᇁ") + str(e) + bstack1l1ll_opy_ (u"ࠥࠦᇂ"))
    @measure(event_name=EVENTS.bstack11l1l1l11_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def get_accessibility_results(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠦ࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡴࡨࡷࡺࡲࡴࡴ࠼ࠣࡥ࠶࠷ࡹࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠨᇃ"))
            return
        if self.bstack1ll11l1lll1_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࡦࡶࡰࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨᇄ"))
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1ll111l1l1l_opy_(driver, framework_name, bstack1l1ll_opy_ (u"ࠨࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠥᇅ"))
        bstack1ll1111lll1_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1ll_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠦᇆ"), None)
        if not bstack1ll1111lll1_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᇇ") + str(framework_name) + bstack1l1ll_opy_ (u"ࠤࠥᇈ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11l1l1111_opy_ = datetime.now()
        if framework_name == bstack1l1ll_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᇉ"):
            result = self.bstack1ll11lll11l_opy_.bstack1ll11llll1l_opy_(driver, bstack1ll1111lll1_opy_)
        else:
            result = driver.execute_async_script(bstack1ll1111lll1_opy_)
        instance = bstack11111111l1_opy_.bstack1lllll1l11l_opy_(driver)
        if instance:
            instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼ࡪࡩࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡲࡦࡵࡸࡰࡹࡹࠢᇊ"), datetime.now() - bstack11l1l1111_opy_)
        return result
    @measure(event_name=EVENTS.bstack1ll111l1ll_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def get_accessibility_results_summary(self, driver: object, framework_name):
        if not self.accessibility:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡵࡩࡸࡻ࡬ࡵࡵࡢࡷࡺࡳ࡭ࡢࡴࡼ࠾ࠥࡧ࠱࠲ࡻࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠣᇋ"))
            return
        if self.bstack1ll11l1lll1_opy_:
            self.perform_scan(driver, method=None, framework_name=framework_name)
            return self.bstack1ll111l1l1l_opy_(driver, framework_name, bstack1l1ll_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠪᇌ"))
        bstack1ll1111lll1_opy_ = self.scripts.get(framework_name, {}).get(bstack1l1ll_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠦᇍ"), None)
        if not bstack1ll1111lll1_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠣ࡯࡬ࡷࡸ࡯࡮ࡨࠢࠪ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠧࠡࡵࡦࡶ࡮ࡶࡴࠡࡨࡲࡶࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪࡃࠢᇎ") + str(framework_name) + bstack1l1ll_opy_ (u"ࠤࠥᇏ"))
            return
        self.perform_scan(driver, method=None, framework_name=framework_name)
        bstack11l1l1111_opy_ = datetime.now()
        if framework_name == bstack1l1ll_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧᇐ"):
            result = self.bstack1ll11lll11l_opy_.bstack1ll11llll1l_opy_(driver, bstack1ll1111lll1_opy_)
        else:
            result = driver.execute_async_script(bstack1ll1111lll1_opy_)
        instance = bstack11111111l1_opy_.bstack1lllll1l11l_opy_(driver)
        if instance:
            instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠦࡦ࠷࠱ࡺ࠼ࡪࡩࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡲࡦࡵࡸࡰࡹࡹ࡟ࡴࡷࡰࡱࡦࡸࡹࠣᇑ"), datetime.now() - bstack11l1l1111_opy_)
        return result
    @measure(event_name=EVENTS.bstack1ll11l1l11l_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def bstack1ll1111llll_opy_(
        self,
        platform_index: int,
        framework_name: str,
        framework_version: str,
        hub_url: str,
    ):
        self.bstack1ll1111ll11_opy_()
        req = structs.AccessibilityConfigRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = platform_index
        req.framework_name = framework_name
        req.framework_version = framework_version
        req.hub_url = hub_url
        try:
            r = self.bstack1lll1ll111l_opy_.AccessibilityConfig(req)
            if not r.success:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡸࡥࡤࡧ࡬ࡺࡪࡪࠠࡧࡴࡲࡱࠥࡹࡥࡳࡸࡨࡶ࠿ࠦࠢᇒ") + str(r) + bstack1l1ll_opy_ (u"ࠨࠢᇓ"))
            else:
                self.bstack1ll11ll1lll_opy_(framework_name, r)
            return r
        except grpc.RpcError as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠢࡳࡲࡦ࠱ࡪࡸࡲࡰࡴ࠽ࠤࠧᇔ") + str(e) + bstack1l1ll_opy_ (u"ࠣࠤᇕ"))
            traceback.print_exc()
            raise e
    def bstack1ll11ll1lll_opy_(self, framework_name: str, result: structs.AccessibilityConfigResponse) -> bool:
        if not result.success or not result.accessibility.success:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠤ࡯ࡳࡦࡪ࡟ࡤࡱࡱࡪ࡮࡭࠺ࠡࡣ࠴࠵ࡾࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠤᇖ"))
            return False
        if result.accessibility.is_app_accessibility:
            self.bstack1ll11l1lll1_opy_ = result.accessibility.is_app_accessibility
        if result.testhub.build_hashed_id:
            self.bstack1ll111lllll_opy_[bstack1l1ll_opy_ (u"ࠥࡸࡪࡹࡴࡩࡷࡥࡣࡧࡻࡩ࡭ࡦࡢࡹࡺ࡯ࡤࠣᇗ")] = result.testhub.build_hashed_id
        if result.testhub.jwt:
            self.bstack1ll111lllll_opy_[bstack1l1ll_opy_ (u"ࠦࡹ࡮࡟࡫ࡹࡷࡣࡹࡵ࡫ࡦࡰࠥᇘ")] = result.testhub.jwt
        if result.accessibility.options:
            options = result.accessibility.options
            if options.capabilities:
                for caps in options.capabilities:
                    self.bstack1ll111lllll_opy_[caps.name] = caps.value
            if options.scripts:
                self.scripts[framework_name] = {row.name: row.command for row in options.scripts}
            if options.commands_to_wrap and options.commands_to_wrap.commands:
                scripts_to_run = [s for s in options.commands_to_wrap.scripts_to_run]
                if not scripts_to_run:
                    return False
                bstack1ll111l1lll_opy_ = dict()
                for command in options.commands_to_wrap.commands:
                    if command.library == self.bstack1ll111l1l11_opy_ and command.module == self.bstack1ll11ll1l11_opy_:
                        if command.method and not command.method in bstack1ll111l1lll_opy_:
                            bstack1ll111l1lll_opy_[command.method] = dict()
                        if command.name and not command.name in bstack1ll111l1lll_opy_[command.method]:
                            bstack1ll111l1lll_opy_[command.method][command.name] = list()
                        bstack1ll111l1lll_opy_[command.method][command.name].extend(scripts_to_run)
                self.commands[framework_name] = bstack1ll111l1lll_opy_
        return bool(self.commands.get(framework_name, None))
    def bstack1ll1l11ll11_opy_(
        self,
        f: bstack1lll11lll1l_opy_,
        exec: Tuple[bstack1llll1ll1l1_opy_, str],
        *args,
        **kwargs,
    ):
        instance, method_name = exec
        if isinstance(self.bstack1ll11lll11l_opy_, bstack1ll1ll111ll_opy_) and method_name != bstack1l1ll_opy_ (u"ࠬࡩ࡯࡯ࡰࡨࡧࡹ࠭ᇙ"):
            return
        if bstack11111111l1_opy_.bstack1lllllllll1_opy_(instance, bstack1ll1l1l1ll1_opy_.bstack1ll11lll1ll_opy_):
            return
        if f.bstack1ll111ll1ll_opy_(method_name, *args):
            bstack1ll11lll111_opy_ = False
            desired_capabilities = f.bstack1ll11ll11ll_opy_(instance)
            if isinstance(desired_capabilities, dict):
                hub_url = f.bstack1ll1l11l111_opy_(instance)
                platform_index = f.bstack1lllll111ll_opy_(instance, bstack1lll11lll1l_opy_.bstack1ll111l111l_opy_, 0)
                bstack1ll1l11l1ll_opy_ = datetime.now()
                r = self.bstack1ll1111llll_opy_(platform_index, f.framework_name, f.framework_version, hub_url)
                instance.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡣࡨࡵ࡮ࡧ࡫ࡪࠦᇚ"), datetime.now() - bstack1ll1l11l1ll_opy_)
                bstack1ll11lll111_opy_ = r.success
            else:
                self.logger.error(bstack1l1ll_opy_ (u"ࠢ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡦࡨࡷ࡮ࡸࡥࡥࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳ࠾ࠤᇛ") + str(desired_capabilities) + bstack1l1ll_opy_ (u"ࠣࠤᇜ"))
            f.bstack1lllll1l111_opy_(instance, bstack1ll1l1l1ll1_opy_.bstack1ll11lll1ll_opy_, bstack1ll11lll111_opy_)
    def bstack1lllll1111_opy_(self, test_tags):
        bstack1ll1111llll_opy_ = self.config.get(bstack1l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩᇝ"))
        if not bstack1ll1111llll_opy_:
            return True
        try:
            include_tags = bstack1ll1111llll_opy_[bstack1l1ll_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨᇞ")] if bstack1l1ll_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩᇟ") in bstack1ll1111llll_opy_ and isinstance(bstack1ll1111llll_opy_[bstack1l1ll_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪᇠ")], list) else []
            exclude_tags = bstack1ll1111llll_opy_[bstack1l1ll_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫᇡ")] if bstack1l1ll_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬᇢ") in bstack1ll1111llll_opy_ and isinstance(bstack1ll1111llll_opy_[bstack1l1ll_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ᇣ")], list) else []
            excluded = any(tag in exclude_tags for tag in test_tags)
            included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
            return not excluded and included
        except Exception as error:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡷࡣ࡯࡭ࡩࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡧࡱࡵࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡧ࡫ࡦࡰࡴࡨࠤࡸࡩࡡ࡯ࡰ࡬ࡲ࡬࠴ࠠࡆࡴࡵࡳࡷࠦ࠺ࠡࠤᇤ") + str(error))
        return False
    def bstack1ll1llllll_opy_(self, caps):
        try:
            if self.bstack1ll11l1lll1_opy_:
                bstack1ll11l1l1ll_opy_ = caps.get(bstack1l1ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤᇥ"))
                if bstack1ll11l1l1ll_opy_ is not None and str(bstack1ll11l1l1ll_opy_).lower() == bstack1l1ll_opy_ (u"ࠦࡦࡴࡤࡳࡱ࡬ࡨࠧᇦ"):
                    bstack1ll11l1llll_opy_ = caps.get(bstack1l1ll_opy_ (u"ࠧࡧࡰࡱ࡫ࡸࡱ࠿ࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢᇧ")) or caps.get(bstack1l1ll_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣᇨ"))
                    if bstack1ll11l1llll_opy_ is not None and int(bstack1ll11l1llll_opy_) < 11:
                        self.logger.warning(bstack1l1ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡂࡰࡧࡶࡴ࡯ࡤࠡ࠳࠴ࠤࡦࡴࡤࠡࡣࡥࡳࡻ࡫࠮ࠡࡅࡸࡶࡷ࡫࡮ࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡃࠢᇩ") + str(bstack1ll11l1llll_opy_) + bstack1l1ll_opy_ (u"ࠣࠤᇪ"))
                        return False
                return True
            bstack1ll111l11l1_opy_ = caps.get(bstack1l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᇫ"), {}).get(bstack1l1ll_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧᇬ"), caps.get(bstack1l1ll_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫᇭ"), bstack1l1ll_opy_ (u"ࠬ࠭ᇮ")))
            if bstack1ll111l11l1_opy_:
                self.logger.warning(bstack1l1ll_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡄࡦࡵ࡮ࡸࡴࡶࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥᇯ"))
                return False
            browser = caps.get(bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᇰ"), bstack1l1ll_opy_ (u"ࠨࠩᇱ")).lower()
            if browser != bstack1l1ll_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩᇲ"):
                self.logger.warning(bstack1l1ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨᇳ"))
                return False
            bstack1ll11l1ll11_opy_ = bstack1ll11ll1ll1_opy_
            if not self.config.get(bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭ᇴ")) or self.config.get(bstack1l1ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩᇵ")):
                bstack1ll11l1ll11_opy_ = bstack1ll1111ll1l_opy_
            browser_version = caps.get(bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᇶ"))
            if not browser_version:
                browser_version = caps.get(bstack1l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᇷ"), {}).get(bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᇸ"), bstack1l1ll_opy_ (u"ࠩࠪᇹ"))
            if browser_version and browser_version != bstack1l1ll_opy_ (u"ࠪࡰࡦࡺࡥࡴࡶࠪᇺ") and int(browser_version.split(bstack1l1ll_opy_ (u"ࠫ࠳࠭ᇻ"))[0]) <= bstack1ll11l1ll11_opy_:
                self.logger.warning(bstack1l1ll_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡨࡴࡨࡥࡹ࡫ࡲࠡࡶ࡫ࡥࡳࠦࠢᇼ") + str(bstack1ll11l1ll11_opy_) + bstack1l1ll_opy_ (u"ࠨ࠮ࠣᇽ"))
                return False
            bstack1ll111l1ll1_opy_ = caps.get(bstack1l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᇾ"), {}).get(bstack1l1ll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨᇿ"))
            if not bstack1ll111l1ll1_opy_:
                bstack1ll111l1ll1_opy_ = caps.get(bstack1l1ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧሀ"), {})
            if bstack1ll111l1ll1_opy_ and bstack1l1ll_opy_ (u"ࠪ࠱࠲࡮ࡥࡢࡦ࡯ࡩࡸࡹࠧሁ") in bstack1ll111l1ll1_opy_.get(bstack1l1ll_opy_ (u"ࠫࡦࡸࡧࡴࠩሂ"), []):
                self.logger.warning(bstack1l1ll_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠ࡯ࡱࡷࠤࡷࡻ࡮ࠡࡱࡱࠤࡱ࡫ࡧࡢࡥࡼࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲࡙ࠥࡷࡪࡶࡦ࡬ࠥࡺ࡯ࠡࡰࡨࡻࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩࠥࡵࡲࠡࡣࡹࡳ࡮ࡪࠠࡶࡵ࡬ࡲ࡬ࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠢሃ"))
                return False
            return True
        except Exception as error:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡼࡡ࡭࡫ࡧࡥࡹ࡫ࠠࡢ࠳࠴ࡽࠥࡹࡵࡱࡲࡲࡶࡹࠦ࠺ࠣሄ") + str(error))
            return False
    def bstack1ll111l1111_opy_(self, test_uuid: str, result: structs.FetchDriverExecuteParamsEventResponse):
        bstack1ll11ll11l1_opy_ = {
            bstack1l1ll_opy_ (u"ࠧࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠧህ"): test_uuid,
        }
        bstack1ll111lll11_opy_ = {}
        if result.success:
            bstack1ll111lll11_opy_ = json.loads(result.accessibility_execute_params)
        return bstack1ll1l111l1l_opy_(bstack1ll11ll11l1_opy_, bstack1ll111lll11_opy_)
    def bstack1lll1llll1_opy_(self, driver: object, name: str, framework_name: str, test_uuid: str):
        bstack1ll1l11l11l_opy_ = None
        try:
            self.bstack1ll1111ll11_opy_()
            req = structs.FetchDriverExecuteParamsEventRequest()
            req.bin_session_id = self.bin_session_id
            req.product = bstack1l1ll_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠣሆ")
            req.script_name = bstack1l1ll_opy_ (u"ࠤࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠢሇ")
            r = self.bstack1lll1ll111l_opy_.FetchDriverExecuteParamsEvent(req)
            if not r.success:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡶࡪࡩࡥࡪࡸࡨࡨࠥࡪࡲࡪࡸࡨࡶࠥ࡫ࡸࡦࡥࡸࡸࡪࠦࡰࡢࡴࡤࡱࡸࠦࡦࡳࡱࡰࠤࡸ࡫ࡲࡷࡧࡵ࠾ࠥࠨለ") + str(r.error) + bstack1l1ll_opy_ (u"ࠦࠧሉ"))
            else:
                bstack1ll11ll11l1_opy_ = self.bstack1ll111l1111_opy_(test_uuid, r)
                bstack1ll1111lll1_opy_ = r.script
            self.logger.debug(bstack1l1ll_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡣࡹ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨሊ") + str(bstack1ll11ll11l1_opy_))
            self.perform_scan(driver, name, framework_name=framework_name)
            if not bstack1ll1111lll1_opy_:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠨࡰࡦࡴࡩࡳࡷࡳ࡟ࡴࡥࡤࡲ࠿ࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࠨࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸ࠭ࠠࡴࡥࡵ࡭ࡵࡺࠠࡧࡱࡵࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࡂࠨላ") + str(framework_name) + bstack1l1ll_opy_ (u"ࠢࠡࠤሌ"))
                return
            bstack1ll1l11l11l_opy_ = bstack1llll11l1l1_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack1ll111lll1l_opy_.value)
            self.bstack1ll1l11ll1l_opy_(driver, bstack1ll1111lll1_opy_, bstack1ll11ll11l1_opy_, framework_name)
            self.logger.info(bstack1l1ll_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠦል"))
            bstack1llll11l1l1_opy_.end(EVENTS.bstack1ll111lll1l_opy_.value, bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤሎ"), bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠥ࠾ࡪࡴࡤࠣሏ"), True, None, command=bstack1l1ll_opy_ (u"ࠫࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠩሐ"),test_name=name)
        except Exception as bstack1ll111ll1l1_opy_:
            self.logger.error(bstack1l1ll_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡣࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡥࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡫ࡤࠡࡨࡲࡶࠥࡺࡨࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢሑ") + bstack1l1ll_opy_ (u"ࠨࡳࡵࡴࠫࡴࡦࡺࡨࠪࠤሒ") + bstack1l1ll_opy_ (u"ࠢࠡࡇࡵࡶࡴࡸࠠ࠻ࠤሓ") + str(bstack1ll111ll1l1_opy_))
            bstack1llll11l1l1_opy_.end(EVENTS.bstack1ll111lll1l_opy_.value, bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣሔ"), bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢሕ"), False, bstack1ll111ll1l1_opy_, command=bstack1l1ll_opy_ (u"ࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨሖ"),test_name=name)
    def bstack1ll1l11ll1l_opy_(self, driver, bstack1ll1111lll1_opy_, bstack1ll11ll11l1_opy_, framework_name):
        if framework_name == bstack1l1ll_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨሗ"):
            self.bstack1ll11lll11l_opy_.bstack1ll11llll1l_opy_(driver, bstack1ll1111lll1_opy_, bstack1ll11ll11l1_opy_)
        else:
            self.logger.debug(driver.execute_async_script(bstack1ll1111lll1_opy_, bstack1ll11ll11l1_opy_))
    def _1ll1l111l11_opy_(self, instance: bstack1lll1ll1111_opy_, args: Tuple) -> list:
        bstack1l1ll_opy_ (u"ࠧࠨࠢࡆࡺࡷࡶࡦࡩࡴࠡࡶࡤ࡫ࡸࠦࡢࡢࡵࡨࡨࠥࡵ࡮ࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠴ࠢࠣࠤመ")
        if bstack1l1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠪሙ") in instance.bstack1ll1l111111_opy_:
            return args[2].tags if hasattr(args[2], bstack1l1ll_opy_ (u"ࠧࡵࡣࡪࡷࠬሚ")) else []
        if hasattr(args[0], bstack1l1ll_opy_ (u"ࠨࡱࡺࡲࡤࡳࡡࡳ࡭ࡨࡶࡸ࠭ማ")):
            return [marker.name for marker in args[0].own_markers]
        return []
    def bstack1ll1l11111l_opy_(self, tags, capabilities):
        return self.bstack1lllll1111_opy_(tags) and self.bstack1ll1llllll_opy_(capabilities)