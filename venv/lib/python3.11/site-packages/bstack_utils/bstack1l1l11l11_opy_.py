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
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack111llll1l11_opy_, bstack1lll111lll_opy_, bstack11ll1ll11_opy_, bstack11l1l1111l_opy_, \
    bstack11l11ll1ll1_opy_
from bstack_utils.measure import measure
def bstack11lllll1l1_opy_(bstack11111111l11_opy_):
    for driver in bstack11111111l11_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1l11l1lll1_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
def bstack1l1l111l1_opy_(driver, status, reason=bstack1l1ll_opy_ (u"ࠫࠬ὚")):
    bstack11l1lll1_opy_ = Config.bstack11ll11ll1_opy_()
    if bstack11l1lll1_opy_.bstack11111l11ll_opy_():
        return
    bstack1l11111ll_opy_ = bstack1l1ll11lll_opy_(bstack1l1ll_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨὛ"), bstack1l1ll_opy_ (u"࠭ࠧ὜"), status, reason, bstack1l1ll_opy_ (u"ࠧࠨὝ"), bstack1l1ll_opy_ (u"ࠨࠩ὞"))
    driver.execute_script(bstack1l11111ll_opy_)
@measure(event_name=EVENTS.bstack1l11l1lll1_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
def bstack1111l1ll_opy_(page, status, reason=bstack1l1ll_opy_ (u"ࠩࠪὟ")):
    try:
        if page is None:
            return
        bstack11l1lll1_opy_ = Config.bstack11ll11ll1_opy_()
        if bstack11l1lll1_opy_.bstack11111l11ll_opy_():
            return
        bstack1l11111ll_opy_ = bstack1l1ll11lll_opy_(bstack1l1ll_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ὠ"), bstack1l1ll_opy_ (u"ࠫࠬὡ"), status, reason, bstack1l1ll_opy_ (u"ࠬ࠭ὢ"), bstack1l1ll_opy_ (u"࠭ࠧὣ"))
        page.evaluate(bstack1l1ll_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣὤ"), bstack1l11111ll_opy_)
    except Exception as e:
        print(bstack1l1ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡿࢂࠨὥ"), e)
def bstack1l1ll11lll_opy_(type, name, status, reason, bstack1l1ll1ll11_opy_, bstack1l111l1l1l_opy_):
    bstack1l11l1l111_opy_ = {
        bstack1l1ll_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩὦ"): type,
        bstack1l1ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ὧ"): {}
    }
    if type == bstack1l1ll_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭Ὠ"):
        bstack1l11l1l111_opy_[bstack1l1ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨὩ")][bstack1l1ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬὪ")] = bstack1l1ll1ll11_opy_
        bstack1l11l1l111_opy_[bstack1l1ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪὫ")][bstack1l1ll_opy_ (u"ࠨࡦࡤࡸࡦ࠭Ὤ")] = json.dumps(str(bstack1l111l1l1l_opy_))
    if type == bstack1l1ll_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪὭ"):
        bstack1l11l1l111_opy_[bstack1l1ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭Ὦ")][bstack1l1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩὯ")] = name
    if type == bstack1l1ll_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨὰ"):
        bstack1l11l1l111_opy_[bstack1l1ll_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩά")][bstack1l1ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧὲ")] = status
        if status == bstack1l1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨέ") and str(reason) != bstack1l1ll_opy_ (u"ࠤࠥὴ"):
            bstack1l11l1l111_opy_[bstack1l1ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ή")][bstack1l1ll_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫὶ")] = json.dumps(str(reason))
    bstack1l1lll111_opy_ = bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪί").format(json.dumps(bstack1l11l1l111_opy_))
    return bstack1l1lll111_opy_
def bstack11lll11l_opy_(url, config, logger, bstack1l1l1lll_opy_=False):
    hostname = bstack1lll111lll_opy_(url)
    is_private = bstack11l1l1111l_opy_(hostname)
    try:
        if is_private or bstack1l1l1lll_opy_:
            file_path = bstack111llll1l11_opy_(bstack1l1ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ὸ"), bstack1l1ll_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ό"), logger)
            if os.environ.get(bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ὺ")) and eval(
                    os.environ.get(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧύ"))):
                return
            if (bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧὼ") in config and not config[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨώ")]):
                os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪ὾")] = str(True)
                bstack111111111ll_opy_ = {bstack1l1ll_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ὿"): hostname}
                bstack11l11ll1ll1_opy_(bstack1l1ll_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ᾀ"), bstack1l1ll_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭ᾁ"), bstack111111111ll_opy_, logger)
    except Exception as e:
        pass
def bstack1l1l11lll1_opy_(caps, bstack111111111l1_opy_):
    if bstack1l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᾂ") in caps:
        caps[bstack1l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᾃ")][bstack1l1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪᾄ")] = True
        if bstack111111111l1_opy_:
            caps[bstack1l1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ᾅ")][bstack1l1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᾆ")] = bstack111111111l1_opy_
    else:
        caps[bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬᾇ")] = True
        if bstack111111111l1_opy_:
            caps[bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᾈ")] = bstack111111111l1_opy_
def bstack11111l1l1l1_opy_(bstack111l1l1ll1_opy_):
    bstack11111111l1l_opy_ = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ᾉ"), bstack1l1ll_opy_ (u"ࠪࠫᾊ"))
    if bstack11111111l1l_opy_ == bstack1l1ll_opy_ (u"ࠫࠬᾋ") or bstack11111111l1l_opy_ == bstack1l1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᾌ"):
        threading.current_thread().testStatus = bstack111l1l1ll1_opy_
    else:
        if bstack111l1l1ll1_opy_ == bstack1l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᾍ"):
            threading.current_thread().testStatus = bstack111l1l1ll1_opy_