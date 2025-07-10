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
import re
from typing import List, Dict, Any
from bstack_utils.bstack1l1111111_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll1l1ll11l_opy_:
    bstack1l1ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡅࡸࡷࡹࡵ࡭ࡕࡣࡪࡑࡦࡴࡡࡨࡧࡵࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡸࠦࡵࡵ࡫࡯࡭ࡹࡿࠠ࡮ࡧࡷ࡬ࡴࡪࡳࠡࡶࡲࠤࡸ࡫ࡴࠡࡣࡱࡨࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡤࡷࡶࡸࡴࡳࠠࡵࡣࡪࠤࡲ࡫ࡴࡢࡦࡤࡸࡦ࠴ࠊࠡࠢࠣࠤࡎࡺࠠ࡮ࡣ࡬ࡲࡹࡧࡩ࡯ࡵࠣࡸࡼࡵࠠࡴࡧࡳࡥࡷࡧࡴࡦࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡩࡦࡵࠣࡪࡴࡸࠠࡵࡧࡶࡸࠥࡲࡥࡷࡧ࡯ࠤࡦࡴࡤࠡࡤࡸ࡭ࡱࡪࠠ࡭ࡧࡹࡩࡱࠦࡣࡶࡵࡷࡳࡲࠦࡴࡢࡩࡶ࠲ࠏࠦࠠࠡࠢࡈࡥࡨ࡮ࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡨࡲࡹࡸࡹࠡ࡫ࡶࠤࡪࡾࡰࡦࡥࡷࡩࡩࠦࡴࡰࠢࡥࡩࠥࡹࡴࡳࡷࡦࡸࡺࡸࡥࡥࠢࡤࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦ࡫ࡦࡻ࠽ࠤࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦ࡫࡯ࡥ࡭ࡦࡢࡸࡾࡶࡥࠣ࠼ࠣࠦࡲࡻ࡬ࡵ࡫ࡢࡨࡷࡵࡰࡥࡱࡺࡲࠧ࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡼࡡ࡭ࡷࡨࡷࠧࡀࠠ࡜࡮࡬ࡷࡹࠦ࡯ࡧࠢࡷࡥ࡬ࠦࡶࡢ࡮ࡸࡩࡸࡣࠊࠡࠢࠣࠤࠥࠦࠠࡾࠌࠣࠤࠥࠦࠢࠣࠤᗓ")
    _11llll111ll_opy_: Dict[str, Dict[str, Any]] = {}
    _11lll1llll1_opy_: Dict[str, Dict[str, Any]] = {}
    @staticmethod
    def set_custom_tag(bstack1lllll11_opy_: str, key_value: str, bstack11llll1111l_opy_: bool = False) -> None:
        if not bstack1lllll11_opy_ or not key_value or bstack1lllll11_opy_.strip() == bstack1l1ll_opy_ (u"ࠤࠥᗔ") or key_value.strip() == bstack1l1ll_opy_ (u"ࠥࠦᗕ"):
            logger.error(bstack1l1ll_opy_ (u"ࠦࡰ࡫ࡹࡠࡰࡤࡱࡪࠦࡡ࡯ࡦࠣ࡯ࡪࡿ࡟ࡷࡣ࡯ࡹࡪࠦ࡭ࡶࡵࡷࠤࡧ࡫ࠠ࡯ࡱࡱ࠱ࡳࡻ࡬࡭ࠢࡤࡲࡩࠦ࡮ࡰࡰ࠰ࡩࡲࡶࡴࡺࠤᗖ"))
        values: List[str] = bstack1ll1l1ll11l_opy_.bstack11llll11l1l_opy_(key_value)
        bstack11lll1lllll_opy_ = {bstack1l1ll_opy_ (u"ࠧ࡬ࡩࡦ࡮ࡧࡣࡹࡿࡰࡦࠤᗗ"): bstack1l1ll_opy_ (u"ࠨ࡭ࡶ࡮ࡷ࡭ࡤࡪࡲࡰࡲࡧࡳࡼࡴࠢᗘ"), bstack1l1ll_opy_ (u"ࠢࡷࡣ࡯ࡹࡪࡹࠢᗙ"): values}
        bstack11llll111l1_opy_ = bstack1ll1l1ll11l_opy_._11lll1llll1_opy_ if bstack11llll1111l_opy_ else bstack1ll1l1ll11l_opy_._11llll111ll_opy_
        if bstack1lllll11_opy_ in bstack11llll111l1_opy_:
            bstack11llll11111_opy_ = bstack11llll111l1_opy_[bstack1lllll11_opy_]
            bstack11lll1lll11_opy_ = bstack11llll11111_opy_.get(bstack1l1ll_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࡳࠣᗚ"), [])
            for val in values:
                if val not in bstack11lll1lll11_opy_:
                    bstack11lll1lll11_opy_.append(val)
            bstack11llll11111_opy_[bstack1l1ll_opy_ (u"ࠤࡹࡥࡱࡻࡥࡴࠤᗛ")] = bstack11lll1lll11_opy_
        else:
            bstack11llll111l1_opy_[bstack1lllll11_opy_] = bstack11lll1lllll_opy_
    @staticmethod
    def bstack11lllllll1l_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll1l1ll11l_opy_._11llll111ll_opy_
    @staticmethod
    def bstack11llll11l11_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll1l1ll11l_opy_._11lll1llll1_opy_
    @staticmethod
    def bstack11llll11l1l_opy_(bstack11lll1lll1l_opy_: str) -> List[str]:
        bstack1l1ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡔࡲ࡯࡭ࡹࡹࠠࡵࡪࡨࠤ࡮ࡴࡰࡶࡶࠣࡷࡹࡸࡩ࡯ࡩࠣࡦࡾࠦࡣࡰ࡯ࡰࡥࡸࠦࡷࡩ࡫࡯ࡩࠥࡸࡥࡴࡲࡨࡧࡹ࡯࡮ࡨࠢࡧࡳࡺࡨ࡬ࡦ࠯ࡴࡹࡴࡺࡥࡥࠢࡶࡹࡧࡹࡴࡳ࡫ࡱ࡫ࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡈࡲࡶࠥ࡫ࡸࡢ࡯ࡳࡰࡪࡀࠠࠨࡣ࠯ࠤࠧࡨࠬࡤࠤ࠯ࠤࡩ࠭ࠠ࠮ࡀࠣ࡟ࠬࡧࠧ࠭ࠢࠪࡦ࠱ࡩࠧ࠭ࠢࠪࡨࠬࡣࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᗜ")
        pattern = re.compile(bstack1l1ll_opy_ (u"ࡶࠬࠨࠨ࡜ࡠࠥࡡ࠯࠯ࠢࡽࠪ࡞ࡢ࠱ࡣࠫࠪࠩᗝ"))
        result = []
        for match in pattern.finditer(bstack11lll1lll1l_opy_):
            if match.group(1) is not None:
                result.append(match.group(1).strip())
            elif match.group(2) is not None:
                result.append(match.group(2).strip())
        return result
    def __new__(cls, *args, **kwargs):
        raise Exception(bstack1l1ll_opy_ (u"࡛ࠧࡴࡪ࡮࡬ࡸࡾࠦࡣ࡭ࡣࡶࡷࠥࡹࡨࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡥࡩࠥ࡯࡮ࡴࡶࡤࡲࡹ࡯ࡡࡵࡧࡧࠦᗞ"))