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
    from . import _itkRoundImageFilterPython
else:
    import _itkRoundImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRoundImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRoundImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkUnaryGeneratorImageFilterPython
import itk.itkInPlaceImageFilterAPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkImageToImageFilterBPython
import itk.itkVectorImagePython
import itk.stdcomplexPython
import itk.itkImagePython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkCovariantVectorPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.itkPointPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkRGBPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkImageRegionPython
import itk.itkRGBAPixelPython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageToImageFilterAPython
import itk.itkInPlaceImageFilterBPython

def itkRoundImageFilterID2ID2_New():
    return itkRoundImageFilterID2ID2.New()

class itkRoundImageFilterID2ID2(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    r"""


    Rounds the value of each pixel.

    The computations are performed using itk::Math::Round(x). 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkRoundImageFilterPython.itkRoundImageFilterID2ID2_Clone)
    __swig_destroy__ = _itkRoundImageFilterPython.delete_itkRoundImageFilterID2ID2
    cast = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkRoundImageFilterID2ID2

        Create a new object of the class itkRoundImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRoundImageFilterID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRoundImageFilterID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRoundImageFilterID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRoundImageFilterID2ID2 in _itkRoundImageFilterPython:
_itkRoundImageFilterPython.itkRoundImageFilterID2ID2_swigregister(itkRoundImageFilterID2ID2)
itkRoundImageFilterID2ID2___New_orig__ = _itkRoundImageFilterPython.itkRoundImageFilterID2ID2___New_orig__
itkRoundImageFilterID2ID2_cast = _itkRoundImageFilterPython.itkRoundImageFilterID2ID2_cast


def itkRoundImageFilterID3ID3_New():
    return itkRoundImageFilterID3ID3.New()

class itkRoundImageFilterID3ID3(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    r"""


    Rounds the value of each pixel.

    The computations are performed using itk::Math::Round(x). 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkRoundImageFilterPython.itkRoundImageFilterID3ID3_Clone)
    __swig_destroy__ = _itkRoundImageFilterPython.delete_itkRoundImageFilterID3ID3
    cast = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkRoundImageFilterID3ID3

        Create a new object of the class itkRoundImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRoundImageFilterID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRoundImageFilterID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRoundImageFilterID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRoundImageFilterID3ID3 in _itkRoundImageFilterPython:
_itkRoundImageFilterPython.itkRoundImageFilterID3ID3_swigregister(itkRoundImageFilterID3ID3)
itkRoundImageFilterID3ID3___New_orig__ = _itkRoundImageFilterPython.itkRoundImageFilterID3ID3___New_orig__
itkRoundImageFilterID3ID3_cast = _itkRoundImageFilterPython.itkRoundImageFilterID3ID3_cast


def itkRoundImageFilterID4ID4_New():
    return itkRoundImageFilterID4ID4.New()

class itkRoundImageFilterID4ID4(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID4ID4):
    r"""


    Rounds the value of each pixel.

    The computations are performed using itk::Math::Round(x). 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkRoundImageFilterPython.itkRoundImageFilterID4ID4_Clone)
    __swig_destroy__ = _itkRoundImageFilterPython.delete_itkRoundImageFilterID4ID4
    cast = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkRoundImageFilterID4ID4

        Create a new object of the class itkRoundImageFilterID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRoundImageFilterID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRoundImageFilterID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRoundImageFilterID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRoundImageFilterID4ID4 in _itkRoundImageFilterPython:
_itkRoundImageFilterPython.itkRoundImageFilterID4ID4_swigregister(itkRoundImageFilterID4ID4)
itkRoundImageFilterID4ID4___New_orig__ = _itkRoundImageFilterPython.itkRoundImageFilterID4ID4___New_orig__
itkRoundImageFilterID4ID4_cast = _itkRoundImageFilterPython.itkRoundImageFilterID4ID4_cast


def itkRoundImageFilterIF2IF2_New():
    return itkRoundImageFilterIF2IF2.New()

class itkRoundImageFilterIF2IF2(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    r"""


    Rounds the value of each pixel.

    The computations are performed using itk::Math::Round(x). 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkRoundImageFilterPython.itkRoundImageFilterIF2IF2_Clone)
    __swig_destroy__ = _itkRoundImageFilterPython.delete_itkRoundImageFilterIF2IF2
    cast = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkRoundImageFilterIF2IF2

        Create a new object of the class itkRoundImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRoundImageFilterIF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRoundImageFilterIF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRoundImageFilterIF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRoundImageFilterIF2IF2 in _itkRoundImageFilterPython:
_itkRoundImageFilterPython.itkRoundImageFilterIF2IF2_swigregister(itkRoundImageFilterIF2IF2)
itkRoundImageFilterIF2IF2___New_orig__ = _itkRoundImageFilterPython.itkRoundImageFilterIF2IF2___New_orig__
itkRoundImageFilterIF2IF2_cast = _itkRoundImageFilterPython.itkRoundImageFilterIF2IF2_cast


def itkRoundImageFilterIF3IF3_New():
    return itkRoundImageFilterIF3IF3.New()

class itkRoundImageFilterIF3IF3(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    r"""


    Rounds the value of each pixel.

    The computations are performed using itk::Math::Round(x). 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkRoundImageFilterPython.itkRoundImageFilterIF3IF3_Clone)
    __swig_destroy__ = _itkRoundImageFilterPython.delete_itkRoundImageFilterIF3IF3
    cast = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkRoundImageFilterIF3IF3

        Create a new object of the class itkRoundImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRoundImageFilterIF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRoundImageFilterIF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRoundImageFilterIF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRoundImageFilterIF3IF3 in _itkRoundImageFilterPython:
_itkRoundImageFilterPython.itkRoundImageFilterIF3IF3_swigregister(itkRoundImageFilterIF3IF3)
itkRoundImageFilterIF3IF3___New_orig__ = _itkRoundImageFilterPython.itkRoundImageFilterIF3IF3___New_orig__
itkRoundImageFilterIF3IF3_cast = _itkRoundImageFilterPython.itkRoundImageFilterIF3IF3_cast


def itkRoundImageFilterIF4IF4_New():
    return itkRoundImageFilterIF4IF4.New()

class itkRoundImageFilterIF4IF4(itk.itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF4IF4):
    r"""


    Rounds the value of each pixel.

    The computations are performed using itk::Math::Round(x). 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterIF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkRoundImageFilterPython.itkRoundImageFilterIF4IF4_Clone)
    __swig_destroy__ = _itkRoundImageFilterPython.delete_itkRoundImageFilterIF4IF4
    cast = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterIF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkRoundImageFilterIF4IF4

        Create a new object of the class itkRoundImageFilterIF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRoundImageFilterIF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRoundImageFilterIF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRoundImageFilterIF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRoundImageFilterIF4IF4 in _itkRoundImageFilterPython:
_itkRoundImageFilterPython.itkRoundImageFilterIF4IF4_swigregister(itkRoundImageFilterIF4IF4)
itkRoundImageFilterIF4IF4___New_orig__ = _itkRoundImageFilterPython.itkRoundImageFilterIF4IF4___New_orig__
itkRoundImageFilterIF4IF4_cast = _itkRoundImageFilterPython.itkRoundImageFilterIF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def round_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for RoundImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.RoundImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def round_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageIntensity.RoundImageFilter
    round_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    round_image_filter.__doc__ = filter_object.__doc__




