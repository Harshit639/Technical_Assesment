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
from filelock import FileLock
import json
import os
import time
import uuid
import logging
from typing import Dict, List, Optional
from bstack_utils.bstack1l1111111_opy_ import get_logger
logger = get_logger(__name__)
bstack11111ll1l11_opy_: Dict[str, float] = {}
bstack11111ll1ll1_opy_: List = []
bstack11111lll1ll_opy_ = 5
bstack11lllll1_opy_ = os.path.join(os.getcwd(), bstack1l1ll_opy_ (u"ࠧ࡭ࡱࡪࠫẠ"), bstack1l1ll_opy_ (u"ࠨ࡭ࡨࡽ࠲ࡳࡥࡵࡴ࡬ࡧࡸ࠴ࡪࡴࡱࡱࠫạ"))
logging.getLogger(bstack1l1ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠫẢ")).setLevel(logging.WARNING)
lock = FileLock(bstack11lllll1_opy_+bstack1l1ll_opy_ (u"ࠥ࠲ࡱࡵࡣ࡬ࠤả"))
class bstack11111ll11ll_opy_:
    duration: float
    name: str
    startTime: float
    worker: int
    status: bool
    failure: str
    details: Optional[str]
    entryType: str
    platform: Optional[int]
    command: Optional[str]
    hookType: Optional[str]
    cli: Optional[bool]
    def __init__(self, duration: float, name: str, start_time: float, bstack11111ll1l1l_opy_: int, status: bool, failure: str, details: Optional[str] = None, platform: Optional[int] = None, command: Optional[str] = None, test_name: Optional[str] = None, hook_type: Optional[str] = None, cli: Optional[bool] = False) -> None:
        self.duration = duration
        self.name = name
        self.startTime = start_time
        self.worker = bstack11111ll1l1l_opy_
        self.status = status
        self.failure = failure
        self.details = details
        self.entryType = bstack1l1ll_opy_ (u"ࠦࡲ࡫ࡡࡴࡷࡵࡩࠧẤ")
        self.platform = platform
        self.command = command
        self.testName = test_name
        self.hookType = hook_type
        self.cli = cli
class bstack1llll11l1l1_opy_:
    global bstack11111ll1l11_opy_
    @staticmethod
    def bstack1ll11l1ll1l_opy_(key: str):
        bstack1ll1l11l11l_opy_ = bstack1llll11l1l1_opy_.bstack11ll1l11l11_opy_(key)
        bstack1llll11l1l1_opy_.mark(bstack1ll1l11l11l_opy_+bstack1l1ll_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧấ"))
        return bstack1ll1l11l11l_opy_
    @staticmethod
    def mark(key: str) -> None:
        try:
            bstack11111ll1l11_opy_[key] = time.time_ns() / 1000000
        except Exception as e:
            logger.debug(bstack1l1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶ࠿ࠦࡻࡾࠤẦ").format(e))
    @staticmethod
    def end(label: str, start: str, end: str, status: bool, failure: Optional[str] = None, hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            bstack1llll11l1l1_opy_.mark(end)
            bstack1llll11l1l1_opy_.measure(label, start, end, status, failure, hook_type, details, command, test_name)
        except Exception as e:
            logger.debug(bstack1l1ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹ࠺ࠡࡽࢀࠦầ").format(e))
    @staticmethod
    def measure(label: str, start: str, end: str, status: bool, failure: Optional[str], hook_type: Optional[str] = None, details: Optional[str] = None, command: Optional[str] = None, test_name: Optional[str] = None) -> None:
        try:
            if start not in bstack11111ll1l11_opy_ or end not in bstack11111ll1l11_opy_:
                logger.debug(bstack1l1ll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡹࡧࡲࡵࠢ࡮ࡩࡾࠦࡷࡪࡶ࡫ࠤࡻࡧ࡬ࡶࡧࠣࡿࢂࠦ࡯ࡳࠢࡨࡲࡩࠦ࡫ࡦࡻࠣࡻ࡮ࡺࡨࠡࡸࡤࡰࡺ࡫ࠠࡼࡿࠥẨ").format(start,end))
                return
            duration: float = bstack11111ll1l11_opy_[end] - bstack11111ll1l11_opy_[start]
            bstack11111lll11l_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡌࡒࡆࡘ࡙ࡠࡋࡖࡣࡗ࡛ࡎࡏࡋࡑࡋࠧẩ"), bstack1l1ll_opy_ (u"ࠥࡪࡦࡲࡳࡦࠤẪ")).lower() == bstack1l1ll_opy_ (u"ࠦࡹࡸࡵࡦࠤẫ")
            bstack11111lll1l1_opy_: bstack11111ll11ll_opy_ = bstack11111ll11ll_opy_(duration, label, bstack11111ll1l11_opy_[start], os.getpid(), status, failure, details, os.environ.get(bstack1l1ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠧẬ"), 0), command, test_name, hook_type, bstack11111lll11l_opy_)
            del bstack11111ll1l11_opy_[start]
            del bstack11111ll1l11_opy_[end]
            bstack1llll11l1l1_opy_.bstack11111ll1lll_opy_(bstack11111lll1l1_opy_)
        except Exception as e:
            logger.debug(bstack1l1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡲ࡫ࡡࡴࡷࡵ࡭ࡳ࡭ࠠ࡬ࡧࡼࠤࡲ࡫ࡴࡳ࡫ࡦࡷ࠿ࠦࡻࡾࠤậ").format(e))
    @staticmethod
    def bstack11111ll1lll_opy_(bstack11111lll1l1_opy_):
        os.makedirs(os.path.dirname(bstack11lllll1_opy_)) if not os.path.exists(os.path.dirname(bstack11lllll1_opy_)) else None
        bstack1llll11l1l1_opy_.bstack11111llll11_opy_()
        try:
            with lock:
                with open(bstack11lllll1_opy_, bstack1l1ll_opy_ (u"ࠢࡳ࠭ࠥẮ"), encoding=bstack1l1ll_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢắ")) as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
                    data.append(bstack11111lll1l1_opy_.__dict__)
                    file.seek(0)
                    file.truncate()
                    json.dump(data, file, indent=4)
        except FileNotFoundError as bstack11111lll111_opy_:
            logger.debug(bstack1l1ll_opy_ (u"ࠤࡉ࡭ࡱ࡫ࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦࠣࡿࢂࠨẰ").format(bstack11111lll111_opy_))
            with lock:
                with open(bstack11lllll1_opy_, bstack1l1ll_opy_ (u"ࠥࡻࠧằ"), encoding=bstack1l1ll_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥẲ")) as file:
                    data = [bstack11111lll1l1_opy_.__dict__]
                    json.dump(data, file, indent=4)
        except Exception as e:
            logger.debug(bstack1l1ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠ࡬ࡧࡼࠤࡲ࡫ࡴࡳ࡫ࡦࡷࠥࡧࡰࡱࡧࡱࡨࠥࢁࡽࠣẳ").format(str(e)))
        finally:
            if os.path.exists(bstack11lllll1_opy_+bstack1l1ll_opy_ (u"ࠨ࠮࡭ࡱࡦ࡯ࠧẴ")):
                os.remove(bstack11lllll1_opy_+bstack1l1ll_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨẵ"))
    @staticmethod
    def bstack11111llll11_opy_():
        attempt = 0
        while (attempt < bstack11111lll1ll_opy_):
            attempt += 1
            if os.path.exists(bstack11lllll1_opy_+bstack1l1ll_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢẶ")):
                time.sleep(0.5)
            else:
                break
    @staticmethod
    def bstack11ll1l11l11_opy_(label: str) -> str:
        try:
            return bstack1l1ll_opy_ (u"ࠤࡾࢁ࠿ࢁࡽࠣặ").format(label,str(uuid.uuid4().hex)[:6])
        except Exception as e:
            logger.debug(bstack1l1ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨẸ").format(e))