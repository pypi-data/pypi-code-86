# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKCommonPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkSpatialFunctionPython
else:
    import _itkSpatialFunctionPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSpatialFunctionPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSpatialFunctionPython.SWIG_PyStaticMethod_New

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
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.ITKCommonBasePython
import itk.itkFunctionBasePython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkRGBAPixelPython
import itk.itkImagePython
import itk.itkImageRegionPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBPixelPython
import itk.itkArrayPython
class itkSpatialFunctionD2PD2(itk.itkFunctionBasePython.itkFunctionBasePD2D):
    r"""


    N-dimensional spatial function class.

    itk::SpatialFunction provides the ability to define functions that can
    be evaluated at an arbitrary point in space (physical or otherwise).
    The return type is specified by the derived class, and the input to
    the function is an n-dimensional itk::Point.

    Although itk::ImageFunction and itk::SpatialFunction are quite
    similar, itk::SpatialFunction derived classes exist without reference
    to an Image type.

    SpatialFunction is templated over output type (the data type returned
    by an evaluate() call) and dimensionality. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

# Register itkSpatialFunctionD2PD2 in _itkSpatialFunctionPython:
_itkSpatialFunctionPython.itkSpatialFunctionD2PD2_swigregister(itkSpatialFunctionD2PD2)

class itkSpatialFunctionD3PD3(itk.itkFunctionBasePython.itkFunctionBasePD3D):
    r"""


    N-dimensional spatial function class.

    itk::SpatialFunction provides the ability to define functions that can
    be evaluated at an arbitrary point in space (physical or otherwise).
    The return type is specified by the derived class, and the input to
    the function is an n-dimensional itk::Point.

    Although itk::ImageFunction and itk::SpatialFunction are quite
    similar, itk::SpatialFunction derived classes exist without reference
    to an Image type.

    SpatialFunction is templated over output type (the data type returned
    by an evaluate() call) and dimensionality. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

# Register itkSpatialFunctionD3PD3 in _itkSpatialFunctionPython:
_itkSpatialFunctionPython.itkSpatialFunctionD3PD3_swigregister(itkSpatialFunctionD3PD3)

class itkSpatialFunctionD4PD4(itk.itkFunctionBasePython.itkFunctionBasePD4D):
    r"""


    N-dimensional spatial function class.

    itk::SpatialFunction provides the ability to define functions that can
    be evaluated at an arbitrary point in space (physical or otherwise).
    The return type is specified by the derived class, and the input to
    the function is an n-dimensional itk::Point.

    Although itk::ImageFunction and itk::SpatialFunction are quite
    similar, itk::SpatialFunction derived classes exist without reference
    to an Image type.

    SpatialFunction is templated over output type (the data type returned
    by an evaluate() call) and dimensionality. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

# Register itkSpatialFunctionD4PD4 in _itkSpatialFunctionPython:
_itkSpatialFunctionPython.itkSpatialFunctionD4PD4_swigregister(itkSpatialFunctionD4PD4)

class itkSpatialFunctionF2PD2(itk.itkFunctionBasePython.itkFunctionBasePD2F):
    r"""


    N-dimensional spatial function class.

    itk::SpatialFunction provides the ability to define functions that can
    be evaluated at an arbitrary point in space (physical or otherwise).
    The return type is specified by the derived class, and the input to
    the function is an n-dimensional itk::Point.

    Although itk::ImageFunction and itk::SpatialFunction are quite
    similar, itk::SpatialFunction derived classes exist without reference
    to an Image type.

    SpatialFunction is templated over output type (the data type returned
    by an evaluate() call) and dimensionality. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

# Register itkSpatialFunctionF2PD2 in _itkSpatialFunctionPython:
_itkSpatialFunctionPython.itkSpatialFunctionF2PD2_swigregister(itkSpatialFunctionF2PD2)

class itkSpatialFunctionF3PD3(itk.itkFunctionBasePython.itkFunctionBasePD3F):
    r"""


    N-dimensional spatial function class.

    itk::SpatialFunction provides the ability to define functions that can
    be evaluated at an arbitrary point in space (physical or otherwise).
    The return type is specified by the derived class, and the input to
    the function is an n-dimensional itk::Point.

    Although itk::ImageFunction and itk::SpatialFunction are quite
    similar, itk::SpatialFunction derived classes exist without reference
    to an Image type.

    SpatialFunction is templated over output type (the data type returned
    by an evaluate() call) and dimensionality. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

# Register itkSpatialFunctionF3PD3 in _itkSpatialFunctionPython:
_itkSpatialFunctionPython.itkSpatialFunctionF3PD3_swigregister(itkSpatialFunctionF3PD3)

class itkSpatialFunctionF4PD4(itk.itkFunctionBasePython.itkFunctionBasePD4F):
    r"""


    N-dimensional spatial function class.

    itk::SpatialFunction provides the ability to define functions that can
    be evaluated at an arbitrary point in space (physical or otherwise).
    The return type is specified by the derived class, and the input to
    the function is an n-dimensional itk::Point.

    Although itk::ImageFunction and itk::SpatialFunction are quite
    similar, itk::SpatialFunction derived classes exist without reference
    to an Image type.

    SpatialFunction is templated over output type (the data type returned
    by an evaluate() call) and dimensionality. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

# Register itkSpatialFunctionF4PD4 in _itkSpatialFunctionPython:
_itkSpatialFunctionPython.itkSpatialFunctionF4PD4_swigregister(itkSpatialFunctionF4PD4)



