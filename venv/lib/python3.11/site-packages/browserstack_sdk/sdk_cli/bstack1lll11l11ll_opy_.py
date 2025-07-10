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
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1llllllll1l_opy_ import (
    bstack1lllll1lll1_opy_,
    bstack1llll1lllll_opy_,
    bstack1llll1ll1l1_opy_,
    bstack1111111l11_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1l1ll1111ll_opy_, bstack1lll11l111_opy_
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll11lll1l_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11ll11_opy_, bstack1lll1111lll_opy_, bstack1lll1ll1111_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll1l1l_opy_ import bstack1ll1lllll11_opy_
from browserstack_sdk.sdk_cli.bstack1l1llll1lll_opy_ import bstack1l1lllll111_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack1l1l11l11_opy_ import bstack1l1ll11lll_opy_, bstack1l1l111l1_opy_, bstack1111l1ll_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1ll1ll111ll_opy_(bstack1l1lllll111_opy_):
    bstack1l1l111l1l1_opy_ = bstack1l1ll_opy_ (u"ࠢࡵࡧࡶࡸࡤࡪࡲࡪࡸࡨࡶࡸࠨጁ")
    bstack1l1l1llllll_opy_ = bstack1l1ll_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢጂ")
    bstack1l1l111l111_opy_ = bstack1l1ll_opy_ (u"ࠤࡱࡳࡳࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦጃ")
    bstack1l11lllll1l_opy_ = bstack1l1ll_opy_ (u"ࠥࡸࡪࡹࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࠥጄ")
    bstack1l1l111ll11_opy_ = bstack1l1ll_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡷࡹࡧ࡮ࡤࡧࡢࡶࡪ࡬ࡳࠣጅ")
    bstack1l1lll11ll1_opy_ = bstack1l1ll_opy_ (u"ࠧࡩࡢࡵࡡࡶࡩࡸࡹࡩࡰࡰࡢࡧࡷ࡫ࡡࡵࡧࡧࠦጆ")
    bstack1l1l11111ll_opy_ = bstack1l1ll_opy_ (u"ࠨࡣࡣࡶࡢࡷࡪࡹࡳࡪࡱࡱࡣࡳࡧ࡭ࡦࠤጇ")
    bstack1l1l111ll1l_opy_ = bstack1l1ll_opy_ (u"ࠢࡤࡤࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡹࡴࡢࡶࡸࡷࠧገ")
    def __init__(self):
        super().__init__(bstack1l1llllll11_opy_=self.bstack1l1l111l1l1_opy_, frameworks=[bstack1lll11lll1l_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1ll111ll111_opy_((bstack1llll11ll11_opy_.BEFORE_EACH, bstack1lll1111lll_opy_.POST), self.bstack1l11llllll1_opy_)
        if bstack1lll11l111_opy_():
            TestFramework.bstack1ll111ll111_opy_((bstack1llll11ll11_opy_.TEST, bstack1lll1111lll_opy_.POST), self.bstack1ll11l1111l_opy_)
        else:
            TestFramework.bstack1ll111ll111_opy_((bstack1llll11ll11_opy_.TEST, bstack1lll1111lll_opy_.PRE), self.bstack1ll11l1111l_opy_)
        TestFramework.bstack1ll111ll111_opy_((bstack1llll11ll11_opy_.TEST, bstack1lll1111lll_opy_.POST), self.bstack1ll11l11lll_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1l11llllll1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll1111_opy_,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        *args,
        **kwargs,
    ):
        bstack1l1l111lll1_opy_ = self.bstack1l1l111l11l_opy_(instance.context)
        if not bstack1l1l111lll1_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡵࡨࡸࡤࡧࡣࡵ࡫ࡹࡩࡤࡶࡡࡨࡧ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࠨጉ") + str(bstack1llllllll11_opy_) + bstack1l1ll_opy_ (u"ࠤࠥጊ"))
            return
        f.bstack1lllll1l111_opy_(instance, bstack1ll1ll111ll_opy_.bstack1l1l1llllll_opy_, bstack1l1l111lll1_opy_)
    def bstack1l1l111l11l_opy_(self, context: bstack1111111l11_opy_, bstack1l1l1111l11_opy_= True):
        if bstack1l1l1111l11_opy_:
            bstack1l1l111lll1_opy_ = self.bstack1l1llll1l11_opy_(context, reverse=True)
        else:
            bstack1l1l111lll1_opy_ = self.bstack1l1llllll1l_opy_(context, reverse=True)
        return [f for f in bstack1l1l111lll1_opy_ if f[1].state != bstack1lllll1lll1_opy_.QUIT]
    def bstack1ll11l1111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll1111_opy_,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11llllll1_opy_(f, instance, bstack1llllllll11_opy_, *args, **kwargs)
        if not bstack1l1ll1111ll_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨጋ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠦࠧጌ"))
            return
        bstack1l1l111lll1_opy_ = f.bstack1lllll111ll_opy_(instance, bstack1ll1ll111ll_opy_.bstack1l1l1llllll_opy_, [])
        if not bstack1l1l111lll1_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣግ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠨࠢጎ"))
            return
        if len(bstack1l1l111lll1_opy_) > 1:
            self.logger.debug(
                bstack1llll1l1l1l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡱࡣࡪࡩࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤጏ"))
        bstack1l1l1111lll_opy_, bstack1l1l1l1lll1_opy_ = bstack1l1l111lll1_opy_[0]
        page = bstack1l1l1111lll_opy_()
        if not page:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣጐ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠤࠥ጑"))
            return
        bstack1l1ll11l1l_opy_ = getattr(args[0], bstack1l1ll_opy_ (u"ࠥࡲࡴࡪࡥࡪࡦࠥጒ"), None)
        try:
            page.evaluate(bstack1l1ll_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧጓ"),
                        bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠩጔ") + json.dumps(
                            bstack1l1ll11l1l_opy_) + bstack1l1ll_opy_ (u"ࠨࡽࡾࠤጕ"))
        except Exception as e:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢࡾࢁࠧ጖"), e)
    def bstack1ll11l11lll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll1111_opy_,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11llllll1_opy_(f, instance, bstack1llllllll11_opy_, *args, **kwargs)
        if not bstack1l1ll1111ll_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡲࡴࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡧࡱࡵࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࠦ጗") + str(kwargs) + bstack1l1ll_opy_ (u"ࠤࠥጘ"))
            return
        bstack1l1l111lll1_opy_ = f.bstack1lllll111ll_opy_(instance, bstack1ll1ll111ll_opy_.bstack1l1l1llllll_opy_, [])
        if not bstack1l1l111lll1_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡳࡳࡥࡢࡦࡨࡲࡶࡪࡥࡴࡦࡵࡷ࠾ࠥࡴ࡯ࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨጙ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠦࠧጚ"))
            return
        if len(bstack1l1l111lll1_opy_) > 1:
            self.logger.debug(
                bstack1llll1l1l1l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠࡼ࡮ࡨࡲ࠭ࡶࡡࡨࡧࡢ࡭ࡳࡹࡴࡢࡰࡦࡩࡸ࠯ࡽࠡࡦࡵ࡭ࡻ࡫ࡲࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࢁ࡫ࡸࡣࡵ࡫ࡸࢃࠢጛ"))
        bstack1l1l1111lll_opy_, bstack1l1l1l1lll1_opy_ = bstack1l1l111lll1_opy_[0]
        page = bstack1l1l1111lll_opy_()
        if not page:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨጜ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠢࠣጝ"))
            return
        status = f.bstack1lllll111ll_opy_(instance, TestFramework.bstack1l1l111l1ll_opy_, None)
        if not status:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡰࡲࠤࡸࡺࡡࡵࡷࡶࠤ࡫ࡵࡲࠡࡶࡨࡷࡹ࠲ࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࠦጞ") + str(bstack1llllllll11_opy_) + bstack1l1ll_opy_ (u"ࠤࠥጟ"))
            return
        bstack1l1l1111ll1_opy_ = {bstack1l1ll_opy_ (u"ࠥࡷࡹࡧࡴࡶࡵࠥጠ"): status.lower()}
        bstack1l11lllllll_opy_ = f.bstack1lllll111ll_opy_(instance, TestFramework.bstack1l1l11111l1_opy_, None)
        if status.lower() == bstack1l1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫጡ") and bstack1l11lllllll_opy_ is not None:
            bstack1l1l1111ll1_opy_[bstack1l1ll_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬጢ")] = bstack1l11lllllll_opy_[0][bstack1l1ll_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩጣ")][0] if isinstance(bstack1l11lllllll_opy_, list) else str(bstack1l11lllllll_opy_)
        try:
              page.evaluate(
                    bstack1l1ll_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣጤ"),
                    bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥ࠭ጥ")
                    + json.dumps(bstack1l1l1111ll1_opy_)
                    + bstack1l1ll_opy_ (u"ࠤࢀࠦጦ")
                )
        except Exception as e:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡼࡿࠥጧ"), e)
    def bstack1l1ll1l11l1_opy_(
        self,
        instance: bstack1lll1ll1111_opy_,
        f: TestFramework,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11llllll1_opy_(f, instance, bstack1llllllll11_opy_, *args, **kwargs)
        if not bstack1l1ll1111ll_opy_:
            self.logger.debug(
                bstack1llll1l1l1l_opy_ (u"ࠦࡲࡧࡲ࡬ࡡࡲ࠵࠶ࡿ࡟ࡴࡻࡱࡧ࠿ࠦ࡮ࡰࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵ࠽ࡼࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࢁࠥࡧࡲࡨࡵࡀࡿࡦࡸࡧࡴࡿࠣ࡯ࡼࡧࡲࡨࡵࡀࡿࡰࡽࡡࡳࡩࡶࢁࠧጨ"))
            return
        bstack1l1l111lll1_opy_ = f.bstack1lllll111ll_opy_(instance, bstack1ll1ll111ll_opy_.bstack1l1l1llllll_opy_, [])
        if not bstack1l1l111lll1_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣጩ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠨࠢጪ"))
            return
        if len(bstack1l1l111lll1_opy_) > 1:
            self.logger.debug(
                bstack1llll1l1l1l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡾࡰࡪࡴࠨࡱࡣࡪࡩࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࡼ࡭ࡺࡥࡷ࡭ࡳࡾࠤጫ"))
        bstack1l1l1111lll_opy_, bstack1l1l1l1lll1_opy_ = bstack1l1l111lll1_opy_[0]
        page = bstack1l1l1111lll_opy_()
        if not page:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠣ࡯ࡤࡶࡰࡥ࡯࠲࠳ࡼࡣࡸࡿ࡮ࡤ࠼ࠣࡲࡴࠦࡰࡢࡩࡨࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣጬ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠤࠥጭ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack1l1ll_opy_ (u"ࠥࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࡖࡽࡳࡩ࠺ࠣጮ") + str(timestamp)
        try:
            page.evaluate(
                bstack1l1ll_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧጯ"),
                bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪጰ").format(
                    json.dumps(
                        {
                            bstack1l1ll_opy_ (u"ࠨࡡࡤࡶ࡬ࡳࡳࠨጱ"): bstack1l1ll_opy_ (u"ࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤጲ"),
                            bstack1l1ll_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦጳ"): {
                                bstack1l1ll_opy_ (u"ࠤࡷࡽࡵ࡫ࠢጴ"): bstack1l1ll_opy_ (u"ࠥࡅࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠢጵ"),
                                bstack1l1ll_opy_ (u"ࠦࡩࡧࡴࡢࠤጶ"): data,
                                bstack1l1ll_opy_ (u"ࠧࡲࡥࡷࡧ࡯ࠦጷ"): bstack1l1ll_opy_ (u"ࠨࡤࡦࡤࡸ࡫ࠧጸ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡳ࠶࠷ࡹࠡࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡻࡾࠤጹ"), e)
    def bstack1l1ll1ll111_opy_(
        self,
        instance: bstack1lll1ll1111_opy_,
        f: TestFramework,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1l11llllll1_opy_(f, instance, bstack1llllllll11_opy_, *args, **kwargs)
        if f.bstack1lllll111ll_opy_(instance, bstack1ll1ll111ll_opy_.bstack1l1lll11ll1_opy_, False):
            return
        self.bstack1ll1111ll11_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1ll111l111l_opy_)
        req.test_framework_name = TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1ll11llll11_opy_)
        req.test_framework_version = TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1l1ll1ll11l_opy_)
        req.test_framework_state = bstack1llllllll11_opy_[0].name
        req.test_hook_state = bstack1llllllll11_opy_[1].name
        req.test_uuid = TestFramework.bstack1lllll111ll_opy_(instance, TestFramework.bstack1ll11l111l1_opy_)
        for bstack1l1l1111l1l_opy_ in bstack1ll1lllll11_opy_.bstack1llllllllll_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack1l1ll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠢጺ")
                if bstack1l1ll1111ll_opy_
                else bstack1l1ll_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࡢ࡫ࡷ࡯ࡤࠣጻ")
            )
            session.ref = bstack1l1l1111l1l_opy_.ref()
            session.hub_url = bstack1ll1lllll11_opy_.bstack1lllll111ll_opy_(bstack1l1l1111l1l_opy_, bstack1ll1lllll11_opy_.bstack1l1l11l111l_opy_, bstack1l1ll_opy_ (u"ࠥࠦጼ"))
            session.framework_name = bstack1l1l1111l1l_opy_.framework_name
            session.framework_version = bstack1l1l1111l1l_opy_.framework_version
            session.framework_session_id = bstack1ll1lllll11_opy_.bstack1lllll111ll_opy_(bstack1l1l1111l1l_opy_, bstack1ll1lllll11_opy_.bstack1l1l11l1l1l_opy_, bstack1l1ll_opy_ (u"ࠦࠧጽ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1ll11ll111l_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll1111_opy_,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        *args,
        **kwargs
    ):
        bstack1l1l111lll1_opy_ = f.bstack1lllll111ll_opy_(instance, bstack1ll1ll111ll_opy_.bstack1l1l1llllll_opy_, [])
        if not bstack1l1l111lll1_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠧ࡭ࡥࡵࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡤࡳ࡫ࡹࡩࡷࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࡴࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࡾ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࢃࠠࡢࡴࡪࡷࡂࢁࡡࡳࡩࡶࢁࠥࡱࡷࡢࡴࡪࡷࡂࠨጾ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠨࠢጿ"))
            return
        if len(bstack1l1l111lll1_opy_) > 1:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠢࡨࡧࡷࡣࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾࡰࡪࡴࠨࡱࡣࡪࡩࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫ࡳࠪࡿࠣࡨࡷ࡯ࡶࡦࡴࡶࠤ࡫ࡵࡲࠡࡪࡲࡳࡰࡥࡩ࡯ࡨࡲࡁࢀ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯ࡾࠢࡤࡶ࡬ࡹ࠽ࡼࡣࡵ࡫ࡸࢃࠠ࡬ࡹࡤࡶ࡬ࡹ࠽ࠣፀ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠣࠤፁ"))
        bstack1l1l1111lll_opy_, bstack1l1l1l1lll1_opy_ = bstack1l1l111lll1_opy_[0]
        page = bstack1l1l1111lll_opy_()
        if not page:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠤࡪࡩࡹࡥࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡨࡷ࡯ࡶࡦࡴ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤፂ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠥࠦፃ"))
            return
        return page
    def bstack1ll1l11l1l1_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1ll1111_opy_,
        bstack1llllllll11_opy_: Tuple[bstack1llll11ll11_opy_, bstack1lll1111lll_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1l1l111111l_opy_ = {}
        for bstack1l1l1111l1l_opy_ in bstack1ll1lllll11_opy_.bstack1llllllllll_opy_.values():
            caps = bstack1ll1lllll11_opy_.bstack1lllll111ll_opy_(bstack1l1l1111l1l_opy_, bstack1ll1lllll11_opy_.bstack1l1l11l1lll_opy_, bstack1l1ll_opy_ (u"ࠦࠧፄ"))
        bstack1l1l111111l_opy_[bstack1l1ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥፅ")] = caps.get(bstack1l1ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࠢፆ"), bstack1l1ll_opy_ (u"ࠢࠣፇ"))
        bstack1l1l111111l_opy_[bstack1l1ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢፈ")] = caps.get(bstack1l1ll_opy_ (u"ࠤࡲࡷࠧፉ"), bstack1l1ll_opy_ (u"ࠥࠦፊ"))
        bstack1l1l111111l_opy_[bstack1l1ll_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨፋ")] = caps.get(bstack1l1ll_opy_ (u"ࠧࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠤፌ"), bstack1l1ll_opy_ (u"ࠨࠢፍ"))
        bstack1l1l111111l_opy_[bstack1l1ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣፎ")] = caps.get(bstack1l1ll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠥፏ"), bstack1l1ll_opy_ (u"ࠤࠥፐ"))
        return bstack1l1l111111l_opy_
    def bstack1ll11llll1l_opy_(self, page: object, bstack1ll1111lll1_opy_, args={}):
        try:
            bstack1l1l1111111_opy_ = bstack1l1ll_opy_ (u"ࠥࠦࠧ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࠪ࠱࠲࠳ࡨࡳࡵࡣࡦ࡯ࡘࡪ࡫ࡂࡴࡪࡷ࠮ࠦࡻࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡳ࡫ࡷࠡࡒࡵࡳࡲ࡯ࡳࡦࠪࠫࡶࡪࡹ࡯࡭ࡸࡨ࠰ࠥࡸࡥ࡫ࡧࡦࡸ࠮ࠦ࠽࠿ࠢࡾࡿࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡧࡹࡴࡢࡥ࡮ࡗࡩࡱࡁࡳࡩࡶ࠲ࡵࡻࡳࡩࠪࡵࡩࡸࡵ࡬ࡷࡧࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢀ࡬࡮ࡠࡤࡲࡨࡾࢃࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࢁ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࡽࠪࠪࡾࡥࡷ࡭࡟࡫ࡵࡲࡲࢂ࠯ࠢࠣࠤፑ")
            bstack1ll1111lll1_opy_ = bstack1ll1111lll1_opy_.replace(bstack1l1ll_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢፒ"), bstack1l1ll_opy_ (u"ࠧࡨࡳࡵࡣࡦ࡯ࡘࡪ࡫ࡂࡴࡪࡷࠧፓ"))
            script = bstack1l1l1111111_opy_.format(fn_body=bstack1ll1111lll1_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠨࡡ࠲࠳ࡼࡣࡸࡩࡲࡪࡲࡷࡣࡪࡾࡥࡤࡷࡷࡩ࠿ࠦࡅࡳࡴࡲࡶࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡧ࠱࠲ࡻࠣࡷࡨࡸࡩࡱࡶ࠯ࠤࠧፔ") + str(e) + bstack1l1ll_opy_ (u"ࠢࠣፕ"))