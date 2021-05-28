# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKOptimizersv4Python



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkLBFGSOptimizerBasev4Python
else:
    import _itkLBFGSOptimizerBasev4Python

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLBFGSOptimizerBasev4Python.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLBFGSOptimizerBasev4Python.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import collections.abc
import itk.itkLBFGSOptimizerBaseHelperv4Python
import itk.itkVnlTypesPython
import itk.vnl_matrixPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_cost_functionPython
import itk.vnl_unary_functionPython
import itk.ITKCommonBasePython
import itk.itkSingleValuedNonLinearVnlOptimizerv4Python
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkObjectToObjectMetricBasePython
import itk.itkSingleValuedCostFunctionv4Python
import itk.itkCostFunctionPython
import itk.itkObjectToObjectOptimizerBasePython
import itk.itkOptimizerParameterScalesEstimatorPython
class itkLBFGSOptimizerBasev4vnl_lbfgs(itk.itkSingleValuedNonLinearVnlOptimizerv4Python.itkSingleValuedNonLinearVnlOptimizerv4):
    r"""


    Abstract base for vnl lbfgs algorithm optimizers in ITKv4 registration
    framework.

    The StopConditionDescription returned by this class is directly from
    the vnl optimizer by calling  m_VnlOptimizer->get_failure_code(). This
    seems to return "Failure" even when no error has occurred. The same
    behavior is observed in the ITKv3 version of this optimizer.

    Local-support (high-density) transforms. Local-support transforms are
    not supported. To add support for these, the class must be modified
    thusly:

    1) Parameter updates: In SingleValuedNonLinearCostFunctionAdaptor, the
    handling of the gradient must be changed to accommodate the fact that
    local-support transforms expect a gradient to be added to the
    transform parameters using the UpdateTransformParameters method of the
    local support transform. Other optimizers in the v4 framework use this
    method, but the use of the vnl optimizers here complicates it.

    2) Efficiency To work efficiently with local-support transforms, this
    class should be modified to use a single parameter object to avoid the
    multiple parameter copies that are currently performed. It should work
    to use the transform parameters pointer.  This code has been adapted
    for the ITKv4 registration framework from the v3 version,
    itkLBFGSOptimizer. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    GetOptimizer = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgs_GetOptimizer)
    StartOptimization = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgs_StartOptimization)
    SetTrace = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgs_SetTrace)
    GetTrace = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgs_GetTrace)
    TraceOn = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgs_TraceOn)
    TraceOff = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgs_TraceOff)
    SetMaximumNumberOfFunctionEvaluations = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgs_SetMaximumNumberOfFunctionEvaluations)
    GetMaximumNumberOfFunctionEvaluations = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgs_GetMaximumNumberOfFunctionEvaluations)
    SetGradientConvergenceTolerance = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgs_SetGradientConvergenceTolerance)
    GetGradientConvergenceTolerance = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgs_GetGradientConvergenceTolerance)
    __swig_destroy__ = _itkLBFGSOptimizerBasev4Python.delete_itkLBFGSOptimizerBasev4vnl_lbfgs
    cast = _swig_new_static_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgs_cast)

# Register itkLBFGSOptimizerBasev4vnl_lbfgs in _itkLBFGSOptimizerBasev4Python:
_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgs_swigregister(itkLBFGSOptimizerBasev4vnl_lbfgs)
itkLBFGSOptimizerBasev4vnl_lbfgs_cast = _itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgs_cast

class itkLBFGSOptimizerBasev4vnl_lbfgsb(itk.itkSingleValuedNonLinearVnlOptimizerv4Python.itkSingleValuedNonLinearVnlOptimizerv4):
    r"""


    Abstract base for vnl lbfgs algorithm optimizers in ITKv4 registration
    framework.

    The StopConditionDescription returned by this class is directly from
    the vnl optimizer by calling  m_VnlOptimizer->get_failure_code(). This
    seems to return "Failure" even when no error has occurred. The same
    behavior is observed in the ITKv3 version of this optimizer.

    Local-support (high-density) transforms. Local-support transforms are
    not supported. To add support for these, the class must be modified
    thusly:

    1) Parameter updates: In SingleValuedNonLinearCostFunctionAdaptor, the
    handling of the gradient must be changed to accommodate the fact that
    local-support transforms expect a gradient to be added to the
    transform parameters using the UpdateTransformParameters method of the
    local support transform. Other optimizers in the v4 framework use this
    method, but the use of the vnl optimizers here complicates it.

    2) Efficiency To work efficiently with local-support transforms, this
    class should be modified to use a single parameter object to avoid the
    multiple parameter copies that are currently performed. It should work
    to use the transform parameters pointer.  This code has been adapted
    for the ITKv4 registration framework from the v3 version,
    itkLBFGSOptimizer. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    GetOptimizer = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgsb_GetOptimizer)
    StartOptimization = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgsb_StartOptimization)
    SetTrace = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgsb_SetTrace)
    GetTrace = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgsb_GetTrace)
    TraceOn = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgsb_TraceOn)
    TraceOff = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgsb_TraceOff)
    SetMaximumNumberOfFunctionEvaluations = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgsb_SetMaximumNumberOfFunctionEvaluations)
    GetMaximumNumberOfFunctionEvaluations = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgsb_GetMaximumNumberOfFunctionEvaluations)
    SetGradientConvergenceTolerance = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgsb_SetGradientConvergenceTolerance)
    GetGradientConvergenceTolerance = _swig_new_instance_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgsb_GetGradientConvergenceTolerance)
    __swig_destroy__ = _itkLBFGSOptimizerBasev4Python.delete_itkLBFGSOptimizerBasev4vnl_lbfgsb
    cast = _swig_new_static_method(_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgsb_cast)

# Register itkLBFGSOptimizerBasev4vnl_lbfgsb in _itkLBFGSOptimizerBasev4Python:
_itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgsb_swigregister(itkLBFGSOptimizerBasev4vnl_lbfgsb)
itkLBFGSOptimizerBasev4vnl_lbfgsb_cast = _itkLBFGSOptimizerBasev4Python.itkLBFGSOptimizerBasev4vnl_lbfgsb_cast



