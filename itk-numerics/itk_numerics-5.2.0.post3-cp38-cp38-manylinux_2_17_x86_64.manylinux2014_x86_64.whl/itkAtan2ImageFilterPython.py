# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKImageIntensityPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkAtan2ImageFilterPython
else:
    import _itkAtan2ImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkAtan2ImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkAtan2ImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkBinaryGeneratorImageFilterPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkRGBAPixelPython
import itk.itkFixedArrayPython
import itk.itkRGBPixelPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkInPlaceImageFilterBPython
import itk.itkImageToImageFilterBPython
import itk.itkImagePython
import itk.itkPointPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageToImageFilterCommonPython
import itk.itkInPlaceImageFilterAPython
import itk.itkImageToImageFilterAPython

def itkAtan2ImageFilterID2ID2ID2_New():
    return itkAtan2ImageFilterID2ID2ID2.New()

class itkAtan2ImageFilterID2ID2ID2(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID2ID2ID2):
    r"""


    Computes two argument inverse tangent.

    The first argument to the atan function is provided by a pixel in the
    first input image (SetInput1()) and the corresponding pixel in the
    second input image (SetInput2()) is used as the second argument.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Both pixel input types are cast to double in order to be used as
    parameters of std::atan2(). The resulting double value is cast to the
    output pixel type. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_Clone)
    Input1ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAtan2ImageFilterPython.delete_itkAtan2ImageFilterID2ID2ID2
    cast = _swig_new_static_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkAtan2ImageFilterID2ID2ID2

        Create a new object of the class itkAtan2ImageFilterID2ID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtan2ImageFilterID2ID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAtan2ImageFilterID2ID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAtan2ImageFilterID2ID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAtan2ImageFilterID2ID2ID2 in _itkAtan2ImageFilterPython:
_itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_swigregister(itkAtan2ImageFilterID2ID2ID2)
itkAtan2ImageFilterID2ID2ID2___New_orig__ = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2___New_orig__
itkAtan2ImageFilterID2ID2ID2_cast = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_cast


def itkAtan2ImageFilterID3ID3ID3_New():
    return itkAtan2ImageFilterID3ID3ID3.New()

class itkAtan2ImageFilterID3ID3ID3(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID3ID3ID3):
    r"""


    Computes two argument inverse tangent.

    The first argument to the atan function is provided by a pixel in the
    first input image (SetInput1()) and the corresponding pixel in the
    second input image (SetInput2()) is used as the second argument.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Both pixel input types are cast to double in order to be used as
    parameters of std::atan2(). The resulting double value is cast to the
    output pixel type. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_Clone)
    Input1ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAtan2ImageFilterPython.delete_itkAtan2ImageFilterID3ID3ID3
    cast = _swig_new_static_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkAtan2ImageFilterID3ID3ID3

        Create a new object of the class itkAtan2ImageFilterID3ID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtan2ImageFilterID3ID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAtan2ImageFilterID3ID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAtan2ImageFilterID3ID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAtan2ImageFilterID3ID3ID3 in _itkAtan2ImageFilterPython:
_itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_swigregister(itkAtan2ImageFilterID3ID3ID3)
itkAtan2ImageFilterID3ID3ID3___New_orig__ = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3___New_orig__
itkAtan2ImageFilterID3ID3ID3_cast = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_cast


def itkAtan2ImageFilterID4ID4ID4_New():
    return itkAtan2ImageFilterID4ID4ID4.New()

class itkAtan2ImageFilterID4ID4ID4(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID4ID4ID4):
    r"""


    Computes two argument inverse tangent.

    The first argument to the atan function is provided by a pixel in the
    first input image (SetInput1()) and the corresponding pixel in the
    second input image (SetInput2()) is used as the second argument.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Both pixel input types are cast to double in order to be used as
    parameters of std::atan2(). The resulting double value is cast to the
    output pixel type. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterID4ID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterID4ID4ID4_Clone)
    Input1ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID4ID4ID4_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID4ID4ID4_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID4ID4ID4_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAtan2ImageFilterPython.delete_itkAtan2ImageFilterID4ID4ID4
    cast = _swig_new_static_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterID4ID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkAtan2ImageFilterID4ID4ID4

        Create a new object of the class itkAtan2ImageFilterID4ID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtan2ImageFilterID4ID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAtan2ImageFilterID4ID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAtan2ImageFilterID4ID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAtan2ImageFilterID4ID4ID4 in _itkAtan2ImageFilterPython:
_itkAtan2ImageFilterPython.itkAtan2ImageFilterID4ID4ID4_swigregister(itkAtan2ImageFilterID4ID4ID4)
itkAtan2ImageFilterID4ID4ID4___New_orig__ = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID4ID4ID4___New_orig__
itkAtan2ImageFilterID4ID4ID4_cast = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID4ID4ID4_cast


def itkAtan2ImageFilterIF2IF2IF2_New():
    return itkAtan2ImageFilterIF2IF2IF2.New()

class itkAtan2ImageFilterIF2IF2IF2(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF2IF2IF2):
    r"""


    Computes two argument inverse tangent.

    The first argument to the atan function is provided by a pixel in the
    first input image (SetInput1()) and the corresponding pixel in the
    second input image (SetInput2()) is used as the second argument.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Both pixel input types are cast to double in order to be used as
    parameters of std::atan2(). The resulting double value is cast to the
    output pixel type. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_Clone)
    Input1ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAtan2ImageFilterPython.delete_itkAtan2ImageFilterIF2IF2IF2
    cast = _swig_new_static_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkAtan2ImageFilterIF2IF2IF2

        Create a new object of the class itkAtan2ImageFilterIF2IF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtan2ImageFilterIF2IF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAtan2ImageFilterIF2IF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAtan2ImageFilterIF2IF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAtan2ImageFilterIF2IF2IF2 in _itkAtan2ImageFilterPython:
_itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_swigregister(itkAtan2ImageFilterIF2IF2IF2)
itkAtan2ImageFilterIF2IF2IF2___New_orig__ = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2___New_orig__
itkAtan2ImageFilterIF2IF2IF2_cast = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_cast


def itkAtan2ImageFilterIF3IF3IF3_New():
    return itkAtan2ImageFilterIF3IF3IF3.New()

class itkAtan2ImageFilterIF3IF3IF3(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF3IF3IF3):
    r"""


    Computes two argument inverse tangent.

    The first argument to the atan function is provided by a pixel in the
    first input image (SetInput1()) and the corresponding pixel in the
    second input image (SetInput2()) is used as the second argument.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Both pixel input types are cast to double in order to be used as
    parameters of std::atan2(). The resulting double value is cast to the
    output pixel type. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_Clone)
    Input1ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAtan2ImageFilterPython.delete_itkAtan2ImageFilterIF3IF3IF3
    cast = _swig_new_static_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkAtan2ImageFilterIF3IF3IF3

        Create a new object of the class itkAtan2ImageFilterIF3IF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtan2ImageFilterIF3IF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAtan2ImageFilterIF3IF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAtan2ImageFilterIF3IF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAtan2ImageFilterIF3IF3IF3 in _itkAtan2ImageFilterPython:
_itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_swigregister(itkAtan2ImageFilterIF3IF3IF3)
itkAtan2ImageFilterIF3IF3IF3___New_orig__ = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3___New_orig__
itkAtan2ImageFilterIF3IF3IF3_cast = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_cast


def itkAtan2ImageFilterIF4IF4IF4_New():
    return itkAtan2ImageFilterIF4IF4IF4.New()

class itkAtan2ImageFilterIF4IF4IF4(itk.itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF4IF4IF4):
    r"""


    Computes two argument inverse tangent.

    The first argument to the atan function is provided by a pixel in the
    first input image (SetInput1()) and the corresponding pixel in the
    second input image (SetInput2()) is used as the second argument.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Both pixel input types are cast to double in order to be used as
    parameters of std::atan2(). The resulting double value is cast to the
    output pixel type. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterIF4IF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterIF4IF4IF4_Clone)
    Input1ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF4IF4IF4_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF4IF4IF4_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF4IF4IF4_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAtan2ImageFilterPython.delete_itkAtan2ImageFilterIF4IF4IF4
    cast = _swig_new_static_method(_itkAtan2ImageFilterPython.itkAtan2ImageFilterIF4IF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkAtan2ImageFilterIF4IF4IF4

        Create a new object of the class itkAtan2ImageFilterIF4IF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtan2ImageFilterIF4IF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkAtan2ImageFilterIF4IF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkAtan2ImageFilterIF4IF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAtan2ImageFilterIF4IF4IF4 in _itkAtan2ImageFilterPython:
_itkAtan2ImageFilterPython.itkAtan2ImageFilterIF4IF4IF4_swigregister(itkAtan2ImageFilterIF4IF4IF4)
itkAtan2ImageFilterIF4IF4IF4___New_orig__ = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF4IF4IF4___New_orig__
itkAtan2ImageFilterIF4IF4IF4_cast = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF4IF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def atan2_image_filter(*args: itkt.ImageLike,  constant1: float=..., constant2: float=..., constant: float=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for Atan2ImageFilter"""
    import itk

    kwarg_typehints = { 'constant1':constant1,'constant2':constant2,'constant':constant }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.Atan2ImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def atan2_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageIntensity.Atan2ImageFilter
    atan2_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    atan2_image_filter.__doc__ = filter_object.__doc__




