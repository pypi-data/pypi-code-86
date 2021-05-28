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
    from . import _itkObjectToObjectMetricBasePython
else:
    import _itkObjectToObjectMetricBasePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkObjectToObjectMetricBasePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkObjectToObjectMetricBasePython.SWIG_PyStaticMethod_New

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
import itk.itkOptimizerParametersPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkSingleValuedCostFunctionv4Python
import itk.itkCostFunctionPython
class itkObjectToObjectMetricBaseTemplateD(itk.itkSingleValuedCostFunctionv4Python.itkSingleValuedCostFunctionv4TemplateD):
    r"""Proxy of C++ itkObjectToObjectMetricBaseTemplateD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetFixedObject = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_SetFixedObject)
    GetFixedObject = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_GetFixedObject)
    SetMovingObject = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_SetMovingObject)
    GetMovingObject = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_GetMovingObject)
    SetGradientSource = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_SetGradientSource)
    GetGradientSource = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_GetGradientSource)
    GetGradientSourceIncludesFixed = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_GetGradientSourceIncludesFixed)
    GetGradientSourceIncludesMoving = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_GetGradientSourceIncludesMoving)
    Initialize = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_Initialize)
    GetDerivative = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_GetDerivative)
    GetNumberOfLocalParameters = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_GetNumberOfLocalParameters)
    SetParameters = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_SetParameters)
    GetParameters = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_GetParameters)
    HasLocalSupport = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_HasLocalSupport)
    UpdateTransformParameters = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_UpdateTransformParameters)
    GetCurrentValue = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_GetCurrentValue)
    GetMetricCategory = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_GetMetricCategory)
    __swig_destroy__ = _itkObjectToObjectMetricBasePython.delete_itkObjectToObjectMetricBaseTemplateD
    cast = _swig_new_static_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_cast)

# Register itkObjectToObjectMetricBaseTemplateD in _itkObjectToObjectMetricBasePython:
_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_swigregister(itkObjectToObjectMetricBaseTemplateD)
itkObjectToObjectMetricBaseTemplateD_cast = _itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateD_cast

class itkObjectToObjectMetricBaseTemplateEnums(object):
    r"""Proxy of C++ itkObjectToObjectMetricBaseTemplateEnums class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    GradientSource_GRADIENT_SOURCE_FIXED = _itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateEnums_GradientSource_GRADIENT_SOURCE_FIXED
    
    GradientSource_GRADIENT_SOURCE_MOVING = _itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateEnums_GradientSource_GRADIENT_SOURCE_MOVING
    
    GradientSource_GRADIENT_SOURCE_BOTH = _itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateEnums_GradientSource_GRADIENT_SOURCE_BOTH
    
    MetricCategory_UNKNOWN_METRIC = _itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateEnums_MetricCategory_UNKNOWN_METRIC
    
    MetricCategory_OBJECT_METRIC = _itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateEnums_MetricCategory_OBJECT_METRIC
    
    MetricCategory_IMAGE_METRIC = _itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateEnums_MetricCategory_IMAGE_METRIC
    
    MetricCategory_POINT_SET_METRIC = _itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateEnums_MetricCategory_POINT_SET_METRIC
    
    MetricCategory_MULTI_METRIC = _itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateEnums_MetricCategory_MULTI_METRIC
    

    def __init__(self, *args):
        r"""
        __init__(self) -> itkObjectToObjectMetricBaseTemplateEnums
        __init__(self, arg0) -> itkObjectToObjectMetricBaseTemplateEnums

        Parameters
        ----------
        arg0: itkObjectToObjectMetricBaseTemplateEnums const &

        """
        _itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateEnums_swiginit(self, _itkObjectToObjectMetricBasePython.new_itkObjectToObjectMetricBaseTemplateEnums(*args))
    __swig_destroy__ = _itkObjectToObjectMetricBasePython.delete_itkObjectToObjectMetricBaseTemplateEnums

# Register itkObjectToObjectMetricBaseTemplateEnums in _itkObjectToObjectMetricBasePython:
_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateEnums_swigregister(itkObjectToObjectMetricBaseTemplateEnums)

class itkObjectToObjectMetricBaseTemplateF(itk.itkSingleValuedCostFunctionv4Python.itkSingleValuedCostFunctionv4TemplateF):
    r"""Proxy of C++ itkObjectToObjectMetricBaseTemplateF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetFixedObject = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_SetFixedObject)
    GetFixedObject = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_GetFixedObject)
    SetMovingObject = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_SetMovingObject)
    GetMovingObject = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_GetMovingObject)
    SetGradientSource = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_SetGradientSource)
    GetGradientSource = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_GetGradientSource)
    GetGradientSourceIncludesFixed = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_GetGradientSourceIncludesFixed)
    GetGradientSourceIncludesMoving = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_GetGradientSourceIncludesMoving)
    Initialize = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_Initialize)
    GetDerivative = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_GetDerivative)
    GetNumberOfLocalParameters = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_GetNumberOfLocalParameters)
    SetParameters = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_SetParameters)
    GetParameters = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_GetParameters)
    HasLocalSupport = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_HasLocalSupport)
    UpdateTransformParameters = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_UpdateTransformParameters)
    GetCurrentValue = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_GetCurrentValue)
    GetMetricCategory = _swig_new_instance_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_GetMetricCategory)
    __swig_destroy__ = _itkObjectToObjectMetricBasePython.delete_itkObjectToObjectMetricBaseTemplateF
    cast = _swig_new_static_method(_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_cast)

# Register itkObjectToObjectMetricBaseTemplateF in _itkObjectToObjectMetricBasePython:
_itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_swigregister(itkObjectToObjectMetricBaseTemplateF)
itkObjectToObjectMetricBaseTemplateF_cast = _itkObjectToObjectMetricBasePython.itkObjectToObjectMetricBaseTemplateF_cast



