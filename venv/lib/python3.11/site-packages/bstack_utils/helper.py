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
import collections
import datetime
import json
import os
import platform
import re
import subprocess
import traceback
import tempfile
import multiprocessing
import threading
import sys
import logging
from math import ceil
import urllib
from urllib.parse import urlparse
import copy
import zipfile
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import (bstack11lllll1ll_opy_, bstack1l111l11ll_opy_, bstack1lll1lll11_opy_,
                                    bstack11ll11111ll_opy_, bstack11l1ll111ll_opy_, bstack11l1llll11l_opy_, bstack11l1ll11l1l_opy_)
from bstack_utils.measure import measure
from bstack_utils.messages import bstack11l11l1ll_opy_, bstack11l1l1l1l_opy_
from bstack_utils.proxy import bstack11ll1llll_opy_, bstack11llll1l11_opy_
from bstack_utils.constants import *
from bstack_utils import bstack1l1111111_opy_
from bstack_utils.bstack1ll1llll_opy_ import bstack111ll111_opy_
from browserstack_sdk._version import __version__
bstack11l1lll1_opy_ = Config.bstack11ll11ll1_opy_()
logger = bstack1l1111111_opy_.get_logger(__name__, bstack1l1111111_opy_.bstack1ll1llll1l1_opy_())
def bstack11ll1l111ll_opy_(config):
    return config[bstack1l1ll_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ᫨")]
def bstack11ll1llllll_opy_(config):
    return config[bstack1l1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ᫩")]
def bstack11ll1l1l1_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack11l1111lll1_opy_(obj):
    values = []
    bstack11l11l11111_opy_ = re.compile(bstack1l1ll_opy_ (u"ࡴࠥࡢࡈ࡛ࡓࡕࡑࡐࡣ࡙ࡇࡇࡠ࡞ࡧ࠯ࠩࠨ᫪"), re.I)
    for key in obj.keys():
        if bstack11l11l11111_opy_.match(key):
            values.append(obj[key])
    return values
def bstack11l11l1l1ll_opy_(config):
    tags = []
    tags.extend(bstack11l1111lll1_opy_(os.environ))
    tags.extend(bstack11l1111lll1_opy_(config))
    return tags
def bstack11l1111llll_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack11l11ll1l11_opy_(bstack11l11l1l1l1_opy_):
    if not bstack11l11l1l1l1_opy_:
        return bstack1l1ll_opy_ (u"ࠪࠫ᫫")
    return bstack1l1ll_opy_ (u"ࠦࢀࢃࠠࠩࡽࢀ࠭ࠧ᫬").format(bstack11l11l1l1l1_opy_.name, bstack11l11l1l1l1_opy_.email)
def bstack11ll1ll1lll_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack11l111lll11_opy_ = repo.common_dir
        info = {
            bstack1l1ll_opy_ (u"ࠧࡹࡨࡢࠤ᫭"): repo.head.commit.hexsha,
            bstack1l1ll_opy_ (u"ࠨࡳࡩࡱࡵࡸࡤࡹࡨࡢࠤ᫮"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack1l1ll_opy_ (u"ࠢࡣࡴࡤࡲࡨ࡮ࠢ᫯"): repo.active_branch.name,
            bstack1l1ll_opy_ (u"ࠣࡶࡤ࡫ࠧ᫰"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack1l1ll_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡶࡨࡶࠧ᫱"): bstack11l11ll1l11_opy_(repo.head.commit.committer),
            bstack1l1ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡷࡩࡷࡥࡤࡢࡶࡨࠦ᫲"): repo.head.commit.committed_datetime.isoformat(),
            bstack1l1ll_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࠦ᫳"): bstack11l11ll1l11_opy_(repo.head.commit.author),
            bstack1l1ll_opy_ (u"ࠧࡧࡵࡵࡪࡲࡶࡤࡪࡡࡵࡧࠥ᫴"): repo.head.commit.authored_datetime.isoformat(),
            bstack1l1ll_opy_ (u"ࠨࡣࡰ࡯ࡰ࡭ࡹࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠢ᫵"): repo.head.commit.message,
            bstack1l1ll_opy_ (u"ࠢࡳࡱࡲࡸࠧ᫶"): repo.git.rev_parse(bstack1l1ll_opy_ (u"ࠣ࠯࠰ࡷ࡭ࡵࡷ࠮ࡶࡲࡴࡱ࡫ࡶࡦ࡮ࠥ᫷")),
            bstack1l1ll_opy_ (u"ࠤࡦࡳࡲࡳ࡯࡯ࡡࡪ࡭ࡹࡥࡤࡪࡴࠥ᫸"): bstack11l111lll11_opy_,
            bstack1l1ll_opy_ (u"ࠥࡻࡴࡸ࡫ࡵࡴࡨࡩࡤ࡭ࡩࡵࡡࡧ࡭ࡷࠨ᫹"): subprocess.check_output([bstack1l1ll_opy_ (u"ࠦ࡬࡯ࡴࠣ᫺"), bstack1l1ll_opy_ (u"ࠧࡸࡥࡷ࠯ࡳࡥࡷࡹࡥࠣ᫻"), bstack1l1ll_opy_ (u"ࠨ࠭࠮ࡩ࡬ࡸ࠲ࡩ࡯࡮࡯ࡲࡲ࠲ࡪࡩࡳࠤ᫼")]).strip().decode(
                bstack1l1ll_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭᫽")),
            bstack1l1ll_opy_ (u"ࠣ࡮ࡤࡷࡹࡥࡴࡢࡩࠥ᫾"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack1l1ll_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡵࡢࡷ࡮ࡴࡣࡦࡡ࡯ࡥࡸࡺ࡟ࡵࡣࡪࠦ᫿"): repo.git.rev_list(
                bstack1l1ll_opy_ (u"ࠥࡿࢂ࠴࠮ࡼࡿࠥᬀ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack11l11111ll1_opy_ = []
        for remote in remotes:
            bstack11l11l1llll_opy_ = {
                bstack1l1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᬁ"): remote.name,
                bstack1l1ll_opy_ (u"ࠧࡻࡲ࡭ࠤᬂ"): remote.url,
            }
            bstack11l11111ll1_opy_.append(bstack11l11l1llll_opy_)
        bstack11l11ll1l1l_opy_ = {
            bstack1l1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᬃ"): bstack1l1ll_opy_ (u"ࠢࡨ࡫ࡷࠦᬄ"),
            **info,
            bstack1l1ll_opy_ (u"ࠣࡴࡨࡱࡴࡺࡥࡴࠤᬅ"): bstack11l11111ll1_opy_
        }
        bstack11l11ll1l1l_opy_ = bstack11l11ll11ll_opy_(bstack11l11ll1l1l_opy_)
        return bstack11l11ll1l1l_opy_
    except git.InvalidGitRepositoryError:
        return {}
    except Exception as err:
        print(bstack1l1ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡲࡴࡺࡲࡡࡵ࡫ࡱ࡫ࠥࡍࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᬆ").format(err))
        return {}
def bstack11l11ll11ll_opy_(bstack11l11ll1l1l_opy_):
    bstack11l111ll11l_opy_ = bstack11l11ll111l_opy_(bstack11l11ll1l1l_opy_)
    if bstack11l111ll11l_opy_ and bstack11l111ll11l_opy_ > bstack11ll11111ll_opy_:
        bstack11l1111l1l1_opy_ = bstack11l111ll11l_opy_ - bstack11ll11111ll_opy_
        bstack111llllll1l_opy_ = bstack111llllll11_opy_(bstack11l11ll1l1l_opy_[bstack1l1ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡪࡶࡢࡱࡪࡹࡳࡢࡩࡨࠦᬇ")], bstack11l1111l1l1_opy_)
        bstack11l11ll1l1l_opy_[bstack1l1ll_opy_ (u"ࠦࡨࡵ࡭࡮࡫ࡷࡣࡲ࡫ࡳࡴࡣࡪࡩࠧᬈ")] = bstack111llllll1l_opy_
        logger.info(bstack1l1ll_opy_ (u"࡚ࠧࡨࡦࠢࡦࡳࡲࡳࡩࡵࠢ࡫ࡥࡸࠦࡢࡦࡧࡱࠤࡹࡸࡵ࡯ࡥࡤࡸࡪࡪ࠮ࠡࡕ࡬ࡾࡪࠦ࡯ࡧࠢࡦࡳࡲࡳࡩࡵࠢࡤࡪࡹ࡫ࡲࠡࡶࡵࡹࡳࡩࡡࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡽࢀࠤࡐࡈࠢᬉ")
                    .format(bstack11l11ll111l_opy_(bstack11l11ll1l1l_opy_) / 1024))
    return bstack11l11ll1l1l_opy_
def bstack11l11ll111l_opy_(bstack1ll111ll11_opy_):
    try:
        if bstack1ll111ll11_opy_:
            bstack11l11lll11l_opy_ = json.dumps(bstack1ll111ll11_opy_)
            bstack11l111ll1ll_opy_ = sys.getsizeof(bstack11l11lll11l_opy_)
            return bstack11l111ll1ll_opy_
    except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"ࠨࡓࡰ࡯ࡨࡸ࡭࡯࡮ࡨࠢࡺࡩࡳࡺࠠࡸࡴࡲࡲ࡬ࠦࡷࡩ࡫࡯ࡩࠥࡩࡡ࡭ࡥࡸࡰࡦࡺࡩ࡯ࡩࠣࡷ࡮ࢀࡥࠡࡱࡩࠤࡏ࡙ࡏࡏࠢࡲࡦ࡯࡫ࡣࡵ࠼ࠣࡿࢂࠨᬊ").format(e))
    return -1
def bstack111llllll11_opy_(field, bstack111lll1ll1l_opy_):
    try:
        bstack11l111111l1_opy_ = len(bytes(bstack11l1ll111ll_opy_, bstack1l1ll_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ᬋ")))
        bstack111llll1lll_opy_ = bytes(field, bstack1l1ll_opy_ (u"ࠨࡷࡷࡪ࠲࠾ࠧᬌ"))
        bstack111lll1lll1_opy_ = len(bstack111llll1lll_opy_)
        bstack11l111l1111_opy_ = ceil(bstack111lll1lll1_opy_ - bstack111lll1ll1l_opy_ - bstack11l111111l1_opy_)
        if bstack11l111l1111_opy_ > 0:
            bstack11l11l11l11_opy_ = bstack111llll1lll_opy_[:bstack11l111l1111_opy_].decode(bstack1l1ll_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨᬍ"), errors=bstack1l1ll_opy_ (u"ࠪ࡭࡬ࡴ࡯ࡳࡧࠪᬎ")) + bstack11l1ll111ll_opy_
            return bstack11l11l11l11_opy_
    except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡷࡶࡺࡴࡣࡢࡶ࡬ࡲ࡬ࠦࡦࡪࡧ࡯ࡨ࠱ࠦ࡮ࡰࡶ࡫࡭ࡳ࡭ࠠࡸࡣࡶࠤࡹࡸࡵ࡯ࡥࡤࡸࡪࡪࠠࡩࡧࡵࡩ࠿ࠦࡻࡾࠤᬏ").format(e))
    return field
def bstack1ll11llll_opy_():
    env = os.environ
    if (bstack1l1ll_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡕࡓࡎࠥᬐ") in env and len(env[bstack1l1ll_opy_ (u"ࠨࡊࡆࡐࡎࡍࡓ࡙࡟ࡖࡔࡏࠦᬑ")]) > 0) or (
            bstack1l1ll_opy_ (u"ࠢࡋࡇࡑࡏࡎࡔࡓࡠࡊࡒࡑࡊࠨᬒ") in env and len(env[bstack1l1ll_opy_ (u"ࠣࡌࡈࡒࡐࡏࡎࡔࡡࡋࡓࡒࡋࠢᬓ")]) > 0):
        return {
            bstack1l1ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᬔ"): bstack1l1ll_opy_ (u"ࠥࡎࡪࡴ࡫ࡪࡰࡶࠦᬕ"),
            bstack1l1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᬖ"): env.get(bstack1l1ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠣᬗ")),
            bstack1l1ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᬘ"): env.get(bstack1l1ll_opy_ (u"ࠢࡋࡑࡅࡣࡓࡇࡍࡆࠤᬙ")),
            bstack1l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᬚ"): env.get(bstack1l1ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣᬛ"))
        }
    if env.get(bstack1l1ll_opy_ (u"ࠥࡇࡎࠨᬜ")) == bstack1l1ll_opy_ (u"ࠦࡹࡸࡵࡦࠤᬝ") and bstack1ll1l11l_opy_(env.get(bstack1l1ll_opy_ (u"ࠧࡉࡉࡓࡅࡏࡉࡈࡏࠢᬞ"))):
        return {
            bstack1l1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᬟ"): bstack1l1ll_opy_ (u"ࠢࡄ࡫ࡵࡧࡱ࡫ࡃࡊࠤᬠ"),
            bstack1l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᬡ"): env.get(bstack1l1ll_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡡࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧᬢ")),
            bstack1l1ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᬣ"): env.get(bstack1l1ll_opy_ (u"ࠦࡈࡏࡒࡄࡎࡈࡣࡏࡕࡂࠣᬤ")),
            bstack1l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᬥ"): env.get(bstack1l1ll_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࠤᬦ"))
        }
    if env.get(bstack1l1ll_opy_ (u"ࠢࡄࡋࠥᬧ")) == bstack1l1ll_opy_ (u"ࠣࡶࡵࡹࡪࠨᬨ") and bstack1ll1l11l_opy_(env.get(bstack1l1ll_opy_ (u"ࠤࡗࡖࡆ࡜ࡉࡔࠤᬩ"))):
        return {
            bstack1l1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᬪ"): bstack1l1ll_opy_ (u"࡙ࠦࡸࡡࡷ࡫ࡶࠤࡈࡏࠢᬫ"),
            bstack1l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᬬ"): env.get(bstack1l1ll_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࡥࡂࡖࡋࡏࡈࡤ࡝ࡅࡃࡡࡘࡖࡑࠨᬭ")),
            bstack1l1ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᬮ"): env.get(bstack1l1ll_opy_ (u"ࠣࡖࡕࡅ࡛ࡏࡓࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥᬯ")),
            bstack1l1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᬰ"): env.get(bstack1l1ll_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᬱ"))
        }
    if env.get(bstack1l1ll_opy_ (u"ࠦࡈࡏࠢᬲ")) == bstack1l1ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᬳ") and env.get(bstack1l1ll_opy_ (u"ࠨࡃࡊࡡࡑࡅࡒࡋ᬴ࠢ")) == bstack1l1ll_opy_ (u"ࠢࡤࡱࡧࡩࡸ࡮ࡩࡱࠤᬵ"):
        return {
            bstack1l1ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᬶ"): bstack1l1ll_opy_ (u"ࠤࡆࡳࡩ࡫ࡳࡩ࡫ࡳࠦᬷ"),
            bstack1l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᬸ"): None,
            bstack1l1ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᬹ"): None,
            bstack1l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦᬺ"): None
        }
    if env.get(bstack1l1ll_opy_ (u"ࠨࡂࡊࡖࡅ࡙ࡈࡑࡅࡕࡡࡅࡖࡆࡔࡃࡉࠤᬻ")) and env.get(bstack1l1ll_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡇࡔࡓࡍࡊࡖࠥᬼ")):
        return {
            bstack1l1ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᬽ"): bstack1l1ll_opy_ (u"ࠤࡅ࡭ࡹࡨࡵࡤ࡭ࡨࡸࠧᬾ"),
            bstack1l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᬿ"): env.get(bstack1l1ll_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡈࡋࡗࡣࡍ࡚ࡔࡑࡡࡒࡖࡎࡍࡉࡏࠤᭀ")),
            bstack1l1ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᭁ"): None,
            bstack1l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᭂ"): env.get(bstack1l1ll_opy_ (u"ࠢࡃࡋࡗࡆ࡚ࡉࡋࡆࡖࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᭃ"))
        }
    if env.get(bstack1l1ll_opy_ (u"ࠣࡅࡌ᭄ࠦ")) == bstack1l1ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᭅ") and bstack1ll1l11l_opy_(env.get(bstack1l1ll_opy_ (u"ࠥࡈࡗࡕࡎࡆࠤᭆ"))):
        return {
            bstack1l1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᭇ"): bstack1l1ll_opy_ (u"ࠧࡊࡲࡰࡰࡨࠦᭈ"),
            bstack1l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᭉ"): env.get(bstack1l1ll_opy_ (u"ࠢࡅࡔࡒࡒࡊࡥࡂࡖࡋࡏࡈࡤࡒࡉࡏࡍࠥᭊ")),
            bstack1l1ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᭋ"): None,
            bstack1l1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᭌ"): env.get(bstack1l1ll_opy_ (u"ࠥࡈࡗࡕࡎࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣ᭍"))
        }
    if env.get(bstack1l1ll_opy_ (u"ࠦࡈࡏࠢ᭎")) == bstack1l1ll_opy_ (u"ࠧࡺࡲࡶࡧࠥ᭏") and bstack1ll1l11l_opy_(env.get(bstack1l1ll_opy_ (u"ࠨࡓࡆࡏࡄࡔࡍࡕࡒࡆࠤ᭐"))):
        return {
            bstack1l1ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ᭑"): bstack1l1ll_opy_ (u"ࠣࡕࡨࡱࡦࡶࡨࡰࡴࡨࠦ᭒"),
            bstack1l1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ᭓"): env.get(bstack1l1ll_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࡥࡏࡓࡉࡄࡒࡎࡠࡁࡕࡋࡒࡒࡤ࡛ࡒࡍࠤ᭔")),
            bstack1l1ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ᭕"): env.get(bstack1l1ll_opy_ (u"࡙ࠧࡅࡎࡃࡓࡌࡔࡘࡅࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥ᭖")),
            bstack1l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᭗"): env.get(bstack1l1ll_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡎࡔࡈ࡟ࡊࡆࠥ᭘"))
        }
    if env.get(bstack1l1ll_opy_ (u"ࠣࡅࡌࠦ᭙")) == bstack1l1ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ᭚") and bstack1ll1l11l_opy_(env.get(bstack1l1ll_opy_ (u"ࠥࡋࡎ࡚ࡌࡂࡄࡢࡇࡎࠨ᭛"))):
        return {
            bstack1l1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᭜"): bstack1l1ll_opy_ (u"ࠧࡍࡩࡵࡎࡤࡦࠧ᭝"),
            bstack1l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᭞"): env.get(bstack1l1ll_opy_ (u"ࠢࡄࡋࡢࡎࡔࡈ࡟ࡖࡔࡏࠦ᭟")),
            bstack1l1ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ᭠"): env.get(bstack1l1ll_opy_ (u"ࠤࡆࡍࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢ᭡")),
            bstack1l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ᭢"): env.get(bstack1l1ll_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣࡎࡊࠢ᭣"))
        }
    if env.get(bstack1l1ll_opy_ (u"ࠧࡉࡉࠣ᭤")) == bstack1l1ll_opy_ (u"ࠨࡴࡳࡷࡨࠦ᭥") and bstack1ll1l11l_opy_(env.get(bstack1l1ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࠥ᭦"))):
        return {
            bstack1l1ll_opy_ (u"ࠣࡰࡤࡱࡪࠨ᭧"): bstack1l1ll_opy_ (u"ࠤࡅࡹ࡮ࡲࡤ࡬࡫ࡷࡩࠧ᭨"),
            bstack1l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᭩"): env.get(bstack1l1ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥ᭪")),
            bstack1l1ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ᭫"): env.get(bstack1l1ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡏࡅࡇࡋࡌ᭬ࠣ")) or env.get(bstack1l1ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡑࡉࡕࡇࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡔࡁࡎࡇࠥ᭭")),
            bstack1l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᭮"): env.get(bstack1l1ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡌࡋࡗࡉࡤࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦ᭯"))
        }
    if bstack1ll1l11l_opy_(env.get(bstack1l1ll_opy_ (u"ࠥࡘࡋࡥࡂࡖࡋࡏࡈࠧ᭰"))):
        return {
            bstack1l1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᭱"): bstack1l1ll_opy_ (u"ࠧ࡜ࡩࡴࡷࡤࡰ࡙ࠥࡴࡶࡦ࡬ࡳ࡚ࠥࡥࡢ࡯ࠣࡗࡪࡸࡶࡪࡥࡨࡷࠧ᭲"),
            bstack1l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᭳"): bstack1l1ll_opy_ (u"ࠢࡼࡿࡾࢁࠧ᭴").format(env.get(bstack1l1ll_opy_ (u"ࠨࡕ࡜ࡗ࡙ࡋࡍࡠࡖࡈࡅࡒࡌࡏࡖࡐࡇࡅ࡙ࡏࡏࡏࡕࡈࡖ࡛ࡋࡒࡖࡔࡌࠫ᭵")), env.get(bstack1l1ll_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡐࡓࡑࡍࡉࡈ࡚ࡉࡅࠩ᭶"))),
            bstack1l1ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧ᭷"): env.get(bstack1l1ll_opy_ (u"ࠦࡘ࡟ࡓࡕࡇࡐࡣࡉࡋࡆࡊࡐࡌࡘࡎࡕࡎࡊࡆࠥ᭸")),
            bstack1l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ᭹"): env.get(bstack1l1ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨ᭺"))
        }
    if bstack1ll1l11l_opy_(env.get(bstack1l1ll_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࠤ᭻"))):
        return {
            bstack1l1ll_opy_ (u"ࠣࡰࡤࡱࡪࠨ᭼"): bstack1l1ll_opy_ (u"ࠤࡄࡴࡵࡼࡥࡺࡱࡵࠦ᭽"),
            bstack1l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ᭾"): bstack1l1ll_opy_ (u"ࠦࢀࢃ࠯ࡱࡴࡲ࡮ࡪࡩࡴ࠰ࡽࢀ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿࠥ᭿").format(env.get(bstack1l1ll_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡖࡔࡏࠫᮀ")), env.get(bstack1l1ll_opy_ (u"࠭ࡁࡑࡒ࡙ࡉ࡞ࡕࡒࡠࡃࡆࡇࡔ࡛ࡎࡕࡡࡑࡅࡒࡋࠧᮁ")), env.get(bstack1l1ll_opy_ (u"ࠧࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡓࡖࡔࡐࡅࡄࡖࡢࡗࡑ࡛ࡇࠨᮂ")), env.get(bstack1l1ll_opy_ (u"ࠨࡃࡓࡔ࡛ࡋ࡙ࡐࡔࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬᮃ"))),
            bstack1l1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᮄ"): env.get(bstack1l1ll_opy_ (u"ࠥࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢᮅ")),
            bstack1l1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᮆ"): env.get(bstack1l1ll_opy_ (u"ࠧࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨᮇ"))
        }
    if env.get(bstack1l1ll_opy_ (u"ࠨࡁ࡛ࡗࡕࡉࡤࡎࡔࡕࡒࡢ࡙ࡘࡋࡒࡠࡃࡊࡉࡓ࡚ࠢᮈ")) and env.get(bstack1l1ll_opy_ (u"ࠢࡕࡈࡢࡆ࡚ࡏࡌࡅࠤᮉ")):
        return {
            bstack1l1ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᮊ"): bstack1l1ll_opy_ (u"ࠤࡄࡾࡺࡸࡥࠡࡅࡌࠦᮋ"),
            bstack1l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᮌ"): bstack1l1ll_opy_ (u"ࠦࢀࢃࡻࡾ࠱ࡢࡦࡺ࡯࡬ࡥ࠱ࡵࡩࡸࡻ࡬ࡵࡵࡂࡦࡺ࡯࡬ࡥࡋࡧࡁࢀࢃࠢᮍ").format(env.get(bstack1l1ll_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡉࡓ࡚ࡔࡄࡂࡖࡌࡓࡓ࡙ࡅࡓࡘࡈࡖ࡚ࡘࡉࠨᮎ")), env.get(bstack1l1ll_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡔࡗࡕࡊࡆࡅࡗࠫᮏ")), env.get(bstack1l1ll_opy_ (u"ࠧࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡎࡊࠧᮐ"))),
            bstack1l1ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥᮑ"): env.get(bstack1l1ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊࡉࡅࠤᮒ")),
            bstack1l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤᮓ"): env.get(bstack1l1ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠦᮔ"))
        }
    if any([env.get(bstack1l1ll_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᮕ")), env.get(bstack1l1ll_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡕࡉࡘࡕࡌࡗࡇࡇࡣࡘࡕࡕࡓࡅࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࠧᮖ")), env.get(bstack1l1ll_opy_ (u"ࠢࡄࡑࡇࡉࡇ࡛ࡉࡍࡆࡢࡗࡔ࡛ࡒࡄࡇࡢ࡚ࡊࡘࡓࡊࡑࡑࠦᮗ"))]):
        return {
            bstack1l1ll_opy_ (u"ࠣࡰࡤࡱࡪࠨᮘ"): bstack1l1ll_opy_ (u"ࠤࡄ࡛ࡘࠦࡃࡰࡦࡨࡆࡺ࡯࡬ࡥࠤᮙ"),
            bstack1l1ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨᮚ"): env.get(bstack1l1ll_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡑࡗࡅࡐࡎࡉ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥᮛ")),
            bstack1l1ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢᮜ"): env.get(bstack1l1ll_opy_ (u"ࠨࡃࡐࡆࡈࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᮝ")),
            bstack1l1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨᮞ"): env.get(bstack1l1ll_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨᮟ"))
        }
    if env.get(bstack1l1ll_opy_ (u"ࠤࡥࡥࡲࡨ࡯ࡰࡡࡥࡹ࡮ࡲࡤࡏࡷࡰࡦࡪࡸࠢᮠ")):
        return {
            bstack1l1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣᮡ"): bstack1l1ll_opy_ (u"ࠦࡇࡧ࡭ࡣࡱࡲࠦᮢ"),
            bstack1l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣᮣ"): env.get(bstack1l1ll_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡗ࡫ࡳࡶ࡮ࡷࡷ࡚ࡸ࡬ࠣᮤ")),
            bstack1l1ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᮥ"): env.get(bstack1l1ll_opy_ (u"ࠣࡤࡤࡱࡧࡵ࡯ࡠࡵ࡫ࡳࡷࡺࡊࡰࡤࡑࡥࡲ࡫ࠢᮦ")),
            bstack1l1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᮧ"): env.get(bstack1l1ll_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡐࡸࡱࡧ࡫ࡲࠣᮨ"))
        }
    if env.get(bstack1l1ll_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࠧᮩ")) or env.get(bstack1l1ll_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡍࡂࡋࡑࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡓࡕࡃࡕࡘࡊࡊ᮪ࠢ")):
        return {
            bstack1l1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨ᮫ࠦ"): bstack1l1ll_opy_ (u"ࠢࡘࡧࡵࡧࡰ࡫ࡲࠣᮬ"),
            bstack1l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᮭ"): env.get(bstack1l1ll_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠨᮮ")),
            bstack1l1ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᮯ"): bstack1l1ll_opy_ (u"ࠦࡒࡧࡩ࡯ࠢࡓ࡭ࡵ࡫࡬ࡪࡰࡨࠦ᮰") if env.get(bstack1l1ll_opy_ (u"ࠧ࡝ࡅࡓࡅࡎࡉࡗࡥࡍࡂࡋࡑࡣࡕࡏࡐࡆࡎࡌࡒࡊࡥࡓࡕࡃࡕࡘࡊࡊࠢ᮱")) else None,
            bstack1l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ᮲"): env.get(bstack1l1ll_opy_ (u"ࠢࡘࡇࡕࡇࡐࡋࡒࡠࡉࡌࡘࡤࡉࡏࡎࡏࡌࡘࠧ᮳"))
        }
    if any([env.get(bstack1l1ll_opy_ (u"ࠣࡉࡆࡔࡤࡖࡒࡐࡌࡈࡇ࡙ࠨ᮴")), env.get(bstack1l1ll_opy_ (u"ࠤࡊࡇࡑࡕࡕࡅࡡࡓࡖࡔࡐࡅࡄࡖࠥ᮵")), env.get(bstack1l1ll_opy_ (u"ࠥࡋࡔࡕࡇࡍࡇࡢࡇࡑࡕࡕࡅࡡࡓࡖࡔࡐࡅࡄࡖࠥ᮶"))]):
        return {
            bstack1l1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᮷"): bstack1l1ll_opy_ (u"ࠧࡍ࡯ࡰࡩ࡯ࡩࠥࡉ࡬ࡰࡷࡧࠦ᮸"),
            bstack1l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᮹"): None,
            bstack1l1ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᮺ"): env.get(bstack1l1ll_opy_ (u"ࠣࡒࡕࡓࡏࡋࡃࡕࡡࡌࡈࠧᮻ")),
            bstack1l1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᮼ"): env.get(bstack1l1ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡌࡈࠧᮽ"))
        }
    if env.get(bstack1l1ll_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋࠢᮾ")):
        return {
            bstack1l1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᮿ"): bstack1l1ll_opy_ (u"ࠨࡓࡩ࡫ࡳࡴࡦࡨ࡬ࡦࠤᯀ"),
            bstack1l1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᯁ"): env.get(bstack1l1ll_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᯂ")),
            bstack1l1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᯃ"): bstack1l1ll_opy_ (u"ࠥࡎࡴࡨࠠࠤࡽࢀࠦᯄ").format(env.get(bstack1l1ll_opy_ (u"ࠫࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡋࡑࡅࡣࡎࡊࠧᯅ"))) if env.get(bstack1l1ll_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡌࡒࡆࡤࡏࡄࠣᯆ")) else None,
            bstack1l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᯇ"): env.get(bstack1l1ll_opy_ (u"ࠢࡔࡊࡌࡔࡕࡇࡂࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࠤᯈ"))
        }
    if bstack1ll1l11l_opy_(env.get(bstack1l1ll_opy_ (u"ࠣࡐࡈࡘࡑࡏࡆ࡚ࠤᯉ"))):
        return {
            bstack1l1ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢᯊ"): bstack1l1ll_opy_ (u"ࠥࡒࡪࡺ࡬ࡪࡨࡼࠦᯋ"),
            bstack1l1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢᯌ"): env.get(bstack1l1ll_opy_ (u"ࠧࡊࡅࡑࡎࡒ࡝ࡤ࡛ࡒࡍࠤᯍ")),
            bstack1l1ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣᯎ"): env.get(bstack1l1ll_opy_ (u"ࠢࡔࡋࡗࡉࡤࡔࡁࡎࡇࠥᯏ")),
            bstack1l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢᯐ"): env.get(bstack1l1ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡋࡇࠦᯑ"))
        }
    if bstack1ll1l11l_opy_(env.get(bstack1l1ll_opy_ (u"ࠥࡋࡎ࡚ࡈࡖࡄࡢࡅࡈ࡚ࡉࡐࡐࡖࠦᯒ"))):
        return {
            bstack1l1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤᯓ"): bstack1l1ll_opy_ (u"ࠧࡍࡩࡵࡊࡸࡦࠥࡇࡣࡵ࡫ࡲࡲࡸࠨᯔ"),
            bstack1l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤᯕ"): bstack1l1ll_opy_ (u"ࠢࡼࡿ࠲ࡿࢂ࠵ࡡࡤࡶ࡬ࡳࡳࡹ࠯ࡳࡷࡱࡷ࠴ࢁࡽࠣᯖ").format(env.get(bstack1l1ll_opy_ (u"ࠨࡉࡌࡘࡍ࡛ࡂࡠࡕࡈࡖ࡛ࡋࡒࡠࡗࡕࡐࠬᯗ")), env.get(bstack1l1ll_opy_ (u"ࠩࡊࡍ࡙ࡎࡕࡃࡡࡕࡉࡕࡕࡓࡊࡖࡒࡖ࡞࠭ᯘ")), env.get(bstack1l1ll_opy_ (u"ࠪࡋࡎ࡚ࡈࡖࡄࡢࡖ࡚ࡔ࡟ࡊࡆࠪᯙ"))),
            bstack1l1ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨᯚ"): env.get(bstack1l1ll_opy_ (u"ࠧࡍࡉࡕࡊࡘࡆࡤ࡝ࡏࡓࡍࡉࡐࡔ࡝ࠢᯛ")),
            bstack1l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᯜ"): env.get(bstack1l1ll_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡗࡑࡣࡎࡊࠢᯝ"))
        }
    if env.get(bstack1l1ll_opy_ (u"ࠣࡅࡌࠦᯞ")) == bstack1l1ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᯟ") and env.get(bstack1l1ll_opy_ (u"࡚ࠥࡊࡘࡃࡆࡎࠥᯠ")) == bstack1l1ll_opy_ (u"ࠦ࠶ࠨᯡ"):
        return {
            bstack1l1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᯢ"): bstack1l1ll_opy_ (u"ࠨࡖࡦࡴࡦࡩࡱࠨᯣ"),
            bstack1l1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᯤ"): bstack1l1ll_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࡽࢀࠦᯥ").format(env.get(bstack1l1ll_opy_ (u"࡙ࠩࡉࡗࡉࡅࡍࡡࡘࡖࡑ᯦࠭"))),
            bstack1l1ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧᯧ"): None,
            bstack1l1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᯨ"): None,
        }
    if env.get(bstack1l1ll_opy_ (u"࡚ࠧࡅࡂࡏࡆࡍ࡙࡟࡟ࡗࡇࡕࡗࡎࡕࡎࠣᯩ")):
        return {
            bstack1l1ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦᯪ"): bstack1l1ll_opy_ (u"ࠢࡕࡧࡤࡱࡨ࡯ࡴࡺࠤᯫ"),
            bstack1l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦᯬ"): None,
            bstack1l1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᯭ"): env.get(bstack1l1ll_opy_ (u"ࠥࡘࡊࡇࡍࡄࡋࡗ࡝ࡤࡖࡒࡐࡌࡈࡇ࡙ࡥࡎࡂࡏࡈࠦᯮ")),
            bstack1l1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᯯ"): env.get(bstack1l1ll_opy_ (u"ࠧࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࠦᯰ"))
        }
    if any([env.get(bstack1l1ll_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࠤᯱ")), env.get(bstack1l1ll_opy_ (u"ࠢࡄࡑࡑࡇࡔ࡛ࡒࡔࡇࡢ࡙ࡗࡒ᯲ࠢ")), env.get(bstack1l1ll_opy_ (u"ࠣࡅࡒࡒࡈࡕࡕࡓࡕࡈࡣ࡚࡙ࡅࡓࡐࡄࡑࡊࠨ᯳")), env.get(bstack1l1ll_opy_ (u"ࠤࡆࡓࡓࡉࡏࡖࡔࡖࡉࡤ࡚ࡅࡂࡏࠥ᯴"))]):
        return {
            bstack1l1ll_opy_ (u"ࠥࡲࡦࡳࡥࠣ᯵"): bstack1l1ll_opy_ (u"ࠦࡈࡵ࡮ࡤࡱࡸࡶࡸ࡫ࠢ᯶"),
            bstack1l1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ᯷"): None,
            bstack1l1ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ᯸"): env.get(bstack1l1ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣ᯹")) or None,
            bstack1l1ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ᯺"): env.get(bstack1l1ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡋࡇࠦ᯻"), 0)
        }
    if env.get(bstack1l1ll_opy_ (u"ࠥࡋࡔࡥࡊࡐࡄࡢࡒࡆࡓࡅࠣ᯼")):
        return {
            bstack1l1ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ᯽"): bstack1l1ll_opy_ (u"ࠧࡍ࡯ࡄࡆࠥ᯾"),
            bstack1l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ᯿"): None,
            bstack1l1ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤᰀ"): env.get(bstack1l1ll_opy_ (u"ࠣࡉࡒࡣࡏࡕࡂࡠࡐࡄࡑࡊࠨᰁ")),
            bstack1l1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣᰂ"): env.get(bstack1l1ll_opy_ (u"ࠥࡋࡔࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡅࡒ࡙ࡓ࡚ࡅࡓࠤᰃ"))
        }
    if env.get(bstack1l1ll_opy_ (u"ࠦࡈࡌ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠤᰄ")):
        return {
            bstack1l1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥᰅ"): bstack1l1ll_opy_ (u"ࠨࡃࡰࡦࡨࡊࡷ࡫ࡳࡩࠤᰆ"),
            bstack1l1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥᰇ"): env.get(bstack1l1ll_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢᰈ")),
            bstack1l1ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦᰉ"): env.get(bstack1l1ll_opy_ (u"ࠥࡇࡋࡥࡐࡊࡒࡈࡐࡎࡔࡅࡠࡐࡄࡑࡊࠨᰊ")),
            bstack1l1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥᰋ"): env.get(bstack1l1ll_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥᰌ"))
        }
    return {bstack1l1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧᰍ"): None}
def get_host_info():
    return {
        bstack1l1ll_opy_ (u"ࠢࡩࡱࡶࡸࡳࡧ࡭ࡦࠤᰎ"): platform.node(),
        bstack1l1ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥᰏ"): platform.system(),
        bstack1l1ll_opy_ (u"ࠤࡷࡽࡵ࡫ࠢᰐ"): platform.machine(),
        bstack1l1ll_opy_ (u"ࠥࡺࡪࡸࡳࡪࡱࡱࠦᰑ"): platform.version(),
        bstack1l1ll_opy_ (u"ࠦࡦࡸࡣࡩࠤᰒ"): platform.architecture()[0]
    }
def bstack11111111_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack111llll11l1_opy_():
    if bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ᰓ")):
        return bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᰔ")
    return bstack1l1ll_opy_ (u"ࠧࡶࡰ࡮ࡲࡴࡽ࡮ࡠࡩࡵ࡭ࡩ࠭ᰕ")
def bstack111lllll1ll_opy_(driver):
    info = {
        bstack1l1ll_opy_ (u"ࠨࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧᰖ"): driver.capabilities,
        bstack1l1ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩ࠭ᰗ"): driver.session_id,
        bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫᰘ"): driver.capabilities.get(bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩᰙ"), None),
        bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧᰚ"): driver.capabilities.get(bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧᰛ"), None),
        bstack1l1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᰜ"): driver.capabilities.get(bstack1l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧᰝ"), None),
        bstack1l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬᰞ"):driver.capabilities.get(bstack1l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬᰟ"), None),
    }
    if bstack111llll11l1_opy_() == bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪᰠ"):
        if bstack1l1l1l1ll_opy_():
            info[bstack1l1ll_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ᰡ")] = bstack1l1ll_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᰢ")
        elif driver.capabilities.get(bstack1l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨᰣ"), {}).get(bstack1l1ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬᰤ"), False):
            info[bstack1l1ll_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪᰥ")] = bstack1l1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧᰦ")
        else:
            info[bstack1l1ll_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬᰧ")] = bstack1l1ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᰨ")
    return info
