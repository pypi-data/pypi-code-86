# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKImageFeaturePython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkHessian3DToVesselnessMeasureImageFilterPython
else:
    import _itkHessian3DToVesselnessMeasureImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkHessian3DToVesselnessMeasureImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkHessian3DToVesselnessMeasureImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImageToImageFilterBPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.stdcomplexPython
import itk.itkImagePython
import itk.itkSizePython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkCovariantVectorPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkRGBAPixelPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython

def itkHessian3DToVesselnessMeasureImageFilterD_New():
    return itkHessian3DToVesselnessMeasureImageFilterD.New()

class itkHessian3DToVesselnessMeasureImageFilterD(itk.itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33ID3):
    r"""


    Line filter to provide a vesselness measure for tubular objects from
    the hessian matrix.

    The filter takes as input an image of hessian pixels
    (SymmetricSecondRankTensor pixels) and preserves pixels that have
    eigen values $ \\lambda_3 $ close to 0 and $\\lambda_2$ and
    $\\lambda_1$ as large negative values (for bright tubular
    structures).

    \\[ | \\lambda_1 | < | \\lambda_2 | < | \\lambda_3 | \\]

    Notes: The filter takes into account that the eigen values play a
    crucial role in discriminating shape and orientation of structures.

    Bright tubular structures will have low $\\lambda_1$ and large
    negative values of $\\lambda_2$ and $\\lambda_3$.

    Conversely dark tubular structures will have a low value of
    $\\lambda_1$ and large positive values of $\\lambda_2$ and
    $\\lambda_3$.

    Bright plate like structures have low values of $\\lambda_1$ and
    $\\lambda_2$ and large negative values of $\\lambda_3$

    Dark plate like structures have low values of $\\lambda_1$ and
    $\\lambda_2$ and large positive values of $\\lambda_3$

    Bright spherical (blob) like structures have all three eigen values as
    large negative numbers

    Dark spherical (blob) like structures have all three eigen values as
    large positive numbers  This filter is used to discriminate the Bright
    tubular structures.

    References: "3D Multi-scale line filter for segmentation and
    visualization of curvilinear structures in medical images", Yoshinobu
    Sato, Shin Nakajima, Hideki Atsumi, Thomas Koller, Guido Gerig,
    Shigeyuki Yoshida, Ron Kikinis.
    http://www.image.med.osaka-u.ac.jp/member/yoshi/paper/linefilter.pdf

    See:   HessianRecursiveGaussianImageFilter

    See:  SymmetricEigenAnalysisImageFilter

    See:  SymmetricSecondRankTensor 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD___New_orig__)
    Clone = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_Clone)
    SetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_SetAlpha1)
    GetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_GetAlpha1)
    SetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_SetAlpha2)
    GetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_GetAlpha2)
    DoubleConvertibleToOutputCheck = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkHessian3DToVesselnessMeasureImageFilterPython.delete_itkHessian3DToVesselnessMeasureImageFilterD
    cast = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_cast)

    def New(*args, **kargs):
        """New() -> itkHessian3DToVesselnessMeasureImageFilterD

        Create a new object of the class itkHessian3DToVesselnessMeasureImageFilterD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHessian3DToVesselnessMeasureImageFilterD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHessian3DToVesselnessMeasureImageFilterD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHessian3DToVesselnessMeasureImageFilterD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHessian3DToVesselnessMeasureImageFilterD in _itkHessian3DToVesselnessMeasureImageFilterPython:
_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_swigregister(itkHessian3DToVesselnessMeasureImageFilterD)
itkHessian3DToVesselnessMeasureImageFilterD___New_orig__ = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD___New_orig__
itkHessian3DToVesselnessMeasureImageFilterD_cast = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterD_cast


def itkHessian3DToVesselnessMeasureImageFilterF_New():
    return itkHessian3DToVesselnessMeasureImageFilterF.New()

