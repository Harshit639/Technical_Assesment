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
import atexit
import signal
import yaml
import socket
import datetime
import string
import random
import collections.abc
import traceback
import copy
import threading
from concurrent.futures import ThreadPoolExecutor, TimeoutError
import json
from packaging import version
from browserstack.local import Local
from urllib.parse import urlparse
from dotenv import load_dotenv
from browserstack_sdk.bstack1l1111ll11_opy_ import bstack1lllll1l1_opy_
from browserstack_sdk.bstack1lll1ll11l_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack1l111l11_opy_():
  global CONFIG
  headers = {
        bstack1l1ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩࡶ"): bstack1l1ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧࡷ"),
      }
  proxies = bstack11ll1llll_opy_(CONFIG, bstack1111lll1_opy_)
  try:
    response = requests.get(bstack1111lll1_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack11lll1l1ll_opy_ = response.json()[bstack1l1ll_opy_ (u"ࠬ࡮ࡵࡣࡵࠪࡸ")]
      logger.debug(bstack1ll1l1l1l_opy_.format(response.json()))
      return bstack11lll1l1ll_opy_
    else:
      logger.debug(bstack11llllll1_opy_.format(bstack1l1ll_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧࡹ")))
  except Exception as e:
    logger.debug(bstack11llllll1_opy_.format(e))
def bstack1lll1ll1l_opy_(hub_url):
  global CONFIG
  url = bstack1l1ll_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤࡺ")+  hub_url + bstack1l1ll_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣࡻ")
  headers = {
        bstack1l1ll_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨࡼ"): bstack1l1ll_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ࡽ"),
      }
  proxies = bstack11ll1llll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1ll11lll1_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1l11ll11_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack111l1ll1l_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
def bstack11l1l11lll_opy_():
  try:
    global bstack1lll11lll_opy_
    bstack11lll1l1ll_opy_ = bstack1l111l11_opy_()
    bstack11ll1lll11_opy_ = []
    results = []
    for bstack1lll111l_opy_ in bstack11lll1l1ll_opy_:
      bstack11ll1lll11_opy_.append(bstack1ll1lll11_opy_(target=bstack1lll1ll1l_opy_,args=(bstack1lll111l_opy_,)))
    for t in bstack11ll1lll11_opy_:
      t.start()
    for t in bstack11ll1lll11_opy_:
      results.append(t.join())
    bstack1lll1l1l11_opy_ = {}
    for item in results:
      hub_url = item[bstack1l1ll_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬࡾ")]
      latency = item[bstack1l1ll_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭ࡿ")]
      bstack1lll1l1l11_opy_[hub_url] = latency
    bstack1lll111l11_opy_ = min(bstack1lll1l1l11_opy_, key= lambda x: bstack1lll1l1l11_opy_[x])
    bstack1lll11lll_opy_ = bstack1lll111l11_opy_
    logger.debug(bstack1l1llll111_opy_.format(bstack1lll111l11_opy_))
  except Exception as e:
    logger.debug(bstack1llll1ll11_opy_.format(e))
from browserstack_sdk.bstack11l1ll111_opy_ import *
from browserstack_sdk.bstack1l11ll1111_opy_ import *
from browserstack_sdk.bstack11l11lll1l_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack1l1111111_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack1lll1ll111_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
def bstack11ll1ll1ll_opy_():
    global bstack1lll11lll_opy_
    try:
        bstack1ll1lllll1_opy_ = bstack1l11l1111l_opy_()
        bstack111lll1l_opy_(bstack1ll1lllll1_opy_)
        hub_url = bstack1ll1lllll1_opy_.get(bstack1l1ll_opy_ (u"ࠨࡵࡳ࡮ࠥࢀ"), bstack1l1ll_opy_ (u"ࠢࠣࢁ"))
        if hub_url.endswith(bstack1l1ll_opy_ (u"ࠨ࠱ࡺࡨ࠴࡮ࡵࡣࠩࢂ")):
            hub_url = hub_url.rsplit(bstack1l1ll_opy_ (u"ࠩ࠲ࡻࡩ࠵ࡨࡶࡤࠪࢃ"), 1)[0]
        if hub_url.startswith(bstack1l1ll_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࠫࢄ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack1l1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࠭ࢅ")):
            hub_url = hub_url[8:]
        bstack1lll11lll_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack1l11l1111l_opy_():
    global CONFIG
    bstack1llllll1l1_opy_ = CONFIG.get(bstack1l1ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩࢆ"), {}).get(bstack1l1ll_opy_ (u"࠭ࡧࡳ࡫ࡧࡒࡦࡳࡥࠨࢇ"), bstack1l1ll_opy_ (u"ࠧࡏࡑࡢࡋࡗࡏࡄࡠࡐࡄࡑࡊࡥࡐࡂࡕࡖࡉࡉ࠭࢈"))
    if not isinstance(bstack1llllll1l1_opy_, str):
        raise ValueError(bstack1l1ll_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡈࡴ࡬ࡨࠥࡴࡡ࡮ࡧࠣࡱࡺࡹࡴࠡࡤࡨࠤࡦࠦࡶࡢ࡮࡬ࡨࠥࡹࡴࡳ࡫ࡱ࡫ࠧࢉ"))
    try:
        bstack1ll1lllll1_opy_ = bstack1l1l111ll_opy_(bstack1llllll1l1_opy_)
        return bstack1ll1lllll1_opy_
    except Exception as e:
        logger.error(bstack1l1ll_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣࢊ").format(str(e)))
        return {}
def bstack1l1l111ll_opy_(bstack1llllll1l1_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack1l1ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬࢋ")] or not CONFIG[bstack1l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧࢌ")]:
            raise ValueError(bstack1l1ll_opy_ (u"ࠧࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡻࡳࡦࡴࡱࡥࡲ࡫ࠠࡰࡴࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠢࢍ"))
        url = bstack1111l1l1_opy_ + bstack1llllll1l1_opy_
        auth = (CONFIG[bstack1l1ll_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨࢎ")], CONFIG[bstack1l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ࢏")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack11l1l11ll1_opy_ = json.loads(response.text)
            return bstack11l1l11ll1_opy_
    except ValueError as ve:
        logger.error(bstack1l1ll_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣ࢐").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack1l1ll_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶࠤ࠿ࠦࡻࡾࠤ࢑").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack111lll1l_opy_(bstack111l1ll11_opy_):
    global CONFIG
    if bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ࢒") not in CONFIG or str(CONFIG[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ࢓")]).lower() == bstack1l1ll_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ࢔"):
        CONFIG[bstack1l1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬ࢕")] = False
    elif bstack1l1ll_opy_ (u"ࠧࡪࡵࡗࡶ࡮ࡧ࡬ࡈࡴ࡬ࡨࠬ࢖") in bstack111l1ll11_opy_:
        bstack111l111l1_opy_ = CONFIG.get(bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬࢗ"), {})
        logger.debug(bstack1l1ll_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴࡩࡡ࡭ࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࠪࡹࠢ࢘"), bstack111l111l1_opy_)
        bstack1l11l1llll_opy_ = bstack111l1ll11_opy_.get(bstack1l1ll_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡕࡩࡵ࡫ࡡࡵࡧࡵࡷ࢙ࠧ"), [])
        bstack11l1llll_opy_ = bstack1l1ll_opy_ (u"ࠦ࠱ࠨ࢚").join(bstack1l11l1llll_opy_)
        logger.debug(bstack1l1ll_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡈࡻࡳࡵࡱࡰࠤࡷ࡫ࡰࡦࡣࡷࡩࡷࠦࡳࡵࡴ࡬ࡲ࡬ࡀࠠࠦࡵ࢛ࠥ"), bstack11l1llll_opy_)
        bstack11ll111l11_opy_ = {
            bstack1l1ll_opy_ (u"ࠨ࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣ࢜"): bstack1l1ll_opy_ (u"ࠢࡢࡶࡶ࠱ࡷ࡫ࡰࡦࡣࡷࡩࡷࠨ࢝"),
            bstack1l1ll_opy_ (u"ࠣࡨࡲࡶࡨ࡫ࡌࡰࡥࡤࡰࠧ࢞"): bstack1l1ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ࢟"),
            bstack1l1ll_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠧࢠ"): bstack11l1llll_opy_
        }
        bstack111l111l1_opy_.update(bstack11ll111l11_opy_)
        logger.debug(bstack1l1ll_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼࡙ࠣࡵࡪࡡࡵࡧࡧࠤࡱࡵࡣࡢ࡮ࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࠫࡳࠣࢡ"), bstack111l111l1_opy_)
        CONFIG[bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩࢢ")] = bstack111l111l1_opy_
        logger.debug(bstack1l1ll_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡌࡩ࡯ࡣ࡯ࠤࡈࡕࡎࡇࡋࡊ࠾ࠥࠫࡳࠣࢣ"), CONFIG)
def bstack1ll11lll_opy_():
    bstack1ll1lllll1_opy_ = bstack1l11l1111l_opy_()
    if not bstack1ll1lllll1_opy_[bstack1l1ll_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠧࢤ")]:
      raise ValueError(bstack1l1ll_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠡ࡫ࡶࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࡬ࡲࡰ࡯ࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠥࢥ"))
    return bstack1ll1lllll1_opy_[bstack1l1ll_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࡛ࡲ࡭ࠩࢦ")] + bstack1l1ll_opy_ (u"ࠪࡃࡨࡧࡰࡴ࠿ࠪࢧ")
@measure(event_name=EVENTS.bstack11l11ll11l_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
def bstack1llllllll1_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack1l1ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ࢨ")], CONFIG[bstack1l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨࢩ")])
        url = bstack1lllllllll_opy_
        logger.debug(bstack1l1ll_opy_ (u"ࠨࡁࡵࡶࡨࡱࡵࡺࡩ࡯ࡩࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬ࡲࡰ࡯ࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡗࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࠦࡁࡑࡋࠥࢪ"))
        try:
            response = requests.get(url, auth=auth, headers={bstack1l1ll_opy_ (u"ࠢࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪࠨࢫ"): bstack1l1ll_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠦࢬ")})
            if response.status_code == 200:
                bstack1l1l1l111_opy_ = json.loads(response.text)
                bstack11l11llll_opy_ = bstack1l1l1l111_opy_.get(bstack1l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡴࠩࢭ"), [])
                if bstack11l11llll_opy_:
                    bstack1l11ll1l11_opy_ = bstack11l11llll_opy_[0]
                    build_hashed_id = bstack1l11ll1l11_opy_.get(bstack1l1ll_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ࢮ"))
                    bstack1l1ll111l1_opy_ = bstack111l11l11_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1l1ll111l1_opy_])
                    logger.info(bstack11lll1l1l_opy_.format(bstack1l1ll111l1_opy_))
                    bstack11l111ll11_opy_ = CONFIG[bstack1l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧࢯ")]
                    if bstack1l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧࢰ") in CONFIG:
                      bstack11l111ll11_opy_ += bstack1l1ll_opy_ (u"࠭ࠠࠨࢱ") + CONFIG[bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩࢲ")]
                    if bstack11l111ll11_opy_ != bstack1l11ll1l11_opy_.get(bstack1l1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ࢳ")):
                      logger.debug(bstack11l1lll1ll_opy_.format(bstack1l11ll1l11_opy_.get(bstack1l1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧࢴ")), bstack11l111ll11_opy_))
                    return result
                else:
                    logger.debug(bstack1l1ll_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡑࡳࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡵࡪࡨࠤࡷ࡫ࡳࡱࡱࡱࡷࡪ࠴ࠢࢵ"))
            else:
                logger.debug(bstack1l1ll_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨࢶ"))
        except Exception as e:
            logger.error(bstack1l1ll_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࡹࠠ࠻ࠢࡾࢁࠧࢷ").format(str(e)))
    else:
        logger.debug(bstack1l1ll_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡉࡏࡏࡈࡌࡋࠥ࡯ࡳࠡࡰࡲࡸࠥࡹࡥࡵ࠰࡙ࠣࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨࢸ"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack11ll1lll1l_opy_ import bstack11ll1lll1l_opy_, bstack111l1lll_opy_, bstack1l1l1ll111_opy_, bstack1l11111l1_opy_
from bstack_utils.measure import bstack11l1l111l_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1l11111l1l_opy_ import bstack1l111ll11l_opy_
from bstack_utils.messages import *
from bstack_utils import bstack1l1111111_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack11l1111l1_opy_, bstack1ll1l1l1l1_opy_, bstack1lll1ll1ll_opy_, bstack11ll1ll11_opy_, \
  bstack1ll1ll111l_opy_, \
  Notset, bstack1l111l1l1_opy_, \
  bstack11l1111ll1_opy_, bstack1l11111111_opy_, bstack1ll1ll1ll_opy_, bstack1ll11llll_opy_, bstack1lll11l111_opy_, bstack11111111_opy_, \
  bstack11ll1l1l1_opy_, \
  bstack11lllllll_opy_, bstack11l11ll1l1_opy_, bstack1l1l111111_opy_, bstack1l1l1l1l11_opy_, \
  bstack1lll1l11ll_opy_, bstack11lllll1l_opy_, bstack1ll1l11l_opy_, bstack11l1l1l1_opy_
from bstack_utils.bstack1ll1llll_opy_ import bstack111ll111_opy_
from bstack_utils.bstack11l11l11ll_opy_ import bstack11l1111l_opy_, bstack1lll11lll1_opy_
from bstack_utils.bstack11l1111l1l_opy_ import bstack1l11ll111_opy_
from bstack_utils.bstack1l1l11l11_opy_ import bstack1l1l111l1_opy_, bstack1111l1ll_opy_
from bstack_utils.bstack11111lll_opy_ import bstack11111lll_opy_
from bstack_utils.bstack1lll11l11l_opy_ import bstack11l1lll1l1_opy_
from bstack_utils.proxy import bstack11l1111l11_opy_, bstack11ll1llll_opy_, bstack11llll1l11_opy_, bstack1ll1111l1_opy_
from bstack_utils.bstack1ll1lll1ll_opy_ import bstack1l111l1111_opy_
import bstack_utils.bstack1l1111llll_opy_ as bstack1l111l111l_opy_
import bstack_utils.bstack11l11l1l1_opy_ as bstack1lll1lll1l_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack11l1lll11l_opy_ import bstack1111111l1_opy_
from bstack_utils.bstack111llllll1_opy_ import bstack1ll1l111l1_opy_
from bstack_utils.bstack1lll11ll_opy_ import bstack11lllll11_opy_
if os.getenv(bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡌࡔࡕࡋࡔࠩࢹ")):
  cli.bstack1llllll111_opy_()
else:
  os.environ[bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡍࡕࡏࡌࡕࠪࢺ")] = bstack1l1ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧࢻ")
bstack11l1lll111_opy_ = bstack1l1ll_opy_ (u"ࠪࠤࠥ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࠣࠤ࡮࡬ࠨࡱࡣࡪࡩࠥࡃ࠽࠾ࠢࡹࡳ࡮ࡪࠠ࠱ࠫࠣࡿࡡࡴࠠࠡࠢࡷࡶࡾࢁ࡜࡯ࠢࡦࡳࡳࡹࡴࠡࡨࡶࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨ࡝ࠩࡩࡷࡡ࠭ࠩ࠼࡞ࡱࠤࠥࠦࠠࠡࡨࡶ࠲ࡦࡶࡰࡦࡰࡧࡊ࡮ࡲࡥࡔࡻࡱࡧ࠭ࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪ࠯ࠤࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡶ࡟ࡪࡰࡧࡩࡽ࠯ࠠࠬࠢࠥ࠾ࠧࠦࠫࠡࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࠨࡢࡹࡤ࡭ࡹࠦ࡮ࡦࡹࡓࡥ࡬࡫࠲࠯ࡧࡹࡥࡱࡻࡡࡵࡧࠫࠦ࠭࠯ࠠ࠾ࡀࠣࡿࢂࠨࠬࠡ࡞ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥ࡫ࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡄࡦࡶࡤ࡭ࡱࡹࠢࡾ࡞ࠪ࠭࠮࠯࡛ࠣࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠦࡢ࠯ࠠࠬࠢࠥ࠰ࡡࡢ࡮ࠣࠫ࡟ࡲࠥࠦࠠࠡࡿࡦࡥࡹࡩࡨࠩࡧࡻ࠭ࢀࡢ࡮ࠡࠢࠣࠤࢂࡢ࡮ࠡࠢࢀࡠࡳࠦࠠ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱ࠪࢼ")
bstack11llll11l1_opy_ = bstack1l1ll_opy_ (u"ࠫࡡࡴ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰࡞ࡱࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡳࡥࡹ࡮ࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠶ࡡࡡࡴࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠷࡝࡝ࡰࡦࡳࡳࡹࡴࠡࡲࡢ࡭ࡳࡪࡥࡹࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠷ࡣ࡜࡯ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯ࡵ࡯࡭ࡨ࡫ࠨ࠱࠮ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸࠯࡜࡯ࡥࡲࡲࡸࡺࠠࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯ࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨࠩ࠼࡞ࡱ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡰࡦࡻ࡮ࡤࡪࠣࡁࠥࡧࡳࡺࡰࡦࠤ࠭ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷ࠮ࠦ࠽࠿ࠢࡾࡠࡳࡲࡥࡵࠢࡦࡥࡵࡹ࠻࡝ࡰࡷࡶࡾࠦࡻ࡝ࡰࡦࡥࡵࡹࠠ࠾ࠢࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶ࠭ࡡࡴࠠࠡࡿࠣࡧࡦࡺࡣࡩࠪࡨࡼ࠮ࠦࡻ࡝ࡰࠣࠤࠥࠦࡽ࡝ࡰࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡦࡽࡡࡪࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡧࡴࡴ࡮ࡦࡥࡷࠬࢀࡢ࡮ࠡࠢࠣࠤࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴ࠻ࠢࡣࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠩࢁࡥ࡯ࡥࡲࡨࡪ࡛ࡒࡊࡅࡲࡱࡵࡵ࡮ࡦࡰࡷࠬࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡩࡡࡱࡵࠬ࠭ࢂࡦࠬ࡝ࡰࠣࠤࠥࠦ࠮࠯࠰࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴ࡞ࡱࠤࠥࢃࠩ࡝ࡰࢀࡠࡳ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࠪࢽ")
from ._version import __version__
bstack1ll1ll1l1l_opy_ = None
CONFIG = {}
bstack1l1l1l1l1_opy_ = {}
bstack111ll1l11_opy_ = {}
bstack1lllll11ll_opy_ = None
bstack11ll111ll_opy_ = None
bstack1l1l1ll1l_opy_ = None
bstack11ll1ll111_opy_ = -1
bstack1l1ll1ll_opy_ = 0
bstack11l1llll11_opy_ = bstack111l1111l_opy_
bstack1l1l1111ll_opy_ = 1
bstack1llll1l1_opy_ = False
bstack1111l11l_opy_ = False
bstack111llll11_opy_ = bstack1l1ll_opy_ (u"ࠬ࠭ࢾ")
bstack111ll1l1_opy_ = bstack1l1ll_opy_ (u"࠭ࠧࢿ")
bstack1llll1l1l1_opy_ = False
bstack1ll1l111ll_opy_ = True
bstack1llll1lll_opy_ = bstack1l1ll_opy_ (u"ࠧࠨࣀ")
bstack1lllllll1_opy_ = []
bstack1lllll11l_opy_ = threading.Lock()
bstack1l1ll1lll_opy_ = threading.Lock()
bstack1lll11lll_opy_ = bstack1l1ll_opy_ (u"ࠨࠩࣁ")
bstack1lll1l1111_opy_ = False
bstack1l1l1l1ll1_opy_ = None
bstack111l1111_opy_ = None
bstack11llll11_opy_ = None
bstack1ll11ll1l_opy_ = -1
bstack1lll1l1l_opy_ = os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠩࢁࠫࣂ")), bstack1l1ll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪࣃ"), bstack1l1ll_opy_ (u"ࠫ࠳ࡸ࡯ࡣࡱࡷ࠱ࡷ࡫ࡰࡰࡴࡷ࠱࡭࡫࡬ࡱࡧࡵ࠲࡯ࡹ࡯࡯ࠩࣄ"))
bstack1llll1l11l_opy_ = 0
bstack1l1l1ll1_opy_ = 0
bstack11lll11111_opy_ = []
bstack111llll1l_opy_ = []
bstack1l11l1l11_opy_ = []
bstack1ll1l11lll_opy_ = []
bstack1l1l1lll1_opy_ = bstack1l1ll_opy_ (u"ࠬ࠭ࣅ")
bstack111111ll_opy_ = bstack1l1ll_opy_ (u"࠭ࠧࣆ")
bstack111ll111l_opy_ = False
bstack111ll11ll_opy_ = False
bstack1l11l1111_opy_ = {}
bstack1l11lll1l_opy_ = None
bstack1l1l11lll_opy_ = None
bstack1ll11111l_opy_ = None
bstack111lllll1l_opy_ = None
bstack11ll11l1ll_opy_ = None
bstack11ll1lllll_opy_ = None
bstack1l1ll1ll1l_opy_ = None
bstack11111llll_opy_ = None
bstack11111l11l_opy_ = None
bstack11llll111_opy_ = None
bstack1111l11l1_opy_ = None
bstack1ll111ll1_opy_ = None
bstack11l111ll_opy_ = None
bstack1l11lll1ll_opy_ = None
bstack11ll111lll_opy_ = None
bstack1l1111l1ll_opy_ = None
bstack11ll1111l_opy_ = None
bstack11l11111_opy_ = None
bstack11ll1lll_opy_ = None
bstack1llll111l_opy_ = None
bstack11ll11llll_opy_ = None
bstack1l11ll11l_opy_ = None
bstack1l1l1llll_opy_ = None
thread_local = threading.local()
bstack1lll111l1l_opy_ = False
bstack1l1lll1ll_opy_ = bstack1l1ll_opy_ (u"ࠢࠣࣇ")
logger = bstack1l1111111_opy_.get_logger(__name__, bstack11l1llll11_opy_)
bstack11l1lll1_opy_ = Config.bstack11ll11ll1_opy_()
percy = bstack1lll1l11_opy_()
bstack1l11111l_opy_ = bstack1l111ll11l_opy_()
bstack11llll1ll1_opy_ = bstack11l11lll1l_opy_()
def bstack11ll1111_opy_():
  global CONFIG
  global bstack111ll111l_opy_
  global bstack11l1lll1_opy_
  testContextOptions = bstack111lllllll_opy_(CONFIG)
  if bstack1ll1ll111l_opy_(CONFIG):
    if (bstack1l1ll_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪࣈ") in testContextOptions and str(testContextOptions[bstack1l1ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫࣉ")]).lower() == bstack1l1ll_opy_ (u"ࠪࡸࡷࡻࡥࠨ࣊")):
      bstack111ll111l_opy_ = True
    bstack11l1lll1_opy_.bstack1ll1111lll_opy_(testContextOptions.get(bstack1l1ll_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ࣋"), False))
  else:
    bstack111ll111l_opy_ = True
    bstack11l1lll1_opy_.bstack1ll1111lll_opy_(True)
def bstack1lllllll1l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1l1l1l111l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1ll1l11l11_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1l1ll_opy_ (u"ࠧ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡩ࡯࡯ࡨ࡬࡫࡫࡯࡬ࡦࠤ࣌") == args[i].lower() or bstack1l1ll_opy_ (u"ࠨ࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡱࡪ࡮࡭ࠢ࣍") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1llll1lll_opy_
      bstack1llll1lll_opy_ += bstack1l1ll_opy_ (u"ࠧ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡄࡱࡱࡪ࡮࡭ࡆࡪ࡮ࡨࠤࠧ࠭࣎") + path + bstack1l1ll_opy_ (u"ࠨࠤ࣏ࠪ")
      return path
  return None
bstack11l1111111_opy_ = re.compile(bstack1l1ll_opy_ (u"ࡴࠥ࠲࠯ࡅ࡜ࠥࡽࠫ࠲࠯ࡅࠩࡾ࠰࠭ࡃ࣐ࠧ"))
def bstack1l111lll_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack11l1111111_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1l1ll_opy_ (u"ࠥࠨࢀࠨ࣑") + group + bstack1l1ll_opy_ (u"ࠦࢂࠨ࣒"), os.environ.get(group))
  return value
def bstack1lll111l1_opy_():
  global bstack1l1l1llll_opy_
  if bstack1l1l1llll_opy_ is None:
        bstack1l1l1llll_opy_ = bstack1ll1l11l11_opy_()
  bstack11l111lll_opy_ = bstack1l1l1llll_opy_
  if bstack11l111lll_opy_ and os.path.exists(os.path.abspath(bstack11l111lll_opy_)):
    fileName = bstack11l111lll_opy_
  if bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆ࣓ࠩ") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࡤࡌࡉࡍࡇࠪࣔ")])) and not bstack1l1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡓࡧ࡭ࡦࠩࣕ") in locals():
    fileName = os.environ[bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬࣖ")]
  if bstack1l1ll_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡎࡢ࡯ࡨࠫࣗ") in locals():
    bstack1l1l1l1_opy_ = os.path.abspath(fileName)
  else:
    bstack1l1l1l1_opy_ = bstack1l1ll_opy_ (u"ࠪࠫࣘ")
  bstack111l11ll1_opy_ = os.getcwd()
  bstack11ll1l111_opy_ = bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠧࣙ")
  bstack1111111ll_opy_ = bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡧ࡭࡭ࠩࣚ")
  while (not os.path.exists(bstack1l1l1l1_opy_)) and bstack111l11ll1_opy_ != bstack1l1ll_opy_ (u"ࠨࠢࣛ"):
    bstack1l1l1l1_opy_ = os.path.join(bstack111l11ll1_opy_, bstack11ll1l111_opy_)
    if not os.path.exists(bstack1l1l1l1_opy_):
      bstack1l1l1l1_opy_ = os.path.join(bstack111l11ll1_opy_, bstack1111111ll_opy_)
    if bstack111l11ll1_opy_ != os.path.dirname(bstack111l11ll1_opy_):
      bstack111l11ll1_opy_ = os.path.dirname(bstack111l11ll1_opy_)
    else:
      bstack111l11ll1_opy_ = bstack1l1ll_opy_ (u"ࠢࠣࣜ")
  bstack1l1l1llll_opy_ = bstack1l1l1l1_opy_ if os.path.exists(bstack1l1l1l1_opy_) else None
  return bstack1l1l1llll_opy_
def bstack1llll111_opy_():
  bstack1l1l1l1_opy_ = bstack1lll111l1_opy_()
  if not os.path.exists(bstack1l1l1l1_opy_):
    bstack111111l11_opy_(
      bstack11l1l1l111_opy_.format(os.getcwd()))
  try:
    with open(bstack1l1l1l1_opy_, bstack1l1ll_opy_ (u"ࠨࡴࠪࣝ")) as stream:
      yaml.add_implicit_resolver(bstack1l1ll_opy_ (u"ࠤࠤࡴࡦࡺࡨࡦࡺࠥࣞ"), bstack11l1111111_opy_)
      yaml.add_constructor(bstack1l1ll_opy_ (u"ࠥࠥࡵࡧࡴࡩࡧࡻࠦࣟ"), bstack1l111lll_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      return config
  except:
    with open(bstack1l1l1l1_opy_, bstack1l1ll_opy_ (u"ࠫࡷ࠭࣠")) as stream:
      try:
        config = yaml.safe_load(stream)
        return config
      except yaml.YAMLError as exc:
        bstack111111l11_opy_(bstack1ll111ll1l_opy_.format(str(exc)))
def bstack11ll111l1l_opy_(config):
  bstack11111111l_opy_ = bstack1111llll1_opy_(config)
  for option in list(bstack11111111l_opy_):
    if option.lower() in bstack1l1lll11l1_opy_ and option != bstack1l1lll11l1_opy_[option.lower()]:
      bstack11111111l_opy_[bstack1l1lll11l1_opy_[option.lower()]] = bstack11111111l_opy_[option]
      del bstack11111111l_opy_[option]
  return config
def bstack1ll11l111_opy_():
  global bstack111ll1l11_opy_
  for key, bstack1ll1111ll1_opy_ in bstack1l1ll111l_opy_.items():
    if isinstance(bstack1ll1111ll1_opy_, list):
      for var in bstack1ll1111ll1_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack111ll1l11_opy_[key] = os.environ[var]
          break
    elif bstack1ll1111ll1_opy_ in os.environ and os.environ[bstack1ll1111ll1_opy_] and str(os.environ[bstack1ll1111ll1_opy_]).strip():
      bstack111ll1l11_opy_[key] = os.environ[bstack1ll1111ll1_opy_]
  if bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ࣡") in os.environ:
    bstack111ll1l11_opy_[bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ࣢")] = {}
    bstack111ll1l11_opy_[bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࣣࠫ")][bstack1l1ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪࣤ")] = os.environ[bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫࣥ")]
def bstack11l11111l1_opy_():
  global bstack1l1l1l1l1_opy_
  global bstack1llll1lll_opy_
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) and bstack1l1ll_opy_ (u"ࠪ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࣦ࠭").lower() == val.lower():
      bstack1l1l1l1l1_opy_[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨࣧ")] = {}
      bstack1l1l1l1l1_opy_[bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩࣨ")][bstack1l1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣩ")] = sys.argv[idx + 1]
      del sys.argv[idx:idx + 2]
      break
  for key, bstack111lll1ll_opy_ in bstack1l111llll1_opy_.items():
    if isinstance(bstack111lll1ll_opy_, list):
      for idx, val in enumerate(sys.argv):
        for var in bstack111lll1ll_opy_:
          if idx < len(sys.argv) and bstack1l1ll_opy_ (u"ࠧ࠮࠯ࠪ࣪") + var.lower() == val.lower() and not key in bstack1l1l1l1l1_opy_:
            bstack1l1l1l1l1_opy_[key] = sys.argv[idx + 1]
            bstack1llll1lll_opy_ += bstack1l1ll_opy_ (u"ࠨࠢ࠰࠱ࠬ࣫") + var + bstack1l1ll_opy_ (u"ࠩࠣࠫ࣬") + sys.argv[idx + 1]
            del sys.argv[idx:idx + 2]
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx < len(sys.argv) and bstack1l1ll_opy_ (u"ࠪ࠱࠲࣭࠭") + bstack111lll1ll_opy_.lower() == val.lower() and not key in bstack1l1l1l1l1_opy_:
          bstack1l1l1l1l1_opy_[key] = sys.argv[idx + 1]
          bstack1llll1lll_opy_ += bstack1l1ll_opy_ (u"ࠫࠥ࠳࠭ࠨ࣮") + bstack111lll1ll_opy_ + bstack1l1ll_opy_ (u"࣯ࠬࠦࠧ") + sys.argv[idx + 1]
          del sys.argv[idx:idx + 2]
def bstack11ll111l1_opy_(config):
  bstack1ll11111ll_opy_ = config.keys()
  for bstack1ll1lllll_opy_, bstack11lll111l1_opy_ in bstack11111l11_opy_.items():
    if bstack11lll111l1_opy_ in bstack1ll11111ll_opy_:
      config[bstack1ll1lllll_opy_] = config[bstack11lll111l1_opy_]
      del config[bstack11lll111l1_opy_]
  for bstack1ll1lllll_opy_, bstack11lll111l1_opy_ in bstack1l1llll1l1_opy_.items():
    if isinstance(bstack11lll111l1_opy_, list):
      for bstack11l11l1lll_opy_ in bstack11lll111l1_opy_:
        if bstack11l11l1lll_opy_ in bstack1ll11111ll_opy_:
          config[bstack1ll1lllll_opy_] = config[bstack11l11l1lll_opy_]
          del config[bstack11l11l1lll_opy_]
          break
    elif bstack11lll111l1_opy_ in bstack1ll11111ll_opy_:
      config[bstack1ll1lllll_opy_] = config[bstack11lll111l1_opy_]
      del config[bstack11lll111l1_opy_]
  for bstack11l11l1lll_opy_ in list(config):
    for bstack11llll1111_opy_ in bstack11l11l111_opy_:
      if bstack11l11l1lll_opy_.lower() == bstack11llll1111_opy_.lower() and bstack11l11l1lll_opy_ != bstack11llll1111_opy_:
        config[bstack11llll1111_opy_] = config[bstack11l11l1lll_opy_]
        del config[bstack11l11l1lll_opy_]
  bstack1l1111l11_opy_ = [{}]
  if not config.get(bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࣰࠩ")):
    config[bstack1l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࣱࠪ")] = [{}]
  bstack1l1111l11_opy_ = config[bstack1l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࣲࠫ")]
  for platform in bstack1l1111l11_opy_:
    for bstack11l11l1lll_opy_ in list(platform):
      for bstack11llll1111_opy_ in bstack11l11l111_opy_:
        if bstack11l11l1lll_opy_.lower() == bstack11llll1111_opy_.lower() and bstack11l11l1lll_opy_ != bstack11llll1111_opy_:
          platform[bstack11llll1111_opy_] = platform[bstack11l11l1lll_opy_]
          del platform[bstack11l11l1lll_opy_]
  for bstack1ll1lllll_opy_, bstack11lll111l1_opy_ in bstack1l1llll1l1_opy_.items():
    for platform in bstack1l1111l11_opy_:
      if isinstance(bstack11lll111l1_opy_, list):
        for bstack11l11l1lll_opy_ in bstack11lll111l1_opy_:
          if bstack11l11l1lll_opy_ in platform:
            platform[bstack1ll1lllll_opy_] = platform[bstack11l11l1lll_opy_]
            del platform[bstack11l11l1lll_opy_]
            break
      elif bstack11lll111l1_opy_ in platform:
        platform[bstack1ll1lllll_opy_] = platform[bstack11lll111l1_opy_]
        del platform[bstack11lll111l1_opy_]
  for bstack1lll1l11l1_opy_ in bstack1lll11l1l1_opy_:
    if bstack1lll1l11l1_opy_ in config:
      if not bstack1lll11l1l1_opy_[bstack1lll1l11l1_opy_] in config:
        config[bstack1lll11l1l1_opy_[bstack1lll1l11l1_opy_]] = {}
      config[bstack1lll11l1l1_opy_[bstack1lll1l11l1_opy_]].update(config[bstack1lll1l11l1_opy_])
      del config[bstack1lll1l11l1_opy_]
  for platform in bstack1l1111l11_opy_:
    for bstack1lll1l11l1_opy_ in bstack1lll11l1l1_opy_:
      if bstack1lll1l11l1_opy_ in list(platform):
        if not bstack1lll11l1l1_opy_[bstack1lll1l11l1_opy_] in platform:
          platform[bstack1lll11l1l1_opy_[bstack1lll1l11l1_opy_]] = {}
        platform[bstack1lll11l1l1_opy_[bstack1lll1l11l1_opy_]].update(platform[bstack1lll1l11l1_opy_])
        del platform[bstack1lll1l11l1_opy_]
  config = bstack11ll111l1l_opy_(config)
  return config
def bstack1l1lll1ll1_opy_(config):
  global bstack111ll1l1_opy_
  bstack11lll111_opy_ = False
  if bstack1l1ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ࣳ") in config and str(config[bstack1l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧࣴ")]).lower() != bstack1l1ll_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪࣵ"):
    if bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࣶࠩ") not in config or str(config[bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪࣷ")]).lower() == bstack1l1ll_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ࣸ"):
      config[bstack1l1ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࣹࠧ")] = False
    else:
      bstack1ll1lllll1_opy_ = bstack1l11l1111l_opy_()
      if bstack1l1ll_opy_ (u"ࠩ࡬ࡷ࡙ࡸࡩࡢ࡮ࡊࡶ࡮ࡪࣺࠧ") in bstack1ll1lllll1_opy_:
        if not bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧࣻ") in config:
          config[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨࣼ")] = {}
        config[bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩࣽ")][bstack1l1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨࣾ")] = bstack1l1ll_opy_ (u"ࠧࡢࡶࡶ࠱ࡷ࡫ࡰࡦࡣࡷࡩࡷ࠭ࣿ")
        bstack11lll111_opy_ = True
        bstack111ll1l1_opy_ = config[bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬऀ")].get(bstack1l1ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫँ"))
  if bstack1ll1ll111l_opy_(config) and bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧं") in config and str(config[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨः")]).lower() != bstack1l1ll_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫऄ") and not bstack11lll111_opy_:
    if not bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪअ") in config:
      config[bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫआ")] = {}
    if not config[bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬइ")].get(bstack1l1ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡂࡪࡰࡤࡶࡾࡏ࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡢࡶ࡬ࡳࡳ࠭ई")) and not bstack1l1ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬउ") in config[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨऊ")]:
      bstack1lllll1l11_opy_ = datetime.datetime.now()
      bstack1ll111l1_opy_ = bstack1lllll1l11_opy_.strftime(bstack1l1ll_opy_ (u"ࠬࠫࡤࡠࠧࡥࡣࠪࡎࠥࡎࠩऋ"))
      hostname = socket.gethostname()
      bstack111111l1_opy_ = bstack1l1ll_opy_ (u"࠭ࠧऌ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1l1ll_opy_ (u"ࠧࡼࡿࡢࡿࢂࡥࡻࡾࠩऍ").format(bstack1ll111l1_opy_, hostname, bstack111111l1_opy_)
      config[bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬऎ")][bstack1l1ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫए")] = identifier
    bstack111ll1l1_opy_ = config[bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧऐ")].get(bstack1l1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ऑ"))
  return config
def bstack1l11111ll1_opy_():
  bstack11l1lllll_opy_ =  bstack1ll11llll_opy_()[bstack1l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠫऒ")]
  return bstack11l1lllll_opy_ if bstack11l1lllll_opy_ else -1
def bstack11lll1ll11_opy_(bstack11l1lllll_opy_):
  global CONFIG
  if not bstack1l1ll_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨओ") in CONFIG[bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩऔ")]:
    return
  CONFIG[bstack1l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪक")] = CONFIG[bstack1l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫख")].replace(
    bstack1l1ll_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬग"),
    str(bstack11l1lllll_opy_)
  )
def bstack1l1l1111l1_opy_():
  global CONFIG
  if not bstack1l1ll_opy_ (u"ࠫࠩࢁࡄࡂࡖࡈࡣ࡙ࡏࡍࡆࡿࠪघ") in CONFIG[bstack1l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧङ")]:
    return
  bstack1lllll1l11_opy_ = datetime.datetime.now()
  bstack1ll111l1_opy_ = bstack1lllll1l11_opy_.strftime(bstack1l1ll_opy_ (u"࠭ࠥࡥ࠯ࠨࡦ࠲ࠫࡈ࠻ࠧࡐࠫच"))
  CONFIG[bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩछ")] = CONFIG[bstack1l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪज")].replace(
    bstack1l1ll_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨझ"),
    bstack1ll111l1_opy_
  )
def bstack11l11lll1_opy_():
  global CONFIG
  if bstack1l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬञ") in CONFIG and not bool(CONFIG[bstack1l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ट")]):
    del CONFIG[bstack1l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧठ")]
    return
  if not bstack1l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨड") in CONFIG:
    CONFIG[bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩढ")] = bstack1l1ll_opy_ (u"ࠨࠥࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫण")
  if bstack1l1ll_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨत") in CONFIG[bstack1l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬथ")]:
    bstack1l1l1111l1_opy_()
    os.environ[bstack1l1ll_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨद")] = CONFIG[bstack1l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧध")]
  if not bstack1l1ll_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨन") in CONFIG[bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩऩ")]:
    return
  bstack11l1lllll_opy_ = bstack1l1ll_opy_ (u"ࠨࠩप")
  bstack1l11lll111_opy_ = bstack1l11111ll1_opy_()
  if bstack1l11lll111_opy_ != -1:
    bstack11l1lllll_opy_ = bstack1l1ll_opy_ (u"ࠩࡆࡍࠥ࠭फ") + str(bstack1l11lll111_opy_)
  if bstack11l1lllll_opy_ == bstack1l1ll_opy_ (u"ࠪࠫब"):
    bstack11l1l1l1l1_opy_ = bstack1lll1lll_opy_(CONFIG[bstack1l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧभ")])
    if bstack11l1l1l1l1_opy_ != -1:
      bstack11l1lllll_opy_ = str(bstack11l1l1l1l1_opy_)
  if bstack11l1lllll_opy_:
    bstack11lll1ll11_opy_(bstack11l1lllll_opy_)
    os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩम")] = CONFIG[bstack1l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨय")]
def bstack1l1lllll_opy_(bstack1l1ll1111_opy_, bstack1l1l11llll_opy_, path):
  bstack1ll111ll11_opy_ = {
    bstack1l1ll_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫर"): bstack1l1l11llll_opy_
  }
  if os.path.exists(path):
    bstack111l11lll_opy_ = json.load(open(path, bstack1l1ll_opy_ (u"ࠨࡴࡥࠫऱ")))
  else:
    bstack111l11lll_opy_ = {}
  bstack111l11lll_opy_[bstack1l1ll1111_opy_] = bstack1ll111ll11_opy_
  with open(path, bstack1l1ll_opy_ (u"ࠤࡺ࠯ࠧल")) as outfile:
    json.dump(bstack111l11lll_opy_, outfile)
def bstack1lll1lll_opy_(bstack1l1ll1111_opy_):
  bstack1l1ll1111_opy_ = str(bstack1l1ll1111_opy_)
  bstack1l1ll1lll1_opy_ = os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠪࢂࠬळ")), bstack1l1ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫऴ"))
  try:
    if not os.path.exists(bstack1l1ll1lll1_opy_):
      os.makedirs(bstack1l1ll1lll1_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠬࢄࠧव")), bstack1l1ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭श"), bstack1l1ll_opy_ (u"ࠧ࠯ࡤࡸ࡭ࡱࡪ࠭࡯ࡣࡰࡩ࠲ࡩࡡࡤࡪࡨ࠲࡯ࡹ࡯࡯ࠩष"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1l1ll_opy_ (u"ࠨࡹࠪस")):
        pass
      with open(file_path, bstack1l1ll_opy_ (u"ࠤࡺ࠯ࠧह")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1l1ll_opy_ (u"ࠪࡶࠬऺ")) as bstack11l1l1ll11_opy_:
      bstack1l1ll11ll1_opy_ = json.load(bstack11l1l1ll11_opy_)
    if bstack1l1ll1111_opy_ in bstack1l1ll11ll1_opy_:
      bstack1ll1ll1l1_opy_ = bstack1l1ll11ll1_opy_[bstack1l1ll1111_opy_][bstack1l1ll_opy_ (u"ࠫ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨऻ")]
      bstack1l1llll1ll_opy_ = int(bstack1ll1ll1l1_opy_) + 1
      bstack1l1lllll_opy_(bstack1l1ll1111_opy_, bstack1l1llll1ll_opy_, file_path)
      return bstack1l1llll1ll_opy_
    else:
      bstack1l1lllll_opy_(bstack1l1ll1111_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack11l11l1ll_opy_.format(str(e)))
    return -1
def bstack1lllll111l_opy_(config):
  if not config[bstack1l1ll_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫़ࠧ")] or not config[bstack1l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩऽ")]:
    return True
  else:
    return False
