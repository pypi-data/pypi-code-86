# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKBinaryMathematicalMorphologyPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkBinaryPruningImageFilterPython
else:
    import _itkBinaryPruningImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBinaryPruningImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBinaryPruningImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.stdcomplexPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkCovariantVectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkPointPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkImageRegionPython
import itk.itkRGBAPixelPython
import itk.itkImageToImageFilterAPython
import itk.itkImageToImageFilterCommonPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython

def itkBinaryPruningImageFilterID2ID2_New():
    return itkBinaryPruningImageFilterID2ID2.New()

class itkBinaryPruningImageFilterID2ID2(itk.itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""


    This filter removes "spurs" of less than a certain length in the
    input image.

    This class is parameterized over the type of the input image and the
    type of the output image.

    The input is assumed to be a binary image.

    This filter is a sequential pruning algorithm and known to be
    computational time dependable of the image size. The algorithm is the
    N-dimensional version of that given for two dimensions in:

    Rafael C. Gonzales and Richard E. Woods. Digital Image Processing.
    Addison Wesley, 491-494, (1993).

    See:  MorphologyImageFilter

    See:   BinaryErodeImageFilter

    See:   BinaryDilateImageFilter

    See:   BinaryThinningImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_Clone)
    GetPruning = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_GetPruning)
    SetIteration = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_SetIteration)
    GetIteration = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_GetIteration)
    SameDimensionCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_SameDimensionCheck
    
    SameTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_SameTypeCheck
    
    AdditiveOperatorsCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_AdditiveOperatorsCheck
    
    IntConvertibleToPixelTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_IntConvertibleToPixelTypeCheck
    
    PixelLessThanIntCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_PixelLessThanIntCheck
    
    __swig_destroy__ = _itkBinaryPruningImageFilterPython.delete_itkBinaryPruningImageFilterID2ID2
    cast = _swig_new_static_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryPruningImageFilterID2ID2

        Create a new object of the class itkBinaryPruningImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryPruningImageFilterID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBinaryPruningImageFilterID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBinaryPruningImageFilterID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryPruningImageFilterID2ID2 in _itkBinaryPruningImageFilterPython:
_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_swigregister(itkBinaryPruningImageFilterID2ID2)
itkBinaryPruningImageFilterID2ID2___New_orig__ = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2___New_orig__
itkBinaryPruningImageFilterID2ID2_cast = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterID2ID2_cast


def itkBinaryPruningImageFilterIF2IF2_New():
    return itkBinaryPruningImageFilterIF2IF2.New()

class itkBinaryPruningImageFilterIF2IF2(itk.itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""


    This filter removes "spurs" of less than a certain length in the
    input image.

    This class is parameterized over the type of the input image and the
    type of the output image.

    The input is assumed to be a binary image.

    This filter is a sequential pruning algorithm and known to be
    computational time dependable of the image size. The algorithm is the
    N-dimensional version of that given for two dimensions in:

    Rafael C. Gonzales and Richard E. Woods. Digital Image Processing.
    Addison Wesley, 491-494, (1993).

    See:  MorphologyImageFilter

    See:   BinaryErodeImageFilter

    See:   BinaryDilateImageFilter

    See:   BinaryThinningImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_Clone)
    GetPruning = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_GetPruning)
    SetIteration = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_SetIteration)
    GetIteration = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_GetIteration)
    SameDimensionCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_SameDimensionCheck
    
    SameTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_SameTypeCheck
    
    AdditiveOperatorsCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_AdditiveOperatorsCheck
    
    IntConvertibleToPixelTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_IntConvertibleToPixelTypeCheck
    
    PixelLessThanIntCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_PixelLessThanIntCheck
    
    __swig_destroy__ = _itkBinaryPruningImageFilterPython.delete_itkBinaryPruningImageFilterIF2IF2
    cast = _swig_new_static_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryPruningImageFilterIF2IF2

        Create a new object of the class itkBinaryPruningImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryPruningImageFilterIF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBinaryPruningImageFilterIF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBinaryPruningImageFilterIF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryPruningImageFilterIF2IF2 in _itkBinaryPruningImageFilterPython:
_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_swigregister(itkBinaryPruningImageFilterIF2IF2)
itkBinaryPruningImageFilterIF2IF2___New_orig__ = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2___New_orig__
itkBinaryPruningImageFilterIF2IF2_cast = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIF2IF2_cast


def itkBinaryPruningImageFilterIUC2IUC2_New():
    return itkBinaryPruningImageFilterIUC2IUC2.New()

