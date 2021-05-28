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
    from . import _itkImageKernelOperatorPython
else:
    import _itkImageKernelOperatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkImageKernelOperatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkImageKernelOperatorPython.SWIG_PyStaticMethod_New

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
import itk.itkNeighborhoodOperatorPython
import itk.itkNeighborhoodPython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.itkCovariantVectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkSizePython
import itk.ITKCommonBasePython
import itk.itkOffsetPython
import itk.itkImagePython
import itk.itkIndexPython
import itk.itkPointPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkImageRegionPython
import itk.itkRGBAPixelPython
class itkImageKernelOperatorD2(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    r"""


    A NeighborhoodOperator whose coefficients are from an image.

    This code was contributed in the Insight Journal paper:

    "Image Kernel Convolution" by Tustison N., Gee
    J.https://www.insight-journal.org/browse/publication/208

    ImageKernelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetImageKernel = _swig_new_instance_method(_itkImageKernelOperatorPython.itkImageKernelOperatorD2_SetImageKernel)
    GetImageKernel = _swig_new_instance_method(_itkImageKernelOperatorPython.itkImageKernelOperatorD2_GetImageKernel)
    __swig_destroy__ = _itkImageKernelOperatorPython.delete_itkImageKernelOperatorD2

    def __init__(self, *args):
        r"""
        __init__(self, arg0) -> itkImageKernelOperatorD2

        Parameters
        ----------
        arg0: itkImageKernelOperatorD2 const &

        __init__(self) -> itkImageKernelOperatorD2


        A NeighborhoodOperator whose coefficients are from an image.

        This code was contributed in the Insight Journal paper:

        "Image Kernel Convolution" by Tustison N., Gee
        J.https://www.insight-journal.org/browse/publication/208

        ImageKernelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood 
        """
        _itkImageKernelOperatorPython.itkImageKernelOperatorD2_swiginit(self, _itkImageKernelOperatorPython.new_itkImageKernelOperatorD2(*args))

# Register itkImageKernelOperatorD2 in _itkImageKernelOperatorPython:
_itkImageKernelOperatorPython.itkImageKernelOperatorD2_swigregister(itkImageKernelOperatorD2)

class itkImageKernelOperatorD3(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    r"""


    A NeighborhoodOperator whose coefficients are from an image.

    This code was contributed in the Insight Journal paper:

    "Image Kernel Convolution" by Tustison N., Gee
    J.https://www.insight-journal.org/browse/publication/208

    ImageKernelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetImageKernel = _swig_new_instance_method(_itkImageKernelOperatorPython.itkImageKernelOperatorD3_SetImageKernel)
    GetImageKernel = _swig_new_instance_method(_itkImageKernelOperatorPython.itkImageKernelOperatorD3_GetImageKernel)
    __swig_destroy__ = _itkImageKernelOperatorPython.delete_itkImageKernelOperatorD3

    def __init__(self, *args):
        r"""
        __init__(self, arg0) -> itkImageKernelOperatorD3

        Parameters
        ----------
        arg0: itkImageKernelOperatorD3 const &

        __init__(self) -> itkImageKernelOperatorD3


        A NeighborhoodOperator whose coefficients are from an image.

        This code was contributed in the Insight Journal paper:

        "Image Kernel Convolution" by Tustison N., Gee
        J.https://www.insight-journal.org/browse/publication/208

        ImageKernelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood 
        """
        _itkImageKernelOperatorPython.itkImageKernelOperatorD3_swiginit(self, _itkImageKernelOperatorPython.new_itkImageKernelOperatorD3(*args))

# Register itkImageKernelOperatorD3 in _itkImageKernelOperatorPython:
_itkImageKernelOperatorPython.itkImageKernelOperatorD3_swigregister(itkImageKernelOperatorD3)

class itkImageKernelOperatorD4(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4):
    r"""


    A NeighborhoodOperator whose coefficients are from an image.

    This code was contributed in the Insight Journal paper:

    "Image Kernel Convolution" by Tustison N., Gee
    J.https://www.insight-journal.org/browse/publication/208

    ImageKernelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetImageKernel = _swig_new_instance_method(_itkImageKernelOperatorPython.itkImageKernelOperatorD4_SetImageKernel)
    GetImageKernel = _swig_new_instance_method(_itkImageKernelOperatorPython.itkImageKernelOperatorD4_GetImageKernel)
    __swig_destroy__ = _itkImageKernelOperatorPython.delete_itkImageKernelOperatorD4

    def __init__(self, *args):
        r"""
        __init__(self, arg0) -> itkImageKernelOperatorD4

        Parameters
        ----------
        arg0: itkImageKernelOperatorD4 const &

        __init__(self) -> itkImageKernelOperatorD4


        A NeighborhoodOperator whose coefficients are from an image.

        This code was contributed in the Insight Journal paper:

        "Image Kernel Convolution" by Tustison N., Gee
        J.https://www.insight-journal.org/browse/publication/208

        ImageKernelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood 
        """
        _itkImageKernelOperatorPython.itkImageKernelOperatorD4_swiginit(self, _itkImageKernelOperatorPython.new_itkImageKernelOperatorD4(*args))

# Register itkImageKernelOperatorD4 in _itkImageKernelOperatorPython:
_itkImageKernelOperatorPython.itkImageKernelOperatorD4_swigregister(itkImageKernelOperatorD4)

class itkImageKernelOperatorF2(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    r"""


    A NeighborhoodOperator whose coefficients are from an image.

    This code was contributed in the Insight Journal paper:

    "Image Kernel Convolution" by Tustison N., Gee
    J.https://www.insight-journal.org/browse/publication/208

    ImageKernelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetImageKernel = _swig_new_instance_method(_itkImageKernelOperatorPython.itkImageKernelOperatorF2_SetImageKernel)
    GetImageKernel = _swig_new_instance_method(_itkImageKernelOperatorPython.itkImageKernelOperatorF2_GetImageKernel)
    __swig_destroy__ = _itkImageKernelOperatorPython.delete_itkImageKernelOperatorF2

    def __init__(self, *args):
        r"""
        __init__(self, arg0) -> itkImageKernelOperatorF2

        Parameters
        ----------
        arg0: itkImageKernelOperatorF2 const &

        __init__(self) -> itkImageKernelOperatorF2


        A NeighborhoodOperator whose coefficients are from an image.

        This code was contributed in the Insight Journal paper:

        "Image Kernel Convolution" by Tustison N., Gee
        J.https://www.insight-journal.org/browse/publication/208

        ImageKernelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood 
        """
        _itkImageKernelOperatorPython.itkImageKernelOperatorF2_swiginit(self, _itkImageKernelOperatorPython.new_itkImageKernelOperatorF2(*args))

# Register itkImageKernelOperatorF2 in _itkImageKernelOperatorPython:
_itkImageKernelOperatorPython.itkImageKernelOperatorF2_swigregister(itkImageKernelOperatorF2)

class itkImageKernelOperatorF3(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    r"""


    A NeighborhoodOperator whose coefficients are from an image.

    This code was contributed in the Insight Journal paper:

    "Image Kernel Convolution" by Tustison N., Gee
    J.https://www.insight-journal.org/browse/publication/208

    ImageKernelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetImageKernel = _swig_new_instance_method(_itkImageKernelOperatorPython.itkImageKernelOperatorF3_SetImageKernel)
    GetImageKernel = _swig_new_instance_method(_itkImageKernelOperatorPython.itkImageKernelOperatorF3_GetImageKernel)
    __swig_destroy__ = _itkImageKernelOperatorPython.delete_itkImageKernelOperatorF3

    def __init__(self, *args):
        r"""
        __init__(self, arg0) -> itkImageKernelOperatorF3

        Parameters
        ----------
        arg0: itkImageKernelOperatorF3 const &

        __init__(self) -> itkImageKernelOperatorF3


        A NeighborhoodOperator whose coefficients are from an image.

        This code was contributed in the Insight Journal paper:

        "Image Kernel Convolution" by Tustison N., Gee
        J.https://www.insight-journal.org/browse/publication/208

        ImageKernelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood 
        """
        _itkImageKernelOperatorPython.itkImageKernelOperatorF3_swiginit(self, _itkImageKernelOperatorPython.new_itkImageKernelOperatorF3(*args))

# Register itkImageKernelOperatorF3 in _itkImageKernelOperatorPython:
_itkImageKernelOperatorPython.itkImageKernelOperatorF3_swigregister(itkImageKernelOperatorF3)

class itkImageKernelOperatorF4(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4):
    r"""


    A NeighborhoodOperator whose coefficients are from an image.

    This code was contributed in the Insight Journal paper:

    "Image Kernel Convolution" by Tustison N., Gee
    J.https://www.insight-journal.org/browse/publication/208

    ImageKernelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetImageKernel = _swig_new_instance_method(_itkImageKernelOperatorPython.itkImageKernelOperatorF4_SetImageKernel)
    GetImageKernel = _swig_new_instance_method(_itkImageKernelOperatorPython.itkImageKernelOperatorF4_GetImageKernel)
    __swig_destroy__ = _itkImageKernelOperatorPython.delete_itkImageKernelOperatorF4

    def __init__(self, *args):
        r"""
        __init__(self, arg0) -> itkImageKernelOperatorF4

        Parameters
        ----------
        arg0: itkImageKernelOperatorF4 const &

        __init__(self) -> itkImageKernelOperatorF4


        A NeighborhoodOperator whose coefficients are from an image.

        This code was contributed in the Insight Journal paper:

        "Image Kernel Convolution" by Tustison N., Gee
        J.https://www.insight-journal.org/browse/publication/208

        ImageKernelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood 
        """
        _itkImageKernelOperatorPython.itkImageKernelOperatorF4_swiginit(self, _itkImageKernelOperatorPython.new_itkImageKernelOperatorF4(*args))

# Register itkImageKernelOperatorF4 in _itkImageKernelOperatorPython:
_itkImageKernelOperatorPython.itkImageKernelOperatorF4_swigregister(itkImageKernelOperatorF4)



