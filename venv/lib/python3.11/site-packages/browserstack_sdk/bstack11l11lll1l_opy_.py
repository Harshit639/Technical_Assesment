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
import threading
import os
import logging
from uuid import uuid4
from bstack_utils.bstack111ll11l1l_opy_ import bstack111ll1lll1_opy_, bstack111ll1l1l1_opy_
from bstack_utils.bstack111llll111_opy_ import bstack11ll1llll1_opy_
from bstack_utils.helper import bstack11ll1ll11_opy_, bstack1lllll1l11_opy_, Result
from bstack_utils.bstack111lll1111_opy_ import bstack11ll1ll1_opy_
from bstack_utils.capture import bstack111ll11l11_opy_
from bstack_utils.constants import *
logger = logging.getLogger(__name__)
class bstack11l11lll1l_opy_:
    def __init__(self):
        self.bstack111ll111l1_opy_ = bstack111ll11l11_opy_(self.bstack111lll11ll_opy_)
        self.tests = {}
    @staticmethod
    def bstack111lll11ll_opy_(log):
        if not (log[bstack1l1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ༬")] and log[bstack1l1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ༭")].strip()):
            return
        active = bstack11ll1llll1_opy_.bstack111lll11l1_opy_()
        log = {
            bstack1l1ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ༮"): log[bstack1l1ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ༯")],
            bstack1l1ll_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭༰"): bstack1lllll1l11_opy_(),
            bstack1l1ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ༱"): log[bstack1l1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭༲")],
        }
        if active:
            if active[bstack1l1ll_opy_ (u"࠭ࡴࡺࡲࡨࠫ༳")] == bstack1l1ll_opy_ (u"ࠧࡩࡱࡲ࡯ࠬ༴"):
                log[bstack1l1ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ༵")] = active[bstack1l1ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ༶")]
            elif active[bstack1l1ll_opy_ (u"ࠪࡸࡾࡶࡥࠨ༷")] == bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࠩ༸"):
                log[bstack1l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨ༹ࠬ")] = active[bstack1l1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭༺")]
        bstack11ll1ll1_opy_.bstack11l1l1lll1_opy_([log])
    def start_test(self, attrs):
        test_uuid = uuid4().__str__()
        self.tests[test_uuid] = {}
        self.bstack111ll111l1_opy_.start()
        driver = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭༻"), None)
        bstack111ll11l1l_opy_ = bstack111ll1l1l1_opy_(
            name=attrs.scenario.name,
            uuid=test_uuid,
            started_at=bstack1lllll1l11_opy_(),
            file_path=attrs.feature.filename,
            result=bstack1l1ll_opy_ (u"ࠣࡲࡨࡲࡩ࡯࡮ࡨࠤ༼"),
            framework=bstack1l1ll_opy_ (u"ࠩࡅࡩ࡭ࡧࡶࡦࠩ༽"),
            scope=[attrs.feature.name],
            bstack111lll1ll1_opy_=bstack11ll1ll1_opy_.bstack111lll1l1l_opy_(driver) if driver and driver.session_id else {},
            meta={},
            tags=attrs.scenario.tags
        )
        self.tests[test_uuid][bstack1l1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭༾")] = bstack111ll11l1l_opy_
        threading.current_thread().current_test_uuid = test_uuid
        bstack11ll1ll1_opy_.bstack111ll111ll_opy_(bstack1l1ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ༿"), bstack111ll11l1l_opy_)
    def end_test(self, attrs):
        bstack111ll1l111_opy_ = {
            bstack1l1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥཀ"): attrs.feature.name,
            bstack1l1ll_opy_ (u"ࠨࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠦཁ"): attrs.feature.description
        }
        current_test_uuid = threading.current_thread().current_test_uuid
        bstack111ll11l1l_opy_ = self.tests[current_test_uuid][bstack1l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪག")]
        meta = {
            bstack1l1ll_opy_ (u"ࠣࡨࡨࡥࡹࡻࡲࡦࠤགྷ"): bstack111ll1l111_opy_,
            bstack1l1ll_opy_ (u"ࠤࡶࡸࡪࡶࡳࠣང"): bstack111ll11l1l_opy_.meta.get(bstack1l1ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩཅ"), []),
            bstack1l1ll_opy_ (u"ࠦࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨཆ"): {
                bstack1l1ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥཇ"): attrs.feature.scenarios[0].name if len(attrs.feature.scenarios) else None
            }
        }
        bstack111ll11l1l_opy_.bstack111lll1lll_opy_(meta)
        bstack111ll11l1l_opy_.bstack111ll1l1ll_opy_(bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡶࠫ཈"), []))
        bstack111ll1l11l_opy_, exception = self._111ll11lll_opy_(attrs)
        bstack111llll11l_opy_ = Result(result=attrs.status.name, exception=exception, bstack111ll1ll1l_opy_=[bstack111ll1l11l_opy_])
        self.tests[threading.current_thread().current_test_uuid][bstack1l1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪཉ")].stop(time=bstack1lllll1l11_opy_(), duration=int(attrs.duration)*1000, result=bstack111llll11l_opy_)
        bstack11ll1ll1_opy_.bstack111ll111ll_opy_(bstack1l1ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪཊ"), self.tests[threading.current_thread().current_test_uuid][bstack1l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬཋ")])
    def bstack111l1ll1_opy_(self, attrs):
        bstack111ll1111l_opy_ = {
            bstack1l1ll_opy_ (u"ࠪ࡭ࡩ࠭ཌ"): uuid4().__str__(),
            bstack1l1ll_opy_ (u"ࠫࡰ࡫ࡹࡸࡱࡵࡨࠬཌྷ"): attrs.keyword,
            bstack1l1ll_opy_ (u"ࠬࡹࡴࡦࡲࡢࡥࡷ࡭ࡵ࡮ࡧࡱࡸࠬཎ"): [],
            bstack1l1ll_opy_ (u"࠭ࡴࡦࡺࡷࠫཏ"): attrs.name,
            bstack1l1ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫཐ"): bstack1lllll1l11_opy_(),
            bstack1l1ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨད"): bstack1l1ll_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪདྷ"),
            bstack1l1ll_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨན"): bstack1l1ll_opy_ (u"ࠫࠬཔ")
        }
        self.tests[threading.current_thread().current_test_uuid][bstack1l1ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡨࡦࡺࡡࠨཕ")].add_step(bstack111ll1111l_opy_)
        threading.current_thread().current_step_uuid = bstack111ll1111l_opy_[bstack1l1ll_opy_ (u"࠭ࡩࡥࠩབ")]
    def bstack1ll11ll11_opy_(self, attrs):
        current_test_id = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫབྷ"), None)
        current_step_uuid = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡶࡸࡪࡶ࡟ࡶࡷ࡬ࡨࠬམ"), None)
        bstack111ll1l11l_opy_, exception = self._111ll11lll_opy_(attrs)
        bstack111llll11l_opy_ = Result(result=attrs.status.name, exception=exception, bstack111ll1ll1l_opy_=[bstack111ll1l11l_opy_])
        self.tests[current_test_id][bstack1l1ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬཙ")].bstack111ll1ll11_opy_(current_step_uuid, duration=int(attrs.duration)*1000, result=bstack111llll11l_opy_)
        threading.current_thread().current_step_uuid = None
    def bstack1l1llll11_opy_(self, name, attrs):
        try:
            bstack111ll1llll_opy_ = uuid4().__str__()
            self.tests[bstack111ll1llll_opy_] = {}
            self.bstack111ll111l1_opy_.start()
            scopes = []
            driver = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩཚ"), None)
            current_thread = threading.current_thread()
            if not hasattr(current_thread, bstack1l1ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢ࡬ࡴࡵ࡫ࡴࠩཛ")):
                current_thread.current_test_hooks = []
            current_thread.current_test_hooks.append(bstack111ll1llll_opy_)
            if name in [bstack1l1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤཛྷ"), bstack1l1ll_opy_ (u"ࠨࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠤཝ")]:
                file_path = os.path.join(attrs.config.base_dir, attrs.config.environment_file)
                scopes = [attrs.config.environment_file]
            elif name in [bstack1l1ll_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠣཞ"), bstack1l1ll_opy_ (u"ࠣࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠣཟ")]:
                file_path = attrs.filename
                scopes = [attrs.name]
            else:
                file_path = attrs.filename
                if hasattr(attrs, bstack1l1ll_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪའ")):
                    scopes =  [attrs.feature.name]
            hook_data = bstack111ll1lll1_opy_(
                name=name,
                uuid=bstack111ll1llll_opy_,
                started_at=bstack1lllll1l11_opy_(),
                file_path=file_path,
                framework=bstack1l1ll_opy_ (u"ࠥࡆࡪ࡮ࡡࡷࡧࠥཡ"),
                bstack111lll1ll1_opy_=bstack11ll1ll1_opy_.bstack111lll1l1l_opy_(driver) if driver and driver.session_id else {},
                scope=scopes,
                result=bstack1l1ll_opy_ (u"ࠦࡵ࡫࡮ࡥ࡫ࡱ࡫ࠧར"),
                hook_type=name
            )
            self.tests[bstack111ll1llll_opy_][bstack1l1ll_opy_ (u"ࠧࡺࡥࡴࡶࡢࡨࡦࡺࡡࠣལ")] = hook_data
            current_test_id = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠨࡣࡶࡴࡵࡩࡳࡺ࡟ࡵࡧࡶࡸࡤࡻࡵࡪࡦࠥཤ"), None)
            if current_test_id:
                hook_data.bstack111lll1l11_opy_(current_test_id)
            if name == bstack1l1ll_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦཥ"):
                threading.current_thread().before_all_hook_uuid = bstack111ll1llll_opy_
            threading.current_thread().current_hook_uuid = bstack111ll1llll_opy_
            bstack11ll1ll1_opy_.bstack111ll111ll_opy_(bstack1l1ll_opy_ (u"ࠣࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠤས"), hook_data)
        except Exception as e:
            logger.debug(bstack1l1ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡱࡦࡧࡺࡸࡲࡦࡦࠣ࡭ࡳࠦࡳࡵࡣࡵࡸࠥ࡮࡯ࡰ࡭ࠣࡩࡻ࡫࡮ࡵࡵ࠯ࠤ࡭ࡵ࡯࡬ࠢࡱࡥࡲ࡫࠺ࠡࠧࡶ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࠫࡳࠣཧ"), name, e)
    def bstack1111lll1l_opy_(self, attrs):
        bstack111lll111l_opy_ = bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧཨ"), None)
        hook_data = self.tests[bstack111lll111l_opy_][bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧཀྵ")]
        status = bstack1l1ll_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧཪ")
        exception = None
        bstack111ll1l11l_opy_ = None
        if hook_data.name == bstack1l1ll_opy_ (u"ࠨࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠤཫ"):
            self.bstack111ll111l1_opy_.reset()
            bstack111ll11ll1_opy_ = self.tests[bstack11ll1ll11_opy_(threading.current_thread(), bstack1l1ll_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧཬ"), None)][bstack1l1ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫ཭")].result.result
            if bstack111ll11ll1_opy_ == bstack1l1ll_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ཮"):
                if attrs.hook_failures == 1:
                    status = bstack1l1ll_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ཯")
                elif attrs.hook_failures == 2:
                    status = bstack1l1ll_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ཰")
            elif attrs.aborted:
                status = bstack1l1ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨཱࠧ")
            threading.current_thread().before_all_hook_uuid = None
        else:
            if hook_data.name == bstack1l1ll_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ིࠪ") and attrs.hook_failures == 1:
                status = bstack1l1ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪཱིࠢ")
            elif hasattr(attrs, bstack1l1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠨུ")) and attrs.error_message:
                status = bstack1l1ll_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤཱུ")
            bstack111ll1l11l_opy_, exception = self._111ll11lll_opy_(attrs)
        bstack111llll11l_opy_ = Result(result=status, exception=exception, bstack111ll1ll1l_opy_=[bstack111ll1l11l_opy_])
        hook_data.stop(time=bstack1lllll1l11_opy_(), duration=0, result=bstack111llll11l_opy_)
        bstack11ll1ll1_opy_.bstack111ll111ll_opy_(bstack1l1ll_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬྲྀ"), self.tests[bstack111lll111l_opy_][bstack1l1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡧࡥࡹࡧࠧཷ")])
        threading.current_thread().current_hook_uuid = None
    def _111ll11lll_opy_(self, attrs):
        try:
            import traceback
            bstack11l11l111l_opy_ = traceback.format_tb(attrs.exc_traceback)
            bstack111ll1l11l_opy_ = bstack11l11l111l_opy_[-1] if bstack11l11l111l_opy_ else None
            exception = attrs.exception
        except Exception:
            logger.debug(bstack1l1ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡵࡩࡩࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡣࡶࡵࡷࡳࡲࠦࡴࡳࡣࡦࡩࡧࡧࡣ࡬ࠤླྀ"))
            bstack111ll1l11l_opy_ = None
            exception = None
        return bstack111ll1l11l_opy_, exception