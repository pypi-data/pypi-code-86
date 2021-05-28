# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKQuadEdgeMeshFilteringPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkMatrixCoefficientsPython
else:
    import _itkMatrixCoefficientsPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMatrixCoefficientsPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMatrixCoefficientsPython.SWIG_PyStaticMethod_New

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
import itk.itkQuadEdgeMeshBasePython
import itk.itkQuadEdgeMeshLineCellPython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.ITKCommonBasePython
import itk.itkQuadEdgeCellTraitsInfoPython
import itk.itkQuadEdgeMeshPointPython
import itk.itkGeometricalQuadEdgePython
import itk.itkQuadEdgePython
import itk.itkPointPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkCovariantVectorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkImageRegionPython
import itk.itkRGBAPixelPython
import itk.itkMapContainerPython
class itkMatrixCoefficientsQEMD2(object):
    r"""Proxy of C++ itkMatrixCoefficientsQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkMatrixCoefficientsQEMD2
    __call__ = _swig_new_instance_method(_itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD2___call__)

# Register itkMatrixCoefficientsQEMD2 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD2_swigregister(itkMatrixCoefficientsQEMD2)

class itkMatrixCoefficientsQEMD3(object):
    r"""Proxy of C++ itkMatrixCoefficientsQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkMatrixCoefficientsQEMD3
    __call__ = _swig_new_instance_method(_itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD3___call__)

# Register itkMatrixCoefficientsQEMD3 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD3_swigregister(itkMatrixCoefficientsQEMD3)