def bstack1l1l1l1ll_opy_():
    if bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬᰩ")):
        return True
    if bstack1ll1l11l_opy_(os.environ.get(bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨᰪ"), None)):
        return True
    return False
def bstack1ll1l1l1l1_opy_(bstack11l11111111_opy_, url, data, config):
    headers = config.get(bstack1l1ll_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩᰫ"), None)
    proxies = bstack11ll1llll_opy_(config, url)
    auth = config.get(bstack1l1ll_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᰬ"), None)
    response = requests.request(
            bstack11l11111111_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1111ll11_opy_(bstack1lll11ll11_opy_, size):
    bstack1ll1111l1l_opy_ = []
    while len(bstack1lll11ll11_opy_) > size:
        bstack1l1ll1l1_opy_ = bstack1lll11ll11_opy_[:size]
        bstack1ll1111l1l_opy_.append(bstack1l1ll1l1_opy_)
        bstack1lll11ll11_opy_ = bstack1lll11ll11_opy_[size:]
    bstack1ll1111l1l_opy_.append(bstack1lll11ll11_opy_)
    return bstack1ll1111l1l_opy_
def bstack11l11l11ll1_opy_(message, bstack111lll11lll_opy_=False):
    os.write(1, bytes(message, bstack1l1ll_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩᰭ")))
    os.write(1, bytes(bstack1l1ll_opy_ (u"ࠫࡡࡴࠧᰮ"), bstack1l1ll_opy_ (u"ࠬࡻࡴࡧ࠯࠻ࠫᰯ")))
    if bstack111lll11lll_opy_:
        with open(bstack1l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࠳࡯࠲࠳ࡼ࠱ࠬᰰ") + os.environ[bstack1l1ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡇ࡛ࡉࡍࡆࡢࡌࡆ࡙ࡈࡆࡆࡢࡍࡉ࠭ᰱ")] + bstack1l1ll_opy_ (u"ࠨ࠰࡯ࡳ࡬࠭ᰲ"), bstack1l1ll_opy_ (u"ࠩࡤࠫᰳ")) as f:
            f.write(message + bstack1l1ll_opy_ (u"ࠪࡠࡳ࠭ᰴ"))
def bstack1l1ll1111ll_opy_():
    return os.environ[bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧᰵ")].lower() == bstack1l1ll_opy_ (u"ࠬࡺࡲࡶࡧࠪᰶ")
def bstack1lllll1l11_opy_():
    return bstack1111ll1l1l_opy_().replace(tzinfo=None).isoformat() + bstack1l1ll_opy_ (u"࡚࠭ࠨ᰷")
def bstack11l1l111ll1_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack1l1ll_opy_ (u"࡛ࠧࠩ᰸"))) - datetime.datetime.fromisoformat(start.rstrip(bstack1l1ll_opy_ (u"ࠨ࡜ࠪ᰹")))).total_seconds() * 1000
def bstack11l11llll1l_opy_(timestamp):
    return bstack11l1111ll11_opy_(timestamp).isoformat() + bstack1l1ll_opy_ (u"ࠩ࡝ࠫ᰺")
def bstack111lll11ll1_opy_(bstack11l111l1l11_opy_):
    date_format = bstack1l1ll_opy_ (u"ࠪࠩ࡞ࠫ࡭ࠦࡦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗ࠳ࠫࡦࠨ᰻")
    bstack11l1l111lll_opy_ = datetime.datetime.strptime(bstack11l111l1l11_opy_, date_format)
    return bstack11l1l111lll_opy_.isoformat() + bstack1l1ll_opy_ (u"ࠫ࡟࠭᰼")
def bstack11l11ll11l1_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack1l1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ᰽")
    else:
        return bstack1l1ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭᰾")
def bstack1ll1l11l_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack1l1ll_opy_ (u"ࠧࡵࡴࡸࡩࠬ᰿")
def bstack11l11llll11_opy_(val):
    return val.__str__().lower() == bstack1l1ll_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ᱀")
def bstack111l111ll1_opy_(bstack11l111l11ll_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack11l111l11ll_opy_ as e:
                print(bstack1l1ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡿࢂࠦ࠭࠿ࠢࡾࢁ࠿ࠦࡻࡾࠤ᱁").format(func.__name__, bstack11l111l11ll_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack111llll1l1l_opy_(bstack111lll1l1l1_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack111lll1l1l1_opy_(cls, *args, **kwargs)
            except bstack11l111l11ll_opy_ as e:
                print(bstack1l1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࢀࢃࠠ࠮ࡀࠣࡿࢂࡀࠠࡼࡿࠥ᱂").format(bstack111lll1l1l1_opy_.__name__, bstack11l111l11ll_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack111llll1l1l_opy_
    else:
        return decorator
def bstack1ll1ll111l_opy_(bstack11111llll1_opy_):
    if os.getenv(bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧ᱃")) is not None:
        return bstack1ll1l11l_opy_(os.getenv(bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ᱄")))
    if bstack1l1ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ᱅") in bstack11111llll1_opy_ and bstack11l11llll11_opy_(bstack11111llll1_opy_[bstack1l1ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᱆")]):
        return False
    if bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ᱇") in bstack11111llll1_opy_ and bstack11l11llll11_opy_(bstack11111llll1_opy_[bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ᱈")]):
        return False
    return True
def bstack1lll11l111_opy_():
    try:
        from pytest_bdd import reporting
        bstack11l11111l1l_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠥ᱉"), None)
        return bstack11l11111l1l_opy_ is None or bstack11l11111l1l_opy_ == bstack1l1ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠣ᱊")
    except Exception as e:
        return False
def bstack11ll1l1l1l_opy_(hub_url, CONFIG):
    if bstack1l1l1l111l_opy_() <= version.parse(bstack1l1ll_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬ᱋")):
        if hub_url:
            return bstack1l1ll_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢ᱌") + hub_url + bstack1l1ll_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦᱍ")
        return bstack1l111l11ll_opy_
    if hub_url:
        return bstack1l1ll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥᱎ") + hub_url + bstack1l1ll_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥᱏ")
    return bstack1lll1lll11_opy_
def bstack11l1111111l_opy_():
    return isinstance(os.getenv(bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡐ࡚ࡍࡉࡏࠩ᱐")), str)
def bstack1lll111lll_opy_(url):
    return urlparse(url).hostname
def bstack11l1l1111l_opy_(hostname):
    for bstack1l11l1ll11_opy_ in bstack11lllll1ll_opy_:
        regex = re.compile(bstack1l11l1ll11_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack111llll1l11_opy_(bstack111lllll111_opy_, file_name, logger):
    bstack1l1ll1lll1_opy_ = os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠫࢃ࠭᱑")), bstack111lllll111_opy_)
    try:
        if not os.path.exists(bstack1l1ll1lll1_opy_):
            os.makedirs(bstack1l1ll1lll1_opy_)
        file_path = os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠬࢄࠧ᱒")), bstack111lllll111_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack1l1ll_opy_ (u"࠭ࡷࠨ᱓")):
                pass
            with open(file_path, bstack1l1ll_opy_ (u"ࠢࡸ࠭ࠥ᱔")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack11l11l1ll_opy_.format(str(e)))
def bstack11l11ll1ll1_opy_(file_name, key, value, logger):
    file_path = bstack111llll1l11_opy_(bstack1l1ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ᱕"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack111l11lll_opy_ = json.load(open(file_path, bstack1l1ll_opy_ (u"ࠩࡵࡦࠬ᱖")))
        else:
            bstack111l11lll_opy_ = {}
        bstack111l11lll_opy_[key] = value
        with open(file_path, bstack1l1ll_opy_ (u"ࠥࡻ࠰ࠨ᱗")) as outfile:
            json.dump(bstack111l11lll_opy_, outfile)
def bstack11l1111ll1_opy_(file_name, logger):
    file_path = bstack111llll1l11_opy_(bstack1l1ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ᱘"), file_name, logger)
    bstack111l11lll_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack1l1ll_opy_ (u"ࠬࡸࠧ᱙")) as bstack11l1l1ll11_opy_:
            bstack111l11lll_opy_ = json.load(bstack11l1l1ll11_opy_)
    return bstack111l11lll_opy_
def bstack1l11111111_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡪ࡮ࡲࡥ࠻ࠢࠪᱚ") + file_path + bstack1l1ll_opy_ (u"ࠧࠡࠩᱛ") + str(e))
def bstack1l1l1l111l_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack1l1ll_opy_ (u"ࠣ࠾ࡑࡓ࡙࡙ࡅࡕࡀࠥᱜ")
def bstack1l111l1l1_opy_(config):
    if bstack1l1ll_opy_ (u"ࠩ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨᱝ") in config:
        del (config[bstack1l1ll_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩᱞ")])
        return False
    if bstack1l1l1l111l_opy_() < version.parse(bstack1l1ll_opy_ (u"ࠫ࠸࠴࠴࠯࠲ࠪᱟ")):
        return False
    if bstack1l1l1l111l_opy_() >= version.parse(bstack1l1ll_opy_ (u"ࠬ࠺࠮࠲࠰࠸ࠫᱠ")):
        return True
    if bstack1l1ll_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ᱡ") in config and config[bstack1l1ll_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧᱢ")] is False:
        return False
    else:
        return True
def bstack1ll1ll1ll_opy_(args_list, bstack11l11ll1lll_opy_):
    index = -1
    for value in bstack11l11ll1lll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
def bstack11ll1l1l111_opy_(a, b):
  for k, v in b.items():
    if isinstance(v, dict) and k in a and isinstance(a[k], dict):
        bstack11ll1l1l111_opy_(a[k], v)
    else:
        a[k] = v
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack111ll1ll1l_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack111ll1ll1l_opy_ = bstack111ll1ll1l_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack1l1ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᱣ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack1l1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᱤ"), exception=exception)
    def bstack111111llll_opy_(self):
        if self.result != bstack1l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᱥ"):
            return None
        if isinstance(self.exception_type, str) and bstack1l1ll_opy_ (u"ࠦࡆࡹࡳࡦࡴࡷ࡭ࡴࡴࠢᱦ") in self.exception_type:
            return bstack1l1ll_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࡆࡴࡵࡳࡷࠨᱧ")
        return bstack1l1ll_opy_ (u"ࠨࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠢᱨ")
    def bstack11l1l111111_opy_(self):
        if self.result != bstack1l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᱩ"):
            return None
        if self.bstack111ll1ll1l_opy_:
            return self.bstack111ll1ll1l_opy_
        return bstack11l111l1lll_opy_(self.exception)
def bstack11l111l1lll_opy_(exc):
    return [traceback.format_exception(exc)]
def bstack111lll1l111_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack11ll1ll11_opy_(object, key, default_value):
    if not object or not object.__dict__:
        return default_value
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack11lllllll_opy_(config, logger):
    try:
        import playwright
        bstack111llll111l_opy_ = playwright.__file__
        bstack111lll11l1l_opy_ = os.path.split(bstack111llll111l_opy_)
        bstack11l111l1ll1_opy_ = bstack111lll11l1l_opy_[0] + bstack1l1ll_opy_ (u"ࠨ࠱ࡧࡶ࡮ࡼࡥࡳ࠱ࡳࡥࡨࡱࡡࡨࡧ࠲ࡰ࡮ࡨ࠯ࡤ࡮࡬࠳ࡨࡲࡩ࠯࡬ࡶࠫᱪ")
        os.environ[bstack1l1ll_opy_ (u"ࠩࡊࡐࡔࡈࡁࡍࡡࡄࡋࡊࡔࡔࡠࡊࡗࡘࡕࡥࡐࡓࡑ࡛࡝ࠬᱫ")] = bstack11llll1l11_opy_(config)
        with open(bstack11l111l1ll1_opy_, bstack1l1ll_opy_ (u"ࠪࡶࠬᱬ")) as f:
            bstack1l1111l11l_opy_ = f.read()
            bstack11l11l1l11l_opy_ = bstack1l1ll_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠪᱭ")
            bstack111llll11ll_opy_ = bstack1l1111l11l_opy_.find(bstack11l11l1l11l_opy_)
            if bstack111llll11ll_opy_ == -1:
              process = subprocess.Popen(bstack1l1ll_opy_ (u"ࠧࡴࡰ࡮ࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣ࡫ࡱࡵࡢࡢ࡮࠰ࡥ࡬࡫࡮ࡵࠤᱮ"), shell=True, cwd=bstack111lll11l1l_opy_[0])
              process.wait()
              bstack11l11111l11_opy_ = bstack1l1ll_opy_ (u"࠭ࠢࡶࡵࡨࠤࡸࡺࡲࡪࡥࡷࠦࡀ࠭ᱯ")
              bstack11l11l1ll11_opy_ = bstack1l1ll_opy_ (u"ࠢࠣࠤࠣࡠࠧࡻࡳࡦࠢࡶࡸࡷ࡯ࡣࡵ࡞ࠥ࠿ࠥࡩ࡯࡯ࡵࡷࠤࢀࠦࡢࡰࡱࡷࡷࡹࡸࡡࡱࠢࢀࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠨࡩ࡯ࡳࡧࡧ࡬࠮ࡣࡪࡩࡳࡺࠧࠪ࠽ࠣ࡭࡫ࠦࠨࡱࡴࡲࡧࡪࡹࡳ࠯ࡧࡱࡺ࠳ࡍࡌࡐࡄࡄࡐࡤࡇࡇࡆࡐࡗࡣࡍ࡚ࡔࡑࡡࡓࡖࡔ࡞࡙ࠪࠢࡥࡳࡴࡺࡳࡵࡴࡤࡴ࠭࠯࠻ࠡࠤࠥࠦᱰ")
              bstack11l1111l1ll_opy_ = bstack1l1111l11l_opy_.replace(bstack11l11111l11_opy_, bstack11l11l1ll11_opy_)
              with open(bstack11l111l1ll1_opy_, bstack1l1ll_opy_ (u"ࠨࡹࠪᱱ")) as f:
                f.write(bstack11l1111l1ll_opy_)
    except Exception as e:
        logger.error(bstack11l1l1l1l_opy_.format(str(e)))
def bstack11l11ll1l1_opy_():
  try:
    bstack111lllllll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1ll_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯࠲࡯ࡹ࡯࡯ࠩᱲ"))
    bstack11l111ll111_opy_ = []
    if os.path.exists(bstack111lllllll1_opy_):
      with open(bstack111lllllll1_opy_) as f:
        bstack11l111ll111_opy_ = json.load(f)
      os.remove(bstack111lllllll1_opy_)
    return bstack11l111ll111_opy_
  except:
    pass
  return []
def bstack1l1l111111_opy_(bstack1ll1111l_opy_):
  try:
    bstack11l111ll111_opy_ = []
    bstack111lllllll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1ll_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰ࠳ࡰࡳࡰࡰࠪᱳ"))
    if os.path.exists(bstack111lllllll1_opy_):
      with open(bstack111lllllll1_opy_) as f:
        bstack11l111ll111_opy_ = json.load(f)
    bstack11l111ll111_opy_.append(bstack1ll1111l_opy_)
    with open(bstack111lllllll1_opy_, bstack1l1ll_opy_ (u"ࠫࡼ࠭ᱴ")) as f:
        json.dump(bstack11l111ll111_opy_, f)
  except:
    pass
def bstack1lll1l11ll_opy_(logger, bstack11l11lll1l1_opy_ = False):
  try:
    test_name = os.environ.get(bstack1l1ll_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘࡤ࡚ࡅࡔࡖࡢࡒࡆࡓࡅࠨᱵ"), bstack1l1ll_opy_ (u"࠭ࠧᱶ"))
    if test_name == bstack1l1ll_opy_ (u"ࠧࠨᱷ"):
        test_name = threading.current_thread().__dict__.get(bstack1l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡃࡦࡧࡣࡹ࡫ࡳࡵࡡࡱࡥࡲ࡫ࠧᱸ"), bstack1l1ll_opy_ (u"ࠩࠪᱹ"))
    bstack11l111ll1l1_opy_ = bstack1l1ll_opy_ (u"ࠪ࠰ࠥ࠭ᱺ").join(threading.current_thread().bstackTestErrorMessages)
    if bstack11l11lll1l1_opy_:
        bstack1ll1l1111l_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫᱻ"), bstack1l1ll_opy_ (u"ࠬ࠶ࠧᱼ"))
        bstack1l111l1l_opy_ = {bstack1l1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᱽ"): test_name, bstack1l1ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭᱾"): bstack11l111ll1l1_opy_, bstack1l1ll_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ᱿"): bstack1ll1l1111l_opy_}
        bstack11l1l1111l1_opy_ = []
        bstack11l11lll111_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡳࡴࡵࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨᲀ"))
        if os.path.exists(bstack11l11lll111_opy_):
            with open(bstack11l11lll111_opy_) as f:
                bstack11l1l1111l1_opy_ = json.load(f)
        bstack11l1l1111l1_opy_.append(bstack1l111l1l_opy_)
        with open(bstack11l11lll111_opy_, bstack1l1ll_opy_ (u"ࠪࡻࠬᲁ")) as f:
            json.dump(bstack11l1l1111l1_opy_, f)
    else:
        bstack1l111l1l_opy_ = {bstack1l1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᲂ"): test_name, bstack1l1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᲃ"): bstack11l111ll1l1_opy_, bstack1l1ll_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬᲄ"): str(multiprocessing.current_process().name)}
        if bstack1l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷࠫᲅ") not in multiprocessing.current_process().__dict__.keys():
            multiprocessing.current_process().bstack_error_list = []
        multiprocessing.current_process().bstack_error_list.append(bstack1l111l1l_opy_)
  except Exception as e:
      logger.warn(bstack1l1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡴࡾࡺࡥࡴࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡ࠻ࠢࡾࢁࠧᲆ").format(e))
def bstack11lllll1l_opy_(error_message, test_name, index, logger):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬᲇ"))
    try:
      bstack11l11l111l1_opy_ = []
      bstack1l111l1l_opy_ = {bstack1l1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨᲈ"): test_name, bstack1l1ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᲉ"): error_message, bstack1l1ll_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᲊ"): index}
      bstack11l1111ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧ᲋"))
      if os.path.exists(bstack11l1111ll1l_opy_):
          with open(bstack11l1111ll1l_opy_) as f:
              bstack11l11l111l1_opy_ = json.load(f)
      bstack11l11l111l1_opy_.append(bstack1l111l1l_opy_)
      with open(bstack11l1111ll1l_opy_, bstack1l1ll_opy_ (u"ࠧࡸࠩ᲌")) as f:
          json.dump(bstack11l11l111l1_opy_, f)
    except Exception as e:
      logger.warn(bstack1l1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺ࡯ࡳࡧࠣࡶࡴࡨ࡯ࡵࠢࡩࡹࡳࡴࡥ࡭ࠢࡧࡥࡹࡧ࠺ࠡࡽࢀࠦ᲍").format(e))
    return
  bstack11l11l111l1_opy_ = []
  bstack1l111l1l_opy_ = {bstack1l1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ᲎"): test_name, bstack1l1ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ᲏"): error_message, bstack1l1ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪᲐ"): index}
  bstack11l1111ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭Ბ"))
  lock_file = bstack11l1111ll1l_opy_ + bstack1l1ll_opy_ (u"࠭࠮࡭ࡱࡦ࡯ࠬᲒ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack11l1111ll1l_opy_):
          with open(bstack11l1111ll1l_opy_, bstack1l1ll_opy_ (u"ࠧࡳࠩᲓ")) as f:
              content = f.read().strip()
              if content:
                  bstack11l11l111l1_opy_ = json.load(open(bstack11l1111ll1l_opy_))
      bstack11l11l111l1_opy_.append(bstack1l111l1l_opy_)
      with open(bstack11l1111ll1l_opy_, bstack1l1ll_opy_ (u"ࠨࡹࠪᲔ")) as f:
          json.dump(bstack11l11l111l1_opy_, f)
  except Exception as e:
    logger.warn(bstack1l1ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡰࡴࡨࠤࡷࡵࡢࡰࡶࠣࡪࡺࡴ࡮ࡦ࡮ࠣࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡦࡪ࡮ࡨࠤࡱࡵࡣ࡬࡫ࡱ࡫࠿ࠦࡻࡾࠤᲕ").format(e))
def bstack1l1l1l1l11_opy_(bstack11lll111l_opy_, name, logger):
  try:
    bstack1l111l1l_opy_ = {bstack1l1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨᲖ"): name, bstack1l1ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᲗ"): bstack11lll111l_opy_, bstack1l1ll_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫᲘ"): str(threading.current_thread()._name)}
    return bstack1l111l1l_opy_
  except Exception as e:
    logger.warn(bstack1l1ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡴࡸࡥࠡࡤࡨ࡬ࡦࡼࡥࠡࡨࡸࡲࡳ࡫࡬ࠡࡦࡤࡸࡦࡀࠠࡼࡿࠥᲙ").format(e))
  return
def bstack11l1l11111l_opy_():
    return platform.system() == bstack1l1ll_opy_ (u"ࠧࡘ࡫ࡱࡨࡴࡽࡳࠨᲚ")
def bstack11l1111l1_opy_(bstack11l1l1111ll_opy_, config, logger):
    bstack11l11llllll_opy_ = {}
    try:
        return {key: config[key] for key in config if bstack11l1l1111ll_opy_.match(key)}
    except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡬ࡵࡧࡵࠤࡨࡵ࡮ࡧ࡫ࡪࠤࡰ࡫ࡹࡴࠢࡥࡽࠥࡸࡥࡨࡧࡻࠤࡲࡧࡴࡤࡪ࠽ࠤࢀࢃࠢᲛ").format(e))
    return bstack11l11llllll_opy_
def bstack11l111l111l_opy_(bstack11l11lll1ll_opy_, bstack11l11l11lll_opy_):
    bstack11l111lll1l_opy_ = version.parse(bstack11l11lll1ll_opy_)
    bstack111lll1l1ll_opy_ = version.parse(bstack11l11l11lll_opy_)
    if bstack11l111lll1l_opy_ > bstack111lll1l1ll_opy_:
        return 1
    elif bstack11l111lll1l_opy_ < bstack111lll1l1ll_opy_:
        return -1
    else:
        return 0
def bstack1111ll1l1l_opy_():
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
def bstack11l1111ll11_opy_(timestamp):
    return datetime.datetime.fromtimestamp(timestamp, datetime.timezone.utc).replace(tzinfo=None)
def bstack111llllllll_opy_(framework):
    from browserstack_sdk._version import __version__
    return str(framework) + str(__version__)
def bstack11ll11l111_opy_(options, framework, config, bstack11l1ll11l_opy_={}):
    if options is None:
        return
    if getattr(options, bstack1l1ll_opy_ (u"ࠩࡪࡩࡹ࠭Ნ"), None):
        caps = options
    else:
        caps = options.to_capabilities()
    bstack11l1l111l1_opy_ = caps.get(bstack1l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᲝ"))
    bstack111lllll11l_opy_ = True
    bstack11ll11ll1l_opy_ = os.environ[bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᲞ")]
    bstack1ll1l11111l_opy_ = config.get(bstack1l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᲟ"), False)
    if bstack1ll1l11111l_opy_:
        bstack1llll11l11l_opy_ = config.get(bstack1l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭Რ"), {})
        bstack1llll11l11l_opy_[bstack1l1ll_opy_ (u"ࠧࡢࡷࡷ࡬࡙ࡵ࡫ࡦࡰࠪᲡ")] = os.getenv(bstack1l1ll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭Ტ"))
        bstack11lll111111_opy_ = json.loads(os.getenv(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪᲣ"), bstack1l1ll_opy_ (u"ࠪࡿࢂ࠭Ფ"))).get(bstack1l1ll_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬᲥ"))
    if bstack11l11llll11_opy_(caps.get(bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡺࡹࡥࡘ࠵ࡆࠫᲦ"))) or bstack11l11llll11_opy_(caps.get(bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡻࡳࡦࡡࡺ࠷ࡨ࠭Ყ"))):
        bstack111lllll11l_opy_ = False
    if bstack1l111l1l1_opy_({bstack1l1ll_opy_ (u"ࠢࡶࡵࡨ࡛࠸ࡉࠢᲨ"): bstack111lllll11l_opy_}):
        bstack11l1l111l1_opy_ = bstack11l1l111l1_opy_ or {}
        bstack11l1l111l1_opy_[bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪᲩ")] = bstack111llllllll_opy_(framework)
        bstack11l1l111l1_opy_[bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫᲪ")] = bstack1l1ll1111ll_opy_()
        bstack11l1l111l1_opy_[bstack1l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭Ძ")] = bstack11ll11ll1l_opy_
        bstack11l1l111l1_opy_[bstack1l1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭Წ")] = bstack11l1ll11l_opy_
        if bstack1ll1l11111l_opy_:
            bstack11l1l111l1_opy_[bstack1l1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬᲭ")] = bstack1ll1l11111l_opy_
            bstack11l1l111l1_opy_[bstack1l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭Ხ")] = bstack1llll11l11l_opy_
            bstack11l1l111l1_opy_[bstack1l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧᲯ")][bstack1l1ll_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩᲰ")] = bstack11lll111111_opy_
        if getattr(options, bstack1l1ll_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻࠪᲱ"), None):
            options.set_capability(bstack1l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫᲲ"), bstack11l1l111l1_opy_)
        else:
            options[bstack1l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᲳ")] = bstack11l1l111l1_opy_
    else:
        if getattr(options, bstack1l1ll_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭Ჴ"), None):
            options.set_capability(bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᲵ"), bstack111llllllll_opy_(framework))
            options.set_capability(bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᲶ"), bstack1l1ll1111ll_opy_())
            options.set_capability(bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪᲷ"), bstack11ll11ll1l_opy_)
            options.set_capability(bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪᲸ"), bstack11l1ll11l_opy_)
            if bstack1ll1l11111l_opy_:
                options.set_capability(bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩᲹ"), bstack1ll1l11111l_opy_)
                options.set_capability(bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪᲺ"), bstack1llll11l11l_opy_)
                options.set_capability(bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶ࠲ࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ᲻"), bstack11lll111111_opy_)
        else:
            options[bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ᲼")] = bstack111llllllll_opy_(framework)
            options[bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨᲽ")] = bstack1l1ll1111ll_opy_()
            options[bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪᲾ")] = bstack11ll11ll1l_opy_
            options[bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪᲿ")] = bstack11l1ll11l_opy_
            if bstack1ll1l11111l_opy_:
                options[bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ᳀")] = bstack1ll1l11111l_opy_
                options[bstack1l1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ᳁")] = bstack1llll11l11l_opy_
                options[bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ᳂")][bstack1l1ll_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ᳃")] = bstack11lll111111_opy_
    return options
def bstack11l111111ll_opy_(bstack111llll1111_opy_, framework):
    bstack11l1ll11l_opy_ = bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠢࡑࡎࡄ࡝࡜ࡘࡉࡈࡊࡗࡣࡕࡘࡏࡅࡗࡆࡘࡤࡓࡁࡑࠤ᳄"))
    if bstack111llll1111_opy_ and len(bstack111llll1111_opy_.split(bstack1l1ll_opy_ (u"ࠨࡥࡤࡴࡸࡃࠧ᳅"))) > 1:
        ws_url = bstack111llll1111_opy_.split(bstack1l1ll_opy_ (u"ࠩࡦࡥࡵࡹ࠽ࠨ᳆"))[0]
        if bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭᳇") in ws_url:
            from browserstack_sdk._version import __version__
            bstack111lll1ll11_opy_ = json.loads(urllib.parse.unquote(bstack111llll1111_opy_.split(bstack1l1ll_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪ᳈"))[1]))
            bstack111lll1ll11_opy_ = bstack111lll1ll11_opy_ or {}
            bstack11ll11ll1l_opy_ = os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ᳉")]
            bstack111lll1ll11_opy_[bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ᳊")] = str(framework) + str(__version__)
            bstack111lll1ll11_opy_[bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨ᳋")] = bstack1l1ll1111ll_opy_()
            bstack111lll1ll11_opy_[bstack1l1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪ᳌")] = bstack11ll11ll1l_opy_
            bstack111lll1ll11_opy_[bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪ᳍")] = bstack11l1ll11l_opy_
            bstack111llll1111_opy_ = bstack111llll1111_opy_.split(bstack1l1ll_opy_ (u"ࠪࡧࡦࡶࡳ࠾ࠩ᳎"))[0] + bstack1l1ll_opy_ (u"ࠫࡨࡧࡰࡴ࠿ࠪ᳏") + urllib.parse.quote(json.dumps(bstack111lll1ll11_opy_))
    return bstack111llll1111_opy_
def bstack1lllll1l1l_opy_():
    global bstack1l11ll11l_opy_
    from playwright._impl._browser_type import BrowserType
    bstack1l11ll11l_opy_ = BrowserType.connect
    return bstack1l11ll11l_opy_
def bstack1ll1111ll_opy_(framework_name):
    global bstack111llll11_opy_
    bstack111llll11_opy_ = framework_name
    return framework_name
def bstack1111l1l1l_opy_(self, *args, **kwargs):
    global bstack1l11ll11l_opy_
    try:
        global bstack111llll11_opy_
        if bstack1l1ll_opy_ (u"ࠬࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵࠩ᳐") in kwargs:
            kwargs[bstack1l1ll_opy_ (u"࠭ࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶࠪ᳑")] = bstack11l111111ll_opy_(
                kwargs.get(bstack1l1ll_opy_ (u"ࠧࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷࠫ᳒"), None),
                bstack111llll11_opy_
            )
    except Exception as e:
        logger.error(bstack1l1ll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪࡨࡲࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡖࡈࡐࠦࡣࡢࡲࡶ࠾ࠥࢁࡽࠣ᳓").format(str(e)))
    return bstack1l11ll11l_opy_(self, *args, **kwargs)
def bstack11l1111l111_opy_(bstack111lll1l11l_opy_, proxies):
    proxy_settings = {}
    try:
        if not proxies:
            proxies = bstack11ll1llll_opy_(bstack111lll1l11l_opy_, bstack1l1ll_opy_ (u"ࠤ᳔ࠥ"))
        if proxies and proxies.get(bstack1l1ll_opy_ (u"ࠥ࡬ࡹࡺࡰࡴࠤ᳕")):
            parsed_url = urlparse(proxies.get(bstack1l1ll_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ᳖ࠥ")))
            if parsed_url and parsed_url.hostname: proxy_settings[bstack1l1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࡌࡴࡹࡴࠨ᳗")] = str(parsed_url.hostname)
            if parsed_url and parsed_url.port: proxy_settings[bstack1l1ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡵࡲࡵ᳘ࠩ")] = str(parsed_url.port)
            if parsed_url and parsed_url.username: proxy_settings[bstack1l1ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴ᳙ࠪ")] = str(parsed_url.username)
            if parsed_url and parsed_url.password: proxy_settings[bstack1l1ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡢࡵࡶࠫ᳚")] = str(parsed_url.password)
        return proxy_settings
    except:
        return proxy_settings
def bstack11l1l1l1_opy_(bstack111lll1l11l_opy_):
    bstack11l111l1l1l_opy_ = {
        bstack11l1ll11l1l_opy_[bstack111lll11l11_opy_]: bstack111lll1l11l_opy_[bstack111lll11l11_opy_]
        for bstack111lll11l11_opy_ in bstack111lll1l11l_opy_
        if bstack111lll11l11_opy_ in bstack11l1ll11l1l_opy_
    }
    bstack11l111l1l1l_opy_[bstack1l1ll_opy_ (u"ࠤࡳࡶࡴࡾࡹࡔࡧࡷࡸ࡮ࡴࡧࡴࠤ᳛")] = bstack11l1111l111_opy_(bstack111lll1l11l_opy_, bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠥࡴࡷࡵࡸࡺࡕࡨࡸࡹ࡯࡮ࡨࡵ᳜ࠥ")))
    bstack111lll1llll_opy_ = [element.lower() for element in bstack11l1llll11l_opy_]
    bstack11l11l1ll1l_opy_(bstack11l111l1l1l_opy_, bstack111lll1llll_opy_)
    return bstack11l111l1l1l_opy_
def bstack11l11l1ll1l_opy_(d, keys):
    for key in list(d.keys()):
        if key.lower() in keys:
            d[key] = bstack1l1ll_opy_ (u"ࠦ࠯࠰ࠪࠫࠤ᳝")
    for value in d.values():
        if isinstance(value, dict):
            bstack11l11l1ll1l_opy_(value, keys)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    bstack11l11l1ll1l_opy_(item, keys)
def bstack1l1ll1l11ll_opy_():
    bstack11l111l11l1_opy_ = [os.environ.get(bstack1l1ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡏࡌࡆࡕࡢࡈࡎࡘ᳞ࠢ")), os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"ࠨࡾ᳟ࠣ")), bstack1l1ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ᳠")), os.path.join(bstack1l1ll_opy_ (u"ࠨ࠱ࡷࡱࡵ࠭᳡"), bstack1l1ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬᳢ࠩ"))]
    for path in bstack11l111l11l1_opy_:
        if path is None:
            continue
        try:
            if os.path.exists(path):
                logger.debug(bstack1l1ll_opy_ (u"ࠥࡊ࡮ࡲࡥ᳣ࠡࠩࠥ") + str(path) + bstack1l1ll_opy_ (u"ࠦࠬࠦࡥࡹ࡫ࡶࡸࡸ࠴᳤ࠢ"))
                if not os.access(path, os.W_OK):
                    logger.debug(bstack1l1ll_opy_ (u"ࠧࡍࡩࡷ࡫ࡱ࡫ࠥࡶࡥࡳ࡯࡬ࡷࡸ࡯࡯࡯ࡵࠣࡪࡴࡸࠠࠨࠤ᳥") + str(path) + bstack1l1ll_opy_ (u"ࠨ᳦ࠧࠣ"))
                    os.chmod(path, 0o777)
                else:
                    logger.debug(bstack1l1ll_opy_ (u"ࠢࡇ࡫࡯ࡩ᳧ࠥ࠭ࠢ") + str(path) + bstack1l1ll_opy_ (u"ࠣࠩࠣࡥࡱࡸࡥࡢࡦࡼࠤ࡭ࡧࡳࠡࡶ࡫ࡩࠥࡸࡥࡲࡷ࡬ࡶࡪࡪࠠࡱࡧࡵࡱ࡮ࡹࡳࡪࡱࡱࡷ࠳ࠨ᳨"))
            else:
                logger.debug(bstack1l1ll_opy_ (u"ࠤࡆࡶࡪࡧࡴࡪࡰࡪࠤ࡫࡯࡬ࡦࠢࠪࠦᳩ") + str(path) + bstack1l1ll_opy_ (u"ࠥࠫࠥࡽࡩࡵࡪࠣࡻࡷ࡯ࡴࡦࠢࡳࡩࡷࡳࡩࡴࡵ࡬ࡳࡳ࠴ࠢᳪ"))
                os.makedirs(path, exist_ok=True)
                os.chmod(path, 0o777)
            logger.debug(bstack1l1ll_opy_ (u"ࠦࡔࡶࡥࡳࡣࡷ࡭ࡴࡴࠠࡴࡷࡦࡧࡪ࡫ࡤࡦࡦࠣࡪࡴࡸࠠࠨࠤᳫ") + str(path) + bstack1l1ll_opy_ (u"ࠧ࠭࠮ࠣᳬ"))
            return path
        except Exception as e:
            logger.debug(bstack1l1ll_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡵࡱࠢࡩ࡭ࡱ࡫ࠠࠨࡽࡳࡥࡹ࡮ࡽࠨ࠼᳭ࠣࠦ") + str(e) + bstack1l1ll_opy_ (u"ࠢࠣᳮ"))
    logger.debug(bstack1l1ll_opy_ (u"ࠣࡃ࡯ࡰࠥࡶࡡࡵࡪࡶࠤ࡫ࡧࡩ࡭ࡧࡧ࠲ࠧᳯ"))
    return None
@measure(event_name=EVENTS.bstack11l1lll1ll1_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
def bstack1lll11ll11l_opy_(binary_path, bstack1llll111l1l_opy_, bs_config):
    logger.debug(bstack1l1ll_opy_ (u"ࠤࡆࡹࡷࡸࡥ࡯ࡶࠣࡇࡑࡏࠠࡑࡣࡷ࡬ࠥ࡬࡯ࡶࡰࡧ࠾ࠥࢁࡽࠣᳰ").format(binary_path))
    bstack11l11ll1111_opy_ = bstack1l1ll_opy_ (u"ࠪࠫᳱ")
    bstack11l111lllll_opy_ = {
        bstack1l1ll_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩᳲ"): __version__,
        bstack1l1ll_opy_ (u"ࠧࡵࡳࠣᳳ"): platform.system(),
        bstack1l1ll_opy_ (u"ࠨ࡯ࡴࡡࡤࡶࡨ࡮ࠢ᳴"): platform.machine(),
        bstack1l1ll_opy_ (u"ࠢࡤ࡮࡬ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧᳵ"): bstack1l1ll_opy_ (u"ࠨ࠲ࠪᳶ"),
        bstack1l1ll_opy_ (u"ࠤࡶࡨࡰࡥ࡬ࡢࡰࡪࡹࡦ࡭ࡥࠣ᳷"): bstack1l1ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ᳸")
    }
    bstack11l1l111l11_opy_(bstack11l111lllll_opy_)
    try:
        if binary_path:
            bstack11l111lllll_opy_[bstack1l1ll_opy_ (u"ࠫࡨࡲࡩࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ᳹")] = subprocess.check_output([binary_path, bstack1l1ll_opy_ (u"ࠧࡼࡥࡳࡵ࡬ࡳࡳࠨᳺ")]).strip().decode(bstack1l1ll_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬ᳻"))
        response = requests.request(
            bstack1l1ll_opy_ (u"ࠧࡈࡇࡗࠫ᳼"),
            url=bstack111ll111_opy_(bstack11l1lllll1l_opy_),
            headers=None,
            auth=(bs_config[bstack1l1ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ᳽")], bs_config[bstack1l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ᳾")]),
            json=None,
            params=bstack11l111lllll_opy_
        )
        data = response.json()
        if response.status_code == 200 and bstack1l1ll_opy_ (u"ࠪࡹࡷࡲࠧ᳿") in data.keys() and bstack1l1ll_opy_ (u"ࠫࡺࡶࡤࡢࡶࡨࡨࡤࡩ࡬ࡪࡡࡹࡩࡷࡹࡩࡰࡰࠪᴀ") in data.keys():
            logger.debug(bstack1l1ll_opy_ (u"ࠧࡔࡥࡦࡦࠣࡸࡴࠦࡵࡱࡦࡤࡸࡪࠦࡢࡪࡰࡤࡶࡾ࠲ࠠࡤࡷࡵࡶࡪࡴࡴࠡࡤ࡬ࡲࡦࡸࡹࠡࡸࡨࡶࡸ࡯࡯࡯࠼ࠣࡿࢂࠨᴁ").format(bstack11l111lllll_opy_[bstack1l1ll_opy_ (u"࠭ࡣ࡭࡫ࡢࡺࡪࡸࡳࡪࡱࡱࠫᴂ")]))
            if bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡊࡐࡄࡖ࡞ࡥࡕࡓࡎࠪᴃ") in os.environ:
                logger.debug(bstack1l1ll_opy_ (u"ࠣࡕ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡦ࡮ࡴࡡࡳࡻࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡧࡳࠡࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡖࡔࡏࠤ࡮ࡹࠠࡴࡧࡷࠦᴄ"))
                data[bstack1l1ll_opy_ (u"ࠩࡸࡶࡱ࠭ᴅ")] = os.environ[bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅࡍࡓࡇࡒ࡚ࡡࡘࡖࡑ࠭ᴆ")]
            bstack11l1111l11l_opy_ = bstack11l11l11l1l_opy_(data[bstack1l1ll_opy_ (u"ࠫࡺࡸ࡬ࠨᴇ")], bstack1llll111l1l_opy_)
            bstack11l11ll1111_opy_ = os.path.join(bstack1llll111l1l_opy_, bstack11l1111l11l_opy_)
            os.chmod(bstack11l11ll1111_opy_, 0o777) # bstack11l111llll1_opy_ permission
            return bstack11l11ll1111_opy_
    except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡨࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡰࡨࡻ࡙ࠥࡄࡌࠢࡾࢁࠧᴈ").format(e))
    return binary_path
def bstack11l1l111l11_opy_(bstack11l111lllll_opy_):
    try:
        if bstack1l1ll_opy_ (u"࠭࡬ࡪࡰࡸࡼࠬᴉ") not in bstack11l111lllll_opy_[bstack1l1ll_opy_ (u"ࠧࡰࡵࠪᴊ")].lower():
            return
        if os.path.exists(bstack1l1ll_opy_ (u"ࠣ࠱ࡨࡸࡨ࠵࡯ࡴ࠯ࡵࡩࡱ࡫ࡡࡴࡧࠥᴋ")):
            with open(bstack1l1ll_opy_ (u"ࠤ࠲ࡩࡹࡩ࠯ࡰࡵ࠰ࡶࡪࡲࡥࡢࡵࡨࠦᴌ"), bstack1l1ll_opy_ (u"ࠥࡶࠧᴍ")) as f:
                bstack11l1l111l1l_opy_ = {}
                for line in f:
                    if bstack1l1ll_opy_ (u"ࠦࡂࠨᴎ") in line:
                        key, value = line.rstrip().split(bstack1l1ll_opy_ (u"ࠧࡃࠢᴏ"), 1)
                        bstack11l1l111l1l_opy_[key] = value.strip(bstack1l1ll_opy_ (u"࠭ࠢ࡝ࠩࠪᴐ"))
                bstack11l111lllll_opy_[bstack1l1ll_opy_ (u"ࠧࡥ࡫ࡶࡸࡷࡵࠧᴑ")] = bstack11l1l111l1l_opy_.get(bstack1l1ll_opy_ (u"ࠣࡋࡇࠦᴒ"), bstack1l1ll_opy_ (u"ࠤࠥᴓ"))
        elif os.path.exists(bstack1l1ll_opy_ (u"ࠥ࠳ࡪࡺࡣ࠰ࡣ࡯ࡴ࡮ࡴࡥ࠮ࡴࡨࡰࡪࡧࡳࡦࠤᴔ")):
            bstack11l111lllll_opy_[bstack1l1ll_opy_ (u"ࠫࡩ࡯ࡳࡵࡴࡲࠫᴕ")] = bstack1l1ll_opy_ (u"ࠬࡧ࡬ࡱ࡫ࡱࡩࠬᴖ")
    except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡹࠦࡤࡪࡵࡷࡶࡴࠦ࡯ࡧࠢ࡯࡭ࡳࡻࡸࠣᴗ") + e)
@measure(event_name=EVENTS.bstack11l1ll1111l_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
def bstack11l11l11l1l_opy_(bstack11l11l1l111_opy_, bstack111lllll1l1_opy_):
    logger.debug(bstack1l1ll_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳ࠺ࠡࠤᴘ") + str(bstack11l11l1l111_opy_) + bstack1l1ll_opy_ (u"ࠣࠤᴙ"))
    zip_path = os.path.join(bstack111lllll1l1_opy_, bstack1l1ll_opy_ (u"ࠤࡧࡳࡼࡴ࡬ࡰࡣࡧࡩࡩࡥࡦࡪ࡮ࡨ࠲ࡿ࡯ࡰࠣᴚ"))
    bstack11l1111l11l_opy_ = bstack1l1ll_opy_ (u"ࠪࠫᴛ")
    with requests.get(bstack11l11l1l111_opy_, stream=True) as response:
        response.raise_for_status()
        with open(zip_path, bstack1l1ll_opy_ (u"ࠦࡼࡨࠢᴜ")) as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        logger.debug(bstack1l1ll_opy_ (u"ࠧࡌࡩ࡭ࡧࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾ࠴ࠢᴝ"))
    with zipfile.ZipFile(zip_path, bstack1l1ll_opy_ (u"࠭ࡲࠨᴞ")) as zip_ref:
        bstack11l11l111ll_opy_ = zip_ref.namelist()
        if len(bstack11l11l111ll_opy_) > 0:
            bstack11l1111l11l_opy_ = bstack11l11l111ll_opy_[0] # bstack111llll1ll1_opy_ bstack11l1lll111l_opy_ will be bstack11l11l1lll1_opy_ 1 file i.e. the binary in the zip
        zip_ref.extractall(bstack111lllll1l1_opy_)
        logger.debug(bstack1l1ll_opy_ (u"ࠢࡇ࡫࡯ࡩࡸࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥ࡫ࡸࡵࡴࡤࡧࡹ࡫ࡤࠡࡶࡲࠤࠬࠨᴟ") + str(bstack111lllll1l1_opy_) + bstack1l1ll_opy_ (u"ࠣࠩࠥᴠ"))
    os.remove(zip_path)
    return bstack11l1111l11l_opy_
def get_cli_dir():
    bstack11l11111lll_opy_ = bstack1l1ll1l11ll_opy_()
    if bstack11l11111lll_opy_:
        bstack1llll111l1l_opy_ = os.path.join(bstack11l11111lll_opy_, bstack1l1ll_opy_ (u"ࠤࡦࡰ࡮ࠨᴡ"))
        if not os.path.exists(bstack1llll111l1l_opy_):
            os.makedirs(bstack1llll111l1l_opy_, mode=0o777, exist_ok=True)
        return bstack1llll111l1l_opy_
    else:
        raise FileNotFoundError(bstack1l1ll_opy_ (u"ࠥࡒࡴࠦࡷࡳ࡫ࡷࡥࡧࡲࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡕࡇࡏࠥࡨࡩ࡯ࡣࡵࡽ࠳ࠨᴢ"))
def bstack1ll1ll11l11_opy_(bstack1llll111l1l_opy_):
    bstack1l1ll_opy_ (u"ࠦࠧࠨࡇࡦࡶࠣࡸ࡭࡫ࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯࡙ࠥࡄࡌࠢࡥ࡭ࡳࡧࡲࡺࠢ࡬ࡲࠥࡧࠠࡸࡴ࡬ࡸࡦࡨ࡬ࡦࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠳ࠨࠢࠣᴣ")
    bstack11l11l1111l_opy_ = [
        os.path.join(bstack1llll111l1l_opy_, f)
        for f in os.listdir(bstack1llll111l1l_opy_)
        if os.path.isfile(os.path.join(bstack1llll111l1l_opy_, f)) and f.startswith(bstack1l1ll_opy_ (u"ࠧࡨࡩ࡯ࡣࡵࡽ࠲ࠨᴤ"))
    ]
    if len(bstack11l11l1111l_opy_) > 0:
        return max(bstack11l11l1111l_opy_, key=os.path.getmtime) # get bstack11l11lllll1_opy_ binary
    return bstack1l1ll_opy_ (u"ࠨࠢᴥ")
def bstack11lll1111ll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1ll1l111l1l_opy_(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = bstack1ll1l111l1l_opy_(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack1lll1ll1ll_opy_(data, keys, default=None):
    bstack1l1ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡔࡣࡩࡩࡱࡿࠠࡨࡧࡷࠤࡦࠦ࡮ࡦࡵࡷࡩࡩࠦࡶࡢ࡮ࡸࡩࠥ࡬ࡲࡰ࡯ࠣࡥࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺࠢࡲࡶࠥࡲࡩࡴࡶ࠱ࠎࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡦࡤࡸࡦࡀࠠࡕࡪࡨࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹࠡࡱࡵࠤࡱ࡯ࡳࡵࠢࡷࡳࠥࡺࡲࡢࡸࡨࡶࡸ࡫࠮ࠋࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡱࡥࡺࡵ࠽ࠤࡆࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠ࡬ࡧࡼࡷ࠴࡯࡮ࡥ࡫ࡦࡩࡸࠦࡲࡦࡲࡵࡩࡸ࡫࡮ࡵ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡳࡥࡹ࡮࠮ࠋࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡪࡥࡧࡣࡸࡰࡹࡀࠠࡗࡣ࡯ࡹࡪࠦࡴࡰࠢࡵࡩࡹࡻࡲ࡯ࠢ࡬ࡪࠥࡺࡨࡦࠢࡳࡥࡹ࡮ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴ࠯ࠌࠣࠤࠥࠦ࠺ࡳࡧࡷࡹࡷࡴ࠺ࠡࡖ࡫ࡩࠥࡼࡡ࡭ࡷࡨࠤࡦࡺࠠࡵࡪࡨࠤࡳ࡫ࡳࡵࡧࡧࠤࡵࡧࡴࡩ࠮ࠣࡳࡷࠦࡤࡦࡨࡤࡹࡱࡺࠠࡪࡨࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᴦ")
    if not data:
        return default
    current = data
    try:
        for key in keys:
            if isinstance(current, dict):
                current = current[key]
            elif isinstance(current, list) and isinstance(key, int):
                current = current[key]
            else:
                return default
        return current
    except (KeyError, IndexError, TypeError):
        return default