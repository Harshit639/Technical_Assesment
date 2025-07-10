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
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l1lllll_opy_, bstack11l1ll1llll_opy_, bstack11l1llll11l_opy_
import tempfile
import json
bstack111l1llll1l_opy_ = os.getenv(bstack1l1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡋࡤࡌࡉࡍࡇࠥᵒ"), None) or os.path.join(tempfile.gettempdir(), bstack1l1ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡧࡩࡧࡻࡧ࠯࡮ࡲ࡫ࠧᵓ"))
bstack111ll1111ll_opy_ = os.path.join(bstack1l1ll_opy_ (u"ࠦࡱࡵࡧࠣᵔ"), bstack1l1ll_opy_ (u"ࠬࡹࡤ࡬࠯ࡦࡰ࡮࠳ࡤࡦࡤࡸ࡫࠳ࡲ࡯ࡨࠩᵕ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack1l1ll_opy_ (u"࠭ࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩᵖ"),
      datefmt=bstack1l1ll_opy_ (u"࡛ࠧࠦ࠰ࠩࡲ࠳ࠥࡥࡖࠨࡌ࠿ࠫࡍ࠻ࠧࡖ࡞ࠬᵗ"),
      stream=sys.stdout
    )
  return logger
def bstack1ll1llll1l1_opy_():
  bstack111ll1111l1_opy_ = os.environ.get(bstack1l1ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡅࡇࡅ࡙ࡌࠨᵘ"), bstack1l1ll_opy_ (u"ࠤࡩࡥࡱࡹࡥࠣᵙ"))
  return logging.DEBUG if bstack111ll1111l1_opy_.lower() == bstack1l1ll_opy_ (u"ࠥࡸࡷࡻࡥࠣᵚ") else logging.INFO
def bstack1l1ll11lll1_opy_():
  global bstack111l1llll1l_opy_
  if os.path.exists(bstack111l1llll1l_opy_):
    os.remove(bstack111l1llll1l_opy_)
  if os.path.exists(bstack111ll1111ll_opy_):
    os.remove(bstack111ll1111ll_opy_)
def bstack1ll1l11ll1_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def bstack1lll1l1ll_opy_(config, log_level):
  bstack111ll11llll_opy_ = log_level
  if bstack1l1ll_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ᵛ") in config and config[bstack1l1ll_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧᵜ")] in bstack11l1ll1llll_opy_:
    bstack111ll11llll_opy_ = bstack11l1ll1llll_opy_[config[bstack1l1ll_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨᵝ")]]
  if config.get(bstack1l1ll_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩᵞ"), False):
    logging.getLogger().setLevel(bstack111ll11llll_opy_)
    return bstack111ll11llll_opy_
  global bstack111l1llll1l_opy_
  bstack1ll1l11ll1_opy_()
  bstack111ll1l11ll_opy_ = logging.Formatter(
    fmt=bstack1l1ll_opy_ (u"ࠨࠧࠫࡥࡸࡩࡴࡪ࡯ࡨ࠭ࡸ࡛ࠦࠦࠪࡱࡥࡲ࡫ࠩࡴ࡟࡞ࠩ࠭ࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠪࡵࡠࠤ࠲ࠦࠥࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࡶࠫᵟ"),
    datefmt=bstack1l1ll_opy_ (u"ࠩࠨ࡝࠲ࠫ࡭࠮ࠧࡧࡘࠪࡎ࠺ࠦࡏ࠽ࠩࡘࡠࠧᵠ"),
  )
  bstack111ll111lll_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack111l1llll1l_opy_)
  file_handler.setFormatter(bstack111ll1l11ll_opy_)
  bstack111ll111lll_opy_.setFormatter(bstack111ll1l11ll_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack111ll111lll_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack1l1ll_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲ࠯ࡴࡨࡱࡴࡺࡥ࠯ࡴࡨࡱࡴࡺࡥࡠࡥࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲࠬᵡ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack111ll111lll_opy_.setLevel(bstack111ll11llll_opy_)
  logging.getLogger().addHandler(bstack111ll111lll_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack111ll11llll_opy_
def bstack111l1lllll1_opy_(config):
  try:
    bstack111ll1l1111_opy_ = set(bstack11l1llll11l_opy_)
    bstack111ll1l11l1_opy_ = bstack1l1ll_opy_ (u"ࠫࠬᵢ")
    with open(bstack1l1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨᵣ")) as bstack111ll111ll1_opy_:
      bstack111ll11l1ll_opy_ = bstack111ll111ll1_opy_.read()
      bstack111ll1l11l1_opy_ = re.sub(bstack1l1ll_opy_ (u"ࡸࠧ࡟ࠪ࡟ࡷ࠰࠯࠿ࠤ࠰࠭ࠨࡡࡴࠧᵤ"), bstack1l1ll_opy_ (u"ࠧࠨᵥ"), bstack111ll11l1ll_opy_, flags=re.M)
      bstack111ll1l11l1_opy_ = re.sub(
        bstack1l1ll_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠫࠫᵦ") + bstack1l1ll_opy_ (u"ࠩࡿࠫᵧ").join(bstack111ll1l1111_opy_) + bstack1l1ll_opy_ (u"ࠪ࠭࠳࠰ࠤࠨᵨ"),
        bstack1l1ll_opy_ (u"ࡶࠬࡢ࠲࠻ࠢ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭ᵩ"),
        bstack111ll1l11l1_opy_, flags=re.M | re.I
      )
    def bstack111ll11ll11_opy_(dic):
      bstack111ll11ll1l_opy_ = {}
      for key, value in dic.items():
        if key in bstack111ll1l1111_opy_:
          bstack111ll11ll1l_opy_[key] = bstack1l1ll_opy_ (u"ࠬࡡࡒࡆࡆࡄࡇ࡙ࡋࡄ࡞ࠩᵪ")
        else:
          if isinstance(value, dict):
            bstack111ll11ll1l_opy_[key] = bstack111ll11ll11_opy_(value)
          else:
            bstack111ll11ll1l_opy_[key] = value
      return bstack111ll11ll1l_opy_
    bstack111ll11ll1l_opy_ = bstack111ll11ll11_opy_(config)
    return {
      bstack1l1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩᵫ"): bstack111ll1l11l1_opy_,
      bstack1l1ll_opy_ (u"ࠧࡧ࡫ࡱࡥࡱࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪᵬ"): json.dumps(bstack111ll11ll1l_opy_)
    }
  except Exception as e:
    return {}
def bstack111ll11lll1_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack1l1ll_opy_ (u"ࠨ࡮ࡲ࡫ࠬᵭ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack111ll111111_opy_ = os.path.join(log_dir, bstack1l1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵࠪᵮ"))
  if not os.path.exists(bstack111ll111111_opy_):
    bstack111ll11l11l_opy_ = {
      bstack1l1ll_opy_ (u"ࠥ࡭ࡳ࡯ࡰࡢࡶ࡫ࠦᵯ"): str(inipath),
      bstack1l1ll_opy_ (u"ࠦࡷࡵ࡯ࡵࡲࡤࡸ࡭ࠨᵰ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack1l1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫᵱ")), bstack1l1ll_opy_ (u"࠭ࡷࠨᵲ")) as bstack111ll11l1l1_opy_:
      bstack111ll11l1l1_opy_.write(json.dumps(bstack111ll11l11l_opy_))
def bstack111ll11l111_opy_():
  try:
    bstack111ll111111_opy_ = os.path.join(os.getcwd(), bstack1l1ll_opy_ (u"ࠧ࡭ࡱࡪࠫᵳ"), bstack1l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴ࠰࡭ࡷࡴࡴࠧᵴ"))
    if os.path.exists(bstack111ll111111_opy_):
      with open(bstack111ll111111_opy_, bstack1l1ll_opy_ (u"ࠩࡵࠫᵵ")) as bstack111ll11l1l1_opy_:
        bstack111ll11111l_opy_ = json.load(bstack111ll11l1l1_opy_)
      return bstack111ll11111l_opy_.get(bstack1l1ll_opy_ (u"ࠪ࡭ࡳ࡯ࡰࡢࡶ࡫ࠫᵶ"), bstack1l1ll_opy_ (u"ࠫࠬᵷ")), bstack111ll11111l_opy_.get(bstack1l1ll_opy_ (u"ࠬࡸ࡯ࡰࡶࡳࡥࡹ࡮ࠧᵸ"), bstack1l1ll_opy_ (u"࠭ࠧᵹ"))
  except:
    pass
  return None, None
def bstack111ll111l11_opy_():
  try:
    bstack111ll111111_opy_ = os.path.join(os.getcwd(), bstack1l1ll_opy_ (u"ࠧ࡭ࡱࡪࠫᵺ"), bstack1l1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴ࠰࡭ࡷࡴࡴࠧᵻ"))
    if os.path.exists(bstack111ll111111_opy_):
      os.remove(bstack111ll111111_opy_)
  except:
    pass
def bstack11l1l1lll1_opy_(config):
  try:
    from bstack_utils.helper import bstack11l1lll1_opy_, bstack1lll1ll1ll_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack111l1llll1l_opy_
    if config.get(bstack1l1ll_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫᵼ"), False):
      return
    uuid = os.getenv(bstack1l1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᵽ")) if os.getenv(bstack1l1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᵾ")) else bstack11l1lll1_opy_.get_property(bstack1l1ll_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢᵿ"))
    if not uuid or uuid == bstack1l1ll_opy_ (u"࠭࡮ࡶ࡮࡯ࠫᶀ"):
      return
    bstack111l1llllll_opy_ = [bstack1l1ll_opy_ (u"ࠧࡳࡧࡴࡹ࡮ࡸࡥ࡮ࡧࡱࡸࡸ࠴ࡴࡹࡶࠪᶁ"), bstack1l1ll_opy_ (u"ࠨࡒ࡬ࡴ࡫࡯࡬ࡦࠩᶂ"), bstack1l1ll_opy_ (u"ࠩࡳࡽࡵࡸ࡯࡫ࡧࡦࡸ࠳ࡺ࡯࡮࡮ࠪᶃ"), bstack111l1llll1l_opy_, bstack111ll1111ll_opy_]
    bstack111l1llll11_opy_, root_path = bstack111ll11l111_opy_()
    if bstack111l1llll11_opy_ != None:
      bstack111l1llllll_opy_.append(bstack111l1llll11_opy_)
    if root_path != None:
      bstack111l1llllll_opy_.append(os.path.join(root_path, bstack1l1ll_opy_ (u"ࠪࡧࡴࡴࡦࡵࡧࡶࡸ࠳ࡶࡹࠨᶄ")))
    bstack1ll1l11ll1_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack1l1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠱ࡱࡵࡧࡴ࠯ࠪᶅ") + uuid + bstack1l1ll_opy_ (u"ࠬ࠴ࡴࡢࡴ࠱࡫ࡿ࠭ᶆ"))
    with tarfile.open(output_file, bstack1l1ll_opy_ (u"ࠨࡷ࠻ࡩࡽࠦᶇ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack111l1llllll_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack111l1lllll1_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack111ll1l111l_opy_ = data.encode()
        tarinfo.size = len(bstack111ll1l111l_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack111ll1l111l_opy_))
    bstack11l11l1ll1_opy_ = MultipartEncoder(
      fields= {
        bstack1l1ll_opy_ (u"ࠧࡥࡣࡷࡥࠬᶈ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack1l1ll_opy_ (u"ࠨࡴࡥࠫᶉ")), bstack1l1ll_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯ࡹ࠯ࡪࡾ࡮ࡶࠧᶊ")),
        bstack1l1ll_opy_ (u"ࠪࡧࡱ࡯ࡥ࡯ࡶࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬᶋ"): uuid
      }
    )
    bstack111ll111l1l_opy_ = bstack1lll1ll1ll_opy_(cli.config, [bstack1l1ll_opy_ (u"ࠦࡦࡶࡩࡴࠤᶌ"), bstack1l1ll_opy_ (u"ࠧࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠧᶍ"), bstack1l1ll_opy_ (u"ࠨࡵࡱ࡮ࡲࡥࡩࠨᶎ")], bstack11l1l1lllll_opy_)
    response = requests.post(
      bstack1l1ll_opy_ (u"ࠢࡼࡿ࠲ࡧࡱ࡯ࡥ࡯ࡶ࠰ࡰࡴ࡭ࡳ࠰ࡷࡳࡰࡴࡧࡤࠣᶏ").format(bstack111ll111l1l_opy_),
      data=bstack11l11l1ll1_opy_,
      headers={bstack1l1ll_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧᶐ"): bstack11l11l1ll1_opy_.content_type},
      auth=(config[bstack1l1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᶑ")], config[bstack1l1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᶒ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack1l1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡹࡵࡲ࡯ࡢࡦࠣࡰࡴ࡭ࡳ࠻ࠢࠪᶓ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack1l1ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸ࡫࡮ࡥ࡫ࡱ࡫ࠥࡲ࡯ࡨࡵ࠽ࠫᶔ") + str(e))
  finally:
    try:
      bstack1l1ll11lll1_opy_()
      bstack111ll111l11_opy_()
    except:
      pass