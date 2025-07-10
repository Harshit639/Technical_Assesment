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
import logging
import os
import datetime
import threading
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll1l111ll_opy_, bstack11ll1llllll_opy_, bstack1ll1l1l1l1_opy_, bstack111l111ll1_opy_, bstack111llll11l1_opy_, bstack111lllll1ll_opy_, bstack11l11l11ll1_opy_, bstack1lllll1l11_opy_, bstack11ll1ll11_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack111111l1ll1_opy_ import bstack111111lll1l_opy_
import bstack_utils.bstack1l1111llll_opy_ as bstack1l111l111l_opy_
from bstack_utils.bstack111llll111_opy_ import bstack11ll1llll1_opy_
import bstack_utils.accessibility as bstack111111l1l_opy_
from bstack_utils.bstack11111lll_opy_ import bstack11111lll_opy_
from bstack_utils.bstack111ll11l1l_opy_ import bstack111l111l1l_opy_
bstack1lllll1lll1l_opy_ = bstack1l1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡣࡰ࡮࡯ࡩࡨࡺ࡯ࡳ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ ")
logger = logging.getLogger(__name__)
class bstack11ll1ll1_opy_:
    bstack111111l1ll1_opy_ = None
    bs_config = None
    bstack11lll11lll_opy_ = None
    @classmethod
    @bstack111l111ll1_opy_(class_method=True)
    @measure(event_name=EVENTS.bstack11l1llll1ll_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def launch(cls, bs_config, bstack11lll11lll_opy_):
        cls.bs_config = bs_config
        cls.bstack11lll11lll_opy_ = bstack11lll11lll_opy_
        try:
            cls.bstack1lllll1l11l1_opy_()
            bstack11ll1llll11_opy_ = bstack11ll1l111ll_opy_(bs_config)
            bstack11ll1lll111_opy_ = bstack11ll1llllll_opy_(bs_config)
            data = bstack1l111l111l_opy_.bstack1lllll1lll11_opy_(bs_config, bstack11lll11lll_opy_)
            config = {
                bstack1l1ll_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ​"): (bstack11ll1llll11_opy_, bstack11ll1lll111_opy_),
                bstack1l1ll_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ‌"): cls.default_headers()
            }
            response = bstack1ll1l1l1l1_opy_(bstack1l1ll_opy_ (u"ࠨࡒࡒࡗ࡙࠭‍"), cls.request_url(bstack1l1ll_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠳࠱ࡥࡹ࡮ࡲࡤࡴࠩ‎")), data, config)
            if response.status_code != 200:
                bstack1ll1l1ll1l_opy_ = response.json()
                if bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ‏")] == False:
                    cls.bstack1llllll1111l_opy_(bstack1ll1l1ll1l_opy_)
                    return
                cls.bstack1lllll1lllll_opy_(bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ‐")])
                cls.bstack1lllll1ll111_opy_(bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ‑")])
                return None
            bstack1lllll1l111l_opy_ = cls.bstack1lllll11llll_opy_(response)
            return bstack1lllll1l111l_opy_, response.json()
        except Exception as error:
            logger.error(bstack1l1ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࠢࡩࡳࡷࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࡽࢀࠦ‒").format(str(error)))
            return None
    @classmethod
    @bstack111l111ll1_opy_(class_method=True)
    def stop(cls, bstack1lllll1l1ll1_opy_=None):
        if not bstack11ll1llll1_opy_.on() and not bstack111111l1l_opy_.on():
            return
        if os.environ.get(bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ–")) == bstack1l1ll_opy_ (u"ࠣࡰࡸࡰࡱࠨ—") or os.environ.get(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ―")) == bstack1l1ll_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ‖"):
            logger.error(bstack1l1ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡵࡰࠡࡤࡸ࡭ࡱࡪࠠࡳࡧࡴࡹࡪࡹࡴࠡࡶࡲࠤ࡙࡫ࡳࡵࡊࡸࡦ࠿ࠦࡍࡪࡵࡶ࡭ࡳ࡭ࠠࡢࡷࡷ࡬ࡪࡴࡴࡪࡥࡤࡸ࡮ࡵ࡮ࠡࡶࡲ࡯ࡪࡴࠧ‗"))
            return {
                bstack1l1ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ‘"): bstack1l1ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ’"),
                bstack1l1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ‚"): bstack1l1ll_opy_ (u"ࠨࡖࡲ࡯ࡪࡴ࠯ࡣࡷ࡬ࡰࡩࡏࡄࠡ࡫ࡶࠤࡺࡴࡤࡦࡨ࡬ࡲࡪࡪࠬࠡࡤࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢࡰ࡭࡬࡮ࡴࠡࡪࡤࡺࡪࠦࡦࡢ࡫࡯ࡩࡩ࠭‛")
            }
        try:
            cls.bstack111111l1ll1_opy_.shutdown()
            data = {
                bstack1l1ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ“"): bstack1lllll1l11_opy_()
            }
            if not bstack1lllll1l1ll1_opy_ is None:
                data[bstack1l1ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡳࡥࡵࡣࡧࡥࡹࡧࠧ”")] = [{
                    bstack1l1ll_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫ„"): bstack1l1ll_opy_ (u"ࠬࡻࡳࡦࡴࡢ࡯࡮ࡲ࡬ࡦࡦࠪ‟"),
                    bstack1l1ll_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱ࠭†"): bstack1lllll1l1ll1_opy_
                }]
            config = {
                bstack1l1ll_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ‡"): cls.default_headers()
            }
            bstack11ll11ll11l_opy_ = bstack1l1ll_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡸࡺ࡯ࡱࠩ•").format(os.environ[bstack1l1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠢ‣")])
            bstack1lllll11l11l_opy_ = cls.request_url(bstack11ll11ll11l_opy_)
            response = bstack1ll1l1l1l1_opy_(bstack1l1ll_opy_ (u"ࠪࡔ࡚࡚ࠧ․"), bstack1lllll11l11l_opy_, data, config)
            if not response.ok:
                raise Exception(bstack1l1ll_opy_ (u"ࠦࡘࡺ࡯ࡱࠢࡵࡩࡶࡻࡥࡴࡶࠣࡲࡴࡺࠠࡰ࡭ࠥ‥"))
        except Exception as error:
            logger.error(bstack1l1ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺ࡯ࡱࠢࡥࡹ࡮ࡲࡤࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡷࡳ࡚ࠥࡥࡴࡶࡋࡹࡧࡀ࠺ࠡࠤ…") + str(error))
            return {
                bstack1l1ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭‧"): bstack1l1ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ "),
                bstack1l1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ "): str(error)
            }
    @classmethod
    @bstack111l111ll1_opy_(class_method=True)
    def bstack1lllll11llll_opy_(cls, response):
        bstack1ll1l1ll1l_opy_ = response.json() if not isinstance(response, dict) else response
        bstack1lllll1l111l_opy_ = {}
        if bstack1ll1l1ll1l_opy_.get(bstack1l1ll_opy_ (u"ࠩ࡭ࡻࡹ࠭‪")) is None:
            os.environ[bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ‫")] = bstack1l1ll_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ‬")
        else:
            os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ‭")] = bstack1ll1l1ll1l_opy_.get(bstack1l1ll_opy_ (u"࠭ࡪࡸࡶࠪ‮"), bstack1l1ll_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ "))
        os.environ[bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭‰")] = bstack1ll1l1ll1l_opy_.get(bstack1l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ‱"), bstack1l1ll_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ′"))
        logger.info(bstack1l1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡪࡸࡦࠥࡹࡴࡢࡴࡷࡩࡩࠦࡷࡪࡶ࡫ࠤ࡮ࡪ࠺ࠡࠩ″") + os.getenv(bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ‴")));
        if bstack11ll1llll1_opy_.bstack1lllll1ll11l_opy_(cls.bs_config, cls.bstack11lll11lll_opy_.get(bstack1l1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡸࡷࡪࡪࠧ‵"), bstack1l1ll_opy_ (u"ࠧࠨ‶"))) is True:
            bstack1111111l1ll_opy_, build_hashed_id, bstack1lllll11l1ll_opy_ = cls.bstack1lllll1llll1_opy_(bstack1ll1l1ll1l_opy_)
            if bstack1111111l1ll_opy_ != None and build_hashed_id != None:
                bstack1lllll1l111l_opy_[bstack1l1ll_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ‷")] = {
                    bstack1l1ll_opy_ (u"ࠩ࡭ࡻࡹࡥࡴࡰ࡭ࡨࡲࠬ‸"): bstack1111111l1ll_opy_,
                    bstack1l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ‹"): build_hashed_id,
                    bstack1l1ll_opy_ (u"ࠫࡦࡲ࡬ࡰࡹࡢࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨ›"): bstack1lllll11l1ll_opy_
                }
            else:
                bstack1lllll1l111l_opy_[bstack1l1ll_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ※")] = {}
        else:
            bstack1lllll1l111l_opy_[bstack1l1ll_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭‼")] = {}
        bstack1lllll11ll1l_opy_, build_hashed_id = cls.bstack1lllll1ll1l1_opy_(bstack1ll1l1ll1l_opy_)
        if bstack1lllll11ll1l_opy_ != None and build_hashed_id != None:
            bstack1lllll1l111l_opy_[bstack1l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ‽")] = {
                bstack1l1ll_opy_ (u"ࠨࡣࡸࡸ࡭ࡥࡴࡰ࡭ࡨࡲࠬ‾"): bstack1lllll11ll1l_opy_,
                bstack1l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ‿"): build_hashed_id,
            }
        else:
            bstack1lllll1l111l_opy_[bstack1l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⁀")] = {}
        if bstack1lllll1l111l_opy_[bstack1l1ll_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ⁁")].get(bstack1l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ⁂")) != None or bstack1lllll1l111l_opy_[bstack1l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⁃")].get(bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ⁄")) != None:
            cls.bstack1llllll11111_opy_(bstack1ll1l1ll1l_opy_.get(bstack1l1ll_opy_ (u"ࠨ࡬ࡺࡸࠬ⁅")), bstack1ll1l1ll1l_opy_.get(bstack1l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ⁆")))
        return bstack1lllll1l111l_opy_
    @classmethod
    def bstack1lllll1llll1_opy_(cls, bstack1ll1l1ll1l_opy_):
        if bstack1ll1l1ll1l_opy_.get(bstack1l1ll_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⁇")) == None:
            cls.bstack1lllll1lllll_opy_()
            return [None, None, None]
        if bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ⁈")][bstack1l1ll_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭⁉")] != True:
            cls.bstack1lllll1lllll_opy_(bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭⁊")])
            return [None, None, None]
        logger.debug(bstack1l1ll_opy_ (u"ࠧࡕࡧࡶࡸࠥࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠤࠫ⁋"))
        os.environ[bstack1l1ll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧ⁌")] = bstack1l1ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⁍")
        if bstack1ll1l1ll1l_opy_.get(bstack1l1ll_opy_ (u"ࠪ࡮ࡼࡺࠧ⁎")):
            os.environ[bstack1l1ll_opy_ (u"ࠫࡈࡘࡅࡅࡇࡑࡘࡎࡇࡌࡔࡡࡉࡓࡗࡥࡃࡓࡃࡖࡌࡤࡘࡅࡑࡑࡕࡘࡎࡔࡇࠨ⁏")] = json.dumps({
                bstack1l1ll_opy_ (u"ࠬࡻࡳࡦࡴࡱࡥࡲ࡫ࠧ⁐"): bstack11ll1l111ll_opy_(cls.bs_config),
                bstack1l1ll_opy_ (u"࠭ࡰࡢࡵࡶࡻࡴࡸࡤࠨ⁑"): bstack11ll1llllll_opy_(cls.bs_config)
            })
        if bstack1ll1l1ll1l_opy_.get(bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ⁒")):
            os.environ[bstack1l1ll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧ⁓")] = bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ⁔")]
        if bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ⁕")].get(bstack1l1ll_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ⁖"), {}).get(bstack1l1ll_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩ⁗")):
            os.environ[bstack1l1ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧ⁘")] = str(bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠧࡰࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ⁙")][bstack1l1ll_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⁚")][bstack1l1ll_opy_ (u"ࠩࡤࡰࡱࡵࡷࡠࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࡸ࠭⁛")])
        else:
            os.environ[bstack1l1ll_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫ⁜")] = bstack1l1ll_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ⁝")
        return [bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠬࡰࡷࡵࠩ⁞")], bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ ")], os.environ[bstack1l1ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡆࡒࡌࡐ࡙ࡢࡗࡈࡘࡅࡆࡐࡖࡌࡔ࡚ࡓࠨ⁠")]]
    @classmethod
    def bstack1lllll1ll1l1_opy_(cls, bstack1ll1l1ll1l_opy_):
        if bstack1ll1l1ll1l_opy_.get(bstack1l1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⁡")) == None:
            cls.bstack1lllll1ll111_opy_()
            return [None, None]
        if bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⁢")][bstack1l1ll_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ⁣")] != True:
            cls.bstack1lllll1ll111_opy_(bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⁤")])
            return [None, None]
        if bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⁥")].get(bstack1l1ll_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ⁦")):
            logger.debug(bstack1l1ll_opy_ (u"ࠧࡕࡧࡶࡸࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠤࠫ⁧"))
            parsed = json.loads(os.getenv(bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ⁨"), bstack1l1ll_opy_ (u"ࠩࡾࢁࠬ⁩")))
            capabilities = bstack1l111l111l_opy_.bstack1llllll111ll_opy_(bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⁪")][bstack1l1ll_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ⁫")][bstack1l1ll_opy_ (u"ࠬࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⁬")], bstack1l1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ⁭"), bstack1l1ll_opy_ (u"ࠧࡷࡣ࡯ࡹࡪ࠭⁮"))
            bstack1lllll11ll1l_opy_ = capabilities[bstack1l1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡕࡱ࡮ࡩࡳ࠭⁯")]
            os.environ[bstack1l1ll_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ⁰")] = bstack1lllll11ll1l_opy_
            if bstack1l1ll_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࠧⁱ") in bstack1ll1l1ll1l_opy_ and bstack1ll1l1ll1l_opy_.get(bstack1l1ll_opy_ (u"ࠦࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠥ⁲")) is None:
                parsed[bstack1l1ll_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁳")] = capabilities[bstack1l1ll_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ⁴")]
            os.environ[bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ⁵")] = json.dumps(parsed)
            scripts = bstack1l111l111l_opy_.bstack1llllll111ll_opy_(bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⁶")][bstack1l1ll_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪ⁷")][bstack1l1ll_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫ⁸")], bstack1l1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ⁹"), bstack1l1ll_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩ࠭⁺"))
            bstack11111lll_opy_.bstack1111l1ll1_opy_(scripts)
            commands = bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⁻")][bstack1l1ll_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ⁼")][bstack1l1ll_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵࡗࡳ࡜ࡸࡡࡱࠩ⁽")].get(bstack1l1ll_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࠫ⁾"))
            bstack11111lll_opy_.bstack11ll1ll111l_opy_(commands)
            bstack11ll1lll1ll_opy_ = capabilities.get(bstack1l1ll_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨⁿ"))
            bstack11111lll_opy_.bstack11ll11ll1ll_opy_(bstack11ll1lll1ll_opy_)
            bstack11111lll_opy_.store()
        return [bstack1lllll11ll1l_opy_, bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭₀")]]
    @classmethod
    def bstack1lllll1lllll_opy_(cls, response=None):
        os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ₁")] = bstack1l1ll_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ₂")
        os.environ[bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ₃")] = bstack1l1ll_opy_ (u"ࠨࡰࡸࡰࡱ࠭₄")
        os.environ[bstack1l1ll_opy_ (u"ࠩࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡉࡏࡎࡒࡏࡉ࡙ࡋࡄࠨ₅")] = bstack1l1ll_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ₆")
        os.environ[bstack1l1ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪ₇")] = bstack1l1ll_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ₈")
        os.environ[bstack1l1ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧ₉")] = bstack1l1ll_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ₊")
        cls.bstack1llllll1111l_opy_(response, bstack1l1ll_opy_ (u"ࠣࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠣ₋"))
        return [None, None, None]
    @classmethod
    def bstack1lllll1ll111_opy_(cls, response=None):
        os.environ[bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ₌")] = bstack1l1ll_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ₍")
        os.environ[bstack1l1ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ₎")] = bstack1l1ll_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ₏")
        os.environ[bstack1l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪₐ")] = bstack1l1ll_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬₑ")
        cls.bstack1llllll1111l_opy_(response, bstack1l1ll_opy_ (u"ࠣࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠣₒ"))
        return [None, None, None]
    @classmethod
    def bstack1llllll11111_opy_(cls, jwt, build_hashed_id):
        os.environ[bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ₓ")] = jwt
        os.environ[bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨₔ")] = build_hashed_id
    @classmethod
    def bstack1llllll1111l_opy_(cls, response=None, product=bstack1l1ll_opy_ (u"ࠦࠧₕ")):
        if response == None or response.get(bstack1l1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬₖ")) == None:
            logger.error(product + bstack1l1ll_opy_ (u"ࠨࠠࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤࠣₗ"))
            return
        for error in response[bstack1l1ll_opy_ (u"ࠧࡦࡴࡵࡳࡷࡹࠧₘ")]:
            bstack11l111l11ll_opy_ = error[bstack1l1ll_opy_ (u"ࠨ࡭ࡨࡽࠬₙ")]
            error_message = error[bstack1l1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪₚ")]
            if error_message:
                if bstack11l111l11ll_opy_ == bstack1l1ll_opy_ (u"ࠥࡉࡗࡘࡏࡓࡡࡄࡇࡈࡋࡓࡔࡡࡇࡉࡓࡏࡅࡅࠤₛ"):
                    logger.info(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack1l1ll_opy_ (u"ࠦࡉࡧࡴࡢࠢࡸࡴࡱࡵࡡࡥࠢࡷࡳࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࠧₜ") + product + bstack1l1ll_opy_ (u"ࠧࠦࡦࡢ࡫࡯ࡩࡩࠦࡤࡶࡧࠣࡸࡴࠦࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠥ₝"))
    @classmethod
    def bstack1lllll1l11l1_opy_(cls):
        if cls.bstack111111l1ll1_opy_ is not None:
            return
        cls.bstack111111l1ll1_opy_ = bstack111111lll1l_opy_(cls.bstack1lllll1l1111_opy_)
        cls.bstack111111l1ll1_opy_.start()
    @classmethod
    def bstack111l1l1111_opy_(cls):
        if cls.bstack111111l1ll1_opy_ is None:
            return
        cls.bstack111111l1ll1_opy_.shutdown()
    @classmethod
    @bstack111l111ll1_opy_(class_method=True)
    def bstack1lllll1l1111_opy_(cls, bstack111l1llll1_opy_, event_url=bstack1l1ll_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡢࡶࡦ࡬ࠬ₞")):
        config = {
            bstack1l1ll_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ₟"): cls.default_headers()
        }
        logger.debug(bstack1l1ll_opy_ (u"ࠣࡲࡲࡷࡹࡥࡤࡢࡶࡤ࠾࡙ࠥࡥ࡯ࡦ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠤࡹࡵࠠࡵࡧࡶࡸ࡭ࡻࡢࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷࡷࠥࢁࡽࠣ₠").format(bstack1l1ll_opy_ (u"ࠩ࠯ࠤࠬ₡").join([event[bstack1l1ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ₢")] for event in bstack111l1llll1_opy_])))
        response = bstack1ll1l1l1l1_opy_(bstack1l1ll_opy_ (u"ࠫࡕࡕࡓࡕࠩ₣"), cls.request_url(event_url), bstack111l1llll1_opy_, config)
        bstack11ll1l11ll1_opy_ = response.json()
    @classmethod
    def bstack1ll111l1l1_opy_(cls, bstack111l1llll1_opy_, event_url=bstack1l1ll_opy_ (u"ࠬࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡡࡵࡥ࡫ࠫ₤")):
        logger.debug(bstack1l1ll_opy_ (u"ࠨࡳࡦࡰࡧࡣࡩࡧࡴࡢ࠼ࠣࡅࡹࡺࡥ࡮ࡲࡷ࡭ࡳ࡭ࠠࡵࡱࠣࡥࡩࡪࠠࡥࡣࡷࡥࠥࡺ࡯ࠡࡤࡤࡸࡨ࡮ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ࠼ࠣࡿࢂࠨ₥").format(bstack111l1llll1_opy_[bstack1l1ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ₦")]))
        if not bstack1l111l111l_opy_.bstack1lllll11lll1_opy_(bstack111l1llll1_opy_[bstack1l1ll_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ₧")]):
            logger.debug(bstack1l1ll_opy_ (u"ࠤࡶࡩࡳࡪ࡟ࡥࡣࡷࡥ࠿ࠦࡎࡰࡶࠣࡥࡩࡪࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧ࠽ࠤࢀࢃࠢ₨").format(bstack111l1llll1_opy_[bstack1l1ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ₩")]))
            return
        bstack11l1ll11l_opy_ = bstack1l111l111l_opy_.bstack1llllll111l1_opy_(bstack111l1llll1_opy_[bstack1l1ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ₪")], bstack111l1llll1_opy_.get(bstack1l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧ₫")))
        if bstack11l1ll11l_opy_ != None:
            if bstack111l1llll1_opy_.get(bstack1l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨ€")) != None:
                bstack111l1llll1_opy_[bstack1l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩ₭")][bstack1l1ll_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭₮")] = bstack11l1ll11l_opy_
            else:
                bstack111l1llll1_opy_[bstack1l1ll_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࡢࡱࡦࡶࠧ₯")] = bstack11l1ll11l_opy_
        if event_url == bstack1l1ll_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡦࡺࡣࡩࠩ₰"):
            cls.bstack1lllll1l11l1_opy_()
            logger.debug(bstack1l1ll_opy_ (u"ࠦࡸ࡫࡮ࡥࡡࡧࡥࡹࡧ࠺ࠡࡃࡧࡨ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡴࡰࠢࡥࡥࡹࡩࡨࠡࡹ࡬ࡸ࡭ࠦࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧ࠽ࠤࢀࢃࠢ₱").format(bstack111l1llll1_opy_[bstack1l1ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩ₲")]))
            cls.bstack111111l1ll1_opy_.add(bstack111l1llll1_opy_)
        elif event_url == bstack1l1ll_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫ₳"):
            cls.bstack1lllll1l1111_opy_([bstack111l1llll1_opy_], event_url)
    @classmethod
    @bstack111l111ll1_opy_(class_method=True)
    def bstack11l1l1lll1_opy_(cls, logs):
        bstack1lllll1ll1ll_opy_ = []
        for log in logs:
            bstack1lllll1l1l11_opy_ = {
                bstack1l1ll_opy_ (u"ࠧ࡬࡫ࡱࡨࠬ₴"): bstack1l1ll_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡌࡐࡉࠪ₵"),
                bstack1l1ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ₶"): log[bstack1l1ll_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ₷")],
                bstack1l1ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ₸"): log[bstack1l1ll_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ₹")],
                bstack1l1ll_opy_ (u"࠭ࡨࡵࡶࡳࡣࡷ࡫ࡳࡱࡱࡱࡷࡪ࠭₺"): {},
                bstack1l1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ₻"): log[bstack1l1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ₼")],
            }
            if bstack1l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ₽") in log:
                bstack1lllll1l1l11_opy_[bstack1l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ₾")] = log[bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ₿")]
            elif bstack1l1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⃀") in log:
                bstack1lllll1l1l11_opy_[bstack1l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⃁")] = log[bstack1l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⃂")]
            bstack1lllll1ll1ll_opy_.append(bstack1lllll1l1l11_opy_)
        cls.bstack1ll111l1l1_opy_({
            bstack1l1ll_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ⃃"): bstack1l1ll_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭⃄"),
            bstack1l1ll_opy_ (u"ࠪࡰࡴ࡭ࡳࠨ⃅"): bstack1lllll1ll1ll_opy_
        })
    @classmethod
    @bstack111l111ll1_opy_(class_method=True)
    def bstack1lllll1l1lll_opy_(cls, steps):
        bstack1lllll11ll11_opy_ = []
        for step in steps:
            bstack1lllll11l1l1_opy_ = {
                bstack1l1ll_opy_ (u"ࠫࡰ࡯࡮ࡥࠩ⃆"): bstack1l1ll_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗ࡙ࡋࡐࠨ⃇"),
                bstack1l1ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ⃈"): step[bstack1l1ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭⃉")],
                bstack1l1ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ⃊"): step[bstack1l1ll_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ⃋")],
                bstack1l1ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⃌"): step[bstack1l1ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⃍")],
                bstack1l1ll_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧ⃎"): step[bstack1l1ll_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨ⃏")]
            }
            if bstack1l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⃐") in step:
                bstack1lllll11l1l1_opy_[bstack1l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⃑")] = step[bstack1l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥ⃒ࠩ")]
            elif bstack1l1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦ⃓ࠪ") in step:
                bstack1lllll11l1l1_opy_[bstack1l1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⃔")] = step[bstack1l1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⃕")]
            bstack1lllll11ll11_opy_.append(bstack1lllll11l1l1_opy_)
        cls.bstack1ll111l1l1_opy_({
            bstack1l1ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⃖"): bstack1l1ll_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ⃗"),
            bstack1l1ll_opy_ (u"ࠨ࡮ࡲ࡫ࡸ⃘࠭"): bstack1lllll11ll11_opy_
        })
    @classmethod
    @bstack111l111ll1_opy_(class_method=True)
    @measure(event_name=EVENTS.bstack11llll11l_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def bstack1l11ll1ll1_opy_(cls, screenshot):
        cls.bstack1ll111l1l1_opy_({
            bstack1l1ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ⃙࠭"): bstack1l1ll_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪ⃚ࠧ"),
            bstack1l1ll_opy_ (u"ࠫࡱࡵࡧࡴࠩ⃛"): [{
                bstack1l1ll_opy_ (u"ࠬࡱࡩ࡯ࡦࠪ⃜"): bstack1l1ll_opy_ (u"࠭ࡔࡆࡕࡗࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࠨ⃝"),
                bstack1l1ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ⃞"): datetime.datetime.utcnow().isoformat() + bstack1l1ll_opy_ (u"ࠨ࡜ࠪ⃟"),
                bstack1l1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⃠"): screenshot[bstack1l1ll_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩ⃡")],
                bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⃢"): screenshot[bstack1l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬ⃣")]
            }]
        }, event_url=bstack1l1ll_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫ⃤"))
    @classmethod
    @bstack111l111ll1_opy_(class_method=True)
    def bstack1l1111l111_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack1ll111l1l1_opy_({
            bstack1l1ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨ⃥ࠫ"): bstack1l1ll_opy_ (u"ࠨࡅࡅࡘࡘ࡫ࡳࡴ࡫ࡲࡲࡈࡸࡥࡢࡶࡨࡨ⃦ࠬ"),
            bstack1l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫ⃧"): {
                bstack1l1ll_opy_ (u"ࠥࡹࡺ࡯ࡤ⃨ࠣ"): cls.current_test_uuid(),
                bstack1l1ll_opy_ (u"ࠦ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠥ⃩"): cls.bstack111lll1l1l_opy_(driver)
            }
        })
    @classmethod
    def bstack111ll111ll_opy_(cls, event: str, bstack111l1llll1_opy_: bstack111l111l1l_opy_):
        bstack1111lllll1_opy_ = {
            bstack1l1ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ⃪ࠩ"): event,
            bstack111l1llll1_opy_.bstack111l1lll11_opy_(): bstack111l1llll1_opy_.bstack111l1l111l_opy_(event)
        }
        cls.bstack1ll111l1l1_opy_(bstack1111lllll1_opy_)
        result = getattr(bstack111l1llll1_opy_, bstack1l1ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ⃫࠭"), None)
        if event == bstack1l1ll_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ⃬"):
            threading.current_thread().bstackTestMeta = {bstack1l1ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ⃭"): bstack1l1ll_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩ⃮ࠪ")}
        elif event == bstack1l1ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨ⃯ࠬ"):
            threading.current_thread().bstackTestMeta = {bstack1l1ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ⃰"): getattr(result, bstack1l1ll_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬ⃱"), bstack1l1ll_opy_ (u"࠭ࠧ⃲"))}
    @classmethod
    def on(cls):
        if (os.environ.get(bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ⃳"), None) is None or os.environ[bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ⃴")] == bstack1l1ll_opy_ (u"ࠤࡱࡹࡱࡲࠢ⃵")) and (os.environ.get(bstack1l1ll_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ⃶"), None) is None or os.environ[bstack1l1ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ⃷")] == bstack1l1ll_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ⃸")):
            return False
        return True
    @staticmethod
    def bstack1lllll1l1l1l_opy_(func):
        def wrap(*args, **kwargs):
            if bstack11ll1ll1_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def default_headers():
        headers = {
            bstack1l1ll_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬ⃹"): bstack1l1ll_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ⃺"),
            bstack1l1ll_opy_ (u"ࠨ࡚࠰ࡆࡘ࡚ࡁࡄࡍ࠰ࡘࡊ࡙ࡔࡐࡒࡖࠫ⃻"): bstack1l1ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⃼")
        }
        if os.environ.get(bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧ⃽"), None):
            headers[bstack1l1ll_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫ⃾")] = bstack1l1ll_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨ⃿").format(os.environ[bstack1l1ll_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠥ℀")])
        return headers
    @staticmethod
    def request_url(url):
        return bstack1l1ll_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠭℁").format(bstack1lllll1lll1l_opy_, url)
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack1l1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬℂ"), None)
    @staticmethod
    def bstack111lll1l1l_opy_(driver):
        return {
            bstack111llll11l1_opy_(): bstack111lllll1ll_opy_(driver)
        }
    @staticmethod
    def bstack1lllll1l11ll_opy_(exception_info, report):
        return [{bstack1l1ll_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬ℃"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack111111llll_opy_(typename):
        if bstack1l1ll_opy_ (u"ࠥࡅࡸࡹࡥࡳࡶ࡬ࡳࡳࠨ℄") in typename:
            return bstack1l1ll_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࡅࡳࡴࡲࡶࠧ℅")
        return bstack1l1ll_opy_ (u"࡛ࠧ࡮ࡩࡣࡱࡨࡱ࡫ࡤࡆࡴࡵࡳࡷࠨ℆")