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
from bstack_utils.bstack1l1l11l11_opy_ import bstack11111l1l1l1_opy_
def bstack11111l11111_opy_(fixture_name):
    if fixture_name.startswith(bstack1l1ll_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩở")):
        return bstack1l1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩỠ")
    elif fixture_name.startswith(bstack1l1ll_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩỡ")):
        return bstack1l1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩỢ")
    elif fixture_name.startswith(bstack1l1ll_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩợ")):
        return bstack1l1ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩỤ")
    elif fixture_name.startswith(bstack1l1ll_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫụ")):
        return bstack1l1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩỦ")
def bstack11111l111l1_opy_(fixture_name):
    return bool(re.match(bstack1l1ll_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡽ࡯ࡲࡨࡺࡲࡥࠪࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ủ"), fixture_name))
def bstack11111l11l11_opy_(fixture_name):
    return bool(re.match(bstack1l1ll_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪỨ"), fixture_name))
def bstack11111l111ll_opy_(fixture_name):
    return bool(re.match(bstack1l1ll_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪứ"), fixture_name))
def bstack11111l1111l_opy_(fixture_name):
    if fixture_name.startswith(bstack1l1ll_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭Ừ")):
        return bstack1l1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ừ"), bstack1l1ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫỬ")
    elif fixture_name.startswith(bstack1l1ll_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧử")):
        return bstack1l1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭࡮ࡱࡧࡹࡱ࡫ࠧỮ"), bstack1l1ll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ữ")
    elif fixture_name.startswith(bstack1l1ll_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨỰ")):
        return bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨự"), bstack1l1ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩỲ")
    elif fixture_name.startswith(bstack1l1ll_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩỳ")):
        return bstack1l1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩỴ"), bstack1l1ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫỵ")
    return None, None
def bstack11111l1l1ll_opy_(hook_name):
    if hook_name in [bstack1l1ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨỶ"), bstack1l1ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬỷ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11111l1l111_opy_(hook_name):
    if hook_name in [bstack1l1ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬỸ"), bstack1l1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫỹ")]:
        return bstack1l1ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫỺ")
    elif hook_name in [bstack1l1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ỻ"), bstack1l1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭Ỽ")]:
        return bstack1l1ll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ỽ")
    elif hook_name in [bstack1l1ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧỾ"), bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ỿ")]:
        return bstack1l1ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩἀ")
    elif hook_name in [bstack1l1ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨἁ"), bstack1l1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨἂ")]:
        return bstack1l1ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫἃ")
    return hook_name
def bstack11111l11ll1_opy_(node, scenario):
    if hasattr(node, bstack1l1ll_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫἄ")):
        parts = node.nodeid.rsplit(bstack1l1ll_opy_ (u"ࠥ࡟ࠧἅ"))
        params = parts[-1]
        return bstack1l1ll_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦἆ").format(scenario.name, params)
    return scenario.name
def bstack11111l11l1l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1l1ll_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧἇ")):
            examples = list(node.callspec.params[bstack1l1ll_opy_ (u"࠭࡟ࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡪࡾࡡ࡮ࡲ࡯ࡩࠬἈ")].values())
        return examples
    except:
        return []
def bstack111111lllll_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11111l11lll_opy_(report):
    try:
        status = bstack1l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧἉ")
        if report.passed or (report.failed and hasattr(report, bstack1l1ll_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥἊ"))):
            status = bstack1l1ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩἋ")
        elif report.skipped:
            status = bstack1l1ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫἌ")
        bstack11111l1l1l1_opy_(status)
    except:
        pass
def bstack1l111l1111_opy_(status):
    try:
        bstack11111l1l11l_opy_ = bstack1l1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫἍ")
        if status == bstack1l1ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬἎ"):
            bstack11111l1l11l_opy_ = bstack1l1ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭Ἇ")
        elif status == bstack1l1ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨἐ"):
            bstack11111l1l11l_opy_ = bstack1l1ll_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩἑ")
        bstack11111l1l1l1_opy_(bstack11111l1l11l_opy_)
    except:
        pass
def bstack111111llll1_opy_(item=None, report=None, summary=None, extra=None):
    return