class itkHessian3DToVesselnessMeasureImageFilterF(itk.itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33IF3):
    r"""


    Line filter to provide a vesselness measure for tubular objects from
    the hessian matrix.

    The filter takes as input an image of hessian pixels
    (SymmetricSecondRankTensor pixels) and preserves pixels that have
    eigen values $ \\lambda_3 $ close to 0 and $\\lambda_2$ and
    $\\lambda_1$ as large negative values (for bright tubular
    structures).

    \\[ | \\lambda_1 | < | \\lambda_2 | < | \\lambda_3 | \\]

    Notes: The filter takes into account that the eigen values play a
    crucial role in discriminating shape and orientation of structures.

    Bright tubular structures will have low $\\lambda_1$ and large
    negative values of $\\lambda_2$ and $\\lambda_3$.

    Conversely dark tubular structures will have a low value of
    $\\lambda_1$ and large positive values of $\\lambda_2$ and
    $\\lambda_3$.

    Bright plate like structures have low values of $\\lambda_1$ and
    $\\lambda_2$ and large negative values of $\\lambda_3$

    Dark plate like structures have low values of $\\lambda_1$ and
    $\\lambda_2$ and large positive values of $\\lambda_3$

    Bright spherical (blob) like structures have all three eigen values as
    large negative numbers

    Dark spherical (blob) like structures have all three eigen values as
    large positive numbers  This filter is used to discriminate the Bright
    tubular structures.

    References: "3D Multi-scale line filter for segmentation and
    visualization of curvilinear structures in medical images", Yoshinobu
    Sato, Shin Nakajima, Hideki Atsumi, Thomas Koller, Guido Gerig,
    Shigeyuki Yoshida, Ron Kikinis.
    http://www.image.med.osaka-u.ac.jp/member/yoshi/paper/linefilter.pdf

    See:   HessianRecursiveGaussianImageFilter

    See:  SymmetricEigenAnalysisImageFilter

    See:  SymmetricSecondRankTensor 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF___New_orig__)
    Clone = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_Clone)
    SetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_SetAlpha1)
    GetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_GetAlpha1)
    SetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_SetAlpha2)
    GetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_GetAlpha2)
    DoubleConvertibleToOutputCheck = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkHessian3DToVesselnessMeasureImageFilterPython.delete_itkHessian3DToVesselnessMeasureImageFilterF
    cast = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_cast)

    def New(*args, **kargs):
        """New() -> itkHessian3DToVesselnessMeasureImageFilterF

        Create a new object of the class itkHessian3DToVesselnessMeasureImageFilterF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHessian3DToVesselnessMeasureImageFilterF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHessian3DToVesselnessMeasureImageFilterF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHessian3DToVesselnessMeasureImageFilterF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHessian3DToVesselnessMeasureImageFilterF in _itkHessian3DToVesselnessMeasureImageFilterPython:
_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_swigregister(itkHessian3DToVesselnessMeasureImageFilterF)
itkHessian3DToVesselnessMeasureImageFilterF___New_orig__ = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF___New_orig__
itkHessian3DToVesselnessMeasureImageFilterF_cast = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterF_cast


def itkHessian3DToVesselnessMeasureImageFilterSS_New():
    return itkHessian3DToVesselnessMeasureImageFilterSS.New()

class itkHessian3DToVesselnessMeasureImageFilterSS(itk.itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33ISS3):
    r"""


    Line filter to provide a vesselness measure for tubular objects from
    the hessian matrix.

    The filter takes as input an image of hessian pixels
    (SymmetricSecondRankTensor pixels) and preserves pixels that have
    eigen values $ \\lambda_3 $ close to 0 and $\\lambda_2$ and
    $\\lambda_1$ as large negative values (for bright tubular
    structures).

    \\[ | \\lambda_1 | < | \\lambda_2 | < | \\lambda_3 | \\]

    Notes: The filter takes into account that the eigen values play a
    crucial role in discriminating shape and orientation of structures.

    Bright tubular structures will have low $\\lambda_1$ and large
    negative values of $\\lambda_2$ and $\\lambda_3$.

    Conversely dark tubular structures will have a low value of
    $\\lambda_1$ and large positive values of $\\lambda_2$ and
    $\\lambda_3$.

    Bright plate like structures have low values of $\\lambda_1$ and
    $\\lambda_2$ and large negative values of $\\lambda_3$

    Dark plate like structures have low values of $\\lambda_1$ and
    $\\lambda_2$ and large positive values of $\\lambda_3$

    Bright spherical (blob) like structures have all three eigen values as
    large negative numbers

    Dark spherical (blob) like structures have all three eigen values as
    large positive numbers  This filter is used to discriminate the Bright
    tubular structures.

    References: "3D Multi-scale line filter for segmentation and
    visualization of curvilinear structures in medical images", Yoshinobu
    Sato, Shin Nakajima, Hideki Atsumi, Thomas Koller, Guido Gerig,
    Shigeyuki Yoshida, Ron Kikinis.
    http://www.image.med.osaka-u.ac.jp/member/yoshi/paper/linefilter.pdf

    See:   HessianRecursiveGaussianImageFilter

    See:  SymmetricEigenAnalysisImageFilter

    See:  SymmetricSecondRankTensor 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS___New_orig__)
    Clone = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_Clone)
    SetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_SetAlpha1)
    GetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_GetAlpha1)
    SetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_SetAlpha2)
    GetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_GetAlpha2)
    DoubleConvertibleToOutputCheck = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkHessian3DToVesselnessMeasureImageFilterPython.delete_itkHessian3DToVesselnessMeasureImageFilterSS
    cast = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_cast)

    def New(*args, **kargs):
        """New() -> itkHessian3DToVesselnessMeasureImageFilterSS

        Create a new object of the class itkHessian3DToVesselnessMeasureImageFilterSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHessian3DToVesselnessMeasureImageFilterSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHessian3DToVesselnessMeasureImageFilterSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHessian3DToVesselnessMeasureImageFilterSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHessian3DToVesselnessMeasureImageFilterSS in _itkHessian3DToVesselnessMeasureImageFilterPython:
