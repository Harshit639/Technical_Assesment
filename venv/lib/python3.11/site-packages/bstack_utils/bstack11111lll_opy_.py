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
import json
from bstack_utils.bstack1l1111111_opy_ import get_logger
logger = get_logger(__name__)
class bstack11ll11lll1l_opy_(object):
  bstack1l1ll1lll1_opy_ = os.path.join(os.path.expanduser(bstack1l1ll_opy_ (u"࠭ࡾࠨ᜽")), bstack1l1ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ᜾"))
  bstack11ll11ll1l1_opy_ = os.path.join(bstack1l1ll1lll1_opy_, bstack1l1ll_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵ࠱࡮ࡸࡵ࡮ࠨ᜿"))
  commands_to_wrap = None
  perform_scan = None
  bstack11l1l11l1_opy_ = None
  bstack1ll11l11_opy_ = None
  bstack11ll1lllll1_opy_ = None
  bstack11ll1lll1ll_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1l1ll_opy_ (u"ࠩ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠫᝀ")):
      cls.instance = super(bstack11ll11lll1l_opy_, cls).__new__(cls)
      cls.instance.bstack11ll11lll11_opy_()
    return cls.instance
  def bstack11ll11lll11_opy_(self):
    try:
      with open(self.bstack11ll11ll1l1_opy_, bstack1l1ll_opy_ (u"ࠪࡶࠬᝁ")) as bstack11l1l1ll11_opy_:
        bstack11ll11llll1_opy_ = bstack11l1l1ll11_opy_.read()
        data = json.loads(bstack11ll11llll1_opy_)
        if bstack1l1ll_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ᝂ") in data:
          self.bstack11ll1ll111l_opy_(data[bstack1l1ll_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧᝃ")])
        if bstack1l1ll_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧᝄ") in data:
          self.bstack1111l1ll1_opy_(data[bstack1l1ll_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨᝅ")])
        if bstack1l1ll_opy_ (u"ࠨࡰࡲࡲࡇ࡙ࡴࡢࡥ࡮ࡍࡳ࡬ࡲࡢࡃ࠴࠵ࡾࡉࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬᝆ") in data:
          self.bstack11ll11ll1ll_opy_(data[bstack1l1ll_opy_ (u"ࠩࡱࡳࡳࡈࡓࡵࡣࡦ࡯ࡎࡴࡦࡳࡣࡄ࠵࠶ࡿࡃࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᝇ")])
    except:
      pass
  def bstack11ll11ll1ll_opy_(self, bstack11ll1lll1ll_opy_):
    if bstack11ll1lll1ll_opy_ != None:
      self.bstack11ll1lll1ll_opy_ = bstack11ll1lll1ll_opy_
  def bstack1111l1ll1_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack1l1ll_opy_ (u"ࠪࡷࡨࡧ࡮ࠨᝈ"),bstack1l1ll_opy_ (u"ࠫࠬᝉ"))
      self.bstack11l1l11l1_opy_ = scripts.get(bstack1l1ll_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩᝊ"),bstack1l1ll_opy_ (u"࠭ࠧᝋ"))
      self.bstack1ll11l11_opy_ = scripts.get(bstack1l1ll_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠫᝌ"),bstack1l1ll_opy_ (u"ࠨࠩᝍ"))
      self.bstack11ll1lllll1_opy_ = scripts.get(bstack1l1ll_opy_ (u"ࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧᝎ"),bstack1l1ll_opy_ (u"ࠪࠫᝏ"))
  def bstack11ll1ll111l_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack11ll11ll1l1_opy_, bstack1l1ll_opy_ (u"ࠫࡼ࠭ᝐ")) as file:
        json.dump({
          bstack1l1ll_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡹࠢᝑ"): self.commands_to_wrap,
          bstack1l1ll_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࡹࠢᝒ"): {
            bstack1l1ll_opy_ (u"ࠢࡴࡥࡤࡲࠧᝓ"): self.perform_scan,
            bstack1l1ll_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧ᝔"): self.bstack11l1l11l1_opy_,
            bstack1l1ll_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾࠨ᝕"): self.bstack1ll11l11_opy_,
            bstack1l1ll_opy_ (u"ࠥࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠣ᝖"): self.bstack11ll1lllll1_opy_
          },
          bstack1l1ll_opy_ (u"ࠦࡳࡵ࡮ࡃࡕࡷࡥࡨࡱࡉ࡯ࡨࡵࡥࡆ࠷࠱ࡺࡅ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠣ᝗"): self.bstack11ll1lll1ll_opy_
        }, file)
    except Exception as e:
      logger.error(bstack1l1ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡹࡵࡲࡪࡰࡪࠤࡨࡵ࡭࡮ࡣࡱࡨࡸࡀࠠࡼࡿࠥ᝘").format(e))
      pass
  def bstack11ll1l1lll_opy_(self, bstack1ll1l1111ll_opy_):
    try:
      return any(command.get(bstack1l1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ᝙")) == bstack1ll1l1111ll_opy_ for command in self.commands_to_wrap)
    except:
      return False
bstack11111lll_opy_ = bstack11ll11lll1l_opy_()