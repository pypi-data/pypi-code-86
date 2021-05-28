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
    from . import _itkGaussianOperatorPython
else:
    import _itkGaussianOperatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkGaussianOperatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkGaussianOperatorPython.SWIG_PyStaticMethod_New

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
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkNeighborhoodOperatorPython
import itk.itkNeighborhoodPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkFixedArrayPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkCovariantVectorPython
import itk.itkRGBPixelPython
class itkGaussianOperatorD2(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    r"""


    A NeighborhoodOperator whose coefficients are a one dimensional,
    discrete Gaussian kernel.

    GaussianOperator can be used to perform Gaussian blurring by taking
    its inner product with a Neighborhood (NeighborhoodIterator) that is
    swept across an image region. It is a directional operator. N
    successive applications oriented along each dimensional direction will
    effect separable, efficient, N-D Gaussian blurring of an image region.

    GaussianOperator takes two parameters:

    (1) The floating-point variance of the desired Gaussian function.

    (2) The "maximum error" allowed in the discrete Gaussian function.
    "Maximum errror" is defined as the difference between the area under
    the discrete Gaussian curve and the area under the continuous
    Gaussian. Maximum error affects the Gaussian operator size. Care
    should be taken not to make this value too small relative to the
    variance lest the operator size become unreasonably large.

    References: The Gaussian kernel contained in this operator was
    described by Tony Lindeberg (Discrete Scale-Space Theory and the
    Scale-Space Primal Sketch. Dissertation. Royal Institute of
    Technology, Stockholm, Sweden. May 1991.).

    GaussianOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetVariance = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD2_SetVariance)
    SetMaximumError = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD2_SetMaximumError)
    GetVariance = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD2_GetVariance)
    GetMaximumError = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD2_GetMaximumError)
    SetMaximumKernelWidth = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD2_SetMaximumKernelWidth)
    GetMaximumKernelWidth = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD2_GetMaximumKernelWidth)
    ModifiedBesselI0 = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD2_ModifiedBesselI0)
    ModifiedBesselI1 = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD2_ModifiedBesselI1)
    ModifiedBesselI = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD2_ModifiedBesselI)
    __swig_destroy__ = _itkGaussianOperatorPython.delete_itkGaussianOperatorD2

    def __init__(self, *args):
        r"""
        __init__(self) -> itkGaussianOperatorD2
        __init__(self, arg0) -> itkGaussianOperatorD2

        Parameters
        ----------
        arg0: itkGaussianOperatorD2 const &



        A NeighborhoodOperator whose coefficients are a one dimensional,
        discrete Gaussian kernel.

        GaussianOperator can be used to perform Gaussian blurring by taking
        its inner product with a Neighborhood (NeighborhoodIterator) that is
        swept across an image region. It is a directional operator. N
        successive applications oriented along each dimensional direction will
        effect separable, efficient, N-D Gaussian blurring of an image region.

        GaussianOperator takes two parameters:

        (1) The floating-point variance of the desired Gaussian function.

        (2) The "maximum error" allowed in the discrete Gaussian function.
        "Maximum errror" is defined as the difference between the area under
        the discrete Gaussian curve and the area under the continuous
        Gaussian. Maximum error affects the Gaussian operator size. Care
        should be taken not to make this value too small relative to the
        variance lest the operator size become unreasonably large.

        References: The Gaussian kernel contained in this operator was
        described by Tony Lindeberg (Discrete Scale-Space Theory and the
        Scale-Space Primal Sketch. Dissertation. Royal Institute of
        Technology, Stockholm, Sweden. May 1991.).

        GaussianOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood 
        """
        _itkGaussianOperatorPython.itkGaussianOperatorD2_swiginit(self, _itkGaussianOperatorPython.new_itkGaussianOperatorD2(*args))

# Register itkGaussianOperatorD2 in _itkGaussianOperatorPython:
_itkGaussianOperatorPython.itkGaussianOperatorD2_swigregister(itkGaussianOperatorD2)

class itkGaussianOperatorD3(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    r"""


    A NeighborhoodOperator whose coefficients are a one dimensional,
    discrete Gaussian kernel.

    GaussianOperator can be used to perform Gaussian blurring by taking
    its inner product with a Neighborhood (NeighborhoodIterator) that is
    swept across an image region. It is a directional operator. N
    successive applications oriented along each dimensional direction will
    effect separable, efficient, N-D Gaussian blurring of an image region.

    GaussianOperator takes two parameters:

    (1) The floating-point variance of the desired Gaussian function.

    (2) The "maximum error" allowed in the discrete Gaussian function.
    "Maximum errror" is defined as the difference between the area under
    the discrete Gaussian curve and the area under the continuous
    Gaussian. Maximum error affects the Gaussian operator size. Care
    should be taken not to make this value too small relative to the
    variance lest the operator size become unreasonably large.

    References: The Gaussian kernel contained in this operator was
    described by Tony Lindeberg (Discrete Scale-Space Theory and the
    Scale-Space Primal Sketch. Dissertation. Royal Institute of
    Technology, Stockholm, Sweden. May 1991.).

    GaussianOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetVariance = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD3_SetVariance)
    SetMaximumError = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD3_SetMaximumError)
    GetVariance = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD3_GetVariance)
    GetMaximumError = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD3_GetMaximumError)
    SetMaximumKernelWidth = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD3_SetMaximumKernelWidth)
    GetMaximumKernelWidth = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD3_GetMaximumKernelWidth)
    ModifiedBesselI0 = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD3_ModifiedBesselI0)
    ModifiedBesselI1 = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD3_ModifiedBesselI1)
    ModifiedBesselI = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD3_ModifiedBesselI)
    __swig_destroy__ = _itkGaussianOperatorPython.delete_itkGaussianOperatorD3

    def __init__(self, *args):
        r"""
        __init__(self) -> itkGaussianOperatorD3
        __init__(self, arg0) -> itkGaussianOperatorD3

        Parameters
        ----------
        arg0: itkGaussianOperatorD3 const &



        A NeighborhoodOperator whose coefficients are a one dimensional,
        discrete Gaussian kernel.

        GaussianOperator can be used to perform Gaussian blurring by taking
        its inner product with a Neighborhood (NeighborhoodIterator) that is
        swept across an image region. It is a directional operator. N
        successive applications oriented along each dimensional direction will
        effect separable, efficient, N-D Gaussian blurring of an image region.

        GaussianOperator takes two parameters:

        (1) The floating-point variance of the desired Gaussian function.

        (2) The "maximum error" allowed in the discrete Gaussian function.
        "Maximum errror" is defined as the difference between the area under
        the discrete Gaussian curve and the area under the continuous
        Gaussian. Maximum error affects the Gaussian operator size. Care
        should be taken not to make this value too small relative to the
        variance lest the operator size become unreasonably large.

        References: The Gaussian kernel contained in this operator was
        described by Tony Lindeberg (Discrete Scale-Space Theory and the
        Scale-Space Primal Sketch. Dissertation. Royal Institute of
        Technology, Stockholm, Sweden. May 1991.).

        GaussianOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood 
        """
        _itkGaussianOperatorPython.itkGaussianOperatorD3_swiginit(self, _itkGaussianOperatorPython.new_itkGaussianOperatorD3(*args))

