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
    from . import _itkSingleValuedCostFunctionv4Python
else:
    import _itkSingleValuedCostFunctionv4Python

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSingleValuedCostFunctionv4Python.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSingleValuedCostFunctionv4Python.SWIG_PyStaticMethod_New

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
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_matrixPython
import itk.itkCostFunctionPython
import itk.ITKCommonBasePython
class itkSingleValuedCostFunctionv4TemplateD(itk.itkCostFunctionPython.itkCostFunctionTemplateD):
    r"""Proxy of C++ itkSingleValuedCostFunctionv4TemplateD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetValue = _swig_new_instance_method(_itkSingleValuedCostFunctionv4Python.itkSingleValuedCostFunctionv4TemplateD_GetValue)
    GetValueAndDerivative = _swig_new_instance_method(_itkSingleValuedCostFunctionv4Python.itkSingleValuedCostFunctionv4TemplateD_GetValueAndDerivative)
    __swig_destroy__ = _itkSingleValuedCostFunctionv4Python.delete_itkSingleValuedCostFunctionv4TemplateD
    cast = _swig_new_static_method(_itkSingleValuedCostFunctionv4Python.itkSingleValuedCostFunctionv4TemplateD_cast)

# Register itkSingleValuedCostFunctionv4TemplateD in _itkSingleValuedCostFunctionv4Python:
_itkSingleValuedCostFunctionv4Python.itkSingleValuedCostFunctionv4TemplateD_swigregister(itkSingleValuedCostFunctionv4TemplateD)
itkSingleValuedCostFunctionv4TemplateD_cast = _itkSingleValuedCostFunctionv4Python.itkSingleValuedCostFunctionv4TemplateD_cast

class itkSingleValuedCostFunctionv4TemplateF(itk.itkCostFunctionPython.itkCostFunctionTemplateF):
    r"""Proxy of C++ itkSingleValuedCostFunctionv4TemplateF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    GetValue = _swig_new_instance_method(_itkSingleValuedCostFunctionv4Python.itkSingleValuedCostFunctionv4TemplateF_GetValue)
    GetValueAndDerivative = _swig_new_instance_method(_itkSingleValuedCostFunctionv4Python.itkSingleValuedCostFunctionv4TemplateF_GetValueAndDerivative)
    __swig_destroy__ = _itkSingleValuedCostFunctionv4Python.delete_itkSingleValuedCostFunctionv4TemplateF
    cast = _swig_new_static_method(_itkSingleValuedCostFunctionv4Python.itkSingleValuedCostFunctionv4TemplateF_cast)

# Register itkSingleValuedCostFunctionv4TemplateF in _itkSingleValuedCostFunctionv4Python:
_itkSingleValuedCostFunctionv4Python.itkSingleValuedCostFunctionv4TemplateF_swigregister(itkSingleValuedCostFunctionv4TemplateF)
itkSingleValuedCostFunctionv4TemplateF_cast = _itkSingleValuedCostFunctionv4Python.itkSingleValuedCostFunctionv4TemplateF_cast



