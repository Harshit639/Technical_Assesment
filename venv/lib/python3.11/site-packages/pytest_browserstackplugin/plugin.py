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
import datetime
import inspect
import logging
import signal
import threading
from uuid import uuid4
from bstack_utils.measure import bstack11l1l111l_opy_
from bstack_utils.percy_sdk import PercySDK
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack1l1l1l11_opy_, bstack11ll111l1_opy_, update, bstack1ll1lll111_opy_,
                                       bstack1ll1l1l1ll_opy_, bstack1l11l11ll1_opy_, bstack1lll11l1_opy_, bstack1l1l1lll11_opy_,
                                       bstack1l11lll1l1_opy_, bstack1111l1l11_opy_, bstack1l1llll1_opy_,
                                       bstack11l1l11l_opy_, getAccessibilityResults, getAccessibilityResultsSummary, perform_scan, bstack1lll1111l1_opy_)
from browserstack_sdk.bstack11l1ll111_opy_ import bstack1lll1111_opy_
from browserstack_sdk._version import __version__
from bstack_utils import bstack1l1111111_opy_
from bstack_utils.capture import bstack111ll11l11_opy_
from bstack_utils.config import Config
from bstack_utils.percy import *
from bstack_utils.constants import bstack111l1111l_opy_, bstack1llllll1ll_opy_, bstack11lll11l1l_opy_, \
    bstack11ll1111ll_opy_
from bstack_utils.helper import bstack11ll1ll11_opy_, bstack11l1111ll11_opy_, bstack1111ll1l1l_opy_, bstack11111111_opy_, bstack1l1ll1111ll_opy_, bstack1lllll1l11_opy_, \
    bstack11l11ll11l1_opy_, \
    bstack11l1111llll_opy_, bstack1l1l1l111l_opy_, bstack11ll1l1l1l_opy_, bstack11l1111111l_opy_, bstack1lll11l111_opy_, Notset, \
    bstack1l111l1l1_opy_, bstack11l1l111ll1_opy_, bstack11l111l1lll_opy_, Result, bstack11l11llll1l_opy_, bstack111lll1l111_opy_, bstack111l111ll1_opy_, \
    bstack1l1l111111_opy_, bstack1lll1l11ll_opy_, bstack1ll1l11l_opy_, bstack11l1l11111l_opy_
from bstack_utils.bstack111ll1ll1ll_opy_ import bstack111lll11111_opy_
from bstack_utils.messages import bstack1l1l1l1111_opy_, bstack11ll11ll11_opy_, bstack1l1ll111_opy_, bstack1111111l_opy_, bstack11lll1lll1_opy_, \
    bstack11l1l1l1l_opy_, bstack1llll111ll_opy_, bstack1l11l11l1l_opy_, bstack1ll1l1l11l_opy_, bstack1l1l1ll1ll_opy_, \
    bstack11l111lll1_opy_, bstack1ll1l1ll1_opy_
from bstack_utils.proxy import bstack11llll1l11_opy_, bstack11l1111l11_opy_
from bstack_utils.bstack1ll1lll1ll_opy_ import bstack111111llll1_opy_, bstack11111l1l1ll_opy_, bstack11111l1l111_opy_, bstack11111l11l11_opy_, \
    bstack11111l111ll_opy_, bstack11111l11ll1_opy_, bstack111111lllll_opy_, bstack1l111l1111_opy_, bstack11111l11lll_opy_
from bstack_utils.bstack11l1111l1l_opy_ import bstack1l11ll111_opy_
from bstack_utils.bstack1l1l11l11_opy_ import bstack1l1ll11lll_opy_, bstack11lll11l_opy_, bstack1l1l11lll1_opy_, \
    bstack1l1l111l1_opy_, bstack1111l1ll_opy_
