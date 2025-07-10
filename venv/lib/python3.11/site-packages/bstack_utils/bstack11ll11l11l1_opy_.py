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
import requests
from urllib.parse import urljoin, urlencode
from datetime import datetime
import os
import logging
import json
from bstack_utils.constants import bstack11l1lll1l1l_opy_
logger = logging.getLogger(__name__)
class bstack11ll11l1l1l_opy_:
    @staticmethod
    def results(builder,params=None):
        bstack1111111ll11_opy_ = urljoin(builder, bstack1l1ll_opy_ (u"ࠧࡪࡵࡶࡹࡪࡹࠧ἗"))
        if params:
            bstack1111111ll11_opy_ += bstack1l1ll_opy_ (u"ࠣࡁࡾࢁࠧἘ").format(urlencode({bstack1l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩἙ"): params.get(bstack1l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪἚ"))}))
        return bstack11ll11l1l1l_opy_.bstack1111111llll_opy_(bstack1111111ll11_opy_)
    @staticmethod
    def bstack11ll11l1111_opy_(builder,params=None):
        bstack1111111ll11_opy_ = urljoin(builder, bstack1l1ll_opy_ (u"ࠫ࡮ࡹࡳࡶࡧࡶ࠱ࡸࡻ࡭࡮ࡣࡵࡽࠬἛ"))
        if params:
            bstack1111111ll11_opy_ += bstack1l1ll_opy_ (u"ࠧࡅࡻࡾࠤἜ").format(urlencode({bstack1l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭Ἕ"): params.get(bstack1l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ἞"))}))
        return bstack11ll11l1l1l_opy_.bstack1111111llll_opy_(bstack1111111ll11_opy_)
    @staticmethod
    def bstack1111111llll_opy_(bstack1111111lll1_opy_):
        bstack1111111l1ll_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭἟"), os.environ.get(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ἠ"), bstack1l1ll_opy_ (u"ࠪࠫἡ")))
        headers = {bstack1l1ll_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫἢ"): bstack1l1ll_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥࢁࡽࠨἣ").format(bstack1111111l1ll_opy_)}
        response = requests.get(bstack1111111lll1_opy_, headers=headers)
        bstack111111l1111_opy_ = {}
        try:
            bstack111111l1111_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1l1ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧἤ").format(e))
            pass
        if bstack111111l1111_opy_ is not None:
            bstack111111l1111_opy_[bstack1l1ll_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨἥ")] = response.headers.get(bstack1l1ll_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩἦ"), str(int(datetime.now().timestamp() * 1000)))
            bstack111111l1111_opy_[bstack1l1ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩἧ")] = response.status_code
        return bstack111111l1111_opy_
    @staticmethod
    def bstack1111111l1l1_opy_(bstack1111111ll1l_opy_, data):
        logger.debug(bstack1l1ll_opy_ (u"ࠥࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡓࡧࡴࡹࡪࡹࡴࠡࡨࡲࡶࠥࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡕࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࠧἨ"))
        return bstack11ll11l1l1l_opy_.bstack111111l111l_opy_(bstack1l1ll_opy_ (u"ࠫࡕࡕࡓࡕࠩἩ"), bstack1111111ll1l_opy_, data=data)
    @staticmethod
    def bstack111111l11l1_opy_(bstack1111111ll1l_opy_, data):
        logger.debug(bstack1l1ll_opy_ (u"ࠧࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡕࡩࡶࡻࡥࡴࡶࠣࡪࡴࡸࠠࡨࡧࡷࡘࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡷࠧἪ"))
        res = bstack11ll11l1l1l_opy_.bstack111111l111l_opy_(bstack1l1ll_opy_ (u"࠭ࡇࡆࡖࠪἫ"), bstack1111111ll1l_opy_, data=data)
        return res
    @staticmethod
    def bstack111111l111l_opy_(method, bstack1111111ll1l_opy_, data=None, params=None, extra_headers=None):
        bstack1111111l1ll_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫἬ"), bstack1l1ll_opy_ (u"ࠨࠩἭ"))
        headers = {
            bstack1l1ll_opy_ (u"ࠩࡤࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩἮ"): bstack1l1ll_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭Ἧ").format(bstack1111111l1ll_opy_),
            bstack1l1ll_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪἰ"): bstack1l1ll_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨἱ"),
            bstack1l1ll_opy_ (u"࠭ࡁࡤࡥࡨࡴࡹ࠭ἲ"): bstack1l1ll_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪἳ")
        }
        if extra_headers:
            headers.update(extra_headers)
        url = bstack11l1lll1l1l_opy_ + bstack1l1ll_opy_ (u"ࠣ࠱ࠥἴ") + bstack1111111ll1l_opy_.lstrip(bstack1l1ll_opy_ (u"ࠩ࠲ࠫἵ"))
        try:
            if method == bstack1l1ll_opy_ (u"ࠪࡋࡊ࡚ࠧἶ"):
                response = requests.get(url, headers=headers, params=params, json=data)
            elif method == bstack1l1ll_opy_ (u"ࠫࡕࡕࡓࡕࠩἷ"):
                response = requests.post(url, headers=headers, json=data)
            elif method == bstack1l1ll_opy_ (u"ࠬࡖࡕࡕࠩἸ"):
                response = requests.put(url, headers=headers, json=data)
            else:
                raise ValueError(bstack1l1ll_opy_ (u"ࠨࡕ࡯ࡵࡸࡴࡵࡵࡲࡵࡧࡧࠤࡍ࡚ࡔࡑࠢࡰࡩࡹ࡮࡯ࡥ࠼ࠣࡿࢂࠨἹ").format(method))
            logger.debug(bstack1l1ll_opy_ (u"ࠢࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡳࡧࡴࡹࡪࡹࡴࠡ࡯ࡤࡨࡪࠦࡴࡰࠢࡘࡖࡑࡀࠠࡼࡿࠣࡻ࡮ࡺࡨࠡ࡯ࡨࡸ࡭ࡵࡤ࠻ࠢࡾࢁࠧἺ").format(url, method))
            bstack111111l1111_opy_ = {}
            try:
                bstack111111l1111_opy_ = response.json()
            except Exception as e:
                logger.debug(bstack1l1ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡎࡘࡕࡎࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠠ࠮ࠢࡾࢁࠧἻ").format(e, response.text))
            if bstack111111l1111_opy_ is not None:
                bstack111111l1111_opy_[bstack1l1ll_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪἼ")] = response.headers.get(
                    bstack1l1ll_opy_ (u"ࠪࡲࡪࡾࡴࡠࡲࡲࡰࡱࡥࡴࡪ࡯ࡨࠫἽ"), str(int(datetime.now().timestamp() * 1000))
                )
                bstack111111l1111_opy_[bstack1l1ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫἾ")] = response.status_code
            return bstack111111l1111_opy_
        except Exception as e:
            logger.error(bstack1l1ll_opy_ (u"ࠧࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡸࡥࡲࡷࡨࡷࡹࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࡼࡿࠣ࠱ࠥࢁࡽࠣἿ").format(e, url))
            return None
    @staticmethod
    def bstack11l1l1l11l1_opy_(bstack1111111lll1_opy_, data):
        bstack1l1ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡗࡪࡴࡤࡴࠢࡤࠤࡕ࡛ࡔࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡹ࡮ࡥࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡶࡨࡷࡹࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦὀ")
        bstack1111111l1ll_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫὁ"), bstack1l1ll_opy_ (u"ࠨࠩὂ"))
        headers = {
            bstack1l1ll_opy_ (u"ࠩࡤࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩὃ"): bstack1l1ll_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࡿࢂ࠭ὄ").format(bstack1111111l1ll_opy_),
            bstack1l1ll_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪὅ"): bstack1l1ll_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ὆")
        }
        response = requests.put(bstack1111111lll1_opy_, headers=headers, json=data)
        bstack111111l1111_opy_ = {}
        try:
            bstack111111l1111_opy_ = response.json()
        except Exception as e:
            logger.debug(bstack1l1ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧ὇").format(e))
            pass
        logger.debug(bstack1l1ll_opy_ (u"ࠢࡓࡧࡴࡹࡪࡹࡴࡖࡶ࡬ࡰࡸࡀࠠࡱࡷࡷࡣ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤὈ").format(bstack111111l1111_opy_))
        if bstack111111l1111_opy_ is not None:
            bstack111111l1111_opy_[bstack1l1ll_opy_ (u"ࠨࡰࡨࡼࡹࡥࡰࡰ࡮࡯ࡣࡹ࡯࡭ࡦࠩὉ")] = response.headers.get(
                bstack1l1ll_opy_ (u"ࠩࡱࡩࡽࡺ࡟ࡱࡱ࡯ࡰࡤࡺࡩ࡮ࡧࠪὊ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack111111l1111_opy_[bstack1l1ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪὋ")] = response.status_code
        return bstack111111l1111_opy_
    @staticmethod
    def bstack11l1l1l1lll_opy_(bstack1111111lll1_opy_):
        bstack1l1ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡕࡨࡲࡩࡹࠠࡢࠢࡊࡉ࡙ࠦࡲࡦࡳࡸࡩࡸࡺࠠࡵࡱࠣ࡫ࡪࡺࠠࡵࡪࡨࠤࡨࡵࡵ࡯ࡶࠣࡳ࡫ࠦࡦࡢ࡫࡯ࡩࡩࠦࡴࡦࡵࡷࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤὌ")
        bstack1111111l1ll_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩὍ"), bstack1l1ll_opy_ (u"࠭ࠧ὎"))
        headers = {
            bstack1l1ll_opy_ (u"ࠧࡢࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧ὏"): bstack1l1ll_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࡽࢀࠫὐ").format(bstack1111111l1ll_opy_),
            bstack1l1ll_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨὑ"): bstack1l1ll_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ὒ")
        }
        response = requests.get(bstack1111111lll1_opy_, headers=headers)
        bstack111111l1111_opy_ = {}
        try:
            bstack111111l1111_opy_ = response.json()
            logger.debug(bstack1l1ll_opy_ (u"ࠦࡗ࡫ࡱࡶࡧࡶࡸ࡚ࡺࡩ࡭ࡵ࠽ࠤ࡬࡫ࡴࡠࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨὓ").format(bstack111111l1111_opy_))
        except Exception as e:
            logger.debug(bstack1l1ll_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠤ࠲ࠦࡻࡾࠤὔ").format(e, response.text))
            pass
        if bstack111111l1111_opy_ is not None:
            bstack111111l1111_opy_[bstack1l1ll_opy_ (u"࠭࡮ࡦࡺࡷࡣࡵࡵ࡬࡭ࡡࡷ࡭ࡲ࡫ࠧὕ")] = response.headers.get(
                bstack1l1ll_opy_ (u"ࠧ࡯ࡧࡻࡸࡤࡶ࡯࡭࡮ࡢࡸ࡮ࡳࡥࠨὖ"), str(int(datetime.now().timestamp() * 1000))
            )
            bstack111111l1111_opy_[bstack1l1ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨὗ")] = response.status_code
        return bstack111111l1111_opy_