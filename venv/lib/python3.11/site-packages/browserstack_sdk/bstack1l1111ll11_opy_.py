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
import multiprocessing
import os
from bstack_utils.config import Config
class bstack1lllll1l1_opy_():
  def __init__(self, args, logger, bstack11111llll1_opy_, bstack11111ll1ll_opy_, bstack11111l1111_opy_):
    self.args = args
    self.logger = logger
    self.bstack11111llll1_opy_ = bstack11111llll1_opy_
    self.bstack11111ll1ll_opy_ = bstack11111ll1ll_opy_
    self.bstack11111l1111_opy_ = bstack11111l1111_opy_
  def bstack11llll1ll_opy_(self, bstack11111lll11_opy_, bstack1l1lll111l_opy_, bstack11111l111l_opy_=False):
    bstack1l1lllll1l_opy_ = []
    manager = multiprocessing.Manager()
    bstack1111l111l1_opy_ = manager.list()
    bstack11l1lll1_opy_ = Config.bstack11ll11ll1_opy_()
    if bstack11111l111l_opy_:
      for index, platform in enumerate(self.bstack11111llll1_opy_[bstack1l1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫၾ")]):
        if index == 0:
          bstack1l1lll111l_opy_[bstack1l1ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬၿ")] = self.args
        bstack1l1lllll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11111lll11_opy_,
                                                    args=(bstack1l1lll111l_opy_, bstack1111l111l1_opy_)))
    else:
      for index, platform in enumerate(self.bstack11111llll1_opy_[bstack1l1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ႀ")]):
        bstack1l1lllll1l_opy_.append(multiprocessing.Process(name=str(index),
                                                    target=bstack11111lll11_opy_,
                                                    args=(bstack1l1lll111l_opy_, bstack1111l111l1_opy_)))
    i = 0
    for t in bstack1l1lllll1l_opy_:
      try:
        if bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬႁ")):
          os.environ[bstack1l1ll_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭ႂ")] = json.dumps(self.bstack11111llll1_opy_[bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩႃ")][i % self.bstack11111l1111_opy_])
      except Exception as e:
        self.logger.debug(bstack1l1ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡹࡴࡰࡴ࡬ࡲ࡬ࠦࡣࡶࡴࡵࡩࡳࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡩࡹࡧࡩ࡭ࡵ࠽ࠤࢀࢃࠢႄ").format(str(e)))
      i += 1
      t.start()
    for t in bstack1l1lllll1l_opy_:
      t.join()
    return list(bstack1111l111l1_opy_)