_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_swigregister(itkHessian3DToVesselnessMeasureImageFilterSS)
itkHessian3DToVesselnessMeasureImageFilterSS___New_orig__ = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS___New_orig__
itkHessian3DToVesselnessMeasureImageFilterSS_cast = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterSS_cast


def itkHessian3DToVesselnessMeasureImageFilterUC_New():
    return itkHessian3DToVesselnessMeasureImageFilterUC.New()

class itkHessian3DToVesselnessMeasureImageFilterUC(itk.itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33IUC3):
    r"""


    Line filter to provide a vesselness measure for tubular objects from
    the hessian matrix.

    The filter takes as input an image of hessian pixels
    (SymmetricSecondRankTensor pixels) and preserves pixels that have
    eigen values $ \\lambda_3 $ close to 0 and $\\lambda_2$ and
    $\\lambda_1$ as large negative values (for bright tubular
    structures).

    \\[ | \\lambda_1 | < | \\lambda_2 | < | \\lambda_3 | \\]

    Notes: The filter takes into account that the eigen values play a
    crucial role in discriminating shape and orientation of structures.

    Bright tubular structures will have low $\\lambda_1$ and large
    negative values of $\\lambda_2$ and $\\lambda_3$.

    Conversely dark tubular structures will have a low value of
    $\\lambda_1$ and large positive values of $\\lambda_2$ and
    $\\lambda_3$.

    Bright plate like structures have low values of $\\lambda_1$ and
    $\\lambda_2$ and large negative values of $\\lambda_3$

    Dark plate like structures have low values of $\\lambda_1$ and
    $\\lambda_2$ and large positive values of $\\lambda_3$

    Bright spherical (blob) like structures have all three eigen values as
    large negative numbers

    Dark spherical (blob) like structures have all three eigen values as
    large positive numbers  This filter is used to discriminate the Bright
    tubular structures.

    References: "3D Multi-scale line filter for segmentation and
    visualization of curvilinear structures in medical images", Yoshinobu
    Sato, Shin Nakajima, Hideki Atsumi, Thomas Koller, Guido Gerig,
    Shigeyuki Yoshida, Ron Kikinis.
    http://www.image.med.osaka-u.ac.jp/member/yoshi/paper/linefilter.pdf

    See:   HessianRecursiveGaussianImageFilter

    See:  SymmetricEigenAnalysisImageFilter

    See:  SymmetricSecondRankTensor 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC___New_orig__)
    Clone = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_Clone)
    SetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_SetAlpha1)
    GetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_GetAlpha1)
    SetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_SetAlpha2)
    GetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_GetAlpha2)
    DoubleConvertibleToOutputCheck = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkHessian3DToVesselnessMeasureImageFilterPython.delete_itkHessian3DToVesselnessMeasureImageFilterUC
    cast = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_cast)

    def New(*args, **kargs):
        """New() -> itkHessian3DToVesselnessMeasureImageFilterUC

        Create a new object of the class itkHessian3DToVesselnessMeasureImageFilterUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHessian3DToVesselnessMeasureImageFilterUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHessian3DToVesselnessMeasureImageFilterUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHessian3DToVesselnessMeasureImageFilterUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHessian3DToVesselnessMeasureImageFilterUC in _itkHessian3DToVesselnessMeasureImageFilterPython:
