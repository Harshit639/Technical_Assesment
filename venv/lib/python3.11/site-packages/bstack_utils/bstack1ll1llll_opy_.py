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
from bstack_utils.constants import bstack11ll11ll111_opy_
def bstack111ll111_opy_(bstack11ll11ll11l_opy_):
    from browserstack_sdk.sdk_cli.cli import cli
    from bstack_utils.helper import bstack1lll1ll1ll_opy_
    host = bstack1lll1ll1ll_opy_(cli.config, [bstack1l1ll_opy_ (u"ࠢࡢࡲ࡬ࡷࠧ᝚"), bstack1l1ll_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵࡧࠥ᝛"), bstack1l1ll_opy_ (u"ࠤࡤࡴ࡮ࠨ᝜")], bstack11ll11ll111_opy_)
    return bstack1l1ll_opy_ (u"ࠪࡿࢂ࠵ࡻࡾࠩ᝝").format(host, bstack11ll11ll11l_opy_)