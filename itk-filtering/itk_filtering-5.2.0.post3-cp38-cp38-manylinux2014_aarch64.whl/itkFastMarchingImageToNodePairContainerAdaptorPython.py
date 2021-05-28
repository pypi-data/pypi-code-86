# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKFastMarchingPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkFastMarchingImageToNodePairContainerAdaptorPython
else:
    import _itkFastMarchingImageToNodePairContainerAdaptorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkFastMarchingImageToNodePairContainerAdaptorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkFastMarchingImageToNodePairContainerAdaptorPython.SWIG_PyStaticMethod_New

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
import itk.itkImagePython
import itk.itkSizePython
import itk.pyBasePython
import itk.ITKCommonBasePython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkCovariantVectorPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkRGBAPixelPython
import itk.ITKFastMarchingBasePython
import itk.itkNodePairPython
import itk.itkFastMarchingStoppingCriterionBasePython
import itk.itkImageToImageFilterAPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkLevelSetNodePython

def itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_New():
    return itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2.New()

class itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2(itk.ITKCommonBasePython.itkObject):
    r"""


    Convenient adaptor class which converts Image into
    FastMarching::NodePairContainerType used for initializing the
    FastMarching.

    One provides images by means of SetAliveImage, SetTrialImage,
    SetForbiddenImage and get corresponding containers by means of
    GetAlivePoints, GetTrialPoints, GetForbiddenPoints.

    One can globally set the associated value for all
    FastMarchingTraitsBase::Alive points by means of SetAliveValue; and
    for all FastMarchingTraitsBase::Trial points by means of
    SetTrialValue.

    To restrict the evolution of the front in certain area, one can use
    SetForbiddenImage and SetIsForbiddenImageBinaryMask depending on the
    input image.

    See:  FastMarchingTraitsBase

    See:   FastMarchingBase 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_Clone)
    SetAliveImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_SetAliveImage)
    SetTrialImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_SetTrialImage)
    SetForbiddenImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_SetForbiddenImage)
    SetIsForbiddenImageBinaryMask = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_SetIsForbiddenImageBinaryMask)
    IsForbiddenImageBinaryMaskOn = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_IsForbiddenImageBinaryMaskOn)
    IsForbiddenImageBinaryMaskOff = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_IsForbiddenImageBinaryMaskOff)
    GetAlivePoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_GetAlivePoints)
    GetTrialPoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_GetTrialPoints)
    GetForbiddenPoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_GetForbiddenPoints)
    SetAliveValue = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_SetAliveValue)
    SetTrialValue = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_SetTrialValue)
    Update = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_Update)
    __swig_destroy__ = _itkFastMarchingImageToNodePairContainerAdaptorPython.delete_itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2
    cast = _swig_new_static_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2

        Create a new object of the class itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2 in _itkFastMarchingImageToNodePairContainerAdaptorPython:
_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_swigregister(itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2)
itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2___New_orig__ = _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2___New_orig__
itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_cast = _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID2ID2ID2_cast


def itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_New():
    return itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3.New()

class itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3(itk.ITKCommonBasePython.itkObject):
    r"""


    Convenient adaptor class which converts Image into
    FastMarching::NodePairContainerType used for initializing the
    FastMarching.

    One provides images by means of SetAliveImage, SetTrialImage,
    SetForbiddenImage and get corresponding containers by means of
    GetAlivePoints, GetTrialPoints, GetForbiddenPoints.

    One can globally set the associated value for all
    FastMarchingTraitsBase::Alive points by means of SetAliveValue; and
    for all FastMarchingTraitsBase::Trial points by means of
    SetTrialValue.

    To restrict the evolution of the front in certain area, one can use
    SetForbiddenImage and SetIsForbiddenImageBinaryMask depending on the
    input image.

    See:  FastMarchingTraitsBase

    See:   FastMarchingBase 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_Clone)
    SetAliveImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_SetAliveImage)
    SetTrialImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_SetTrialImage)
    SetForbiddenImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_SetForbiddenImage)
    SetIsForbiddenImageBinaryMask = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_SetIsForbiddenImageBinaryMask)
    IsForbiddenImageBinaryMaskOn = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_IsForbiddenImageBinaryMaskOn)
    IsForbiddenImageBinaryMaskOff = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_IsForbiddenImageBinaryMaskOff)
    GetAlivePoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_GetAlivePoints)
    GetTrialPoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_GetTrialPoints)
    GetForbiddenPoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_GetForbiddenPoints)
    SetAliveValue = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_SetAliveValue)
    SetTrialValue = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_SetTrialValue)
    Update = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_Update)
    __swig_destroy__ = _itkFastMarchingImageToNodePairContainerAdaptorPython.delete_itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3
    cast = _swig_new_static_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3

        Create a new object of the class itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3 in _itkFastMarchingImageToNodePairContainerAdaptorPython:
