# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKImageFusionPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkLabelMapContourOverlayImageFilterPython
else:
    import _itkLabelMapContourOverlayImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLabelMapContourOverlayImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLabelMapContourOverlayImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkSizePython
import itk.pyBasePython
import itk.ITKLabelMapBasePython
import itk.itkImageRegionPython
import itk.ITKCommonBasePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkImagePython
import itk.itkRGBAPixelPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkPointPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBPixelPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageToImageFilterCommonPython
import itk.itkStatisticsLabelObjectPython
import itk.itkShapeLabelObjectPython
import itk.itkAffineTransformPython
import itk.itkTransformBasePython
import itk.itkArray2DPython
import itk.itkArrayPython
import itk.itkOptimizerParametersPython
import itk.itkDiffusionTensor3DPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkLabelObjectPython
import itk.itkLabelObjectLinePython
import itk.itkHistogramPython
import itk.itkSamplePython
import itk.itkLabelMapFilterPython

def itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_New():
    return itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.New()

class itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2(itk.itkLabelMapFilterPython.itkLabelMapFilterLM2IRGBUC2):
    r"""


    Apply a colormap to the contours (outlines) of each object in a label
    map and superimpose it on top of the feature image.

    The feature image is typically the image from which the labeling was
    produced. Use the SetInput function to set the LabelMap, and the
    SetFeatureImage function to set the feature image.

    Apply a colormap to a label map and put it on top of the input image.
    The set of colors is a good selection of distinct colors. The opacity
    of the label map can be defined by the user. A background label
    produce a gray pixel with the same intensity than the input one.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   LabelMapOverlayImageFilter, LabelOverlayImageFilter,
    LabelOverlayFunctor

    See:  LabelMapToBinaryImageFilter, LabelMapToLabelImageFilter, 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    PLAIN = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_PLAIN
    
    CONTOUR = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_CONTOUR
    
    SLICE_CONTOUR = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SLICE_CONTOUR
    
    HIGH_LABEL_ON_TOP = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_HIGH_LABEL_ON_TOP
    
    LOW_LABEL_ON_TOP = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_LOW_LABEL_ON_TOP
    
    __New_orig__ = _swig_new_static_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_Clone)
    SetFeatureImage = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetFeatureImage)
    GetFeatureImage = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetFeatureImage)
    SetInput1 = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetInput2)
    SetOpacity = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetOpacity)
    GetOpacity = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetOpacity)
    SetType = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetType)
    GetType = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetType)
    SetPriority = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetPriority)
    GetPriority = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetPriority)
    SetDilationRadius = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetDilationRadius)
    GetDilationRadius = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetDilationRadius)
    SetContourThickness = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetContourThickness)
    GetContourThickness = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetContourThickness)
    SetSliceDimension = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetSliceDimension)
    GetSliceDimension = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetSliceDimension)
    SetFunctor = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_SetFunctor)
    GetFunctor = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_GetFunctor)
    __swig_destroy__ = _itkLabelMapContourOverlayImageFilterPython.delete_itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2
    cast = _swig_new_static_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2

        Create a new object of the class itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2 in _itkLabelMapContourOverlayImageFilterPython:
_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_swigregister(itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2)
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2___New_orig__ = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2___New_orig__
itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_cast = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM2IUC2IRGBUC2_cast


def itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_New():
    return itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.New()

class itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3(itk.itkLabelMapFilterPython.itkLabelMapFilterLM3IRGBUC3):
    r"""


    Apply a colormap to the contours (outlines) of each object in a label
    map and superimpose it on top of the feature image.

    The feature image is typically the image from which the labeling was
    produced. Use the SetInput function to set the LabelMap, and the
    SetFeatureImage function to set the feature image.

    Apply a colormap to a label map and put it on top of the input image.
    The set of colors is a good selection of distinct colors. The opacity
    of the label map can be defined by the user. A background label
    produce a gray pixel with the same intensity than the input one.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   LabelMapOverlayImageFilter, LabelOverlayImageFilter,
    LabelOverlayFunctor

    See:  LabelMapToBinaryImageFilter, LabelMapToLabelImageFilter, 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    PLAIN = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_PLAIN
    
    CONTOUR = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_CONTOUR
    
    SLICE_CONTOUR = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SLICE_CONTOUR
    
    HIGH_LABEL_ON_TOP = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_HIGH_LABEL_ON_TOP
    
    LOW_LABEL_ON_TOP = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_LOW_LABEL_ON_TOP
    
    __New_orig__ = _swig_new_static_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_Clone)
    SetFeatureImage = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetFeatureImage)
    GetFeatureImage = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetFeatureImage)
    SetInput1 = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetInput2)
    SetOpacity = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetOpacity)
    GetOpacity = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetOpacity)
    SetType = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetType)
    GetType = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetType)
    SetPriority = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetPriority)
    GetPriority = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetPriority)
    SetDilationRadius = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetDilationRadius)
    GetDilationRadius = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetDilationRadius)
    SetContourThickness = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetContourThickness)
    GetContourThickness = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetContourThickness)
    SetSliceDimension = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetSliceDimension)
    GetSliceDimension = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetSliceDimension)
    SetFunctor = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_SetFunctor)
    GetFunctor = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_GetFunctor)
    __swig_destroy__ = _itkLabelMapContourOverlayImageFilterPython.delete_itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3
    cast = _swig_new_static_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3

        Create a new object of the class itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3 in _itkLabelMapContourOverlayImageFilterPython:
_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_swigregister(itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3)
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3___New_orig__ = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3___New_orig__
itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_cast = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM3IUC3IRGBUC3_cast


def itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_New():
    return itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4.New()

class itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4(itk.itkLabelMapFilterPython.itkLabelMapFilterLM4IRGBUC4):
    r"""


    Apply a colormap to the contours (outlines) of each object in a label
    map and superimpose it on top of the feature image.

    The feature image is typically the image from which the labeling was
    produced. Use the SetInput function to set the LabelMap, and the
    SetFeatureImage function to set the feature image.

    Apply a colormap to a label map and put it on top of the input image.
    The set of colors is a good selection of distinct colors. The opacity
    of the label map can be defined by the user. A background label
    produce a gray pixel with the same intensity than the input one.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   LabelMapOverlayImageFilter, LabelOverlayImageFilter,
    LabelOverlayFunctor

    See:  LabelMapToBinaryImageFilter, LabelMapToLabelImageFilter, 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    PLAIN = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_PLAIN
    
    CONTOUR = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_CONTOUR
    
    SLICE_CONTOUR = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_SLICE_CONTOUR
    
    HIGH_LABEL_ON_TOP = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_HIGH_LABEL_ON_TOP
    
    LOW_LABEL_ON_TOP = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_LOW_LABEL_ON_TOP
    
    __New_orig__ = _swig_new_static_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_Clone)
    SetFeatureImage = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_SetFeatureImage)
    GetFeatureImage = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_GetFeatureImage)
    SetInput1 = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_SetInput2)
    SetOpacity = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_SetOpacity)
    GetOpacity = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_GetOpacity)
    SetType = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_SetType)
    GetType = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_GetType)
    SetPriority = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_SetPriority)
    GetPriority = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_GetPriority)
    SetDilationRadius = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_SetDilationRadius)
    GetDilationRadius = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_GetDilationRadius)
    SetContourThickness = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_SetContourThickness)
    GetContourThickness = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_GetContourThickness)
    SetSliceDimension = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_SetSliceDimension)
    GetSliceDimension = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_GetSliceDimension)
    SetFunctor = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_SetFunctor)
    GetFunctor = _swig_new_instance_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_GetFunctor)
    __swig_destroy__ = _itkLabelMapContourOverlayImageFilterPython.delete_itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4
    cast = _swig_new_static_method(_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4

        Create a new object of the class itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4 in _itkLabelMapContourOverlayImageFilterPython:
_itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_swigregister(itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4)
itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4___New_orig__ = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4___New_orig__
itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_cast = _itkLabelMapContourOverlayImageFilterPython.itkLabelMapContourOverlayImageFilterLM4IUC4IRGBUC4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def label_map_contour_overlay_image_filter(*args: itkt.ImageLike,  feature_image: itkt.Image=..., opacity: float=..., type: int=..., priority: int=..., dilation_radius: Sequence[int]=..., contour_thickness: Sequence[int]=..., slice_dimension: int=..., functor=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for LabelMapContourOverlayImageFilter"""
    import itk

    kwarg_typehints = { 'feature_image':feature_image,'opacity':opacity,'type':type,'priority':priority,'dilation_radius':dilation_radius,'contour_thickness':contour_thickness,'slice_dimension':slice_dimension,'functor':functor }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.LabelMapContourOverlayImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def label_map_contour_overlay_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKImageFusion.LabelMapContourOverlayImageFilter
    label_map_contour_overlay_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    label_map_contour_overlay_image_filter.__doc__ = filter_object.__doc__




