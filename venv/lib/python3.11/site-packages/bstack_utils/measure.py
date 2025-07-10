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
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack1l1111111_opy_ import get_logger
from bstack_utils.bstack11l1l111l_opy_ import bstack1llll11l1l1_opy_
bstack11l1l111l_opy_ = bstack1llll11l1l1_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1l1ll11l1l_opy_: Optional[str] = None):
    bstack1l1ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡄࡦࡥࡲࡶࡦࡺ࡯ࡳࠢࡷࡳࠥࡲ࡯ࡨࠢࡷ࡬ࡪࠦࡳࡵࡣࡵࡸࠥࡺࡩ࡮ࡧࠣࡳ࡫ࠦࡡࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࡥࡱࡵ࡮ࡨࠢࡺ࡭ࡹ࡮ࠠࡦࡸࡨࡲࡹࠦ࡮ࡢ࡯ࡨࠤࡦࡴࡤࠡࡵࡷࡥ࡬࡫࠮ࠋࠢࠣࠤࠥࠨࠢࠣᶕ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll1l11l11l_opy_: str = bstack11l1l111l_opy_.bstack11ll1l11l11_opy_(label)
            start_mark: str = label + bstack1l1ll_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᶖ")
            end_mark: str = label + bstack1l1ll_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᶗ")
            result = None
            try:
                if stage.value == STAGE.bstack1l1llllll_opy_.value:
                    bstack11l1l111l_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack11l1l111l_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1l1ll11l1l_opy_)
                elif stage.value == STAGE.bstack11ll1l11ll_opy_.value:
                    start_mark: str = bstack1ll1l11l11l_opy_ + bstack1l1ll_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᶘ")
                    end_mark: str = bstack1ll1l11l11l_opy_ + bstack1l1ll_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᶙ")
                    bstack11l1l111l_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack11l1l111l_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1l1ll11l1l_opy_)
            except Exception as e:
                bstack11l1l111l_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1l1ll11l1l_opy_)
            return result
        return wrapper
    return decorator