from bstack_utils.bstack111ll11l1l_opy_ import bstack111ll1l1l1_opy_
from bstack_utils.bstack111llll111_opy_ import bstack11ll1llll1_opy_
import bstack_utils.accessibility as bstack111111l1l_opy_
from bstack_utils.bstack111lll1111_opy_ import bstack11ll1ll1_opy_
from bstack_utils.bstack11111lll_opy_ import bstack11111lll_opy_
from bstack_utils.bstack111llllll1_opy_ import bstack1ll1l111l1_opy_
from browserstack_sdk.__init__ import bstack1ll11lll_opy_
from browserstack_sdk.sdk_cli.bstack1llll1l1ll1_opy_ import bstack1lll1l1l1l1_opy_
from browserstack_sdk.sdk_cli.bstack11ll1lll1l_opy_ import bstack11ll1lll1l_opy_, bstack111l1lll_opy_, bstack1l11111l1_opy_
from browserstack_sdk.sdk_cli.test_framework import bstack1l111lll1ll_opy_, bstack1llll11ll11_opy_, bstack1lll1111lll_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack11ll1lll1l_opy_ import bstack11ll1lll1l_opy_, bstack111l1lll_opy_, bstack1l11111l1_opy_
bstack1l11lll1l_opy_ = None
bstack1l1l11lll_opy_ = None
bstack1l1ll1ll1l_opy_ = None
bstack11111llll_opy_ = None
bstack11llll111_opy_ = None
bstack1111l11l1_opy_ = None
bstack1ll111ll1_opy_ = None
bstack11l111ll_opy_ = None
bstack1l11lll1ll_opy_ = None
bstack11ll111lll_opy_ = None
bstack1l1111l1ll_opy_ = None
bstack11ll1111l_opy_ = None
bstack11ll1lll_opy_ = None
bstack111llll11_opy_ = bstack1l1ll_opy_ (u"ࠨࠩⅲ")
CONFIG = {}
bstack1llll1l1l1_opy_ = False
bstack1lll11lll_opy_ = bstack1l1ll_opy_ (u"ࠩࠪⅳ")
bstack111ll1l1_opy_ = bstack1l1ll_opy_ (u"ࠪࠫⅴ")
bstack1llll1l1_opy_ = False
bstack1lllllll1_opy_ = []
bstack11l1llll11_opy_ = bstack111l1111l_opy_
bstack1llll1ll11ll_opy_ = bstack1l1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫⅵ")
bstack1l11l1111_opy_ = {}
bstack1l1l1ll1l_opy_ = None
bstack1lll111l1l_opy_ = False
logger = bstack1l1111111_opy_.get_logger(__name__, bstack11l1llll11_opy_)
store = {
    bstack1l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩⅶ"): []
}
bstack1llll1l11l11_opy_ = False
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_1111lll1ll_opy_ = {}
current_test_uuid = None
cli_context = bstack1l111lll1ll_opy_(
    test_framework_name=bstack1ll1llll1_opy_[bstack1l1ll_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙࠳ࡂࡅࡆࠪⅷ")] if bstack1lll11l111_opy_() else bstack1ll1llll1_opy_[bstack1l1ll_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚ࠧⅸ")],
    test_framework_version=pytest.__version__,
    platform_index=-1,
)
def bstack1ll11111l1_opy_(page, bstack11lll1lll_opy_):
    try:
        page.evaluate(bstack1l1ll_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤⅹ"),
                      bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭ⅺ") + json.dumps(
                          bstack11lll1lll_opy_) + bstack1l1ll_opy_ (u"ࠥࢁࢂࠨⅻ"))
    except Exception as e:
        print(bstack1l1ll_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾࠤⅼ"), e)
def bstack11l111l1ll_opy_(page, message, level):
    try:
        page.evaluate(bstack1l1ll_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨⅽ"), bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫⅾ") + json.dumps(
            message) + bstack1l1ll_opy_ (u"ࠧ࠭ࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠪⅿ") + json.dumps(level) + bstack1l1ll_opy_ (u"ࠨࡿࢀࠫↀ"))
    except Exception as e:
        print(bstack1l1ll_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡾࢁࠧↁ"), e)
def pytest_configure(config):
    global bstack1lll11lll_opy_
    global CONFIG
    bstack11l1lll1_opy_ = Config.bstack11ll11ll1_opy_()
    config.args = bstack11ll1llll1_opy_.bstack1llll1lll111_opy_(config.args)
    bstack11l1lll1_opy_.bstack1ll1111lll_opy_(bstack1ll1l11l_opy_(config.getoption(bstack1l1ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧↂ"))))
    try:
        bstack1l1111111_opy_.bstack111ll11lll1_opy_(config.inipath, config.rootpath)
    except:
        pass
    if cli.is_running():
        bstack11ll1lll1l_opy_.invoke(bstack111l1lll_opy_.CONNECT, bstack1l11111l1_opy_())
        cli_context.platform_index = int(os.environ.get(bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫↃ"), bstack1l1ll_opy_ (u"ࠬ࠶ࠧↄ")))
        config = json.loads(os.environ.get(bstack1l1ll_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࠧↅ"), bstack1l1ll_opy_ (u"ࠢࡼࡿࠥↆ")))
        cli.bstack1lll1l1l1ll_opy_(bstack11ll1l1l1l_opy_(bstack1lll11lll_opy_, CONFIG), cli_context.platform_index, bstack1ll1lll111_opy_)
    if cli.bstack1lll1l1l111_opy_(bstack1lll1l1l1l1_opy_):
        cli.bstack1ll1ll1llll_opy_()
        logger.debug(bstack1l1ll_opy_ (u"ࠣࡅࡏࡍࠥ࡯ࡳࠡࡣࡦࡸ࡮ࡼࡥࠡࡨࡲࡶࠥࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࡃࠢↇ") + str(cli_context.platform_index) + bstack1l1ll_opy_ (u"ࠤࠥↈ"))
        cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.BEFORE_ALL, bstack1lll1111lll_opy_.PRE, config)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    when = getattr(call, bstack1l1ll_opy_ (u"ࠥࡻ࡭࡫࡮ࠣ↉"), None)
    if cli.is_running() and when == bstack1l1ll_opy_ (u"ࠦࡨࡧ࡬࡭ࠤ↊"):
        cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.LOG_REPORT, bstack1lll1111lll_opy_.PRE, item, call)
    outcome = yield
    if when == bstack1l1ll_opy_ (u"ࠧࡩࡡ࡭࡮ࠥ↋"):
        report = outcome.get_result()
        passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1l1ll_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣ↌")))
        if not passed:
            config = json.loads(os.environ.get(bstack1l1ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࠨ↍"), bstack1l1ll_opy_ (u"ࠣࡽࢀࠦ↎")))
            if bstack1ll1l111l1_opy_.bstack1l1ll1l1l_opy_(config):
                bstack111l111111l_opy_ = bstack1ll1l111l1_opy_.bstack1l1ll1ll1_opy_(config)
                if item.execution_count > bstack111l111111l_opy_:
                    print(bstack1l1ll_opy_ (u"ࠩࡗࡩࡸࡺࠠࡧࡣ࡬ࡰࡪࡪࠠࡢࡨࡷࡩࡷࠦࡲࡦࡶࡵ࡭ࡪࡹ࠺ࠡࠩ↏"), report.nodeid, os.environ.get(bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ←")))
                    bstack1ll1l111l1_opy_.bstack111l1l11111_opy_(report.nodeid)
            else:
                print(bstack1l1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࠫ↑"), report.nodeid, os.environ.get(bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ→")))
                bstack1ll1l111l1_opy_.bstack111l1l11111_opy_(report.nodeid)
        else:
            print(bstack1l1ll_opy_ (u"࠭ࡔࡦࡵࡷࠤࡵࡧࡳࡴࡧࡧ࠾ࠥ࠭↓"), report.nodeid, os.environ.get(bstack1l1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ↔")))
    if cli.is_running():
        if when == bstack1l1ll_opy_ (u"ࠣࡵࡨࡸࡺࡶࠢ↕"):
            cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.BEFORE_EACH, bstack1lll1111lll_opy_.POST, item, call, outcome)
        elif when == bstack1l1ll_opy_ (u"ࠤࡦࡥࡱࡲࠢ↖"):
            cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.LOG_REPORT, bstack1lll1111lll_opy_.POST, item, call, outcome)
        elif when == bstack1l1ll_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧ↗"):
            cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.AFTER_EACH, bstack1lll1111lll_opy_.POST, item, call, outcome)
        return # skip all existing bstack1llll11ll1ll_opy_
    skipSessionName = item.config.getoption(bstack1l1ll_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭↘"))
    plugins = item.config.getoption(bstack1l1ll_opy_ (u"ࠧࡶ࡬ࡶࡩ࡬ࡲࡸࠨ↙"))
    report = outcome.get_result()
    os.environ[bstack1l1ll_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙ࡥࡔࡆࡕࡗࡣࡓࡇࡍࡆࠩ↚")] = report.nodeid
    bstack1llll11ll11l_opy_(item, call, report)
    if bstack1l1ll_opy_ (u"ࠢࡱࡻࡷࡩࡸࡺ࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡶ࡬ࡶࡩ࡬ࡲࠧ↛") not in plugins or bstack1lll11l111_opy_():
        return
    summary = []
    driver = getattr(item, bstack1l1ll_opy_ (u"ࠣࡡࡧࡶ࡮ࡼࡥࡳࠤ↜"), None)
    page = getattr(item, bstack1l1ll_opy_ (u"ࠤࡢࡴࡦ࡭ࡥࠣ↝"), None)
    try:
        if (driver == None or driver.session_id == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None or cli.is_running()):
        bstack1llll1ll1ll1_opy_(item, report, summary, skipSessionName)
    if (page is not None):
        bstack1llll1ll11l1_opy_(item, report, summary, skipSessionName)
def bstack1llll1ll1ll1_opy_(item, report, summary, skipSessionName):
    if report.when == bstack1l1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ↞") and report.skipped:
        bstack11111l11lll_opy_(report)
    if report.when in [bstack1l1ll_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࠥ↟"), bstack1l1ll_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴࠢ↠")]:
        return
    if not bstack1l1ll1111ll_opy_():
        return
    try:
        if ((str(skipSessionName).lower() != bstack1l1ll_opy_ (u"࠭ࡴࡳࡷࡨࠫ↡")) and (not cli.is_running())) and item._driver.session_id:
            item._driver.execute_script(
                bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬ↢") + json.dumps(
                    report.nodeid) + bstack1l1ll_opy_ (u"ࠨࡿࢀࠫ↣"))
        os.environ[bstack1l1ll_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬ↤")] = report.nodeid
    except Exception as e:
        summary.append(
            bstack1l1ll_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩ࠿ࠦࡻ࠱ࡿࠥ↥").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1l1ll_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨ↦")))
    bstack1l1l11ll_opy_ = bstack1l1ll_opy_ (u"ࠧࠨ↧")
    bstack11111l11lll_opy_(report)
    if not passed:
        try:
            bstack1l1l11ll_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack1l1ll_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨ↨").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1l1l11ll_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack1l1ll_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤ↩")))
        bstack1l1l11ll_opy_ = bstack1l1ll_opy_ (u"ࠣࠤ↪")
        if not passed:
            try:
                bstack1l1l11ll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1l1ll_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡧࡷࡩࡷࡳࡩ࡯ࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡷ࡫ࡡࡴࡱࡱ࠾ࠥࢁ࠰ࡾࠤ↫").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1l1l11ll_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡤࡢࡶࡤࠦ࠿ࠦࠧ↬")
                    + json.dumps(bstack1l1ll_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠥࠧ↭"))
                    + bstack1l1ll_opy_ (u"ࠧࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࠣ↮")
                )
            else:
                item._driver.execute_script(
                    bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡨࡦࡺࡡࠣ࠼ࠣࠫ↯")
                    + json.dumps(str(bstack1l1l11ll_opy_))
                    + bstack1l1ll_opy_ (u"ࠢ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࢀࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡿࠥ↰")
                )
        except Exception as e:
            summary.append(bstack1l1ll_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡡ࡯ࡰࡲࡸࡦࡺࡥ࠻ࠢࡾ࠴ࢂࠨ↱").format(e))
def bstack1llll1l1l111_opy_(test_name, error_message):
    try:
        bstack1llll11ll111_opy_ = []
        bstack1ll1l1111l_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ↲"), bstack1l1ll_opy_ (u"ࠪ࠴ࠬ↳"))
        bstack1l111l1l_opy_ = {bstack1l1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ↴"): test_name, bstack1l1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ↵"): error_message, bstack1l1ll_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ↶"): bstack1ll1l1111l_opy_}
        bstack1llll11lll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1ll_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ↷"))
        if os.path.exists(bstack1llll11lll1l_opy_):
            with open(bstack1llll11lll1l_opy_) as f:
                bstack1llll11ll111_opy_ = json.load(f)
        bstack1llll11ll111_opy_.append(bstack1l111l1l_opy_)
        with open(bstack1llll11lll1l_opy_, bstack1l1ll_opy_ (u"ࠨࡹࠪ↸")) as f:
            json.dump(bstack1llll11ll111_opy_, f)
    except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵ࡫ࡲࡴ࡫ࡶࡸ࡮ࡴࡧࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡶࡹࡵࡧࡶࡸࠥ࡫ࡲࡳࡱࡵࡷ࠿ࠦࠧ↹") + str(e))
def bstack1llll1ll11l1_opy_(item, report, summary, skipSessionName):
    if report.when in [bstack1l1ll_opy_ (u"ࠥࡷࡪࡺࡵࡱࠤ↺"), bstack1l1ll_opy_ (u"ࠦࡹ࡫ࡡࡳࡦࡲࡻࡳࠨ↻")]:
        return
    if (str(skipSessionName).lower() != bstack1l1ll_opy_ (u"ࠬࡺࡲࡶࡧࠪ↼")):
        bstack1ll11111l1_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack1l1ll_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣ↽")))
    bstack1l1l11ll_opy_ = bstack1l1ll_opy_ (u"ࠢࠣ↾")
    bstack11111l11lll_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1l1l11ll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack1l1ll_opy_ (u"࡙ࠣࡄࡖࡓࡏࡎࡈ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡤࡦࡶࡨࡶࡲ࡯࡮ࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡶࡪࡧࡳࡰࡰ࠽ࠤࢀ࠶ࡽࠣ↿").format(e)
                )
        try:
            if passed:
                bstack1111l1ll_opy_(getattr(item, bstack1l1ll_opy_ (u"ࠩࡢࡴࡦ࡭ࡥࠨ⇀"), None), bstack1l1ll_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ⇁"))
            else:
                error_message = bstack1l1ll_opy_ (u"ࠫࠬ⇂")
                if bstack1l1l11ll_opy_:
                    bstack11l111l1ll_opy_(item._page, str(bstack1l1l11ll_opy_), bstack1l1ll_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦ⇃"))
                    bstack1111l1ll_opy_(getattr(item, bstack1l1ll_opy_ (u"࠭࡟ࡱࡣࡪࡩࠬ⇄"), None), bstack1l1ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ⇅"), str(bstack1l1l11ll_opy_))
                    error_message = str(bstack1l1l11ll_opy_)
                else:
                    bstack1111l1ll_opy_(getattr(item, bstack1l1ll_opy_ (u"ࠨࡡࡳࡥ࡬࡫ࠧ⇆"), None), bstack1l1ll_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ⇇"))
                bstack1llll1l1l111_opy_(report.nodeid, error_message)
        except Exception as e:
            summary.append(bstack1l1ll_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡷࡳࡨࡦࡺࡥࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿ࠵ࢃࠢ⇈").format(e))
def pytest_addoption(parser):
    parser.addoption(bstack1l1ll_opy_ (u"ࠦ࠲࠳ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ⇉"), default=bstack1l1ll_opy_ (u"ࠧࡌࡡ࡭ࡵࡨࠦ⇊"), help=bstack1l1ll_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡩࡤࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠧ⇋"))
    parser.addoption(bstack1l1ll_opy_ (u"ࠢ࠮࠯ࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨ⇌"), default=bstack1l1ll_opy_ (u"ࠣࡈࡤࡰࡸ࡫ࠢ⇍"), help=bstack1l1ll_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡧࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠣ⇎"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack1l1ll_opy_ (u"ࠥ࠱࠲ࡪࡲࡪࡸࡨࡶࠧ⇏"), action=bstack1l1ll_opy_ (u"ࠦࡸࡺ࡯ࡳࡧࠥ⇐"), default=bstack1l1ll_opy_ (u"ࠧࡩࡨࡳࡱࡰࡩࠧ⇑"),
                         help=bstack1l1ll_opy_ (u"ࠨࡄࡳ࡫ࡹࡩࡷࠦࡴࡰࠢࡵࡹࡳࠦࡴࡦࡵࡷࡷࠧ⇒"))
def bstack111lll11ll_opy_(log):
    if not (log[bstack1l1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⇓")] and log[bstack1l1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⇔")].strip()):
        return
    active = bstack111lll11l1_opy_()
    log = {
        bstack1l1ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ⇕"): log[bstack1l1ll_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ⇖")],
        bstack1l1ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ⇗"): bstack1111ll1l1l_opy_().isoformat() + bstack1l1ll_opy_ (u"ࠬࡠࠧ⇘"),
        bstack1l1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⇙"): log[bstack1l1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⇚")],
    }
    if active:
        if active[bstack1l1ll_opy_ (u"ࠨࡶࡼࡴࡪ࠭⇛")] == bstack1l1ll_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ⇜"):
            log[bstack1l1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ⇝")] = active[bstack1l1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇞")]
        elif active[bstack1l1ll_opy_ (u"ࠬࡺࡹࡱࡧࠪ⇟")] == bstack1l1ll_opy_ (u"࠭ࡴࡦࡵࡷࠫ⇠"):
            log[bstack1l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⇡")] = active[bstack1l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ⇢")]
    bstack11ll1ll1_opy_.bstack11l1l1lll1_opy_([log])
def bstack111lll11l1_opy_():
    if len(store[bstack1l1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭⇣")]) > 0 and store[bstack1l1ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧ⇤")][-1]:
        return {
            bstack1l1ll_opy_ (u"ࠫࡹࡿࡰࡦࠩ⇥"): bstack1l1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪ⇦"),
            bstack1l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⇧"): store[bstack1l1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡪࡲࡳࡰࡥࡵࡶ࡫ࡧࠫ⇨")][-1]
        }
    if store.get(bstack1l1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ⇩"), None):
        return {
            bstack1l1ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ⇪"): bstack1l1ll_opy_ (u"ࠪࡸࡪࡹࡴࠨ⇫"),
            bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⇬"): store[bstack1l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ⇭")]
        }
    return None
