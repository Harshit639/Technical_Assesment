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
import multiprocessing
import os
import json
from time import sleep
import time
import bstack_utils.accessibility as bstack111111l1l_opy_
import subprocess
from browserstack_sdk.bstack1l11ll1111_opy_ import *
from bstack_utils.config import Config
from bstack_utils.messages import bstack11lll1lll1_opy_
from bstack_utils.bstack111llllll1_opy_ import bstack1ll1l111l1_opy_
from bstack_utils.constants import bstack1111l111ll_opy_
from bstack_utils.bstack1l1l1l1lll_opy_ import bstack11ll1l1ll1_opy_
class bstack1lll1111_opy_:
    def __init__(self, args, logger, bstack11111llll1_opy_, bstack11111ll1ll_opy_):
        self.args = args
        self.logger = logger
        self.bstack11111llll1_opy_ = bstack11111llll1_opy_
        self.bstack11111ll1ll_opy_ = bstack11111ll1ll_opy_
        self._prepareconfig = None
        self.Config = None
        self.runner = None
        self.bstack11ll11l11l_opy_ = []
        self.bstack11111l1l11_opy_ = None
        self.bstack1l1l1lllll_opy_ = []
        self.bstack11111ll11l_opy_ = self.bstack1ll1l11ll_opy_()
        self.bstack1l111ll111_opy_ = -1
    def bstack1l1lll111l_opy_(self, bstack11111lllll_opy_):
        self.parse_args()
        self.bstack1111l1111l_opy_()
        self.bstack1111l11ll1_opy_(bstack11111lllll_opy_)
        self.bstack1111l1lll1_opy_()
    def bstack11l11l1111_opy_(self):
        bstack1l1l1l1lll_opy_ = bstack11ll1l1ll1_opy_.bstack11ll11ll1_opy_(self.bstack11111llll1_opy_, self.logger)
        if bstack1l1l1l1lll_opy_ is None:
            self.logger.warn(bstack1l1ll_opy_ (u"ࠥࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣ࡬ࡦࡴࡤ࡭ࡧࡵࠤ࡮ࡹࠠ࡯ࡱࡷࠤ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡥࡥ࠰ࠣࡗࡰ࡯ࡰࡱ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࠨ၈"))
            return
        bstack1111l1l1ll_opy_ = False
        bstack1l1l1l1lll_opy_.bstack1111ll1111_opy_(bstack1l1ll_opy_ (u"ࠦࡪࡴࡡࡣ࡮ࡨࡨࠧ၉"), bstack1l1l1l1lll_opy_.bstack11ll1l11l_opy_())
        start_time = time.time()
        if bstack1l1l1l1lll_opy_.bstack11ll1l11l_opy_():
            test_files = self.bstack11111ll111_opy_()
            bstack1111l1l1ll_opy_ = True
            bstack1111l1l111_opy_ = bstack1l1l1l1lll_opy_.bstack11111l11l1_opy_(test_files)
            if bstack1111l1l111_opy_:
                self.bstack11ll11l11l_opy_ = [os.path.normpath(item).replace(bstack1l1ll_opy_ (u"ࠬࡢ࡜ࠨ၊"), bstack1l1ll_opy_ (u"࠭࠯ࠨ။")) for item in bstack1111l1l111_opy_]
                self.__1111l1l1l1_opy_()
                bstack1l1l1l1lll_opy_.bstack1111l1llll_opy_(bstack1111l1l1ll_opy_)
                self.logger.info(bstack1l1ll_opy_ (u"ࠢࡕࡧࡶࡸࡸࠦࡲࡦࡱࡵࡨࡪࡸࡥࡥࠢࡸࡷ࡮ࡴࡧࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧ၌").format(self.bstack11ll11l11l_opy_))
            else:
                self.logger.info(bstack1l1ll_opy_ (u"ࠣࡐࡲࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡹࡨࡶࡪࠦࡲࡦࡱࡵࡨࡪࡸࡥࡥࠢࡥࡽࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠳ࠨ၍"))
        bstack1l1l1l1lll_opy_.bstack1111ll1111_opy_(bstack1l1ll_opy_ (u"ࠤࡷ࡭ࡲ࡫ࡔࡢ࡭ࡨࡲ࡙ࡵࡁࡱࡲ࡯ࡽࠧ၎"), int((time.time() - start_time) * 1000)) # bstack1111l1l11l_opy_ to bstack1111l11111_opy_
    def __1111l1l1l1_opy_(self):
        bstack1l1ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡳࡰࡦࡩࡥࠡࡣ࡯ࡰࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࠡࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠤ࡮ࡴࠠࡴࡧ࡯ࡪ࠳ࡧࡲࡨࡵࠣࡻ࡮ࡺࡨࠡࡵࡨࡰ࡫࠴ࡳࡱࡧࡦࡣ࡫࡯࡬ࡦࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡕ࡮࡭ࡻࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡥࡥࠢࡩ࡭ࡱ࡫ࡳࠡࡹ࡬ࡰࡱࠦࡢࡦࠢࡵࡹࡳࡁࠠࡢ࡮࡯ࠤࡴࡺࡨࡦࡴࠣࡇࡑࡏࠠࡧ࡮ࡤ࡫ࡸࠦࡡࡳࡧࠣࡴࡷ࡫ࡳࡦࡴࡹࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ၏")
        bstack11111l1lll_opy_ = [arg for arg in self.args if not (arg.endswith(bstack1l1ll_opy_ (u"ࠫ࠳ࡶࡹࠨၐ")) and os.path.exists(arg))]
        self.args = self.bstack11ll11l11l_opy_ + bstack11111l1lll_opy_
    @staticmethod
    def version():
        import pytest
        return pytest.__version__
    @staticmethod
    def bstack1111l11lll_opy_():
        import importlib
        if getattr(importlib, bstack1l1ll_opy_ (u"ࠬ࡬ࡩ࡯ࡦࡢࡰࡴࡧࡤࡦࡴࠪၑ"), False):
            bstack1111l1ll11_opy_ = importlib.find_loader(bstack1l1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨၒ"))
        else:
            bstack1111l1ll11_opy_ = importlib.util.find_spec(bstack1l1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩၓ"))
    def bstack11111l1l1l_opy_(self, arg):
        if arg in self.args:
            i = self.args.index(arg)
            self.args.pop(i + 1)
            self.args.pop(i)
    def parse_args(self):
        self.bstack1l111ll111_opy_ = -1
        if self.bstack11111ll1ll_opy_ and bstack1l1ll_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨၔ") in self.bstack11111llll1_opy_:
            self.bstack1l111ll111_opy_ = int(self.bstack11111llll1_opy_[bstack1l1ll_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩၕ")])
        try:
            bstack11111ll1l1_opy_ = [bstack1l1ll_opy_ (u"ࠪ࠱࠲ࡪࡲࡪࡸࡨࡶࠬၖ"), bstack1l1ll_opy_ (u"ࠫ࠲࠳ࡰ࡭ࡷࡪ࡭ࡳࡹࠧၗ"), bstack1l1ll_opy_ (u"ࠬ࠳ࡰࠨၘ")]
            if self.bstack1l111ll111_opy_ >= 0:
                bstack11111ll1l1_opy_.extend([bstack1l1ll_opy_ (u"࠭࠭࠮ࡰࡸࡱࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧၙ"), bstack1l1ll_opy_ (u"ࠧ࠮ࡰࠪၚ")])
            for arg in bstack11111ll1l1_opy_:
                self.bstack11111l1l1l_opy_(arg)
        except Exception as exc:
            self.logger.error(str(exc))
    def get_args(self):
        return self.args
    def bstack1111l1111l_opy_(self):
        bstack11111l1l11_opy_ = [os.path.normpath(item) for item in self.args]
        self.bstack11111l1l11_opy_ = bstack11111l1l11_opy_
        return bstack11111l1l11_opy_
    def bstack111lll11l_opy_(self):
        try:
            from _pytest.config import _prepareconfig
            from _pytest.config import Config
            from _pytest import runner
            self.bstack1111l11lll_opy_()
            self._prepareconfig = _prepareconfig
            self.Config = Config
            self.runner = runner
        except Exception as e:
            self.logger.warn(e, bstack11lll1lll1_opy_)
    def bstack1111l11ll1_opy_(self, bstack11111lllll_opy_):
        bstack11l1lll1_opy_ = Config.bstack11ll11ll1_opy_()
        if bstack11111lllll_opy_:
            self.bstack11111l1l11_opy_.append(bstack1l1ll_opy_ (u"ࠨ࠯࠰ࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬၛ"))
            self.bstack11111l1l11_opy_.append(bstack1l1ll_opy_ (u"ࠩࡗࡶࡺ࡫ࠧၜ"))
        if bstack11l1lll1_opy_.bstack11111l11ll_opy_():
            self.bstack11111l1l11_opy_.append(bstack1l1ll_opy_ (u"ࠪ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩၝ"))
            self.bstack11111l1l11_opy_.append(bstack1l1ll_opy_ (u"࡙ࠫࡸࡵࡦࠩၞ"))
        self.bstack11111l1l11_opy_.append(bstack1l1ll_opy_ (u"ࠬ࠳ࡰࠨၟ"))
        self.bstack11111l1l11_opy_.append(bstack1l1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡵࡲࡵࡨ࡫ࡱࠫၠ"))
        self.bstack11111l1l11_opy_.append(bstack1l1ll_opy_ (u"ࠧ࠮࠯ࡧࡶ࡮ࡼࡥࡳࠩၡ"))
        self.bstack11111l1l11_opy_.append(bstack1l1ll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨၢ"))
        if self.bstack1l111ll111_opy_ > 1:
            self.bstack11111l1l11_opy_.append(bstack1l1ll_opy_ (u"ࠩ࠰ࡲࠬၣ"))
            self.bstack11111l1l11_opy_.append(str(self.bstack1l111ll111_opy_))
    def bstack1111l1lll1_opy_(self):
        if bstack1ll1l111l1_opy_.bstack1l1ll1l1l_opy_(self.bstack11111llll1_opy_):
             self.bstack11111l1l11_opy_ += [
                bstack1111l111ll_opy_.get(bstack1l1ll_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࠩၤ")), str(bstack1ll1l111l1_opy_.bstack1l1ll1ll1_opy_(self.bstack11111llll1_opy_)),
                bstack1111l111ll_opy_.get(bstack1l1ll_opy_ (u"ࠫࡩ࡫࡬ࡢࡻࠪၥ")), str(bstack1111l111ll_opy_.get(bstack1l1ll_opy_ (u"ࠬࡸࡥࡳࡷࡱ࠱ࡩ࡫࡬ࡢࡻࠪၦ")))
            ]
    def bstack11111l1ll1_opy_(self):
        bstack1l1l1lllll_opy_ = []
        for spec in self.bstack11ll11l11l_opy_:
            bstack11lll1l111_opy_ = [spec]
            bstack11lll1l111_opy_ += self.bstack11111l1l11_opy_
            bstack1l1l1lllll_opy_.append(bstack11lll1l111_opy_)
        self.bstack1l1l1lllll_opy_ = bstack1l1l1lllll_opy_
        return bstack1l1l1lllll_opy_
    def bstack1ll1l11ll_opy_(self):
        try:
            from pytest_bdd import reporting
            self.bstack11111ll11l_opy_ = True
            return True
        except Exception as e:
            self.bstack11111ll11l_opy_ = False
        return self.bstack11111ll11l_opy_
    def bstack1ll1l1l111_opy_(self):
        bstack1l1ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡈࡧࡷࠤࡹ࡮ࡥࠡࡥࡲࡹࡳࡺࠠࡰࡨࠣࡸࡪࡹࡴࡴࠢࡺ࡭ࡹ࡮࡯ࡶࡶࠣࡶࡺࡴ࡮ࡪࡰࡪࠤࡹ࡮ࡥ࡮ࠢࡸࡷ࡮ࡴࡧࠡࡲࡼࡸࡪࡹࡴࠨࡵࠣ࠱࠲ࡩ࡯࡭࡮ࡨࡧࡹ࠳࡯࡯࡮ࡼࠤ࡫ࡲࡡࡨ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡯࡮ࡵ࠼ࠣࡘ࡭࡫ࠠࡵࡱࡷࡥࡱࠦ࡮ࡶ࡯ࡥࡩࡷࠦ࡯ࡧࠢࡷࡩࡸࡺࡳࠡࡥࡲࡰࡱ࡫ࡣࡵࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤၧ")
        try:
            self.logger.info(bstack1l1ll_opy_ (u"ࠢࡄࡱ࡯ࡰࡪࡩࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࡵࠣࡹࡸ࡯࡮ࡨࠢࡳࡽࡹ࡫ࡳࡵࠢ࠰࠱ࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡵ࡮࡭ࡻࠥၨ"))
            bstack1111l11l1l_opy_ = [bstack1l1ll_opy_ (u"ࠣࡲࡼࡸࡪࡹࡴࠣၩ"), *self.bstack11111l1l11_opy_, bstack1l1ll_opy_ (u"ࠤ࠰࠱ࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡵ࡮࡭ࡻࠥၪ")]
            result = subprocess.run(bstack1111l11l1l_opy_, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                self.logger.error(bstack1l1ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࡶ࠾ࠥࢁࡽࠣၫ").format(result.stderr))
                return 0
            test_count = result.stdout.count(bstack1l1ll_opy_ (u"ࠦࡁࡌࡵ࡯ࡥࡷ࡭ࡴࡴࠠࠣၬ"))
            self.logger.info(bstack1l1ll_opy_ (u"࡚ࠧ࡯ࡵࡣ࡯ࠤࡹ࡫ࡳࡵࡵࠣࡧࡴࡲ࡬ࡦࡥࡷࡩࡩࡀࠠࡼࡿࠥၭ").format(test_count))
            return test_count
        except Exception as e:
            self.logger.error(bstack1l1ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤࡱࡸࡲࡹࡀࠠࡼࡿࠥၮ").format(e))
            return 0
    def bstack11llll1ll_opy_(self, bstack11111lll11_opy_, bstack1l1lll111l_opy_):
        bstack1l1lll111l_opy_[bstack1l1ll_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧၯ")] = self.bstack11111llll1_opy_
        multiprocessing.set_start_method(bstack1l1ll_opy_ (u"ࠨࡵࡳࡥࡼࡴࠧၰ"))
        bstack1l1lllll1l_opy_ = []
        manager = multiprocessing.Manager()
        bstack1111l111l1_opy_ = manager.list()
        if bstack1l1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬၱ") in self.bstack11111llll1_opy_:
            for index, platform in enumerate(self.bstack11111llll1_opy_[bstack1l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ၲ")]):
                bstack1l1lllll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                            target=bstack11111lll11_opy_,
                                                            args=(self.bstack11111l1l11_opy_, bstack1l1lll111l_opy_, bstack1111l111l1_opy_)))
            bstack1111l1ll1l_opy_ = len(self.bstack11111llll1_opy_[bstack1l1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧၳ")])
        else:
            bstack1l1lllll1l_opy_.append(multiprocessing.Process(name=str(0),
                                                        target=bstack11111lll11_opy_,
                                                        args=(self.bstack11111l1l11_opy_, bstack1l1lll111l_opy_, bstack1111l111l1_opy_)))
            bstack1111l1ll1l_opy_ = 1
        i = 0
        for t in bstack1l1lllll1l_opy_:
            os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬၴ")] = str(i)
            if bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩၵ") in self.bstack11111llll1_opy_:
                os.environ[bstack1l1ll_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨၶ")] = json.dumps(self.bstack11111llll1_opy_[bstack1l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫၷ")][i % bstack1111l1ll1l_opy_])
            i += 1
            t.start()
        for t in bstack1l1lllll1l_opy_:
            t.join()
        return list(bstack1111l111l1_opy_)
    @staticmethod
    def bstack11111l111_opy_(driver, bstack11111lll1l_opy_, logger, item=None, wait=False):
        item = item or getattr(threading.current_thread(), bstack1l1ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭ၸ"), None)
        if item and getattr(item, bstack1l1ll_opy_ (u"ࠪࡣࡦ࠷࠱ࡺࡡࡷࡩࡸࡺ࡟ࡤࡣࡶࡩࠬၹ"), None) and not getattr(item, bstack1l1ll_opy_ (u"ࠫࡤࡧ࠱࠲ࡻࡢࡷࡹࡵࡰࡠࡦࡲࡲࡪ࠭ၺ"), False):
            logger.info(
                bstack1l1ll_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠣࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡯ࡳࠡࡷࡱࡨࡪࡸࡷࡢࡻ࠱ࠦၻ"))
            bstack1111l11l11_opy_ = item.cls.__name__ if not item.cls is None else None
            bstack111111l1l_opy_.bstack1lll1llll1_opy_(driver, item.name, item.path)
            item._a11y_stop_done = True
            if wait:
                sleep(2)
    def bstack11111ll111_opy_(self):
        bstack1l1ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶࠤࡹ࡮ࡥࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡴࡰࠢࡥࡩࠥ࡫ࡸࡦࡥࡸࡸࡪࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧၼ")
        test_files = []
        for arg in self.args:
            if arg.endswith(bstack1l1ll_opy_ (u"ࠧ࠯ࡲࡼࠫၽ")) and os.path.exists(arg):
                test_files.append(arg)
        return test_files