_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_swigregister(itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3)
itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3___New_orig__ = _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3___New_orig__
itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_cast = _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID3ID3ID3_cast


def itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_New():
    return itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4.New()

class itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4(itk.ITKCommonBasePython.itkObject):
    r"""


    Convenient adaptor class which converts Image into
    FastMarching::NodePairContainerType used for initializing the
    FastMarching.

    One provides images by means of SetAliveImage, SetTrialImage,
    SetForbiddenImage and get corresponding containers by means of
    GetAlivePoints, GetTrialPoints, GetForbiddenPoints.

    One can globally set the associated value for all
    FastMarchingTraitsBase::Alive points by means of SetAliveValue; and
    for all FastMarchingTraitsBase::Trial points by means of
    SetTrialValue.

    To restrict the evolution of the front in certain area, one can use
    SetForbiddenImage and SetIsForbiddenImageBinaryMask depending on the
    input image.

    See:  FastMarchingTraitsBase

    See:   FastMarchingBase 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_Clone)
    SetAliveImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_SetAliveImage)
    SetTrialImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_SetTrialImage)
    SetForbiddenImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_SetForbiddenImage)
    SetIsForbiddenImageBinaryMask = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_SetIsForbiddenImageBinaryMask)
    IsForbiddenImageBinaryMaskOn = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_IsForbiddenImageBinaryMaskOn)
    IsForbiddenImageBinaryMaskOff = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_IsForbiddenImageBinaryMaskOff)
    GetAlivePoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_GetAlivePoints)
    GetTrialPoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_GetTrialPoints)
    GetForbiddenPoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_GetForbiddenPoints)
    SetAliveValue = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_SetAliveValue)
    SetTrialValue = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_SetTrialValue)
    Update = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_Update)
    __swig_destroy__ = _itkFastMarchingImageToNodePairContainerAdaptorPython.delete_itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4
    cast = _swig_new_static_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4

        Create a new object of the class itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4 in _itkFastMarchingImageToNodePairContainerAdaptorPython:
_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_swigregister(itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4)
itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4___New_orig__ = _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4___New_orig__
itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_cast = _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorID4ID4ID4_cast


def itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_New():
    return itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.New()

class itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2(itk.ITKCommonBasePython.itkObject):
    r"""


    Convenient adaptor class which converts Image into
    FastMarching::NodePairContainerType used for initializing the
    FastMarching.

    One provides images by means of SetAliveImage, SetTrialImage,
    SetForbiddenImage and get corresponding containers by means of
    GetAlivePoints, GetTrialPoints, GetForbiddenPoints.

    One can globally set the associated value for all
    FastMarchingTraitsBase::Alive points by means of SetAliveValue; and
    for all FastMarchingTraitsBase::Trial points by means of
    SetTrialValue.

    To restrict the evolution of the front in certain area, one can use
    SetForbiddenImage and SetIsForbiddenImageBinaryMask depending on the
    input image.

    See:  FastMarchingTraitsBase

    See:   FastMarchingBase 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_Clone)
    SetAliveImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetAliveImage)
    SetTrialImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetTrialImage)
    SetForbiddenImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetForbiddenImage)
    SetIsForbiddenImageBinaryMask = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetIsForbiddenImageBinaryMask)
    IsForbiddenImageBinaryMaskOn = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_IsForbiddenImageBinaryMaskOn)
    IsForbiddenImageBinaryMaskOff = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_IsForbiddenImageBinaryMaskOff)
    GetAlivePoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_GetAlivePoints)
    GetTrialPoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_GetTrialPoints)
    GetForbiddenPoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_GetForbiddenPoints)
    SetAliveValue = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetAliveValue)
    SetTrialValue = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_SetTrialValue)
    Update = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_Update)
    __swig_destroy__ = _itkFastMarchingImageToNodePairContainerAdaptorPython.delete_itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2
    cast = _swig_new_static_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2

        Create a new object of the class itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2 in _itkFastMarchingImageToNodePairContainerAdaptorPython:
