# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKVoronoiPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkVoronoiSegmentationImageFilterPython
else:
    import _itkVoronoiSegmentationImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkVoronoiSegmentationImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkVoronoiSegmentationImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkSizePython
import itk.itkOffsetPython
import itk.stdcomplexPython
import itk.itkRGBPixelPython
import itk.itkFixedArrayPython
import itk.itkCovariantVectorPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkRGBAPixelPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkImageToImageFilterAPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython

def itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_New():
    return itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass.New()

class itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass(itk.itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    r"""Proxy of C++ itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_Clone)
    SetNumberOfSeeds = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_SetNumberOfSeeds)
    GetNumberOfSeeds = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_GetNumberOfSeeds)
    SetMinRegion = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_SetMinRegion)
    GetMinRegion = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_GetMinRegion)
    SetSteps = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_SetSteps)
    GetSteps = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_GetSteps)
    GetLastStepSeeds = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_GetLastStepSeeds)
    GetNumberOfSeedsToAdded = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_GetNumberOfSeedsToAdded)
    SetUseBackgroundInAPrior = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_SetUseBackgroundInAPrior)
    GetUseBackgroundInAPrior = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_GetUseBackgroundInAPrior)
    SetOutputBoundary = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_SetOutputBoundary)
    GetOutputBoundary = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_GetOutputBoundary)
    SetInteractiveSegmentation = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_SetInteractiveSegmentation)
    GetInteractiveSegmentation = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_GetInteractiveSegmentation)
    InteractiveSegmentationOn = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_InteractiveSegmentationOn)
    InteractiveSegmentationOff = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_InteractiveSegmentationOff)
    SetMeanDeviation = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_SetMeanDeviation)
    GetMeanDeviation = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_GetMeanDeviation)
    SetSize = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_SetSize)
    GetSize = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_GetSize)
    TakeAPrior = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_TakeAPrior)
    RunSegment = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_RunSegment)
    RunSegmentOneStep = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_RunSegmentOneStep)
    MakeSegmentBoundary = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_MakeSegmentBoundary)
    MakeSegmentObject = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_MakeSegmentObject)
    GetVoronoiDiagram = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_GetVoronoiDiagram)
    SetSeeds = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_SetSeeds)
    GetSeed = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_GetSeed)
    DrawDiagram = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_DrawDiagram)
    BeforeNextStep = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_BeforeNextStep)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkVoronoiSegmentationImageFilterPython.delete_itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass
    cast = _swig_new_static_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass

        Create a new object of the class itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass in _itkVoronoiSegmentationImageFilterPython:
_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_swigregister(itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass)
itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass___New_orig__ = _itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass___New_orig__
itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_cast = _itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass_cast


def itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_New():
    return itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass.New()

class itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass(itk.itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    r"""Proxy of C++ itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_Clone)
    SetNumberOfSeeds = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_SetNumberOfSeeds)
    GetNumberOfSeeds = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_GetNumberOfSeeds)
    SetMinRegion = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_SetMinRegion)
    GetMinRegion = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_GetMinRegion)
    SetSteps = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_SetSteps)
    GetSteps = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_GetSteps)
    GetLastStepSeeds = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_GetLastStepSeeds)
    GetNumberOfSeedsToAdded = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_GetNumberOfSeedsToAdded)
    SetUseBackgroundInAPrior = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_SetUseBackgroundInAPrior)
    GetUseBackgroundInAPrior = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_GetUseBackgroundInAPrior)
    SetOutputBoundary = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_SetOutputBoundary)
    GetOutputBoundary = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_GetOutputBoundary)
    SetInteractiveSegmentation = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_SetInteractiveSegmentation)
    GetInteractiveSegmentation = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_GetInteractiveSegmentation)
    InteractiveSegmentationOn = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_InteractiveSegmentationOn)
    InteractiveSegmentationOff = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_InteractiveSegmentationOff)
    SetMeanDeviation = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_SetMeanDeviation)
    GetMeanDeviation = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_GetMeanDeviation)
    SetSize = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_SetSize)
    GetSize = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_GetSize)
    TakeAPrior = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_TakeAPrior)
    RunSegment = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_RunSegment)
    RunSegmentOneStep = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_RunSegmentOneStep)
    MakeSegmentBoundary = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_MakeSegmentBoundary)
    MakeSegmentObject = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_MakeSegmentObject)
    GetVoronoiDiagram = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_GetVoronoiDiagram)
    SetSeeds = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_SetSeeds)
    GetSeed = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_GetSeed)
    DrawDiagram = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_DrawDiagram)
    BeforeNextStep = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_BeforeNextStep)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkVoronoiSegmentationImageFilterPython.delete_itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass
    cast = _swig_new_static_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass

        Create a new object of the class itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass in _itkVoronoiSegmentationImageFilterPython:
_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_swigregister(itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass)
itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass___New_orig__ = _itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass___New_orig__
itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_cast = _itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass_cast


def itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_New():
    return itkVoronoiSegmentationImageFilterIUC2IUC2IUC2.New()

class itkVoronoiSegmentationImageFilterIUC2IUC2IUC2(itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Superclass):
    r"""


    Perform the segmentation of 2D images (single channel) by Voronoi
    Diagram. Used as a node of the segmentation toolkits. The homogeneity
    operator here is the testing of mean and standard deviation value. By
    setting the tolerance level, the "internal" region was defined as
    those that is closed to the gold-standard value in the sense that the
    difference is within the tolerance value.

    See VoronoiSegmentationImageFilterBase for detail description of
    voronoi segmentation principles.

    The parameters here are: the estimation of the statistics of the
    object. (mean and std.)

    the tolerance for the classification. (around the mean ans std.
    estimated value).

    The parameters can also be automatically set by given a prior, as a
    binary image.

    Detail information about this algorithm can be found in: " Semi-
    automated color segmentation of anatomical tissue," C. Imelinska, M.
    Downes, and W. Yuan Computerized Medical Imaging and Graphics, Vor.24,
    pp 173-180, 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_Clone)
    SetMean = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_SetMean)
    GetMean = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_GetMean)
    SetSTD = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_SetSTD)
    GetSTD = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_GetSTD)
    SetMeanTolerance = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_SetMeanTolerance)
    GetMeanTolerance = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_GetMeanTolerance)
    SetSTDTolerance = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_SetSTDTolerance)
    GetSTDTolerance = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_GetSTDTolerance)
    SetMeanPercentError = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_SetMeanPercentError)
    GetMeanPercentError = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_GetMeanPercentError)
    GetSTDPercentError = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_GetSTDPercentError)
    SetSTDPercentError = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_SetSTDPercentError)
    SameDimensionCheck = _itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_SameDimensionCheck
    
    IntConvertibleToOutputCheck = _itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_IntConvertibleToOutputCheck
    
    __swig_destroy__ = _itkVoronoiSegmentationImageFilterPython.delete_itkVoronoiSegmentationImageFilterIUC2IUC2IUC2
    cast = _swig_new_static_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkVoronoiSegmentationImageFilterIUC2IUC2IUC2

        Create a new object of the class itkVoronoiSegmentationImageFilterIUC2IUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVoronoiSegmentationImageFilterIUC2IUC2IUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVoronoiSegmentationImageFilterIUC2IUC2IUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVoronoiSegmentationImageFilterIUC2IUC2IUC2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVoronoiSegmentationImageFilterIUC2IUC2IUC2 in _itkVoronoiSegmentationImageFilterPython:
_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_swigregister(itkVoronoiSegmentationImageFilterIUC2IUC2IUC2)
itkVoronoiSegmentationImageFilterIUC2IUC2IUC2___New_orig__ = _itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2___New_orig__
itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_cast = _itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUC2IUC2IUC2_cast


def itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_New():
    return itkVoronoiSegmentationImageFilterIUS2IUS2IUS2.New()

class itkVoronoiSegmentationImageFilterIUS2IUS2IUS2(itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Superclass):
    r"""


    Perform the segmentation of 2D images (single channel) by Voronoi
    Diagram. Used as a node of the segmentation toolkits. The homogeneity
    operator here is the testing of mean and standard deviation value. By
    setting the tolerance level, the "internal" region was defined as
    those that is closed to the gold-standard value in the sense that the
    difference is within the tolerance value.

    See VoronoiSegmentationImageFilterBase for detail description of
    voronoi segmentation principles.

    The parameters here are: the estimation of the statistics of the
    object. (mean and std.)

    the tolerance for the classification. (around the mean ans std.
    estimated value).

    The parameters can also be automatically set by given a prior, as a
    binary image.

    Detail information about this algorithm can be found in: " Semi-
    automated color segmentation of anatomical tissue," C. Imelinska, M.
    Downes, and W. Yuan Computerized Medical Imaging and Graphics, Vor.24,
    pp 173-180, 2000. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_Clone)
    SetMean = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_SetMean)
    GetMean = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_GetMean)
    SetSTD = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_SetSTD)
    GetSTD = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_GetSTD)
    SetMeanTolerance = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_SetMeanTolerance)
    GetMeanTolerance = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_GetMeanTolerance)
    SetSTDTolerance = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_SetSTDTolerance)
    GetSTDTolerance = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_GetSTDTolerance)
    SetMeanPercentError = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_SetMeanPercentError)
    GetMeanPercentError = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_GetMeanPercentError)
    GetSTDPercentError = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_GetSTDPercentError)
    SetSTDPercentError = _swig_new_instance_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_SetSTDPercentError)
    SameDimensionCheck = _itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_SameDimensionCheck
    
    IntConvertibleToOutputCheck = _itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_IntConvertibleToOutputCheck
    
    __swig_destroy__ = _itkVoronoiSegmentationImageFilterPython.delete_itkVoronoiSegmentationImageFilterIUS2IUS2IUS2
    cast = _swig_new_static_method(_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkVoronoiSegmentationImageFilterIUS2IUS2IUS2

        Create a new object of the class itkVoronoiSegmentationImageFilterIUS2IUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVoronoiSegmentationImageFilterIUS2IUS2IUS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkVoronoiSegmentationImageFilterIUS2IUS2IUS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkVoronoiSegmentationImageFilterIUS2IUS2IUS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVoronoiSegmentationImageFilterIUS2IUS2IUS2 in _itkVoronoiSegmentationImageFilterPython:
_itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_swigregister(itkVoronoiSegmentationImageFilterIUS2IUS2IUS2)
itkVoronoiSegmentationImageFilterIUS2IUS2IUS2___New_orig__ = _itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2___New_orig__
itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_cast = _itkVoronoiSegmentationImageFilterPython.itkVoronoiSegmentationImageFilterIUS2IUS2IUS2_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def voronoi_segmentation_image_filter(*args: itkt.ImageLike,  mean: float=..., std: float=..., mean_tolerance: float=..., std_tolerance: float=..., mean_percent_error: float=..., std_percent_error: float=..., number_of_seeds: int=..., min_region: int=..., steps: int=..., use_background_in_a_prior: bool=..., output_boundary: bool=..., interactive_segmentation: bool=..., mean_deviation: float=..., size: Sequence[int]=..., seeds=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for VoronoiSegmentationImageFilter"""
    import itk

    kwarg_typehints = { 'mean':mean,'std':std,'mean_tolerance':mean_tolerance,'std_tolerance':std_tolerance,'mean_percent_error':mean_percent_error,'std_percent_error':std_percent_error,'number_of_seeds':number_of_seeds,'min_region':min_region,'steps':steps,'use_background_in_a_prior':use_background_in_a_prior,'output_boundary':output_boundary,'interactive_segmentation':interactive_segmentation,'mean_deviation':mean_deviation,'size':size,'seeds':seeds }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.VoronoiSegmentationImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def voronoi_segmentation_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKVoronoi.VoronoiSegmentationImageFilter
    voronoi_segmentation_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    voronoi_segmentation_image_filter.__doc__ = filter_object.__doc__

from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def voronoi_segmentation_image_filter_base(*args: itkt.ImageLike,  number_of_seeds: int=..., min_region: int=..., steps: int=..., use_background_in_a_prior: bool=..., output_boundary: bool=..., interactive_segmentation: bool=..., mean_deviation: float=..., size: Sequence[int]=..., seeds=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for VoronoiSegmentationImageFilterBase"""
    import itk

    kwarg_typehints = { 'number_of_seeds':number_of_seeds,'min_region':min_region,'steps':steps,'use_background_in_a_prior':use_background_in_a_prior,'output_boundary':output_boundary,'interactive_segmentation':interactive_segmentation,'mean_deviation':mean_deviation,'size':size,'seeds':seeds }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.VoronoiSegmentationImageFilterBase.New(*args, **kwargs)
    return instance.__internal_call__()

def voronoi_segmentation_image_filter_base_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKVoronoi.VoronoiSegmentationImageFilterBase
    voronoi_segmentation_image_filter_base.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    voronoi_segmentation_image_filter_base.__doc__ = filter_object.__doc__




