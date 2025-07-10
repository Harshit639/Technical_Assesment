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
from _pytest import fixtures
from _pytest.python import _call_with_optional_argument
from pytest import Module, Class
from bstack_utils.helper import Result, bstack11l111l111l_opy_
from browserstack_sdk.bstack11l1ll111_opy_ import bstack1lll1111_opy_
def _111ll1l1lll_opy_(method, this, arg):
    arg_count = method.__code__.co_argcount
    if arg_count > 1:
        method(this, arg)
    else:
        method(this)
class bstack111lll11111_opy_:
    def __init__(self, handler):
        self._111ll1l1l11_opy_ = {}
        self._111ll1ll11l_opy_ = {}
        self.handler = handler
        self.patch()
        pass
    def patch(self):
        pytest_version = bstack1lll1111_opy_.version()
        if bstack11l111l111l_opy_(pytest_version, bstack1l1ll_opy_ (u"ࠣ࠺࠱࠵࠳࠷ࠢᴧ")) >= 0:
            self._111ll1l1l11_opy_[bstack1l1ll_opy_ (u"ࠩࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᴨ")] = Module._register_setup_function_fixture
            self._111ll1l1l11_opy_[bstack1l1ll_opy_ (u"ࠪࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᴩ")] = Module._register_setup_module_fixture
            self._111ll1l1l11_opy_[bstack1l1ll_opy_ (u"ࠫࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᴪ")] = Class._register_setup_class_fixture
            self._111ll1l1l11_opy_[bstack1l1ll_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᴫ")] = Class._register_setup_method_fixture
            Module._register_setup_function_fixture = self.bstack111ll1llll1_opy_(bstack1l1ll_opy_ (u"࠭ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᴬ"))
            Module._register_setup_module_fixture = self.bstack111ll1llll1_opy_(bstack1l1ll_opy_ (u"ࠧ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᴭ"))
            Class._register_setup_class_fixture = self.bstack111ll1llll1_opy_(bstack1l1ll_opy_ (u"ࠨࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᴮ"))
            Class._register_setup_method_fixture = self.bstack111ll1llll1_opy_(bstack1l1ll_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᴯ"))
        else:
            self._111ll1l1l11_opy_[bstack1l1ll_opy_ (u"ࠪࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᴰ")] = Module._inject_setup_function_fixture
            self._111ll1l1l11_opy_[bstack1l1ll_opy_ (u"ࠫࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᴱ")] = Module._inject_setup_module_fixture
            self._111ll1l1l11_opy_[bstack1l1ll_opy_ (u"ࠬࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᴲ")] = Class._inject_setup_class_fixture
            self._111ll1l1l11_opy_[bstack1l1ll_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᴳ")] = Class._inject_setup_method_fixture
            Module._inject_setup_function_fixture = self.bstack111ll1llll1_opy_(bstack1l1ll_opy_ (u"ࠧࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᴴ"))
            Module._inject_setup_module_fixture = self.bstack111ll1llll1_opy_(bstack1l1ll_opy_ (u"ࠨ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᴵ"))
            Class._inject_setup_class_fixture = self.bstack111ll1llll1_opy_(bstack1l1ll_opy_ (u"ࠩࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᴶ"))
            Class._inject_setup_method_fixture = self.bstack111ll1llll1_opy_(bstack1l1ll_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᴷ"))
    def bstack111ll1lll1l_opy_(self, bstack111ll1lllll_opy_, hook_type):
        bstack111ll1l1ll1_opy_ = id(bstack111ll1lllll_opy_.__class__)
        if (bstack111ll1l1ll1_opy_, hook_type) in self._111ll1ll11l_opy_:
            return
        meth = getattr(bstack111ll1lllll_opy_, hook_type, None)
        if meth is not None and fixtures.getfixturemarker(meth) is None:
            self._111ll1ll11l_opy_[(bstack111ll1l1ll1_opy_, hook_type)] = meth
            setattr(bstack111ll1lllll_opy_, hook_type, self.bstack111ll1ll111_opy_(hook_type, bstack111ll1l1ll1_opy_))
    def bstack111lll111ll_opy_(self, instance, bstack111lll111l1_opy_):
        if bstack111lll111l1_opy_ == bstack1l1ll_opy_ (u"ࠦ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠢᴸ"):
            self.bstack111ll1lll1l_opy_(instance.obj, bstack1l1ll_opy_ (u"ࠧࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠨᴹ"))
            self.bstack111ll1lll1l_opy_(instance.obj, bstack1l1ll_opy_ (u"ࠨࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠥᴺ"))
        if bstack111lll111l1_opy_ == bstack1l1ll_opy_ (u"ࠢ࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠣᴻ"):
            self.bstack111ll1lll1l_opy_(instance.obj, bstack1l1ll_opy_ (u"ࠣࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠢᴼ"))
            self.bstack111ll1lll1l_opy_(instance.obj, bstack1l1ll_opy_ (u"ࠤࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠦᴽ"))
        if bstack111lll111l1_opy_ == bstack1l1ll_opy_ (u"ࠥࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࠥᴾ"):
            self.bstack111ll1lll1l_opy_(instance.obj, bstack1l1ll_opy_ (u"ࠦࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠤᴿ"))
            self.bstack111ll1lll1l_opy_(instance.obj, bstack1l1ll_opy_ (u"ࠧࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸࠨᵀ"))
        if bstack111lll111l1_opy_ == bstack1l1ll_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࡥࡦࡪࡺࡷࡹࡷ࡫ࠢᵁ"):
            self.bstack111ll1lll1l_opy_(instance.obj, bstack1l1ll_opy_ (u"ࠢࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩࠨᵂ"))
            self.bstack111ll1lll1l_opy_(instance.obj, bstack1l1ll_opy_ (u"ࠣࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠥᵃ"))
    @staticmethod
    def bstack111ll1lll11_opy_(hook_type, func, args):
        if hook_type in [bstack1l1ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨᵄ"), bstack1l1ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬᵅ")]:
            _111ll1l1lll_opy_(func, args[0], args[1])
            return
        _call_with_optional_argument(func, args[0])
    def bstack111ll1ll111_opy_(self, hook_type, bstack111ll1l1ll1_opy_):
        def bstack111lll1111l_opy_(arg=None):
            self.handler(hook_type, bstack1l1ll_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫᵆ"))
            result = None
            try:
                bstack1lllll11lll_opy_ = self._111ll1ll11l_opy_[(bstack111ll1l1ll1_opy_, hook_type)]
                self.bstack111ll1lll11_opy_(hook_type, bstack1lllll11lll_opy_, (arg,))
                result = Result(result=bstack1l1ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᵇ"))
            except Exception as e:
                result = Result(result=bstack1l1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᵈ"), exception=e)
                self.handler(hook_type, bstack1l1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷ࠭ᵉ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l1ll_opy_ (u"ࠨࡣࡩࡸࡪࡸࠧᵊ"), result)
        def bstack111ll1l1l1l_opy_(this, arg=None):
            self.handler(hook_type, bstack1l1ll_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩᵋ"))
            result = None
            exception = None
            try:
                self.bstack111ll1lll11_opy_(hook_type, self._111ll1ll11l_opy_[hook_type], (this, arg))
                result = Result(result=bstack1l1ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᵌ"))
            except Exception as e:
                result = Result(result=bstack1l1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᵍ"), exception=e)
                self.handler(hook_type, bstack1l1ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࠫᵎ"), result)
                raise e.with_traceback(e.__traceback__)
            self.handler(hook_type, bstack1l1ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࠬᵏ"), result)
        if hook_type in [bstack1l1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᵐ"), bstack1l1ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪᵑ")]:
            return bstack111ll1l1l1l_opy_
        return bstack111lll1111l_opy_
    def bstack111ll1llll1_opy_(self, bstack111lll111l1_opy_):
        def bstack111ll1ll1l1_opy_(this, *args, **kwargs):
            self.bstack111lll111ll_opy_(this, bstack111lll111l1_opy_)
            self._111ll1l1l11_opy_[bstack111lll111l1_opy_](this, *args, **kwargs)
        return bstack111ll1ll1l1_opy_