def pytest_runtest_logstart(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.INIT_TEST, bstack1lll1111lll_opy_.PRE, nodeid, location)
def pytest_runtest_logfinish(nodeid, location):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.INIT_TEST, bstack1lll1111lll_opy_.POST, nodeid, location)
def pytest_runtest_call(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.TEST, bstack1lll1111lll_opy_.PRE, item)
        return
    try:
        global CONFIG
        item._1llll1l1llll_opy_ = True
        bstack11l1ll111l_opy_ = bstack111111l1l_opy_.bstack1lllll1111_opy_(bstack11l1111llll_opy_(item.own_markers))
        if not cli.bstack1lll1l1l111_opy_(bstack1lll1l1l1l1_opy_):
            item._a11y_test_case = bstack11l1ll111l_opy_
            if bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ⇮"), None):
                driver = getattr(item, bstack1l1ll_opy_ (u"ࠧࡠࡦࡵ࡭ࡻ࡫ࡲࠨ⇯"), None)
                item._a11y_started = bstack111111l1l_opy_.bstack1l1ll1llll_opy_(driver, bstack11l1ll111l_opy_)
        if not bstack11ll1ll1_opy_.on() or bstack1llll1ll11ll_opy_ != bstack1l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ⇰"):
            return
        global current_test_uuid #, bstack111ll111l1_opy_
        bstack1111ll111l_opy_ = {
            bstack1l1ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ⇱"): uuid4().__str__(),
            bstack1l1ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⇲"): bstack1111ll1l1l_opy_().isoformat() + bstack1l1ll_opy_ (u"ࠫ࡟࠭⇳")
        }
        current_test_uuid = bstack1111ll111l_opy_[bstack1l1ll_opy_ (u"ࠬࡻࡵࡪࡦࠪ⇴")]
        store[bstack1l1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ⇵")] = bstack1111ll111l_opy_[bstack1l1ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⇶")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _1111lll1ll_opy_[item.nodeid] = {**_1111lll1ll_opy_[item.nodeid], **bstack1111ll111l_opy_}
        bstack1llll1l111ll_opy_(item, _1111lll1ll_opy_[item.nodeid], bstack1l1ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ⇷"))
    except Exception as err:
        print(bstack1l1ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡴࡸࡲࡹ࡫ࡳࡵࡡࡦࡥࡱࡲ࠺ࠡࡽࢀࠫ⇸"), str(err))
def pytest_runtest_setup(item):
    store[bstack1l1ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ⇹")] = item
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.BEFORE_EACH, bstack1lll1111lll_opy_.PRE, item, bstack1l1ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ⇺"))
    if bstack1ll1l111l1_opy_.bstack111l111ll1l_opy_():
            bstack1llll1ll1111_opy_ = bstack1l1ll_opy_ (u"࡙ࠧ࡫ࡪࡲࡳ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡧࡳࠡࡶ࡫ࡩࠥࡧࡢࡰࡴࡷࠤࡧࡻࡩ࡭ࡦࠣࡪ࡮ࡲࡥࠡࡧࡻ࡭ࡸࡺࡳ࠯ࠤ⇻")
            logger.error(bstack1llll1ll1111_opy_)
            bstack1111ll111l_opy_ = {
                bstack1l1ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⇼"): uuid4().__str__(),
                bstack1l1ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⇽"): bstack1111ll1l1l_opy_().isoformat() + bstack1l1ll_opy_ (u"ࠨ࡜ࠪ⇾"),
                bstack1l1ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⇿"): bstack1111ll1l1l_opy_().isoformat() + bstack1l1ll_opy_ (u"ࠪ࡞ࠬ∀"),
                bstack1l1ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫ∁"): bstack1l1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭∂"),
                bstack1l1ll_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭∃"): bstack1llll1ll1111_opy_,
                bstack1l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭∄"): [],
                bstack1l1ll_opy_ (u"ࠨࡨ࡬ࡼࡹࡻࡲࡦࡵࠪ∅"): []
            }
            bstack1llll1l111ll_opy_(item, bstack1111ll111l_opy_, bstack1l1ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖ࡯࡮ࡶࡰࡦࡦࠪ∆"))
            pytest.skip(bstack1llll1ll1111_opy_)
            return # skip all existing bstack1llll11ll1ll_opy_
    global bstack1llll1l11l11_opy_
    threading.current_thread().percySessionName = item.nodeid
    if bstack11l1111111l_opy_():
        atexit.register(bstack11lllll1l1_opy_)
        if not bstack1llll1l11l11_opy_:
            try:
                bstack1llll1l1ll1l_opy_ = [signal.SIGINT, signal.SIGTERM]
                if not bstack11l1l11111l_opy_():
                    bstack1llll1l1ll1l_opy_.extend([signal.SIGHUP, signal.SIGQUIT])
                for s in bstack1llll1l1ll1l_opy_:
                    signal.signal(s, bstack1llll1l1111l_opy_)
                bstack1llll1l11l11_opy_ = True
            except Exception as e:
                logger.debug(
                    bstack1l1ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡨ࡫ࡶࡸࡪࡸࠠࡴ࡫ࡪࡲࡦࡲࠠࡩࡣࡱࡨࡱ࡫ࡲࡴ࠼ࠣࠦ∇") + str(e))
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack111111llll1_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack1l1ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ∈")
    try:
        if not bstack11ll1ll1_opy_.on():
            return
        uuid = uuid4().__str__()
        bstack1111ll111l_opy_ = {
            bstack1l1ll_opy_ (u"ࠬࡻࡵࡪࡦࠪ∉"): uuid,
            bstack1l1ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ∊"): bstack1111ll1l1l_opy_().isoformat() + bstack1l1ll_opy_ (u"࡛ࠧࠩ∋"),
            bstack1l1ll_opy_ (u"ࠨࡶࡼࡴࡪ࠭∌"): bstack1l1ll_opy_ (u"ࠩ࡫ࡳࡴࡱࠧ∍"),
            bstack1l1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡶࡼࡴࡪ࠭∎"): bstack1l1ll_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩ∏"),
            bstack1l1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡲࡦࡳࡥࠨ∐"): bstack1l1ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ∑")
        }
        threading.current_thread().current_hook_uuid = uuid
        threading.current_thread().current_test_item = item
        store[bstack1l1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ−")] = item
        store[bstack1l1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡ࡫ࡳࡴࡱ࡟ࡶࡷ࡬ࡨࠬ∓")] = [uuid]
        if not _1111lll1ll_opy_.get(item.nodeid, None):
            _1111lll1ll_opy_[item.nodeid] = {bstack1l1ll_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨ∔"): [], bstack1l1ll_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬ∕"): []}
        _1111lll1ll_opy_[item.nodeid][bstack1l1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ∖")].append(bstack1111ll111l_opy_[bstack1l1ll_opy_ (u"ࠬࡻࡵࡪࡦࠪ∗")])
        _1111lll1ll_opy_[item.nodeid + bstack1l1ll_opy_ (u"࠭࠭ࡴࡧࡷࡹࡵ࠭∘")] = bstack1111ll111l_opy_
        bstack1llll1l11lll_opy_(item, bstack1111ll111l_opy_, bstack1l1ll_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ∙"))
    except Exception as err:
        print(bstack1l1ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࡟ࡳࡷࡱࡸࡪࡹࡴࡠࡵࡨࡸࡺࡶ࠺ࠡࡽࢀࠫ√"), str(err))
def pytest_runtest_teardown(item):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.TEST, bstack1lll1111lll_opy_.POST, item)
        cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.AFTER_EACH, bstack1lll1111lll_opy_.PRE, item, bstack1l1ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫ∛"))
        return # skip all existing bstack1llll11ll1ll_opy_
    try:
        global bstack1l11l1111_opy_
        bstack1ll1l1111l_opy_ = 0
        if bstack1llll1l1_opy_ is True:
            bstack1ll1l1111l_opy_ = int(os.environ.get(bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪ∜")))
        if bstack1lll1l11_opy_.bstack1111ll1ll_opy_() == bstack1l1ll_opy_ (u"ࠦࡹࡸࡵࡦࠤ∝"):
            if bstack1lll1l11_opy_.bstack11ll1ll1l_opy_() == bstack1l1ll_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢ∞"):
                bstack1llll11lll11_opy_ = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ∟"), None)
                bstack111l1l11_opy_ = bstack1llll11lll11_opy_ + bstack1l1ll_opy_ (u"ࠢ࠮ࡶࡨࡷࡹࡩࡡࡴࡧࠥ∠")
                driver = getattr(item, bstack1l1ll_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩ∡"), None)
                bstack1l111l11l1_opy_ = getattr(item, bstack1l1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ∢"), None)
                bstack11l11l11_opy_ = getattr(item, bstack1l1ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ∣"), None)
                PercySDK.screenshot(driver, bstack111l1l11_opy_, bstack1l111l11l1_opy_=bstack1l111l11l1_opy_, bstack11l11l11_opy_=bstack11l11l11_opy_, bstack1l1l11ll11_opy_=bstack1ll1l1111l_opy_)
        if not cli.bstack1lll1l1l111_opy_(bstack1lll1l1l1l1_opy_):
            if getattr(item, bstack1l1ll_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡷࡹࡧࡲࡵࡧࡧࠫ∤"), False):
                bstack1lll1111_opy_.bstack11111l111_opy_(getattr(item, bstack1l1ll_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭∥"), None), bstack1l11l1111_opy_, logger, item)
        if not bstack11ll1ll1_opy_.on():
            return
        bstack1111ll111l_opy_ = {
            bstack1l1ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ∦"): uuid4().__str__(),
            bstack1l1ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ∧"): bstack1111ll1l1l_opy_().isoformat() + bstack1l1ll_opy_ (u"ࠨ࡜ࠪ∨"),
            bstack1l1ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ∩"): bstack1l1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨ∪"),
            bstack1l1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧ∫"): bstack1l1ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩ∬"),
            bstack1l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩ∭"): bstack1l1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩ∮")
        }
        _1111lll1ll_opy_[item.nodeid + bstack1l1ll_opy_ (u"ࠨ࠯ࡷࡩࡦࡸࡤࡰࡹࡱࠫ∯")] = bstack1111ll111l_opy_
        bstack1llll1l11lll_opy_(item, bstack1111ll111l_opy_, bstack1l1ll_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ∰"))
    except Exception as err:
        print(bstack1l1ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡵࡹࡳࡺࡥࡴࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲ࠿ࠦࡻࡾࠩ∱"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if bstack11111l11l11_opy_(fixturedef.argname):
        store[bstack1l1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡯ࡴࡦ࡯ࠪ∲")] = request.node
    elif bstack11111l111ll_opy_(fixturedef.argname):
        store[bstack1l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡣ࡭ࡣࡶࡷࡤ࡯ࡴࡦ࡯ࠪ∳")] = request.node
    if not bstack11ll1ll1_opy_.on():
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.SETUP_FIXTURE, bstack1lll1111lll_opy_.PRE, fixturedef, request)
        outcome = yield
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.SETUP_FIXTURE, bstack1lll1111lll_opy_.POST, fixturedef, request, outcome)
        return # skip all existing bstack1llll11ll1ll_opy_
    start_time = datetime.datetime.now()
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.SETUP_FIXTURE, bstack1lll1111lll_opy_.PRE, fixturedef, request)
    outcome = yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.SETUP_FIXTURE, bstack1lll1111lll_opy_.POST, fixturedef, request, outcome)
        return # skip all existing bstack1llll11ll1ll_opy_
    try:
        fixture = {
            bstack1l1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ∴"): fixturedef.argname,
            bstack1l1ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ∵"): bstack11l11ll11l1_opy_(outcome),
            bstack1l1ll_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪ∶"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        current_test_item = store[bstack1l1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭∷")]
        if not _1111lll1ll_opy_.get(current_test_item.nodeid, None):
            _1111lll1ll_opy_[current_test_item.nodeid] = {bstack1l1ll_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬ∸"): []}
        _1111lll1ll_opy_[current_test_item.nodeid][bstack1l1ll_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭∹")].append(fixture)
    except Exception as err:
        logger.debug(bstack1l1ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡤࡹࡥࡵࡷࡳ࠾ࠥࢁࡽࠨ∺"), str(err))
if bstack1lll11l111_opy_() and bstack11ll1ll1_opy_.on():
    def pytest_bdd_before_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.STEP, bstack1lll1111lll_opy_.PRE, request, step)
            return
        try:
            _1111lll1ll_opy_[request.node.nodeid][bstack1l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩ∻")].bstack111l1ll1_opy_(id(step))
        except Exception as err:
            print(bstack1l1ll_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰ࠻ࠢࡾࢁࠬ∼"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.STEP, bstack1lll1111lll_opy_.POST, request, step, exception)
            return
        try:
            _1111lll1ll_opy_[request.node.nodeid][bstack1l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ∽")].bstack111ll1ll11_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack1l1ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤࡹࡴࡦࡲࡢࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂ࠭∾"), str(err))
    def pytest_bdd_after_step(request, step):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.STEP, bstack1lll1111lll_opy_.POST, request, step)
            return
        try:
            bstack111ll11l1l_opy_: bstack111ll1l1l1_opy_ = _1111lll1ll_opy_[request.node.nodeid][bstack1l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭∿")]
            bstack111ll11l1l_opy_.bstack111ll1ll11_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack1l1ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡴࡶࡨࡴࡤ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠨ≀"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack1llll1ll11ll_opy_
        try:
            if not bstack11ll1ll1_opy_.on() or bstack1llll1ll11ll_opy_ != bstack1l1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩ≁"):
                return
            if cli.is_running():
                cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.TEST, bstack1lll1111lll_opy_.PRE, request, feature, scenario)
                return
            driver = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ≂"), None)
            if not _1111lll1ll_opy_.get(request.node.nodeid, None):
                _1111lll1ll_opy_[request.node.nodeid] = {}
            bstack111ll11l1l_opy_ = bstack111ll1l1l1_opy_.bstack1lllllllllll_opy_(
                scenario, feature, request.node,
                name=bstack11111l11ll1_opy_(request.node, scenario),
                started_at=bstack1lllll1l11_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack1l1ll_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩ≃"),
                tags=bstack111111lllll_opy_(feature, scenario),
                bstack111lll1ll1_opy_=bstack11ll1ll1_opy_.bstack111lll1l1l_opy_(driver) if driver and driver.session_id else {}
            )
            _1111lll1ll_opy_[request.node.nodeid][bstack1l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ≄")] = bstack111ll11l1l_opy_
            bstack1llll1l11111_opy_(bstack111ll11l1l_opy_.uuid)
            bstack11ll1ll1_opy_.bstack111ll111ll_opy_(bstack1l1ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ≅"), bstack111ll11l1l_opy_)
        except Exception as err:
            print(bstack1l1ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬ≆"), str(err))
def bstack1llll1l1l11l_opy_(bstack111ll1llll_opy_):
    if bstack111ll1llll_opy_ in store[bstack1l1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨ≇")]:
        store[bstack1l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩ≈")].remove(bstack111ll1llll_opy_)
def bstack1llll1l11111_opy_(test_uuid):
    store[bstack1l1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠪ≉")] = test_uuid
    threading.current_thread().current_test_uuid = test_uuid
@bstack11ll1ll1_opy_.bstack1lllll1l1l1l_opy_
def bstack1llll11ll11l_opy_(item, call, report):
    logger.debug(bstack1l1ll_opy_ (u"ࠧࡩࡣࡱࡨࡱ࡫࡟ࡰ࠳࠴ࡽࡤࡺࡥࡴࡶࡢࡩࡻ࡫࡮ࡵ࠼ࠣࡷࡹࡧࡲࡵࠩ≊"))
    global bstack1llll1ll11ll_opy_
    bstack111ll1lll_opy_ = bstack1lllll1l11_opy_()
    if hasattr(report, bstack1l1ll_opy_ (u"ࠨࡵࡷࡳࡵ࠭≋")):
        bstack111ll1lll_opy_ = bstack11l11llll1l_opy_(report.stop)
    elif hasattr(report, bstack1l1ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࠨ≌")):
        bstack111ll1lll_opy_ = bstack11l11llll1l_opy_(report.start)
    try:
        if getattr(report, bstack1l1ll_opy_ (u"ࠪࡻ࡭࡫࡮ࠨ≍"), bstack1l1ll_opy_ (u"ࠫࠬ≎")) == bstack1l1ll_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ≏"):
            logger.debug(bstack1l1ll_opy_ (u"࠭ࡨࡢࡰࡧࡰࡪࡥ࡯࠲࠳ࡼࡣࡹ࡫ࡳࡵࡡࡨࡺࡪࡴࡴ࠻ࠢࡶࡸࡦࡺࡥࠡ࠯ࠣࡿࢂ࠲ࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠣ࠱ࠥࢁࡽࠨ≐").format(getattr(report, bstack1l1ll_opy_ (u"ࠧࡸࡪࡨࡲࠬ≑"), bstack1l1ll_opy_ (u"ࠨࠩ≒")).__str__(), bstack1llll1ll11ll_opy_))
            if bstack1llll1ll11ll_opy_ == bstack1l1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ≓"):
                _1111lll1ll_opy_[item.nodeid][bstack1l1ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ≔")] = bstack111ll1lll_opy_
                bstack1llll1l111ll_opy_(item, _1111lll1ll_opy_[item.nodeid], bstack1l1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭≕"), report, call)
                store[bstack1l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩ≖")] = None
            elif bstack1llll1ll11ll_opy_ == bstack1l1ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠥ≗"):
                bstack111ll11l1l_opy_ = _1111lll1ll_opy_[item.nodeid][bstack1l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ≘")]
                bstack111ll11l1l_opy_.set(hooks=_1111lll1ll_opy_[item.nodeid].get(bstack1l1ll_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ≙"), []))
                exception, bstack111ll1ll1l_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack111ll1ll1l_opy_ = [call.excinfo.exconly(), getattr(report, bstack1l1ll_opy_ (u"ࠩ࡯ࡳࡳ࡭ࡲࡦࡲࡵࡸࡪࡾࡴࠨ≚"), bstack1l1ll_opy_ (u"ࠪࠫ≛"))]
                bstack111ll11l1l_opy_.stop(time=bstack111ll1lll_opy_, result=Result(result=getattr(report, bstack1l1ll_opy_ (u"ࠫࡴࡻࡴࡤࡱࡰࡩࠬ≜"), bstack1l1ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ≝")), exception=exception, bstack111ll1ll1l_opy_=bstack111ll1ll1l_opy_))
                bstack11ll1ll1_opy_.bstack111ll111ll_opy_(bstack1l1ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ≞"), _1111lll1ll_opy_[item.nodeid][bstack1l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪ≟")])
        elif getattr(report, bstack1l1ll_opy_ (u"ࠨࡹ࡫ࡩࡳ࠭≠"), bstack1l1ll_opy_ (u"ࠩࠪ≡")) in [bstack1l1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ≢"), bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭≣")]:
            logger.debug(bstack1l1ll_opy_ (u"ࠬ࡮ࡡ࡯ࡦ࡯ࡩࡤࡵ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺ࠺ࠡࡵࡷࡥࡹ࡫ࠠ࠮ࠢࡾࢁ࠱ࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠢ࠰ࠤࢀࢃࠧ≤").format(getattr(report, bstack1l1ll_opy_ (u"࠭ࡷࡩࡧࡱࠫ≥"), bstack1l1ll_opy_ (u"ࠧࠨ≦")).__str__(), bstack1llll1ll11ll_opy_))
            bstack111lll111l_opy_ = item.nodeid + bstack1l1ll_opy_ (u"ࠨ࠯ࠪ≧") + getattr(report, bstack1l1ll_opy_ (u"ࠩࡺ࡬ࡪࡴࠧ≨"), bstack1l1ll_opy_ (u"ࠪࠫ≩"))
            if getattr(report, bstack1l1ll_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ≪"), False):
                hook_type = bstack1l1ll_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪ≫") if getattr(report, bstack1l1ll_opy_ (u"࠭ࡷࡩࡧࡱࠫ≬"), bstack1l1ll_opy_ (u"ࠧࠨ≭")) == bstack1l1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ≮") else bstack1l1ll_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭≯")
                _1111lll1ll_opy_[bstack111lll111l_opy_] = {
                    bstack1l1ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ≰"): uuid4().__str__(),
                    bstack1l1ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ≱"): bstack111ll1lll_opy_,
                    bstack1l1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ≲"): hook_type
                }
            _1111lll1ll_opy_[bstack111lll111l_opy_][bstack1l1ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ≳")] = bstack111ll1lll_opy_
            bstack1llll1l1l11l_opy_(_1111lll1ll_opy_[bstack111lll111l_opy_][bstack1l1ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ≴")])
            bstack1llll1l11lll_opy_(item, _1111lll1ll_opy_[bstack111lll111l_opy_], bstack1l1ll_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ≵"), report, call)
            if getattr(report, bstack1l1ll_opy_ (u"ࠩࡺ࡬ࡪࡴࠧ≶"), bstack1l1ll_opy_ (u"ࠪࠫ≷")) == bstack1l1ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ≸"):
                if getattr(report, bstack1l1ll_opy_ (u"ࠬࡵࡵࡵࡥࡲࡱࡪ࠭≹"), bstack1l1ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭≺")) == bstack1l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ≻"):
                    bstack1111ll111l_opy_ = {
                        bstack1l1ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭≼"): uuid4().__str__(),
                        bstack1l1ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭≽"): bstack1lllll1l11_opy_(),
                        bstack1l1ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ≾"): bstack1lllll1l11_opy_()
                    }
                    _1111lll1ll_opy_[item.nodeid] = {**_1111lll1ll_opy_[item.nodeid], **bstack1111ll111l_opy_}
                    bstack1llll1l111ll_opy_(item, _1111lll1ll_opy_[item.nodeid], bstack1l1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ≿"))
                    bstack1llll1l111ll_opy_(item, _1111lll1ll_opy_[item.nodeid], bstack1l1ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ⊀"), report, call)
    except Exception as err:
        print(bstack1l1ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡮ࡡ࡯ࡦ࡯ࡩࡤࡵ࠱࠲ࡻࡢࡸࡪࡹࡴࡠࡧࡹࡩࡳࡺ࠺ࠡࡽࢀࠫ⊁"), str(err))
def bstack1llll1l1lll1_opy_(test, bstack1111ll111l_opy_, result=None, call=None, bstack1llll11lll_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack111ll11l1l_opy_ = {
        bstack1l1ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⊂"): bstack1111ll111l_opy_[bstack1l1ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭⊃")],
        bstack1l1ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧ⊄"): bstack1l1ll_opy_ (u"ࠪࡸࡪࡹࡴࠨ⊅"),
        bstack1l1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ⊆"): test.name,
        bstack1l1ll_opy_ (u"ࠬࡨ࡯ࡥࡻࠪ⊇"): {
            bstack1l1ll_opy_ (u"࠭࡬ࡢࡰࡪࠫ⊈"): bstack1l1ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ⊉"),
            bstack1l1ll_opy_ (u"ࠨࡥࡲࡨࡪ࠭⊊"): inspect.getsource(test.obj)
        },
        bstack1l1ll_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭⊋"): test.name,
        bstack1l1ll_opy_ (u"ࠪࡷࡨࡵࡰࡦࠩ⊌"): test.name,
        bstack1l1ll_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫ⊍"): bstack11ll1llll1_opy_.bstack111l1lllll_opy_(test),
        bstack1l1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ⊎"): file_path,
        bstack1l1ll_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠨ⊏"): file_path,
        bstack1l1ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⊐"): bstack1l1ll_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ⊑"),
        bstack1l1ll_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧ⊒"): file_path,
        bstack1l1ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ⊓"): bstack1111ll111l_opy_[bstack1l1ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⊔")],
        bstack1l1ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ⊕"): bstack1l1ll_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭⊖"),
        bstack1l1ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪ⊗"): {
            bstack1l1ll_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬ⊘"): test.nodeid
        },
        bstack1l1ll_opy_ (u"ࠩࡷࡥ࡬ࡹࠧ⊙"): bstack11l1111llll_opy_(test.own_markers)
    }
    if bstack1llll11lll_opy_ in [bstack1l1ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡰ࡯ࡰࡱࡧࡧࠫ⊚"), bstack1l1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭⊛")]:
        bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"ࠬࡳࡥࡵࡣࠪ⊜")] = {
            bstack1l1ll_opy_ (u"࠭ࡦࡪࡺࡷࡹࡷ࡫ࡳࠨ⊝"): bstack1111ll111l_opy_.get(bstack1l1ll_opy_ (u"ࠧࡧ࡫ࡻࡸࡺࡸࡥࡴࠩ⊞"), [])
        }
    if bstack1llll11lll_opy_ == bstack1l1ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩ⊟"):
        bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⊠")] = bstack1l1ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ⊡")
        bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⊢")] = bstack1111ll111l_opy_[bstack1l1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ⊣")]
        bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⊤")] = bstack1111ll111l_opy_[bstack1l1ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⊥")]
    if result:
        bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ⊦")] = result.outcome
        bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪ⊧")] = result.duration * 1000
        bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⊨")] = bstack1111ll111l_opy_[bstack1l1ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⊩")]
        if result.failed:
            bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫ⊪")] = bstack11ll1ll1_opy_.bstack111111llll_opy_(call.excinfo.typename)
            bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧ⊫")] = bstack11ll1ll1_opy_.bstack1lllll1l11ll_opy_(call.excinfo, result)
        bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⊬")] = bstack1111ll111l_opy_[bstack1l1ll_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ⊭")]
    if outcome:
        bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⊮")] = bstack11l11ll11l1_opy_(outcome)
        bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫ⊯")] = 0
        bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⊰")] = bstack1111ll111l_opy_[bstack1l1ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ⊱")]
        if bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⊲")] == bstack1l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ⊳"):
            bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧ⊴")] = bstack1l1ll_opy_ (u"ࠩࡘࡲ࡭ࡧ࡮ࡥ࡮ࡨࡨࡊࡸࡲࡰࡴࠪ⊵")  # bstack1llll1l111l1_opy_
            bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫ⊶")] = [{bstack1l1ll_opy_ (u"ࠫࡧࡧࡣ࡬ࡶࡵࡥࡨ࡫ࠧ⊷"): [bstack1l1ll_opy_ (u"ࠬࡹ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠩ⊸")]}]
        bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬ⊹")] = bstack1111ll111l_opy_[bstack1l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭⊺")]
    return bstack111ll11l1l_opy_
def bstack1llll1l1l1l1_opy_(test, bstack111l1l11ll_opy_, bstack1llll11lll_opy_, result, call, outcome, bstack1llll11llll1_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack111l1l11ll_opy_[bstack1l1ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫ⊻")]
    hook_name = bstack111l1l11ll_opy_[bstack1l1ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬ⊼")]
    hook_data = {
        bstack1l1ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⊽"): bstack111l1l11ll_opy_[bstack1l1ll_opy_ (u"ࠫࡺࡻࡩࡥࠩ⊾")],
        bstack1l1ll_opy_ (u"ࠬࡺࡹࡱࡧࠪ⊿"): bstack1l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ⋀"),
        bstack1l1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ⋁"): bstack1l1ll_opy_ (u"ࠨࡽࢀࠫ⋂").format(bstack11111l1l1ll_opy_(hook_name)),
        bstack1l1ll_opy_ (u"ࠩࡥࡳࡩࡿࠧ⋃"): {
            bstack1l1ll_opy_ (u"ࠪࡰࡦࡴࡧࠨ⋄"): bstack1l1ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ⋅"),
            bstack1l1ll_opy_ (u"ࠬࡩ࡯ࡥࡧࠪ⋆"): None
        },
        bstack1l1ll_opy_ (u"࠭ࡳࡤࡱࡳࡩࠬ⋇"): test.name,
        bstack1l1ll_opy_ (u"ࠧࡴࡥࡲࡴࡪࡹࠧ⋈"): bstack11ll1llll1_opy_.bstack111l1lllll_opy_(test, hook_name),
        bstack1l1ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ⋉"): file_path,
        bstack1l1ll_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫ⋊"): file_path,
        bstack1l1ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⋋"): bstack1l1ll_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ⋌"),
        bstack1l1ll_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪ⋍"): file_path,
        bstack1l1ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ⋎"): bstack111l1l11ll_opy_[bstack1l1ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ⋏")],
        bstack1l1ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ⋐"): bstack1l1ll_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫ⋑") if bstack1llll1ll11ll_opy_ == bstack1l1ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠧ⋒") else bstack1l1ll_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷࠫ⋓"),
        bstack1l1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ⋔"): hook_type
    }
    bstack1ll11l11ll1_opy_ = bstack111l111lll_opy_(_1111lll1ll_opy_.get(test.nodeid, None))
    if bstack1ll11l11ll1_opy_:
        hook_data[bstack1l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠ࡫ࡧࠫ⋕")] = bstack1ll11l11ll1_opy_
    if result:
        hook_data[bstack1l1ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧ⋖")] = result.outcome
        hook_data[bstack1l1ll_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩ⋗")] = result.duration * 1000
        hook_data[bstack1l1ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⋘")] = bstack111l1l11ll_opy_[bstack1l1ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨ⋙")]
        if result.failed:
            hook_data[bstack1l1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪ⋚")] = bstack11ll1ll1_opy_.bstack111111llll_opy_(call.excinfo.typename)
            hook_data[bstack1l1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭⋛")] = bstack11ll1ll1_opy_.bstack1lllll1l11ll_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack1l1ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭⋜")] = bstack11l11ll11l1_opy_(outcome)
        hook_data[bstack1l1ll_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨ⋝")] = 100
        hook_data[bstack1l1ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⋞")] = bstack111l1l11ll_opy_[bstack1l1ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧ⋟")]
        if hook_data[bstack1l1ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⋠")] == bstack1l1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ⋡"):
            hook_data[bstack1l1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫ⋢")] = bstack1l1ll_opy_ (u"࠭ࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠧ⋣")  # bstack1llll1l111l1_opy_
            hook_data[bstack1l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨ⋤")] = [{bstack1l1ll_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫ⋥"): [bstack1l1ll_opy_ (u"ࠩࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷ࠭⋦")]}]
    if bstack1llll11llll1_opy_:
        hook_data[bstack1l1ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ⋧")] = bstack1llll11llll1_opy_.result
        hook_data[bstack1l1ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬ⋨")] = bstack11l1l111ll1_opy_(bstack111l1l11ll_opy_[bstack1l1ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ⋩")], bstack111l1l11ll_opy_[bstack1l1ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ⋪")])
        hook_data[bstack1l1ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ⋫")] = bstack111l1l11ll_opy_[bstack1l1ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭⋬")]
        if hook_data[bstack1l1ll_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ⋭")] == bstack1l1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ⋮"):
            hook_data[bstack1l1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪ⋯")] = bstack11ll1ll1_opy_.bstack111111llll_opy_(bstack1llll11llll1_opy_.exception_type)
            hook_data[bstack1l1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭⋰")] = [{bstack1l1ll_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩ⋱"): bstack11l111l1lll_opy_(bstack1llll11llll1_opy_.exception)}]
    return hook_data
def bstack1llll1l111ll_opy_(test, bstack1111ll111l_opy_, bstack1llll11lll_opy_, result=None, call=None, outcome=None):
    logger.debug(bstack1l1ll_opy_ (u"ࠧࡴࡧࡱࡨࡤࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡦࡸࡨࡲࡹࡀࠠࡂࡶࡷࡩࡲࡶࡴࡪࡰࡪࠤࡹࡵࠠࡨࡧࡱࡩࡷࡧࡴࡦࠢࡷࡩࡸࡺࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࠦ࠭ࠡࡽࢀࠫ⋲").format(bstack1llll11lll_opy_))
    bstack111ll11l1l_opy_ = bstack1llll1l1lll1_opy_(test, bstack1111ll111l_opy_, result, call, bstack1llll11lll_opy_, outcome)
    driver = getattr(test, bstack1l1ll_opy_ (u"ࠨࡡࡧࡶ࡮ࡼࡥࡳࠩ⋳"), None)
    if bstack1llll11lll_opy_ == bstack1l1ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪ⋴") and driver:
        bstack111ll11l1l_opy_[bstack1l1ll_opy_ (u"ࠪ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠩ⋵")] = bstack11ll1ll1_opy_.bstack111lll1l1l_opy_(driver)
    if bstack1llll11lll_opy_ == bstack1l1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡱࡩࡱࡲࡨࡨࠬ⋶"):
        bstack1llll11lll_opy_ = bstack1l1ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ⋷")
    bstack1111lllll1_opy_ = {
        bstack1l1ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪ⋸"): bstack1llll11lll_opy_,
        bstack1l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࠩ⋹"): bstack111ll11l1l_opy_
    }
    bstack11ll1ll1_opy_.bstack1ll111l1l1_opy_(bstack1111lllll1_opy_)
    if bstack1llll11lll_opy_ == bstack1l1ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ⋺"):
        threading.current_thread().bstackTestMeta = {bstack1l1ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ⋻"): bstack1l1ll_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫ⋼")}
    elif bstack1llll11lll_opy_ == bstack1l1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭⋽"):
        threading.current_thread().bstackTestMeta = {bstack1l1ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⋾"): getattr(result, bstack1l1ll_opy_ (u"࠭࡯ࡶࡶࡦࡳࡲ࡫ࠧ⋿"), bstack1l1ll_opy_ (u"ࠧࠨ⌀"))}
def bstack1llll1l11lll_opy_(test, bstack1111ll111l_opy_, bstack1llll11lll_opy_, result=None, call=None, outcome=None, bstack1llll11llll1_opy_=None):
    logger.debug(bstack1l1ll_opy_ (u"ࠨࡵࡨࡲࡩࡥࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡧࡹࡩࡳࡺ࠺ࠡࡃࡷࡸࡪࡳࡰࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡩࡨࡲࡪࡸࡡࡵࡧࠣ࡬ࡴࡵ࡫ࠡࡦࡤࡸࡦ࠲ࠠࡦࡸࡨࡲࡹ࡚ࡹࡱࡧࠣ࠱ࠥࢁࡽࠨ⌁").format(bstack1llll11lll_opy_))
    hook_data = bstack1llll1l1l1l1_opy_(test, bstack1111ll111l_opy_, bstack1llll11lll_opy_, result, call, outcome, bstack1llll11llll1_opy_)
    bstack1111lllll1_opy_ = {
        bstack1l1ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭⌂"): bstack1llll11lll_opy_,
        bstack1l1ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࠬ⌃"): hook_data
    }
    bstack11ll1ll1_opy_.bstack1ll111l1l1_opy_(bstack1111lllll1_opy_)
def bstack111l111lll_opy_(bstack1111ll111l_opy_):
    if not bstack1111ll111l_opy_:
        return None
    if bstack1111ll111l_opy_.get(bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧ⌄"), None):
        return getattr(bstack1111ll111l_opy_[bstack1l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨ⌅")], bstack1l1ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⌆"), None)
    return bstack1111ll111l_opy_.get(bstack1l1ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ⌇"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.LOG, bstack1lll1111lll_opy_.PRE, request, caplog)
    yield
    if cli.is_running():
        cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_.LOG, bstack1lll1111lll_opy_.POST, request, caplog)
        return # skip all existing bstack1llll11ll1ll_opy_
    try:
        if not bstack11ll1ll1_opy_.on():
            return
        places = [bstack1l1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ⌈"), bstack1l1ll_opy_ (u"ࠩࡦࡥࡱࡲࠧ⌉"), bstack1l1ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬ⌊")]
        logs = []
        for bstack1llll11ll1l1_opy_ in places:
            records = caplog.get_records(bstack1llll11ll1l1_opy_)
            bstack1llll1ll1l1l_opy_ = bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ⌋") if bstack1llll11ll1l1_opy_ == bstack1l1ll_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ⌌") else bstack1l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭⌍")
            bstack1llll1l11l1l_opy_ = request.node.nodeid + (bstack1l1ll_opy_ (u"ࠧࠨ⌎") if bstack1llll11ll1l1_opy_ == bstack1l1ll_opy_ (u"ࠨࡥࡤࡰࡱ࠭⌏") else bstack1l1ll_opy_ (u"ࠩ࠰ࠫ⌐") + bstack1llll11ll1l1_opy_)
            test_uuid = bstack111l111lll_opy_(_1111lll1ll_opy_.get(bstack1llll1l11l1l_opy_, None))
            if not test_uuid:
                continue
            for record in records:
                if bstack111lll1l111_opy_(record.message):
                    continue
                logs.append({
                    bstack1l1ll_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭⌑"): bstack11l1111ll11_opy_(record.created).isoformat() + bstack1l1ll_opy_ (u"ࠫ࡟࠭⌒"),
                    bstack1l1ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ⌓"): record.levelname,
                    bstack1l1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⌔"): record.message,
                    bstack1llll1ll1l1l_opy_: test_uuid
                })
        if len(logs) > 0:
            bstack11ll1ll1_opy_.bstack11l1l1lll1_opy_(logs)
    except Exception as err:
        print(bstack1l1ll_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡥࡲࡲࡩࡥࡦࡪࡺࡷࡹࡷ࡫࠺ࠡࡽࢀࠫ⌕"), str(err))
def bstack11111ll11_opy_(sequence, driver_command, response=None, driver = None, args = None):
    global bstack1lll111l1l_opy_
    bstack11l1l11l1l_opy_ = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ⌖"), None) and bstack11ll1ll11_opy_(
            threading.current_thread(), bstack1l1ll_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ⌗"), None)
    bstack11l11ll1ll_opy_ = getattr(driver, bstack1l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪ⌘"), None) != None and getattr(driver, bstack1l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫ⌙"), None) == True
    if sequence == bstack1l1ll_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬ⌚") and driver != None:
      if not bstack1lll111l1l_opy_ and bstack1l1ll1111ll_opy_() and bstack1l1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⌛") in CONFIG and CONFIG[bstack1l1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⌜")] == True and bstack11111lll_opy_.bstack11ll1l1lll_opy_(driver_command) and (bstack11l11ll1ll_opy_ or bstack11l1l11l1l_opy_) and not bstack1lll1111l1_opy_(args):
        try:
          bstack1lll111l1l_opy_ = True
          logger.debug(bstack1l1ll_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡼࡿࠪ⌝").format(driver_command))
          logger.debug(perform_scan(driver, driver_command=driver_command))
        except Exception as err:
          logger.debug(bstack1l1ll_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡥࡳࡨࡲࡶࡲࠦࡳࡤࡣࡱࠤࢀࢃࠧ⌞").format(str(err)))
        bstack1lll111l1l_opy_ = False
    if sequence == bstack1l1ll_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩ⌟"):
        if driver_command == bstack1l1ll_opy_ (u"ࠫࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨ⌠"):
            bstack11ll1ll1_opy_.bstack1l11ll1ll1_opy_({
                bstack1l1ll_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫ⌡"): response[bstack1l1ll_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬ⌢")],
                bstack1l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ⌣"): store[bstack1l1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬ⌤")]
            })
def bstack11lllll1l1_opy_():
    global bstack1lllllll1_opy_
    bstack1l1111111_opy_.bstack1ll1l11ll1_opy_()
    logging.shutdown()
    bstack11ll1ll1_opy_.bstack111l1l1111_opy_()
    for driver in bstack1lllllll1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1llll1l1111l_opy_(*args):
    global bstack1lllllll1_opy_
    bstack11ll1ll1_opy_.bstack111l1l1111_opy_()
    for driver in bstack1lllllll1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1l1l1l11ll_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1ll1lll1l_opy_(self, *args, **kwargs):
    bstack1l11l1ll1_opy_ = bstack1l11lll1l_opy_(self, *args, **kwargs)
    bstack1ll1ll1lll_opy_ = getattr(threading.current_thread(), bstack1l1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡖࡨࡷࡹࡓࡥࡵࡣࠪ⌥"), None)
    if bstack1ll1ll1lll_opy_ and bstack1ll1ll1lll_opy_.get(bstack1l1ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ⌦"), bstack1l1ll_opy_ (u"ࠫࠬ⌧")) == bstack1l1ll_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭⌨"):
        bstack11ll1ll1_opy_.bstack1l1111l111_opy_(self)
    return bstack1l11l1ll1_opy_
@measure(event_name=EVENTS.bstack1lll1lllll_opy_, stage=STAGE.bstack1l1llllll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack11llllll_opy_(framework_name):
    from bstack_utils.config import Config
    bstack11l1lll1_opy_ = Config.bstack11ll11ll1_opy_()
    if bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪ〈")):
        return
    bstack11l1lll1_opy_.bstack1111lllll_opy_(bstack1l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫ〉"), True)
    global bstack111llll11_opy_
    global bstack1lll1l1111_opy_
    bstack111llll11_opy_ = framework_name
    logger.info(bstack1ll1l1ll1_opy_.format(bstack111llll11_opy_.split(bstack1l1ll_opy_ (u"ࠨ࠯ࠪ⌫"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1l1ll1111ll_opy_():
            Service.start = bstack1lll11l1_opy_
            Service.stop = bstack1l1l1lll11_opy_
            webdriver.Remote.get = bstack1l11ll11ll_opy_
            webdriver.Remote.__init__ = bstack1l1l111lll_opy_
            if not isinstance(os.getenv(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡄࡖࡆࡒࡌࡆࡎࠪ⌬")), str):
                return
            WebDriver.quit = bstack1lll1llll_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.get_accessibility_results = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
            WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
            WebDriver.performScan = perform_scan
            WebDriver.perform_scan = perform_scan
        elif bstack11ll1ll1_opy_.on():
            webdriver.Remote.__init__ = bstack1ll1lll1l_opy_
        bstack1lll1l1111_opy_ = True
    except Exception as e:
        pass
    if os.environ.get(bstack1l1ll_opy_ (u"ࠪࡗࡊࡒࡅࡏࡋࡘࡑࡤࡕࡒࡠࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡏࡎࡔࡖࡄࡐࡑࡋࡄࠨ⌭")):
        bstack1lll1l1111_opy_ = eval(os.environ.get(bstack1l1ll_opy_ (u"ࠫࡘࡋࡌࡆࡐࡌ࡙ࡒࡥࡏࡓࡡࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡉࡏࡕࡗࡅࡑࡒࡅࡅࠩ⌮")))
    if not bstack1lll1l1111_opy_:
        bstack1111l1l11_opy_(bstack1l1ll_opy_ (u"ࠧࡖࡡࡤ࡭ࡤ࡫ࡪࡹࠠ࡯ࡱࡷࠤ࡮ࡴࡳࡵࡣ࡯ࡰࡪࡪࠢ⌯"), bstack11l111lll1_opy_)
    if bstack111l1l1ll_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            if hasattr(RemoteConnection, bstack1l1ll_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧ⌰")) and callable(getattr(RemoteConnection, bstack1l1ll_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ⌱"))):
                RemoteConnection._get_proxy_url = bstack111ll11l1_opy_
            else:
                from selenium.webdriver.remote.client_config import ClientConfig
                ClientConfig.get_proxy_url = bstack111ll11l1_opy_
        except Exception as e:
            logger.error(bstack11l1l1l1l_opy_.format(str(e)))
    if bstack1l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ⌲") in str(framework_name).lower():
        if not bstack1l1ll1111ll_opy_():
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
@measure(event_name=EVENTS.bstack11111ll1_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1lll1llll_opy_(self):
    global bstack111llll11_opy_
    global bstack1lllll11ll_opy_
    global bstack1l1l11lll_opy_
    try:
        if bstack1l1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ⌳") in bstack111llll11_opy_ and self.session_id != None and bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡔࡶࡤࡸࡺࡹࠧ⌴"), bstack1l1ll_opy_ (u"ࠫࠬ⌵")) != bstack1l1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭⌶"):
            bstack111l1l11l_opy_ = bstack1l1ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭⌷") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1l1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ⌸")
            bstack1lll1l11ll_opy_(logger, True)
            if os.environ.get(bstack1l1ll_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔࡠࡖࡈࡗ࡙ࡥࡎࡂࡏࡈࠫ⌹"), None):
                self.execute_script(
                    bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧ⌺") + json.dumps(
                        os.environ.get(bstack1l1ll_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖࡢࡘࡊ࡙ࡔࡠࡐࡄࡑࡊ࠭⌻"))) + bstack1l1ll_opy_ (u"ࠫࢂࢃࠧ⌼"))
            if self != None:
                bstack1l1l111l1_opy_(self, bstack111l1l11l_opy_, bstack1l1ll_opy_ (u"ࠬ࠲ࠠࠨ⌽").join(threading.current_thread().bstackTestErrorMessages))
        if not cli.bstack1lll1l1l111_opy_(bstack1lll1l1l1l1_opy_):
            item = store.get(bstack1l1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡯ࡴࡦ࡯ࠪ⌾"), None)
            if item is not None and bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭⌿"), None):
                bstack1lll1111_opy_.bstack11111l111_opy_(self, bstack1l11l1111_opy_, logger, item)
        threading.current_thread().testStatus = bstack1l1ll_opy_ (u"ࠨࠩ⍀")
    except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠ࡮ࡣࡵ࡯࡮ࡴࡧࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࠥ⍁") + str(e))
    bstack1l1l11lll_opy_(self)
    self.session_id = None
@measure(event_name=EVENTS.bstack11l1ll1lll_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1l1l111lll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack1lllll11ll_opy_
    global bstack1l1l1ll1l_opy_
    global bstack1llll1l1_opy_
    global bstack111llll11_opy_
    global bstack1l11lll1l_opy_
    global bstack1lllllll1_opy_
    global bstack1lll11lll_opy_
    global bstack111ll1l1_opy_
    global bstack1l11l1111_opy_
    CONFIG[bstack1l1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ⍂")] = str(bstack111llll11_opy_) + str(__version__)
    command_executor = bstack11ll1l1l1l_opy_(bstack1lll11lll_opy_, CONFIG)
    logger.debug(bstack1111111l_opy_.format(command_executor))
    proxy = bstack11l1l11l_opy_(CONFIG, proxy)
    bstack1ll1l1111l_opy_ = 0
    try:
        if bstack1llll1l1_opy_ is True:
            bstack1ll1l1111l_opy_ = int(os.environ.get(bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ⍃")))
    except:
        bstack1ll1l1111l_opy_ = 0
    bstack1l1lll1l11_opy_ = bstack1l1l1l11_opy_(CONFIG, bstack1ll1l1111l_opy_)
    logger.debug(bstack1l11l11l1l_opy_.format(str(bstack1l1lll1l11_opy_)))
    bstack1l11l1111_opy_ = CONFIG.get(bstack1l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ⍄"))[bstack1ll1l1111l_opy_]
    if bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ⍅") in CONFIG and CONFIG[bstack1l1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ⍆")]:
        bstack1l1l11lll1_opy_(bstack1l1lll1l11_opy_, bstack111ll1l1_opy_)
    if bstack111111l1l_opy_.bstack1l1ll11l11_opy_(CONFIG, bstack1ll1l1111l_opy_) and bstack111111l1l_opy_.bstack1ll1llllll_opy_(bstack1l1lll1l11_opy_, options, desired_capabilities):
        threading.current_thread().a11yPlatform = True
        if not cli.bstack1lll1l1l111_opy_(bstack1lll1l1l1l1_opy_):
            bstack111111l1l_opy_.set_capabilities(bstack1l1lll1l11_opy_, CONFIG)
    if desired_capabilities:
        bstack11ll1lll1_opy_ = bstack11ll111l1_opy_(desired_capabilities)
        bstack11ll1lll1_opy_[bstack1l1ll_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨ⍇")] = bstack1l111l1l1_opy_(CONFIG)
        bstack1ll11l1ll_opy_ = bstack1l1l1l11_opy_(bstack11ll1lll1_opy_)
        if bstack1ll11l1ll_opy_:
            bstack1l1lll1l11_opy_ = update(bstack1ll11l1ll_opy_, bstack1l1lll1l11_opy_)
        desired_capabilities = None
    if options:
        bstack1l11lll1l1_opy_(options, bstack1l1lll1l11_opy_)
    if not options:
        options = bstack1ll1lll111_opy_(bstack1l1lll1l11_opy_)
    if proxy and bstack1l1l1l111l_opy_() >= version.parse(bstack1l1ll_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩ⍈")):
        options.proxy(proxy)
    if options and bstack1l1l1l111l_opy_() >= version.parse(bstack1l1ll_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ⍉")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1l1l1l111l_opy_() < version.parse(bstack1l1ll_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ⍊")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1l1lll1l11_opy_)
    logger.info(bstack1l1ll111_opy_)
    bstack11l1l111l_opy_.end(EVENTS.bstack1lll1lllll_opy_.value, EVENTS.bstack1lll1lllll_opy_.value + bstack1l1ll_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ⍋"),
                               EVENTS.bstack1lll1lllll_opy_.value + bstack1l1ll_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ⍌"), True, None)
    if bstack1l1l1l111l_opy_() >= version.parse(bstack1l1ll_opy_ (u"ࠧ࠵࠰࠴࠴࠳࠶ࠧ⍍")):
        bstack1l11lll1l_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l1l1l111l_opy_() >= version.parse(bstack1l1ll_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ⍎")):
        bstack1l11lll1l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l1l1l111l_opy_() >= version.parse(bstack1l1ll_opy_ (u"ࠩ࠵࠲࠺࠹࠮࠱ࠩ⍏")):
        bstack1l11lll1l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack1l11lll1l_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack1ll1111l_opy_ = bstack1l1ll_opy_ (u"ࠪࠫ⍐")
        if bstack1l1l1l111l_opy_() >= version.parse(bstack1l1ll_opy_ (u"ࠫ࠹࠴࠰࠯࠲ࡥ࠵ࠬ⍑")):
            bstack1ll1111l_opy_ = self.caps.get(bstack1l1ll_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧ⍒"))
        else:
            bstack1ll1111l_opy_ = self.capabilities.get(bstack1l1ll_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨ⍓"))
        if bstack1ll1111l_opy_:
            bstack1l1l111111_opy_(bstack1ll1111l_opy_)
            if bstack1l1l1l111l_opy_() <= version.parse(bstack1l1ll_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧ⍔")):
                self.command_executor._url = bstack1l1ll_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤ⍕") + bstack1lll11lll_opy_ + bstack1l1ll_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨ⍖")
            else:
                self.command_executor._url = bstack1l1ll_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧ⍗") + bstack1ll1111l_opy_ + bstack1l1ll_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧ⍘")
            logger.debug(bstack11ll11ll11_opy_.format(bstack1ll1111l_opy_))
        else:
            logger.debug(bstack1l1l1l1111_opy_.format(bstack1l1ll_opy_ (u"ࠧࡕࡰࡵ࡫ࡰࡥࡱࠦࡈࡶࡤࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩࠨ⍙")))
    except Exception as e:
        logger.debug(bstack1l1l1l1111_opy_.format(e))
    bstack1lllll11ll_opy_ = self.session_id
    if bstack1l1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭⍚") in bstack111llll11_opy_:
        threading.current_thread().bstackSessionId = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        item = store.get(bstack1l1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡩࡵࡧࡰࠫ⍛"), None)
        if item:
            bstack1llll1l11ll1_opy_ = getattr(item, bstack1l1ll_opy_ (u"ࠨࡡࡷࡩࡸࡺ࡟ࡤࡣࡶࡩࡤࡹࡴࡢࡴࡷࡩࡩ࠭⍜"), False)
            if not getattr(item, bstack1l1ll_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪ⍝"), None) and bstack1llll1l11ll1_opy_:
                setattr(store[bstack1l1ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧ⍞")], bstack1l1ll_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬ⍟"), self)
        bstack1ll1ll1lll_opy_ = getattr(threading.current_thread(), bstack1l1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࡙࡫ࡳࡵࡏࡨࡸࡦ࠭⍠"), None)
        if bstack1ll1ll1lll_opy_ and bstack1ll1ll1lll_opy_.get(bstack1l1ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭⍡"), bstack1l1ll_opy_ (u"ࠧࠨ⍢")) == bstack1l1ll_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ⍣"):
            bstack11ll1ll1_opy_.bstack1l1111l111_opy_(self)
    bstack1lllllll1_opy_.append(self)
    if bstack1l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ⍤") in CONFIG and bstack1l1ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ⍥") in CONFIG[bstack1l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ⍦")][bstack1ll1l1111l_opy_]:
        bstack1l1l1ll1l_opy_ = CONFIG[bstack1l1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ⍧")][bstack1ll1l1111l_opy_][bstack1l1ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ⍨")]
    logger.debug(bstack1l1l1ll1ll_opy_.format(bstack1lllll11ll_opy_))
@measure(event_name=EVENTS.bstack1l1l1111l_opy_, stage=STAGE.bstack11ll1l11ll_opy_, bstack1l1ll11l1l_opy_=bstack1l1l1ll1l_opy_)
def bstack1l11ll11ll_opy_(self, url):
    global bstack1l11lll1ll_opy_
    global CONFIG
    try:
        bstack11lll11l_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1ll1l1l11l_opy_.format(str(err)))
    try:
        bstack1l11lll1ll_opy_(self, url)
    except Exception as e:
        try:
            bstack111ll1ll1_opy_ = str(e)
            if any(err_msg in bstack111ll1ll1_opy_ for err_msg in bstack11lll11l1l_opy_):
                bstack11lll11l_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1ll1l1l11l_opy_.format(str(err)))
        raise e
def bstack111lllll1_opy_(item, when):
    global bstack11ll1111l_opy_
    try:
        bstack11ll1111l_opy_(item, when)
    except Exception as e:
        pass
def bstack111111111_opy_(item, call, rep):
    global bstack11ll1lll_opy_
    global bstack1lllllll1_opy_
    name = bstack1l1ll_opy_ (u"ࠧࠨ⍩")
    try:
        if rep.when == bstack1l1ll_opy_ (u"ࠨࡥࡤࡰࡱ࠭⍪"):
            bstack1lllll11ll_opy_ = threading.current_thread().bstackSessionId
            skipSessionName = item.config.getoption(bstack1l1ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ⍫"))
            try:
                if (str(skipSessionName).lower() != bstack1l1ll_opy_ (u"ࠪࡸࡷࡻࡥࠨ⍬")):
                    name = str(rep.nodeid)
                    bstack1l11111ll_opy_ = bstack1l1ll11lll_opy_(bstack1l1ll_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ⍭"), name, bstack1l1ll_opy_ (u"ࠬ࠭⍮"), bstack1l1ll_opy_ (u"࠭ࠧ⍯"), bstack1l1ll_opy_ (u"ࠧࠨ⍰"), bstack1l1ll_opy_ (u"ࠨࠩ⍱"))
                    os.environ[bstack1l1ll_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕࡡࡗࡉࡘ࡚࡟ࡏࡃࡐࡉࠬ⍲")] = name
                    for driver in bstack1lllllll1_opy_:
                        if bstack1lllll11ll_opy_ == driver.session_id:
                            driver.execute_script(bstack1l11111ll_opy_)
            except Exception as e:
                logger.debug(bstack1l1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪ⍳").format(str(e)))
            try:
                bstack1l111l1111_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack1l1ll_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ⍴"):
                    status = bstack1l1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ⍵") if rep.outcome.lower() == bstack1l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭⍶") else bstack1l1ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ⍷")
                    reason = bstack1l1ll_opy_ (u"ࠨࠩ⍸")
                    if status == bstack1l1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ⍹"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack1l1ll_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨ⍺") if status == bstack1l1ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ⍻") else bstack1l1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ⍼")
                    data = name + bstack1l1ll_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨ⍽") if status == bstack1l1ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ⍾") else name + bstack1l1ll_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥࠣࠣࠫ⍿") + reason
                    bstack1l1l11l11l_opy_ = bstack1l1ll11lll_opy_(bstack1l1ll_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫ⎀"), bstack1l1ll_opy_ (u"ࠪࠫ⎁"), bstack1l1ll_opy_ (u"ࠫࠬ⎂"), bstack1l1ll_opy_ (u"ࠬ࠭⎃"), level, data)
                    for driver in bstack1lllllll1_opy_:
                        if bstack1lllll11ll_opy_ == driver.session_id:
                            driver.execute_script(bstack1l1l11l11l_opy_)
            except Exception as e:
                logger.debug(bstack1l1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡴࡴࡴࡦࡺࡷࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪ⎄").format(str(e)))
    except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡷࡹࡧࡴࡦࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࡽࢀࠫ⎅").format(str(e)))
    bstack11ll1lll_opy_(item, call, rep)
notset = Notset()
def bstack1l11l1l1ll_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack1l1111l1ll_opy_
    if str(name).lower() == bstack1l1ll_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࠨ⎆"):
        return bstack1l1ll_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣ⎇")
    else:
        return bstack1l1111l1ll_opy_(self, name, default, skip)
def bstack111ll11l1_opy_(self):
    global CONFIG
    global bstack1ll111ll1_opy_
    try:
        proxy = bstack11llll1l11_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack1l1ll_opy_ (u"ࠪ࠲ࡵࡧࡣࠨ⎈")):
                proxies = bstack11l1111l11_opy_(proxy, bstack11ll1l1l1l_opy_())
                if len(proxies) > 0:
                    protocol, bstack1l1ll1l111_opy_ = proxies.popitem()
                    if bstack1l1ll_opy_ (u"ࠦ࠿࠵࠯ࠣ⎉") in bstack1l1ll1l111_opy_:
                        return bstack1l1ll1l111_opy_
                    else:
                        return bstack1l1ll_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨ⎊") + bstack1l1ll1l111_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack1l1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡳࡶࡴࡾࡹࠡࡷࡵࡰࠥࡀࠠࡼࡿࠥ⎋").format(str(e)))
    return bstack1ll111ll1_opy_(self)
def bstack111l1l1ll_opy_():
    return (bstack1l1ll_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪ⎌") in CONFIG or bstack1l1ll_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ⎍") in CONFIG) and bstack11111111_opy_() and bstack1l1l1l111l_opy_() >= version.parse(
        bstack1llllll1ll_opy_)
def bstack1ll1l1lll_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1l1l1ll1l_opy_
    global bstack1llll1l1_opy_
    global bstack111llll11_opy_
    CONFIG[bstack1l1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ⎎")] = str(bstack111llll11_opy_) + str(__version__)
    bstack1ll1l1111l_opy_ = 0
    try:
        if bstack1llll1l1_opy_ is True:
            bstack1ll1l1111l_opy_ = int(os.environ.get(bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪ⎏")))
    except:
        bstack1ll1l1111l_opy_ = 0
    CONFIG[bstack1l1ll_opy_ (u"ࠦ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ⎐")] = True
    bstack1l1lll1l11_opy_ = bstack1l1l1l11_opy_(CONFIG, bstack1ll1l1111l_opy_)
    logger.debug(bstack1l11l11l1l_opy_.format(str(bstack1l1lll1l11_opy_)))
    if CONFIG.get(bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ⎑")):
        bstack1l1l11lll1_opy_(bstack1l1lll1l11_opy_, bstack111ll1l1_opy_)
    if bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⎒") in CONFIG and bstack1l1ll_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ⎓") in CONFIG[bstack1l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ⎔")][bstack1ll1l1111l_opy_]:
        bstack1l1l1ll1l_opy_ = CONFIG[bstack1l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ⎕")][bstack1ll1l1111l_opy_][bstack1l1ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ⎖")]
    import urllib
    import json
    if bstack1l1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ⎗") in CONFIG and str(CONFIG[bstack1l1ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ⎘")]).lower() != bstack1l1ll_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ⎙"):
        bstack11lllllll1_opy_ = bstack1ll11lll_opy_()
        bstack1l1ll111ll_opy_ = bstack11lllllll1_opy_ + urllib.parse.quote(json.dumps(bstack1l1lll1l11_opy_))
    else:
        bstack1l1ll111ll_opy_ = bstack1l1ll_opy_ (u"ࠧࡸࡵࡶ࠾࠴࠵ࡣࡥࡲ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡂࡧࡦࡶࡳ࠾ࠩ⎚") + urllib.parse.quote(json.dumps(bstack1l1lll1l11_opy_))
    browser = self.connect(bstack1l1ll111ll_opy_)
    return browser
def bstack1l111lll11_opy_():
    global bstack1lll1l1111_opy_
    global bstack111llll11_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1111l1l1l_opy_
        if not bstack1l1ll1111ll_opy_():
            global bstack1l11ll11l_opy_
            if not bstack1l11ll11l_opy_:
                from bstack_utils.helper import bstack1lllll1l1l_opy_, bstack1ll1111ll_opy_
                bstack1l11ll11l_opy_ = bstack1lllll1l1l_opy_()
                bstack1ll1111ll_opy_(bstack111llll11_opy_)
            BrowserType.connect = bstack1111l1l1l_opy_
            return
        BrowserType.launch = bstack1ll1l1lll_opy_
        bstack1lll1l1111_opy_ = True
    except Exception as e:
        pass
def bstack1llll1ll1l11_opy_():
    global CONFIG
    global bstack1llll1l1l1_opy_
    global bstack1lll11lll_opy_
    global bstack111ll1l1_opy_
    global bstack1llll1l1_opy_
    global bstack11l1llll11_opy_
    CONFIG = json.loads(os.environ.get(bstack1l1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠧ⎛")))
    bstack1llll1l1l1_opy_ = eval(os.environ.get(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ⎜")))
    bstack1lll11lll_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡋ࡙ࡇࡥࡕࡓࡎࠪ⎝"))
    bstack1l1llll1_opy_(CONFIG, bstack1llll1l1l1_opy_)
    bstack11l1llll11_opy_ = bstack1l1111111_opy_.bstack1lll1l1ll_opy_(CONFIG, bstack11l1llll11_opy_)
    if cli.bstack11l111111_opy_():
        bstack11ll1lll1l_opy_.invoke(bstack111l1lll_opy_.CONNECT, bstack1l11111l1_opy_())
        cli_context.platform_index = int(os.environ.get(bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ⎞"), bstack1l1ll_opy_ (u"ࠬ࠶ࠧ⎟")))
        cli.bstack1lll111l1l1_opy_(cli_context.platform_index)
        cli.bstack1lll1l1l1ll_opy_(bstack11ll1l1l1l_opy_(bstack1lll11lll_opy_, CONFIG), cli_context.platform_index, bstack1ll1lll111_opy_)
        cli.bstack1ll1ll1llll_opy_()
        logger.debug(bstack1l1ll_opy_ (u"ࠨࡃࡍࡋࠣ࡭ࡸࠦࡡࡤࡶ࡬ࡺࡪࠦࡦࡰࡴࠣࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࡁࠧ⎠") + str(cli_context.platform_index) + bstack1l1ll_opy_ (u"ࠢࠣ⎡"))
        return # skip all existing bstack1llll11ll1ll_opy_
    global bstack1l11lll1l_opy_
    global bstack1l1l11lll_opy_
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
    except Exception as e:
        pass
    if (bstack1l1ll_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫ⎢") in CONFIG or bstack1l1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭⎣") in CONFIG) and bstack11111111_opy_():
        if bstack1l1l1l111l_opy_() < version.parse(bstack1llllll1ll_opy_):
            logger.error(bstack1llll111ll_opy_.format(bstack1l1l1l111l_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                if hasattr(RemoteConnection, bstack1l1ll_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫ⎤")) and callable(getattr(RemoteConnection, bstack1l1ll_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ⎥"))):
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
        logger.debug(bstack1l1ll_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡴࠦࡲࡶࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࡸ࠭⎦"))
    bstack111ll1l1_opy_ = CONFIG.get(bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ⎧"), {}).get(bstack1l1ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ⎨"))
    bstack1llll1l1_opy_ = True
    bstack11llllll_opy_(bstack11ll1111ll_opy_)
if (bstack11l1111111l_opy_()):
    bstack1llll1ll1l11_opy_()
@bstack111l111ll1_opy_(class_method=False)
def bstack1llll11lllll_opy_(hook_name, event, bstack1l11111l1l1_opy_=None):
    if hook_name not in [bstack1l1ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩ⎩"), bstack1l1ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭⎪"), bstack1l1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩ⎫"), bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪ࠭⎬"), bstack1l1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠪ⎭"), bstack1l1ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠧ⎮"), bstack1l1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭⎯"), bstack1l1ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪ⎰")]:
        return
    node = store[bstack1l1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭⎱")]
    if hook_name in [bstack1l1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩ⎲"), bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪ࠭⎳")]:
        node = store[bstack1l1ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥ࡭ࡰࡦࡸࡰࡪࡥࡩࡵࡧࡰࠫ⎴")]
    elif hook_name in [bstack1l1ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠫ⎵"), bstack1l1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨ⎶")]:
        node = store[bstack1l1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡦࡰࡦࡹࡳࡠ࡫ࡷࡩࡲ࠭⎷")]
    hook_type = bstack11111l1l111_opy_(hook_name)
    if event == bstack1l1ll_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩ⎸"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_[hook_type], bstack1lll1111lll_opy_.PRE, node, hook_name)
            return
        uuid = uuid4().__str__()
        bstack111l1l11ll_opy_ = {
            bstack1l1ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ⎹"): uuid,
            bstack1l1ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨ⎺"): bstack1lllll1l11_opy_(),
            bstack1l1ll_opy_ (u"ࠬࡺࡹࡱࡧࠪ⎻"): bstack1l1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ⎼"),
            bstack1l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪ⎽"): hook_type,
            bstack1l1ll_opy_ (u"ࠨࡪࡲࡳࡰࡥ࡮ࡢ࡯ࡨࠫ⎾"): hook_name
        }
        store[bstack1l1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭⎿")].append(uuid)
        bstack1llll1ll111l_opy_ = node.nodeid
        if hook_type == bstack1l1ll_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨ⏀"):
            if not _1111lll1ll_opy_.get(bstack1llll1ll111l_opy_, None):
                _1111lll1ll_opy_[bstack1llll1ll111l_opy_] = {bstack1l1ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪ⏁"): []}
            _1111lll1ll_opy_[bstack1llll1ll111l_opy_][bstack1l1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫ⏂")].append(bstack111l1l11ll_opy_[bstack1l1ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ⏃")])
        _1111lll1ll_opy_[bstack1llll1ll111l_opy_ + bstack1l1ll_opy_ (u"ࠧ࠮ࠩ⏄") + hook_name] = bstack111l1l11ll_opy_
        bstack1llll1l11lll_opy_(node, bstack111l1l11ll_opy_, bstack1l1ll_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ⏅"))
    elif event == bstack1l1ll_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࠨ⏆"):
        if cli.is_running():
            cli.test_framework.track_event(cli_context, bstack1llll11ll11_opy_[hook_type], bstack1lll1111lll_opy_.POST, node, None, bstack1l11111l1l1_opy_)
            return
        bstack111lll111l_opy_ = node.nodeid + bstack1l1ll_opy_ (u"ࠪ࠱ࠬ⏇") + hook_name
        _1111lll1ll_opy_[bstack111lll111l_opy_][bstack1l1ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩ⏈")] = bstack1lllll1l11_opy_()
        bstack1llll1l1l11l_opy_(_1111lll1ll_opy_[bstack111lll111l_opy_][bstack1l1ll_opy_ (u"ࠬࡻࡵࡪࡦࠪ⏉")])
        bstack1llll1l11lll_opy_(node, _1111lll1ll_opy_[bstack111lll111l_opy_], bstack1l1ll_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡆࡪࡰ࡬ࡷ࡭࡫ࡤࠨ⏊"), bstack1llll11llll1_opy_=bstack1l11111l1l1_opy_)
def bstack1llll1l1l1ll_opy_():
    global bstack1llll1ll11ll_opy_
    if bstack1lll11l111_opy_():
        bstack1llll1ll11ll_opy_ = bstack1l1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫ⏋")
    else:
        bstack1llll1ll11ll_opy_ = bstack1l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ⏌")
@bstack11ll1ll1_opy_.bstack1lllll1l1l1l_opy_
def bstack1llll1l1ll11_opy_():
    bstack1llll1l1l1ll_opy_()
    if cli.is_running():
        try:
            bstack111lll11111_opy_(bstack1llll11lllll_opy_)
        except Exception as e:
            logger.debug(bstack1l1ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡪࡲࡳࡰࡹࠠࡱࡣࡷࡧ࡭ࡀࠠࡼࡿࠥ⏍").format(e))
        return
    if bstack11111111_opy_():
        bstack11l1lll1_opy_ = Config.bstack11ll11ll1_opy_()
        bstack1l1ll_opy_ (u"ࠪࠫࠬࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡋࡵࡲࠡࡲࡳࡴࠥࡃࠠ࠲࠮ࠣࡱࡴࡪ࡟ࡦࡺࡨࡧࡺࡺࡥࠡࡩࡨࡸࡸࠦࡵࡴࡧࡧࠤ࡫ࡵࡲࠡࡣ࠴࠵ࡾࠦࡣࡰ࡯ࡰࡥࡳࡪࡳ࠮ࡹࡵࡥࡵࡶࡩ࡯ࡩࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡈࡲࡶࠥࡶࡰࡱࠢࡁࠤ࠶࠲ࠠ࡮ࡱࡧࡣࡪࡾࡥࡤࡷࡷࡩࠥࡪ࡯ࡦࡵࠣࡲࡴࡺࠠࡳࡷࡱࠤࡧ࡫ࡣࡢࡷࡶࡩࠥ࡯ࡴࠡ࡫ࡶࠤࡵࡧࡴࡤࡪࡨࡨࠥ࡯࡮ࠡࡣࠣࡨ࡮࡬ࡦࡦࡴࡨࡲࡹࠦࡰࡳࡱࡦࡩࡸࡹࠠࡪࡦࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡖ࡫ࡹࡸࠦࡷࡦࠢࡱࡩࡪࡪࠠࡵࡱࠣࡹࡸ࡫ࠠࡔࡧ࡯ࡩࡳ࡯ࡵ࡮ࡒࡤࡸࡨ࡮ࠨࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࡡ࡫ࡥࡳࡪ࡬ࡦࡴࠬࠤ࡫ࡵࡲࠡࡲࡳࡴࠥࡄࠠ࠲ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠫࠬ࠭⏎")
        if bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡲࡵࡤࡠࡥࡤࡰࡱ࡫ࡤࠨ⏏")):
            if CONFIG.get(bstack1l1ll_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ⏐")) is not None and int(CONFIG[bstack1l1ll_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭⏑")]) > 1:
                bstack1l11ll111_opy_(bstack11111ll11_opy_)
            return
        bstack1l11ll111_opy_(bstack11111ll11_opy_)
    try:
        bstack111lll11111_opy_(bstack1llll11lllll_opy_)
    except Exception as e:
        logger.debug(bstack1l1ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡨࡰࡱ࡮ࡷࠥࡶࡡࡵࡥ࡫࠾ࠥࢁࡽࠣ⏒").format(e))
bstack1llll1l1ll11_opy_()