_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_swigregister(itkHessian3DToVesselnessMeasureImageFilterUC)
itkHessian3DToVesselnessMeasureImageFilterUC___New_orig__ = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC___New_orig__
itkHessian3DToVesselnessMeasureImageFilterUC_cast = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUC_cast


def itkHessian3DToVesselnessMeasureImageFilterUS_New():
    return itkHessian3DToVesselnessMeasureImageFilterUS.New()

class itkHessian3DToVesselnessMeasureImageFilterUS(itk.itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33IUS3):
    r"""


    Line filter to provide a vesselness measure for tubular objects from
    the hessian matrix.

    The filter takes as input an image of hessian pixels
    (SymmetricSecondRankTensor pixels) and preserves pixels that have
    eigen values $ \\lambda_3 $ close to 0 and $\\lambda_2$ and
    $\\lambda_1$ as large negative values (for bright tubular
    structures).

    \\[ | \\lambda_1 | < | \\lambda_2 | < | \\lambda_3 | \\]

    Notes: The filter takes into account that the eigen values play a
    crucial role in discriminating shape and orientation of structures.

    Bright tubular structures will have low $\\lambda_1$ and large
    negative values of $\\lambda_2$ and $\\lambda_3$.

    Conversely dark tubular structures will have a low value of
    $\\lambda_1$ and large positive values of $\\lambda_2$ and
    $\\lambda_3$.

    Bright plate like structures have low values of $\\lambda_1$ and
    $\\lambda_2$ and large negative values of $\\lambda_3$

    Dark plate like structures have low values of $\\lambda_1$ and
    $\\lambda_2$ and large positive values of $\\lambda_3$

    Bright spherical (blob) like structures have all three eigen values as
    large negative numbers

    Dark spherical (blob) like structures have all three eigen values as
    large positive numbers  This filter is used to discriminate the Bright
    tubular structures.

    References: "3D Multi-scale line filter for segmentation and
    visualization of curvilinear structures in medical images", Yoshinobu
    Sato, Shin Nakajima, Hideki Atsumi, Thomas Koller, Guido Gerig,
    Shigeyuki Yoshida, Ron Kikinis.
    http://www.image.med.osaka-u.ac.jp/member/yoshi/paper/linefilter.pdf

    See:   HessianRecursiveGaussianImageFilter

    See:  SymmetricEigenAnalysisImageFilter

    See:  SymmetricSecondRankTensor 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS___New_orig__)
    Clone = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_Clone)
    SetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_SetAlpha1)
    GetAlpha1 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_GetAlpha1)
    SetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_SetAlpha2)
    GetAlpha2 = _swig_new_instance_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_GetAlpha2)
    DoubleConvertibleToOutputCheck = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkHessian3DToVesselnessMeasureImageFilterPython.delete_itkHessian3DToVesselnessMeasureImageFilterUS
    cast = _swig_new_static_method(_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_cast)

    def New(*args, **kargs):
        """New() -> itkHessian3DToVesselnessMeasureImageFilterUS

        Create a new object of the class itkHessian3DToVesselnessMeasureImageFilterUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHessian3DToVesselnessMeasureImageFilterUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHessian3DToVesselnessMeasureImageFilterUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHessian3DToVesselnessMeasureImageFilterUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHessian3DToVesselnessMeasureImageFilterUS in _itkHessian3DToVesselnessMeasureImageFilterPython:
_itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_swigregister(itkHessian3DToVesselnessMeasureImageFilterUS)
itkHessian3DToVesselnessMeasureImageFilterUS___New_orig__ = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS___New_orig__
itkHessian3DToVesselnessMeasureImageFilterUS_cast = _itkHessian3DToVesselnessMeasureImageFilterPython.itkHessian3DToVesselnessMeasureImageFilterUS_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def hessian3_d_to_vesselness_measure_image_filter(*args: itkt.ImageLike,  alpha1: float=..., alpha2: float=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for Hessian3DToVesselnessMeasureImageFilter"""
    import itk

    kwarg_typehints = { 'alpha1':alpha1,'alpha2':alpha2 }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.Hessian3DToVesselnessMeasureImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def hessian3_d_to_vesselness_measure_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageFeature.Hessian3DToVesselnessMeasureImageFilter
    hessian3_d_to_vesselness_measure_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    hessian3_d_to_vesselness_measure_image_filter.__doc__ = filter_object.__doc__