# Register itkGaussianOperatorD3 in _itkGaussianOperatorPython:
_itkGaussianOperatorPython.itkGaussianOperatorD3_swigregister(itkGaussianOperatorD3)

class itkGaussianOperatorD4(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD4):
    r"""


    A NeighborhoodOperator whose coefficients are a one dimensional,
    discrete Gaussian kernel.

    GaussianOperator can be used to perform Gaussian blurring by taking
    its inner product with a Neighborhood (NeighborhoodIterator) that is
    swept across an image region. It is a directional operator. N
    successive applications oriented along each dimensional direction will
    effect separable, efficient, N-D Gaussian blurring of an image region.

    GaussianOperator takes two parameters:

    (1) The floating-point variance of the desired Gaussian function.

    (2) The "maximum error" allowed in the discrete Gaussian function.
    "Maximum errror" is defined as the difference between the area under
    the discrete Gaussian curve and the area under the continuous
    Gaussian. Maximum error affects the Gaussian operator size. Care
    should be taken not to make this value too small relative to the
    variance lest the operator size become unreasonably large.

    References: The Gaussian kernel contained in this operator was
    described by Tony Lindeberg (Discrete Scale-Space Theory and the
    Scale-Space Primal Sketch. Dissertation. Royal Institute of
    Technology, Stockholm, Sweden. May 1991.).

    GaussianOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetVariance = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD4_SetVariance)
    SetMaximumError = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD4_SetMaximumError)
    GetVariance = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD4_GetVariance)
    GetMaximumError = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD4_GetMaximumError)
    SetMaximumKernelWidth = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD4_SetMaximumKernelWidth)
    GetMaximumKernelWidth = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD4_GetMaximumKernelWidth)
    ModifiedBesselI0 = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD4_ModifiedBesselI0)
    ModifiedBesselI1 = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD4_ModifiedBesselI1)
    ModifiedBesselI = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorD4_ModifiedBesselI)
    __swig_destroy__ = _itkGaussianOperatorPython.delete_itkGaussianOperatorD4

    def __init__(self, *args):
        r"""
        __init__(self) -> itkGaussianOperatorD4
        __init__(self, arg0) -> itkGaussianOperatorD4

        Parameters
        ----------
        arg0: itkGaussianOperatorD4 const &



        A NeighborhoodOperator whose coefficients are a one dimensional,
        discrete Gaussian kernel.

        GaussianOperator can be used to perform Gaussian blurring by taking
        its inner product with a Neighborhood (NeighborhoodIterator) that is
        swept across an image region. It is a directional operator. N
        successive applications oriented along each dimensional direction will
        effect separable, efficient, N-D Gaussian blurring of an image region.

        GaussianOperator takes two parameters:

        (1) The floating-point variance of the desired Gaussian function.

        (2) The "maximum error" allowed in the discrete Gaussian function.
        "Maximum errror" is defined as the difference between the area under
        the discrete Gaussian curve and the area under the continuous
        Gaussian. Maximum error affects the Gaussian operator size. Care
        should be taken not to make this value too small relative to the
        variance lest the operator size become unreasonably large.

        References: The Gaussian kernel contained in this operator was
        described by Tony Lindeberg (Discrete Scale-Space Theory and the
        Scale-Space Primal Sketch. Dissertation. Royal Institute of
        Technology, Stockholm, Sweden. May 1991.).

        GaussianOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood 
        """
        _itkGaussianOperatorPython.itkGaussianOperatorD4_swiginit(self, _itkGaussianOperatorPython.new_itkGaussianOperatorD4(*args))

# Register itkGaussianOperatorD4 in _itkGaussianOperatorPython:
_itkGaussianOperatorPython.itkGaussianOperatorD4_swigregister(itkGaussianOperatorD4)

class itkGaussianOperatorF2(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    r"""


    A NeighborhoodOperator whose coefficients are a one dimensional,
    discrete Gaussian kernel.

    GaussianOperator can be used to perform Gaussian blurring by taking
    its inner product with a Neighborhood (NeighborhoodIterator) that is
    swept across an image region. It is a directional operator. N
    successive applications oriented along each dimensional direction will
    effect separable, efficient, N-D Gaussian blurring of an image region.

    GaussianOperator takes two parameters:

    (1) The floating-point variance of the desired Gaussian function.

    (2) The "maximum error" allowed in the discrete Gaussian function.
    "Maximum errror" is defined as the difference between the area under
    the discrete Gaussian curve and the area under the continuous
    Gaussian. Maximum error affects the Gaussian operator size. Care
    should be taken not to make this value too small relative to the
    variance lest the operator size become unreasonably large.

    References: The Gaussian kernel contained in this operator was
    described by Tony Lindeberg (Discrete Scale-Space Theory and the
    Scale-Space Primal Sketch. Dissertation. Royal Institute of
    Technology, Stockholm, Sweden. May 1991.).

    GaussianOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetVariance = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF2_SetVariance)
    SetMaximumError = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF2_SetMaximumError)
    GetVariance = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF2_GetVariance)
    GetMaximumError = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF2_GetMaximumError)
    SetMaximumKernelWidth = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF2_SetMaximumKernelWidth)
    GetMaximumKernelWidth = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF2_GetMaximumKernelWidth)
    ModifiedBesselI0 = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF2_ModifiedBesselI0)
    ModifiedBesselI1 = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF2_ModifiedBesselI1)
    ModifiedBesselI = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF2_ModifiedBesselI)
    __swig_destroy__ = _itkGaussianOperatorPython.delete_itkGaussianOperatorF2

    def __init__(self, *args):
        r"""
        __init__(self) -> itkGaussianOperatorF2
        __init__(self, arg0) -> itkGaussianOperatorF2

        Parameters
        ----------
        arg0: itkGaussianOperatorF2 const &



        A NeighborhoodOperator whose coefficients are a one dimensional,
        discrete Gaussian kernel.

        GaussianOperator can be used to perform Gaussian blurring by taking
        its inner product with a Neighborhood (NeighborhoodIterator) that is
        swept across an image region. It is a directional operator. N
        successive applications oriented along each dimensional direction will
        effect separable, efficient, N-D Gaussian blurring of an image region.

        GaussianOperator takes two parameters:

        (1) The floating-point variance of the desired Gaussian function.

        (2) The "maximum error" allowed in the discrete Gaussian function.
        "Maximum errror" is defined as the difference between the area under
        the discrete Gaussian curve and the area under the continuous
        Gaussian. Maximum error affects the Gaussian operator size. Care
        should be taken not to make this value too small relative to the
        variance lest the operator size become unreasonably large.

        References: The Gaussian kernel contained in this operator was
        described by Tony Lindeberg (Discrete Scale-Space Theory and the
        Scale-Space Primal Sketch. Dissertation. Royal Institute of
        Technology, Stockholm, Sweden. May 1991.).

        GaussianOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood 
        """
        _itkGaussianOperatorPython.itkGaussianOperatorF2_swiginit(self, _itkGaussianOperatorPython.new_itkGaussianOperatorF2(*args))