def bstack1l1lll11l_opy_(config, index=0):
  global bstack1llll1l1l1_opy_
  bstack11l1l111l1_opy_ = {}
  caps = bstack1ll1lll1l1_opy_ + bstack111lll11_opy_
  if config.get(bstack1l1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫा"), False):
    bstack11l1l111l1_opy_[bstack1l1ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬि")] = True
    bstack11l1l111l1_opy_[bstack1l1ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ी")] = config.get(bstack1l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧु"), {})
  if bstack1llll1l1l1_opy_:
    caps += bstack1lll1lll1_opy_
  for key in config:
    if key in caps + [bstack1l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧू")]:
      continue
    bstack11l1l111l1_opy_[key] = config[key]
  if bstack1l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨृ") in config:
    for bstack1ll111l111_opy_ in config[bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩॄ")][index]:
      if bstack1ll111l111_opy_ in caps:
        continue
      bstack11l1l111l1_opy_[bstack1ll111l111_opy_] = config[bstack1l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪॅ")][index][bstack1ll111l111_opy_]
  bstack11l1l111l1_opy_[bstack1l1ll_opy_ (u"ࠨࡪࡲࡷࡹࡔࡡ࡮ࡧࠪॆ")] = socket.gethostname()
  if bstack1l1ll_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪे") in bstack11l1l111l1_opy_:
    del (bstack11l1l111l1_opy_[bstack1l1ll_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫै")])
  return bstack11l1l111l1_opy_
def bstack11l1ll1ll_opy_(config):
  global bstack1llll1l1l1_opy_
  bstack111111lll_opy_ = {}
  caps = bstack111lll11_opy_
  if bstack1llll1l1l1_opy_:
    caps += bstack1lll1lll1_opy_
  for key in caps:
    if key in config:
      bstack111111lll_opy_[key] = config[key]
  return bstack111111lll_opy_
def bstack1l11ll1l1_opy_(bstack11l1l111l1_opy_, bstack111111lll_opy_):
  bstack1l1lll11_opy_ = {}
  for key in bstack11l1l111l1_opy_.keys():
    if key in bstack11111l11_opy_:
      bstack1l1lll11_opy_[bstack11111l11_opy_[key]] = bstack11l1l111l1_opy_[key]
    else:
      bstack1l1lll11_opy_[key] = bstack11l1l111l1_opy_[key]
  for key in bstack111111lll_opy_:
    if key in bstack11111l11_opy_:
      bstack1l1lll11_opy_[bstack11111l11_opy_[key]] = bstack111111lll_opy_[key]
    else:
      bstack1l1lll11_opy_[key] = bstack111111lll_opy_[key]
  return bstack1l1lll11_opy_
def bstack1l1l1l11_opy_(config, index=0):
  global bstack1llll1l1l1_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1ll11l1l11_opy_ = bstack11l1111l1_opy_(bstack1l111111l1_opy_, config, logger)
  bstack111111lll_opy_ = bstack11l1ll1ll_opy_(config)
  bstack1ll1l1l11_opy_ = bstack111lll11_opy_
  bstack1ll1l1l11_opy_ += bstack1lllllll11_opy_
  bstack111111lll_opy_ = update(bstack111111lll_opy_, bstack1ll11l1l11_opy_)
  if bstack1llll1l1l1_opy_:
    bstack1ll1l1l11_opy_ += bstack1lll1lll1_opy_
  if bstack1l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧॉ") in config:
    if bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪॊ") in config[bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩो")][index]:
      caps[bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬौ")] = config[bstack1l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶ्ࠫ")][index][bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧॎ")]
    if bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫॏ") in config[bstack1l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧॐ")][index]:
      caps[bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭॑")] = str(config[bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴ॒ࠩ")][index][bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ॓")])
    bstack11ll111l_opy_ = bstack11l1111l1_opy_(bstack1l111111l1_opy_, config[bstack1l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ॔")][index], logger)
    bstack1ll1l1l11_opy_ += list(bstack11ll111l_opy_.keys())
    for bstack1l111l11l_opy_ in bstack1ll1l1l11_opy_:
      if bstack1l111l11l_opy_ in config[bstack1l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬॕ")][index]:
        if bstack1l111l11l_opy_ == bstack1l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬॖ"):
          try:
            bstack11ll111l_opy_[bstack1l111l11l_opy_] = str(config[bstack1l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧॗ")][index][bstack1l111l11l_opy_] * 1.0)
          except:
            bstack11ll111l_opy_[bstack1l111l11l_opy_] = str(config[bstack1l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨक़")][index][bstack1l111l11l_opy_])
        else:
          bstack11ll111l_opy_[bstack1l111l11l_opy_] = config[bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩख़")][index][bstack1l111l11l_opy_]
        del (config[bstack1l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪग़")][index][bstack1l111l11l_opy_])
    bstack111111lll_opy_ = update(bstack111111lll_opy_, bstack11ll111l_opy_)
  bstack11l1l111l1_opy_ = bstack1l1lll11l_opy_(config, index)
  for bstack11l11l1lll_opy_ in bstack111lll11_opy_ + list(bstack1ll11l1l11_opy_.keys()):
    if bstack11l11l1lll_opy_ in bstack11l1l111l1_opy_:
      bstack111111lll_opy_[bstack11l11l1lll_opy_] = bstack11l1l111l1_opy_[bstack11l11l1lll_opy_]
      del (bstack11l1l111l1_opy_[bstack11l11l1lll_opy_])
  if bstack1l111l1l1_opy_(config):
    bstack11l1l111l1_opy_[bstack1l1ll_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨज़")] = True
    caps.update(bstack111111lll_opy_)
    caps[bstack1l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪड़")] = bstack11l1l111l1_opy_
  else:
    bstack11l1l111l1_opy_[bstack1l1ll_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪढ़")] = False
    caps.update(bstack1l11ll1l1_opy_(bstack11l1l111l1_opy_, bstack111111lll_opy_))
    if bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩफ़") in caps:
      caps[bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭य़")] = caps[bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫॠ")]
      del (caps[bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬॡ")])
    if bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩॢ") in caps:
      caps[bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫॣ")] = caps[bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ।")]
      del (caps[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ॥")])
  return caps
def bstack11ll1l1l1l_opy_():
  global bstack1lll11lll_opy_
  global CONFIG
  if bstack1l1l1l111l_opy_() <= version.parse(bstack1l1ll_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬ०")):
    if bstack1lll11lll_opy_ != bstack1l1ll_opy_ (u"࠭ࠧ१"):
      return bstack1l1ll_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣ२") + bstack1lll11lll_opy_ + bstack1l1ll_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧ३")
    return bstack1l111l11ll_opy_
  if bstack1lll11lll_opy_ != bstack1l1ll_opy_ (u"ࠩࠪ४"):
    return bstack1l1ll_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧ५") + bstack1lll11lll_opy_ + bstack1l1ll_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧ६")
  return bstack1lll1lll11_opy_
def bstack11l1ll1l1_opy_(options):
  return hasattr(options, bstack1l1ll_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭७"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1lll11111l_opy_(options, bstack11ll11lll_opy_):
  for bstack1ll111l11_opy_ in bstack11ll11lll_opy_:
    if bstack1ll111l11_opy_ in [bstack1l1ll_opy_ (u"࠭ࡡࡳࡩࡶࠫ८"), bstack1l1ll_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ९")]:
      continue
    if bstack1ll111l11_opy_ in options._experimental_options:
      options._experimental_options[bstack1ll111l11_opy_] = update(options._experimental_options[bstack1ll111l11_opy_],
                                                         bstack11ll11lll_opy_[bstack1ll111l11_opy_])
    else:
      options.add_experimental_option(bstack1ll111l11_opy_, bstack11ll11lll_opy_[bstack1ll111l11_opy_])
  if bstack1l1ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭॰") in bstack11ll11lll_opy_:
    for arg in bstack11ll11lll_opy_[bstack1l1ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧॱ")]:
      options.add_argument(arg)
    del (bstack11ll11lll_opy_[bstack1l1ll_opy_ (u"ࠪࡥࡷ࡭ࡳࠨॲ")])
  if bstack1l1ll_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨॳ") in bstack11ll11lll_opy_:
    for ext in bstack11ll11lll_opy_[bstack1l1ll_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩॴ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack11ll11lll_opy_[bstack1l1ll_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪॵ")])
def bstack1llll11l11_opy_(options, bstack1ll11l1ll1_opy_):
  if bstack1l1ll_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ॶ") in bstack1ll11l1ll1_opy_:
    for bstack1ll1l111_opy_ in bstack1ll11l1ll1_opy_[bstack1l1ll_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧॷ")]:
      if bstack1ll1l111_opy_ in options._preferences:
        options._preferences[bstack1ll1l111_opy_] = update(options._preferences[bstack1ll1l111_opy_], bstack1ll11l1ll1_opy_[bstack1l1ll_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨॸ")][bstack1ll1l111_opy_])
      else:
        options.set_preference(bstack1ll1l111_opy_, bstack1ll11l1ll1_opy_[bstack1l1ll_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩॹ")][bstack1ll1l111_opy_])
  if bstack1l1ll_opy_ (u"ࠫࡦࡸࡧࡴࠩॺ") in bstack1ll11l1ll1_opy_:
    for arg in bstack1ll11l1ll1_opy_[bstack1l1ll_opy_ (u"ࠬࡧࡲࡨࡵࠪॻ")]:
      options.add_argument(arg)
def bstack11l1l11l11_opy_(options, bstack111l1lll1_opy_):
  if bstack1l1ll_opy_ (u"࠭ࡷࡦࡤࡹ࡭ࡪࡽࠧॼ") in bstack111l1lll1_opy_:
    options.use_webview(bool(bstack111l1lll1_opy_[bstack1l1ll_opy_ (u"ࠧࡸࡧࡥࡺ࡮࡫ࡷࠨॽ")]))
  bstack1lll11111l_opy_(options, bstack111l1lll1_opy_)
def bstack1l1l11ll1l_opy_(options, bstack11ll1l1l_opy_):
  for bstack1ll1l11l1_opy_ in bstack11ll1l1l_opy_:
    if bstack1ll1l11l1_opy_ in [bstack1l1ll_opy_ (u"ࠨࡶࡨࡧ࡭ࡴ࡯࡭ࡱࡪࡽࡕࡸࡥࡷ࡫ࡨࡻࠬॾ"), bstack1l1ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧॿ")]:
      continue
    options.set_capability(bstack1ll1l11l1_opy_, bstack11ll1l1l_opy_[bstack1ll1l11l1_opy_])
  if bstack1l1ll_opy_ (u"ࠪࡥࡷ࡭ࡳࠨঀ") in bstack11ll1l1l_opy_:
    for arg in bstack11ll1l1l_opy_[bstack1l1ll_opy_ (u"ࠫࡦࡸࡧࡴࠩঁ")]:
      options.add_argument(arg)
  if bstack1l1ll_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩং") in bstack11ll1l1l_opy_:
    options.bstack1llll11ll1_opy_(bool(bstack11ll1l1l_opy_[bstack1l1ll_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪঃ")]))
def bstack11ll1ll11l_opy_(options, bstack1l1l1l1l_opy_):
  for bstack1lll1l1l1l_opy_ in bstack1l1l1l1l_opy_:
    if bstack1lll1l1l1l_opy_ in [bstack1l1ll_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ঄"), bstack1l1ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭অ")]:
      continue
    options._options[bstack1lll1l1l1l_opy_] = bstack1l1l1l1l_opy_[bstack1lll1l1l1l_opy_]
  if bstack1l1ll_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭আ") in bstack1l1l1l1l_opy_:
    for bstack1ll11lllll_opy_ in bstack1l1l1l1l_opy_[bstack1l1ll_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧই")]:
      options.bstack11lll11ll1_opy_(
        bstack1ll11lllll_opy_, bstack1l1l1l1l_opy_[bstack1l1ll_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨঈ")][bstack1ll11lllll_opy_])
  if bstack1l1ll_opy_ (u"ࠬࡧࡲࡨࡵࠪউ") in bstack1l1l1l1l_opy_:
    for arg in bstack1l1l1l1l_opy_[bstack1l1ll_opy_ (u"࠭ࡡࡳࡩࡶࠫঊ")]:
      options.add_argument(arg)
def bstack1l1lllll11_opy_(options, caps):
  if not hasattr(options, bstack1l1ll_opy_ (u"ࠧࡌࡇ࡜ࠫঋ")):
    return
  if options.KEY == bstack1l1ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ঌ"):
    options = bstack111111l1l_opy_.bstack1l1l11l1ll_opy_(bstack11111lll1_opy_=options, config=CONFIG)
  if options.KEY == bstack1l1ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ঍") and options.KEY in caps:
    bstack1lll11111l_opy_(options, caps[bstack1l1ll_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ঎")])
  elif options.KEY == bstack1l1ll_opy_ (u"ࠫࡲࡵࡺ࠻ࡨ࡬ࡶࡪ࡬࡯ࡹࡑࡳࡸ࡮ࡵ࡮ࡴࠩএ") and options.KEY in caps:
    bstack1llll11l11_opy_(options, caps[bstack1l1ll_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪঐ")])
  elif options.KEY == bstack1l1ll_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧ঑") and options.KEY in caps:
    bstack1l1l11ll1l_opy_(options, caps[bstack1l1ll_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨ঒")])
  elif options.KEY == bstack1l1ll_opy_ (u"ࠨ࡯ࡶ࠾ࡪࡪࡧࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩও") and options.KEY in caps:
    bstack11l1l11l11_opy_(options, caps[bstack1l1ll_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪঔ")])
  elif options.KEY == bstack1l1ll_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩক") and options.KEY in caps:
    bstack11ll1ll11l_opy_(options, caps[bstack1l1ll_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪখ")])
def bstack1ll1lll111_opy_(caps):
  global bstack1llll1l1l1_opy_
  if isinstance(os.environ.get(bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭গ")), str):
    bstack1llll1l1l1_opy_ = eval(os.getenv(bstack1l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧঘ")))
  if bstack1llll1l1l1_opy_:
    if bstack1lllllll1l_opy_() < version.parse(bstack1l1ll_opy_ (u"ࠧ࠳࠰࠶࠲࠵࠭ঙ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1l1ll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨচ")
    if bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧছ") in caps:
      browser = caps[bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨজ")]
    elif bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬঝ") in caps:
      browser = caps[bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ঞ")]
    browser = str(browser).lower()
    if browser == bstack1l1ll_opy_ (u"࠭ࡩࡱࡪࡲࡲࡪ࠭ট") or browser == bstack1l1ll_opy_ (u"ࠧࡪࡲࡤࡨࠬঠ"):
      browser = bstack1l1ll_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨড")
    if browser == bstack1l1ll_opy_ (u"ࠩࡶࡥࡲࡹࡵ࡯ࡩࠪঢ"):
      browser = bstack1l1ll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪণ")
    if browser not in [bstack1l1ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫত"), bstack1l1ll_opy_ (u"ࠬ࡫ࡤࡨࡧࠪথ"), bstack1l1ll_opy_ (u"࠭ࡩࡦࠩদ"), bstack1l1ll_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࠧধ"), bstack1l1ll_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩন")]:
      return None
    try:
      package = bstack1l1ll_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࠲ࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸ࠮ࡼࡿ࠱ࡳࡵࡺࡩࡰࡰࡶࠫ঩").format(browser)
      name = bstack1l1ll_opy_ (u"ࠪࡓࡵࡺࡩࡰࡰࡶࠫপ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack11l1ll1l1_opy_(options):
        return None
      for bstack11l11l1lll_opy_ in caps.keys():
        options.set_capability(bstack11l11l1lll_opy_, caps[bstack11l11l1lll_opy_])
      bstack1l1lllll11_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1l11lll1l1_opy_(options, bstack1l1lll1l11_opy_):
  if not bstack11l1ll1l1_opy_(options):
    return
  for bstack11l11l1lll_opy_ in bstack1l1lll1l11_opy_.keys():
    if bstack11l11l1lll_opy_ in bstack1lllllll11_opy_:
      continue
    if bstack11l11l1lll_opy_ in options._caps and type(options._caps[bstack11l11l1lll_opy_]) in [dict, list]:
      options._caps[bstack11l11l1lll_opy_] = update(options._caps[bstack11l11l1lll_opy_], bstack1l1lll1l11_opy_[bstack11l11l1lll_opy_])
    else:
      options.set_capability(bstack11l11l1lll_opy_, bstack1l1lll1l11_opy_[bstack11l11l1lll_opy_])
  bstack1l1lllll11_opy_(options, bstack1l1lll1l11_opy_)
  if bstack1l1ll_opy_ (u"ࠫࡲࡵࡺ࠻ࡦࡨࡦࡺ࡭ࡧࡦࡴࡄࡨࡩࡸࡥࡴࡵࠪফ") in options._caps:
    if options._caps[bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪব")] and options._caps[bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫভ")].lower() != bstack1l1ll_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨম"):
      del options._caps[bstack1l1ll_opy_ (u"ࠨ࡯ࡲࡾ࠿ࡪࡥࡣࡷࡪ࡫ࡪࡸࡁࡥࡦࡵࡩࡸࡹࠧয")]
def bstack1l1ll11l1_opy_(proxy_config):
  if bstack1l1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭র") in proxy_config:
    proxy_config[bstack1l1ll_opy_ (u"ࠪࡷࡸࡲࡐࡳࡱࡻࡽࠬ঱")] = proxy_config[bstack1l1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨল")]
    del (proxy_config[bstack1l1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ঳")])
  if bstack1l1ll_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩ঴") in proxy_config and proxy_config[bstack1l1ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪ঵")].lower() != bstack1l1ll_opy_ (u"ࠨࡦ࡬ࡶࡪࡩࡴࠨশ"):
    proxy_config[bstack1l1ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬষ")] = bstack1l1ll_opy_ (u"ࠪࡱࡦࡴࡵࡢ࡮ࠪস")
  if bstack1l1ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡄࡹࡹࡵࡣࡰࡰࡩ࡭࡬࡛ࡲ࡭ࠩহ") in proxy_config:
    proxy_config[bstack1l1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ঺")] = bstack1l1ll_opy_ (u"࠭ࡰࡢࡥࠪ঻")
  return proxy_config
def bstack11l1l11l_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1l1ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ়࠭") in config:
    return proxy
  config[bstack1l1ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧঽ")] = bstack1l1ll11l1_opy_(config[bstack1l1ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨা")])
  if proxy == None:
    proxy = Proxy(config[bstack1l1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩি")])
  return proxy
def bstack111ll11l1_opy_(self):
  global CONFIG
  global bstack1ll111ll1_opy_
  try:
    proxy = bstack11llll1l11_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1l1ll_opy_ (u"ࠫ࠳ࡶࡡࡤࠩী")):
        proxies = bstack11l1111l11_opy_(proxy, bstack11ll1l1l1l_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1ll1l111_opy_ = proxies.popitem()
          if bstack1l1ll_opy_ (u"ࠧࡀ࠯࠰ࠤু") in bstack1l1ll1l111_opy_:
            return bstack1l1ll1l111_opy_
          else:
            return bstack1l1ll_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢূ") + bstack1l1ll1l111_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1l1ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡴࡷࡵࡸࡺࠢࡸࡶࡱࠦ࠺ࠡࡽࢀࠦৃ").format(str(e)))
  return bstack1ll111ll1_opy_(self)
def bstack111l1l1ll_opy_():
  global CONFIG
  return bstack1ll1111l1_opy_(CONFIG) and bstack11111111_opy_() and bstack1l1l1l111l_opy_() >= version.parse(bstack1llllll1ll_opy_)
def bstack1l1ll1l1l1_opy_():
  global CONFIG
  return (bstack1l1ll_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫৄ") in CONFIG or bstack1l1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭৅") in CONFIG) and bstack11ll1l1l1_opy_()
def bstack1111llll1_opy_(config):
  bstack11111111l_opy_ = {}
  if bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ৆") in config:
    bstack11111111l_opy_ = config[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨে")]
  if bstack1l1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫৈ") in config:
    bstack11111111l_opy_ = config[bstack1l1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ৉")]
  proxy = bstack11llll1l11_opy_(config)
  if proxy:
    if proxy.endswith(bstack1l1ll_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ৊")) and os.path.isfile(proxy):
      bstack11111111l_opy_[bstack1l1ll_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫো")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1l1ll_opy_ (u"ࠩ࠱ࡴࡦࡩࠧৌ")):
        proxies = bstack11ll1llll_opy_(config, bstack11ll1l1l1l_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1ll1l111_opy_ = proxies.popitem()
          if bstack1l1ll_opy_ (u"ࠥ࠾࠴࠵্ࠢ") in bstack1l1ll1l111_opy_:
            parsed_url = urlparse(bstack1l1ll1l111_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1l1ll_opy_ (u"ࠦ࠿࠵࠯ࠣৎ") + bstack1l1ll1l111_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack11111111l_opy_[bstack1l1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࡌࡴࡹࡴࠨ৏")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack11111111l_opy_[bstack1l1ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡵࡲࡵࠩ৐")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack11111111l_opy_[bstack1l1ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴࠪ৑")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack11111111l_opy_[bstack1l1ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡢࡵࡶࠫ৒")] = str(parsed_url.password)
  return bstack11111111l_opy_
def bstack111lllllll_opy_(config):
  if bstack1l1ll_opy_ (u"ࠩࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠧ৓") in config:
    return config[bstack1l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨ৔")]
  return {}
def bstack1l1l11lll1_opy_(caps):
  global bstack111ll1l1_opy_
  if bstack1l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ৕") in caps:
    caps[bstack1l1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭৖")][bstack1l1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬৗ")] = True
    if bstack111ll1l1_opy_:
      caps[bstack1l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ৘")][bstack1l1ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ৙")] = bstack111ll1l1_opy_
  else:
    caps[bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࠧ৚")] = True
    if bstack111ll1l1_opy_:
      caps[bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ৛")] = bstack111ll1l1_opy_
@measure(event_name=EVENTS.bstack111l11l1l_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1l1l1l1l1l_opy_():
  global CONFIG
  if not bstack1ll1ll111l_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨড়") in CONFIG and bstack1ll1l11l_opy_(CONFIG[bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩঢ়")]):
    if (
      bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ৞") in CONFIG
      and bstack1ll1l11l_opy_(CONFIG[bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫয়")].get(bstack1l1ll_opy_ (u"ࠨࡵ࡮࡭ࡵࡈࡩ࡯ࡣࡵࡽࡎࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡡࡵ࡫ࡲࡲࠬৠ")))
    ):
      logger.debug(bstack1l1ll_opy_ (u"ࠤࡏࡳࡨࡧ࡬ࠡࡤ࡬ࡲࡦࡸࡹࠡࡰࡲࡸࠥࡹࡴࡢࡴࡷࡩࡩࠦࡡࡴࠢࡶ࡯࡮ࡶࡂࡪࡰࡤࡶࡾࡏ࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡢࡶ࡬ࡳࡳࠦࡩࡴࠢࡨࡲࡦࡨ࡬ࡦࡦࠥৡ"))
      return
    bstack11111111l_opy_ = bstack1111llll1_opy_(CONFIG)
    bstack1l1111111l_opy_(CONFIG[bstack1l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ৢ")], bstack11111111l_opy_)
def bstack1l1111111l_opy_(key, bstack11111111l_opy_):
  global bstack1ll1ll1l1l_opy_
  logger.info(bstack1llllll1l_opy_)
  try:
    bstack1ll1ll1l1l_opy_ = Local()
    bstack1l11lll1_opy_ = {bstack1l1ll_opy_ (u"ࠫࡰ࡫ࡹࠨৣ"): key}
    bstack1l11lll1_opy_.update(bstack11111111l_opy_)
    logger.debug(bstack1l1ll1l11_opy_.format(str(bstack1l11lll1_opy_)).replace(key, bstack1l1ll_opy_ (u"ࠬࡡࡒࡆࡆࡄࡇ࡙ࡋࡄ࡞ࠩ৤")))
    bstack1ll1ll1l1l_opy_.start(**bstack1l11lll1_opy_)
    if bstack1ll1ll1l1l_opy_.isRunning():
      logger.info(bstack1l111ll1l1_opy_)
  except Exception as e:
    bstack111111l11_opy_(bstack1111ll1l1_opy_.format(str(e)))
def bstack11l1l1lll_opy_():
  global bstack1ll1ll1l1l_opy_
  if bstack1ll1ll1l1l_opy_.isRunning():
    logger.info(bstack1ll1l11l1l_opy_)
    bstack1ll1ll1l1l_opy_.stop()
  bstack1ll1ll1l1l_opy_ = None
def bstack1ll111llll_opy_(bstack1ll11llll1_opy_=[]):
  global CONFIG
  bstack11l1lll11_opy_ = []
  bstack11lll11l1_opy_ = [bstack1l1ll_opy_ (u"࠭࡯ࡴࠩ৥"), bstack1l1ll_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪ০"), bstack1l1ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬ১"), bstack1l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ২"), bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ৩"), bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ৪")]
  try:
    for err in bstack1ll11llll1_opy_:
      bstack1lll1111ll_opy_ = {}
      for k in bstack11lll11l1_opy_:
        val = CONFIG[bstack1l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ৫")][int(err[bstack1l1ll_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ৬")])].get(k)
        if val:
          bstack1lll1111ll_opy_[k] = val
      if(err[bstack1l1ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭৭")] != bstack1l1ll_opy_ (u"ࠨࠩ৮")):
        bstack1lll1111ll_opy_[bstack1l1ll_opy_ (u"ࠩࡷࡩࡸࡺࡳࠨ৯")] = {
          err[bstack1l1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨৰ")]: err[bstack1l1ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪৱ")]
        }
        bstack11l1lll11_opy_.append(bstack1lll1111ll_opy_)
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧࡱࡵࡱࡦࡺࡴࡪࡰࡪࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡥࡷࡧࡱࡸ࠿ࠦࠧ৲") + str(e))
  finally:
    return bstack11l1lll11_opy_
def bstack111llllll_opy_(file_name):
  bstack1l1l11ll1_opy_ = []
  try:
    bstack1l11ll11l1_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1l11ll11l1_opy_):
      with open(bstack1l11ll11l1_opy_) as f:
        bstack1l11ll1l1l_opy_ = json.load(f)
        bstack1l1l11ll1_opy_ = bstack1l11ll1l1l_opy_
      os.remove(bstack1l11ll11l1_opy_)
    return bstack1l1l11ll1_opy_
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨ࡬ࡲࡩ࡯࡮ࡨࠢࡨࡶࡷࡵࡲࠡ࡮࡬ࡷࡹࡀࠠࠨ৳") + str(e))
    return bstack1l1l11ll1_opy_
def bstack1ll1l1l1_opy_():
  try:
      from bstack_utils.constants import bstack1111l111l_opy_, EVENTS
      from bstack_utils.helper import bstack1ll1l1l1l1_opy_, get_host_info, bstack11l1lll1_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack11lllll1_opy_ = os.path.join(os.getcwd(), bstack1l1ll_opy_ (u"ࠧ࡭ࡱࡪࠫ৴"), bstack1l1ll_opy_ (u"ࠨ࡭ࡨࡽ࠲ࡳࡥࡵࡴ࡬ࡧࡸ࠴ࡪࡴࡱࡱࠫ৵"))
      lock = FileLock(bstack11lllll1_opy_+bstack1l1ll_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣ৶"))
      def bstack1ll111l1l1_opy_():
          try:
              with lock:
                  with open(bstack11lllll1_opy_, bstack1l1ll_opy_ (u"ࠥࡶࠧ৷"), encoding=bstack1l1ll_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥ৸")) as file:
                      data = json.load(file)
                      config = {
                          bstack1l1ll_opy_ (u"ࠧ࡮ࡥࡢࡦࡨࡶࡸࠨ৹"): {
                              bstack1l1ll_opy_ (u"ࠨࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠧ৺"): bstack1l1ll_opy_ (u"ࠢࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠥ৻"),
                          }
                      }
                      bstack1llll1111l_opy_ = datetime.utcnow()
                      bstack1lllll1l11_opy_ = bstack1llll1111l_opy_.strftime(bstack1l1ll_opy_ (u"ࠣࠧ࡜࠱ࠪࡳ࠭ࠦࡦࡗࠩࡍࡀࠥࡎ࠼ࠨࡗ࠳ࠫࡦࠡࡗࡗࡇࠧৼ"))
                      bstack111ll11l_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ৽")) if os.environ.get(bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ৾")) else bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠦࡸࡪ࡫ࡓࡷࡱࡍࡩࠨ৿"))
                      payload = {
                          bstack1l1ll_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠤ਀"): bstack1l1ll_opy_ (u"ࠨࡳࡥ࡭ࡢࡩࡻ࡫࡮ࡵࡵࠥਁ"),
                          bstack1l1ll_opy_ (u"ࠢࡥࡣࡷࡥࠧਂ"): {
                              bstack1l1ll_opy_ (u"ࠣࡶࡨࡷࡹ࡮ࡵࡣࡡࡸࡹ࡮ࡪࠢਃ"): bstack111ll11l_opy_,
                              bstack1l1ll_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡦࡢࡨࡦࡿࠢ਄"): bstack1lllll1l11_opy_,
                              bstack1l1ll_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡱࡥࡲ࡫ࠢਅ"): bstack1l1ll_opy_ (u"ࠦࡘࡊࡋࡇࡧࡤࡸࡺࡸࡥࡑࡧࡵࡪࡴࡸ࡭ࡢࡰࡦࡩࠧਆ"),
                              bstack1l1ll_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣ࡯ࡹ࡯࡯ࠤਇ"): {
                                  bstack1l1ll_opy_ (u"ࠨ࡭ࡦࡣࡶࡹࡷ࡫ࡳࠣਈ"): data,
                                  bstack1l1ll_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤਉ"): bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠣࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠥਊ"))
                              },
                              bstack1l1ll_opy_ (u"ࠤࡸࡷࡪࡸ࡟ࡥࡣࡷࡥࠧ਋"): bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠥࡹࡸ࡫ࡲࡏࡣࡰࡩࠧ਌")),
                              bstack1l1ll_opy_ (u"ࠦ࡭ࡵࡳࡵࡡ࡬ࡲ࡫ࡵࠢ਍"): get_host_info()
                          }
                      }
                      bstack1l1lll1l1l_opy_ = bstack1lll1ll1ll_opy_(cli.config, [bstack1l1ll_opy_ (u"ࠧࡧࡰࡪࡵࠥ਎"), bstack1l1ll_opy_ (u"ࠨࡥࡥࡵࡌࡲࡸࡺࡲࡶ࡯ࡨࡲࡹࡧࡴࡪࡱࡱࠦਏ"), bstack1l1ll_opy_ (u"ࠢࡢࡲ࡬ࠦਐ")], bstack1111l111l_opy_)
                      response = bstack1ll1l1l1l1_opy_(bstack1l1ll_opy_ (u"ࠣࡒࡒࡗ࡙ࠨ਑"), bstack1l1lll1l1l_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack1l1ll_opy_ (u"ࠤࡇࡥࡹࡧࠠࡴࡧࡱࡸࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼࠤࡹࡵࠠࡼࡿࠣࡻ࡮ࡺࡨࠡࡦࡤࡸࡦࠦࡻࡾࠤ਒").format(bstack1111l111l_opy_, payload))
                      else:
                          logger.debug(bstack1l1ll_opy_ (u"ࠥࡖࡪࡷࡵࡦࡵࡷࠤ࡫ࡧࡩ࡭ࡧࡧࠤ࡫ࡵࡲࠡࡽࢀࠤࡼ࡯ࡴࡩࠢࡧࡥࡹࡧࠠࡼࡿࠥਓ").format(bstack1111l111l_opy_, payload))
          except Exception as e:
              logger.debug(bstack1l1ll_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡱࡨࠥࡱࡥࡺࠢࡰࡩࡹࡸࡩࡤࡵࠣࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶࠥࢁࡽࠣਔ").format(e))
      bstack1ll111l1l1_opy_()
      bstack1l11111111_opy_(bstack11lllll1_opy_, logger)
  except:
    pass
def bstack11lllll1l1_opy_():
  global bstack1l1lll1ll_opy_
  global bstack1lllllll1_opy_
  global bstack11lll11111_opy_
  global bstack111llll1l_opy_
  global bstack1l11l1l11_opy_
  global bstack111111ll_opy_
  global CONFIG
  bstack1l11lll11l_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠬࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࡠࡗࡖࡉࡉ࠭ਕ"))
  if bstack1l11lll11l_opy_ in [bstack1l1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬਖ"), bstack1l1ll_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ਗ")]:
    bstack1l1111l1l1_opy_()
  percy.shutdown()
  if bstack1l1lll1ll_opy_:
    logger.warning(bstack1lllll11l1_opy_.format(str(bstack1l1lll1ll_opy_)))
  else:
    try:
      bstack111l11lll_opy_ = bstack11l1111ll1_opy_(bstack1l1ll_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧਘ"), logger)
      if bstack111l11lll_opy_.get(bstack1l1ll_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧਙ")) and bstack111l11lll_opy_.get(bstack1l1ll_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨਚ")).get(bstack1l1ll_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭ਛ")):
        logger.warning(bstack1lllll11l1_opy_.format(str(bstack111l11lll_opy_[bstack1l1ll_opy_ (u"ࠬࡴࡵࡥࡩࡨࡣࡱࡵࡣࡢ࡮ࠪਜ")][bstack1l1ll_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨਝ")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack11ll1lll1l_opy_.invoke(bstack111l1lll_opy_.bstack11l1l1ll1_opy_)
  logger.info(bstack1lll1l11l_opy_)
  global bstack1ll1ll1l1l_opy_
  if bstack1ll1ll1l1l_opy_:
    bstack11l1l1lll_opy_()
  try:
    with bstack1lllll11l_opy_:
      bstack1l11l1lll_opy_ = bstack1lllllll1_opy_.copy()
    for driver in bstack1l11l1lll_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1ll111ll_opy_)
  if bstack111111ll_opy_ == bstack1l1ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ਞ"):
    bstack1l11l1l11_opy_ = bstack111llllll_opy_(bstack1l1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩਟ"))
  if bstack111111ll_opy_ == bstack1l1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩਠ") and len(bstack111llll1l_opy_) == 0:
    bstack111llll1l_opy_ = bstack111llllll_opy_(bstack1l1ll_opy_ (u"ࠪࡴࡼࡥࡰࡺࡶࡨࡷࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨਡ"))
    if len(bstack111llll1l_opy_) == 0:
      bstack111llll1l_opy_ = bstack111llllll_opy_(bstack1l1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡵࡶࡰࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪਢ"))
  bstack1l1lll1lll_opy_ = bstack1l1ll_opy_ (u"ࠬ࠭ਣ")
  if len(bstack11lll11111_opy_) > 0:
    bstack1l1lll1lll_opy_ = bstack1ll111llll_opy_(bstack11lll11111_opy_)
  elif len(bstack111llll1l_opy_) > 0:
    bstack1l1lll1lll_opy_ = bstack1ll111llll_opy_(bstack111llll1l_opy_)
  elif len(bstack1l11l1l11_opy_) > 0:
    bstack1l1lll1lll_opy_ = bstack1ll111llll_opy_(bstack1l11l1l11_opy_)
  elif len(bstack1ll1l11lll_opy_) > 0:
    bstack1l1lll1lll_opy_ = bstack1ll111llll_opy_(bstack1ll1l11lll_opy_)
  if bool(bstack1l1lll1lll_opy_):
    bstack1l11llll1l_opy_(bstack1l1lll1lll_opy_)
  else:
    bstack1l11llll1l_opy_()
  bstack1l11111111_opy_(bstack11ll11l1l_opy_, logger)
  if bstack1l11lll11l_opy_ not in [bstack1l1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧਤ")]:
    bstack1ll1l1l1_opy_()
  bstack1l1111111_opy_.bstack11l1l1lll1_opy_(CONFIG)
  if len(bstack1l11l1l11_opy_) > 0:
    sys.exit(len(bstack1l11l1l11_opy_))
def bstack1l1l11l1l1_opy_(bstack11111ll1l_opy_, frame):
  global bstack11l1lll1_opy_
  logger.error(bstack11ll111111_opy_)
  bstack11l1lll1_opy_.bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡏࡱࠪਥ"), bstack11111ll1l_opy_)
  if hasattr(signal, bstack1l1ll_opy_ (u"ࠨࡕ࡬࡫ࡳࡧ࡬ࡴࠩਦ")):
    bstack11l1lll1_opy_.bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩਧ"), signal.Signals(bstack11111ll1l_opy_).name)
  else:
    bstack11l1lll1_opy_.bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪਨ"), bstack1l1ll_opy_ (u"ࠫࡘࡏࡇࡖࡐࡎࡒࡔ࡝ࡎࠨ਩"))
  if cli.is_running():
    bstack11ll1lll1l_opy_.invoke(bstack111l1lll_opy_.bstack11l1l1ll1_opy_)
  bstack1l11lll11l_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠬࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࡠࡗࡖࡉࡉ࠭ਪ"))
  if bstack1l11lll11l_opy_ == bstack1l1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ਫ") and not cli.is_enabled(CONFIG):
    bstack11ll1ll1_opy_.stop(bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧਬ")))
  bstack11lllll1l1_opy_()
  sys.exit(1)
def bstack111111l11_opy_(err):
  logger.critical(bstack1l111l1ll_opy_.format(str(err)))
  bstack1l11llll1l_opy_(bstack1l111l1ll_opy_.format(str(err)), True)
  atexit.unregister(bstack11lllll1l1_opy_)
  bstack1l1111l1l1_opy_()
  sys.exit(1)
def bstack1111l1l11_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l11llll1l_opy_(message, True)
  atexit.unregister(bstack11lllll1l1_opy_)
  bstack1l1111l1l1_opy_()
  sys.exit(1)
def bstack11l11lllll_opy_():
  global CONFIG
  global bstack1l1l1l1l1_opy_
  global bstack111ll1l11_opy_
  global bstack1ll1l111ll_opy_
  CONFIG = bstack1llll111_opy_()
  load_dotenv(CONFIG.get(bstack1l1ll_opy_ (u"ࠨࡧࡱࡺࡋ࡯࡬ࡦࠩਭ")))
  bstack1ll11l111_opy_()
  bstack11l11111l1_opy_()
  CONFIG = bstack11ll111l1_opy_(CONFIG)
  update(CONFIG, bstack111ll1l11_opy_)
  update(CONFIG, bstack1l1l1l1l1_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack1l1lll1ll1_opy_(CONFIG)
  bstack1ll1l111ll_opy_ = bstack1ll1ll111l_opy_(CONFIG)
  os.environ[bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬਮ")] = bstack1ll1l111ll_opy_.__str__().lower()
  bstack11l1lll1_opy_.bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫਯ"), bstack1ll1l111ll_opy_)
  if (bstack1l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧਰ") in CONFIG and bstack1l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ਱") in bstack1l1l1l1l1_opy_) or (
          bstack1l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩਲ") in CONFIG and bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪਲ਼") not in bstack111ll1l11_opy_):
    if os.getenv(bstack1l1ll_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬ਴")):
      CONFIG[bstack1l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫਵ")] = os.getenv(bstack1l1ll_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧਸ਼"))
    else:
      if not CONFIG.get(bstack1l1ll_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠢ਷"), bstack1l1ll_opy_ (u"ࠧࠨਸ")) in bstack1ll1ll11_opy_:
        bstack11l11lll1_opy_()
  elif (bstack1l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩਹ") not in CONFIG and bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ਺") in CONFIG) or (
          bstack1l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ਻") in bstack111ll1l11_opy_ and bstack1l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩ਼ࠬ") not in bstack1l1l1l1l1_opy_):
    del (CONFIG[bstack1l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ਽")])
  if bstack1lllll111l_opy_(CONFIG):
    bstack111111l11_opy_(bstack1111lll11_opy_)
  Config.bstack11ll11ll1_opy_().bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠦࡺࡹࡥࡳࡐࡤࡱࡪࠨਾ"), CONFIG[bstack1l1ll_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧਿ")])
  bstack1l1ll11111_opy_()
  bstack1ll11ll111_opy_()
  if bstack1llll1l1l1_opy_ and not CONFIG.get(bstack1l1ll_opy_ (u"ࠨࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠤੀ"), bstack1l1ll_opy_ (u"ࠢࠣੁ")) in bstack1ll1ll11_opy_:
    CONFIG[bstack1l1ll_opy_ (u"ࠨࡣࡳࡴࠬੂ")] = bstack111lll111_opy_(CONFIG)
    logger.info(bstack11l1lll1l_opy_.format(CONFIG[bstack1l1ll_opy_ (u"ࠩࡤࡴࡵ࠭੃")]))
  if not bstack1ll1l111ll_opy_:
    CONFIG[bstack1l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭੄")] = [{}]
def bstack1l1llll1_opy_(config, bstack1l1l1l1ll_opy_):
  global CONFIG
  global bstack1llll1l1l1_opy_
  CONFIG = config
  bstack1llll1l1l1_opy_ = bstack1l1l1l1ll_opy_
def bstack1ll11ll111_opy_():
  global CONFIG
  global bstack1llll1l1l1_opy_
  if bstack1l1ll_opy_ (u"ࠫࡦࡶࡰࠨ੅") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1111l1l11_opy_(e, bstack1l1111l1_opy_)
    bstack1llll1l1l1_opy_ = True
    bstack11l1lll1_opy_.bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ੆"), True)
def bstack111lll111_opy_(config):
  bstack1ll111lll_opy_ = bstack1l1ll_opy_ (u"࠭ࠧੇ")
  app = config[bstack1l1ll_opy_ (u"ࠧࡢࡲࡳࠫੈ")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack11lll1ll1l_opy_:
      if os.path.exists(app):
        bstack1ll111lll_opy_ = bstack1ll11l11l_opy_(config, app)
      elif bstack11llll1l_opy_(app):
        bstack1ll111lll_opy_ = app
      else:
        bstack111111l11_opy_(bstack111111ll1_opy_.format(app))
    else:
      if bstack11llll1l_opy_(app):
        bstack1ll111lll_opy_ = app
      elif os.path.exists(app):
        bstack1ll111lll_opy_ = bstack1ll11l11l_opy_(app)
      else:
        bstack111111l11_opy_(bstack1l11l111l1_opy_)
  else:
    if len(app) > 2:
      bstack111111l11_opy_(bstack1l1l1ll1l1_opy_)
    elif len(app) == 2:
      if bstack1l1ll_opy_ (u"ࠨࡲࡤࡸ࡭࠭੉") in app and bstack1l1ll_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬ੊") in app:
        if os.path.exists(app[bstack1l1ll_opy_ (u"ࠪࡴࡦࡺࡨࠨੋ")]):
          bstack1ll111lll_opy_ = bstack1ll11l11l_opy_(config, app[bstack1l1ll_opy_ (u"ࠫࡵࡧࡴࡩࠩੌ")], app[bstack1l1ll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨ੍")])
        else:
          bstack111111l11_opy_(bstack111111ll1_opy_.format(app))
      else:
        bstack111111l11_opy_(bstack1l1l1ll1l1_opy_)
    else:
      for key in app:
        if key in bstack11llll1lll_opy_:
          if key == bstack1l1ll_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ੎"):
            if os.path.exists(app[key]):
              bstack1ll111lll_opy_ = bstack1ll11l11l_opy_(config, app[key])
            else:
              bstack111111l11_opy_(bstack111111ll1_opy_.format(app))
          else:
            bstack1ll111lll_opy_ = app[key]
        else:
          bstack111111l11_opy_(bstack11l11111ll_opy_)
  return bstack1ll111lll_opy_
def bstack11llll1l_opy_(bstack1ll111lll_opy_):
  import re
  bstack111l111ll_opy_ = re.compile(bstack1l1ll_opy_ (u"ࡲࠣࡠ࡞ࡥ࠲ࢀࡁ࠮࡜࠳࠱࠾ࡢ࡟࠯࡞࠰ࡡ࠯ࠪࠢ੏"))
  bstack1ll1l11111_opy_ = re.compile(bstack1l1ll_opy_ (u"ࡳࠤࡡ࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰࠯࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧ੐"))
  if bstack1l1ll_opy_ (u"ࠩࡥࡷ࠿࠵࠯ࠨੑ") in bstack1ll111lll_opy_ or re.fullmatch(bstack111l111ll_opy_, bstack1ll111lll_opy_) or re.fullmatch(bstack1ll1l11111_opy_, bstack1ll111lll_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack11lllll11l_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1ll11l11l_opy_(config, path, bstack11ll11111_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1l1ll_opy_ (u"ࠪࡶࡧ࠭੒")).read()).hexdigest()
  bstack1l11l11111_opy_ = bstack11l1llll1_opy_(md5_hash)
  bstack1ll111lll_opy_ = None
  if bstack1l11l11111_opy_:
    logger.info(bstack1llll1l11_opy_.format(bstack1l11l11111_opy_, md5_hash))
    return bstack1l11l11111_opy_
  bstack11l1l1111_opy_ = datetime.datetime.now()
  bstack11l11l1ll1_opy_ = MultipartEncoder(
    fields={
      bstack1l1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࠩ੓"): (os.path.basename(path), open(os.path.abspath(path), bstack1l1ll_opy_ (u"ࠬࡸࡢࠨ੔")), bstack1l1ll_opy_ (u"࠭ࡴࡦࡺࡷ࠳ࡵࡲࡡࡪࡰࠪ੕")),
      bstack1l1ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪ੖"): bstack11ll11111_opy_
    }
  )
  response = requests.post(bstack11l1l11111_opy_, data=bstack11l11l1ll1_opy_,
                           headers={bstack1l1ll_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧ੗"): bstack11l11l1ll1_opy_.content_type},
                           auth=(config[bstack1l1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ੘")], config[bstack1l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ਖ਼")]))
  try:
    res = json.loads(response.text)
    bstack1ll111lll_opy_ = res[bstack1l1ll_opy_ (u"ࠫࡦࡶࡰࡠࡷࡵࡰࠬਗ਼")]
    logger.info(bstack111lllll11_opy_.format(bstack1ll111lll_opy_))
    bstack1llll11111_opy_(md5_hash, bstack1ll111lll_opy_)
    cli.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽ࡹࡵࡲ࡯ࡢࡦࡢࡥࡵࡶࠢਜ਼"), datetime.datetime.now() - bstack11l1l1111_opy_)
  except ValueError as err:
    bstack111111l11_opy_(bstack1l1l1l11l_opy_.format(str(err)))
  return bstack1ll111lll_opy_
def bstack1l1ll11111_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1l1l1111ll_opy_
  bstack1lll1ll1_opy_ = 1
  bstack1l1ll11ll_opy_ = 1
  if bstack1l1ll_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ੜ") in CONFIG:
    bstack1l1ll11ll_opy_ = CONFIG[bstack1l1ll_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ੝")]
  else:
    bstack1l1ll11ll_opy_ = bstack1lllll1ll1_opy_(framework_name, args) or 1
  if bstack1l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫਫ਼") in CONFIG:
    bstack1lll1ll1_opy_ = len(CONFIG[bstack1l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ੟")])
  bstack1l1l1111ll_opy_ = int(bstack1l1ll11ll_opy_) * int(bstack1lll1ll1_opy_)
def bstack1lllll1ll1_opy_(framework_name, args):
  if framework_name == bstack11l111l11l_opy_ and args and bstack1l1ll_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨ੠") in args:
      bstack1lll1l1lll_opy_ = args.index(bstack1l1ll_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ੡"))
      return int(args[bstack1lll1l1lll_opy_ + 1]) or 1
  return 1
def bstack11l1llll1_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨ੢"))
    bstack1lll1l111l_opy_ = os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"࠭ࡾࠨ੣")), bstack1l1ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ੤"), bstack1l1ll_opy_ (u"ࠨࡣࡳࡴ࡚ࡶ࡬ࡰࡣࡧࡑࡉ࠻ࡈࡢࡵ࡫࠲࡯ࡹ࡯࡯ࠩ੥"))
    if os.path.exists(bstack1lll1l111l_opy_):
      try:
        bstack1l1ll1111l_opy_ = json.load(open(bstack1lll1l111l_opy_, bstack1l1ll_opy_ (u"ࠩࡵࡦࠬ੦")))
        if md5_hash in bstack1l1ll1111l_opy_:
          bstack1l1lll1l1_opy_ = bstack1l1ll1111l_opy_[md5_hash]
          bstack111ll1lll_opy_ = datetime.datetime.now()
          bstack111l11111_opy_ = datetime.datetime.strptime(bstack1l1lll1l1_opy_[bstack1l1ll_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭੧")], bstack1l1ll_opy_ (u"ࠫࠪࡪ࠯ࠦ࡯࠲ࠩ࡞ࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓࠨ੨"))
          if (bstack111ll1lll_opy_ - bstack111l11111_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack1l1lll1l1_opy_[bstack1l1ll_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ੩")]):
            return None
          return bstack1l1lll1l1_opy_[bstack1l1ll_opy_ (u"࠭ࡩࡥࠩ੪")]
      except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡎࡆ࠸ࠤ࡭ࡧࡳࡩࠢࡩ࡭ࡱ࡫࠺ࠡࡽࢀࠫ੫").format(str(e)))
    return None
  bstack1lll1l111l_opy_ = os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠨࢀࠪ੬")), bstack1l1ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ੭"), bstack1l1ll_opy_ (u"ࠪࡥࡵࡶࡕࡱ࡮ࡲࡥࡩࡓࡄ࠶ࡊࡤࡷ࡭࠴ࡪࡴࡱࡱࠫ੮"))
  lock_file = bstack1lll1l111l_opy_ + bstack1l1ll_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪ੯")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1lll1l111l_opy_):
        with open(bstack1lll1l111l_opy_, bstack1l1ll_opy_ (u"ࠬࡸࠧੰ")) as f:
          content = f.read().strip()
          if content:
            bstack1l1ll1111l_opy_ = json.loads(content)
            if md5_hash in bstack1l1ll1111l_opy_:
              bstack1l1lll1l1_opy_ = bstack1l1ll1111l_opy_[md5_hash]
              bstack111ll1lll_opy_ = datetime.datetime.now()
              bstack111l11111_opy_ = datetime.datetime.strptime(bstack1l1lll1l1_opy_[bstack1l1ll_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩੱ")], bstack1l1ll_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫੲ"))
              if (bstack111ll1lll_opy_ - bstack111l11111_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack1l1lll1l1_opy_[bstack1l1ll_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ੳ")]):
                return None
              return bstack1l1lll1l1_opy_[bstack1l1ll_opy_ (u"ࠩ࡬ࡨࠬੴ")]
      return None
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡺ࡭ࡹ࡮ࠠࡧ࡫࡯ࡩࠥࡲ࡯ࡤ࡭࡬ࡲ࡬ࠦࡦࡰࡴࠣࡑࡉ࠻ࠠࡩࡣࡶ࡬࠿ࠦࡻࡾࠩੵ").format(str(e)))
    return None
def bstack1llll11111_opy_(md5_hash, bstack1ll111lll_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1ll_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧ੶"))
    bstack1l1ll1lll1_opy_ = os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠬࢄࠧ੷")), bstack1l1ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭੸"))
    if not os.path.exists(bstack1l1ll1lll1_opy_):
      os.makedirs(bstack1l1ll1lll1_opy_)
    bstack1lll1l111l_opy_ = os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠧࡿࠩ੹")), bstack1l1ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ੺"), bstack1l1ll_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪ੻"))
    bstack1l11l111ll_opy_ = {
      bstack1l1ll_opy_ (u"ࠪ࡭ࡩ࠭੼"): bstack1ll111lll_opy_,
      bstack1l1ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ੽"): datetime.datetime.strftime(datetime.datetime.now(), bstack1l1ll_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩ੾")),
      bstack1l1ll_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫ੿"): str(__version__)
    }
    try:
      bstack1l1ll1111l_opy_ = {}
      if os.path.exists(bstack1lll1l111l_opy_):
        bstack1l1ll1111l_opy_ = json.load(open(bstack1lll1l111l_opy_, bstack1l1ll_opy_ (u"ࠧࡳࡤࠪ઀")))
      bstack1l1ll1111l_opy_[md5_hash] = bstack1l11l111ll_opy_
      with open(bstack1lll1l111l_opy_, bstack1l1ll_opy_ (u"ࠣࡹ࠮ࠦઁ")) as outfile:
        json.dump(bstack1l1ll1111l_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1l1ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡷࡳࡨࡦࡺࡩ࡯ࡩࠣࡑࡉ࠻ࠠࡩࡣࡶ࡬ࠥ࡬ࡩ࡭ࡧ࠽ࠤࢀࢃࠧં").format(str(e)))
    return
  bstack1l1ll1lll1_opy_ = os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠪࢂࠬઃ")), bstack1l1ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ઄"))
  if not os.path.exists(bstack1l1ll1lll1_opy_):
    os.makedirs(bstack1l1ll1lll1_opy_)
  bstack1lll1l111l_opy_ = os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠬࢄࠧઅ")), bstack1l1ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭આ"), bstack1l1ll_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨઇ"))
  lock_file = bstack1lll1l111l_opy_ + bstack1l1ll_opy_ (u"ࠨ࠰࡯ࡳࡨࡱࠧઈ")
  bstack1l11l111ll_opy_ = {
    bstack1l1ll_opy_ (u"ࠩ࡬ࡨࠬઉ"): bstack1ll111lll_opy_,
    bstack1l1ll_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ઊ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1l1ll_opy_ (u"ࠫࠪࡪ࠯ࠦ࡯࠲ࠩ࡞ࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓࠨઋ")),
    bstack1l1ll_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪઌ"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1l1ll1111l_opy_ = {}
      if os.path.exists(bstack1lll1l111l_opy_):
        with open(bstack1lll1l111l_opy_, bstack1l1ll_opy_ (u"࠭ࡲࠨઍ")) as f:
          content = f.read().strip()
          if content:
            bstack1l1ll1111l_opy_ = json.loads(content)
      bstack1l1ll1111l_opy_[md5_hash] = bstack1l11l111ll_opy_
      with open(bstack1lll1l111l_opy_, bstack1l1ll_opy_ (u"ࠢࡸࠤ઎")) as outfile:
        json.dump(bstack1l1ll1111l_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡸ࡫ࡷ࡬ࠥ࡬ࡩ࡭ࡧࠣࡰࡴࡩ࡫ࡪࡰࡪࠤ࡫ࡵࡲࠡࡏࡇ࠹ࠥ࡮ࡡࡴࡪࠣࡹࡵࡪࡡࡵࡧ࠽ࠤࢀࢃࠧએ").format(str(e)))
def bstack1lll11l1_opy_(self):
  return
def bstack1l1l1lll11_opy_(self):
  return
def bstack1ll1111l11_opy_():
  global bstack11llll11_opy_
  bstack11llll11_opy_ = True
@measure(event_name=EVENTS.bstack11111ll1_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1lll1llll_opy_(self):
  global bstack111llll11_opy_
  global bstack1lllll11ll_opy_
  global bstack1l1l11lll_opy_
  try:
    if bstack1l1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩઐ") in bstack111llll11_opy_ and self.session_id != None and bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡔࡶࡤࡸࡺࡹࠧઑ"), bstack1l1ll_opy_ (u"ࠫࠬ઒")) != bstack1l1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ઓ"):
      bstack111l1l11l_opy_ = bstack1l1ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ઔ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧક")
      if bstack111l1l11l_opy_ == bstack1l1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨખ"):
        bstack1lll1l11ll_opy_(logger)
      if self != None:
        bstack1l1l111l1_opy_(self, bstack111l1l11l_opy_, bstack1l1ll_opy_ (u"ࠩ࠯ࠤࠬગ").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack1l1ll_opy_ (u"ࠪࠫઘ")
    if bstack1l1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫઙ") in bstack111llll11_opy_ and getattr(threading.current_thread(), bstack1l1ll_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫચ"), None):
      bstack1lll1111_opy_.bstack11111l111_opy_(self, bstack1l11l1111_opy_, logger, wait=True)
    if bstack1l1ll_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭છ") in bstack111llll11_opy_:
      if not threading.currentThread().behave_test_status:
        bstack1l1l111l1_opy_(self, bstack1l1ll_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢજ"))
      bstack1lll1lll1l_opy_.bstack1l1l11l1l_opy_(self)
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࠤઝ") + str(e))
  bstack1l1l11lll_opy_(self)
  self.session_id = None
def bstack1l11l1l1l_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack11ll11l111_opy_
    global bstack111llll11_opy_
    command_executor = kwargs.get(bstack1l1ll_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠬઞ"), bstack1l1ll_opy_ (u"ࠪࠫટ"))
    bstack1llll1l1l_opy_ = False
    if type(command_executor) == str and bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧઠ") in command_executor:
      bstack1llll1l1l_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨડ") in str(getattr(command_executor, bstack1l1ll_opy_ (u"࠭࡟ࡶࡴ࡯ࠫઢ"), bstack1l1ll_opy_ (u"ࠧࠨણ"))):
      bstack1llll1l1l_opy_ = True
    else:
      kwargs = bstack111111l1l_opy_.bstack1l1l11l1ll_opy_(bstack11111lll1_opy_=kwargs, config=CONFIG)
      return bstack1l11lll1l_opy_(self, *args, **kwargs)
    if bstack1llll1l1l_opy_:
      bstack11l1ll11l_opy_ = bstack1l111l111l_opy_.bstack11l11l1l1l_opy_(CONFIG, bstack111llll11_opy_)
      if kwargs.get(bstack1l1ll_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩત")):
        kwargs[bstack1l1ll_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪથ")] = bstack11ll11l111_opy_(kwargs[bstack1l1ll_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫદ")], bstack111llll11_opy_, CONFIG, bstack11l1ll11l_opy_)
      elif kwargs.get(bstack1l1ll_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫધ")):
        kwargs[bstack1l1ll_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬન")] = bstack11ll11l111_opy_(kwargs[bstack1l1ll_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭઩")], bstack111llll11_opy_, CONFIG, bstack11l1ll11l_opy_)
  except Exception as e:
    logger.error(bstack1l1ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩࡧࡱࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡕࡇࡏࠥࡩࡡࡱࡵ࠽ࠤࢀࢃࠢપ").format(str(e)))
  return bstack1l11lll1l_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l1l1l11ll_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1ll1lll1l_opy_(self, command_executor=bstack1l1ll_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰࠳࠵࠻࠳࠶࠮࠱࠰࠴࠾࠹࠺࠴࠵ࠤફ"), *args, **kwargs):
  global bstack1lllll11ll_opy_
  global bstack1lllllll1_opy_
  bstack1l11l1ll1_opy_ = bstack1l11l1l1l_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack11ll1llll1_opy_.on():
    return bstack1l11l1ll1_opy_
  try:
    logger.debug(bstack1l1ll_opy_ (u"ࠩࡆࡳࡲࡳࡡ࡯ࡦࠣࡉࡽ࡫ࡣࡶࡶࡲࡶࠥࡽࡨࡦࡰࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡩࡴࠢࡩࡥࡱࡹࡥࠡ࠯ࠣࡿࢂ࠭બ").format(str(command_executor)))
    logger.debug(bstack1l1ll_opy_ (u"ࠪࡌࡺࡨࠠࡖࡔࡏࠤ࡮ࡹࠠ࠮ࠢࡾࢁࠬભ").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧમ") in command_executor._url:
      bstack11l1lll1_opy_.bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ય"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩર") in command_executor):
    bstack11l1lll1_opy_.bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ઱"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1ll1ll1lll_opy_ = getattr(threading.current_thread(), bstack1l1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡕࡧࡶࡸࡒ࡫ࡴࡢࠩલ"), None)
  bstack11l1lllll1_opy_ = {}
  if self.capabilities is not None:
    bstack11l1lllll1_opy_[bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡲࡦࡳࡥࠨળ")] = self.capabilities.get(bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ઴"))
    bstack11l1lllll1_opy_[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭વ")] = self.capabilities.get(bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭શ"))
    bstack11l1lllll1_opy_[bstack1l1ll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡥ࡯ࡱࡶ࡬ࡳࡳࡹࠧષ")] = self.capabilities.get(bstack1l1ll_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬસ"))
  if CONFIG.get(bstack1l1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨહ"), False) and bstack111111l1l_opy_.bstack11l111111l_opy_(bstack11l1lllll1_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack1l1ll_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ઺") in bstack111llll11_opy_ or bstack1l1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ઻") in bstack111llll11_opy_:
    bstack11ll1ll1_opy_.bstack1l1111l111_opy_(self)
  if bstack1l1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷ઼ࠫ") in bstack111llll11_opy_ and bstack1ll1ll1lll_opy_ and bstack1ll1ll1lll_opy_.get(bstack1l1ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬઽ"), bstack1l1ll_opy_ (u"࠭ࠧા")) == bstack1l1ll_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨિ"):
    bstack11ll1ll1_opy_.bstack1l1111l111_opy_(self)
  bstack1lllll11ll_opy_ = self.session_id
  with bstack1lllll11l_opy_:
    bstack1lllllll1_opy_.append(self)
  return bstack1l11l1ll1_opy_
def bstack1lll1111l1_opy_(args):
  return bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠩી") in str(args)
def bstack1ll11l1l1_opy_(self, driver_command, *args, **kwargs):
  global bstack1llll111l_opy_
  global bstack1lll111l1l_opy_
  bstack11l1l11l1l_opy_ = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ુ"), None) and bstack11ll1ll11_opy_(
          threading.current_thread(), bstack1l1ll_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩૂ"), None)
  bstack11l1111ll_opy_ = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫૃ"), None) and bstack11ll1ll11_opy_(
          threading.current_thread(), bstack1l1ll_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧૄ"), None)
  bstack11l11ll1ll_opy_ = getattr(self, bstack1l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ૅ"), None) != None and getattr(self, bstack1l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ૆"), None) == True
  if not bstack1lll111l1l_opy_ and bstack1l1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨે") in CONFIG and CONFIG[bstack1l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩૈ")] == True and bstack11111lll_opy_.bstack11ll1l1lll_opy_(driver_command) and (bstack11l11ll1ll_opy_ or bstack11l1l11l1l_opy_ or bstack11l1111ll_opy_) and not bstack1lll1111l1_opy_(args):
    try:
      bstack1lll111l1l_opy_ = True
      logger.debug(bstack1l1ll_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥ࡬࡯ࡳࠢࡾࢁࠬૉ").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack1l1ll_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡧࡵࡪࡴࡸ࡭ࠡࡵࡦࡥࡳࠦࡻࡾࠩ૊").format(str(err)))
    bstack1lll111l1l_opy_ = False
  response = bstack1llll111l_opy_(self, driver_command, *args, **kwargs)
  if (bstack1l1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫો") in str(bstack111llll11_opy_).lower() or bstack1l1ll_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ૌ") in str(bstack111llll11_opy_).lower()) and bstack11ll1llll1_opy_.on():
    try:
      if driver_command == bstack1l1ll_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷ્ࠫ"):
        bstack11ll1ll1_opy_.bstack1l11ll1ll1_opy_({
            bstack1l1ll_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧ૎"): response[bstack1l1ll_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨ૏")],
            bstack1l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪૐ"): bstack11ll1ll1_opy_.current_test_uuid() if bstack11ll1ll1_opy_.current_test_uuid() else bstack11ll1llll1_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack11l1ll1lll_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1l1l111lll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1lllll11ll_opy_
  global bstack11ll1ll111_opy_
  global bstack1l1l1ll1l_opy_
  global bstack1llll1l1_opy_
  global bstack1111l11l_opy_
  global bstack111llll11_opy_
  global bstack1l11lll1l_opy_
  global bstack1lllllll1_opy_
  global bstack1ll11ll1l_opy_
  global bstack1l11l1111_opy_
  CONFIG[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭૑")] = str(bstack111llll11_opy_) + str(__version__)
  bstack11ll11ll1l_opy_ = os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ૒")]
  bstack11l1ll11l_opy_ = bstack1l111l111l_opy_.bstack11l11l1l1l_opy_(CONFIG, bstack111llll11_opy_)
  CONFIG[bstack1l1ll_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩ૓")] = bstack11ll11ll1l_opy_
  CONFIG[bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ૔")] = bstack11l1ll11l_opy_
  if CONFIG.get(bstack1l1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ૕"),bstack1l1ll_opy_ (u"ࠩࠪ૖")) and bstack1l1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ૗") in bstack111llll11_opy_:
    CONFIG[bstack1l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ૘")].pop(bstack1l1ll_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ૙"), None)
    CONFIG[bstack1l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭૚")].pop(bstack1l1ll_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ૛"), None)
  command_executor = bstack11ll1l1l1l_opy_()
  logger.debug(bstack1111111l_opy_.format(command_executor))
  proxy = bstack11l1l11l_opy_(CONFIG, proxy)
  bstack1ll1l1111l_opy_ = 0 if bstack11ll1ll111_opy_ < 0 else bstack11ll1ll111_opy_
  try:
    if bstack1llll1l1_opy_ is True:
      bstack1ll1l1111l_opy_ = int(multiprocessing.current_process().name)
    elif bstack1111l11l_opy_ is True:
      bstack1ll1l1111l_opy_ = int(threading.current_thread().name)
  except:
    bstack1ll1l1111l_opy_ = 0
  bstack1l1lll1l11_opy_ = bstack1l1l1l11_opy_(CONFIG, bstack1ll1l1111l_opy_)
  logger.debug(bstack1l11l11l1l_opy_.format(str(bstack1l1lll1l11_opy_)))
  if bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ૜") in CONFIG and bstack1ll1l11l_opy_(CONFIG[bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭૝")]):
    bstack1l1l11lll1_opy_(bstack1l1lll1l11_opy_)
  if bstack111111l1l_opy_.bstack1l1ll11l11_opy_(CONFIG, bstack1ll1l1111l_opy_) and bstack111111l1l_opy_.bstack1ll1llllll_opy_(bstack1l1lll1l11_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack111111l1l_opy_.set_capabilities(bstack1l1lll1l11_opy_, CONFIG)
  if desired_capabilities:
    bstack11ll1lll1_opy_ = bstack11ll111l1_opy_(desired_capabilities)
    bstack11ll1lll1_opy_[bstack1l1ll_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪ૞")] = bstack1l111l1l1_opy_(CONFIG)
    bstack1ll11l1ll_opy_ = bstack1l1l1l11_opy_(bstack11ll1lll1_opy_)
    if bstack1ll11l1ll_opy_:
      bstack1l1lll1l11_opy_ = update(bstack1ll11l1ll_opy_, bstack1l1lll1l11_opy_)
    desired_capabilities = None
  if options:
    bstack1l11lll1l1_opy_(options, bstack1l1lll1l11_opy_)
  if not options:
    options = bstack1ll1lll111_opy_(bstack1l1lll1l11_opy_)
  bstack1l11l1111_opy_ = CONFIG.get(bstack1l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૟"))[bstack1ll1l1111l_opy_]
  if proxy and bstack1l1l1l111l_opy_() >= version.parse(bstack1l1ll_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬૠ")):
    options.proxy(proxy)
  if options and bstack1l1l1l111l_opy_() >= version.parse(bstack1l1ll_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬૡ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1l1l1l111l_opy_() < version.parse(bstack1l1ll_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ૢ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1l1lll1l11_opy_)
  logger.info(bstack1l1ll111_opy_)
  bstack11l1l111l_opy_.end(EVENTS.bstack1lll1lllll_opy_.value, EVENTS.bstack1lll1lllll_opy_.value + bstack1l1ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣૣ"), EVENTS.bstack1lll1lllll_opy_.value + bstack1l1ll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ૤"), status=True, failure=None, test_name=bstack1l1l1ll1l_opy_)
  if bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡵࡸ࡯ࡧ࡫࡯ࡩࠬ૥") in kwargs:
    del kwargs[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡶࡲࡰࡨ࡬ࡰࡪ࠭૦")]
  if bstack1l1l1l111l_opy_() >= version.parse(bstack1l1ll_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬ૧")):
    bstack1l11lll1l_opy_(self, command_executor=command_executor,
              options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
  elif bstack1l1l1l111l_opy_() >= version.parse(bstack1l1ll_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬ૨")):
    bstack1l11lll1l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities, options=options,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  elif bstack1l1l1l111l_opy_() >= version.parse(bstack1l1ll_opy_ (u"ࠧ࠳࠰࠸࠷࠳࠶ࠧ૩")):
    bstack1l11lll1l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive, file_detector=file_detector)
  else:
    bstack1l11lll1l_opy_(self, command_executor=command_executor,
              desired_capabilities=desired_capabilities,
              browser_profile=browser_profile, proxy=proxy,
              keep_alive=keep_alive)
  if bstack111111l1l_opy_.bstack1l1ll11l11_opy_(CONFIG, bstack1ll1l1111l_opy_) and bstack111111l1l_opy_.bstack1ll1llllll_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack1l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪ૪")][bstack1l1ll_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨ૫")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack111111l1l_opy_.set_capabilities(bstack1l1lll1l11_opy_, CONFIG)
  try:
    bstack1ll1111l_opy_ = bstack1l1ll_opy_ (u"ࠪࠫ૬")
    if bstack1l1l1l111l_opy_() >= version.parse(bstack1l1ll_opy_ (u"ࠫ࠹࠴࠰࠯࠲ࡥ࠵ࠬ૭")):
      if self.caps is not None:
        bstack1ll1111l_opy_ = self.caps.get(bstack1l1ll_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧ૮"))
    else:
      if self.capabilities is not None:
        bstack1ll1111l_opy_ = self.capabilities.get(bstack1l1ll_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨ૯"))
    if bstack1ll1111l_opy_:
      bstack1l1l111111_opy_(bstack1ll1111l_opy_)
      if bstack1l1l1l111l_opy_() <= version.parse(bstack1l1ll_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧ૰")):
        self.command_executor._url = bstack1l1ll_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤ૱") + bstack1lll11lll_opy_ + bstack1l1ll_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨ૲")
      else:
        self.command_executor._url = bstack1l1ll_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧ૳") + bstack1ll1111l_opy_ + bstack1l1ll_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧ૴")
      logger.debug(bstack11ll11ll11_opy_.format(bstack1ll1111l_opy_))
    else:
      logger.debug(bstack1l1l1l1111_opy_.format(bstack1l1ll_opy_ (u"ࠧࡕࡰࡵ࡫ࡰࡥࡱࠦࡈࡶࡤࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩࠨ૵")))
  except Exception as e:
    logger.debug(bstack1l1l1l1111_opy_.format(e))
  if bstack1l1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ૶") in bstack111llll11_opy_:
    bstack1ll1ll1ll1_opy_(bstack11ll1ll111_opy_, bstack1ll11ll1l_opy_)
  bstack1lllll11ll_opy_ = self.session_id
  if bstack1l1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ૷") in bstack111llll11_opy_ or bstack1l1ll_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ૸") in bstack111llll11_opy_ or bstack1l1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨૹ") in bstack111llll11_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack1ll1ll1lll_opy_ = getattr(threading.current_thread(), bstack1l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡗࡩࡸࡺࡍࡦࡶࡤࠫૺ"), None)
  if bstack1l1ll_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫૻ") in bstack111llll11_opy_ or bstack1l1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫૼ") in bstack111llll11_opy_:
    bstack11ll1ll1_opy_.bstack1l1111l111_opy_(self)
  if bstack1l1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭૽") in bstack111llll11_opy_ and bstack1ll1ll1lll_opy_ and bstack1ll1ll1lll_opy_.get(bstack1l1ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ૾"), bstack1l1ll_opy_ (u"ࠨࠩ૿")) == bstack1l1ll_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪ଀"):
    bstack11ll1ll1_opy_.bstack1l1111l111_opy_(self)
  with bstack1lllll11l_opy_:
    bstack1lllllll1_opy_.append(self)
  if bstack1l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଁ") in CONFIG and bstack1l1ll_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩଂ") in CONFIG[bstack1l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨଃ")][bstack1ll1l1111l_opy_]:
    bstack1l1l1ll1l_opy_ = CONFIG[bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ଄")][bstack1ll1l1111l_opy_][bstack1l1ll_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬଅ")]
  logger.debug(bstack1l1l1ll1ll_opy_.format(bstack1lllll11ll_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1ll11lll_opy_
    def bstack11ll11l11_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1lll1l1111_opy_
      if(bstack1l1ll_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࠮࡫ࡵࠥଆ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠩࢁࠫଇ")), bstack1l1ll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪଈ"), bstack1l1ll_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭ଉ")), bstack1l1ll_opy_ (u"ࠬࡽࠧଊ")) as fp:
          fp.write(bstack1l1ll_opy_ (u"ࠨࠢଋ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1l1ll_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤଌ")))):
          with open(args[1], bstack1l1ll_opy_ (u"ࠨࡴࠪ଍")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1l1ll_opy_ (u"ࠩࡤࡷࡾࡴࡣࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡣࡳ࡫ࡷࡑࡣࡪࡩ࠭ࡩ࡯࡯ࡶࡨࡼࡹ࠲ࠠࡱࡣࡪࡩࠥࡃࠠࡷࡱ࡬ࡨࠥ࠶ࠩࠨ଎") in line), None)
            if index is not None:
                lines.insert(index+2, bstack11l1lll111_opy_)
            if bstack1l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧଏ") in CONFIG and str(CONFIG[bstack1l1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨଐ")]).lower() != bstack1l1ll_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ଑"):
                bstack1l1ll111ll_opy_ = bstack1ll11lll_opy_()
                bstack11llll11l1_opy_ = bstack1l1ll_opy_ (u"࠭ࠧࠨࠌ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠏࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸ࡣ࠻ࠋࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࠾ࠎࡨࡵ࡮ࡴࡶࠣࡴࡤ࡯࡮ࡥࡧࡻࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠲࡞࠽ࠍࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡷࡱ࡯ࡣࡦࠪ࠳࠰ࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳ࠪ࠽ࠍࡧࡴࡴࡳࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣࠫ࠾ࠎ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡱࡧࡵ࡯ࡥ࡫ࠤࡂࠦࡡࡴࡻࡱࡧࠥ࠮࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸ࠯ࠠ࠾ࡀࠣࡿࢀࠐࠠࠡ࡮ࡨࡸࠥࡩࡡࡱࡵ࠾ࠎࠥࠦࡴࡳࡻࠣࡿࢀࠐࠠࠡࠢࠣࡧࡦࡶࡳࠡ࠿ࠣࡎࡘࡕࡎ࠯ࡲࡤࡶࡸ࡫ࠨࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷ࠮ࡁࠊࠡࠢࢀࢁࠥࡩࡡࡵࡥ࡫ࠤ࠭࡫ࡸࠪࠢࡾࡿࠏࠦࠠࠡࠢࡦࡳࡳࡹ࡯࡭ࡧ࠱ࡩࡷࡸ࡯ࡳࠪࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶ࠾ࠧ࠲ࠠࡦࡺࠬ࠿ࠏࠦࠠࡾࡿࠍࠤࠥࡸࡥࡵࡷࡵࡲࠥࡧࡷࡢ࡫ࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡨࡵ࡮࡯ࡧࡦࡸ࠭ࢁࡻࠋࠢࠣࠤࠥࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵ࠼ࠣࠫࢀࡩࡤࡱࡗࡵࡰࢂ࠭ࠠࠬࠢࡨࡲࡨࡵࡤࡦࡗࡕࡍࡈࡵ࡭ࡱࡱࡱࡩࡳࡺࠨࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡥࡤࡴࡸ࠯ࠩ࠭ࠌࠣࠤࠥࠦ࠮࠯࠰࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴࠌࠣࠤࢂࢃࠩ࠼ࠌࢀࢁࡀࠐ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰ࠌࠪࠫࠬ଒").format(bstack1l1ll111ll_opy_=bstack1l1ll111ll_opy_)
            lines.insert(1, bstack11llll11l1_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1l1ll_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤଓ")), bstack1l1ll_opy_ (u"ࠨࡹࠪଔ")) as bstack1ll1111111_opy_:
              bstack1ll1111111_opy_.writelines(lines)
        CONFIG[bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫକ")] = str(bstack111llll11_opy_) + str(__version__)
        bstack11ll11ll1l_opy_ = os.environ[bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨଖ")]
        bstack11l1ll11l_opy_ = bstack1l111l111l_opy_.bstack11l11l1l1l_opy_(CONFIG, bstack111llll11_opy_)
        CONFIG[bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧଗ")] = bstack11ll11ll1l_opy_
        CONFIG[bstack1l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧଘ")] = bstack11l1ll11l_opy_
        bstack1ll1l1111l_opy_ = 0 if bstack11ll1ll111_opy_ < 0 else bstack11ll1ll111_opy_
        try:
          if bstack1llll1l1_opy_ is True:
            bstack1ll1l1111l_opy_ = int(multiprocessing.current_process().name)
          elif bstack1111l11l_opy_ is True:
            bstack1ll1l1111l_opy_ = int(threading.current_thread().name)
        except:
          bstack1ll1l1111l_opy_ = 0
        CONFIG[bstack1l1ll_opy_ (u"ࠨࡵࡴࡧ࡚࠷ࡈࠨଙ")] = False
        CONFIG[bstack1l1ll_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨଚ")] = True
        bstack1l1lll1l11_opy_ = bstack1l1l1l11_opy_(CONFIG, bstack1ll1l1111l_opy_)
        logger.debug(bstack1l11l11l1l_opy_.format(str(bstack1l1lll1l11_opy_)))
        if CONFIG.get(bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬଛ")):
          bstack1l1l11lll1_opy_(bstack1l1lll1l11_opy_)
        if bstack1l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଜ") in CONFIG and bstack1l1ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨଝ") in CONFIG[bstack1l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଞ")][bstack1ll1l1111l_opy_]:
          bstack1l1l1ll1l_opy_ = CONFIG[bstack1l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨଟ")][bstack1ll1l1111l_opy_][bstack1l1ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫଠ")]
        args.append(os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠧࡿࠩଡ")), bstack1l1ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨଢ"), bstack1l1ll_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫଣ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1l1lll1l11_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1l1ll_opy_ (u"ࠥ࡭ࡳࡪࡥࡹࡡࡥࡷࡹࡧࡣ࡬࠰࡭ࡷࠧତ"))
      bstack1lll1l1111_opy_ = True
      return bstack11ll111lll_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack1ll1l1lll_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack11ll1ll111_opy_
    global bstack1l1l1ll1l_opy_
    global bstack1llll1l1_opy_
    global bstack1111l11l_opy_
    global bstack111llll11_opy_
    CONFIG[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ଥ")] = str(bstack111llll11_opy_) + str(__version__)
    bstack11ll11ll1l_opy_ = os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪଦ")]
    bstack11l1ll11l_opy_ = bstack1l111l111l_opy_.bstack11l11l1l1l_opy_(CONFIG, bstack111llll11_opy_)
    CONFIG[bstack1l1ll_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩଧ")] = bstack11ll11ll1l_opy_
    CONFIG[bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩନ")] = bstack11l1ll11l_opy_
    bstack1ll1l1111l_opy_ = 0 if bstack11ll1ll111_opy_ < 0 else bstack11ll1ll111_opy_
    try:
      if bstack1llll1l1_opy_ is True:
        bstack1ll1l1111l_opy_ = int(multiprocessing.current_process().name)
      elif bstack1111l11l_opy_ is True:
        bstack1ll1l1111l_opy_ = int(threading.current_thread().name)
    except:
      bstack1ll1l1111l_opy_ = 0
    CONFIG[bstack1l1ll_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ଩")] = True
    bstack1l1lll1l11_opy_ = bstack1l1l1l11_opy_(CONFIG, bstack1ll1l1111l_opy_)
    logger.debug(bstack1l11l11l1l_opy_.format(str(bstack1l1lll1l11_opy_)))
    if CONFIG.get(bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ପ")):
      bstack1l1l11lll1_opy_(bstack1l1lll1l11_opy_)
    if bstack1l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଫ") in CONFIG and bstack1l1ll_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩବ") in CONFIG[bstack1l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨଭ")][bstack1ll1l1111l_opy_]:
      bstack1l1l1ll1l_opy_ = CONFIG[bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩମ")][bstack1ll1l1111l_opy_][bstack1l1ll_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬଯ")]
    import urllib
    import json
    if bstack1l1ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬର") in CONFIG and str(CONFIG[bstack1l1ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭଱")]).lower() != bstack1l1ll_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩଲ"):
        bstack11lllllll1_opy_ = bstack1ll11lll_opy_()
        bstack1l1ll111ll_opy_ = bstack11lllllll1_opy_ + urllib.parse.quote(json.dumps(bstack1l1lll1l11_opy_))
    else:
        bstack1l1ll111ll_opy_ = bstack1l1ll_opy_ (u"ࠫࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂ࠭ଳ") + urllib.parse.quote(json.dumps(bstack1l1lll1l11_opy_))
    browser = self.connect(bstack1l1ll111ll_opy_)
    return browser
except Exception as e:
    pass
def bstack1l111lll11_opy_():
    global bstack1lll1l1111_opy_
    global bstack111llll11_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1111l1l1l_opy_
        global bstack11l1lll1_opy_
        if not bstack1ll1l111ll_opy_:
          global bstack1l11ll11l_opy_
          if not bstack1l11ll11l_opy_:
            from bstack_utils.helper import bstack1lllll1l1l_opy_, bstack1ll1111ll_opy_, bstack11l1l111_opy_
            bstack1l11ll11l_opy_ = bstack1lllll1l1l_opy_()
            bstack1ll1111ll_opy_(bstack111llll11_opy_)
            bstack11l1ll11l_opy_ = bstack1l111l111l_opy_.bstack11l11l1l1l_opy_(CONFIG, bstack111llll11_opy_)
            bstack11l1lll1_opy_.bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠧࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡓࡖࡔࡊࡕࡄࡖࡢࡑࡆࡖࠢ଴"), bstack11l1ll11l_opy_)
          BrowserType.connect = bstack1111l1l1l_opy_
          return
        BrowserType.launch = bstack1ll1l1lll_opy_
        bstack1lll1l1111_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack11ll11l11_opy_
      bstack1lll1l1111_opy_ = True
    except Exception as e:
      pass
def bstack1ll11111l1_opy_(context, bstack11lll1lll_opy_):
  try:
    context.page.evaluate(bstack1l1ll_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢଵ"), bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠫଶ")+ json.dumps(bstack11lll1lll_opy_) + bstack1l1ll_opy_ (u"ࠣࡿࢀࠦଷ"))
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤࢀࢃ࠺ࠡࡽࢀࠦସ").format(str(e), traceback.format_exc()))
def bstack11l111l1ll_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1l1ll_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦହ"), bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ଺") + json.dumps(message) + bstack1l1ll_opy_ (u"ࠬ࠲ࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠨ଻") + json.dumps(level) + bstack1l1ll_opy_ (u"࠭ࡽࡾ଼ࠩ"))
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠠࡼࡿ࠽ࠤࢀࢃࠢଽ").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1l1l1111l_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1l11ll11ll_opy_(self, url):
  global bstack1l11lll1ll_opy_
  try:
    bstack11lll11l_opy_(url)
  except Exception as err:
    logger.debug(bstack1ll1l1l11l_opy_.format(str(err)))
  try:
    bstack1l11lll1ll_opy_(self, url)
  except Exception as e:
    try:
      bstack111ll1ll1_opy_ = str(e)
      if any(err_msg in bstack111ll1ll1_opy_ for err_msg in bstack11lll11l1l_opy_):
        bstack11lll11l_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1ll1l1l11l_opy_.format(str(err)))
    raise e
def bstack1l1l1l11l1_opy_(self):
  global bstack111l1111_opy_
  bstack111l1111_opy_ = self
  return
def bstack1l111l1l11_opy_(self):
  global bstack1l1l1l1ll1_opy_
  bstack1l1l1l1ll1_opy_ = self
  return
def bstack1ll111l1l_opy_(test_name, bstack11llll11ll_opy_):
  global CONFIG
  if percy.bstack1111ll1ll_opy_() == bstack1l1ll_opy_ (u"ࠣࡶࡵࡹࡪࠨା"):
    bstack1l1111lll_opy_ = os.path.relpath(bstack11llll11ll_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1l1111lll_opy_)
    bstack1l1ll11l1l_opy_ = suite_name + bstack1l1ll_opy_ (u"ࠤ࠰ࠦି") + test_name
    threading.current_thread().percySessionName = bstack1l1ll11l1l_opy_
def bstack11llllll1l_opy_(self, test, *args, **kwargs):
  global bstack1ll11111l_opy_
  test_name = None
  bstack11llll11ll_opy_ = None
  if test:
    test_name = str(test.name)
    bstack11llll11ll_opy_ = str(test.source)
  bstack1ll111l1l_opy_(test_name, bstack11llll11ll_opy_)
  bstack1ll11111l_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l111lll1_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack11lll11ll_opy_(driver, bstack1l1ll11l1l_opy_):
  if not bstack111ll111l_opy_ and bstack1l1ll11l1l_opy_:
      bstack1l11l1l111_opy_ = {
          bstack1l1ll_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪୀ"): bstack1l1ll_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬୁ"),
          bstack1l1ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨୂ"): {
              bstack1l1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫୃ"): bstack1l1ll11l1l_opy_
          }
      }
      bstack1l1lll111_opy_ = bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬୄ").format(json.dumps(bstack1l11l1l111_opy_))
      driver.execute_script(bstack1l1lll111_opy_)
  if bstack11ll111ll_opy_:
      bstack11lll1l11_opy_ = {
          bstack1l1ll_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨ୅"): bstack1l1ll_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫ୆"),
          bstack1l1ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭େ"): {
              bstack1l1ll_opy_ (u"ࠫࡩࡧࡴࡢࠩୈ"): bstack1l1ll11l1l_opy_ + bstack1l1ll_opy_ (u"ࠬࠦࡰࡢࡵࡶࡩࡩࠧࠧ୉"),
              bstack1l1ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ୊"): bstack1l1ll_opy_ (u"ࠧࡪࡰࡩࡳࠬୋ")
          }
      }
      if bstack11ll111ll_opy_.status == bstack1l1ll_opy_ (u"ࠨࡒࡄࡗࡘ࠭ୌ"):
          bstack11l1llllll_opy_ = bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃ୍ࠧ").format(json.dumps(bstack11lll1l11_opy_))
          driver.execute_script(bstack11l1llllll_opy_)
          bstack1l1l111l1_opy_(driver, bstack1l1ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ୎"))
      elif bstack11ll111ll_opy_.status == bstack1l1ll_opy_ (u"ࠫࡋࡇࡉࡍࠩ୏"):
          reason = bstack1l1ll_opy_ (u"ࠧࠨ୐")
          bstack1ll1ll11l1_opy_ = bstack1l1ll11l1l_opy_ + bstack1l1ll_opy_ (u"࠭ࠠࡧࡣ࡬ࡰࡪࡪࠧ୑")
          if bstack11ll111ll_opy_.message:
              reason = str(bstack11ll111ll_opy_.message)
              bstack1ll1ll11l1_opy_ = bstack1ll1ll11l1_opy_ + bstack1l1ll_opy_ (u"ࠧࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶ࠿ࠦࠧ୒") + reason
          bstack11lll1l11_opy_[bstack1l1ll_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ୓")] = {
              bstack1l1ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ୔"): bstack1l1ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ୕"),
              bstack1l1ll_opy_ (u"ࠫࡩࡧࡴࡢࠩୖ"): bstack1ll1ll11l1_opy_
          }
          bstack11l1llllll_opy_ = bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪୗ").format(json.dumps(bstack11lll1l11_opy_))
          driver.execute_script(bstack11l1llllll_opy_)
          bstack1l1l111l1_opy_(driver, bstack1l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭୘"), reason)
          bstack11lllll1l_opy_(reason, str(bstack11ll111ll_opy_), str(bstack11ll1ll111_opy_), logger)
@measure(event_name=EVENTS.bstack11llll11l_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1ll11l11l1_opy_(driver, test):
  if percy.bstack1111ll1ll_opy_() == bstack1l1ll_opy_ (u"ࠢࡵࡴࡸࡩࠧ୙") and percy.bstack11ll1ll1l_opy_() == bstack1l1ll_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥ୚"):
      bstack111l1l11_opy_ = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ୛"), None)
      bstack1ll1ll1l11_opy_(driver, bstack111l1l11_opy_, test)
  if (bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧଡ଼"), None) and
      bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪଢ଼"), None)) or (
      bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ୞"), None) and
      bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨୟ"), None)):
      logger.info(bstack1l1ll_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠦࠢୠ"))
      bstack111111l1l_opy_.bstack1lll1llll1_opy_(driver, name=test.name, path=test.source)
def bstack1l11111l11_opy_(test, bstack1l1ll11l1l_opy_):
    try:
      bstack11l1l1111_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack1l1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ୡ")] = bstack1l1ll11l1l_opy_
      if bstack11ll111ll_opy_:
        if bstack11ll111ll_opy_.status == bstack1l1ll_opy_ (u"ࠩࡓࡅࡘ࡙ࠧୢ"):
          data[bstack1l1ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪୣ")] = bstack1l1ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ୤")
        elif bstack11ll111ll_opy_.status == bstack1l1ll_opy_ (u"ࠬࡌࡁࡊࡎࠪ୥"):
          data[bstack1l1ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭୦")] = bstack1l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ୧")
          if bstack11ll111ll_opy_.message:
            data[bstack1l1ll_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨ୨")] = str(bstack11ll111ll_opy_.message)
      user = CONFIG[bstack1l1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ୩")]
      key = CONFIG[bstack1l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭୪")]
      host = bstack1lll1ll1ll_opy_(cli.config, [bstack1l1ll_opy_ (u"ࠦࡦࡶࡩࡴࠤ୫"), bstack1l1ll_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢ୬"), bstack1l1ll_opy_ (u"ࠨࡡࡱ࡫ࠥ୭")], bstack1l1ll_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠣ୮"))
      url = bstack1l1ll_opy_ (u"ࠨࡽࢀ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡳࡦࡵࡶ࡭ࡴࡴࡳ࠰ࡽࢀ࠲࡯ࡹ࡯࡯ࠩ୯").format(host, bstack1lllll11ll_opy_)
      headers = {
        bstack1l1ll_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨ୰"): bstack1l1ll_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ୱ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡸࡴࡩࡧࡴࡦࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡷࡥࡹࡻࡳࠣ୲"), datetime.datetime.now() - bstack11l1l1111_opy_)
    except Exception as e:
      logger.error(bstack11ll1l1ll_opy_.format(str(e)))
def bstack1llllll11l_opy_(test, bstack1l1ll11l1l_opy_):
  global CONFIG
  global bstack1l1l1l1ll1_opy_
  global bstack111l1111_opy_
  global bstack1lllll11ll_opy_
  global bstack11ll111ll_opy_
  global bstack1l1l1ll1l_opy_
  global bstack111lllll1l_opy_
  global bstack11ll11l1ll_opy_
  global bstack11ll1lllll_opy_
  global bstack11ll11llll_opy_
  global bstack1lllllll1_opy_
  global bstack1l11l1111_opy_
  global bstack1l1ll1lll_opy_
  try:
    if not bstack1lllll11ll_opy_:
      with bstack1l1ll1lll_opy_:
        bstack1ll1l1111_opy_ = os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠬࢄࠧ୳")), bstack1l1ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭୴"), bstack1l1ll_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩ୵"))
        if os.path.exists(bstack1ll1l1111_opy_):
          with open(bstack1ll1l1111_opy_, bstack1l1ll_opy_ (u"ࠨࡴࠪ୶")) as f:
            content = f.read().strip()
            if content:
              bstack1l1l11111_opy_ = json.loads(bstack1l1ll_opy_ (u"ࠤࡾࠦ୷") + content + bstack1l1ll_opy_ (u"ࠪࠦࡽࠨ࠺ࠡࠤࡼࠦࠬ୸") + bstack1l1ll_opy_ (u"ࠦࢂࠨ୹"))
              bstack1lllll11ll_opy_ = bstack1l1l11111_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࡵࠣࡪ࡮ࡲࡥ࠻ࠢࠪ୺") + str(e))
  if bstack1lllllll1_opy_:
    with bstack1lllll11l_opy_:
      bstack1llll1111_opy_ = bstack1lllllll1_opy_.copy()
    for driver in bstack1llll1111_opy_:
      if bstack1lllll11ll_opy_ == driver.session_id:
        if test:
          bstack1ll11l11l1_opy_(driver, test)
        bstack11lll11ll_opy_(driver, bstack1l1ll11l1l_opy_)
  elif bstack1lllll11ll_opy_:
    bstack1l11111l11_opy_(test, bstack1l1ll11l1l_opy_)
  if bstack1l1l1l1ll1_opy_:
    bstack11ll11l1ll_opy_(bstack1l1l1l1ll1_opy_)
  if bstack111l1111_opy_:
    bstack11ll1lllll_opy_(bstack111l1111_opy_)
  if bstack11llll11_opy_:
    bstack11ll11llll_opy_()
def bstack1lll11l1l_opy_(self, test, *args, **kwargs):
  bstack1l1ll11l1l_opy_ = None
  if test:
    bstack1l1ll11l1l_opy_ = str(test.name)
  bstack1llllll11l_opy_(test, bstack1l1ll11l1l_opy_)
  bstack111lllll1l_opy_(self, test, *args, **kwargs)
def bstack1111l11ll_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1l1ll1ll1l_opy_
  global CONFIG
  global bstack1lllllll1_opy_
  global bstack1lllll11ll_opy_
  global bstack1l1ll1lll_opy_
  bstack1ll1l1llll_opy_ = None
  try:
    if bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ୻"), None) or bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ୼"), None):
      try:
        if not bstack1lllll11ll_opy_:
          bstack1ll1l1111_opy_ = os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠨࢀࠪ୽")), bstack1l1ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ୾"), bstack1l1ll_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬ୿"))
          with bstack1l1ll1lll_opy_:
            if os.path.exists(bstack1ll1l1111_opy_):
              with open(bstack1ll1l1111_opy_, bstack1l1ll_opy_ (u"ࠫࡷ࠭஀")) as f:
                content = f.read().strip()
                if content:
                  bstack1l1l11111_opy_ = json.loads(bstack1l1ll_opy_ (u"ࠧࢁࠢ஁") + content + bstack1l1ll_opy_ (u"࠭ࠢࡹࠤ࠽ࠤࠧࡿࠢࠨஂ") + bstack1l1ll_opy_ (u"ࠢࡾࠤஃ"))
                  bstack1lllll11ll_opy_ = bstack1l1l11111_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡳࡧࡤࡨ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡌࡈࡸࠦࡦࡪ࡮ࡨࠤ࡮ࡴࠠࡵࡧࡶࡸࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠧ஄") + str(e))
      if bstack1lllllll1_opy_:
        with bstack1lllll11l_opy_:
          bstack1llll1111_opy_ = bstack1lllllll1_opy_.copy()
        for driver in bstack1llll1111_opy_:
          if bstack1lllll11ll_opy_ == driver.session_id:
            bstack1ll1l1llll_opy_ = driver
    bstack11l1ll111l_opy_ = bstack111111l1l_opy_.bstack1lllll1111_opy_(test.tags)
    if bstack1ll1l1llll_opy_:
      threading.current_thread().isA11yTest = bstack111111l1l_opy_.bstack1l1ll1llll_opy_(bstack1ll1l1llll_opy_, bstack11l1ll111l_opy_)
      threading.current_thread().isAppA11yTest = bstack111111l1l_opy_.bstack1l1ll1llll_opy_(bstack1ll1l1llll_opy_, bstack11l1ll111l_opy_)
    else:
      threading.current_thread().isA11yTest = bstack11l1ll111l_opy_
      threading.current_thread().isAppA11yTest = bstack11l1ll111l_opy_
  except:
    pass
  bstack1l1ll1ll1l_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack11ll111ll_opy_
  try:
    bstack11ll111ll_opy_ = self._test
  except:
    bstack11ll111ll_opy_ = self.test
def bstack1ll1l111l_opy_():
  global bstack1lll1l1l_opy_
  try:
    if os.path.exists(bstack1lll1l1l_opy_):
      os.remove(bstack1lll1l1l_opy_)
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡩ࡫࡬ࡦࡶ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬஅ") + str(e))
def bstack11ll1l11_opy_():
  global bstack1lll1l1l_opy_
  bstack111l11lll_opy_ = {}
  lock_file = bstack1lll1l1l_opy_ + bstack1l1ll_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩஆ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1ll_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧஇ"))
    try:
      if not os.path.isfile(bstack1lll1l1l_opy_):
        with open(bstack1lll1l1l_opy_, bstack1l1ll_opy_ (u"ࠬࡽࠧஈ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1lll1l1l_opy_):
        with open(bstack1lll1l1l_opy_, bstack1l1ll_opy_ (u"࠭ࡲࠨஉ")) as f:
          content = f.read().strip()
          if content:
            bstack111l11lll_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack1l1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩஊ") + str(e))
    return bstack111l11lll_opy_
  try:
    os.makedirs(os.path.dirname(bstack1lll1l1l_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack1lll1l1l_opy_):
        with open(bstack1lll1l1l_opy_, bstack1l1ll_opy_ (u"ࠨࡹࠪ஋")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1lll1l1l_opy_):
        with open(bstack1lll1l1l_opy_, bstack1l1ll_opy_ (u"ࠩࡵࠫ஌")) as f:
          content = f.read().strip()
          if content:
            bstack111l11lll_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬ஍") + str(e))
  finally:
    return bstack111l11lll_opy_
def bstack1ll1ll1ll1_opy_(platform_index, item_index):
  global bstack1lll1l1l_opy_
  lock_file = bstack1lll1l1l_opy_ + bstack1l1ll_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪஎ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨஏ"))
    try:
      bstack111l11lll_opy_ = {}
      if os.path.exists(bstack1lll1l1l_opy_):
        with open(bstack1lll1l1l_opy_, bstack1l1ll_opy_ (u"࠭ࡲࠨஐ")) as f:
          content = f.read().strip()
          if content:
            bstack111l11lll_opy_ = json.loads(content)
      bstack111l11lll_opy_[item_index] = platform_index
      with open(bstack1lll1l1l_opy_, bstack1l1ll_opy_ (u"ࠢࡸࠤ஑")) as outfile:
        json.dump(bstack111l11lll_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1l1ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡻࡷ࡯ࡴࡪࡰࡪࠤࡹࡵࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ஒ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack1lll1l1l_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack111l11lll_opy_ = {}
      if os.path.exists(bstack1lll1l1l_opy_):
        with open(bstack1lll1l1l_opy_, bstack1l1ll_opy_ (u"ࠩࡵࠫஓ")) as f:
          content = f.read().strip()
          if content:
            bstack111l11lll_opy_ = json.loads(content)
      bstack111l11lll_opy_[item_index] = platform_index
      with open(bstack1lll1l1l_opy_, bstack1l1ll_opy_ (u"ࠥࡻࠧஔ")) as outfile:
        json.dump(bstack111l11lll_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡷࡳ࡫ࡷ࡭ࡳ࡭ࠠࡵࡱࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩக") + str(e))
def bstack11l11111l_opy_(bstack1ll1lll11l_opy_):
  global CONFIG
  bstack1lll1ll11_opy_ = bstack1l1ll_opy_ (u"ࠬ࠭஖")
  if not bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ஗") in CONFIG:
    logger.info(bstack1l1ll_opy_ (u"ࠧࡏࡱࠣࡴࡱࡧࡴࡧࡱࡵࡱࡸࠦࡰࡢࡵࡶࡩࡩࠦࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫ࡵࡲࠡࡔࡲࡦࡴࡺࠠࡳࡷࡱࠫ஘"))
  try:
    platform = CONFIG[bstack1l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫங")][bstack1ll1lll11l_opy_]
    if bstack1l1ll_opy_ (u"ࠩࡲࡷࠬச") in platform:
      bstack1lll1ll11_opy_ += str(platform[bstack1l1ll_opy_ (u"ࠪࡳࡸ࠭஛")]) + bstack1l1ll_opy_ (u"ࠫ࠱ࠦࠧஜ")
    if bstack1l1ll_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨ஝") in platform:
      bstack1lll1ll11_opy_ += str(platform[bstack1l1ll_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩஞ")]) + bstack1l1ll_opy_ (u"ࠧ࠭ࠢࠪட")
    if bstack1l1ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬ஠") in platform:
      bstack1lll1ll11_opy_ += str(platform[bstack1l1ll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭஡")]) + bstack1l1ll_opy_ (u"ࠪ࠰ࠥ࠭஢")
    if bstack1l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ண") in platform:
      bstack1lll1ll11_opy_ += str(platform[bstack1l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧத")]) + bstack1l1ll_opy_ (u"࠭ࠬࠡࠩ஥")
    if bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ஦") in platform:
      bstack1lll1ll11_opy_ += str(platform[bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭஧")]) + bstack1l1ll_opy_ (u"ࠩ࠯ࠤࠬந")
    if bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫன") in platform:
      bstack1lll1ll11_opy_ += str(platform[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬப")]) + bstack1l1ll_opy_ (u"ࠬ࠲ࠠࠨ஫")
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"࠭ࡓࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡰࡨࡶࡦࡺࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡹࡴࡳ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡵࡩࡵࡵࡲࡵࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡳࡳ࠭஬") + str(e))
  finally:
    if bstack1lll1ll11_opy_[len(bstack1lll1ll11_opy_) - 2:] == bstack1l1ll_opy_ (u"ࠧ࠭ࠢࠪ஭"):
      bstack1lll1ll11_opy_ = bstack1lll1ll11_opy_[:-2]
    return bstack1lll1ll11_opy_
def bstack11l111l1l_opy_(path, bstack1lll1ll11_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack11l111ll1l_opy_ = ET.parse(path)
    bstack1l1lll1111_opy_ = bstack11l111ll1l_opy_.getroot()
    bstack1l1ll11l_opy_ = None
    for suite in bstack1l1lll1111_opy_.iter(bstack1l1ll_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧம")):
      if bstack1l1ll_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩய") in suite.attrib:
        suite.attrib[bstack1l1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨர")] += bstack1l1ll_opy_ (u"ࠫࠥ࠭ற") + bstack1lll1ll11_opy_
        bstack1l1ll11l_opy_ = suite
    bstack1lll1l1l1_opy_ = None
    for robot in bstack1l1lll1111_opy_.iter(bstack1l1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫல")):
      bstack1lll1l1l1_opy_ = robot
    bstack1l11lll11_opy_ = len(bstack1lll1l1l1_opy_.findall(bstack1l1ll_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬள")))
    if bstack1l11lll11_opy_ == 1:
      bstack1lll1l1l1_opy_.remove(bstack1lll1l1l1_opy_.findall(bstack1l1ll_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ழ"))[0])
      bstack11lll1111l_opy_ = ET.Element(bstack1l1ll_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧவ"), attrib={bstack1l1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧஶ"): bstack1l1ll_opy_ (u"ࠪࡗࡺ࡯ࡴࡦࡵࠪஷ"), bstack1l1ll_opy_ (u"ࠫ࡮ࡪࠧஸ"): bstack1l1ll_opy_ (u"ࠬࡹ࠰ࠨஹ")})
      bstack1lll1l1l1_opy_.insert(1, bstack11lll1111l_opy_)
      bstack11l11l1l11_opy_ = None
      for suite in bstack1lll1l1l1_opy_.iter(bstack1l1ll_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ஺")):
        bstack11l11l1l11_opy_ = suite
      bstack11l11l1l11_opy_.append(bstack1l1ll11l_opy_)
      bstack1l1111ll1l_opy_ = None
      for status in bstack1l1ll11l_opy_.iter(bstack1l1ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ஻")):
        bstack1l1111ll1l_opy_ = status
      bstack11l11l1l11_opy_.append(bstack1l1111ll1l_opy_)
    bstack11l111ll1l_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡸࡳࡪࡰࡪࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹ࠭஼") + str(e))
def bstack11ll1111l1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack11l11111_opy_
  global CONFIG
  if bstack1l1ll_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨ஽") in options:
    del options[bstack1l1ll_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢா")]
  bstack1ll111ll11_opy_ = bstack11ll1l11_opy_()
  for bstack1ll11l1l_opy_ in bstack1ll111ll11_opy_.keys():
    path = os.path.join(os.getcwd(), bstack1l1ll_opy_ (u"ࠫࡵࡧࡢࡰࡶࡢࡶࡪࡹࡵ࡭ࡶࡶࠫி"), str(bstack1ll11l1l_opy_), bstack1l1ll_opy_ (u"ࠬࡵࡵࡵࡲࡸࡸ࠳ࡾ࡭࡭ࠩீ"))
    bstack11l111l1l_opy_(path, bstack11l11111l_opy_(bstack1ll111ll11_opy_[bstack1ll11l1l_opy_]))
  bstack1ll1l111l_opy_()
  return bstack11l11111_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack111l1llll_opy_(self, ff_profile_dir):
  global bstack11111llll_opy_
  if not ff_profile_dir:
    return None
  return bstack11111llll_opy_(self, ff_profile_dir)
def bstack111lllll_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack111ll1l1_opy_
  bstack1111l1lll_opy_ = []
  if bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩு") in CONFIG:
    bstack1111l1lll_opy_ = CONFIG[bstack1l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪூ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1l1ll_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࠤ௃")],
      pabot_args[bstack1l1ll_opy_ (u"ࠤࡹࡩࡷࡨ࡯ࡴࡧࠥ௄")],
      argfile,
      pabot_args.get(bstack1l1ll_opy_ (u"ࠥ࡬࡮ࡼࡥࠣ௅")),
      pabot_args[bstack1l1ll_opy_ (u"ࠦࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠢெ")],
      platform[0],
      bstack111ll1l1_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1l1ll_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡦࡪ࡮ࡨࡷࠧே")] or [(bstack1l1ll_opy_ (u"ࠨࠢை"), None)]
    for platform in enumerate(bstack1111l1lll_opy_)
  ]
def bstack11ll1l1l11_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack11l1l1ll1l_opy_=bstack1l1ll_opy_ (u"ࠧࠨ௉")):
  global bstack11llll111_opy_
  self.platform_index = platform_index
  self.bstack1ll111111l_opy_ = bstack11l1l1ll1l_opy_
  bstack11llll111_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1lll111ll_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1111l11l1_opy_
  global bstack1llll1lll_opy_
  bstack1ll11l111l_opy_ = copy.deepcopy(item)
  if not bstack1l1ll_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪொ") in item.options:
    bstack1ll11l111l_opy_.options[bstack1l1ll_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫோ")] = []
  bstack11l11lll11_opy_ = bstack1ll11l111l_opy_.options[bstack1l1ll_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬௌ")].copy()
  for v in bstack1ll11l111l_opy_.options[bstack1l1ll_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ்࠭")]:
    if bstack1l1ll_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛ࠫ௎") in v:
      bstack11l11lll11_opy_.remove(v)
    if bstack1l1ll_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘ࠭௏") in v:
      bstack11l11lll11_opy_.remove(v)
    if bstack1l1ll_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫௐ") in v:
      bstack11l11lll11_opy_.remove(v)
  bstack11l11lll11_opy_.insert(0, bstack1l1ll_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞࠺ࡼࡿࠪ௑").format(bstack1ll11l111l_opy_.platform_index))
  bstack11l11lll11_opy_.insert(0, bstack1l1ll_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࡀࡻࡾࠩ௒").format(bstack1ll11l111l_opy_.bstack1ll111111l_opy_))
  bstack1ll11l111l_opy_.options[bstack1l1ll_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ௓")] = bstack11l11lll11_opy_
  if bstack1llll1lll_opy_:
    bstack1ll11l111l_opy_.options[bstack1l1ll_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭௔")].insert(0, bstack1l1ll_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗ࠿ࢁࡽࠨ௕").format(bstack1llll1lll_opy_))
  return bstack1111l11l1_opy_(caller_id, datasources, is_last, bstack1ll11l111l_opy_, outs_dir)
def bstack11l11lll_opy_(command, item_index):
  try:
    if bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ௖")):
      os.environ[bstack1l1ll_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨௗ")] = json.dumps(CONFIG[bstack1l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ௘")][item_index % bstack1l1ll1ll_opy_])
    global bstack1llll1lll_opy_
    if bstack1llll1lll_opy_:
      command[0] = command[0].replace(bstack1l1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ௙"), bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡶࡨࡰࠦࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠠ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽࠦࠧ௚") + str(
        item_index) + bstack1l1ll_opy_ (u"ࠫࠥ࠭௛") + bstack1llll1lll_opy_, 1)
    else:
      command[0] = command[0].replace(bstack1l1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ௜"),
                                      bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡹࡤ࡬ࠢࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠣ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠢࠪ௝") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack1l1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦ࡭ࡰࡦ࡬ࡪࡾ࡯࡮ࡨࠢࡦࡳࡲࡳࡡ࡯ࡦࠣࡪࡴࡸࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰ࠽ࠤࢀࢃࠧ௞").format(str(e)))
def bstack1l111ll1ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack11111l11l_opy_
  try:
    bstack11l11lll_opy_(command, item_index)
    return bstack11111l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack1l1ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࡀࠠࡼࡿࠪ௟").format(str(e)))
    raise e
def bstack11l111l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack11111l11l_opy_
  try:
    bstack11l11lll_opy_(command, item_index)
    return bstack11111l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack1l1ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴࠠ࠳࠰࠴࠷࠿ࠦࡻࡾࠩ௠").format(str(e)))
    try:
      return bstack11111l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack1l1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤ࠷࠴࠱࠴ࠢࡩࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠨ௡").format(str(e2)))
      raise e
def bstack1l11l11l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack11111l11l_opy_
  try:
    bstack11l11lll_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack11111l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack1l1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯ࠢ࠵࠲࠶࠻࠺ࠡࡽࢀࠫ௢").format(str(e)))
    try:
      return bstack11111l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack1l1ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦ࠲࠯࠳࠸ࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪ௣").format(str(e2)))
      raise e
def bstack1ll11l11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11111l11l_opy_
  try:
    bstack11l11lll_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      import time
      time.sleep(min(sleep_before_start, 5))
    return bstack11111l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1l1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱࠤ࠹࠴࠲࠻ࠢࡾࢁࠬ௤").format(str(e)))
    try:
      return bstack11111l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1l1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡨࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠧ௥").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack11llll1l1_opy_(self, runner, quiet=False, capture=True):
  global bstack1l111ll11_opy_
  bstack11ll11ll_opy_ = bstack1l111ll11_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack1l1ll_opy_ (u"ࠨࡧࡻࡧࡪࡶࡴࡪࡱࡱࡣࡦࡸࡲࠨ௦")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1l1ll_opy_ (u"ࠩࡨࡼࡨࡥࡴࡳࡣࡦࡩࡧࡧࡣ࡬ࡡࡤࡶࡷ࠭௧")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack11ll11ll_opy_
def bstack11l111l1l1_opy_(runner, hook_name, context, element, bstack1111l1111_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack11llll1ll1_opy_.bstack1l1llll11_opy_(hook_name, element)
    bstack1111l1111_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack11llll1ll1_opy_.bstack1111lll1l_opy_(element)
      if hook_name not in [bstack1l1ll_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠧ௨"), bstack1l1ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧ௩")] and args and hasattr(args[0], bstack1l1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡣࡲ࡫ࡳࡴࡣࡪࡩࠬ௪")):
        args[0].error_message = bstack1l1ll_opy_ (u"࠭ࠧ௫")
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣ࡬ࡦࡴࡤ࡭ࡧࠣ࡬ࡴࡵ࡫ࡴࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩ࠿ࠦࡻࡾࠩ௬").format(str(e)))
@measure(event_name=EVENTS.bstack1ll111111_opy_, stage=STAGE.bstack11ll1l11ll_opy_, hook_type=bstack1l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡂ࡮࡯ࠦ௭"), bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1lll11ll1l_opy_(runner, name, context, bstack1111l1111_opy_, *args):
    if runner.hooks.get(bstack1l1ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨ௮")).__name__ != bstack1l1ll_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲ࡟ࡥࡧࡩࡥࡺࡲࡴࡠࡪࡲࡳࡰࠨ௯"):
      bstack11l111l1l1_opy_(runner, name, context, runner, bstack1111l1111_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack111l1l1l_opy_(bstack1l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ௰")) else context.browser
      runner.driver_initialised = bstack1l1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤ௱")
    except Exception as e:
      logger.debug(bstack1l1ll_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡤࡳ࡫ࡹࡩࡷࠦࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡧࠣࡥࡹࡺࡲࡪࡤࡸࡸࡪࡀࠠࡼࡿࠪ௲").format(str(e)))
def bstack1l11l1l1l1_opy_(runner, name, context, bstack1111l1111_opy_, *args):
    bstack11l111l1l1_opy_(runner, name, context, context.feature, bstack1111l1111_opy_, *args)
    try:
      if not bstack111ll111l_opy_:
        bstack1ll1l1llll_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1l1l_opy_(bstack1l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭௳")) else context.browser
        if is_driver_active(bstack1ll1l1llll_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack1l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤ௴")
          bstack11lll1lll_opy_ = str(runner.feature.name)
          bstack1ll11111l1_opy_(context, bstack11lll1lll_opy_)
          bstack1ll1l1llll_opy_.execute_script(bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧ௵") + json.dumps(bstack11lll1lll_opy_) + bstack1l1ll_opy_ (u"ࠪࢁࢂ࠭௶"))
    except Exception as e:
      logger.debug(bstack1l1ll_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫ௷").format(str(e)))
def bstack1l111l1ll1_opy_(runner, name, context, bstack1111l1111_opy_, *args):
    if hasattr(context, bstack1l1ll_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧ௸")):
        bstack11llll1ll1_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack1l1ll_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ௹")) else context.feature
    bstack11l111l1l1_opy_(runner, name, context, target, bstack1111l1111_opy_, *args)
@measure(event_name=EVENTS.bstack1ll11ll11l_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack11l11ll11_opy_(runner, name, context, bstack1111l1111_opy_, *args):
    if len(context.scenario.tags) == 0: bstack11llll1ll1_opy_.start_test(context)
    bstack11l111l1l1_opy_(runner, name, context, context.scenario, bstack1111l1111_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1lll1lll1l_opy_.bstack1l1ll1l1ll_opy_(context, *args)
    try:
      bstack1ll1l1llll_opy_ = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭௺"), context.browser)
      if is_driver_active(bstack1ll1l1llll_opy_):
        bstack11ll1ll1_opy_.bstack1l1111l111_opy_(bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ௻"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack1l1ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦ௼")
        if (not bstack111ll111l_opy_):
          scenario_name = args[0].name
          feature_name = bstack11lll1lll_opy_ = str(runner.feature.name)
          bstack11lll1lll_opy_ = feature_name + bstack1l1ll_opy_ (u"ࠪࠤ࠲ࠦࠧ௽") + scenario_name
          if runner.driver_initialised == bstack1l1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ௾"):
            bstack1ll11111l1_opy_(context, bstack11lll1lll_opy_)
            bstack1ll1l1llll_opy_.execute_script(bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪ௿") + json.dumps(bstack11lll1lll_opy_) + bstack1l1ll_opy_ (u"࠭ࡽࡾࠩఀ"))
    except Exception as e:
      logger.debug(bstack1l1ll_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡪࡴࡡࡳ࡫ࡲ࠾ࠥࢁࡽࠨఁ").format(str(e)))
@measure(event_name=EVENTS.bstack1ll111111_opy_, stage=STAGE.bstack11ll1l11ll_opy_, hook_type=bstack1l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡔࡶࡨࡴࠧం"), bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1l111l111_opy_(runner, name, context, bstack1111l1111_opy_, *args):
    bstack11l111l1l1_opy_(runner, name, context, args[0], bstack1111l1111_opy_, *args)
    try:
      bstack1ll1l1llll_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1l1l_opy_(bstack1l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨః")) else context.browser
      if is_driver_active(bstack1ll1l1llll_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack1l1ll_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣఄ")
        bstack11llll1ll1_opy_.bstack111l1ll1_opy_(args[0])
        if runner.driver_initialised == bstack1l1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤఅ"):
          feature_name = bstack11lll1lll_opy_ = str(runner.feature.name)
          bstack11lll1lll_opy_ = feature_name + bstack1l1ll_opy_ (u"ࠬࠦ࠭ࠡࠩఆ") + context.scenario.name
          bstack1ll1l1llll_opy_.execute_script(bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫఇ") + json.dumps(bstack11lll1lll_opy_) + bstack1l1ll_opy_ (u"ࠧࡾࡿࠪఈ"))
    except Exception as e:
      logger.debug(bstack1l1ll_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡹ࡫ࡰ࠻ࠢࡾࢁࠬఉ").format(str(e)))
@measure(event_name=EVENTS.bstack1ll111111_opy_, stage=STAGE.bstack11ll1l11ll_opy_, hook_type=bstack1l1ll_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࡔࡶࡨࡴࠧఊ"), bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1l11llll_opy_(runner, name, context, bstack1111l1111_opy_, *args):
  bstack11llll1ll1_opy_.bstack1ll11ll11_opy_(args[0])
  try:
    bstack11l1ll11ll_opy_ = args[0].status.name
    bstack1ll1l1llll_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩఋ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack1ll1l1llll_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack1l1ll_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫఌ")
        feature_name = bstack11lll1lll_opy_ = str(runner.feature.name)
        bstack11lll1lll_opy_ = feature_name + bstack1l1ll_opy_ (u"ࠬࠦ࠭ࠡࠩ఍") + context.scenario.name
        bstack1ll1l1llll_opy_.execute_script(bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫఎ") + json.dumps(bstack11lll1lll_opy_) + bstack1l1ll_opy_ (u"ࠧࡾࡿࠪఏ"))
    if str(bstack11l1ll11ll_opy_).lower() == bstack1l1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨఐ"):
      bstack1l1l11ll_opy_ = bstack1l1ll_opy_ (u"ࠩࠪ఑")
      bstack1l11ll1l_opy_ = bstack1l1ll_opy_ (u"ࠪࠫఒ")
      bstack11l1ll1l1l_opy_ = bstack1l1ll_opy_ (u"ࠫࠬఓ")
      try:
        import traceback
        bstack1l1l11ll_opy_ = runner.exception.__class__.__name__
        bstack11l11l111l_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1l11ll1l_opy_ = bstack1l1ll_opy_ (u"ࠬࠦࠧఔ").join(bstack11l11l111l_opy_)
        bstack11l1ll1l1l_opy_ = bstack11l11l111l_opy_[-1]
      except Exception as e:
        logger.debug(bstack1lllll1ll_opy_.format(str(e)))
      bstack1l1l11ll_opy_ += bstack11l1ll1l1l_opy_
      bstack11l111l1ll_opy_(context, json.dumps(str(args[0].name) + bstack1l1ll_opy_ (u"ࠨࠠ࠮ࠢࡉࡥ࡮ࡲࡥࡥࠣ࡟ࡲࠧక") + str(bstack1l11ll1l_opy_)),
                          bstack1l1ll_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨఖ"))
      if runner.driver_initialised == bstack1l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨగ"):
        bstack1111l1ll_opy_(getattr(context, bstack1l1ll_opy_ (u"ࠩࡳࡥ࡬࡫ࠧఘ"), None), bstack1l1ll_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥఙ"), bstack1l1l11ll_opy_)
        bstack1ll1l1llll_opy_.execute_script(bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩచ") + json.dumps(str(args[0].name) + bstack1l1ll_opy_ (u"ࠧࠦ࠭ࠡࡈࡤ࡭ࡱ࡫ࡤࠢ࡞ࡱࠦఛ") + str(bstack1l11ll1l_opy_)) + bstack1l1ll_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭జ"))
      if runner.driver_initialised == bstack1l1ll_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧఝ"):
        bstack1l1l111l1_opy_(bstack1ll1l1llll_opy_, bstack1l1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨఞ"), bstack1l1ll_opy_ (u"ࠤࡖࡧࡪࡴࡡࡳ࡫ࡲࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨట") + str(bstack1l1l11ll_opy_))
    else:
      bstack11l111l1ll_opy_(context, bstack1l1ll_opy_ (u"ࠥࡔࡦࡹࡳࡦࡦࠤࠦఠ"), bstack1l1ll_opy_ (u"ࠦ࡮ࡴࡦࡰࠤడ"))
      if runner.driver_initialised == bstack1l1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥఢ"):
        bstack1111l1ll_opy_(getattr(context, bstack1l1ll_opy_ (u"࠭ࡰࡢࡩࡨࠫణ"), None), bstack1l1ll_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢత"))
      bstack1ll1l1llll_opy_.execute_script(bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭థ") + json.dumps(str(args[0].name) + bstack1l1ll_opy_ (u"ࠤࠣ࠱ࠥࡖࡡࡴࡵࡨࡨࠦࠨద")) + bstack1l1ll_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩధ"))
      if runner.driver_initialised == bstack1l1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤన"):
        bstack1l1l111l1_opy_(bstack1ll1l1llll_opy_, bstack1l1ll_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ఩"))
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣࡷࡹ࡫ࡰ࠻ࠢࡾࢁࠬప").format(str(e)))
  bstack11l111l1l1_opy_(runner, name, context, args[0], bstack1111l1111_opy_, *args)
@measure(event_name=EVENTS.bstack111lll1l1_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1111ll1l_opy_(runner, name, context, bstack1111l1111_opy_, *args):
  bstack11llll1ll1_opy_.end_test(args[0])
  try:
    bstack1l111111ll_opy_ = args[0].status.name
    bstack1ll1l1llll_opy_ = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ఫ"), context.browser)
    bstack1lll1lll1l_opy_.bstack1l1l11l1l_opy_(bstack1ll1l1llll_opy_)
    if str(bstack1l111111ll_opy_).lower() == bstack1l1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨబ"):
      bstack1l1l11ll_opy_ = bstack1l1ll_opy_ (u"ࠩࠪభ")
      bstack1l11ll1l_opy_ = bstack1l1ll_opy_ (u"ࠪࠫమ")
      bstack11l1ll1l1l_opy_ = bstack1l1ll_opy_ (u"ࠫࠬయ")
      try:
        import traceback
        bstack1l1l11ll_opy_ = runner.exception.__class__.__name__
        bstack11l11l111l_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1l11ll1l_opy_ = bstack1l1ll_opy_ (u"ࠬࠦࠧర").join(bstack11l11l111l_opy_)
        bstack11l1ll1l1l_opy_ = bstack11l11l111l_opy_[-1]
      except Exception as e:
        logger.debug(bstack1lllll1ll_opy_.format(str(e)))
      bstack1l1l11ll_opy_ += bstack11l1ll1l1l_opy_
      bstack11l111l1ll_opy_(context, json.dumps(str(args[0].name) + bstack1l1ll_opy_ (u"ࠨࠠ࠮ࠢࡉࡥ࡮ࡲࡥࡥࠣ࡟ࡲࠧఱ") + str(bstack1l11ll1l_opy_)),
                          bstack1l1ll_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨల"))
      if runner.driver_initialised == bstack1l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥళ") or runner.driver_initialised == bstack1l1ll_opy_ (u"ࠩ࡬ࡲࡸࡺࡥࡱࠩఴ"):
        bstack1111l1ll_opy_(getattr(context, bstack1l1ll_opy_ (u"ࠪࡴࡦ࡭ࡥࠨవ"), None), bstack1l1ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦశ"), bstack1l1l11ll_opy_)
        bstack1ll1l1llll_opy_.execute_script(bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪష") + json.dumps(str(args[0].name) + bstack1l1ll_opy_ (u"ࠨࠠ࠮ࠢࡉࡥ࡮ࡲࡥࡥࠣ࡟ࡲࠧస") + str(bstack1l11ll1l_opy_)) + bstack1l1ll_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧహ"))
      if runner.driver_initialised == bstack1l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥ఺") or runner.driver_initialised == bstack1l1ll_opy_ (u"ࠩ࡬ࡲࡸࡺࡥࡱࠩ఻"):
        bstack1l1l111l1_opy_(bstack1ll1l1llll_opy_, bstack1l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦ఼ࠪ"), bstack1l1ll_opy_ (u"ࠦࡘࡩࡥ࡯ࡣࡵ࡭ࡴࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣఽ") + str(bstack1l1l11ll_opy_))
    else:
      bstack11l111l1ll_opy_(context, bstack1l1ll_opy_ (u"ࠧࡖࡡࡴࡵࡨࡨࠦࠨా"), bstack1l1ll_opy_ (u"ࠨࡩ࡯ࡨࡲࠦి"))
      if runner.driver_initialised == bstack1l1ll_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤీ") or runner.driver_initialised == bstack1l1ll_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨు"):
        bstack1111l1ll_opy_(getattr(context, bstack1l1ll_opy_ (u"ࠩࡳࡥ࡬࡫ࠧూ"), None), bstack1l1ll_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥృ"))
      bstack1ll1l1llll_opy_.execute_script(bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩౄ") + json.dumps(str(args[0].name) + bstack1l1ll_opy_ (u"ࠧࠦ࠭ࠡࡒࡤࡷࡸ࡫ࡤࠢࠤ౅")) + bstack1l1ll_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬె"))
      if runner.driver_initialised == bstack1l1ll_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤే") or runner.driver_initialised == bstack1l1ll_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨై"):
        bstack1l1l111l1_opy_(bstack1ll1l1llll_opy_, bstack1l1ll_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ౉"))
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡧࡧࡤࡸࡺࡸࡥ࠻ࠢࡾࢁࠬొ").format(str(e)))
  bstack11l111l1l1_opy_(runner, name, context, context.scenario, bstack1111l1111_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack11lll1ll_opy_(runner, name, context, bstack1111l1111_opy_, *args):
    target = context.scenario if hasattr(context, bstack1l1ll_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ో")) else context.feature
    bstack11l111l1l1_opy_(runner, name, context, target, bstack1111l1111_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack11l1ll11l1_opy_(runner, name, context, bstack1111l1111_opy_, *args):
    try:
      bstack1ll1l1llll_opy_ = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫౌ"), context.browser)
      bstack11lll111l_opy_ = bstack1l1ll_opy_ (u"్࠭ࠧ")
      if context.failed is True:
        bstack1lll1l1ll1_opy_ = []
        bstack1lll11111_opy_ = []
        bstack11l11ll1_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1lll1l1ll1_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11l11l111l_opy_ = traceback.format_tb(exc_tb)
            bstack1l11l11l_opy_ = bstack1l1ll_opy_ (u"ࠧࠡࠩ౎").join(bstack11l11l111l_opy_)
            bstack1lll11111_opy_.append(bstack1l11l11l_opy_)
            bstack11l11ll1_opy_.append(bstack11l11l111l_opy_[-1])
        except Exception as e:
          logger.debug(bstack1lllll1ll_opy_.format(str(e)))
        bstack1l1l11ll_opy_ = bstack1l1ll_opy_ (u"ࠨࠩ౏")
        for i in range(len(bstack1lll1l1ll1_opy_)):
          bstack1l1l11ll_opy_ += bstack1lll1l1ll1_opy_[i] + bstack11l11ll1_opy_[i] + bstack1l1ll_opy_ (u"ࠩ࡟ࡲࠬ౐")
        bstack11lll111l_opy_ = bstack1l1ll_opy_ (u"ࠪࠤࠬ౑").join(bstack1lll11111_opy_)
        if runner.driver_initialised in [bstack1l1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧ౒"), bstack1l1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤ౓")]:
          bstack11l111l1ll_opy_(context, bstack11lll111l_opy_, bstack1l1ll_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧ౔"))
          bstack1111l1ll_opy_(getattr(context, bstack1l1ll_opy_ (u"ࠧࡱࡣࡪࡩౕࠬ"), None), bstack1l1ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤౖࠣ"), bstack1l1l11ll_opy_)
          bstack1ll1l1llll_opy_.execute_script(bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ౗") + json.dumps(bstack11lll111l_opy_) + bstack1l1ll_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪౘ"))
          bstack1l1l111l1_opy_(bstack1ll1l1llll_opy_, bstack1l1ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦౙ"), bstack1l1ll_opy_ (u"࡙ࠧ࡯࡮ࡧࠣࡷࡨ࡫࡮ࡢࡴ࡬ࡳࡸࠦࡦࡢ࡫࡯ࡩࡩࡀࠠ࡝ࡰࠥౚ") + str(bstack1l1l11ll_opy_))
          bstack1l111l1l_opy_ = bstack1l1l1l1l11_opy_(bstack11lll111l_opy_, runner.feature.name, logger)
          if (bstack1l111l1l_opy_ != None):
            bstack1ll1l11lll_opy_.append(bstack1l111l1l_opy_)
      else:
        if runner.driver_initialised in [bstack1l1ll_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠢ౛"), bstack1l1ll_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦ౜")]:
          bstack11l111l1ll_opy_(context, bstack1l1ll_opy_ (u"ࠣࡈࡨࡥࡹࡻࡲࡦ࠼ࠣࠦౝ") + str(runner.feature.name) + bstack1l1ll_opy_ (u"ࠤࠣࡴࡦࡹࡳࡦࡦࠤࠦ౞"), bstack1l1ll_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣ౟"))
          bstack1111l1ll_opy_(getattr(context, bstack1l1ll_opy_ (u"ࠫࡵࡧࡧࡦࠩౠ"), None), bstack1l1ll_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧౡ"))
          bstack1ll1l1llll_opy_.execute_script(bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫౢ") + json.dumps(bstack1l1ll_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥ࠻ࠢࠥౣ") + str(runner.feature.name) + bstack1l1ll_opy_ (u"ࠣࠢࡳࡥࡸࡹࡥࡥࠣࠥ౤")) + bstack1l1ll_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧࢃࡽࠨ౥"))
          bstack1l1l111l1_opy_(bstack1ll1l1llll_opy_, bstack1l1ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ౦"))
          bstack1l111l1l_opy_ = bstack1l1l1l1l11_opy_(bstack11lll111l_opy_, runner.feature.name, logger)
          if (bstack1l111l1l_opy_ != None):
            bstack1ll1l11lll_opy_.append(bstack1l111l1l_opy_)
    except Exception as e:
      logger.debug(bstack1l1ll_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠ࡮ࡣࡵ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡩ࡯ࠢࡤࡪࡹ࡫ࡲࠡࡨࡨࡥࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭౧").format(str(e)))
    bstack11l111l1l1_opy_(runner, name, context, context.feature, bstack1111l1111_opy_, *args)
@measure(event_name=EVENTS.bstack1ll111111_opy_, stage=STAGE.bstack11ll1l11ll_opy_, hook_type=bstack1l1ll_opy_ (u"ࠧࡧࡦࡵࡧࡵࡅࡱࡲࠢ౨"), bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1l1lllll1_opy_(runner, name, context, bstack1111l1111_opy_, *args):
    bstack11l111l1l1_opy_(runner, name, context, runner, bstack1111l1111_opy_, *args)
def bstack1l11ll1lll_opy_(self, name, context, *args):
  try:
    if bstack1ll1l111ll_opy_:
      platform_index = int(threading.current_thread()._name) % bstack1l1ll1ll_opy_
      bstack1l1111l1l_opy_ = CONFIG[bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ౩")][platform_index]
      os.environ[bstack1l1ll_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨ౪")] = json.dumps(bstack1l1111l1l_opy_)
    global bstack1111l1111_opy_
    if not hasattr(self, bstack1l1ll_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡩࡩ࠭౫")):
      self.driver_initialised = None
    bstack1l1l11111l_opy_ = {
        bstack1l1ll_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱ࠭౬"): bstack1lll11ll1l_opy_,
        bstack1l1ll_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠫ౭"): bstack1l11l1l1l1_opy_,
        bstack1l1ll_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡹࡧࡧࠨ౮"): bstack1l111l1ll1_opy_,
        bstack1l1ll_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠧ౯"): bstack11l11ll11_opy_,
        bstack1l1ll_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠫ౰"): bstack1l111l111_opy_,
        bstack1l1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡵࡧࡳࠫ౱"): bstack1l11llll_opy_,
        bstack1l1ll_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩ౲"): bstack1111ll1l_opy_,
        bstack1l1ll_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡶࡤ࡫ࠬ౳"): bstack11lll1ll_opy_,
        bstack1l1ll_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪ౴"): bstack11l1ll11l1_opy_,
        bstack1l1ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧ౵"): bstack1l1lllll1_opy_
    }
    handler = bstack1l1l11111l_opy_.get(name, bstack1111l1111_opy_)
    try:
      handler(self, name, context, bstack1111l1111_opy_, *args)
    except Exception as e:
      logger.debug(bstack1l1ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡩࡱࡲ࡯ࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࠦࡻࡾ࠼ࠣࡿࢂ࠭౶").format(name, str(e)))
    if name in [bstack1l1ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭౷"), bstack1l1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ౸"), bstack1l1ll_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫ౹")]:
      try:
        bstack1ll1l1llll_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1l1l_opy_(bstack1l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ౺")) else context.browser
        bstack11l1llll1l_opy_ = (
          (name == bstack1l1ll_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡤࡰࡱ࠭౻") and self.driver_initialised == bstack1l1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣ౼")) or
          (name == bstack1l1ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣ࡫࡫ࡡࡵࡷࡵࡩࠬ౽") and self.driver_initialised == bstack1l1ll_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠢ౾")) or
          (name == bstack1l1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ౿") and self.driver_initialised in [bstack1l1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥಀ"), bstack1l1ll_opy_ (u"ࠤ࡬ࡲࡸࡺࡥࡱࠤಁ")]) or
          (name == bstack1l1ll_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡸࡪࡶࠧಂ") and self.driver_initialised == bstack1l1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤಃ"))
        )
        if bstack11l1llll1l_opy_:
          self.driver_initialised = None
          if bstack1ll1l1llll_opy_ and hasattr(bstack1ll1l1llll_opy_, bstack1l1ll_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩ಄")):
            try:
              bstack1ll1l1llll_opy_.quit()
            except Exception as e:
              logger.debug(bstack1l1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡷࡵࡪࡶࡷ࡭ࡳ࡭ࠠࡥࡴ࡬ࡺࡪࡸࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧࠣ࡬ࡴࡵ࡫࠻ࠢࡾࢁࠬಅ").format(str(e)))
      except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡤࡪࡹ࡫ࡲࠡࡪࡲࡳࡰࠦࡣ࡭ࡧࡤࡲࡺࡶࠠࡧࡱࡵࠤࢀࢃ࠺ࠡࡽࢀࠫಆ").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠨࡅࡵ࡭ࡹ࡯ࡣࡢ࡮ࠣࡩࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩࠥࡸࡵ࡯ࠢ࡫ࡳࡴࡱࠠࡼࡿ࠽ࠤࢀࢃࠧಇ").format(name, str(e)))
    try:
      bstack1111l1111_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack1l1ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࠦ࡯ࡳ࡫ࡪ࡭ࡳࡧ࡬ࠡࡤࡨ࡬ࡦࡼࡥࠡࡪࡲࡳࡰࠦࡻࡾ࠼ࠣࡿࢂ࠭ಈ").format(name, str(e2)))
def bstack1ll1l1l1ll_opy_(config, startdir):
  return bstack1l1ll_opy_ (u"ࠥࡨࡷ࡯ࡶࡦࡴ࠽ࠤࢀ࠶ࡽࠣಉ").format(bstack1l1ll_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥಊ"))
notset = Notset()
def bstack1l11l1l1ll_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1l1111l1ll_opy_
  if str(name).lower() == bstack1l1ll_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࠬಋ"):
    return bstack1l1ll_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧಌ")
  else:
    return bstack1l1111l1ll_opy_(self, name, default, skip)
def bstack111lllll1_opy_(item, when):
  global bstack11ll1111l_opy_
  try:
    bstack11ll1111l_opy_(item, when)
  except Exception as e:
    pass
def bstack1l11l11ll1_opy_():
  return
def bstack1l1ll11lll_opy_(type, name, status, reason, bstack1l1ll1ll11_opy_, bstack1l111l1l1l_opy_):
  bstack1l11l1l111_opy_ = {
    bstack1l1ll_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ಍"): type,
    bstack1l1ll_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫಎ"): {}
  }
  if type == bstack1l1ll_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫಏ"):
    bstack1l11l1l111_opy_[bstack1l1ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ಐ")][bstack1l1ll_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ಑")] = bstack1l1ll1ll11_opy_
    bstack1l11l1l111_opy_[bstack1l1ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨಒ")][bstack1l1ll_opy_ (u"࠭ࡤࡢࡶࡤࠫಓ")] = json.dumps(str(bstack1l111l1l1l_opy_))
  if type == bstack1l1ll_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨಔ"):
    bstack1l11l1l111_opy_[bstack1l1ll_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫಕ")][bstack1l1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧಖ")] = name
  if type == bstack1l1ll_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ಗ"):
    bstack1l11l1l111_opy_[bstack1l1ll_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧಘ")][bstack1l1ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬಙ")] = status
    if status == bstack1l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ಚ"):
      bstack1l11l1l111_opy_[bstack1l1ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪಛ")][bstack1l1ll_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨಜ")] = json.dumps(str(reason))
  bstack1l1lll111_opy_ = bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧಝ").format(json.dumps(bstack1l11l1l111_opy_))
  return bstack1l1lll111_opy_
def bstack11111ll11_opy_(driver_command, response):
    if driver_command == bstack1l1ll_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠧಞ"):
        bstack11ll1ll1_opy_.bstack1l11ll1ll1_opy_({
            bstack1l1ll_opy_ (u"ࠫ࡮ࡳࡡࡨࡧࠪಟ"): response[bstack1l1ll_opy_ (u"ࠬࡼࡡ࡭ࡷࡨࠫಠ")],
            bstack1l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ಡ"): bstack11ll1ll1_opy_.current_test_uuid()
        })
def bstack111111111_opy_(item, call, rep):
  global bstack11ll1lll_opy_
  global bstack1lllllll1_opy_
  global bstack111ll111l_opy_
  name = bstack1l1ll_opy_ (u"ࠧࠨಢ")
  try:
    if rep.when == bstack1l1ll_opy_ (u"ࠨࡥࡤࡰࡱ࠭ಣ"):
      bstack1lllll11ll_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack111ll111l_opy_:
          name = str(rep.nodeid)
          bstack1l11111ll_opy_ = bstack1l1ll11lll_opy_(bstack1l1ll_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪತ"), name, bstack1l1ll_opy_ (u"ࠪࠫಥ"), bstack1l1ll_opy_ (u"ࠫࠬದ"), bstack1l1ll_opy_ (u"ࠬ࠭ಧ"), bstack1l1ll_opy_ (u"࠭ࠧನ"))
          threading.current_thread().bstack11ll11111l_opy_ = name
          for driver in bstack1lllllll1_opy_:
            if bstack1lllll11ll_opy_ == driver.session_id:
              driver.execute_script(bstack1l11111ll_opy_)
      except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧ಩").format(str(e)))
      try:
        bstack1l111l1111_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1l1ll_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩಪ"):
          status = bstack1l1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩಫ") if rep.outcome.lower() == bstack1l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪಬ") else bstack1l1ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫಭ")
          reason = bstack1l1ll_opy_ (u"ࠬ࠭ಮ")
          if status == bstack1l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ಯ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1l1ll_opy_ (u"ࠧࡪࡰࡩࡳࠬರ") if status == bstack1l1ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨಱ") else bstack1l1ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨಲ")
          data = name + bstack1l1ll_opy_ (u"ࠪࠤࡵࡧࡳࡴࡧࡧࠥࠬಳ") if status == bstack1l1ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ಴") else name + bstack1l1ll_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩࠧࠠࠨವ") + reason
          bstack1l1l11l11l_opy_ = bstack1l1ll11lll_opy_(bstack1l1ll_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨಶ"), bstack1l1ll_opy_ (u"ࠧࠨಷ"), bstack1l1ll_opy_ (u"ࠨࠩಸ"), bstack1l1ll_opy_ (u"ࠩࠪಹ"), level, data)
          for driver in bstack1lllllll1_opy_:
            if bstack1lllll11ll_opy_ == driver.session_id:
              driver.execute_script(bstack1l1l11l11l_opy_)
      except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡤࡱࡱࡸࡪࡾࡴࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧ಺").format(str(e)))
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡶࡤࡸࡪࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࢁࡽࠨ಻").format(str(e)))
  bstack11ll1lll_opy_(item, call, rep)
def bstack1ll1ll1l11_opy_(driver, bstack1llll11l_opy_, test=None):
  global bstack11ll1ll111_opy_
  if test != None:
    bstack1l111l11l1_opy_ = getattr(test, bstack1l1ll_opy_ (u"ࠬࡴࡡ࡮ࡧ಼ࠪ"), None)
    bstack11l11l11_opy_ = getattr(test, bstack1l1ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫಽ"), None)
    PercySDK.screenshot(driver, bstack1llll11l_opy_, bstack1l111l11l1_opy_=bstack1l111l11l1_opy_, bstack11l11l11_opy_=bstack11l11l11_opy_, bstack1l1l11ll11_opy_=bstack11ll1ll111_opy_)
  else:
    PercySDK.screenshot(driver, bstack1llll11l_opy_)
@measure(event_name=EVENTS.bstack11l11ll111_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1llll1ll_opy_(driver):
  if bstack1l11111l_opy_.bstack11ll11l1_opy_() is True or bstack1l11111l_opy_.capturing() is True:
    return
  bstack1l11111l_opy_.bstack1111l111_opy_()
  while not bstack1l11111l_opy_.bstack11ll11l1_opy_():
    bstack11l11l11l_opy_ = bstack1l11111l_opy_.bstack11l111ll1_opy_()
    bstack1ll1ll1l11_opy_(driver, bstack11l11l11l_opy_)
  bstack1l11111l_opy_.bstack1lll1ll1l1_opy_()
def bstack1l1l111l_opy_(sequence, driver_command, response = None, bstack111l1l1l1_opy_ = None, args = None):
    try:
      if sequence != bstack1l1ll_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧಾ"):
        return
      if percy.bstack1111ll1ll_opy_() == bstack1l1ll_opy_ (u"ࠣࡨࡤࡰࡸ࡫ࠢಿ"):
        return
      bstack11l11l11l_opy_ = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬೀ"), None)
      for command in bstack1llllllll_opy_:
        if command == driver_command:
          with bstack1lllll11l_opy_:
            bstack1llll1111_opy_ = bstack1lllllll1_opy_.copy()
          for driver in bstack1llll1111_opy_:
            bstack1llll1ll_opy_(driver)
      bstack11l111l11_opy_ = percy.bstack11ll1ll1l_opy_()
      if driver_command in bstack1l11l11ll_opy_[bstack11l111l11_opy_]:
        bstack1l11111l_opy_.bstack11llll1l1l_opy_(bstack11l11l11l_opy_, driver_command)
    except Exception as e:
      pass
def bstack11llllll_opy_(framework_name):
  if bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡱࡴࡪ࡟ࡤࡣ࡯ࡰࡪࡪࠧು")):
      return
  bstack11l1lll1_opy_.bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡲࡵࡤࡠࡥࡤࡰࡱ࡫ࡤࠨೂ"), True)
  global bstack111llll11_opy_
  global bstack1lll1l1111_opy_
  global bstack111ll11ll_opy_
  bstack111llll11_opy_ = framework_name
  logger.info(bstack1ll1l1ll1_opy_.format(bstack111llll11_opy_.split(bstack1l1ll_opy_ (u"ࠬ࠳ࠧೃ"))[0]))
  bstack11ll1111_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1ll1l111ll_opy_:
      Service.start = bstack1lll11l1_opy_
      Service.stop = bstack1l1l1lll11_opy_
      webdriver.Remote.get = bstack1l11ll11ll_opy_
      WebDriver.quit = bstack1lll1llll_opy_
      webdriver.Remote.__init__ = bstack1l1l111lll_opy_
    if not bstack1ll1l111ll_opy_:
        webdriver.Remote.__init__ = bstack1ll1lll1l_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack1ll11l1l1_opy_
    bstack1lll1l1111_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1ll1l111ll_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1ll1111l11_opy_
  except Exception as e:
    pass
  bstack1l111lll11_opy_()
  if not bstack1lll1l1111_opy_:
    bstack1111l1l11_opy_(bstack1l1ll_opy_ (u"ࠨࡐࡢࡥ࡮ࡥ࡬࡫ࡳࠡࡰࡲࡸࠥ࡯࡮ࡴࡶࡤࡰࡱ࡫ࡤࠣೄ"), bstack11l111lll1_opy_)
  if bstack111l1l1ll_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack1l1ll_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ೅")) and callable(getattr(RemoteConnection, bstack1l1ll_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩೆ"))):
        RemoteConnection._get_proxy_url = bstack111ll11l1_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack111ll11l1_opy_
    except Exception as e:
      logger.error(bstack11l1l1l1l_opy_.format(str(e)))
  if bstack1l1ll1l1l1_opy_():
    bstack11lllllll_opy_(CONFIG, logger)
  if (bstack1l1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨೇ") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1111ll1ll_opy_() == bstack1l1ll_opy_ (u"ࠥࡸࡷࡻࡥࠣೈ"):
          bstack1l11ll111_opy_(bstack1l1l111l_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack111l1llll_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1l111l1l11_opy_
      except Exception as e:
        logger.warn(bstack1ll1ll11l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1l1l1l11l1_opy_
      except Exception as e:
        logger.debug(bstack1111ll111_opy_ + str(e))
    except Exception as e:
      bstack1111l1l11_opy_(e, bstack1ll1ll11l_opy_)
    Output.start_test = bstack11llllll1l_opy_
    Output.end_test = bstack1lll11l1l_opy_
    TestStatus.__init__ = bstack1111l11ll_opy_
    QueueItem.__init__ = bstack11ll1l1l11_opy_
    pabot._create_items = bstack111lllll_opy_
    try:
      from pabot import __version__ as bstack1ll1l1ll_opy_
      if version.parse(bstack1ll1l1ll_opy_) >= version.parse(bstack1l1ll_opy_ (u"ࠫ࠹࠴࠲࠯࠲ࠪ೉")):
        pabot._run = bstack1ll11l11ll_opy_
      elif version.parse(bstack1ll1l1ll_opy_) >= version.parse(bstack1l1ll_opy_ (u"ࠬ࠸࠮࠲࠷࠱࠴ࠬೊ")):
        pabot._run = bstack1l11l11l1_opy_
      elif version.parse(bstack1ll1l1ll_opy_) >= version.parse(bstack1l1ll_opy_ (u"࠭࠲࠯࠳࠶࠲࠵࠭ೋ")):
        pabot._run = bstack11l111l1_opy_
      else:
        pabot._run = bstack1l111ll1ll_opy_
    except Exception as e:
      pabot._run = bstack1l111ll1ll_opy_
    pabot._create_command_for_execution = bstack1lll111ll_opy_
    pabot._report_results = bstack11ll1111l1_opy_
  if bstack1l1ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧೌ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1111l1l11_opy_(e, bstack1ll1ll11ll_opy_)
    Runner.run_hook = bstack1l11ll1lll_opy_
    Step.run = bstack11llll1l1_opy_
  if bstack1l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ್") in str(framework_name).lower():
    if not bstack1ll1l111ll_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1ll1l1l1ll_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1l11l11ll1_opy_
      Config.getoption = bstack1l11l1l1ll_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack111111111_opy_
    except Exception as e:
      pass
def bstack111llll1_opy_():
  global CONFIG
  if bstack1l1ll_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ೎") in CONFIG and int(CONFIG[bstack1l1ll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ೏")]) > 1:
    logger.warn(bstack11111l1l1_opy_)
def bstack11ll111ll1_opy_(arg, bstack1l1lll111l_opy_, bstack1l1l11ll1_opy_=None):
  global CONFIG
  global bstack1lll11lll_opy_
  global bstack1llll1l1l1_opy_
  global bstack1ll1l111ll_opy_
  global bstack11l1lll1_opy_
  bstack1l11lll11l_opy_ = bstack1l1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ೐")
  if bstack1l1lll111l_opy_ and isinstance(bstack1l1lll111l_opy_, str):
    bstack1l1lll111l_opy_ = eval(bstack1l1lll111l_opy_)
  CONFIG = bstack1l1lll111l_opy_[bstack1l1ll_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬ೑")]
  bstack1lll11lll_opy_ = bstack1l1lll111l_opy_[bstack1l1ll_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧ೒")]
  bstack1llll1l1l1_opy_ = bstack1l1lll111l_opy_[bstack1l1ll_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ೓")]
  bstack1ll1l111ll_opy_ = bstack1l1lll111l_opy_[bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫ೔")]
  bstack11l1lll1_opy_.bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪೕ"), bstack1ll1l111ll_opy_)
  os.environ[bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬೖ")] = bstack1l11lll11l_opy_
  os.environ[bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࠪ೗")] = json.dumps(CONFIG)
  os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡍ࡛ࡂࡠࡗࡕࡐࠬ೘")] = bstack1lll11lll_opy_
  os.environ[bstack1l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ೙")] = str(bstack1llll1l1l1_opy_)
  os.environ[bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡍࡗࡊࡍࡓ࠭೚")] = str(True)
  if bstack1ll1ll1ll_opy_(arg, [bstack1l1ll_opy_ (u"ࠨ࠯ࡱࠫ೛"), bstack1l1ll_opy_ (u"ࠩ࠰࠱ࡳࡻ࡭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ೜")]) != -1:
    os.environ[bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡅࡗࡇࡌࡍࡇࡏࠫೝ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack11l11l1l_opy_)
    return
  bstack11l1l1llll_opy_()
  global bstack1l1l1111ll_opy_
  global bstack11ll1ll111_opy_
  global bstack111ll1l1_opy_
  global bstack1llll1lll_opy_
  global bstack111llll1l_opy_
  global bstack111ll11ll_opy_
  global bstack1llll1l1_opy_
  arg.append(bstack1l1ll_opy_ (u"ࠦ࠲࡝ࠢೞ"))
  arg.append(bstack1l1ll_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩ࠿ࡓ࡯ࡥࡷ࡯ࡩࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡩ࡮ࡲࡲࡶࡹ࡫ࡤ࠻ࡲࡼࡸࡪࡹࡴ࠯ࡒࡼࡸࡪࡹࡴࡘࡣࡵࡲ࡮ࡴࡧࠣ೟"))
  arg.append(bstack1l1ll_opy_ (u"ࠨ࠭ࡘࠤೠ"))
  arg.append(bstack1l1ll_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫࠺ࡕࡪࡨࠤ࡭ࡵ࡯࡬࡫ࡰࡴࡱࠨೡ"))
  global bstack1l11lll1l_opy_
  global bstack1l1l11lll_opy_
  global bstack1llll111l_opy_
  global bstack1l1ll1ll1l_opy_
  global bstack11111llll_opy_
  global bstack11llll111_opy_
  global bstack1111l11l1_opy_
  global bstack11l111ll_opy_
  global bstack1l11lll1ll_opy_
  global bstack1ll111ll1_opy_
  global bstack1l1111l1ll_opy_
  global bstack11ll1111l_opy_
  global bstack11ll1lll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l11lll1l_opy_ = webdriver.Remote.__init__
    bstack1l1l11lll_opy_ = WebDriver.quit
    bstack11l111ll_opy_ = WebDriver.close
    bstack1l11lll1ll_opy_ = WebDriver.get
    bstack1llll111l_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1ll1111l1_opy_(CONFIG) and bstack11111111_opy_():
    if bstack1l1l1l111l_opy_() < version.parse(bstack1llllll1ll_opy_):
      logger.error(bstack1llll111ll_opy_.format(bstack1l1l1l111l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1l1ll_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩೢ")) and callable(getattr(RemoteConnection, bstack1l1ll_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪೣ"))):
          bstack1ll111ll1_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack1ll111ll1_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack11l1l1l1l_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1l1111l1ll_opy_ = Config.getoption
    from _pytest import runner
    bstack11ll1111l_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack11lll1lll1_opy_)
  try:
    from pytest_bdd import reporting
    bstack11ll1lll_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack1l1ll_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶࠫ೤"))
  bstack111ll1l1_opy_ = CONFIG.get(bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ೥"), {}).get(bstack1l1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ೦"))
  bstack1llll1l1_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack11l111111_opy_():
      bstack11ll1lll1l_opy_.invoke(bstack111l1lll_opy_.CONNECT, bstack1l11111l1_opy_())
    platform_index = int(os.environ.get(bstack1l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭೧"), bstack1l1ll_opy_ (u"ࠧ࠱ࠩ೨")))
  else:
    bstack11llllll_opy_(bstack11ll1111ll_opy_)
  os.environ[bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩ೩")] = CONFIG[bstack1l1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ೪")]
  os.environ[bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭೫")] = CONFIG[bstack1l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ೬")]
  os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ೭")] = bstack1ll1l111ll_opy_.__str__()
  from _pytest.config import main as bstack11l111llll_opy_
  bstack11ll1l1111_opy_ = []
  try:
    bstack1l1l11l111_opy_ = bstack11l111llll_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack1llll1ll1l_opy_()
    if bstack1l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶࠪ೮") in multiprocessing.current_process().__dict__.keys():
      for bstack1l11l11l11_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11ll1l1111_opy_.append(bstack1l11l11l11_opy_)
    try:
      bstack1l111111_opy_ = (bstack11ll1l1111_opy_, int(bstack1l1l11l111_opy_))
      bstack1l1l11ll1_opy_.append(bstack1l111111_opy_)
    except:
      bstack1l1l11ll1_opy_.append((bstack11ll1l1111_opy_, bstack1l1l11l111_opy_))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack11ll1l1111_opy_.append({bstack1l1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ೯"): bstack1l1ll_opy_ (u"ࠨࡒࡵࡳࡨ࡫ࡳࡴࠢࠪ೰") + os.environ.get(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩೱ")), bstack1l1ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩೲ"): traceback.format_exc(), bstack1l1ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪೳ"): int(os.environ.get(bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ೴")))})
    bstack1l1l11ll1_opy_.append((bstack11ll1l1111_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack1l1ll_opy_ (u"ࠨࡲࡦࡶࡵ࡭ࡪࡹࠢ೵"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack11l1l11ll_opy_ = e.__class__.__name__
    print(bstack1l1ll_opy_ (u"ࠢࠦࡵ࠽ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡶࡺࡴ࡮ࡪࡰࡪࠤࡧ࡫ࡨࡢࡸࡨࠤࡹ࡫ࡳࡵࠢࠨࡷࠧ೶") % (bstack11l1l11ll_opy_, e))
    return 1
def bstack11lll1ll1_opy_(arg):
  global bstack1l1l1ll1_opy_
  bstack11llllll_opy_(bstack1ll1ll1l_opy_)
  os.environ[bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ೷")] = str(bstack1llll1l1l1_opy_)
  retries = bstack1ll1l111l1_opy_.bstack1l1ll1ll1_opy_(CONFIG)
  status_code = 0
  if bstack1ll1l111l1_opy_.bstack1l1ll1l1l_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack1llll11l1_opy_
    status_code = bstack1llll11l1_opy_(arg)
  if status_code != 0:
    bstack1l1l1ll1_opy_ = status_code
def bstack1llll1lll1_opy_():
  logger.info(bstack111l1l111_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1l1ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨ೸"), help=bstack1l1ll_opy_ (u"ࠪࡋࡪࡴࡥࡳࡣࡷࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡨࡵ࡮ࡧ࡫ࡪࠫ೹"))
  parser.add_argument(bstack1l1ll_opy_ (u"ࠫ࠲ࡻࠧ೺"), bstack1l1ll_opy_ (u"ࠬ࠳࠭ࡶࡵࡨࡶࡳࡧ࡭ࡦࠩ೻"), help=bstack1l1ll_opy_ (u"࡙࠭ࡰࡷࡵࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬ೼"))
  parser.add_argument(bstack1l1ll_opy_ (u"ࠧ࠮࡭ࠪ೽"), bstack1l1ll_opy_ (u"ࠨ࠯࠰࡯ࡪࡿࠧ೾"), help=bstack1l1ll_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡡࡤࡥࡨࡷࡸࠦ࡫ࡦࡻࠪ೿"))
  parser.add_argument(bstack1l1ll_opy_ (u"ࠪ࠱࡫࠭ഀ"), bstack1l1ll_opy_ (u"ࠫ࠲࠳ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩഁ"), help=bstack1l1ll_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡸࡪࡹࡴࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫം"))
  bstack1llll1llll_opy_ = parser.parse_args()
  try:
    bstack11ll1l11l1_opy_ = bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡭ࡥ࡯ࡧࡵ࡭ࡨ࠴ࡹ࡮࡮࠱ࡷࡦࡳࡰ࡭ࡧࠪഃ")
    if bstack1llll1llll_opy_.framework and bstack1llll1llll_opy_.framework not in (bstack1l1ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧഄ"), bstack1l1ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴ࠩഅ")):
      bstack11ll1l11l1_opy_ = bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࠲ࡾࡳ࡬࠯ࡵࡤࡱࡵࡲࡥࠨആ")
    bstack1ll1llll1l_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11ll1l11l1_opy_)
    bstack1l11l1ll_opy_ = open(bstack1ll1llll1l_opy_, bstack1l1ll_opy_ (u"ࠪࡶࠬഇ"))
    bstack1l1l111l11_opy_ = bstack1l11l1ll_opy_.read()
    bstack1l11l1ll_opy_.close()
    if bstack1llll1llll_opy_.username:
      bstack1l1l111l11_opy_ = bstack1l1l111l11_opy_.replace(bstack1l1ll_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡘࡗࡊࡘࡎࡂࡏࡈࠫഈ"), bstack1llll1llll_opy_.username)
    if bstack1llll1llll_opy_.key:
      bstack1l1l111l11_opy_ = bstack1l1l111l11_opy_.replace(bstack1l1ll_opy_ (u"ࠬ࡟ࡏࡖࡔࡢࡅࡈࡉࡅࡔࡕࡢࡏࡊ࡟ࠧഉ"), bstack1llll1llll_opy_.key)
    if bstack1llll1llll_opy_.framework:
      bstack1l1l111l11_opy_ = bstack1l1l111l11_opy_.replace(bstack1l1ll_opy_ (u"࡙࠭ࡐࡗࡕࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧഊ"), bstack1llll1llll_opy_.framework)
    file_name = bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪഋ")
    file_path = os.path.abspath(file_name)
    bstack11lllll111_opy_ = open(file_path, bstack1l1ll_opy_ (u"ࠨࡹࠪഌ"))
    bstack11lllll111_opy_.write(bstack1l1l111l11_opy_)
    bstack11lllll111_opy_.close()
    logger.info(bstack11lll1l1l1_opy_)
    try:
      os.environ[bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ഍")] = bstack1llll1llll_opy_.framework if bstack1llll1llll_opy_.framework != None else bstack1l1ll_opy_ (u"ࠥࠦഎ")
      config = yaml.safe_load(bstack1l1l111l11_opy_)
      config[bstack1l1ll_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫഏ")] = bstack1l1ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠲ࡹࡥࡵࡷࡳࠫഐ")
      bstack1llll1l111_opy_(bstack1l1ll1l11l_opy_, config)
    except Exception as e:
      logger.debug(bstack1l11ll1ll_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1lll1111l_opy_.format(str(e)))
def bstack1llll1l111_opy_(bstack1llll11lll_opy_, config, bstack11l111l111_opy_={}):
  global bstack1ll1l111ll_opy_
  global bstack111111ll_opy_
  global bstack11l1lll1_opy_
  if not config:
    return
  bstack111l11ll_opy_ = bstack11llllll11_opy_ if not bstack1ll1l111ll_opy_ else (
    bstack1l1llllll1_opy_ if bstack1l1ll_opy_ (u"࠭ࡡࡱࡲࠪ഑") in config else (
        bstack11l11ll1l_opy_ if config.get(bstack1l1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫഒ")) else bstack11ll11l1l1_opy_
    )
)
  bstack1l1l11l1_opy_ = False
  bstack1l111l1lll_opy_ = False
  if bstack1ll1l111ll_opy_ is True:
      if bstack1l1ll_opy_ (u"ࠨࡣࡳࡴࠬഓ") in config:
          bstack1l1l11l1_opy_ = True
      else:
          bstack1l111l1lll_opy_ = True
  bstack11l1ll11l_opy_ = bstack1l111l111l_opy_.bstack11l11l1l1l_opy_(config, bstack111111ll_opy_)
  bstack1lllll111_opy_ = bstack1lll11lll1_opy_()
  data = {
    bstack1l1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫഔ"): config[bstack1l1ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬക")],
    bstack1l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧഖ"): config[bstack1l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨഗ")],
    bstack1l1ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪഘ"): bstack1llll11lll_opy_,
    bstack1l1ll_opy_ (u"ࠧࡥࡧࡷࡩࡨࡺࡥࡥࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫങ"): os.environ.get(bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪച"), bstack111111ll_opy_),
    bstack1l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫഛ"): bstack1l1l1lll1_opy_,
    bstack1l1ll_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰࠬജ"): bstack11l11ll1l1_opy_(),
    bstack1l1ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧഝ"): {
      bstack1l1ll_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪഞ"): str(config[bstack1l1ll_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ട")]) if bstack1l1ll_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧഠ") in config else bstack1l1ll_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤഡ"),
      bstack1l1ll_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨ࡚ࡪࡸࡳࡪࡱࡱࠫഢ"): sys.version,
      bstack1l1ll_opy_ (u"ࠪࡶࡪ࡬ࡥࡳࡴࡨࡶࠬണ"): bstack1l1lll11ll_opy_(os.environ.get(bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ത"), bstack111111ll_opy_)),
      bstack1l1ll_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧഥ"): bstack1l1ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ദ"),
      bstack1l1ll_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨധ"): bstack111l11ll_opy_,
      bstack1l1ll_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭ന"): bstack11l1ll11l_opy_,
      bstack1l1ll_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡢࡹࡺ࡯ࡤࠨഩ"): os.environ[bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨപ")],
      bstack1l1ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧഫ"): os.environ.get(bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧബ"), bstack111111ll_opy_),
      bstack1l1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩഭ"): bstack11l1111l_opy_(os.environ.get(bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩമ"), bstack111111ll_opy_)),
      bstack1l1ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧയ"): bstack1lllll111_opy_.get(bstack1l1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧര")),
      bstack1l1ll_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩറ"): bstack1lllll111_opy_.get(bstack1l1ll_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬല")),
      bstack1l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨള"): config[bstack1l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩഴ")] if config[bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪവ")] else bstack1l1ll_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤശ"),
      bstack1l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫഷ"): str(config[bstack1l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬസ")]) if bstack1l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ഹ") in config else bstack1l1ll_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨഺ"),
      bstack1l1ll_opy_ (u"࠭࡯ࡴ഻ࠩ"): sys.platform,
      bstack1l1ll_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦ഼ࠩ"): socket.gethostname(),
      bstack1l1ll_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪഽ"): bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫാ"))
    }
  }
  if not bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪി")) is None:
    data[bstack1l1ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧീ")][bstack1l1ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࡍࡦࡶࡤࡨࡦࡺࡡࠨു")] = {
      bstack1l1ll_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ൂ"): bstack1l1ll_opy_ (u"ࠧࡶࡵࡨࡶࡤࡱࡩ࡭࡮ࡨࡨࠬൃ"),
      bstack1l1ll_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࠨൄ"): bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩ൅")),
      bstack1l1ll_opy_ (u"ࠪࡷ࡮࡭࡮ࡢ࡮ࡑࡹࡲࡨࡥࡳࠩെ"): bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡓࡵࠧേ"))
    }
  if bstack1llll11lll_opy_ == bstack1ll1l1ll11_opy_:
    data[bstack1l1ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨൈ")][bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡈࡵ࡮ࡧ࡫ࡪࠫ൉")] = bstack11l1l1l1_opy_(config)
    data[bstack1l1ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪൊ")][bstack1l1ll_opy_ (u"ࠨ࡫ࡶࡔࡪࡸࡣࡺࡃࡸࡸࡴࡋ࡮ࡢࡤ࡯ࡩࡩ࠭ോ")] = percy.bstack1111ll11l_opy_
    data[bstack1l1ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬൌ")][bstack1l1ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࡄࡸ࡭ࡱࡪࡉࡥ്ࠩ")] = percy.percy_build_id
  if not bstack1ll1l111l1_opy_.bstack1l1l1ll11l_opy_(CONFIG):
    data[bstack1l1ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧൎ")][bstack1l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠩ൏")] = bstack1ll1l111l1_opy_.bstack1l1l1ll11l_opy_(CONFIG)
  bstack1l1l1l1lll_opy_ = bstack11ll1l1ll1_opy_.bstack11ll11ll1_opy_(CONFIG, logger)
  bstack111llllll1_opy_ = bstack1ll1l111l1_opy_.bstack11ll11ll1_opy_(config=CONFIG)
  if bstack1l1l1l1lll_opy_ is not None and bstack111llllll1_opy_ is not None and bstack111llllll1_opy_.bstack11ll1l11l_opy_():
    data[bstack1l1ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ൐")][bstack111llllll1_opy_.bstack1ll111l11l_opy_()] = bstack1l1l1l1lll_opy_.bstack1ll11ll1l1_opy_()
  update(data[bstack1l1ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ൑")], bstack11l111l111_opy_)
  try:
    response = bstack1ll1l1l1l1_opy_(bstack1l1ll_opy_ (u"ࠨࡒࡒࡗ࡙࠭൒"), bstack111ll111_opy_(bstack1ll1lll1_opy_), data, {
      bstack1l1ll_opy_ (u"ࠩࡤࡹࡹ࡮ࠧ൓"): (config[bstack1l1ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬൔ")], config[bstack1l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧൕ")])
    })
    if response:
      logger.debug(bstack1llll1ll1_opy_.format(bstack1llll11lll_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1l11111lll_opy_.format(str(e)))
def bstack1l1lll11ll_opy_(framework):
  return bstack1l1ll_opy_ (u"ࠧࢁࡽ࠮ࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࡻࡾࠤൖ").format(str(framework), __version__) if framework else bstack1l1ll_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࢀࢃࠢൗ").format(
    __version__)
def bstack11l1l1llll_opy_():
  global CONFIG
  global bstack11l1llll11_opy_
  if bool(CONFIG):
    return
  try:
    bstack11l11lllll_opy_()
    logger.debug(bstack1111llll_opy_.format(str(CONFIG)))
    bstack11l1llll11_opy_ = bstack1l1111111_opy_.bstack1lll1l1ll_opy_(CONFIG, bstack11l1llll11_opy_)
    bstack11ll1111_opy_()
  except Exception as e:
    logger.error(bstack1l1ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࡵࡱ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠦ൘") + str(e))
    sys.exit(1)
  sys.excepthook = bstack11llllllll_opy_
  atexit.register(bstack11lllll1l1_opy_)
  signal.signal(signal.SIGINT, bstack1l1l11l1l1_opy_)
  signal.signal(signal.SIGTERM, bstack1l1l11l1l1_opy_)
def bstack11llllllll_opy_(exctype, value, traceback):
  global bstack1lllllll1_opy_
  try:
    for driver in bstack1lllllll1_opy_:
      bstack1l1l111l1_opy_(driver, bstack1l1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ൙"), bstack1l1ll_opy_ (u"ࠤࡖࡩࡸࡹࡩࡰࡰࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧ൚") + str(value))
  except Exception:
    pass
  logger.info(bstack1l11llll11_opy_)
  bstack1l11llll1l_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l11llll1l_opy_(message=bstack1l1ll_opy_ (u"ࠪࠫ൛"), bstack11l11llll1_opy_ = False):
  global CONFIG
  bstack1ll11l1lll_opy_ = bstack1l1ll_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡉࡽࡩࡥࡱࡶ࡬ࡳࡳ࠭൜") if bstack11l11llll1_opy_ else bstack1l1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ൝")
  try:
    if message:
      bstack11l111l111_opy_ = {
        bstack1ll11l1lll_opy_ : str(message)
      }
      bstack1llll1l111_opy_(bstack1ll1l1ll11_opy_, CONFIG, bstack11l111l111_opy_)
    else:
      bstack1llll1l111_opy_(bstack1ll1l1ll11_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1l1l1ll11_opy_.format(str(e)))
def bstack1111ll11_opy_(bstack1lll11ll11_opy_, size):
  bstack1ll1111l1l_opy_ = []
  while len(bstack1lll11ll11_opy_) > size:
    bstack1l1ll1l1_opy_ = bstack1lll11ll11_opy_[:size]
    bstack1ll1111l1l_opy_.append(bstack1l1ll1l1_opy_)
    bstack1lll11ll11_opy_ = bstack1lll11ll11_opy_[size:]
  bstack1ll1111l1l_opy_.append(bstack1lll11ll11_opy_)
  return bstack1ll1111l1l_opy_
def bstack11lll1111_opy_(args):
  if bstack1l1ll_opy_ (u"࠭࠭࡮ࠩ൞") in args and bstack1l1ll_opy_ (u"ࠧࡱࡦࡥࠫൟ") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack1lll1lllll_opy_, stage=STAGE.bstack1l1llllll_opy_)
def run_on_browserstack(bstack1l1l1111_opy_=None, bstack1l1l11ll1_opy_=None, bstack1ll11ll1_opy_=False):
  global CONFIG
  global bstack1lll11lll_opy_
  global bstack1llll1l1l1_opy_
  global bstack111111ll_opy_
  global bstack11l1lll1_opy_
  bstack1l11lll11l_opy_ = bstack1l1ll_opy_ (u"ࠨࠩൠ")
  bstack1l11111111_opy_(bstack11ll11l1l_opy_, logger)
  if bstack1l1l1111_opy_ and isinstance(bstack1l1l1111_opy_, str):
    bstack1l1l1111_opy_ = eval(bstack1l1l1111_opy_)
  if bstack1l1l1111_opy_:
    CONFIG = bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩൡ")]
    bstack1lll11lll_opy_ = bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫൢ")]
    bstack1llll1l1l1_opy_ = bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ൣ")]
    bstack11l1lll1_opy_.bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ൤"), bstack1llll1l1l1_opy_)
    bstack1l11lll11l_opy_ = bstack1l1ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭൥")
  bstack11l1lll1_opy_.bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ൦"), uuid4().__str__())
  logger.info(bstack1l1ll_opy_ (u"ࠨࡕࡇࡏࠥࡸࡵ࡯ࠢࡶࡸࡦࡸࡴࡦࡦࠣࡻ࡮ࡺࡨࠡ࡫ࡧ࠾ࠥ࠭൧") + bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫ൨")));
  logger.debug(bstack1l1ll_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࡂ࠭൩") + bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭൪")))
  if not bstack1ll11ll1_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack11l11l1l_opy_)
      return
    if sys.argv[1] == bstack1l1ll_opy_ (u"ࠬ࠳࠭ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ൫") or sys.argv[1] == bstack1l1ll_opy_ (u"࠭࠭ࡷࠩ൬"):
      logger.info(bstack1l1ll_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡐࡺࡶ࡫ࡳࡳࠦࡓࡅࡍࠣࡺࢀࢃࠧ൭").format(__version__))
      return
    if sys.argv[1] == bstack1l1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ൮"):
      bstack1llll1lll1_opy_()
      return
  args = sys.argv
  bstack11l1l1llll_opy_()
  global bstack1l1l1111ll_opy_
  global bstack1l1ll1ll_opy_
  global bstack1llll1l1_opy_
  global bstack1111l11l_opy_
  global bstack11ll1ll111_opy_
  global bstack111ll1l1_opy_
  global bstack1llll1lll_opy_
  global bstack11lll11111_opy_
  global bstack111llll1l_opy_
  global bstack111ll11ll_opy_
  global bstack1llll1l11l_opy_
  bstack1l1ll1ll_opy_ = len(CONFIG.get(bstack1l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ൯"), []))
  if not bstack1l11lll11l_opy_:
    if args[1] == bstack1l1ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ൰") or args[1] == bstack1l1ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬ൱"):
      bstack1l11lll11l_opy_ = bstack1l1ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ൲")
      args = args[2:]
    elif args[1] == bstack1l1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ൳"):
      bstack1l11lll11l_opy_ = bstack1l1ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭൴")
      args = args[2:]
    elif args[1] == bstack1l1ll_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ൵"):
      bstack1l11lll11l_opy_ = bstack1l1ll_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ൶")
      args = args[2:]
    elif args[1] == bstack1l1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ൷"):
      bstack1l11lll11l_opy_ = bstack1l1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ൸")
      args = args[2:]
    elif args[1] == bstack1l1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ൹"):
      bstack1l11lll11l_opy_ = bstack1l1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ൺ")
      args = args[2:]
    elif args[1] == bstack1l1ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧൻ"):
      bstack1l11lll11l_opy_ = bstack1l1ll_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨർ")
      args = args[2:]
    else:
      if not bstack1l1ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬൽ") in CONFIG or str(CONFIG[bstack1l1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ൾ")]).lower() in [bstack1l1ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫൿ"), bstack1l1ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭඀")]:
        bstack1l11lll11l_opy_ = bstack1l1ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ඁ")
        args = args[1:]
      elif str(CONFIG[bstack1l1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪං")]).lower() == bstack1l1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧඃ"):
        bstack1l11lll11l_opy_ = bstack1l1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ඄")
        args = args[1:]
      elif str(CONFIG[bstack1l1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭අ")]).lower() == bstack1l1ll_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪආ"):
        bstack1l11lll11l_opy_ = bstack1l1ll_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫඇ")
        args = args[1:]
      elif str(CONFIG[bstack1l1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩඈ")]).lower() == bstack1l1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧඉ"):
        bstack1l11lll11l_opy_ = bstack1l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨඊ")
        args = args[1:]
      elif str(CONFIG[bstack1l1ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬඋ")]).lower() == bstack1l1ll_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪඌ"):
        bstack1l11lll11l_opy_ = bstack1l1ll_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫඍ")
        args = args[1:]
      else:
        os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧඎ")] = bstack1l11lll11l_opy_
        bstack111111l11_opy_(bstack1lll111ll1_opy_)
  os.environ[bstack1l1ll_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧඏ")] = bstack1l11lll11l_opy_
  bstack111111ll_opy_ = bstack1l11lll11l_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack1l11l1l1_opy_ = bstack1ll1llll1_opy_[bstack1l1ll_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࠭ࡃࡆࡇࠫඐ")] if bstack1l11lll11l_opy_ == bstack1l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨඑ") and bstack1lll11l111_opy_() else bstack1l11lll11l_opy_
      bstack11ll1lll1l_opy_.invoke(bstack111l1lll_opy_.bstack1l111ll1_opy_, bstack1l1l1ll111_opy_(
        sdk_version=__version__,
        path_config=bstack1lll111l1_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack1l11l1l1_opy_,
        frameworks=[bstack1l11l1l1_opy_],
        framework_versions={
          bstack1l11l1l1_opy_: bstack11l1111l_opy_(bstack1l1ll_opy_ (u"ࠩࡕࡳࡧࡵࡴࠨඒ") if bstack1l11lll11l_opy_ in [bstack1l1ll_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩඓ"), bstack1l1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪඔ"), bstack1l1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ඕ")] else bstack1l11lll11l_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack1l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣඖ"), None):
        CONFIG[bstack1l1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤ඗")] = cli.config.get(bstack1l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥ඘"), None)
    except Exception as e:
      bstack11ll1lll1l_opy_.invoke(bstack111l1lll_opy_.bstack1ll1llll11_opy_, e.__traceback__, 1)
    if bstack1llll1l1l1_opy_:
      CONFIG[bstack1l1ll_opy_ (u"ࠤࡤࡴࡵࠨ඙")] = cli.config[bstack1l1ll_opy_ (u"ࠥࡥࡵࡶࠢක")]
      logger.info(bstack11l1lll1l_opy_.format(CONFIG[bstack1l1ll_opy_ (u"ࠫࡦࡶࡰࠨඛ")]))
  else:
    bstack11ll1lll1l_opy_.clear()
  global bstack11ll111lll_opy_
  global bstack1l11ll11l_opy_
  if bstack1l1l1111_opy_:
    try:
      bstack11l1l1111_opy_ = datetime.datetime.now()
      os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧග")] = bstack1l11lll11l_opy_
      bstack1llll1l111_opy_(bstack1l11l1ll1l_opy_, CONFIG)
      cli.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠨࡨࡵࡶࡳ࠾ࡸࡪ࡫ࡠࡶࡨࡷࡹࡥࡡࡵࡶࡨࡱࡵࡺࡥࡥࠤඝ"), datetime.datetime.now() - bstack11l1l1111_opy_)
    except Exception as e:
      logger.debug(bstack1ll111lll1_opy_.format(str(e)))
  global bstack1l11lll1l_opy_
  global bstack1l1l11lll_opy_
  global bstack1ll11111l_opy_
  global bstack111lllll1l_opy_
  global bstack11ll1lllll_opy_
  global bstack11ll11l1ll_opy_
  global bstack1l1ll1ll1l_opy_
  global bstack11111llll_opy_
  global bstack11111l11l_opy_
  global bstack11llll111_opy_
  global bstack1111l11l1_opy_
  global bstack11l111ll_opy_
  global bstack1111l1111_opy_
  global bstack1l111ll11_opy_
  global bstack1l11lll1ll_opy_
  global bstack1ll111ll1_opy_
  global bstack1l1111l1ll_opy_
  global bstack11ll1111l_opy_
  global bstack11l11111_opy_
  global bstack11ll1lll_opy_
  global bstack1llll111l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l11lll1l_opy_ = webdriver.Remote.__init__
    bstack1l1l11lll_opy_ = WebDriver.quit
    bstack11l111ll_opy_ = WebDriver.close
    bstack1l11lll1ll_opy_ = WebDriver.get
    bstack1llll111l_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack11ll111lll_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1lllll1l1l_opy_
    bstack1l11ll11l_opy_ = bstack1lllll1l1l_opy_()
  except Exception as e:
    pass
  try:
    global bstack11ll11llll_opy_
    from QWeb.keywords import browser
    bstack11ll11llll_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1ll1111l1_opy_(CONFIG) and bstack11111111_opy_():
    if bstack1l1l1l111l_opy_() < version.parse(bstack1llllll1ll_opy_):
      logger.error(bstack1llll111ll_opy_.format(bstack1l1l1l111l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1l1ll_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨඞ")) and callable(getattr(RemoteConnection, bstack1l1ll_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩඟ"))):
          RemoteConnection._get_proxy_url = bstack111ll11l1_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack111ll11l1_opy_
      except Exception as e:
        logger.error(bstack11l1l1l1l_opy_.format(str(e)))
  if not CONFIG.get(bstack1l1ll_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫච"), False) and not bstack1l1l1111_opy_:
    logger.info(bstack1l111lllll_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack1l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧඡ") in CONFIG and str(CONFIG[bstack1l1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨජ")]).lower() != bstack1l1ll_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫඣ"):
      bstack11ll1ll1ll_opy_()
    elif bstack1l11lll11l_opy_ != bstack1l1ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ඤ") or (bstack1l11lll11l_opy_ == bstack1l1ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧඥ") and not bstack1l1l1111_opy_):
      bstack11l1l11lll_opy_()
  if (bstack1l11lll11l_opy_ in [bstack1l1ll_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧඦ"), bstack1l1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨට"), bstack1l1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫඨ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack111l1llll_opy_
        bstack11ll11l1ll_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1ll1ll11l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack11ll1lllll_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1111ll111_opy_ + str(e))
    except Exception as e:
      bstack1111l1l11_opy_(e, bstack1ll1ll11l_opy_)
    if bstack1l11lll11l_opy_ != bstack1l1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬඩ"):
      bstack1ll1l111l_opy_()
    bstack1ll11111l_opy_ = Output.start_test
    bstack111lllll1l_opy_ = Output.end_test
    bstack1l1ll1ll1l_opy_ = TestStatus.__init__
    bstack11111l11l_opy_ = pabot._run
    bstack11llll111_opy_ = QueueItem.__init__
    bstack1111l11l1_opy_ = pabot._create_command_for_execution
    bstack11l11111_opy_ = pabot._report_results
  if bstack1l11lll11l_opy_ == bstack1l1ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬඪ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1111l1l11_opy_(e, bstack1ll1ll11ll_opy_)
    bstack1111l1111_opy_ = Runner.run_hook
    bstack1l111ll11_opy_ = Step.run
  if bstack1l11lll11l_opy_ == bstack1l1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ණ"):
    try:
      from _pytest.config import Config
      bstack1l1111l1ll_opy_ = Config.getoption
      from _pytest import runner
      bstack11ll1111l_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack11lll1lll1_opy_)
    try:
      from pytest_bdd import reporting
      bstack11ll1lll_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1l1ll_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨඬ"))
  try:
    framework_name = bstack1l1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧත") if bstack1l11lll11l_opy_ in [bstack1l1ll_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨථ"), bstack1l1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩද"), bstack1l1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬධ")] else bstack1l11l11lll_opy_(bstack1l11lll11l_opy_)
    bstack11lll11lll_opy_ = {
      bstack1l1ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪ࠭න"): bstack1l1ll_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨ඲") if bstack1l11lll11l_opy_ == bstack1l1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧඳ") and bstack1lll11l111_opy_() else framework_name,
      bstack1l1ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬප"): bstack11l1111l_opy_(framework_name),
      bstack1l1ll_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧඵ"): __version__,
      bstack1l1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡵࡴࡧࡧࠫබ"): bstack1l11lll11l_opy_
    }
    if bstack1l11lll11l_opy_ in bstack1l11ll111l_opy_ + bstack1l11l111_opy_:
      if bstack111111l1l_opy_.bstack1llllll11_opy_(CONFIG):
        if bstack1l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫභ") in CONFIG:
          os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ම")] = os.getenv(bstack1l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧඹ"), json.dumps(CONFIG[bstack1l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧය")]))
          CONFIG[bstack1l1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨර")].pop(bstack1l1ll_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ඼"), None)
          CONFIG[bstack1l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪල")].pop(bstack1l1ll_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ඾"), None)
        bstack11lll11lll_opy_[bstack1l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ඿")] = {
          bstack1l1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫව"): bstack1l1ll_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩශ"),
          bstack1l1ll_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩෂ"): str(bstack1l1l1l111l_opy_())
        }
    if bstack1l11lll11l_opy_ not in [bstack1l1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪස")] and not cli.is_running():
      bstack11ll1l111l_opy_, bstack1ll1l1ll1l_opy_ = bstack11ll1ll1_opy_.launch(CONFIG, bstack11lll11lll_opy_)
      if bstack1ll1l1ll1l_opy_.get(bstack1l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪහ")) is not None and bstack111111l1l_opy_.bstack1ll1ll111_opy_(CONFIG) is None:
        value = bstack1ll1l1ll1l_opy_[bstack1l1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫළ")].get(bstack1l1ll_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭ෆ"))
        if value is not None:
            CONFIG[bstack1l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭෇")] = value
        else:
          logger.debug(bstack1l1ll_opy_ (u"ࠢࡏࡱࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡨࡦࡺࡡࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧ෈"))
  except Exception as e:
    logger.debug(bstack111l111l_opy_.format(bstack1l1ll_opy_ (u"ࠨࡖࡨࡷࡹࡎࡵࡣࠩ෉"), str(e)))
  if bstack1l11lll11l_opy_ == bstack1l1ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯්ࠩ"):
    bstack1llll1l1_opy_ = True
    if bstack1l1l1111_opy_ and bstack1ll11ll1_opy_:
      bstack111ll1l1_opy_ = CONFIG.get(bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ෋"), {}).get(bstack1l1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭෌"))
      bstack11llllll_opy_(bstack1l1111ll_opy_)
    elif bstack1l1l1111_opy_:
      bstack111ll1l1_opy_ = CONFIG.get(bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ෍"), {}).get(bstack1l1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ෎"))
      global bstack1lllllll1_opy_
      try:
        if bstack11lll1111_opy_(bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪා")]) and multiprocessing.current_process().name == bstack1l1ll_opy_ (u"ࠨ࠲ࠪැ"):
          bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬෑ")].remove(bstack1l1ll_opy_ (u"ࠪ࠱ࡲ࠭ි"))
          bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧී")].remove(bstack1l1ll_opy_ (u"ࠬࡶࡤࡣࠩු"))
          bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ෕")] = bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪූ")][0]
          with open(bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ෗")], bstack1l1ll_opy_ (u"ࠩࡵࠫෘ")) as f:
            bstack1l1111l11l_opy_ = f.read()
          bstack1lll11ll1_opy_ = bstack1l1ll_opy_ (u"ࠥࠦࠧ࡬ࡲࡰ࡯ࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡨࡰࠦࡩ࡮ࡲࡲࡶࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡦ࠽ࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪ࠮ࡻࡾࠫ࠾ࠤ࡫ࡸ࡯࡮ࠢࡳࡨࡧࠦࡩ࡮ࡲࡲࡶࡹࠦࡐࡥࡤ࠾ࠤࡴ࡭࡟ࡥࡤࠣࡁࠥࡖࡤࡣ࠰ࡧࡳࡤࡨࡲࡦࡣ࡮࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡦࡨࡪࠥࡳ࡯ࡥࡡࡥࡶࡪࡧ࡫ࠩࡵࡨࡰ࡫࠲ࠠࡢࡴࡪ࠰ࠥࡺࡥ࡮ࡲࡲࡶࡦࡸࡹࠡ࠿ࠣ࠴࠮ࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺࡲࡺ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡥࡷ࡭ࠠ࠾ࠢࡶࡸࡷ࠮ࡩ࡯ࡶࠫࡥࡷ࡭ࠩࠬ࠳࠳࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡩࡽࡩࡥࡱࡶࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡡࡴࠢࡨ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡶࡡࡴࡵࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡱࡪࡣࡩࡨࠨࡴࡧ࡯ࡪ࠱ࡧࡲࡨ࠮ࡷࡩࡲࡶ࡯ࡳࡣࡵࡽ࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࠤࡂࠦ࡭ࡰࡦࡢࡦࡷ࡫ࡡ࡬ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡖࡤࡣ࠰ࡧࡳࡤࡨࡲࡦࡣ࡮ࠤࡂࠦ࡭ࡰࡦࡢࡦࡷ࡫ࡡ࡬ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡖࡤࡣࠪࠬ࠲ࡸ࡫ࡴࡠࡶࡵࡥࡨ࡫ࠨࠪ࡞ࡱࠦࠧࠨෙ").format(str(bstack1l1l1111_opy_))
          bstack1lll11llll_opy_ = bstack1lll11ll1_opy_ + bstack1l1111l11l_opy_
          bstack1llll11l1l_opy_ = bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧේ")] + bstack1l1ll_opy_ (u"ࠬࡥࡢࡴࡶࡤࡧࡰࡥࡴࡦ࡯ࡳ࠲ࡵࡿࠧෛ")
          with open(bstack1llll11l1l_opy_, bstack1l1ll_opy_ (u"࠭ࡷࠨො")):
            pass
          with open(bstack1llll11l1l_opy_, bstack1l1ll_opy_ (u"ࠢࡸ࠭ࠥෝ")) as f:
            f.write(bstack1lll11llll_opy_)
          import subprocess
          bstack1lll1l111_opy_ = subprocess.run([bstack1l1ll_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࠣෞ"), bstack1llll11l1l_opy_])
          if os.path.exists(bstack1llll11l1l_opy_):
            os.unlink(bstack1llll11l1l_opy_)
          os._exit(bstack1lll1l111_opy_.returncode)
        else:
          if bstack11lll1111_opy_(bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬෟ")]):
            bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭෠")].remove(bstack1l1ll_opy_ (u"ࠫ࠲ࡳࠧ෡"))
            bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ෢")].remove(bstack1l1ll_opy_ (u"࠭ࡰࡥࡤࠪ෣"))
            bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ෤")] = bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ෥")][0]
          bstack11llllll_opy_(bstack1l1111ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ෦")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1l1ll_opy_ (u"ࠪࡣࡤࡴࡡ࡮ࡧࡢࡣࠬ෧")] = bstack1l1ll_opy_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭෨")
          mod_globals[bstack1l1ll_opy_ (u"ࠬࡥ࡟ࡧ࡫࡯ࡩࡤࡥࠧ෩")] = os.path.abspath(bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ෪")])
          exec(open(bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪ෫")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1l1ll_opy_ (u"ࠨࡅࡤࡹ࡬࡮ࡴࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠨ෬").format(str(e)))
          for driver in bstack1lllllll1_opy_:
            bstack1l1l11ll1_opy_.append({
              bstack1l1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ෭"): bstack1l1l1111_opy_[bstack1l1ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭෮")],
              bstack1l1ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ෯"): str(e),
              bstack1l1ll_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ෰"): multiprocessing.current_process().name
            })
            bstack1l1l111l1_opy_(driver, bstack1l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭෱"), bstack1l1ll_opy_ (u"ࠢࡔࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥෲ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1lllllll1_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1llll1l1l1_opy_, CONFIG, logger)
      bstack1l1l1l1l1l_opy_()
      bstack111llll1_opy_()
      percy.bstack1llll1l1ll_opy_()
      bstack1l1lll111l_opy_ = {
        bstack1l1ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫෳ"): args[0],
        bstack1l1ll_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩ෴"): CONFIG,
        bstack1l1ll_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫ෵"): bstack1lll11lll_opy_,
        bstack1l1ll_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭෶"): bstack1llll1l1l1_opy_
      }
      if bstack1l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ෷") in CONFIG:
        bstack11l1ll1111_opy_ = bstack1lllll1l1_opy_(args, logger, CONFIG, bstack1ll1l111ll_opy_, bstack1l1ll1ll_opy_)
        bstack11lll11111_opy_ = bstack11l1ll1111_opy_.bstack11llll1ll_opy_(run_on_browserstack, bstack1l1lll111l_opy_, bstack11lll1111_opy_(args))
      else:
        if bstack11lll1111_opy_(args):
          bstack1l1lll111l_opy_[bstack1l1ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ෸")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1l1lll111l_opy_,))
          test.start()
          test.join()
        else:
          bstack11llllll_opy_(bstack1l1111ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1l1ll_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩ෹")] = bstack1l1ll_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪ෺")
          mod_globals[bstack1l1ll_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫ෻")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1l11lll11l_opy_ == bstack1l1ll_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ෼") or bstack1l11lll11l_opy_ == bstack1l1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ෽"):
    percy.init(bstack1llll1l1l1_opy_, CONFIG, logger)
    percy.bstack1llll1l1ll_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1111l1l11_opy_(e, bstack1ll1ll11l_opy_)
    bstack1l1l1l1l1l_opy_()
    bstack11llllll_opy_(bstack11l111l11l_opy_)
    if bstack1ll1l111ll_opy_:
      bstack1l1ll11111_opy_(bstack11l111l11l_opy_, args)
      if bstack1l1ll_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ෾") in args:
        i = args.index(bstack1l1ll_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ෿"))
        args.pop(i)
        args.pop(i)
      if bstack1l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ฀") not in CONFIG:
        CONFIG[bstack1l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫก")] = [{}]
        bstack1l1ll1ll_opy_ = 1
      if bstack1l1l1111ll_opy_ == 0:
        bstack1l1l1111ll_opy_ = 1
      args.insert(0, str(bstack1l1l1111ll_opy_))
      args.insert(0, str(bstack1l1ll_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧข")))
    if bstack11ll1ll1_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1ll11l1111_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack111ll1111_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack1l1ll_opy_ (u"ࠥࡖࡔࡈࡏࡕࡡࡒࡔ࡙ࡏࡏࡏࡕࠥฃ"),
        ).parse_args(bstack1ll11l1111_opy_)
        bstack1l1llll11l_opy_ = args.index(bstack1ll11l1111_opy_[0]) if len(bstack1ll11l1111_opy_) > 0 else len(args)
        args.insert(bstack1l1llll11l_opy_, str(bstack1l1ll_opy_ (u"ࠫ࠲࠳࡬ࡪࡵࡷࡩࡳ࡫ࡲࠨค")))
        args.insert(bstack1l1llll11l_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡸ࡯ࡣࡱࡷࡣࡱ࡯ࡳࡵࡧࡱࡩࡷ࠴ࡰࡺࠩฅ"))))
        if bstack1ll1l111l1_opy_.bstack1l1ll1l1l_opy_(CONFIG):
          args.insert(bstack1l1llll11l_opy_, str(bstack1l1ll_opy_ (u"࠭࠭࠮࡮࡬ࡷࡹ࡫࡮ࡦࡴࠪฆ")))
          args.insert(bstack1l1llll11l_opy_ + 1, str(bstack1l1ll_opy_ (u"ࠧࡓࡧࡷࡶࡾࡌࡡࡪ࡮ࡨࡨ࠿ࢁࡽࠨง").format(bstack1ll1l111l1_opy_.bstack1l1ll1ll1_opy_(CONFIG))))
        if bstack1ll1l11l_opy_(os.environ.get(bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓ࠭จ"))) and str(os.environ.get(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘ࠭ฉ"), bstack1l1ll_opy_ (u"ࠪࡲࡺࡲ࡬ࠨช"))) != bstack1l1ll_opy_ (u"ࠫࡳࡻ࡬࡭ࠩซ"):
          for bstack1l11lllll1_opy_ in bstack111ll1111_opy_:
            args.remove(bstack1l11lllll1_opy_)
          test_files = os.environ.get(bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠩฌ")).split(bstack1l1ll_opy_ (u"࠭ࠬࠨญ"))
          for bstack1l1llll1l_opy_ in test_files:
            args.append(bstack1l1llll1l_opy_)
      except Exception as e:
        logger.error(bstack1l1ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡧࡴࡵࡣࡦ࡬࡮ࡴࡧࠡ࡮࡬ࡷࡹ࡫࡮ࡦࡴࠣࡪࡴࡸࠠࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿ࠮ࠡࡇࡵࡶࡴࡸࠠ࠮ࠢࠥฎ").format(e))
    pabot.main(args)
  elif bstack1l11lll11l_opy_ == bstack1l1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩฏ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1111l1l11_opy_(e, bstack1ll1ll11l_opy_)
    for a in args:
      if bstack1l1ll_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡒࡏࡅ࡙ࡌࡏࡓࡏࡌࡒࡉࡋࡘࠨฐ") in a:
        bstack11ll1ll111_opy_ = int(a.split(bstack1l1ll_opy_ (u"ࠪ࠾ࠬฑ"))[1])
      if bstack1l1ll_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡈࡊࡌࡌࡐࡅࡄࡐࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨฒ") in a:
        bstack111ll1l1_opy_ = str(a.split(bstack1l1ll_opy_ (u"ࠬࡀࠧณ"))[1])
      if bstack1l1ll_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘ࠭ด") in a:
        bstack1llll1lll_opy_ = str(a.split(bstack1l1ll_opy_ (u"ࠧ࠻ࠩต"))[1])
    bstack1l111lll1l_opy_ = None
    if bstack1l1ll_opy_ (u"ࠨ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠧถ") in args:
      i = args.index(bstack1l1ll_opy_ (u"ࠩ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠨท"))
      args.pop(i)
      bstack1l111lll1l_opy_ = args.pop(i)
    if bstack1l111lll1l_opy_ is not None:
      global bstack1ll11ll1l_opy_
      bstack1ll11ll1l_opy_ = bstack1l111lll1l_opy_
    bstack11llllll_opy_(bstack11l111l11l_opy_)
    run_cli(args)
    if bstack1l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧธ") in multiprocessing.current_process().__dict__.keys():
      for bstack1l11l11l11_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1l1l11ll1_opy_.append(bstack1l11l11l11_opy_)
  elif bstack1l11lll11l_opy_ == bstack1l1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫน"):
    bstack11l1l111ll_opy_ = bstack1lll1111_opy_(args, logger, CONFIG, bstack1ll1l111ll_opy_)
    bstack11l1l111ll_opy_.bstack111lll11l_opy_()
    bstack1l1l1l1l1l_opy_()
    bstack1111l11l_opy_ = True
    bstack111ll11ll_opy_ = bstack11l1l111ll_opy_.bstack1ll1l11ll_opy_()
    bstack11l1l111ll_opy_.bstack11l11l1111_opy_()
    bstack11l1l111ll_opy_.bstack1l1lll111l_opy_(bstack111ll111l_opy_)
    bstack11lllll11_opy_(bstack1l11lll11l_opy_, CONFIG, bstack11l1l111ll_opy_.bstack1ll1l1l111_opy_())
    bstack1l111111l_opy_ = bstack11l1l111ll_opy_.bstack11llll1ll_opy_(bstack11ll111ll1_opy_, {
      bstack1l1ll_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭บ"): bstack1lll11lll_opy_,
      bstack1l1ll_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨป"): bstack1llll1l1l1_opy_,
      bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪผ"): bstack1ll1l111ll_opy_
    })
    try:
      bstack11ll1l1111_opy_, bstack1l11l111l_opy_ = map(list, zip(*bstack1l111111l_opy_))
      bstack111llll1l_opy_ = bstack11ll1l1111_opy_[0]
      for status_code in bstack1l11l111l_opy_:
        if status_code != 0:
          bstack1llll1l11l_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack1l1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡧࡶࡦࠢࡨࡶࡷࡵࡲࡴࠢࡤࡲࡩࠦࡳࡵࡣࡷࡹࡸࠦࡣࡰࡦࡨ࠲ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࠼ࠣࡿࢂࠨฝ").format(str(e)))
  elif bstack1l11lll11l_opy_ == bstack1l1ll_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩพ"):
    try:
      from behave.__main__ import main as bstack1llll11l1_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1111l1l11_opy_(e, bstack1ll1ll11ll_opy_)
    bstack1l1l1l1l1l_opy_()
    bstack1111l11l_opy_ = True
    bstack1l111ll111_opy_ = 1
    if bstack1l1ll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪฟ") in CONFIG:
      bstack1l111ll111_opy_ = CONFIG[bstack1l1ll_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫภ")]
    if bstack1l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨม") in CONFIG:
      bstack11111l1ll_opy_ = int(bstack1l111ll111_opy_) * int(len(CONFIG[bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩย")]))
    else:
      bstack11111l1ll_opy_ = int(bstack1l111ll111_opy_)
    config = Configuration(args)
    bstack11lll1l11l_opy_ = config.paths
    if len(bstack11lll1l11l_opy_) == 0:
      import glob
      pattern = bstack1l1ll_opy_ (u"ࠧࠫࠬ࠲࠮࠳࡬ࡥࡢࡶࡸࡶࡪ࠭ร")
      bstack11l1ll1ll1_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack11l1ll1ll1_opy_)
      config = Configuration(args)
      bstack11lll1l11l_opy_ = config.paths
    bstack11ll11l11l_opy_ = [os.path.normpath(item) for item in bstack11lll1l11l_opy_]
    bstack11lll11l11_opy_ = [os.path.normpath(item) for item in args]
    bstack11l1l1l1ll_opy_ = [item for item in bstack11lll11l11_opy_ if item not in bstack11ll11l11l_opy_]
    import platform as pf
    if pf.system().lower() == bstack1l1ll_opy_ (u"ࠨࡹ࡬ࡲࡩࡵࡷࡴࠩฤ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack11ll11l11l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1l1l111l1l_opy_)))
                    for bstack1l1l111l1l_opy_ in bstack11ll11l11l_opy_]
    bstack1l1l1lllll_opy_ = []
    for spec in bstack11ll11l11l_opy_:
      bstack11lll1l111_opy_ = []
      bstack11lll1l111_opy_ += bstack11l1l1l1ll_opy_
      bstack11lll1l111_opy_.append(spec)
      bstack1l1l1lllll_opy_.append(bstack11lll1l111_opy_)
    execution_items = []
    for bstack11lll1l111_opy_ in bstack1l1l1lllll_opy_:
      if bstack1l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬล") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack1l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ฦ")]):
          item = {}
          item[bstack1l1ll_opy_ (u"ࠫࡦࡸࡧࠨว")] = bstack1l1ll_opy_ (u"ࠬࠦࠧศ").join(bstack11lll1l111_opy_)
          item[bstack1l1ll_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬษ")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack1l1ll_opy_ (u"ࠧࡢࡴࡪࠫส")] = bstack1l1ll_opy_ (u"ࠨࠢࠪห").join(bstack11lll1l111_opy_)
        item[bstack1l1ll_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨฬ")] = 0
        execution_items.append(item)
    bstack1l1111ll1_opy_ = bstack1111ll11_opy_(execution_items, bstack11111l1ll_opy_)
    for execution_item in bstack1l1111ll1_opy_:
      bstack1l1lllll1l_opy_ = []
      for item in execution_item:
        bstack1l1lllll1l_opy_.append(bstack1ll1lll11_opy_(name=str(item[bstack1l1ll_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩอ")]),
                                             target=bstack11lll1ll1_opy_,
                                             args=(item[bstack1l1ll_opy_ (u"ࠫࡦࡸࡧࠨฮ")],)))
      for t in bstack1l1lllll1l_opy_:
        t.start()
      for t in bstack1l1lllll1l_opy_:
        t.join()
  else:
    bstack111111l11_opy_(bstack1lll111ll1_opy_)
  if not bstack1l1l1111_opy_:
    bstack1l1111l1l1_opy_()
    if(bstack1l11lll11l_opy_ in [bstack1l1ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬฯ"), bstack1l1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ะ")]):
      bstack1ll1l1l1_opy_()
  bstack1l1111111_opy_.bstack1ll1l11ll1_opy_()
def browserstack_initialize(bstack1l1l111ll1_opy_=None):
  logger.info(bstack1l1ll_opy_ (u"ࠧࡓࡷࡱࡲ࡮ࡴࡧࠡࡕࡇࡏࠥࡽࡩࡵࡪࠣࡥࡷ࡭ࡳ࠻ࠢࠪั") + str(bstack1l1l111ll1_opy_))
  run_on_browserstack(bstack1l1l111ll1_opy_, None, True)
@measure(event_name=EVENTS.bstack1l11l1l11l_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1l1111l1l1_opy_():
  global CONFIG
  global bstack111111ll_opy_
  global bstack1llll1l11l_opy_
  global bstack1l1l1ll1_opy_
  global bstack11l1lll1_opy_
  bstack1111111l1_opy_.bstack1l1l1lll1l_opy_()
  if cli.is_running():
    bstack11ll1lll1l_opy_.invoke(bstack111l1lll_opy_.bstack11l1l1ll1_opy_)
  if bstack111111ll_opy_ == bstack1l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨา"):
    if not cli.is_enabled(CONFIG):
      bstack11ll1ll1_opy_.stop()
  else:
    bstack11ll1ll1_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack11ll1llll1_opy_.bstack1l111ll1l_opy_()
  if bstack1l1ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ำ") in CONFIG and str(CONFIG[bstack1l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧิ")]).lower() != bstack1l1ll_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪี"):
    hashed_id, bstack1l1ll111l1_opy_ = bstack1llllllll1_opy_()
  else:
    hashed_id, bstack1l1ll111l1_opy_ = get_build_link()
  bstack1lllll1lll_opy_(hashed_id)
  logger.info(bstack1l1ll_opy_ (u"࡙ࠬࡄࡌࠢࡵࡹࡳࠦࡥ࡯ࡦࡨࡨࠥ࡬࡯ࡳࠢ࡬ࡨ࠿࠭ึ") + bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨื"), bstack1l1ll_opy_ (u"ࠧࠨุ")) + bstack1l1ll_opy_ (u"ࠨ࠮ࠣࡸࡪࡹࡴࡩࡷࡥࠤ࡮ࡪ࠺ูࠡࠩ") + os.getenv(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊฺࠧ"), bstack1l1ll_opy_ (u"ࠪࠫ฻")))
  if hashed_id is not None and bstack1l11111ll1_opy_() != -1:
    sessions = bstack1lll111111_opy_(hashed_id)
    bstack1llll11ll_opy_(sessions, bstack1l1ll111l1_opy_)
  if bstack111111ll_opy_ == bstack1l1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ฼") and bstack1llll1l11l_opy_ != 0:
    sys.exit(bstack1llll1l11l_opy_)
  if bstack111111ll_opy_ == bstack1l1ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ฽") and bstack1l1l1ll1_opy_ != 0:
    sys.exit(bstack1l1l1ll1_opy_)
def bstack1lllll1lll_opy_(new_id):
    global bstack1l1l1lll1_opy_
    bstack1l1l1lll1_opy_ = new_id
def bstack1l11l11lll_opy_(bstack1ll11ll1ll_opy_):
  if bstack1ll11ll1ll_opy_:
    return bstack1ll11ll1ll_opy_.capitalize()
  else:
    return bstack1l1ll_opy_ (u"࠭ࠧ฾")
@measure(event_name=EVENTS.bstack1l1lll1l_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack11l1ll11_opy_(bstack1ll11l1l1l_opy_):
  if bstack1l1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ฿") in bstack1ll11l1l1l_opy_ and bstack1ll11l1l1l_opy_[bstack1l1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭เ")] != bstack1l1ll_opy_ (u"ࠩࠪแ"):
    return bstack1ll11l1l1l_opy_[bstack1l1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨโ")]
  else:
    bstack1l1ll11l1l_opy_ = bstack1l1ll_opy_ (u"ࠦࠧใ")
    if bstack1l1ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬไ") in bstack1ll11l1l1l_opy_ and bstack1ll11l1l1l_opy_[bstack1l1ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ๅ")] != None:
      bstack1l1ll11l1l_opy_ += bstack1ll11l1l1l_opy_[bstack1l1ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧๆ")] + bstack1l1ll_opy_ (u"ࠣ࠮ࠣࠦ็")
      if bstack1ll11l1l1l_opy_[bstack1l1ll_opy_ (u"ࠩࡲࡷ่ࠬ")] == bstack1l1ll_opy_ (u"ࠥ࡭ࡴࡹ้ࠢ"):
        bstack1l1ll11l1l_opy_ += bstack1l1ll_opy_ (u"ࠦ࡮ࡕࡓࠡࠤ๊")
      bstack1l1ll11l1l_opy_ += (bstack1ll11l1l1l_opy_[bstack1l1ll_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯๋ࠩ")] or bstack1l1ll_opy_ (u"࠭ࠧ์"))
      return bstack1l1ll11l1l_opy_
    else:
      bstack1l1ll11l1l_opy_ += bstack1l11l11lll_opy_(bstack1ll11l1l1l_opy_[bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨํ")]) + bstack1l1ll_opy_ (u"ࠣࠢࠥ๎") + (
              bstack1ll11l1l1l_opy_[bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ๏")] or bstack1l1ll_opy_ (u"ࠪࠫ๐")) + bstack1l1ll_opy_ (u"ࠦ࠱ࠦࠢ๑")
      if bstack1ll11l1l1l_opy_[bstack1l1ll_opy_ (u"ࠬࡵࡳࠨ๒")] == bstack1l1ll_opy_ (u"ࠨࡗࡪࡰࡧࡳࡼࡹࠢ๓"):
        bstack1l1ll11l1l_opy_ += bstack1l1ll_opy_ (u"ࠢࡘ࡫ࡱࠤࠧ๔")
      bstack1l1ll11l1l_opy_ += bstack1ll11l1l1l_opy_[bstack1l1ll_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ๕")] or bstack1l1ll_opy_ (u"ࠩࠪ๖")
      return bstack1l1ll11l1l_opy_
@measure(event_name=EVENTS.bstack1l11l1lll1_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1ll1l1lll1_opy_(bstack1ll11lll11_opy_):
  if bstack1ll11lll11_opy_ == bstack1l1ll_opy_ (u"ࠥࡨࡴࡴࡥࠣ๗"):
    return bstack1l1ll_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡧࡳࡧࡨࡲࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡧࡳࡧࡨࡲࠧࡄࡃࡰ࡯ࡳࡰࡪࡺࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ๘")
  elif bstack1ll11lll11_opy_ == bstack1l1ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ๙"):
    return bstack1l1ll_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡴࡨࡨࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡲࡦࡦࠥࡂࡋࡧࡩ࡭ࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩ๚")
  elif bstack1ll11lll11_opy_ == bstack1l1ll_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ๛"):
    return bstack1l1ll_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽࡫ࡷ࡫ࡥ࡯࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥ࡫ࡷ࡫ࡥ࡯ࠤࡁࡔࡦࡹࡳࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ๜")
  elif bstack1ll11lll11_opy_ == bstack1l1ll_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣ๝"):
    return bstack1l1ll_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡸࡥࡥ࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡶࡪࡪࠢ࠿ࡇࡵࡶࡴࡸ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬ๞")
  elif bstack1ll11lll11_opy_ == bstack1l1ll_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧ๟"):
    return bstack1l1ll_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࠤࡧࡨࡥ࠸࠸࠶࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࠦࡩࡪࡧ࠳࠳࠸ࠥࡂ࡙࡯࡭ࡦࡱࡸࡸࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪ๠")
  elif bstack1ll11lll11_opy_ == bstack1l1ll_opy_ (u"ࠨࡲࡶࡰࡱ࡭ࡳ࡭ࠢ๡"):
    return bstack1l1ll_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࡕࡹࡳࡴࡩ࡯ࡩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ๢")
  else:
    return bstack1l1ll_opy_ (u"ࠨ࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡧࡲࡡࡤ࡭࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡧࡲࡡࡤ࡭ࠥࡂࠬ๣") + bstack1l11l11lll_opy_(
      bstack1ll11lll11_opy_) + bstack1l1ll_opy_ (u"ࠩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ๤")
def bstack1l111llll_opy_(session):
  return bstack1l1ll_opy_ (u"ࠪࡀࡹࡸࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡳࡱࡺࠦࡃࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠠࡴࡧࡶࡷ࡮ࡵ࡮࠮ࡰࡤࡱࡪࠨ࠾࠽ࡣࠣ࡬ࡷ࡫ࡦ࠾ࠤࡾࢁࠧࠦࡴࡢࡴࡪࡩࡹࡃࠢࡠࡤ࡯ࡥࡳࡱࠢ࠿ࡽࢀࡀ࠴ࡧ࠾࠽࠱ࡷࡨࡃࢁࡽࡼࡿ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁ࠵ࡴࡳࡀࠪ๥").format(
    session[bstack1l1ll_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨ๦")], bstack11l1ll11_opy_(session), bstack1ll1l1lll1_opy_(session[bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡸࡺࡡࡵࡷࡶࠫ๧")]),
    bstack1ll1l1lll1_opy_(session[bstack1l1ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭๨")]),
    bstack1l11l11lll_opy_(session[bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ๩")] or session[bstack1l1ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ๪")] or bstack1l1ll_opy_ (u"ࠩࠪ๫")) + bstack1l1ll_opy_ (u"ࠥࠤࠧ๬") + (session[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭๭")] or bstack1l1ll_opy_ (u"ࠬ࠭๮")),
    session[bstack1l1ll_opy_ (u"࠭࡯ࡴࠩ๯")] + bstack1l1ll_opy_ (u"ࠢࠡࠤ๰") + session[bstack1l1ll_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ๱")], session[bstack1l1ll_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫ๲")] or bstack1l1ll_opy_ (u"ࠪࠫ๳"),
    session[bstack1l1ll_opy_ (u"ࠫࡨࡸࡥࡢࡶࡨࡨࡤࡧࡴࠨ๴")] if session[bstack1l1ll_opy_ (u"ࠬࡩࡲࡦࡣࡷࡩࡩࡥࡡࡵࠩ๵")] else bstack1l1ll_opy_ (u"࠭ࠧ๶"))
@measure(event_name=EVENTS.bstack1l11llll1_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1llll11ll_opy_(sessions, bstack1l1ll111l1_opy_):
  try:
    bstack11l1ll1l_opy_ = bstack1l1ll_opy_ (u"ࠢࠣ๷")
    if not os.path.exists(bstack1l11lllll_opy_):
      os.mkdir(bstack1l11lllll_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1ll_opy_ (u"ࠨࡣࡶࡷࡪࡺࡳ࠰ࡴࡨࡴࡴࡸࡴ࠯ࡪࡷࡱࡱ࠭๸")), bstack1l1ll_opy_ (u"ࠩࡵࠫ๹")) as f:
      bstack11l1ll1l_opy_ = f.read()
    bstack11l1ll1l_opy_ = bstack11l1ll1l_opy_.replace(bstack1l1ll_opy_ (u"ࠪࡿࠪࡘࡅࡔࡗࡏࡘࡘࡥࡃࡐࡗࡑࡘࠪࢃࠧ๺"), str(len(sessions)))
    bstack11l1ll1l_opy_ = bstack11l1ll1l_opy_.replace(bstack1l1ll_opy_ (u"ࠫࢀࠫࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠧࢀࠫ๻"), bstack1l1ll111l1_opy_)
    bstack11l1ll1l_opy_ = bstack11l1ll1l_opy_.replace(bstack1l1ll_opy_ (u"ࠬࢁࠥࡃࡗࡌࡐࡉࡥࡎࡂࡏࡈࠩࢂ࠭๼"),
                                              sessions[0].get(bstack1l1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡴࡡ࡮ࡧࠪ๽")) if sessions[0] else bstack1l1ll_opy_ (u"ࠧࠨ๾"))
    with open(os.path.join(bstack1l11lllll_opy_, bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡳࡧࡳࡳࡷࡺ࠮ࡩࡶࡰࡰࠬ๿")), bstack1l1ll_opy_ (u"ࠩࡺࠫ຀")) as stream:
      stream.write(bstack11l1ll1l_opy_.split(bstack1l1ll_opy_ (u"ࠪࡿ࡙ࠪࡅࡔࡕࡌࡓࡓ࡙࡟ࡅࡃࡗࡅࠪࢃࠧກ"))[0])
      for session in sessions:
        stream.write(bstack1l111llll_opy_(session))
      stream.write(bstack11l1ll1l_opy_.split(bstack1l1ll_opy_ (u"ࠫࢀࠫࡓࡆࡕࡖࡍࡔࡔࡓࡠࡆࡄࡘࡆࠫࡽࠨຂ"))[1])
    logger.info(bstack1l1ll_opy_ (u"ࠬࡍࡥ࡯ࡧࡵࡥࡹ࡫ࡤࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡣࡷ࡬ࡰࡩࠦࡡࡳࡶ࡬ࡪࡦࡩࡴࡴࠢࡤࡸࠥࢁࡽࠨ຃").format(bstack1l11lllll_opy_));
  except Exception as e:
    logger.debug(bstack11l1ll1l11_opy_.format(str(e)))
def bstack1lll111111_opy_(hashed_id):
  global CONFIG
  try:
    bstack11l1l1111_opy_ = datetime.datetime.now()
    host = bstack1l1ll_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡲ࡬࠱ࡨࡲ࡯ࡶࡦ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ຄ") if bstack1l1ll_opy_ (u"ࠧࡢࡲࡳࠫ຅") in CONFIG else bstack1l1ll_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩຆ")
    user = CONFIG[bstack1l1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫງ")]
    key = CONFIG[bstack1l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ຈ")]
    bstack11lll1llll_opy_ = bstack1l1ll_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪຉ") if bstack1l1ll_opy_ (u"ࠬࡧࡰࡱࠩຊ") in CONFIG else (bstack1l1ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪ຋") if CONFIG.get(bstack1l1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫຌ")) else bstack1l1ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪຍ"))
    host = bstack1lll1ll1ll_opy_(cli.config, [bstack1l1ll_opy_ (u"ࠤࡤࡴ࡮ࡹࠢຎ"), bstack1l1ll_opy_ (u"ࠥࡥࡵࡶࡁࡶࡶࡲࡱࡦࡺࡥࠣຏ"), bstack1l1ll_opy_ (u"ࠦࡦࡶࡩࠣຐ")], host) if bstack1l1ll_opy_ (u"ࠬࡧࡰࡱࠩຑ") in CONFIG else bstack1lll1ll1ll_opy_(cli.config, [bstack1l1ll_opy_ (u"ࠨࡡࡱ࡫ࡶࠦຒ"), bstack1l1ll_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡦࠤຓ"), bstack1l1ll_opy_ (u"ࠣࡣࡳ࡭ࠧດ")], host)
    url = bstack1l1ll_opy_ (u"ࠩࡾࢁ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡸ࡫ࡳࡴ࡫ࡲࡲࡸ࠴ࡪࡴࡱࡱࠫຕ").format(host, bstack11lll1llll_opy_, hashed_id)
    headers = {
      bstack1l1ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩຖ"): bstack1l1ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧທ"),
    }
    proxies = bstack11ll1llll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࡫ࡪࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࡡ࡯࡭ࡸࡺࠢຘ"), datetime.datetime.now() - bstack11l1l1111_opy_)
      return list(map(lambda session: session[bstack1l1ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࠫນ")], response.json()))
  except Exception as e:
    logger.debug(bstack1ll1ll1111_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack11111l1l_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def get_build_link():
  global CONFIG
  global bstack1l1l1lll1_opy_
  try:
    if bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪບ") in CONFIG:
      bstack11l1l1111_opy_ = datetime.datetime.now()
      host = bstack1l1ll_opy_ (u"ࠨࡣࡳ࡭࠲ࡩ࡬ࡰࡷࡧࠫປ") if bstack1l1ll_opy_ (u"ࠩࡤࡴࡵ࠭ຜ") in CONFIG else bstack1l1ll_opy_ (u"ࠪࡥࡵ࡯ࠧຝ")
      user = CONFIG[bstack1l1ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ພ")]
      key = CONFIG[bstack1l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨຟ")]
      bstack11lll1llll_opy_ = bstack1l1ll_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬຠ") if bstack1l1ll_opy_ (u"ࠧࡢࡲࡳࠫມ") in CONFIG else bstack1l1ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪຢ")
      url = bstack1l1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡿࢂࡀࡻࡾࡂࡾࢁ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡽࢀ࠳ࡧࡻࡩ࡭ࡦࡶ࠲࡯ࡹ࡯࡯ࠩຣ").format(user, key, host, bstack11lll1llll_opy_)
      if cli.is_enabled(CONFIG):
        bstack1l1ll111l1_opy_, hashed_id = cli.bstack1l1lllllll_opy_()
        logger.info(bstack11lll1l1l_opy_.format(bstack1l1ll111l1_opy_))
        return [hashed_id, bstack1l1ll111l1_opy_]
      else:
        headers = {
          bstack1l1ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩ຤"): bstack1l1ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧລ"),
        }
        if bstack1l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ຦") in CONFIG:
          params = {bstack1l1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫວ"): CONFIG[bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪຨ")], bstack1l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫຩ"): CONFIG[bstack1l1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫສ")]}
        else:
          params = {bstack1l1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨຫ"): CONFIG[bstack1l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧຬ")]}
        proxies = bstack11ll1llll_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack11llll111l_opy_ = response.json()[0][bstack1l1ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡥࡹ࡮ࡲࡤࠨອ")]
          if bstack11llll111l_opy_:
            bstack1l1ll111l1_opy_ = bstack11llll111l_opy_[bstack1l1ll_opy_ (u"࠭ࡰࡶࡤ࡯࡭ࡨࡥࡵࡳ࡮ࠪຮ")].split(bstack1l1ll_opy_ (u"ࠧࡱࡷࡥࡰ࡮ࡩ࠭ࡣࡷ࡬ࡰࡩ࠭ຯ"))[0] + bstack1l1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡳ࠰ࠩະ") + bstack11llll111l_opy_[
              bstack1l1ll_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬັ")]
            logger.info(bstack11lll1l1l_opy_.format(bstack1l1ll111l1_opy_))
            bstack1l1l1lll1_opy_ = bstack11llll111l_opy_[bstack1l1ll_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭າ")]
            bstack11l111ll11_opy_ = CONFIG[bstack1l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧຳ")]
            if bstack1l1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧິ") in CONFIG:
              bstack11l111ll11_opy_ += bstack1l1ll_opy_ (u"࠭ࠠࠨີ") + CONFIG[bstack1l1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩຶ")]
            if bstack11l111ll11_opy_ != bstack11llll111l_opy_[bstack1l1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ື")]:
              logger.debug(bstack11l1lll1ll_opy_.format(bstack11llll111l_opy_[bstack1l1ll_opy_ (u"ࠩࡱࡥࡲ࡫ຸࠧ")], bstack11l111ll11_opy_))
            cli.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡩࡨࡸࡤࡨࡵࡪ࡮ࡧࡣࡱ࡯࡮࡬ࠤູ"), datetime.datetime.now() - bstack11l1l1111_opy_)
            return [bstack11llll111l_opy_[bstack1l1ll_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪ຺ࠧ")], bstack1l1ll111l1_opy_]
    else:
      logger.warn(bstack11l1l1ll_opy_)
  except Exception as e:
    logger.debug(bstack11l1l1l11l_opy_.format(str(e)))
  return [None, None]
def bstack11lll11l_opy_(url, bstack1l1l1lll_opy_=False):
  global CONFIG
  global bstack1l1lll1ll_opy_
  if not bstack1l1lll1ll_opy_:
    hostname = bstack1lll111lll_opy_(url)
    is_private = bstack11l1l1111l_opy_(hostname)
    if (bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩົ") in CONFIG and not bstack1ll1l11l_opy_(CONFIG[bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪຼ")])) and (is_private or bstack1l1l1lll_opy_):
      bstack1l1lll1ll_opy_ = hostname
def bstack1lll111lll_opy_(url):
  return urlparse(url).hostname
def bstack11l1l1111l_opy_(hostname):
  for bstack1l11l1ll11_opy_ in bstack11lllll1ll_opy_:
    regex = re.compile(bstack1l11l1ll11_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack111l1l1l_opy_(bstack1lllll11_opy_):
  return True if bstack1lllll11_opy_ in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack11l1l1l11_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack11ll1ll111_opy_
  bstack111l11l1_opy_ = not (bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫຽ"), None) and bstack11ll1ll11_opy_(
          threading.current_thread(), bstack1l1ll_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ຾"), None))
  bstack111ll1l1l_opy_ = getattr(driver, bstack1l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩ຿"), None) != True
  bstack11l1111ll_opy_ = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪເ"), None) and bstack11ll1ll11_opy_(
          threading.current_thread(), bstack1l1ll_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ແ"), None)
  if bstack11l1111ll_opy_:
    if not bstack11l1111lll_opy_():
      logger.warning(bstack1l1ll_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳ࠯ࠤໂ"))
      return {}
    logger.debug(bstack1l1ll_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪໃ"))
    logger.debug(perform_scan(driver, driver_command=bstack1l1ll_opy_ (u"ࠧࡦࡺࡨࡧࡺࡺࡥࡔࡥࡵ࡭ࡵࡺࠧໄ")))
    results = bstack11l11l11l1_opy_(bstack1l1ll_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡴࠤ໅"))
    if results is not None and results.get(bstack1l1ll_opy_ (u"ࠤ࡬ࡷࡸࡻࡥࡴࠤໆ")) is not None:
        return results[bstack1l1ll_opy_ (u"ࠥ࡭ࡸࡹࡵࡦࡵࠥ໇")]
    logger.error(bstack1l1ll_opy_ (u"ࠦࡓࡵࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡓࡧࡶࡹࡱࡺࡳࠡࡹࡨࡶࡪࠦࡦࡰࡷࡱࡨ࠳ࠨ່"))
    return []
  if not bstack111111l1l_opy_.bstack1l1ll11l11_opy_(CONFIG, bstack11ll1ll111_opy_) or (bstack111ll1l1l_opy_ and bstack111l11l1_opy_):
    logger.warning(bstack1l1ll_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹ࠮້ࠣ"))
    return {}
  try:
    logger.debug(bstack1l1ll_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵ໊ࠪ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack11111lll_opy_.bstack11l1l11l1_opy_)
    return results
  except Exception:
    logger.error(bstack1l1ll_opy_ (u"ࠢࡏࡱࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡼ࡫ࡲࡦࠢࡩࡳࡺࡴࡤ࠯ࠤ໋"))
    return {}
@measure(event_name=EVENTS.bstack1ll111l1ll_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack11ll1ll111_opy_
  bstack111l11l1_opy_ = not (bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ໌"), None) and bstack11ll1ll11_opy_(
          threading.current_thread(), bstack1l1ll_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨໍ"), None))
  bstack111ll1l1l_opy_ = getattr(driver, bstack1l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪ໎"), None) != True
  bstack11l1111ll_opy_ = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫ໏"), None) and bstack11ll1ll11_opy_(
          threading.current_thread(), bstack1l1ll_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ໐"), None)
  if bstack11l1111ll_opy_:
    if not bstack11l1111lll_opy_():
      logger.warning(bstack1l1ll_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻ࠱ࠦ໑"))
      return {}
    logger.debug(bstack1l1ll_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡸࡻ࡭࡮ࡣࡵࡽࠬ໒"))
    logger.debug(perform_scan(driver, driver_command=bstack1l1ll_opy_ (u"ࠨࡧࡻࡩࡨࡻࡴࡦࡕࡦࡶ࡮ࡶࡴࠨ໓")))
    results = bstack11l11l11l1_opy_(bstack1l1ll_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡕࡸࡱࡲࡧࡲࡺࠤ໔"))
    if results is not None and results.get(bstack1l1ll_opy_ (u"ࠥࡷࡺࡳ࡭ࡢࡴࡼࠦ໕")) is not None:
        return results[bstack1l1ll_opy_ (u"ࠦࡸࡻ࡭࡮ࡣࡵࡽࠧ໖")]
    logger.error(bstack1l1ll_opy_ (u"ࠧࡔ࡯ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡔࡨࡷࡺࡲࡴࡴࠢࡖࡹࡲࡳࡡࡳࡻࠣࡻࡦࡹࠠࡧࡱࡸࡲࡩ࠴ࠢ໗"))
    return {}
  if not bstack111111l1l_opy_.bstack1l1ll11l11_opy_(CONFIG, bstack11ll1ll111_opy_) or (bstack111ll1l1l_opy_ and bstack111l11l1_opy_):
    logger.warning(bstack1l1ll_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺ࠰ࠥ໘"))
    return {}
  try:
    logger.debug(bstack1l1ll_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡸࡻ࡭࡮ࡣࡵࡽࠬ໙"))
    logger.debug(perform_scan(driver))
    bstack1lll11l1ll_opy_ = driver.execute_async_script(bstack11111lll_opy_.bstack1ll11l11_opy_)
    return bstack1lll11l1ll_opy_
  except Exception:
    logger.error(bstack1l1ll_opy_ (u"ࠣࡐࡲࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡻ࡭࡮ࡣࡵࡽࠥࡽࡡࡴࠢࡩࡳࡺࡴࡤ࠯ࠤ໚"))
    return {}
def bstack11l1111lll_opy_():
  global CONFIG
  global bstack11ll1ll111_opy_
  bstack11lll111ll_opy_ = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ໛"), None) and bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬໜ"), None)
  if not bstack111111l1l_opy_.bstack1l1ll11l11_opy_(CONFIG, bstack11ll1ll111_opy_) or not bstack11lll111ll_opy_:
        logger.warning(bstack1l1ll_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡵࡩࡸࡻ࡬ࡵࡵ࠱ࠦໝ"))
        return False
  return True
def bstack11l11l11l1_opy_(bstack11lll1l1_opy_):
    bstack1l1l1llll1_opy_ = bstack11ll1ll1_opy_.current_test_uuid() if bstack11ll1ll1_opy_.current_test_uuid() else bstack11ll1llll1_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack11l1lll1l1_opy_(bstack1l1l1llll1_opy_, bstack11lll1l1_opy_))
        try:
            return future.result(timeout=bstack11ll1ll1l1_opy_)
        except TimeoutError:
            logger.error(bstack1l1ll_opy_ (u"࡚ࠧࡩ࡮ࡧࡲࡹࡹࠦࡡࡧࡶࡨࡶࠥࢁࡽࡴࠢࡺ࡬࡮ࡲࡥࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡖࡪࡹࡵ࡭ࡶࡶࠦໞ").format(bstack11ll1ll1l1_opy_))
        except Exception as ex:
            logger.debug(bstack1l1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡸࡥࡵࡴ࡬ࡩࡻ࡯࡮ࡨࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡿࢂ࠴ࠠࡆࡴࡵࡳࡷࠦ࠭ࠡࡽࢀࠦໟ").format(bstack11lll1l1_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack111ll1ll_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack11ll1ll111_opy_
  bstack111l11l1_opy_ = not (bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫ໠"), None) and bstack11ll1ll11_opy_(
          threading.current_thread(), bstack1l1ll_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ໡"), None))
  bstack1lll11l11_opy_ = not (bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ໢"), None) and bstack11ll1ll11_opy_(
          threading.current_thread(), bstack1l1ll_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ໣"), None))
  bstack111ll1l1l_opy_ = getattr(driver, bstack1l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫ໤"), None) != True
  if not bstack111111l1l_opy_.bstack1l1ll11l11_opy_(CONFIG, bstack11ll1ll111_opy_) or (bstack111ll1l1l_opy_ and bstack111l11l1_opy_ and bstack1lll11l11_opy_):
    logger.warning(bstack1l1ll_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷࡻ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡦࡥࡳ࠴ࠢ໥"))
    return {}
  try:
    bstack1llll111l1_opy_ = bstack1l1ll_opy_ (u"࠭ࡡࡱࡲࠪ໦") in CONFIG and CONFIG.get(bstack1l1ll_opy_ (u"ࠧࡢࡲࡳࠫ໧"), bstack1l1ll_opy_ (u"ࠨࠩ໨"))
    session_id = getattr(driver, bstack1l1ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩ࠭໩"), None)
    if not session_id:
      logger.warning(bstack1l1ll_opy_ (u"ࠥࡒࡴࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡊࡆࠣࡪࡴࡻ࡮ࡥࠢࡩࡳࡷࠦࡤࡳ࡫ࡹࡩࡷࠨ໪"))
      return {bstack1l1ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥ໫"): bstack1l1ll_opy_ (u"ࠧࡔ࡯ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡌࡈࠥ࡬࡯ࡶࡰࡧࠦ໬")}
    if bstack1llll111l1_opy_:
      try:
        bstack1ll11lll1l_opy_ = {
              bstack1l1ll_opy_ (u"࠭ࡴࡩࡌࡺࡸ࡙ࡵ࡫ࡦࡰࠪ໭"): os.environ.get(bstack1l1ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ໮"), os.environ.get(bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬ໯"), bstack1l1ll_opy_ (u"ࠩࠪ໰"))),
              bstack1l1ll_opy_ (u"ࠪࡸ࡭࡚ࡥࡴࡶࡕࡹࡳ࡛ࡵࡪࡦࠪ໱"): bstack11ll1ll1_opy_.current_test_uuid() if bstack11ll1ll1_opy_.current_test_uuid() else bstack11ll1llll1_opy_.current_hook_uuid(),
              bstack1l1ll_opy_ (u"ࠫࡦࡻࡴࡩࡊࡨࡥࡩ࡫ࡲࠨ໲"): os.environ.get(bstack1l1ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ໳")),
              bstack1l1ll_opy_ (u"࠭ࡳࡤࡣࡱࡘ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭໴"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack1l1ll_opy_ (u"ࠧࡵࡪࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬ໵"): os.environ.get(bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭໶"), bstack1l1ll_opy_ (u"ࠩࠪ໷")),
              bstack1l1ll_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪ໸"): kwargs.get(bstack1l1ll_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣࡨࡵ࡭࡮ࡣࡱࡨࠬ໹"), None) or bstack1l1ll_opy_ (u"ࠬ࠭໺")
          }
        if not hasattr(thread_local, bstack1l1ll_opy_ (u"࠭ࡢࡢࡵࡨࡣࡦࡶࡰࡠࡣ࠴࠵ࡾࡥࡳࡤࡴ࡬ࡴࡹ࠭໻")):
            scripts = {bstack1l1ll_opy_ (u"ࠧࡴࡥࡤࡲࠬ໼"): bstack11111lll_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack11ll11lll1_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack11ll11lll1_opy_[bstack1l1ll_opy_ (u"ࠨࡵࡦࡥࡳ࠭໽")] = bstack11ll11lll1_opy_[bstack1l1ll_opy_ (u"ࠩࡶࡧࡦࡴࠧ໾")] % json.dumps(bstack1ll11lll1l_opy_)
        bstack11111lll_opy_.bstack1111l1ll1_opy_(bstack11ll11lll1_opy_)
        bstack11111lll_opy_.store()
        bstack1l1111lll1_opy_ = driver.execute_script(bstack11111lll_opy_.perform_scan)
      except Exception as bstack1ll11111_opy_:
        logger.info(bstack1l1ll_opy_ (u"ࠥࡅࡵࡶࡩࡶ࡯ࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡨࡧ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤ࠻ࠢࠥ໿") + str(bstack1ll11111_opy_))
        bstack1l1111lll1_opy_ = {bstack1l1ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥༀ"): str(bstack1ll11111_opy_)}
    else:
      bstack1l1111lll1_opy_ = driver.execute_async_script(bstack11111lll_opy_.perform_scan, {bstack1l1ll_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࠬ༁"): kwargs.get(bstack1l1ll_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷࡥࡣࡰ࡯ࡰࡥࡳࡪࠧ༂"), None) or bstack1l1ll_opy_ (u"ࠧࠨ༃")})
    return bstack1l1111lll1_opy_
  except Exception as err:
    logger.error(bstack1l1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡷࡻ࡮ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡦࡥࡳ࠴ࠠࡼࡿࠥ༄").format(str(err)))
    return {}