_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_swigregister(itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2)
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2___New_orig__ = _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2___New_orig__
itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_cast = _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF2IF2IF2_cast


def itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_New():
    return itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.New()

class itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3(itk.ITKCommonBasePython.itkObject):
    r"""


    Convenient adaptor class which converts Image into
    FastMarching::NodePairContainerType used for initializing the
    FastMarching.

    One provides images by means of SetAliveImage, SetTrialImage,
    SetForbiddenImage and get corresponding containers by means of
    GetAlivePoints, GetTrialPoints, GetForbiddenPoints.

    One can globally set the associated value for all
    FastMarchingTraitsBase::Alive points by means of SetAliveValue; and
    for all FastMarchingTraitsBase::Trial points by means of
    SetTrialValue.

    To restrict the evolution of the front in certain area, one can use
    SetForbiddenImage and SetIsForbiddenImageBinaryMask depending on the
    input image.

    See:  FastMarchingTraitsBase

    See:   FastMarchingBase 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_Clone)
    SetAliveImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetAliveImage)
    SetTrialImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetTrialImage)
    SetForbiddenImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetForbiddenImage)
    SetIsForbiddenImageBinaryMask = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetIsForbiddenImageBinaryMask)
    IsForbiddenImageBinaryMaskOn = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_IsForbiddenImageBinaryMaskOn)
    IsForbiddenImageBinaryMaskOff = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_IsForbiddenImageBinaryMaskOff)
    GetAlivePoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_GetAlivePoints)
    GetTrialPoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_GetTrialPoints)
    GetForbiddenPoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_GetForbiddenPoints)
    SetAliveValue = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetAliveValue)
    SetTrialValue = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_SetTrialValue)
    Update = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_Update)
    __swig_destroy__ = _itkFastMarchingImageToNodePairContainerAdaptorPython.delete_itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3
    cast = _swig_new_static_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3

        Create a new object of the class itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3 in _itkFastMarchingImageToNodePairContainerAdaptorPython:
_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_swigregister(itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3)
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3___New_orig__ = _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3___New_orig__
itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_cast = _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF3IF3IF3_cast


def itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_New():
    return itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4.New()

class itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4(itk.ITKCommonBasePython.itkObject):
    r"""


    Convenient adaptor class which converts Image into
    FastMarching::NodePairContainerType used for initializing the
    FastMarching.

    One provides images by means of SetAliveImage, SetTrialImage,
    SetForbiddenImage and get corresponding containers by means of
    GetAlivePoints, GetTrialPoints, GetForbiddenPoints.

    One can globally set the associated value for all
    FastMarchingTraitsBase::Alive points by means of SetAliveValue; and
    for all FastMarchingTraitsBase::Trial points by means of
    SetTrialValue.

    To restrict the evolution of the front in certain area, one can use
    SetForbiddenImage and SetIsForbiddenImageBinaryMask depending on the
    input image.

    See:  FastMarchingTraitsBase

    See:   FastMarchingBase 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_Clone)
    SetAliveImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_SetAliveImage)
    SetTrialImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_SetTrialImage)
    SetForbiddenImage = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_SetForbiddenImage)
    SetIsForbiddenImageBinaryMask = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_SetIsForbiddenImageBinaryMask)
    IsForbiddenImageBinaryMaskOn = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_IsForbiddenImageBinaryMaskOn)
    IsForbiddenImageBinaryMaskOff = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_IsForbiddenImageBinaryMaskOff)
    GetAlivePoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_GetAlivePoints)
    GetTrialPoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_GetTrialPoints)
    GetForbiddenPoints = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_GetForbiddenPoints)
    SetAliveValue = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_SetAliveValue)
    SetTrialValue = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_SetTrialValue)
    Update = _swig_new_instance_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_Update)
    __swig_destroy__ = _itkFastMarchingImageToNodePairContainerAdaptorPython.delete_itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4
    cast = _swig_new_static_method(_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4

        Create a new object of the class itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4 in _itkFastMarchingImageToNodePairContainerAdaptorPython:
_itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_swigregister(itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4)
itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4___New_orig__ = _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4___New_orig__
itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_cast = _itkFastMarchingImageToNodePairContainerAdaptorPython.itkFastMarchingImageToNodePairContainerAdaptorIF4IF4IF4_cast



