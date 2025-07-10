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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack1ll1l1l1l1_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1ll1llll_opy_ import bstack111ll111_opy_
class bstack1lll1l11_opy_:
  working_dir = os.getcwd()
  bstack1l1l1l1ll_opy_ = False
  config = {}
  bstack11l1111l11l_opy_ = bstack1l1ll_opy_ (u"ࠨࠩḜ")
  binary_path = bstack1l1ll_opy_ (u"ࠩࠪḝ")
  bstack1111ll1l1l1_opy_ = bstack1l1ll_opy_ (u"ࠪࠫḞ")
  bstack1l11111l_opy_ = False
  bstack1111l1l11ll_opy_ = None
  bstack1111l1ll1ll_opy_ = {}
  bstack1111lll1ll1_opy_ = 300
  bstack1111l11l1l1_opy_ = False
  logger = None
  bstack1111ll1llll_opy_ = False
  bstack1111ll11l_opy_ = False
  percy_build_id = None
  bstack1111llllll1_opy_ = bstack1l1ll_opy_ (u"ࠫࠬḟ")
  bstack1111ll11111_opy_ = {
    bstack1l1ll_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬḠ") : 1,
    bstack1l1ll_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧḡ") : 2,
    bstack1l1ll_opy_ (u"ࠧࡦࡦࡪࡩࠬḢ") : 3,
    bstack1l1ll_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨḣ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1111l11l1ll_opy_(self):
    bstack1111llll11l_opy_ = bstack1l1ll_opy_ (u"ࠩࠪḤ")
    bstack1111l11ll1l_opy_ = sys.platform
    bstack1111ll11l1l_opy_ = bstack1l1ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩḥ")
    if re.match(bstack1l1ll_opy_ (u"ࠦࡩࡧࡲࡸ࡫ࡱࢀࡲࡧࡣࠡࡱࡶࠦḦ"), bstack1111l11ll1l_opy_) != None:
      bstack1111llll11l_opy_ = bstack11l1ll1l1l1_opy_ + bstack1l1ll_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡵࡳࡹ࠰ࡽ࡭ࡵࠨḧ")
      self.bstack1111llllll1_opy_ = bstack1l1ll_opy_ (u"࠭࡭ࡢࡥࠪḨ")
    elif re.match(bstack1l1ll_opy_ (u"ࠢ࡮ࡵࡺ࡭ࡳࢂ࡭ࡴࡻࡶࢀࡲ࡯࡮ࡨࡹࡿࡧࡾ࡭ࡷࡪࡰࡿࡦࡨࡩࡷࡪࡰࡿࡻ࡮ࡴࡣࡦࡾࡨࡱࡨࢂࡷࡪࡰ࠶࠶ࠧḩ"), bstack1111l11ll1l_opy_) != None:
      bstack1111llll11l_opy_ = bstack11l1ll1l1l1_opy_ + bstack1l1ll_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮ࡹ࡬ࡲ࠳ࢀࡩࡱࠤḪ")
      bstack1111ll11l1l_opy_ = bstack1l1ll_opy_ (u"ࠤࡳࡩࡷࡩࡹ࠯ࡧࡻࡩࠧḫ")
      self.bstack1111llllll1_opy_ = bstack1l1ll_opy_ (u"ࠪࡻ࡮ࡴࠧḬ")
    else:
      bstack1111llll11l_opy_ = bstack11l1ll1l1l1_opy_ + bstack1l1ll_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡱ࡯࡮ࡶࡺ࠱ࡾ࡮ࡶࠢḭ")
      self.bstack1111llllll1_opy_ = bstack1l1ll_opy_ (u"ࠬࡲࡩ࡯ࡷࡻࠫḮ")
    return bstack1111llll11l_opy_, bstack1111ll11l1l_opy_
  def bstack1111llll111_opy_(self):
    try:
      bstack1111lll1lll_opy_ = [os.path.join(expanduser(bstack1l1ll_opy_ (u"ࠨࡾࠣḯ")), bstack1l1ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧḰ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1111lll1lll_opy_:
        if(self.bstack1111ll1lll1_opy_(path)):
          return path
      raise bstack1l1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧḱ")
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡲࠡࡲࡨࡶࡨࡿࠠࡥࡱࡺࡲࡱࡵࡡࡥ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠭ࠡࡽࢀࠦḲ").format(e))
  def bstack1111ll1lll1_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack111l111l1l1_opy_(self, bstack111l111l111_opy_):
    return os.path.join(bstack111l111l111_opy_, self.bstack11l1111l11l_opy_ + bstack1l1ll_opy_ (u"ࠥ࠲ࡪࡺࡡࡨࠤḳ"))
  def bstack111l1111ll1_opy_(self, bstack111l111l111_opy_, bstack111l1111lll_opy_):
    if not bstack111l1111lll_opy_: return
    try:
      bstack1111l1lll11_opy_ = self.bstack111l111l1l1_opy_(bstack111l111l111_opy_)
      with open(bstack1111l1lll11_opy_, bstack1l1ll_opy_ (u"ࠦࡼࠨḴ")) as f:
        f.write(bstack111l1111lll_opy_)
        self.logger.debug(bstack1l1ll_opy_ (u"࡙ࠧࡡࡷࡧࡧࠤࡳ࡫ࡷࠡࡇࡗࡥ࡬ࠦࡦࡰࡴࠣࡴࡪࡸࡣࡺࠤḵ"))
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡥࡻ࡫ࠠࡵࡪࡨࠤࡪࡺࡡࡨ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨḶ").format(e))
  def bstack1111ll11l11_opy_(self, bstack111l111l111_opy_):
    try:
      bstack1111l1lll11_opy_ = self.bstack111l111l1l1_opy_(bstack111l111l111_opy_)
      if os.path.exists(bstack1111l1lll11_opy_):
        with open(bstack1111l1lll11_opy_, bstack1l1ll_opy_ (u"ࠢࡳࠤḷ")) as f:
          bstack111l1111lll_opy_ = f.read().strip()
          return bstack111l1111lll_opy_ if bstack111l1111lll_opy_ else None
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡ࡮ࡲࡥࡩ࡯࡮ࡨࠢࡈࡘࡦ࡭ࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦḸ").format(e))
  def bstack1111l1l111l_opy_(self, bstack111l111l111_opy_, bstack1111llll11l_opy_):
    bstack111l11111ll_opy_ = self.bstack1111ll11l11_opy_(bstack111l111l111_opy_)
    if bstack111l11111ll_opy_:
      try:
        bstack1111l1ll11l_opy_ = self.bstack1111lll1l1l_opy_(bstack111l11111ll_opy_, bstack1111llll11l_opy_)
        if not bstack1111l1ll11l_opy_:
          self.logger.debug(bstack1l1ll_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡ࡫ࡶࠤࡺࡶࠠࡵࡱࠣࡨࡦࡺࡥࠡࠪࡈࡘࡦ࡭ࠠࡶࡰࡦ࡬ࡦࡴࡧࡦࡦࠬࠦḹ"))
          return True
        self.logger.debug(bstack1l1ll_opy_ (u"ࠥࡒࡪࡽࠠࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡸࡴࡩࡧࡴࡦࠤḺ"))
        return False
      except Exception as e:
        self.logger.warn(bstack1l1ll_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡤࡪࡨࡧࡰࠦࡦࡰࡴࠣࡦ࡮ࡴࡡࡳࡻࠣࡹࡵࡪࡡࡵࡧࡶ࠰ࠥࡻࡳࡪࡰࡪࠤࡪࡾࡩࡴࡶ࡬ࡲ࡬ࠦࡢࡪࡰࡤࡶࡾࡀࠠࡼࡿࠥḻ").format(e))
    return False
  def bstack1111lll1l1l_opy_(self, bstack111l11111ll_opy_, bstack1111llll11l_opy_):
    try:
      headers = {
        bstack1l1ll_opy_ (u"ࠧࡏࡦ࠮ࡐࡲࡲࡪ࠳ࡍࡢࡶࡦ࡬ࠧḼ"): bstack111l11111ll_opy_
      }
      response = bstack1ll1l1l1l1_opy_(bstack1l1ll_opy_ (u"࠭ࡇࡆࡖࠪḽ"), bstack1111llll11l_opy_, {}, {bstack1l1ll_opy_ (u"ࠢࡩࡧࡤࡨࡪࡸࡳࠣḾ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack1l1ll_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡤࡪࡨࡧࡰ࡯࡮ࡨࠢࡩࡳࡷࠦࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡻࡰࡥࡣࡷࡩࡸࡀࠠࡼࡿࠥḿ").format(e))
  @measure(event_name=EVENTS.bstack11l1ll1l1ll_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
  def bstack1111l1lll1l_opy_(self, bstack1111llll11l_opy_, bstack1111ll11l1l_opy_):
    try:
      bstack1111l1l11l1_opy_ = self.bstack1111llll111_opy_()
      bstack1111l11llll_opy_ = os.path.join(bstack1111l1l11l1_opy_, bstack1l1ll_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯ࡼ࡬ࡴࠬṀ"))
      bstack1111lllllll_opy_ = os.path.join(bstack1111l1l11l1_opy_, bstack1111ll11l1l_opy_)
      if self.bstack1111l1l111l_opy_(bstack1111l1l11l1_opy_, bstack1111llll11l_opy_): # if bstack111l11111l1_opy_, bstack1l1l11lll1l_opy_ bstack111l1111lll_opy_ is bstack1111l11ll11_opy_ to bstack11l11lllll1_opy_ version available (response 304)
        if os.path.exists(bstack1111lllllll_opy_):
          self.logger.info(bstack1l1ll_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡵ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧṁ").format(bstack1111lllllll_opy_))
          return bstack1111lllllll_opy_
        if os.path.exists(bstack1111l11llll_opy_):
          self.logger.info(bstack1l1ll_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡾ࡮ࡶࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡾࢁ࠱ࠦࡵ࡯ࡼ࡬ࡴࡵ࡯࡮ࡨࠤṂ").format(bstack1111l11llll_opy_))
          return self.bstack1111lllll11_opy_(bstack1111l11llll_opy_, bstack1111ll11l1l_opy_)
      self.logger.info(bstack1l1ll_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳࠠࡼࡿࠥṃ").format(bstack1111llll11l_opy_))
      response = bstack1ll1l1l1l1_opy_(bstack1l1ll_opy_ (u"࠭ࡇࡆࡖࠪṄ"), bstack1111llll11l_opy_, {}, {})
      if response.status_code == 200:
        bstack1111lllll1l_opy_ = response.headers.get(bstack1l1ll_opy_ (u"ࠢࡆࡖࡤ࡫ࠧṅ"), bstack1l1ll_opy_ (u"ࠣࠤṆ"))
        if bstack1111lllll1l_opy_:
          self.bstack111l1111ll1_opy_(bstack1111l1l11l1_opy_, bstack1111lllll1l_opy_)
        with open(bstack1111l11llll_opy_, bstack1l1ll_opy_ (u"ࠩࡺࡦࠬṇ")) as file:
          file.write(response.content)
        self.logger.info(bstack1l1ll_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡡ࡯ࡦࠣࡷࡦࡼࡥࡥࠢࡤࡸࠥࢁࡽࠣṈ").format(bstack1111l11llll_opy_))
        return self.bstack1111lllll11_opy_(bstack1111l11llll_opy_, bstack1111ll11l1l_opy_)
      else:
        raise(bstack1l1ll_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡷ࡬ࡪࠦࡦࡪ࡮ࡨ࠲࡙ࠥࡴࡢࡶࡸࡷࠥࡩ࡯ࡥࡧ࠽ࠤࢀࢃࠢṉ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺ࠼ࠣࡿࢂࠨṊ").format(e))
  def bstack1111ll11ll1_opy_(self, bstack1111llll11l_opy_, bstack1111ll11l1l_opy_):
    try:
      retry = 2
      bstack1111lllllll_opy_ = None
      bstack1111l1ll1l1_opy_ = False
      while retry > 0:
        bstack1111lllllll_opy_ = self.bstack1111l1lll1l_opy_(bstack1111llll11l_opy_, bstack1111ll11l1l_opy_)
        bstack1111l1ll1l1_opy_ = self.bstack1111llll1ll_opy_(bstack1111llll11l_opy_, bstack1111ll11l1l_opy_, bstack1111lllllll_opy_)
        if bstack1111l1ll1l1_opy_:
          break
        retry -= 1
      return bstack1111lllllll_opy_, bstack1111l1ll1l1_opy_
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡹࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥࡶࡡࡵࡪࠥṋ").format(e))
    return bstack1111lllllll_opy_, False
  def bstack1111llll1ll_opy_(self, bstack1111llll11l_opy_, bstack1111ll11l1l_opy_, bstack1111lllllll_opy_, bstack111l111111l_opy_ = 0):
    if bstack111l111111l_opy_ > 1:
      return False
    if bstack1111lllllll_opy_ == None or os.path.exists(bstack1111lllllll_opy_) == False:
      self.logger.warn(bstack1l1ll_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠬࠡࡴࡨࡸࡷࡿࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧṌ"))
      return False
    bstack111l111l1ll_opy_ = bstack1l1ll_opy_ (u"ࡳࠤࡡ࠲࠯ࡆࡰࡦࡴࡦࡽ࠴ࡩ࡬ࡪࠢ࡟ࡨ࠰ࡢ࠮࡝ࡦ࠮ࡠ࠳ࡢࡤࠬࠤṍ")
    command = bstack1l1ll_opy_ (u"ࠩࡾࢁࠥ࠳࠭ࡷࡧࡵࡷ࡮ࡵ࡮ࠨṎ").format(bstack1111lllllll_opy_)
    bstack111l1111111_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack111l111l1ll_opy_, bstack111l1111111_opy_) != None:
      return True
    else:
      self.logger.error(bstack1l1ll_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡹࡩࡷࡹࡩࡰࡰࠣࡧ࡭࡫ࡣ࡬ࠢࡩࡥ࡮ࡲࡥࡥࠤṏ"))
      return False
  def bstack1111lllll11_opy_(self, bstack1111l11llll_opy_, bstack1111ll11l1l_opy_):
    try:
      working_dir = os.path.dirname(bstack1111l11llll_opy_)
      shutil.unpack_archive(bstack1111l11llll_opy_, working_dir)
      bstack1111lllllll_opy_ = os.path.join(working_dir, bstack1111ll11l1l_opy_)
      os.chmod(bstack1111lllllll_opy_, 0o755)
      return bstack1111lllllll_opy_
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡶࡰࡽ࡭ࡵࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠧṐ"))
  def bstack1111ll1ll1l_opy_(self):
    try:
      bstack1111l1l1ll1_opy_ = self.config.get(bstack1l1ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫṑ"))
      bstack1111ll1ll1l_opy_ = bstack1111l1l1ll1_opy_ or (bstack1111l1l1ll1_opy_ is None and self.bstack1l1l1l1ll_opy_)
      if not bstack1111ll1ll1l_opy_ or self.config.get(bstack1l1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩṒ"), None) not in bstack11l1ll1l11l_opy_:
        return False
      self.bstack1l11111l_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡪࡺࡥࡤࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤṓ").format(e))
  def bstack1111ll11lll_opy_(self):
    try:
      bstack1111ll11lll_opy_ = self.percy_capture_mode
      return bstack1111ll11lll_opy_
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡥࡷࠤࡵ࡫ࡲࡤࡻࠣࡧࡦࡶࡴࡶࡴࡨࠤࡲࡵࡤࡦ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤṔ").format(e))
  def init(self, bstack1l1l1l1ll_opy_, config, logger):
    self.bstack1l1l1l1ll_opy_ = bstack1l1l1l1ll_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1111ll1ll1l_opy_():
      return
    self.bstack1111l1ll1ll_opy_ = config.get(bstack1l1ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࡐࡲࡷ࡭ࡴࡴࡳࠨṕ"), {})
    self.percy_capture_mode = config.get(bstack1l1ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࡅࡤࡴࡹࡻࡲࡦࡏࡲࡨࡪ࠭Ṗ"))
    try:
      bstack1111llll11l_opy_, bstack1111ll11l1l_opy_ = self.bstack1111l11l1ll_opy_()
      self.bstack11l1111l11l_opy_ = bstack1111ll11l1l_opy_
      bstack1111lllllll_opy_, bstack1111l1ll1l1_opy_ = self.bstack1111ll11ll1_opy_(bstack1111llll11l_opy_, bstack1111ll11l1l_opy_)
      if bstack1111l1ll1l1_opy_:
        self.binary_path = bstack1111lllllll_opy_
        thread = Thread(target=self.bstack1111l1lllll_opy_)
        thread.start()
      else:
        self.bstack1111ll1llll_opy_ = True
        self.logger.error(bstack1l1ll_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡶࡥࡳࡥࡼࠤࡵࡧࡴࡩࠢࡩࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡓࡩࡷࡩࡹࠣṗ").format(bstack1111lllllll_opy_))
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨṘ").format(e))
  def bstack1111l1l1lll_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1l1ll_opy_ (u"࠭࡬ࡰࡩࠪṙ"), bstack1l1ll_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠴࡬ࡰࡩࠪṚ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1l1ll_opy_ (u"ࠣࡒࡸࡷ࡭࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡ࡮ࡲ࡫ࡸࠦࡡࡵࠢࡾࢁࠧṛ").format(logfile))
      self.bstack1111ll1l1l1_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡥࡵࠢࡳࡩࡷࡩࡹࠡ࡮ࡲ࡫ࠥࡶࡡࡵࡪ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥṜ").format(e))
  @measure(event_name=EVENTS.bstack11l1lll11ll_opy_, stage=STAGE.bstack11ll1l11ll_opy_)
  def bstack1111l1lllll_opy_(self):
    bstack1111l1ll111_opy_ = self.bstack111l1111l11_opy_()
    if bstack1111l1ll111_opy_ == None:
      self.bstack1111ll1llll_opy_ = True
      self.logger.error(bstack1l1ll_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡷࡳࡰ࡫࡮ࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧ࠰ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾࠨṝ"))
      return False
    command_args = [bstack1l1ll_opy_ (u"ࠦࡦࡶࡰ࠻ࡧࡻࡩࡨࡀࡳࡵࡣࡵࡸࠧṞ") if self.bstack1l1l1l1ll_opy_ else bstack1l1ll_opy_ (u"ࠬ࡫ࡸࡦࡥ࠽ࡷࡹࡧࡲࡵࠩṟ")]
    bstack111ll111111_opy_ = self.bstack1111lll111l_opy_()
    if bstack111ll111111_opy_ != None:
      command_args.append(bstack1l1ll_opy_ (u"ࠨ࠭ࡤࠢࡾࢁࠧṠ").format(bstack111ll111111_opy_))
    env = os.environ.copy()
    env[bstack1l1ll_opy_ (u"ࠢࡑࡇࡕࡇ࡞ࡥࡔࡐࡍࡈࡒࠧṡ")] = bstack1111l1ll111_opy_
    env[bstack1l1ll_opy_ (u"ࠣࡖࡋࡣࡇ࡛ࡉࡍࡆࡢ࡙࡚ࡏࡄࠣṢ")] = os.environ.get(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧṣ"), bstack1l1ll_opy_ (u"ࠪࠫṤ"))
    bstack1111ll1ll11_opy_ = [self.binary_path]
    self.bstack1111l1l1lll_opy_()
    self.bstack1111l1l11ll_opy_ = self.bstack1111ll1111l_opy_(bstack1111ll1ll11_opy_ + command_args, env)
    self.logger.debug(bstack1l1ll_opy_ (u"ࠦࡘࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠧṥ"))
    bstack111l111111l_opy_ = 0
    while self.bstack1111l1l11ll_opy_.poll() == None:
      bstack1111lll11l1_opy_ = self.bstack1111lll11ll_opy_()
      if bstack1111lll11l1_opy_:
        self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬ࠣṦ"))
        self.bstack1111l11l1l1_opy_ = True
        return True
      bstack111l111111l_opy_ += 1
      self.logger.debug(bstack1l1ll_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡘࡥࡵࡴࡼࠤ࠲ࠦࡻࡾࠤṧ").format(bstack111l111111l_opy_))
      time.sleep(2)
    self.logger.error(bstack1l1ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡣࡩࡸࡪࡸࠠࡼࡿࠣࡥࡹࡺࡥ࡮ࡲࡷࡷࠧṨ").format(bstack111l111111l_opy_))
    self.bstack1111ll1llll_opy_ = True
    return False
  def bstack1111lll11ll_opy_(self, bstack111l111111l_opy_ = 0):
    if bstack111l111111l_opy_ > 10:
      return False
    try:
      bstack1111ll1l1ll_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠨࡒࡈࡖࡈ࡟࡟ࡔࡇࡕ࡚ࡊࡘ࡟ࡂࡆࡇࡖࡊ࡙ࡓࠨṩ"), bstack1l1ll_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱࡯ࡳࡨࡧ࡬ࡩࡱࡶࡸ࠿࠻࠳࠴࠺ࠪṪ"))
      bstack1111ll1l11l_opy_ = bstack1111ll1l1ll_opy_ + bstack11ll1111111_opy_
      response = requests.get(bstack1111ll1l11l_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack1l1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࠩṫ"), {}).get(bstack1l1ll_opy_ (u"ࠫ࡮ࡪࠧṬ"), None)
      return True
    except:
      self.logger.debug(bstack1l1ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡵࡩࡩࠦࡷࡩ࡫࡯ࡩࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡲࡴࡩࠢࡦ࡬ࡪࡩ࡫ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥṭ"))
      return False
  def bstack111l1111l11_opy_(self):
    bstack1111l1l1l1l_opy_ = bstack1l1ll_opy_ (u"࠭ࡡࡱࡲࠪṮ") if self.bstack1l1l1l1ll_opy_ else bstack1l1ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩṯ")
    bstack1111l1l1111_opy_ = bstack1l1ll_opy_ (u"ࠣࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧࠦṰ") if self.config.get(bstack1l1ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨṱ")) is None else True
    bstack11ll11ll11l_opy_ = bstack1l1ll_opy_ (u"ࠥࡥࡵ࡯࠯ࡢࡲࡳࡣࡵ࡫ࡲࡤࡻ࠲࡫ࡪࡺ࡟ࡱࡴࡲ࡮ࡪࡩࡴࡠࡶࡲ࡯ࡪࡴ࠿࡯ࡣࡰࡩࡂࢁࡽࠧࡶࡼࡴࡪࡃࡻࡾࠨࡳࡩࡷࡩࡹ࠾ࡽࢀࠦṲ").format(self.config[bstack1l1ll_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩṳ")], bstack1111l1l1l1l_opy_, bstack1111l1l1111_opy_)
    if self.percy_capture_mode:
      bstack11ll11ll11l_opy_ += bstack1l1ll_opy_ (u"ࠧࠬࡰࡦࡴࡦࡽࡤࡩࡡࡱࡶࡸࡶࡪࡥ࡭ࡰࡦࡨࡁࢀࢃࠢṴ").format(self.percy_capture_mode)
    uri = bstack111ll111_opy_(bstack11ll11ll11l_opy_)
    try:
      response = bstack1ll1l1l1l1_opy_(bstack1l1ll_opy_ (u"࠭ࡇࡆࡖࠪṵ"), uri, {}, {bstack1l1ll_opy_ (u"ࠧࡢࡷࡷ࡬ࠬṶ"): (self.config[bstack1l1ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪṷ")], self.config[bstack1l1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬṸ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1l11111l_opy_ = data.get(bstack1l1ll_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫṹ"))
        self.percy_capture_mode = data.get(bstack1l1ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡢࡧࡦࡶࡴࡶࡴࡨࡣࡲࡵࡤࡦࠩṺ"))
        os.environ[bstack1l1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࠪṻ")] = str(self.bstack1l11111l_opy_)
        os.environ[bstack1l1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪṼ")] = str(self.percy_capture_mode)
        if bstack1111l1l1111_opy_ == bstack1l1ll_opy_ (u"ࠢࡶࡰࡧࡩ࡫࡯࡮ࡦࡦࠥṽ") and str(self.bstack1l11111l_opy_).lower() == bstack1l1ll_opy_ (u"ࠣࡶࡵࡹࡪࠨṾ"):
          self.bstack1111ll11l_opy_ = True
        if bstack1l1ll_opy_ (u"ࠤࡷࡳࡰ࡫࡮ࠣṿ") in data:
          return data[bstack1l1ll_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤẀ")]
        else:
          raise bstack1l1ll_opy_ (u"࡙ࠫࡵ࡫ࡦࡰࠣࡒࡴࡺࠠࡇࡱࡸࡲࡩࠦ࠭ࠡࡽࢀࠫẁ").format(data)
      else:
        raise bstack1l1ll_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡱࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲ࠱ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡵࡷࡥࡹࡻࡳࠡ࠯ࠣࡿࢂ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡅࡳࡩࡿࠠ࠮ࠢࡾࢁࠧẂ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦࡰࡳࡱ࡭ࡩࡨࡺࠢẃ").format(e))
  def bstack1111lll111l_opy_(self):
    bstack1111ll111ll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1ll_opy_ (u"ࠢࡱࡧࡵࡧࡾࡉ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠥẄ"))
    try:
      if bstack1l1ll_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩẅ") not in self.bstack1111l1ll1ll_opy_:
        self.bstack1111l1ll1ll_opy_[bstack1l1ll_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪẆ")] = 2
      with open(bstack1111ll111ll_opy_, bstack1l1ll_opy_ (u"ࠪࡻࠬẇ")) as fp:
        json.dump(self.bstack1111l1ll1ll_opy_, fp)
      return bstack1111ll111ll_opy_
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡤࡴࡨࡥࡹ࡫ࠠࡱࡧࡵࡧࡾࠦࡣࡰࡰࡩ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦẈ").format(e))
  def bstack1111ll1111l_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1111llllll1_opy_ == bstack1l1ll_opy_ (u"ࠬࡽࡩ࡯ࠩẉ"):
        bstack111l1111l1l_opy_ = [bstack1l1ll_opy_ (u"࠭ࡣ࡮ࡦ࠱ࡩࡽ࡫ࠧẊ"), bstack1l1ll_opy_ (u"ࠧ࠰ࡥࠪẋ")]
        cmd = bstack111l1111l1l_opy_ + cmd
      cmd = bstack1l1ll_opy_ (u"ࠨࠢࠪẌ").join(cmd)
      self.logger.debug(bstack1l1ll_opy_ (u"ࠤࡕࡹࡳࡴࡩ࡯ࡩࠣࡿࢂࠨẍ").format(cmd))
      with open(self.bstack1111ll1l1l1_opy_, bstack1l1ll_opy_ (u"ࠥࡥࠧẎ")) as bstack1111l1l1l11_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1111l1l1l11_opy_, text=True, stderr=bstack1111l1l1l11_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1111ll1llll_opy_ = True
      self.logger.error(bstack1l1ll_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽࠥࡽࡩࡵࡪࠣࡧࡲࡪࠠ࠮ࠢࡾࢁ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂࠨẏ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1111l11l1l1_opy_:
        self.logger.info(bstack1l1ll_opy_ (u"࡙ࠧࡴࡰࡲࡳ࡭ࡳ࡭ࠠࡑࡧࡵࡧࡾࠨẐ"))
        cmd = [self.binary_path, bstack1l1ll_opy_ (u"ࠨࡥࡹࡧࡦ࠾ࡸࡺ࡯ࡱࠤẑ")]
        self.bstack1111ll1111l_opy_(cmd)
        self.bstack1111l11l1l1_opy_ = False
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡵࡰࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡤࡱࡰࡱࡦࡴࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢẒ").format(cmd, e))
  def bstack1llll1l1ll_opy_(self):
    if not self.bstack1l11111l_opy_:
      return
    try:
      bstack1111lll1l11_opy_ = 0
      while not self.bstack1111l11l1l1_opy_ and bstack1111lll1l11_opy_ < self.bstack1111lll1ll1_opy_:
        if self.bstack1111ll1llll_opy_:
          self.logger.info(bstack1l1ll_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡴࡧࡷࡹࡵࠦࡦࡢ࡫࡯ࡩࡩࠨẓ"))
          return
        time.sleep(1)
        bstack1111lll1l11_opy_ += 1
      os.environ[bstack1l1ll_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡄࡈࡗ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࠨẔ")] = str(self.bstack1111ll1l111_opy_())
      self.logger.info(bstack1l1ll_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡥࡲࡱࡵࡲࡥࡵࡧࡧࠦẕ"))
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࡹࡵࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧẖ").format(e))
  def bstack1111ll1l111_opy_(self):
    if self.bstack1l1l1l1ll_opy_:
      return
    try:
      bstack1111l11lll1_opy_ = [platform[bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪẗ")].lower() for platform in self.config.get(bstack1l1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩẘ"), [])]
      bstack1111l1llll1_opy_ = sys.maxsize
      bstack1111ll111l1_opy_ = bstack1l1ll_opy_ (u"ࠧࠨẙ")
      for browser in bstack1111l11lll1_opy_:
        if browser in self.bstack1111ll11111_opy_:
          bstack1111llll1l1_opy_ = self.bstack1111ll11111_opy_[browser]
        if bstack1111llll1l1_opy_ < bstack1111l1llll1_opy_:
          bstack1111l1llll1_opy_ = bstack1111llll1l1_opy_
          bstack1111ll111l1_opy_ = browser
      return bstack1111ll111l1_opy_
    except Exception as e:
      self.logger.error(bstack1l1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡥࡩࡸࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤẚ").format(e))
  @classmethod
  def bstack1111ll1ll_opy_(self):
    return os.getenv(bstack1l1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧẛ"), bstack1l1ll_opy_ (u"ࠪࡊࡦࡲࡳࡦࠩẜ")).lower()
  @classmethod
  def bstack11ll1ll1l_opy_(self):
    return os.getenv(bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࡡࡆࡅࡕ࡚ࡕࡓࡇࡢࡑࡔࡊࡅࠨẝ"), bstack1l1ll_opy_ (u"ࠬ࠭ẞ"))
  @classmethod
  def bstack1l1l1l11lll_opy_(cls, value):
    cls.bstack1111ll11l_opy_ = value
  @classmethod
  def bstack1111lll1111_opy_(cls):
    return cls.bstack1111ll11l_opy_
  @classmethod
  def bstack1l1l1l1ll1l_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack111l111l11l_opy_(cls):
    return cls.percy_build_id