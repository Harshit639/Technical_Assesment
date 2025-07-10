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
import os
from urllib.parse import urlparse
from bstack_utils.config import Config
from bstack_utils.messages import bstack111l1lll1ll_opy_
bstack11l1lll1_opy_ = Config.bstack11ll11ll1_opy_()
def bstack11111l1lll1_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11111ll1111_opy_(bstack11111l1llll_opy_, bstack11111ll111l_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11111l1llll_opy_):
        with open(bstack11111l1llll_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11111l1lll1_opy_(bstack11111l1llll_opy_):
        pac = get_pac(url=bstack11111l1llll_opy_)
    else:
        raise Exception(bstack1l1ll_opy_ (u"ࠫࡕࡧࡣࠡࡨ࡬ࡰࡪࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡧࡻ࡭ࡸࡺ࠺ࠡࡽࢀࠫẹ").format(bstack11111l1llll_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack1l1ll_opy_ (u"ࠧ࠾࠮࠹࠰࠻࠲࠽ࠨẺ"), 80))
        bstack11111l1ll1l_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11111l1ll1l_opy_ = bstack1l1ll_opy_ (u"࠭࠰࠯࠲࠱࠴࠳࠶ࠧẻ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11111ll111l_opy_, bstack11111l1ll1l_opy_)
    return proxy_url
def bstack1ll1111l1_opy_(config):
    return bstack1l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪẼ") in config or bstack1l1ll_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬẽ") in config
def bstack11llll1l11_opy_(config):
    if not bstack1ll1111l1_opy_(config):
        return
    if config.get(bstack1l1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬẾ")):
        return config.get(bstack1l1ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ế"))
    if config.get(bstack1l1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨỀ")):
        return config.get(bstack1l1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩề"))
def bstack11ll1llll_opy_(config, bstack11111ll111l_opy_):
    proxy = bstack11llll1l11_opy_(config)
    proxies = {}
    if config.get(bstack1l1ll_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩỂ")) or config.get(bstack1l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫể")):
        if proxy.endswith(bstack1l1ll_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭Ễ")):
            proxies = bstack11l1111l11_opy_(proxy, bstack11111ll111l_opy_)
        else:
            proxies = {
                bstack1l1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨễ"): proxy
            }
    bstack11l1lll1_opy_.bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵࠪỆ"), proxies)
    return proxies
def bstack11l1111l11_opy_(bstack11111l1llll_opy_, bstack11111ll111l_opy_):
    proxies = {}
    global bstack11111ll11l1_opy_
    if bstack1l1ll_opy_ (u"ࠫࡕࡇࡃࡠࡒࡕࡓ࡝࡟ࠧệ") in globals():
        return bstack11111ll11l1_opy_
    try:
        proxy = bstack11111ll1111_opy_(bstack11111l1llll_opy_, bstack11111ll111l_opy_)
        if bstack1l1ll_opy_ (u"ࠧࡊࡉࡓࡇࡆࡘࠧỈ") in proxy:
            proxies = {}
        elif bstack1l1ll_opy_ (u"ࠨࡈࡕࡖࡓࠦỉ") in proxy or bstack1l1ll_opy_ (u"ࠢࡉࡖࡗࡔࡘࠨỊ") in proxy or bstack1l1ll_opy_ (u"ࠣࡕࡒࡇࡐ࡙ࠢị") in proxy:
            bstack11111l1ll11_opy_ = proxy.split(bstack1l1ll_opy_ (u"ࠤࠣࠦỌ"))
            if bstack1l1ll_opy_ (u"ࠥ࠾࠴࠵ࠢọ") in bstack1l1ll_opy_ (u"ࠦࠧỎ").join(bstack11111l1ll11_opy_[1:]):
                proxies = {
                    bstack1l1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫỏ"): bstack1l1ll_opy_ (u"ࠨࠢỐ").join(bstack11111l1ll11_opy_[1:])
                }
            else:
                proxies = {
                    bstack1l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ố"): str(bstack11111l1ll11_opy_[0]).lower() + bstack1l1ll_opy_ (u"ࠣ࠼࠲࠳ࠧỒ") + bstack1l1ll_opy_ (u"ࠤࠥồ").join(bstack11111l1ll11_opy_[1:])
                }
        elif bstack1l1ll_opy_ (u"ࠥࡔࡗࡕࡘ࡚ࠤỔ") in proxy:
            bstack11111l1ll11_opy_ = proxy.split(bstack1l1ll_opy_ (u"ࠦࠥࠨổ"))
            if bstack1l1ll_opy_ (u"ࠧࡀ࠯࠰ࠤỖ") in bstack1l1ll_opy_ (u"ࠨࠢỗ").join(bstack11111l1ll11_opy_[1:]):
                proxies = {
                    bstack1l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭Ộ"): bstack1l1ll_opy_ (u"ࠣࠤộ").join(bstack11111l1ll11_opy_[1:])
                }
            else:
                proxies = {
                    bstack1l1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨỚ"): bstack1l1ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦớ") + bstack1l1ll_opy_ (u"ࠦࠧỜ").join(bstack11111l1ll11_opy_[1:])
                }
        else:
            proxies = {
                bstack1l1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫờ"): proxy
            }
    except Exception as e:
        print(bstack1l1ll_opy_ (u"ࠨࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠥỞ"), bstack111l1lll1ll_opy_.format(bstack11111l1llll_opy_, str(e)))
    bstack11111ll11l1_opy_ = proxies
    return proxies