class itkBinaryPruningImageFilterIUC2IUC2(itk.itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    r"""


    This filter removes "spurs" of less than a certain length in the
    input image.

    This class is parameterized over the type of the input image and the
    type of the output image.

    The input is assumed to be a binary image.

    This filter is a sequential pruning algorithm and known to be
    computational time dependable of the image size. The algorithm is the
    N-dimensional version of that given for two dimensions in:

    Rafael C. Gonzales and Richard E. Woods. Digital Image Processing.
    Addison Wesley, 491-494, (1993).

    See:  MorphologyImageFilter

    See:   BinaryErodeImageFilter

    See:   BinaryDilateImageFilter

    See:   BinaryThinningImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_Clone)
    GetPruning = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_GetPruning)
    SetIteration = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_SetIteration)
    GetIteration = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_GetIteration)
    SameDimensionCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_SameDimensionCheck
    
    SameTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_SameTypeCheck
    
    AdditiveOperatorsCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_AdditiveOperatorsCheck
    
    IntConvertibleToPixelTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_IntConvertibleToPixelTypeCheck
    
    PixelLessThanIntCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_PixelLessThanIntCheck
    
    __swig_destroy__ = _itkBinaryPruningImageFilterPython.delete_itkBinaryPruningImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryPruningImageFilterIUC2IUC2

        Create a new object of the class itkBinaryPruningImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryPruningImageFilterIUC2IUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBinaryPruningImageFilterIUC2IUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBinaryPruningImageFilterIUC2IUC2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryPruningImageFilterIUC2IUC2 in _itkBinaryPruningImageFilterPython:
_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_swigregister(itkBinaryPruningImageFilterIUC2IUC2)
itkBinaryPruningImageFilterIUC2IUC2___New_orig__ = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2___New_orig__
itkBinaryPruningImageFilterIUC2IUC2_cast = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUC2IUC2_cast


def itkBinaryPruningImageFilterIUS2IUS2_New():
    return itkBinaryPruningImageFilterIUS2IUS2.New()

class itkBinaryPruningImageFilterIUS2IUS2(itk.itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    r"""


    This filter removes "spurs" of less than a certain length in the
    input image.

    This class is parameterized over the type of the input image and the
    type of the output image.

    The input is assumed to be a binary image.

    This filter is a sequential pruning algorithm and known to be
    computational time dependable of the image size. The algorithm is the
    N-dimensional version of that given for two dimensions in:

    Rafael C. Gonzales and Richard E. Woods. Digital Image Processing.
    Addison Wesley, 491-494, (1993).

    See:  MorphologyImageFilter

    See:   BinaryErodeImageFilter

    See:   BinaryDilateImageFilter

    See:   BinaryThinningImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_Clone)
    GetPruning = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_GetPruning)
    SetIteration = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_SetIteration)
    GetIteration = _swig_new_instance_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_GetIteration)
    SameDimensionCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_SameDimensionCheck
    
    SameTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_SameTypeCheck
    
    AdditiveOperatorsCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_AdditiveOperatorsCheck
    
    IntConvertibleToPixelTypeCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_IntConvertibleToPixelTypeCheck
    
    PixelLessThanIntCheck = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_PixelLessThanIntCheck
    
    __swig_destroy__ = _itkBinaryPruningImageFilterPython.delete_itkBinaryPruningImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryPruningImageFilterIUS2IUS2

        Create a new object of the class itkBinaryPruningImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryPruningImageFilterIUS2IUS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkBinaryPruningImageFilterIUS2IUS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkBinaryPruningImageFilterIUS2IUS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryPruningImageFilterIUS2IUS2 in _itkBinaryPruningImageFilterPython:
_itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_swigregister(itkBinaryPruningImageFilterIUS2IUS2)
itkBinaryPruningImageFilterIUS2IUS2___New_orig__ = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2___New_orig__
itkBinaryPruningImageFilterIUS2IUS2_cast = _itkBinaryPruningImageFilterPython.itkBinaryPruningImageFilterIUS2IUS2_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def binary_pruning_image_filter(*args: itkt.ImageLike,  iteration: int=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for BinaryPruningImageFilter"""
    import itk

    kwarg_typehints = { 'iteration':iteration }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.BinaryPruningImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def binary_pruning_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKBinaryMathematicalMorphology.BinaryPruningImageFilter
    binary_pruning_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    binary_pruning_image_filter.__doc__ = filter_object.__doc__