class itkMatrixCoefficientsQEMD4(object):
    r"""Proxy of C++ itkMatrixCoefficientsQEMD4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkMatrixCoefficientsQEMD4
    __call__ = _swig_new_instance_method(_itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD4___call__)

# Register itkMatrixCoefficientsQEMD4 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkMatrixCoefficientsQEMD4_swigregister(itkMatrixCoefficientsQEMD4)

class itkOnesMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    r"""Proxy of C++ itkOnesMatrixCoefficientsQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkOnesMatrixCoefficientsQEMD2
        __init__(self, arg0) -> itkOnesMatrixCoefficientsQEMD2

        Parameters
        ----------
        arg0: itkOnesMatrixCoefficientsQEMD2 const &

        """
        _itkMatrixCoefficientsPython.itkOnesMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkOnesMatrixCoefficientsQEMD2(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkOnesMatrixCoefficientsQEMD2

# Register itkOnesMatrixCoefficientsQEMD2 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkOnesMatrixCoefficientsQEMD2_swigregister(itkOnesMatrixCoefficientsQEMD2)

class itkOnesMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    r"""Proxy of C++ itkOnesMatrixCoefficientsQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkOnesMatrixCoefficientsQEMD3
        __init__(self, arg0) -> itkOnesMatrixCoefficientsQEMD3

        Parameters
        ----------
        arg0: itkOnesMatrixCoefficientsQEMD3 const &

        """
        _itkMatrixCoefficientsPython.itkOnesMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkOnesMatrixCoefficientsQEMD3(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkOnesMatrixCoefficientsQEMD3

# Register itkOnesMatrixCoefficientsQEMD3 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkOnesMatrixCoefficientsQEMD3_swigregister(itkOnesMatrixCoefficientsQEMD3)

class itkOnesMatrixCoefficientsQEMD4(itkMatrixCoefficientsQEMD4):
    r"""Proxy of C++ itkOnesMatrixCoefficientsQEMD4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkOnesMatrixCoefficientsQEMD4
        __init__(self, arg0) -> itkOnesMatrixCoefficientsQEMD4

        Parameters
        ----------
        arg0: itkOnesMatrixCoefficientsQEMD4 const &

        """
        _itkMatrixCoefficientsPython.itkOnesMatrixCoefficientsQEMD4_swiginit(self, _itkMatrixCoefficientsPython.new_itkOnesMatrixCoefficientsQEMD4(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkOnesMatrixCoefficientsQEMD4

# Register itkOnesMatrixCoefficientsQEMD4 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkOnesMatrixCoefficientsQEMD4_swigregister(itkOnesMatrixCoefficientsQEMD4)

class itkAuthalicMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    r"""Proxy of C++ itkAuthalicMatrixCoefficientsQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkAuthalicMatrixCoefficientsQEMD2
        __init__(self, arg0) -> itkAuthalicMatrixCoefficientsQEMD2

        Parameters
        ----------
        arg0: itkAuthalicMatrixCoefficientsQEMD2 const &

        """
        _itkMatrixCoefficientsPython.itkAuthalicMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkAuthalicMatrixCoefficientsQEMD2(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkAuthalicMatrixCoefficientsQEMD2

# Register itkAuthalicMatrixCoefficientsQEMD2 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkAuthalicMatrixCoefficientsQEMD2_swigregister(itkAuthalicMatrixCoefficientsQEMD2)

class itkAuthalicMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    r"""Proxy of C++ itkAuthalicMatrixCoefficientsQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkAuthalicMatrixCoefficientsQEMD3
        __init__(self, arg0) -> itkAuthalicMatrixCoefficientsQEMD3

        Parameters
        ----------
        arg0: itkAuthalicMatrixCoefficientsQEMD3 const &

        """
        _itkMatrixCoefficientsPython.itkAuthalicMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkAuthalicMatrixCoefficientsQEMD3(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkAuthalicMatrixCoefficientsQEMD3

# Register itkAuthalicMatrixCoefficientsQEMD3 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkAuthalicMatrixCoefficientsQEMD3_swigregister(itkAuthalicMatrixCoefficientsQEMD3)

class itkAuthalicMatrixCoefficientsQEMD4(itkMatrixCoefficientsQEMD4):
    r"""Proxy of C++ itkAuthalicMatrixCoefficientsQEMD4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkAuthalicMatrixCoefficientsQEMD4
        __init__(self, arg0) -> itkAuthalicMatrixCoefficientsQEMD4

        Parameters
        ----------
        arg0: itkAuthalicMatrixCoefficientsQEMD4 const &

        """
        _itkMatrixCoefficientsPython.itkAuthalicMatrixCoefficientsQEMD4_swiginit(self, _itkMatrixCoefficientsPython.new_itkAuthalicMatrixCoefficientsQEMD4(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkAuthalicMatrixCoefficientsQEMD4

# Register itkAuthalicMatrixCoefficientsQEMD4 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkAuthalicMatrixCoefficientsQEMD4_swigregister(itkAuthalicMatrixCoefficientsQEMD4)

class itkConformalMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    r"""Proxy of C++ itkConformalMatrixCoefficientsQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkConformalMatrixCoefficientsQEMD2
        __init__(self, arg0) -> itkConformalMatrixCoefficientsQEMD2

        Parameters
        ----------
        arg0: itkConformalMatrixCoefficientsQEMD2 const &

        """
        _itkMatrixCoefficientsPython.itkConformalMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkConformalMatrixCoefficientsQEMD2(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkConformalMatrixCoefficientsQEMD2

# Register itkConformalMatrixCoefficientsQEMD2 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkConformalMatrixCoefficientsQEMD2_swigregister(itkConformalMatrixCoefficientsQEMD2)

class itkConformalMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    r"""Proxy of C++ itkConformalMatrixCoefficientsQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkConformalMatrixCoefficientsQEMD3
        __init__(self, arg0) -> itkConformalMatrixCoefficientsQEMD3

        Parameters
        ----------
        arg0: itkConformalMatrixCoefficientsQEMD3 const &

        """
        _itkMatrixCoefficientsPython.itkConformalMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkConformalMatrixCoefficientsQEMD3(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkConformalMatrixCoefficientsQEMD3

# Register itkConformalMatrixCoefficientsQEMD3 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkConformalMatrixCoefficientsQEMD3_swigregister(itkConformalMatrixCoefficientsQEMD3)

class itkConformalMatrixCoefficientsQEMD4(itkMatrixCoefficientsQEMD4):
    r"""Proxy of C++ itkConformalMatrixCoefficientsQEMD4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkConformalMatrixCoefficientsQEMD4
        __init__(self, arg0) -> itkConformalMatrixCoefficientsQEMD4

        Parameters
        ----------
        arg0: itkConformalMatrixCoefficientsQEMD4 const &

        """
        _itkMatrixCoefficientsPython.itkConformalMatrixCoefficientsQEMD4_swiginit(self, _itkMatrixCoefficientsPython.new_itkConformalMatrixCoefficientsQEMD4(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkConformalMatrixCoefficientsQEMD4

# Register itkConformalMatrixCoefficientsQEMD4 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkConformalMatrixCoefficientsQEMD4_swigregister(itkConformalMatrixCoefficientsQEMD4)

class itkHarmonicMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    r"""Proxy of C++ itkHarmonicMatrixCoefficientsQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkHarmonicMatrixCoefficientsQEMD2
        __init__(self, arg0) -> itkHarmonicMatrixCoefficientsQEMD2

        Parameters
        ----------
        arg0: itkHarmonicMatrixCoefficientsQEMD2 const &

        """
        _itkMatrixCoefficientsPython.itkHarmonicMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkHarmonicMatrixCoefficientsQEMD2(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkHarmonicMatrixCoefficientsQEMD2

# Register itkHarmonicMatrixCoefficientsQEMD2 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkHarmonicMatrixCoefficientsQEMD2_swigregister(itkHarmonicMatrixCoefficientsQEMD2)

class itkHarmonicMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    r"""Proxy of C++ itkHarmonicMatrixCoefficientsQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkHarmonicMatrixCoefficientsQEMD3
        __init__(self, arg0) -> itkHarmonicMatrixCoefficientsQEMD3

        Parameters
        ----------
        arg0: itkHarmonicMatrixCoefficientsQEMD3 const &

        """
        _itkMatrixCoefficientsPython.itkHarmonicMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkHarmonicMatrixCoefficientsQEMD3(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkHarmonicMatrixCoefficientsQEMD3

# Register itkHarmonicMatrixCoefficientsQEMD3 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkHarmonicMatrixCoefficientsQEMD3_swigregister(itkHarmonicMatrixCoefficientsQEMD3)

class itkHarmonicMatrixCoefficientsQEMD4(itkMatrixCoefficientsQEMD4):
    r"""Proxy of C++ itkHarmonicMatrixCoefficientsQEMD4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkHarmonicMatrixCoefficientsQEMD4
        __init__(self, arg0) -> itkHarmonicMatrixCoefficientsQEMD4

        Parameters
        ----------
        arg0: itkHarmonicMatrixCoefficientsQEMD4 const &

        """
        _itkMatrixCoefficientsPython.itkHarmonicMatrixCoefficientsQEMD4_swiginit(self, _itkMatrixCoefficientsPython.new_itkHarmonicMatrixCoefficientsQEMD4(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkHarmonicMatrixCoefficientsQEMD4

# Register itkHarmonicMatrixCoefficientsQEMD4 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkHarmonicMatrixCoefficientsQEMD4_swigregister(itkHarmonicMatrixCoefficientsQEMD4)

class itkIntrinsicMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    r"""Proxy of C++ itkIntrinsicMatrixCoefficientsQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, iLambda) -> itkIntrinsicMatrixCoefficientsQEMD2

        Parameters
        ----------
        iLambda: float const &

        __init__(self, arg0) -> itkIntrinsicMatrixCoefficientsQEMD2

        Parameters
        ----------
        arg0: itkIntrinsicMatrixCoefficientsQEMD2 const &

        """
        _itkMatrixCoefficientsPython.itkIntrinsicMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkIntrinsicMatrixCoefficientsQEMD2(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkIntrinsicMatrixCoefficientsQEMD2

# Register itkIntrinsicMatrixCoefficientsQEMD2 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkIntrinsicMatrixCoefficientsQEMD2_swigregister(itkIntrinsicMatrixCoefficientsQEMD2)

class itkIntrinsicMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    r"""Proxy of C++ itkIntrinsicMatrixCoefficientsQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, iLambda) -> itkIntrinsicMatrixCoefficientsQEMD3

        Parameters
        ----------
        iLambda: float const &

        __init__(self, arg0) -> itkIntrinsicMatrixCoefficientsQEMD3

        Parameters
        ----------
        arg0: itkIntrinsicMatrixCoefficientsQEMD3 const &

        """
        _itkMatrixCoefficientsPython.itkIntrinsicMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkIntrinsicMatrixCoefficientsQEMD3(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkIntrinsicMatrixCoefficientsQEMD3

# Register itkIntrinsicMatrixCoefficientsQEMD3 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkIntrinsicMatrixCoefficientsQEMD3_swigregister(itkIntrinsicMatrixCoefficientsQEMD3)

class itkIntrinsicMatrixCoefficientsQEMD4(itkMatrixCoefficientsQEMD4):
    r"""Proxy of C++ itkIntrinsicMatrixCoefficientsQEMD4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self, iLambda) -> itkIntrinsicMatrixCoefficientsQEMD4

        Parameters
        ----------
        iLambda: float const &

        __init__(self, arg0) -> itkIntrinsicMatrixCoefficientsQEMD4

        Parameters
        ----------
        arg0: itkIntrinsicMatrixCoefficientsQEMD4 const &

        """
        _itkMatrixCoefficientsPython.itkIntrinsicMatrixCoefficientsQEMD4_swiginit(self, _itkMatrixCoefficientsPython.new_itkIntrinsicMatrixCoefficientsQEMD4(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkIntrinsicMatrixCoefficientsQEMD4

# Register itkIntrinsicMatrixCoefficientsQEMD4 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkIntrinsicMatrixCoefficientsQEMD4_swigregister(itkIntrinsicMatrixCoefficientsQEMD4)

class itkInverseEuclideanDistanceMatrixCoefficientsQEMD2(itkMatrixCoefficientsQEMD2):
    r"""Proxy of C++ itkInverseEuclideanDistanceMatrixCoefficientsQEMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkInverseEuclideanDistanceMatrixCoefficientsQEMD2
        __init__(self, arg0) -> itkInverseEuclideanDistanceMatrixCoefficientsQEMD2

        Parameters
        ----------
        arg0: itkInverseEuclideanDistanceMatrixCoefficientsQEMD2 const &

        """
        _itkMatrixCoefficientsPython.itkInverseEuclideanDistanceMatrixCoefficientsQEMD2_swiginit(self, _itkMatrixCoefficientsPython.new_itkInverseEuclideanDistanceMatrixCoefficientsQEMD2(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkInverseEuclideanDistanceMatrixCoefficientsQEMD2

# Register itkInverseEuclideanDistanceMatrixCoefficientsQEMD2 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkInverseEuclideanDistanceMatrixCoefficientsQEMD2_swigregister(itkInverseEuclideanDistanceMatrixCoefficientsQEMD2)

class itkInverseEuclideanDistanceMatrixCoefficientsQEMD3(itkMatrixCoefficientsQEMD3):
    r"""Proxy of C++ itkInverseEuclideanDistanceMatrixCoefficientsQEMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkInverseEuclideanDistanceMatrixCoefficientsQEMD3
        __init__(self, arg0) -> itkInverseEuclideanDistanceMatrixCoefficientsQEMD3

        Parameters
        ----------
        arg0: itkInverseEuclideanDistanceMatrixCoefficientsQEMD3 const &

        """
        _itkMatrixCoefficientsPython.itkInverseEuclideanDistanceMatrixCoefficientsQEMD3_swiginit(self, _itkMatrixCoefficientsPython.new_itkInverseEuclideanDistanceMatrixCoefficientsQEMD3(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkInverseEuclideanDistanceMatrixCoefficientsQEMD3

# Register itkInverseEuclideanDistanceMatrixCoefficientsQEMD3 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkInverseEuclideanDistanceMatrixCoefficientsQEMD3_swigregister(itkInverseEuclideanDistanceMatrixCoefficientsQEMD3)

class itkInverseEuclideanDistanceMatrixCoefficientsQEMD4(itkMatrixCoefficientsQEMD4):
    r"""Proxy of C++ itkInverseEuclideanDistanceMatrixCoefficientsQEMD4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(self) -> itkInverseEuclideanDistanceMatrixCoefficientsQEMD4
        __init__(self, arg0) -> itkInverseEuclideanDistanceMatrixCoefficientsQEMD4

        Parameters
        ----------
        arg0: itkInverseEuclideanDistanceMatrixCoefficientsQEMD4 const &

        """
        _itkMatrixCoefficientsPython.itkInverseEuclideanDistanceMatrixCoefficientsQEMD4_swiginit(self, _itkMatrixCoefficientsPython.new_itkInverseEuclideanDistanceMatrixCoefficientsQEMD4(*args))
    __swig_destroy__ = _itkMatrixCoefficientsPython.delete_itkInverseEuclideanDistanceMatrixCoefficientsQEMD4

# Register itkInverseEuclideanDistanceMatrixCoefficientsQEMD4 in _itkMatrixCoefficientsPython:
_itkMatrixCoefficientsPython.itkInverseEuclideanDistanceMatrixCoefficientsQEMD4_swigregister(itkInverseEuclideanDistanceMatrixCoefficientsQEMD4)