# Register itkGaussianOperatorF2 in _itkGaussianOperatorPython:
_itkGaussianOperatorPython.itkGaussianOperatorF2_swigregister(itkGaussianOperatorF2)

class itkGaussianOperatorF3(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    r"""


    A NeighborhoodOperator whose coefficients are a one dimensional,
    discrete Gaussian kernel.

    GaussianOperator can be used to perform Gaussian blurring by taking
    its inner product with a Neighborhood (NeighborhoodIterator) that is
    swept across an image region. It is a directional operator. N
    successive applications oriented along each dimensional direction will
    effect separable, efficient, N-D Gaussian blurring of an image region.

    GaussianOperator takes two parameters:

    (1) The floating-point variance of the desired Gaussian function.

    (2) The "maximum error" allowed in the discrete Gaussian function.
    "Maximum errror" is defined as the difference between the area under
    the discrete Gaussian curve and the area under the continuous
    Gaussian. Maximum error affects the Gaussian operator size. Care
    should be taken not to make this value too small relative to the
    variance lest the operator size become unreasonably large.

    References: The Gaussian kernel contained in this operator was
    described by Tony Lindeberg (Discrete Scale-Space Theory and the
    Scale-Space Primal Sketch. Dissertation. Royal Institute of
    Technology, Stockholm, Sweden. May 1991.).

    GaussianOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetVariance = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF3_SetVariance)
    SetMaximumError = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF3_SetMaximumError)
    GetVariance = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF3_GetVariance)
    GetMaximumError = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF3_GetMaximumError)
    SetMaximumKernelWidth = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF3_SetMaximumKernelWidth)
    GetMaximumKernelWidth = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF3_GetMaximumKernelWidth)
    ModifiedBesselI0 = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF3_ModifiedBesselI0)
    ModifiedBesselI1 = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF3_ModifiedBesselI1)
    ModifiedBesselI = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF3_ModifiedBesselI)
    __swig_destroy__ = _itkGaussianOperatorPython.delete_itkGaussianOperatorF3

    def __init__(self, *args):
        r"""
        __init__(self) -> itkGaussianOperatorF3
        __init__(self, arg0) -> itkGaussianOperatorF3

        Parameters
        ----------
        arg0: itkGaussianOperatorF3 const &



        A NeighborhoodOperator whose coefficients are a one dimensional,
        discrete Gaussian kernel.

        GaussianOperator can be used to perform Gaussian blurring by taking
        its inner product with a Neighborhood (NeighborhoodIterator) that is
        swept across an image region. It is a directional operator. N
        successive applications oriented along each dimensional direction will
        effect separable, efficient, N-D Gaussian blurring of an image region.

        GaussianOperator takes two parameters:

        (1) The floating-point variance of the desired Gaussian function.

        (2) The "maximum error" allowed in the discrete Gaussian function.
        "Maximum errror" is defined as the difference between the area under
        the discrete Gaussian curve and the area under the continuous
        Gaussian. Maximum error affects the Gaussian operator size. Care
        should be taken not to make this value too small relative to the
        variance lest the operator size become unreasonably large.

        References: The Gaussian kernel contained in this operator was
        described by Tony Lindeberg (Discrete Scale-Space Theory and the
        Scale-Space Primal Sketch. Dissertation. Royal Institute of
        Technology, Stockholm, Sweden. May 1991.).

        GaussianOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood 
        """
        _itkGaussianOperatorPython.itkGaussianOperatorF3_swiginit(self, _itkGaussianOperatorPython.new_itkGaussianOperatorF3(*args))

# Register itkGaussianOperatorF3 in _itkGaussianOperatorPython:
_itkGaussianOperatorPython.itkGaussianOperatorF3_swigregister(itkGaussianOperatorF3)

class itkGaussianOperatorF4(itk.itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF4):
    r"""


    A NeighborhoodOperator whose coefficients are a one dimensional,
    discrete Gaussian kernel.

    GaussianOperator can be used to perform Gaussian blurring by taking
    its inner product with a Neighborhood (NeighborhoodIterator) that is
    swept across an image region. It is a directional operator. N
    successive applications oriented along each dimensional direction will
    effect separable, efficient, N-D Gaussian blurring of an image region.

    GaussianOperator takes two parameters:

    (1) The floating-point variance of the desired Gaussian function.

    (2) The "maximum error" allowed in the discrete Gaussian function.
    "Maximum errror" is defined as the difference between the area under
    the discrete Gaussian curve and the area under the continuous
    Gaussian. Maximum error affects the Gaussian operator size. Care
    should be taken not to make this value too small relative to the
    variance lest the operator size become unreasonably large.

    References: The Gaussian kernel contained in this operator was
    described by Tony Lindeberg (Discrete Scale-Space Theory and the
    Scale-Space Primal Sketch. Dissertation. Royal Institute of
    Technology, Stockholm, Sweden. May 1991.).

    GaussianOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    SetVariance = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF4_SetVariance)
    SetMaximumError = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF4_SetMaximumError)
    GetVariance = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF4_GetVariance)
    GetMaximumError = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF4_GetMaximumError)
    SetMaximumKernelWidth = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF4_SetMaximumKernelWidth)
    GetMaximumKernelWidth = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF4_GetMaximumKernelWidth)
    ModifiedBesselI0 = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF4_ModifiedBesselI0)
    ModifiedBesselI1 = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF4_ModifiedBesselI1)
    ModifiedBesselI = _swig_new_instance_method(_itkGaussianOperatorPython.itkGaussianOperatorF4_ModifiedBesselI)
    __swig_destroy__ = _itkGaussianOperatorPython.delete_itkGaussianOperatorF4

    def __init__(self, *args):
        r"""
        __init__(self) -> itkGaussianOperatorF4
        __init__(self, arg0) -> itkGaussianOperatorF4

        Parameters
        ----------
        arg0: itkGaussianOperatorF4 const &



        A NeighborhoodOperator whose coefficients are a one dimensional,
        discrete Gaussian kernel.

        GaussianOperator can be used to perform Gaussian blurring by taking
        its inner product with a Neighborhood (NeighborhoodIterator) that is
        swept across an image region. It is a directional operator. N
        successive applications oriented along each dimensional direction will
        effect separable, efficient, N-D Gaussian blurring of an image region.

        GaussianOperator takes two parameters:

        (1) The floating-point variance of the desired Gaussian function.

        (2) The "maximum error" allowed in the discrete Gaussian function.
        "Maximum errror" is defined as the difference between the area under
        the discrete Gaussian curve and the area under the continuous
        Gaussian. Maximum error affects the Gaussian operator size. Care
        should be taken not to make this value too small relative to the
        variance lest the operator size become unreasonably large.

        References: The Gaussian kernel contained in this operator was
        described by Tony Lindeberg (Discrete Scale-Space Theory and the
        Scale-Space Primal Sketch. Dissertation. Royal Institute of
        Technology, Stockholm, Sweden. May 1991.).

        GaussianOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood 
        """
        _itkGaussianOperatorPython.itkGaussianOperatorF4_swiginit(self, _itkGaussianOperatorPython.new_itkGaussianOperatorF4(*args))

# Register itkGaussianOperatorF4 in _itkGaussianOperatorPython:
_itkGaussianOperatorPython.itkGaussianOperatorF4_swigregister(itkGaussianOperatorF4)



