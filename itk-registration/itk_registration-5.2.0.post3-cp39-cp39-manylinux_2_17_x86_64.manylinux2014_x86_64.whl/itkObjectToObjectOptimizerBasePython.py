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
    from . import _itkObjectToObjectOptimizerBasePython
else:
    import _itkObjectToObjectOptimizerBasePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkObjectToObjectOptimizerBasePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkObjectToObjectOptimizerBasePython.SWIG_PyStaticMethod_New

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
import itk.itkObjectToObjectMetricBasePython
import itk.itkSingleValuedCostFunctionv4Python
import itk.itkCostFunctionPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkOptimizerParametersPython
import itk.itkOptimizerParameterScalesEstimatorPython
class itkObjectToObjectOptimizerBaseTemplateD(itk.ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkObjectToObjectOptimizerBaseTemplateD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetMetric = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_SetMetric)
    GetModifiableMetric = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetModifiableMetric)
    GetMetric = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetMetric)
    GetCurrentMetricValue = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetCurrentMetricValue)
    GetValue = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetValue)
    SetScales = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_SetScales)
    GetScales = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetScales)
    GetScalesAreIdentity = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetScalesAreIdentity)
    SetWeights = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_SetWeights)
    GetWeights = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetWeights)
    GetWeightsAreIdentity = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetWeightsAreIdentity)
    GetScalesInitialized = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetScalesInitialized)
    SetScalesEstimator = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_SetScalesEstimator)
    SetDoEstimateScales = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_SetDoEstimateScales)
    GetDoEstimateScales = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetDoEstimateScales)
    DoEstimateScalesOn = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_DoEstimateScalesOn)
    DoEstimateScalesOff = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_DoEstimateScalesOff)
    SetNumberOfWorkUnits = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_SetNumberOfWorkUnits)
    GetNumberOfWorkUnits = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetNumberOfWorkUnits)
    GetCurrentIteration = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetCurrentIteration)
    SetNumberOfIterations = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_SetNumberOfIterations)
    GetNumberOfIterations = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetNumberOfIterations)
    GetCurrentPosition = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetCurrentPosition)
    StartOptimization = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_StartOptimization)
    GetStopConditionDescription = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_GetStopConditionDescription)
    __swig_destroy__ = _itkObjectToObjectOptimizerBasePython.delete_itkObjectToObjectOptimizerBaseTemplateD
    cast = _swig_new_static_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_cast)

# Register itkObjectToObjectOptimizerBaseTemplateD in _itkObjectToObjectOptimizerBasePython:
_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_swigregister(itkObjectToObjectOptimizerBaseTemplateD)
itkObjectToObjectOptimizerBaseTemplateD_cast = _itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateD_cast

class itkObjectToObjectOptimizerBaseTemplateEnums(object):
    r"""Proxy of C++ itkObjectToObjectOptimizerBaseTemplateEnums class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    StopConditionObjectToObjectOptimizer_MAXIMUM_NUMBER_OF_ITERATIONS = _itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateEnums_StopConditionObjectToObjectOptimizer_MAXIMUM_NUMBER_OF_ITERATIONS
    
    StopConditionObjectToObjectOptimizer_COSTFUNCTION_ERROR = _itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateEnums_StopConditionObjectToObjectOptimizer_COSTFUNCTION_ERROR
    
    StopConditionObjectToObjectOptimizer_UPDATE_PARAMETERS_ERROR = _itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateEnums_StopConditionObjectToObjectOptimizer_UPDATE_PARAMETERS_ERROR
    
    StopConditionObjectToObjectOptimizer_STEP_TOO_SMALL = _itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateEnums_StopConditionObjectToObjectOptimizer_STEP_TOO_SMALL
    
    StopConditionObjectToObjectOptimizer_CONVERGENCE_CHECKER_PASSED = _itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateEnums_StopConditionObjectToObjectOptimizer_CONVERGENCE_CHECKER_PASSED
    
    StopConditionObjectToObjectOptimizer_GRADIENT_MAGNITUDE_TOLEARANCE = _itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateEnums_StopConditionObjectToObjectOptimizer_GRADIENT_MAGNITUDE_TOLEARANCE
    
    StopConditionObjectToObjectOptimizer_OTHER_ERROR = _itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateEnums_StopConditionObjectToObjectOptimizer_OTHER_ERROR
    

    def __init__(self, *args):
        r"""
        __init__(self) -> itkObjectToObjectOptimizerBaseTemplateEnums
        __init__(self, arg0) -> itkObjectToObjectOptimizerBaseTemplateEnums

        Parameters
        ----------
        arg0: itkObjectToObjectOptimizerBaseTemplateEnums const &

        """
        _itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateEnums_swiginit(self, _itkObjectToObjectOptimizerBasePython.new_itkObjectToObjectOptimizerBaseTemplateEnums(*args))
    __swig_destroy__ = _itkObjectToObjectOptimizerBasePython.delete_itkObjectToObjectOptimizerBaseTemplateEnums

# Register itkObjectToObjectOptimizerBaseTemplateEnums in _itkObjectToObjectOptimizerBasePython:
_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateEnums_swigregister(itkObjectToObjectOptimizerBaseTemplateEnums)

class itkObjectToObjectOptimizerBaseTemplateF(itk.ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkObjectToObjectOptimizerBaseTemplateF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetMetric = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_SetMetric)
    GetModifiableMetric = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetModifiableMetric)
    GetMetric = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetMetric)
    GetCurrentMetricValue = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetCurrentMetricValue)
    GetValue = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetValue)
    SetScales = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_SetScales)
    GetScales = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetScales)
    GetScalesAreIdentity = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetScalesAreIdentity)
    SetWeights = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_SetWeights)
    GetWeights = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetWeights)
    GetWeightsAreIdentity = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetWeightsAreIdentity)
    GetScalesInitialized = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetScalesInitialized)
    SetScalesEstimator = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_SetScalesEstimator)
    SetDoEstimateScales = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_SetDoEstimateScales)
    GetDoEstimateScales = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetDoEstimateScales)
    DoEstimateScalesOn = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_DoEstimateScalesOn)
    DoEstimateScalesOff = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_DoEstimateScalesOff)
    SetNumberOfWorkUnits = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_SetNumberOfWorkUnits)
    GetNumberOfWorkUnits = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetNumberOfWorkUnits)
    GetCurrentIteration = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetCurrentIteration)
    SetNumberOfIterations = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_SetNumberOfIterations)
    GetNumberOfIterations = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetNumberOfIterations)
    GetCurrentPosition = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetCurrentPosition)
    StartOptimization = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_StartOptimization)
    GetStopConditionDescription = _swig_new_instance_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_GetStopConditionDescription)
    __swig_destroy__ = _itkObjectToObjectOptimizerBasePython.delete_itkObjectToObjectOptimizerBaseTemplateF
    cast = _swig_new_static_method(_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_cast)

# Register itkObjectToObjectOptimizerBaseTemplateF in _itkObjectToObjectOptimizerBasePython:
_itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_swigregister(itkObjectToObjectOptimizerBaseTemplateF)
itkObjectToObjectOptimizerBaseTemplateF_cast = _itkObjectToObjectOptimizerBasePython.itkObjectToObjectOptimizerBaseTemplateF_cast



