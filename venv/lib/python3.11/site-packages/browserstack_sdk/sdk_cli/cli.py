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
import subprocess
import threading
import time
import sys
import grpc
import os
from browserstack_sdk import sdk_pb2_grpc
from browserstack_sdk import sdk_pb2 as structs
from browserstack_sdk.sdk_cli.bstack111111l11l_opy_ import bstack111111l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lllllll_opy_ import bstack1llll11lll1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll1l1_opy_ import bstack1ll1l1l1ll1_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1l11_opy_ import bstack1ll1ll1111l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1l1lll11_opy_ import bstack1llll1111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll11l1_opy_ import bstack1llll1l111l_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll1ll1_opy_ import bstack1llll111lll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1lll1ll_opy_ import bstack1llll1111ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11l11ll_opy_ import bstack1ll1ll111ll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1ll1_opy_ import bstack1lll1l1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack11ll1lll1l_opy_ import bstack11ll1lll1l_opy_, bstack111l1lll_opy_, bstack1l11111l1_opy_
from browserstack_sdk.sdk_cli.pytest_bdd_framework import PytestBDDFramework
from browserstack_sdk.sdk_cli.bstack1ll1ll1ll1l_opy_ import bstack1lll1l111l1_opy_
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll11lll1l_opy_
from browserstack_sdk.sdk_cli.bstack1llllllll1l_opy_ import bstack11111111l1_opy_
from browserstack_sdk.sdk_cli.bstack1ll1lll1l1l_opy_ import bstack1ll1lllll11_opy_
from bstack_utils.helper import Notset, bstack1lll11ll11l_opy_, get_cli_dir, bstack1ll1ll11l11_opy_, bstack1lll11l111_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework
from browserstack_sdk.sdk_cli.utils.bstack1ll1llllll1_opy_ import bstack1ll1l1ll11l_opy_
from browserstack_sdk.sdk_cli.utils.bstack11l1lll11l_opy_ import bstack1111111l1_opy_
from bstack_utils.helper import Notset, bstack1lll11ll11l_opy_, get_cli_dir, bstack1ll1ll11l11_opy_, bstack1lll11l111_opy_, bstack1ll1l1l1l1_opy_, bstack11ll1l1l1_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll11ll11_opy_, bstack1lll1ll1111_opy_, bstack1lll1111lll_opy_, bstack1llll11llll_opy_
from browserstack_sdk.sdk_cli.bstack1llllllll1l_opy_ import bstack1llll1ll1l1_opy_, bstack1lllll1lll1_opy_, bstack1llll1lllll_opy_
from bstack_utils.constants import *
from bstack_utils.bstack1ll1llll_opy_ import bstack111ll111_opy_
from bstack_utils import bstack1l1111111_opy_
from typing import Any, List, Union, Dict
import traceback
from google.protobuf.json_format import MessageToDict
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
from functools import wraps
from bstack_utils.measure import measure
from bstack_utils.messages import bstack1llll1ll1_opy_, bstack1l11111lll_opy_
logger = bstack1l1111111_opy_.get_logger(__name__, bstack1l1111111_opy_.bstack1ll1llll1l1_opy_())
def bstack1ll1l1l1lll_opy_(bs_config):
    bstack1lll1l11ll1_opy_ = None
    bstack1llll111l1l_opy_ = None
    try:
        bstack1llll111l1l_opy_ = get_cli_dir()
        bstack1lll1l11ll1_opy_ = bstack1ll1ll11l11_opy_(bstack1llll111l1l_opy_)
        bstack1lll1l11l1l_opy_ = bstack1lll11ll11l_opy_(bstack1lll1l11ll1_opy_, bstack1llll111l1l_opy_, bs_config)
        bstack1lll1l11ll1_opy_ = bstack1lll1l11l1l_opy_ if bstack1lll1l11l1l_opy_ else bstack1lll1l11ll1_opy_
        if not bstack1lll1l11ll1_opy_:
            raise ValueError(bstack1l1ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡓࡅࡍࡢࡇࡑࡏ࡟ࡃࡋࡑࡣࡕࡇࡔࡉࠤ႞"))
    except Exception as ex:
        logger.debug(bstack1l1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡷ࡬ࡪࠦ࡬ࡢࡶࡨࡷࡹࠦࡢࡪࡰࡤࡶࡾࠦࡻࡾࠤ႟").format(ex))
        bstack1lll1l11ll1_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠢࡔࡆࡎࡣࡈࡒࡉࡠࡄࡌࡒࡤࡖࡁࡕࡊࠥႠ"))
        if bstack1lll1l11ll1_opy_:
            logger.debug(bstack1l1ll_opy_ (u"ࠣࡈࡤࡰࡱ࡯࡮ࡨࠢࡥࡥࡨࡱࠠࡵࡱࠣࡗࡉࡑ࡟ࡄࡎࡌࡣࡇࡏࡎࡠࡒࡄࡘࡍࠦࡦࡳࡱࡰࠤࡪࡴࡶࡪࡴࡲࡲࡲ࡫࡮ࡵ࠼ࠣࠦႡ") + str(bstack1lll1l11ll1_opy_) + bstack1l1ll_opy_ (u"ࠤࠥႢ"))
        else:
            logger.debug(bstack1l1ll_opy_ (u"ࠥࡒࡴࠦࡶࡢ࡮࡬ࡨ࡙ࠥࡄࡌࡡࡆࡐࡎࡥࡂࡊࡐࡢࡔࡆ࡚ࡈࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡩࡳࡼࡩࡳࡱࡱࡱࡪࡴࡴ࠼ࠢࡶࡩࡹࡻࡰࠡ࡯ࡤࡽࠥࡨࡥࠡ࡫ࡱࡧࡴࡳࡰ࡭ࡧࡷࡩ࠳ࠨႣ"))
    return bstack1lll1l11ll1_opy_, bstack1llll111l1l_opy_
bstack1llll111l11_opy_ = bstack1l1ll_opy_ (u"ࠦ࠾࠿࠹࠺ࠤႤ")
bstack1ll1ll1l1l1_opy_ = bstack1l1ll_opy_ (u"ࠧࡸࡥࡢࡦࡼࠦႥ")
bstack1ll1ll1l111_opy_ = bstack1l1ll_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡅࡍࡓࡥࡓࡆࡕࡖࡍࡔࡔ࡟ࡊࡆࠥႦ")
bstack1lll1l1ll11_opy_ = bstack1l1ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡆࡎࡔ࡟ࡍࡋࡖࡘࡊࡔ࡟ࡂࡆࡇࡖࠧႧ")
bstack1ll1l111ll_opy_ = bstack1l1ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠦႨ")
bstack1lll1l1ll1l_opy_ = re.compile(bstack1l1ll_opy_ (u"ࡴࠥࠬࡄ࡯ࠩ࠯ࠬࠫࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡾࡅࡗ࠮࠴ࠪࠣႩ"))
bstack1lll11l1l1l_opy_ = bstack1l1ll_opy_ (u"ࠥࡨࡪࡼࡥ࡭ࡱࡳࡱࡪࡴࡴࠣႪ")
bstack1lll111ll11_opy_ = [
    bstack111l1lll_opy_.bstack1l111ll1_opy_,
    bstack111l1lll_opy_.CONNECT,
    bstack111l1lll_opy_.bstack11l1l1ll1_opy_,
]
class SDKCLI:
    _1ll1l1ll1ll_opy_ = None
    process: Union[None, Any]
    bstack1lll1lll11l_opy_: bool
    bstack1lll111llll_opy_: bool
    bstack1llll1l1111_opy_: bool
    bin_session_id: Union[None, str]
    cli_bin_session_id: Union[None, str]
    cli_listen_addr: Union[None, str]
    bstack1lll11l11l1_opy_: Union[None, grpc.Channel]
    bstack1lll11lll11_opy_: str
    test_framework: TestFramework
    bstack1llllllll1l_opy_: bstack11111111l1_opy_
    session_framework: str
    config: Union[None, Dict[str, Any]]
    bstack1lll1l1111l_opy_: bstack1lll1l1l1l1_opy_
    accessibility: bstack1ll1l1l1ll1_opy_
    bstack11l1lll11l_opy_: bstack1111111l1_opy_
    ai: bstack1ll1ll1111l_opy_
    bstack1ll1ll11ll1_opy_: bstack1llll1111l1_opy_
    bstack1lll1ll1ll1_opy_: List[bstack1llll11lll1_opy_]
    config_testhub: Any
    config_observability: Any
    config_accessibility: Any
    bstack1lll1ll1lll_opy_: Any
    bstack1ll1llll1ll_opy_: Dict[str, timedelta]
    bstack1llll111111_opy_: str
    bstack111111l11l_opy_: bstack111111l1ll_opy_
    def __new__(cls):
        if not cls._1ll1l1ll1ll_opy_:
            cls._1ll1l1ll1ll_opy_ = super(SDKCLI, cls).__new__(cls)
        return cls._1ll1l1ll1ll_opy_
    def __init__(self):
        self.process = None
        self.bstack1lll1lll11l_opy_ = False
        self.bstack1lll11l11l1_opy_ = None
        self.bstack1lll1ll111l_opy_ = None
        self.cli_bin_session_id = None
        self.cli_listen_addr = os.environ.get(bstack1lll1l1ll11_opy_, None)
        self.bstack1ll1lll111l_opy_ = os.environ.get(bstack1ll1ll1l111_opy_, bstack1l1ll_opy_ (u"ࠦࠧႫ")) == bstack1l1ll_opy_ (u"ࠧࠨႬ")
        self.bstack1lll111llll_opy_ = False
        self.bstack1llll1l1111_opy_ = False
        self.config = None
        self.config_testhub = None
        self.config_observability = None
        self.config_accessibility = None
        self.bstack1lll1ll1lll_opy_ = None
        self.test_framework = None
        self.bstack1llllllll1l_opy_ = None
        self.bstack1lll11lll11_opy_=bstack1l1ll_opy_ (u"ࠨࠢႭ")
        self.session_framework = None
        self.logger = bstack1l1111111_opy_.get_logger(self.__class__.__name__, bstack1l1111111_opy_.bstack1ll1llll1l1_opy_())
        self.bstack1ll1llll1ll_opy_ = defaultdict(lambda: timedelta(microseconds=0))
        self.bstack111111l11l_opy_ = bstack111111l1ll_opy_()
        self.bstack1ll1llll111_opy_ = None
        self.bstack1lll111ll1l_opy_ = None
        self.bstack1lll1l1111l_opy_ = None
        self.accessibility = None
        self.ai = None
        self.percy = None
        self.bstack1lll1ll1ll1_opy_ = []
    def bstack1ll1ll111l_opy_(self):
        return os.environ.get(bstack1ll1l111ll_opy_).lower().__eq__(bstack1l1ll_opy_ (u"ࠢࡵࡴࡸࡩࠧႮ"))
    def is_enabled(self, config):
        if bstack1l1ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬႯ") in config and str(config[bstack1l1ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭Ⴐ")]).lower() != bstack1l1ll_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩႱ"):
            return False
        bstack1lll1lll1l1_opy_ = [bstack1l1ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦႲ"), bstack1l1ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤႳ")]
        bstack1ll1l1lll1l_opy_ = config.get(bstack1l1ll_opy_ (u"ࠨࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠤႴ")) in bstack1lll1lll1l1_opy_ or os.environ.get(bstack1l1ll_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨႵ")) in bstack1lll1lll1l1_opy_
        os.environ[bstack1l1ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡊࡕࡢࡖ࡚ࡔࡎࡊࡐࡊࠦႶ")] = str(bstack1ll1l1lll1l_opy_) # bstack1lll111l111_opy_ bstack1ll1lll1111_opy_ VAR to bstack1lll1l11111_opy_ is binary running
        return bstack1ll1l1lll1l_opy_
    def bstack1llllll111_opy_(self):
        for event in bstack1lll111ll11_opy_:
            bstack11ll1lll1l_opy_.register(
                event, lambda event_name, *args, **kwargs: bstack11ll1lll1l_opy_.logger.debug(bstack1l1ll_opy_ (u"ࠤࡾࡩࡻ࡫࡮ࡵࡡࡱࡥࡲ࡫ࡽࠡ࠿ࡁࠤࢀࡧࡲࡨࡵࢀࠤࠧႷ") + str(kwargs) + bstack1l1ll_opy_ (u"ࠥࠦႸ"))
            )
        bstack11ll1lll1l_opy_.register(bstack111l1lll_opy_.bstack1l111ll1_opy_, self.__1ll1lllll1l_opy_)
        bstack11ll1lll1l_opy_.register(bstack111l1lll_opy_.CONNECT, self.__1lll11l111l_opy_)
        bstack11ll1lll1l_opy_.register(bstack111l1lll_opy_.bstack11l1l1ll1_opy_, self.__1lll1111l1l_opy_)
        bstack11ll1lll1l_opy_.register(bstack111l1lll_opy_.bstack1ll1llll11_opy_, self.__1ll1l1ll111_opy_)
    def bstack11l111111_opy_(self):
        return not self.bstack1ll1lll111l_opy_ and os.environ.get(bstack1ll1ll1l111_opy_, bstack1l1ll_opy_ (u"ࠦࠧႹ")) != bstack1l1ll_opy_ (u"ࠧࠨႺ")
    def is_running(self):
        if self.bstack1ll1lll111l_opy_:
            return self.bstack1lll1lll11l_opy_
        else:
            return bool(self.bstack1lll11l11l1_opy_)
    def bstack1lll1l1l111_opy_(self, module):
        return any(isinstance(m, module) for m in self.bstack1lll1ll1ll1_opy_) and cli.is_running()
    def __1lll1llllll_opy_(self, bstack1lll111l1ll_opy_=10):
        if self.bstack1lll1ll111l_opy_:
            return
        bstack11l1l1111_opy_ = datetime.now()
        cli_listen_addr = os.environ.get(bstack1lll1l1ll11_opy_, self.cli_listen_addr)
        self.logger.debug(bstack1l1ll_opy_ (u"ࠨ࡛ࠣႻ") + str(id(self)) + bstack1l1ll_opy_ (u"ࠢ࡞ࠢࡦࡳࡳࡴࡥࡤࡶ࡬ࡲ࡬ࠨႼ"))
        channel = grpc.insecure_channel(cli_listen_addr, options=[(bstack1l1ll_opy_ (u"ࠣࡩࡵࡴࡨ࠴ࡥ࡯ࡣࡥࡰࡪࡥࡨࡵࡶࡳࡣࡵࡸ࡯ࡹࡻࠥႽ"), 0), (bstack1l1ll_opy_ (u"ࠤࡪࡶࡵࡩ࠮ࡦࡰࡤࡦࡱ࡫࡟ࡩࡶࡷࡴࡸࡥࡰࡳࡱࡻࡽࠧႾ"), 0)])
        grpc.channel_ready_future(channel).result(timeout=bstack1lll111l1ll_opy_)
        self.bstack1lll11l11l1_opy_ = channel
        self.bstack1lll1ll111l_opy_ = sdk_pb2_grpc.SDKStub(self.bstack1lll11l11l1_opy_)
        self.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠥ࡫ࡷࡶࡣ࠻ࡥࡲࡲࡳ࡫ࡣࡵࠤႿ"), datetime.now() - bstack11l1l1111_opy_)
        self.cli_listen_addr = cli_listen_addr
        os.environ[bstack1lll1l1ll11_opy_] = self.cli_listen_addr
        self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡧࡴࡴ࡮ࡦࡥࡷࡩࡩࡀࠠࡪࡵࡢࡧ࡭࡯࡬ࡥࡡࡳࡶࡴࡩࡥࡴࡵࡀࠦჀ") + str(self.bstack11l111111_opy_()) + bstack1l1ll_opy_ (u"ࠧࠨჁ"))
    def __1lll1111l1l_opy_(self, event_name):
        if self.bstack11l111111_opy_():
            self.logger.debug(bstack1l1ll_opy_ (u"ࠨࡣࡩ࡫࡯ࡨ࠲ࡶࡲࡰࡥࡨࡷࡸࡀࠠࡴࡶࡲࡴࡵ࡯࡮ࡨࠢࡆࡐࡎࠨჂ"))
        self.__1llll1l11ll_opy_()
    def __1ll1l1ll111_opy_(self, event_name, bstack1lll1ll1l1l_opy_ = None, bstack1l1l11l111_opy_=1):
        if bstack1l1l11l111_opy_ == 1:
            self.logger.error(bstack1l1ll_opy_ (u"ࠢࡔࡱࡰࡩࡹ࡮ࡩ࡯ࡩࠣࡻࡪࡴࡴࠡࡹࡵࡳࡳ࡭ࠢჃ"))
        bstack1ll1lll1lll_opy_ = Path(bstack1llll1l1l1l_opy_ (u"ࠣࡽࡶࡩࡱ࡬࠮ࡤ࡮࡬ࡣࡩ࡯ࡲࡾ࠱ࡸࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࡶ࠲࡯ࡹ࡯࡯ࠤჄ"))
        if self.bstack1llll111l1l_opy_ and bstack1ll1lll1lll_opy_.exists():
            with open(bstack1ll1lll1lll_opy_, bstack1l1ll_opy_ (u"ࠩࡵࠫჅ"), encoding=bstack1l1ll_opy_ (u"ࠪࡹࡹ࡬࠭࠹ࠩ჆")) as fp:
                data = json.load(fp)
                try:
                    bstack1ll1l1l1l1_opy_(bstack1l1ll_opy_ (u"ࠫࡕࡕࡓࡕࠩჇ"), bstack111ll111_opy_(bstack1ll1lll1_opy_), data, {
                        bstack1l1ll_opy_ (u"ࠬࡧࡵࡵࡪࠪ჈"): (self.config[bstack1l1ll_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ჉")], self.config[bstack1l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ჊")])
                    })
                except Exception as e:
                    logger.debug(bstack1l11111lll_opy_.format(str(e)))
            bstack1ll1lll1lll_opy_.unlink()
        sys.exit(bstack1l1l11l111_opy_)
    @measure(event_name=EVENTS.bstack1ll1lll11l1_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def __1ll1lllll1l_opy_(self, event_name: str, data):
        from bstack_utils.bstack11l1l111l_opy_ import bstack1llll11l1l1_opy_
        self.bstack1lll11lll11_opy_, self.bstack1llll111l1l_opy_ = bstack1ll1l1l1lll_opy_(data.bs_config)
        os.environ[bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡘࡔࡌࡘࡆࡈࡌࡆࡡࡇࡍࡗ࠭჋")] = self.bstack1llll111l1l_opy_
        if not self.bstack1lll11lll11_opy_ or not self.bstack1llll111l1l_opy_:
            raise ValueError(bstack1l1ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡸ࡭࡫ࠠࡔࡆࡎࠤࡈࡒࡉࠡࡤ࡬ࡲࡦࡸࡹࠣ჌"))
        if self.bstack11l111111_opy_():
            self.__1lll11l111l_opy_(event_name, bstack1l11111l1_opy_())
            return
        try:
            bstack1llll11l1l1_opy_.end(EVENTS.bstack1lll1lllll_opy_.value, EVENTS.bstack1lll1lllll_opy_.value + bstack1l1ll_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥჍ"), EVENTS.bstack1lll1lllll_opy_.value + bstack1l1ll_opy_ (u"ࠦ࠿࡫࡮ࡥࠤ჎"), status=True, failure=None, test_name=None)
            logger.debug(bstack1l1ll_opy_ (u"ࠧࡉ࡯࡮ࡲ࡯ࡩࡹ࡫ࠠࡔࡆࡎࠤࡘ࡫ࡴࡶࡲ࠱ࠦ჏"))
        except Exception as e:
            logger.debug(bstack1l1ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹࠠࡼࡿࠥა").format(e))
        start = datetime.now()
        is_started = self.__1lll1111ll1_opy_()
        self.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠢࡴࡲࡤࡻࡳࡥࡴࡪ࡯ࡨࠦბ"), datetime.now() - start)
        if is_started:
            start = datetime.now()
            self.__1lll1llllll_opy_()
            self.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠣࡥࡲࡲࡳ࡫ࡣࡵࡡࡷ࡭ࡲ࡫ࠢგ"), datetime.now() - start)
            start = datetime.now()
            self.__1lll1lll111_opy_(data)
            self.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠤࡶࡸࡦࡸࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡷ࡭ࡲ࡫ࠢდ"), datetime.now() - start)
    @measure(event_name=EVENTS.bstack1ll1ll11l1l_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def __1lll11l111l_opy_(self, event_name: str, data: bstack1l11111l1_opy_):
        if not self.bstack11l111111_opy_():
            self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡣࡰࡰࡱࡩࡨࡺ࠺ࠡࡰࡲࡸࠥࡧࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹࠢე"))
            return
        bin_session_id = os.environ.get(bstack1ll1ll1l111_opy_)
        start = datetime.now()
        self.__1lll1llllll_opy_()
        self.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠦࡨࡵ࡮࡯ࡧࡦࡸࡤࡺࡩ࡮ࡧࠥვ"), datetime.now() - start)
        self.cli_bin_session_id = bin_session_id
        self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶ࠾ࠥࡩ࡯࡯ࡰࡨࡧࡹ࡫ࡤࠡࡶࡲࠤࡪࡾࡩࡴࡶ࡬ࡲ࡬ࠦࡃࡍࡋࠣࠦზ") + str(bin_session_id) + bstack1l1ll_opy_ (u"ࠨࠢთ"))
        start = datetime.now()
        self.__1lll11111ll_opy_()
        self.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠢࡴࡶࡤࡶࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡵ࡫ࡰࡩࠧი"), datetime.now() - start)
    def __1lll1l111ll_opy_(self):
        if not self.bstack1lll1ll111l_opy_ or not self.cli_bin_session_id:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡥࡤࡲࡳࡵࡴࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡨࠤࡲࡵࡤࡶ࡮ࡨࡷࠧკ"))
            return
        bstack1lll1ll11ll_opy_ = {
            bstack1l1ll_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨლ"): (bstack1llll1111ll_opy_, bstack1ll1ll111ll_opy_, bstack1ll1lllll11_opy_),
            bstack1l1ll_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧმ"): (bstack1llll1l111l_opy_, bstack1llll111lll_opy_, bstack1lll11lll1l_opy_),
        }
        if not self.bstack1ll1llll111_opy_ and self.session_framework in bstack1lll1ll11ll_opy_:
            bstack1ll1ll1lll1_opy_, bstack1ll1lll11ll_opy_, bstack1lll1l1lll1_opy_ = bstack1lll1ll11ll_opy_[self.session_framework]
            bstack1lll11111l1_opy_ = bstack1ll1lll11ll_opy_()
            self.bstack1lll111ll1l_opy_ = bstack1lll11111l1_opy_
            self.bstack1ll1llll111_opy_ = bstack1lll1l1lll1_opy_
            self.bstack1lll1ll1ll1_opy_.append(bstack1lll11111l1_opy_)
            self.bstack1lll1ll1ll1_opy_.append(bstack1ll1ll1lll1_opy_(self.bstack1lll111ll1l_opy_))
        if not self.bstack1lll1l1111l_opy_ and self.config_observability and self.config_observability.success: # bstack1lll1l1l11l_opy_
            self.bstack1lll1l1111l_opy_ = bstack1lll1l1l1l1_opy_(self.bstack1ll1llll111_opy_, self.bstack1lll111ll1l_opy_) # bstack1lll11ll111_opy_
            self.bstack1lll1ll1ll1_opy_.append(self.bstack1lll1l1111l_opy_)
        if not self.accessibility and self.config_accessibility and self.config_accessibility.success:
            self.accessibility = bstack1ll1l1l1ll1_opy_(self.bstack1ll1llll111_opy_, self.bstack1lll111ll1l_opy_)
            self.bstack1lll1ll1ll1_opy_.append(self.accessibility)
        if not self.ai and isinstance(self.config, dict) and self.config.get(bstack1l1ll_opy_ (u"ࠦࡸ࡫࡬ࡧࡊࡨࡥࡱࠨნ"), False) == True:
            self.ai = bstack1ll1ll1111l_opy_()
            self.bstack1lll1ll1ll1_opy_.append(self.ai)
        if not self.percy and self.bstack1lll1ll1lll_opy_ and self.bstack1lll1ll1lll_opy_.success:
            self.percy = bstack1llll1111l1_opy_(self.bstack1lll1ll1lll_opy_)
            self.bstack1lll1ll1ll1_opy_.append(self.percy)
        for mod in self.bstack1lll1ll1ll1_opy_:
            if not mod.bstack1llll11l1ll_opy_():
                mod.configure(self.bstack1lll1ll111l_opy_, self.config, self.cli_bin_session_id, self.bstack111111l11l_opy_)
    def __1lll1llll11_opy_(self):
        for mod in self.bstack1lll1ll1ll1_opy_:
            if mod.bstack1llll11l1ll_opy_():
                mod.configure(self.bstack1lll1ll111l_opy_, None, None, None)
    @measure(event_name=EVENTS.bstack1llll11111l_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def __1lll1lll111_opy_(self, data):
        if not self.cli_bin_session_id or self.bstack1lll111llll_opy_:
            return
        self.__1ll1l1llll1_opy_(data)
        bstack11l1l1111_opy_ = datetime.now()
        req = structs.StartBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.path_project = os.getcwd()
        req.language = bstack1l1ll_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧო")
        req.sdk_language = bstack1l1ll_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࠨპ")
        req.path_config = data.path_config
        req.sdk_version = data.sdk_version
        req.test_framework = data.test_framework
        req.frameworks.extend(data.frameworks)
        req.framework_versions.update(data.framework_versions)
        req.env_vars.update({key: value for key, value in os.environ.items() if bool(bstack1lll1l1ll1l_opy_.search(key))})
        req.cli_args.extend(sys.argv)
        try:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠢ࡜ࠤჟ") + str(id(self)) + bstack1l1ll_opy_ (u"ࠣ࡟ࠣࡱࡦ࡯࡮࠮ࡲࡵࡳࡨ࡫ࡳࡴ࠼ࠣࡷࡹࡧࡲࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢრ"))
            r = self.bstack1lll1ll111l_opy_.StartBinSession(req)
            self.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠤࡪࡶࡵࡩ࠺ࡴࡶࡤࡶࡹࡥࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࠦს"), datetime.now() - bstack11l1l1111_opy_)
            os.environ[bstack1ll1ll1l111_opy_] = r.bin_session_id
            self.__1lll111111l_opy_(r)
            self.__1lll1l111ll_opy_()
            self.bstack111111l11l_opy_.start()
            self.bstack1lll111llll_opy_ = True
            self.logger.debug(bstack1l1ll_opy_ (u"ࠥ࡟ࠧტ") + str(id(self)) + bstack1l1ll_opy_ (u"ࠦࡢࠦ࡭ࡢ࡫ࡱ࠱ࡵࡸ࡯ࡤࡧࡶࡷ࠿ࠦࡣࡰࡰࡱࡩࡨࡺࡥࡥࠤუ"))
        except grpc.bstack1ll1llll11l_opy_ as bstack1llll11l111_opy_:
            self.logger.error(bstack1l1ll_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡹ࡯࡭ࡦࡱࡨࡹࡹ࠳ࡥࡳࡴࡲࡶ࠿ࠦࠢფ") + str(bstack1llll11l111_opy_) + bstack1l1ll_opy_ (u"ࠨࠢქ"))
            traceback.print_exc()
            raise bstack1llll11l111_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡲࡱࡥ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦღ") + str(e) + bstack1l1ll_opy_ (u"ࠣࠤყ"))
            traceback.print_exc()
            raise e
    @measure(event_name=EVENTS.bstack1lll11l1ll1_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def __1lll11111ll_opy_(self):
        if not self.bstack11l111111_opy_() or not self.cli_bin_session_id or self.bstack1llll1l1111_opy_:
            return
        bstack11l1l1111_opy_ = datetime.now()
        req = structs.ConnectBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        req.platform_index = int(os.environ.get(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩშ"), bstack1l1ll_opy_ (u"ࠪ࠴ࠬჩ")))
        try:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡠࠨც") + str(id(self)) + bstack1l1ll_opy_ (u"ࠧࡣࠠࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹ࠺ࠡࡥࡲࡲࡳ࡫ࡣࡵࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢძ"))
            r = self.bstack1lll1ll111l_opy_.ConnectBinSession(req)
            self.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡨࡵ࡮࡯ࡧࡦࡸࡤࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠥწ"), datetime.now() - bstack11l1l1111_opy_)
            self.__1lll111111l_opy_(r)
            self.__1lll1l111ll_opy_()
            self.bstack111111l11l_opy_.start()
            self.bstack1llll1l1111_opy_ = True
            self.logger.debug(bstack1l1ll_opy_ (u"ࠢ࡜ࠤჭ") + str(id(self)) + bstack1l1ll_opy_ (u"ࠣ࡟ࠣࡧ࡭࡯࡬ࡥ࠯ࡳࡶࡴࡩࡥࡴࡵ࠽ࠤࡨࡵ࡮࡯ࡧࡦࡸࡪࡪࠢხ"))
        except grpc.bstack1ll1llll11l_opy_ as bstack1llll11l111_opy_:
            self.logger.error(bstack1l1ll_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡶ࡬ࡱࡪࡵࡥࡶࡶ࠰ࡩࡷࡸ࡯ࡳ࠼ࠣࠦჯ") + str(bstack1llll11l111_opy_) + bstack1l1ll_opy_ (u"ࠥࠦჰ"))
            traceback.print_exc()
            raise bstack1llll11l111_opy_
        except grpc.RpcError as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡶࡵࡩ࠭ࡦࡴࡵࡳࡷࡀࠠࠣჱ") + str(e) + bstack1l1ll_opy_ (u"ࠧࠨჲ"))
            traceback.print_exc()
            raise e
    def __1lll111111l_opy_(self, r):
        self.bstack1llll11ll1l_opy_(r)
        if not r.bin_session_id or not r.config or not isinstance(r.config, str):
            raise ValueError(bstack1l1ll_opy_ (u"ࠨࡵ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡷࡪࡸࡶࡦࡴࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧჳ") + str(r))
        self.config = json.loads(r.config)
        if not self.config:
            raise ValueError(bstack1l1ll_opy_ (u"ࠢࡦ࡯ࡳࡸࡾࠦࡣࡰࡰࡩ࡭࡬ࠦࡦࡰࡷࡱࡨࠧჴ"))
        self.session_framework = r.session_framework
        self.config_testhub = r.testhub
        self.config_observability = r.observability
        self.config_accessibility = r.accessibility
        bstack1l1ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡖࡥࡳࡥࡼࠤ࡮ࡹࠠࡴࡧࡱࡸࠥࡵ࡮࡭ࡻࠣࡥࡸࠦࡰࡢࡴࡷࠤࡴ࡬ࠠࡵࡪࡨࠤࠧࡉ࡯࡯ࡰࡨࡧࡹࡈࡩ࡯ࡕࡨࡷࡸ࡯࡯࡯࠮ࠥࠤࡦࡴࡤࠡࡶ࡫࡭ࡸࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࡦࡲࡳࡰࠢࡸࡷࡪࡪࠠࡣࡻࠣࡗࡹࡧࡲࡵࡄ࡬ࡲࡘ࡫ࡳࡴ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡕࡪࡨࡶࡪ࡬࡯ࡳࡧ࠯ࠤࡓࡵ࡮ࡦࠢ࡫ࡥࡳࡪ࡬ࡪࡰࡪࠤ࡮ࡹࠠࡪ࡯ࡳࡰࡪࡳࡥ࡯ࡶࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥჵ")
        self.bstack1lll1ll1lll_opy_ = getattr(r, bstack1l1ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨჶ"), None)
        self.cli_bin_session_id = r.bin_session_id
        os.environ[bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧჷ")] = self.config_testhub.jwt
        os.environ[bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩჸ")] = self.config_testhub.build_hashed_id
    def bstack1lll11llll1_opy_(event_name: EVENTS, stage: STAGE):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if self.bstack1lll1lll11l_opy_:
                    return func(self, *args, **kwargs)
                @measure(event_name=event_name, stage=stage)
                def bstack1lll11l1l11_opy_(*a, **kw):
                    return func(self, *a, **kw)
                return bstack1lll11l1l11_opy_(*args, **kwargs)
            return wrapper
        return decorator
    @bstack1lll11llll1_opy_(event_name=EVENTS.bstack1lll1l11lll_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def __1lll1111ll1_opy_(self, bstack1lll111l1ll_opy_=10):
        if self.bstack1lll1lll11l_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡹࡴࡢࡴࡷ࠾ࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠢჹ"))
            return True
        self.logger.debug(bstack1l1ll_opy_ (u"ࠨࡳࡵࡣࡵࡸࠧჺ"))
        if os.getenv(bstack1l1ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡉࡓ࡜ࠢ჻")) == bstack1lll11l1l1l_opy_:
            self.cli_bin_session_id = bstack1lll11l1l1l_opy_
            self.cli_listen_addr = bstack1l1ll_opy_ (u"ࠣࡷࡱ࡭ࡽࡀ࠯ࡵ࡯ࡳ࠳ࡸࡪ࡫࠮ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࠰ࠩࡸ࠴ࡳࡰࡥ࡮ࠦჼ") % (self.cli_bin_session_id)
            self.bstack1lll1lll11l_opy_ = True
            return True
        self.process = subprocess.Popen(
            [self.bstack1lll11lll11_opy_, bstack1l1ll_opy_ (u"ࠤࡶࡨࡰࠨჽ")],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=dict(os.environ),
            text=True,
            universal_newlines=True, # bstack1lll111lll1_opy_ compat for text=True in bstack1ll1l1ll1l1_opy_ python
            encoding=bstack1l1ll_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤჾ"),
            bufsize=1,
            close_fds=True,
        )
        bstack1ll1lll1l11_opy_ = threading.Thread(target=self.__1llll1l11l1_opy_, args=(bstack1lll111l1ll_opy_,))
        bstack1ll1lll1l11_opy_.start()
        bstack1ll1lll1l11_opy_.join()
        if self.process.returncode is not None:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡷࡵࡧࡷ࡯࠼ࠣࡶࡪࡺࡵࡳࡰࡦࡳࡩ࡫࠽ࡼࡵࡨࡰ࡫࠴ࡰࡳࡱࡦࡩࡸࡹ࠮ࡳࡧࡷࡹࡷࡴࡣࡰࡦࡨࢁࠥࡵࡵࡵ࠿ࡾࡷࡪࡲࡦ࠯ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡶࡸࡩࡵࡵࡵ࠰ࡵࡩࡦࡪࠨࠪࡿࠣࡩࡷࡸ࠽ࠣჿ") + str(self.process.stderr.read()) + bstack1l1ll_opy_ (u"ࠧࠨᄀ"))
        if not self.bstack1lll1lll11l_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠨ࡛ࠣᄁ") + str(id(self)) + bstack1l1ll_opy_ (u"ࠢ࡞ࠢࡦࡰࡪࡧ࡮ࡶࡲࠥᄂ"))
            self.__1llll1l11ll_opy_()
        self.logger.debug(bstack1l1ll_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡱࡴࡲࡧࡪࡹࡳࡠࡴࡨࡥࡩࡿ࠺ࠡࠤᄃ") + str(self.bstack1lll1lll11l_opy_) + bstack1l1ll_opy_ (u"ࠤࠥᄄ"))
        return self.bstack1lll1lll11l_opy_
    def __1llll1l11l1_opy_(self, bstack1lll1l1llll_opy_=10):
        bstack1lll11ll1ll_opy_ = time.time()
        while self.process and time.time() - bstack1lll11ll1ll_opy_ < bstack1lll1l1llll_opy_:
            try:
                line = self.process.stdout.readline()
                if bstack1l1ll_opy_ (u"ࠥ࡭ࡩࡃࠢᄅ") in line:
                    self.cli_bin_session_id = line.split(bstack1l1ll_opy_ (u"ࠦ࡮ࡪ࠽ࠣᄆ"))[-1:][0].strip()
                    self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡩ࡬ࡪࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦ࠽ࠦᄇ") + str(self.cli_bin_session_id) + bstack1l1ll_opy_ (u"ࠨࠢᄈ"))
                    continue
                if bstack1l1ll_opy_ (u"ࠢ࡭࡫ࡶࡸࡪࡴ࠽ࠣᄉ") in line:
                    self.cli_listen_addr = line.split(bstack1l1ll_opy_ (u"ࠣ࡮࡬ࡷࡹ࡫࡮࠾ࠤᄊ"))[-1:][0].strip()
                    self.logger.debug(bstack1l1ll_opy_ (u"ࠤࡦࡰ࡮ࡥ࡬ࡪࡵࡷࡩࡳࡥࡡࡥࡦࡵ࠾ࠧᄋ") + str(self.cli_listen_addr) + bstack1l1ll_opy_ (u"ࠥࠦᄌ"))
                    continue
                if bstack1l1ll_opy_ (u"ࠦࡵࡵࡲࡵ࠿ࠥᄍ") in line:
                    port = line.split(bstack1l1ll_opy_ (u"ࠧࡶ࡯ࡳࡶࡀࠦᄎ"))[-1:][0].strip()
                    self.logger.debug(bstack1l1ll_opy_ (u"ࠨࡰࡰࡴࡷ࠾ࠧᄏ") + str(port) + bstack1l1ll_opy_ (u"ࠢࠣᄐ"))
                    continue
                if line.strip() == bstack1ll1ll1l1l1_opy_ and self.cli_bin_session_id and self.cli_listen_addr:
                    if os.getenv(bstack1l1ll_opy_ (u"ࠣࡕࡇࡏࡤࡉࡌࡊࡡࡉࡐࡆࡍ࡟ࡊࡑࡢࡗ࡙ࡘࡅࡂࡏࠥᄑ"), bstack1l1ll_opy_ (u"ࠤ࠴ࠦᄒ")) == bstack1l1ll_opy_ (u"ࠥ࠵ࠧᄓ"):
                        if not self.process.stdout.closed:
                            self.process.stdout.close()
                        if not self.process.stderr.closed:
                            self.process.stderr.close()
                    self.bstack1lll1lll11l_opy_ = True
                    return True
            except Exception as e:
                self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡪࡸࡲࡰࡴ࠽ࠤࠧᄔ") + str(e) + bstack1l1ll_opy_ (u"ࠧࠨᄕ"))
        return False
    @measure(event_name=EVENTS.bstack1lll1lllll1_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def __1llll1l11ll_opy_(self):
        if self.bstack1lll11l11l1_opy_:
            self.bstack111111l11l_opy_.stop()
            start = datetime.now()
            if self.bstack1ll1ll111l1_opy_():
                self.cli_bin_session_id = None
                if self.bstack1llll1l1111_opy_:
                    self.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠨࡳࡵࡱࡳࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡺࡩ࡮ࡧࠥᄖ"), datetime.now() - start)
                else:
                    self.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠢࡴࡶࡲࡴࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡴࡪ࡯ࡨࠦᄗ"), datetime.now() - start)
            self.__1lll1llll11_opy_()
            start = datetime.now()
            self.bstack1lll11l11l1_opy_.close()
            self.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠣࡦ࡬ࡷࡨࡵ࡮࡯ࡧࡦࡸࡤࡺࡩ࡮ࡧࠥᄘ"), datetime.now() - start)
            self.bstack1lll11l11l1_opy_ = None
        if self.process:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠤࡶࡸࡴࡶࠢᄙ"))
            start = datetime.now()
            self.process.terminate()
            self.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠥ࡯࡮ࡲ࡬ࡠࡶ࡬ࡱࡪࠨᄚ"), datetime.now() - start)
            self.process = None
            if self.bstack1ll1lll111l_opy_ and self.config_observability and self.config_testhub and self.config_testhub.testhub_events:
                self.bstack1llll1ll1l_opy_()
                self.logger.info(
                    bstack1l1ll_opy_ (u"࡛ࠦ࡯ࡳࡪࡶࠣ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿࠣࡸࡴࠦࡶࡪࡧࡺࠤࡧࡻࡩ࡭ࡦࠣࡶࡪࡶ࡯ࡳࡶ࠯ࠤ࡮ࡴࡳࡪࡩ࡫ࡸࡸ࠲ࠠࡢࡰࡧࠤࡲࡧ࡮ࡺࠢࡰࡳࡷ࡫ࠠࡥࡧࡥࡹ࡬࡭ࡩ࡯ࡩࠣ࡭ࡳ࡬࡯ࡳ࡯ࡤࡸ࡮ࡵ࡮ࠡࡣ࡯ࡰࠥࡧࡴࠡࡱࡱࡩࠥࡶ࡬ࡢࡥࡨࠥࡡࡴࠢᄛ").format(
                        self.config_testhub.build_hashed_id
                    )
                )
                os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡅ࡙ࡎࡒࡄࡠࡊࡄࡗࡍࡋࡄࡠࡋࡇࠫᄜ")] = self.config_testhub.build_hashed_id
        self.bstack1lll1lll11l_opy_ = False
    def __1ll1l1llll1_opy_(self, data):
        try:
            import selenium
            data.framework_versions[bstack1l1ll_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣᄝ")] = selenium.__version__
            data.frameworks.append(bstack1l1ll_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤᄞ"))
        except:
            pass
        try:
            from playwright._repo_version import __version__
            data.framework_versions[bstack1l1ll_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧᄟ")] = __version__
            data.frameworks.append(bstack1l1ll_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨᄠ"))
        except:
            pass
    def bstack1lll1l1l1ll_opy_(self, hub_url: str, platform_index: int, bstack1ll1lll111_opy_: Any):
        if self.bstack1llllllll1l_opy_:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡷࡰ࡯ࡰࡱࡧࡧࠤࡸ࡫ࡴࡶࡲࠣࡷࡪࡲࡥ࡯࡫ࡸࡱ࠿ࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡴࡧࡷࠤࡺࡶࠢᄡ"))
            return
        try:
            bstack11l1l1111_opy_ = datetime.now()
            import selenium
            from selenium.webdriver.remote.webdriver import WebDriver
            from selenium.webdriver.common.service import Service
            framework = bstack1l1ll_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨᄢ")
            self.bstack1llllllll1l_opy_ = bstack1lll11lll1l_opy_(
                cli.config.get(bstack1l1ll_opy_ (u"ࠧ࡮ࡵࡣࡗࡵࡰࠧᄣ"), hub_url),
                platform_index,
                framework_name=framework,
                framework_version=selenium.__version__,
                classes=[WebDriver],
                bstack1lll1l11l11_opy_={bstack1l1ll_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡥ࡯ࡱࡶ࡬ࡳࡳࡹ࡟ࡧࡴࡲࡱࡤࡩࡡࡱࡵࠥᄤ"): bstack1ll1lll111_opy_}
            )
            def bstack1lll11l1111_opy_(self):
                return
            if self.config.get(bstack1l1ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠤᄥ"), True):
                Service.start = bstack1lll11l1111_opy_
                Service.stop = bstack1lll11l1111_opy_
            def get_accessibility_results(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results(driver, framework_name=framework)
            def get_accessibility_results_summary(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.get_accessibility_results_summary(driver, framework_name=framework)
            def perform_scan(driver):
                if self.accessibility and self.accessibility.is_enabled():
                    return self.accessibility.perform_scan(driver, method=None, framework_name=framework)
            WebDriver.getAccessibilityResults = get_accessibility_results
            WebDriver.get_accessibility_results = get_accessibility_results
            WebDriver.getAccessibilityResultsSummary = get_accessibility_results_summary
            WebDriver.get_accessibility_results_summary = get_accessibility_results_summary
            WebDriver.upload_attachment = staticmethod(bstack1111111l1_opy_.upload_attachment)
            WebDriver.set_custom_tag = staticmethod(bstack1ll1l1ll11l_opy_.set_custom_tag)
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
            self.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤᄦ"), datetime.now() - bstack11l1l1111_opy_)
        except Exception as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡸ࡫࡬ࡦࡰ࡬ࡹࡲࡀࠠࠣᄧ") + str(e) + bstack1l1ll_opy_ (u"ࠥࠦᄨ"))
    def bstack1lll111l1l1_opy_(self, platform_index: int):
        try:
            from playwright.sync_api import BrowserType
            from playwright.sync_api import BrowserContext
            from playwright._impl._connection import Connection
            from playwright._repo_version import __version__
            from bstack_utils.helper import bstack1111l1l1l_opy_
            self.bstack1llllllll1l_opy_ = bstack1ll1lllll11_opy_(
                platform_index,
                framework_name=bstack1l1ll_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣᄩ"),
                framework_version=__version__,
                classes=[BrowserType, BrowserContext, Connection],
            )
        except Exception as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠾ࠥࠨᄪ") + str(e) + bstack1l1ll_opy_ (u"ࠨࠢᄫ"))
            pass
    def bstack1ll1ll1llll_opy_(self):
        if self.test_framework:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠢࡴ࡭࡬ࡴࡵ࡫ࡤࠡࡵࡨࡸࡺࡶࠠࡱࡻࡷࡩࡸࡺ࠺ࠡࡣ࡯ࡶࡪࡧࡤࡺࠢࡶࡩࡹࠦࡵࡱࠤᄬ"))
            return
        if bstack1lll11l111_opy_():
            import pytest
            self.test_framework = PytestBDDFramework({ bstack1l1ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣᄭ"): pytest.__version__ }, [bstack1l1ll_opy_ (u"ࠤࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠨᄮ")], self.bstack111111l11l_opy_, self.bstack1lll1ll111l_opy_)
            return
        try:
            import pytest
            self.test_framework = bstack1lll1l111l1_opy_({ bstack1l1ll_opy_ (u"ࠥࡴࡾࡺࡥࡴࡶࠥᄯ"): pytest.__version__ }, [bstack1l1ll_opy_ (u"ࠦࡵࡿࡴࡦࡵࡷࠦᄰ")], self.bstack111111l11l_opy_, self.bstack1lll1ll111l_opy_)
        except Exception as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱࡻࡷࡩࡸࡺ࠺ࠡࠤᄱ") + str(e) + bstack1l1ll_opy_ (u"ࠨࠢᄲ"))
        self.bstack1llll111ll1_opy_()
    def bstack1llll111ll1_opy_(self):
        if not self.bstack1ll1ll111l_opy_():
            return
        bstack1l1111l1ll_opy_ = None
        def bstack1ll1l1l1ll_opy_(config, startdir):
            return bstack1l1ll_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࠳ࢁࠧᄳ").format(bstack1l1ll_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢᄴ"))
        def bstack1l11l11ll1_opy_():
            return
        def bstack1l11l1l1ll_opy_(self, name: str, default=Notset(), skip: bool = False):
            if str(name).lower() == bstack1l1ll_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩᄵ"):
                return bstack1l1ll_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤᄶ")
            else:
                return bstack1l1111l1ll_opy_(self, name, default, skip)
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            bstack1l1111l1ll_opy_ = Config.getoption
            pytest_selenium.pytest_report_header = bstack1ll1l1l1ll_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1l11l11ll1_opy_
            Config.getoption = bstack1l11l1l1ll_opy_
        except Exception as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡷࡧ࡭ࠦࡰࡺࡶࡨࡷࡹࠦࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠡࡨࡲࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠾ࠥࠨᄷ") + str(e) + bstack1l1ll_opy_ (u"ࠧࠨᄸ"))
    def bstack1lll11l1lll_opy_(self):
        bstack1ll1l1ll1l_opy_ = MessageToDict(cli.config_testhub, preserving_proto_field_name=True)
        if isinstance(bstack1ll1l1ll1l_opy_, dict):
            if cli.config_observability:
                bstack1ll1l1ll1l_opy_.update(
                    {bstack1l1ll_opy_ (u"ࠨ࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࠨᄹ"): MessageToDict(cli.config_observability, preserving_proto_field_name=True)}
                )
            if cli.config_accessibility:
                accessibility = MessageToDict(cli.config_accessibility, preserving_proto_field_name=True)
                if isinstance(accessibility, dict) and bstack1l1ll_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࡴࡡࡷࡳࡤࡽࡲࡢࡲࠥᄺ") in accessibility.get(bstack1l1ll_opy_ (u"ࠣࡱࡳࡸ࡮ࡵ࡮ࡴࠤᄻ"), {}):
                    bstack1llll11l11l_opy_ = accessibility.get(bstack1l1ll_opy_ (u"ࠤࡲࡴࡹ࡯࡯࡯ࡵࠥᄼ"))
                    bstack1llll11l11l_opy_.update({ bstack1l1ll_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࡷ࡙ࡵࡗࡳࡣࡳࠦᄽ"): bstack1llll11l11l_opy_.pop(bstack1l1ll_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸࡥࡴࡰࡡࡺࡶࡦࡶࠢᄾ")) })
                bstack1ll1l1ll1l_opy_.update({bstack1l1ll_opy_ (u"ࠧࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠧᄿ"): accessibility })
        return bstack1ll1l1ll1l_opy_
    @measure(event_name=EVENTS.bstack1ll1ll1l1ll_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
    def bstack1ll1ll111l1_opy_(self, bstack1ll1ll11111_opy_: str = None, bstack1lll1llll1l_opy_: str = None, bstack1l1l11l111_opy_: int = None):
        if not self.cli_bin_session_id or not self.bstack1lll1ll111l_opy_:
            return
        bstack11l1l1111_opy_ = datetime.now()
        req = structs.StopBinSessionRequest()
        req.bin_session_id = self.cli_bin_session_id
        if bstack1l1l11l111_opy_:
            req.bstack1l1l11l111_opy_ = bstack1l1l11l111_opy_
        if bstack1ll1ll11111_opy_:
            req.bstack1ll1ll11111_opy_ = bstack1ll1ll11111_opy_
        if bstack1lll1llll1l_opy_:
            req.bstack1lll1llll1l_opy_ = bstack1lll1llll1l_opy_
        try:
            r = self.bstack1lll1ll111l_opy_.StopBinSession(req)
            SDKCLI.automate_buildlink = r.automate_buildlink
            SDKCLI.hashed_id = r.hashed_id
            self.bstack1l11llllll_opy_(bstack1l1ll_opy_ (u"ࠨࡧࡳࡲࡦ࠾ࡸࡺ࡯ࡱࡡࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠢᅀ"), datetime.now() - bstack11l1l1111_opy_)
            return r.success
        except grpc.RpcError as e:
            traceback.print_exc()
            raise e
    def bstack1l11llllll_opy_(self, key: str, value: timedelta):
        tag = bstack1l1ll_opy_ (u"ࠢࡤࡪ࡬ࡰࡩ࠳ࡰࡳࡱࡦࡩࡸࡹࠢᅁ") if self.bstack11l111111_opy_() else bstack1l1ll_opy_ (u"ࠣ࡯ࡤ࡭ࡳ࠳ࡰࡳࡱࡦࡩࡸࡹࠢᅂ")
        self.bstack1ll1llll1ll_opy_[bstack1l1ll_opy_ (u"ࠤ࠽ࠦᅃ").join([tag + bstack1l1ll_opy_ (u"ࠥ࠱ࠧᅄ") + str(id(self)), key])] += value
    def bstack1llll1ll1l_opy_(self):
        if not os.getenv(bstack1l1ll_opy_ (u"ࠦࡉࡋࡂࡖࡉࡢࡔࡊࡘࡆࠣᅅ"), bstack1l1ll_opy_ (u"ࠧ࠶ࠢᅆ")) == bstack1l1ll_opy_ (u"ࠨ࠱ࠣᅇ"):
            return
        bstack1ll1ll11lll_opy_ = dict()
        bstack1llllllllll_opy_ = []
        if self.test_framework:
            bstack1llllllllll_opy_.extend(list(self.test_framework.bstack1llllllllll_opy_.values()))
        if self.bstack1llllllll1l_opy_:
            bstack1llllllllll_opy_.extend(list(self.bstack1llllllll1l_opy_.bstack1llllllllll_opy_.values()))
        for instance in bstack1llllllllll_opy_:
            if not instance.platform_index in bstack1ll1ll11lll_opy_:
                bstack1ll1ll11lll_opy_[instance.platform_index] = defaultdict(lambda: timedelta(microseconds=0))
            report = bstack1ll1ll11lll_opy_[instance.platform_index]
            for k, v in instance.bstack1lll111l11l_opy_().items():
                report[k] += v
                report[k.split(bstack1l1ll_opy_ (u"ࠢ࠻ࠤᅈ"))[0]] += v
        bstack1lll1111111_opy_ = sorted([(k, v) for k, v in self.bstack1ll1llll1ll_opy_.items()], key=lambda o: o[1], reverse=True)
        bstack1ll1ll1ll11_opy_ = 0
        for r in bstack1lll1111111_opy_:
            bstack1lll1ll1l11_opy_ = r[1].total_seconds()
            bstack1ll1ll1ll11_opy_ += bstack1lll1ll1l11_opy_
            self.logger.debug(bstack1l1ll_opy_ (u"ࠣ࡝ࡳࡩࡷ࡬࡝ࠡࡥ࡯࡭࠿ࢁࡲ࡜࠲ࡠࢁࡂࠨᅉ") + str(bstack1lll1ll1l11_opy_) + bstack1l1ll_opy_ (u"ࠤࠥᅊ"))
        self.logger.debug(bstack1l1ll_opy_ (u"ࠥ࠱࠲ࠨᅋ"))
        bstack1lll1111l11_opy_ = []
        for platform_index, report in bstack1ll1ll11lll_opy_.items():
            bstack1lll1111l11_opy_.extend([(platform_index, k, v) for k, v in report.items()])
        bstack1lll1111l11_opy_.sort(key=lambda o: o[2], reverse=True)
        bstack1lll1ll1_opy_ = set()
        bstack1ll1l1lllll_opy_ = 0
        for r in bstack1lll1111l11_opy_:
            bstack1lll1ll1l11_opy_ = r[2].total_seconds()
            bstack1ll1l1lllll_opy_ += bstack1lll1ll1l11_opy_
            bstack1lll1ll1_opy_.add(r[0])
            self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡠࡶࡥࡳࡨࡠࠤࡹ࡫ࡳࡵ࠼ࡳࡰࡦࡺࡦࡰࡴࡰ࠱ࢀࡸ࡛࠱࡟ࢀ࠾ࢀࡸ࡛࠲࡟ࢀࡁࠧᅌ") + str(bstack1lll1ll1l11_opy_) + bstack1l1ll_opy_ (u"ࠧࠨᅍ"))
        if self.bstack11l111111_opy_():
            self.logger.debug(bstack1l1ll_opy_ (u"ࠨ࠭࠮ࠤᅎ"))
            self.logger.debug(bstack1l1ll_opy_ (u"ࠢ࡜ࡲࡨࡶ࡫ࡣࠠࡤ࡮࡬࠾ࡨ࡮ࡩ࡭ࡦ࠰ࡴࡷࡵࡣࡦࡵࡶࡁࢀࡺ࡯ࡵࡣ࡯ࡣࡨࡲࡩࡾࠢࡷࡩࡸࡺ࠺ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵ࠰ࡿࡸࡺࡲࠩࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶ࠭ࢂࡃࠢᅏ") + str(bstack1ll1l1lllll_opy_) + bstack1l1ll_opy_ (u"ࠣࠤᅐ"))
        else:
            self.logger.debug(bstack1l1ll_opy_ (u"ࠤ࡞ࡴࡪࡸࡦ࡞ࠢࡦࡰ࡮ࡀ࡭ࡢ࡫ࡱ࠱ࡵࡸ࡯ࡤࡧࡶࡷࡂࠨᅑ") + str(bstack1ll1ll1ll11_opy_) + bstack1l1ll_opy_ (u"ࠥࠦᅒ"))
        self.logger.debug(bstack1l1ll_opy_ (u"ࠦ࠲࠳ࠢᅓ"))
    def test_orchestration_session(self, test_files: list, orchestration_strategy: str):
        request = structs.TestOrchestrationRequest(
            bin_session_id=self.cli_bin_session_id,
            orchestration_strategy=orchestration_strategy,
            test_files=test_files
        )
        if not self.bstack1lll1ll111l_opy_:
            self.logger.error(bstack1l1ll_opy_ (u"ࠧࡩ࡬ࡪࡡࡶࡩࡷࡼࡩࡤࡧࠣ࡭ࡸࠦ࡮ࡰࡶࠣ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿ࡫ࡤ࠯ࠢࡆࡥࡳࡴ࡯ࡵࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡸࡪࡹࡴࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠯ࠤᅔ"))
            return None
        response = self.bstack1lll1ll111l_opy_.TestOrchestration(request)
        self.logger.debug(bstack1l1ll_opy_ (u"ࠨࡴࡦࡵࡷ࠱ࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠱ࡸ࡫ࡳࡴ࡫ࡲࡲࡂࢁࡽࠣᅕ").format(response))
        if response.success:
            return list(response.ordered_test_files)
        return None
    def bstack1llll11ll1l_opy_(self, r):
        if r is not None and getattr(r, bstack1l1ll_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࠨᅖ"), None) and getattr(r.testhub, bstack1l1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨᅗ"), None):
            errors = json.loads(r.testhub.errors.decode(bstack1l1ll_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣᅘ")))
            for bstack1ll1ll1l11l_opy_, err in errors.items():
                if err[bstack1l1ll_opy_ (u"ࠪࡸࡾࡶࡥࠨᅙ")] == bstack1l1ll_opy_ (u"ࠫ࡮ࡴࡦࡰࠩᅚ"):
                    self.logger.info(err[bstack1l1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᅛ")])
                else:
                    self.logger.error(err[bstack1l1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᅜ")])
    def bstack1l1lllllll_opy_(self):
        return SDKCLI.automate_buildlink, SDKCLI.hashed_id
cli = SDKCLI()