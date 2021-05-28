# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKLabelMapPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkLabelMapToBinaryImageFilterPython
else:
    import _itkLabelMapToBinaryImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLabelMapToBinaryImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLabelMapToBinaryImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkLabelMapFilterPython
import itk.itkStatisticsLabelObjectPython
import itk.itkHistogramPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkSamplePython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkAffineTransformPython
import itk.itkMatrixPython
import itk.itkCovariantVectorPython
import itk.itkPointPython
import itk.vnl_matrix_fixedPython
import itk.itkTransformBasePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkArray2DPython
import itk.itkVariableLengthVectorPython
import itk.itkOptimizerParametersPython
import itk.itkDiffusionTensor3DPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkShapeLabelObjectPython
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkLabelObjectPython
import itk.itkLabelObjectLinePython
import itk.ITKLabelMapBasePython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourceCommonPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython

def itkLabelMapToBinaryImageFilterLM2IUC2_New():
    return itkLabelMapToBinaryImageFilterLM2IUC2.New()

class itkLabelMapToBinaryImageFilterLM2IUC2(itk.itkLabelMapFilterPython.itkLabelMapFilterLM2IUC2):
    r"""


    Convert a LabelMap to a binary image.

    LabelMapToBinaryImageFilter to a binary image. All the objects in the
    image are used as foreground. The background values of the original
    binary image can be restored by passing this image to the filter with
    the SetBackgroundImage() method.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   LabelMapToLabelImageFilter, LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_Clone)
    SetBackgroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_GetForegroundValue)
    SetBackgroundImage = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetBackgroundImage)
    GetBackgroundImage = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_GetBackgroundImage)
    SetInput1 = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_SetInput2)
    __swig_destroy__ = _itkLabelMapToBinaryImageFilterPython.delete_itkLabelMapToBinaryImageFilterLM2IUC2
    cast = _swig_new_static_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToBinaryImageFilterLM2IUC2

        Create a new object of the class itkLabelMapToBinaryImageFilterLM2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToBinaryImageFilterLM2IUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToBinaryImageFilterLM2IUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToBinaryImageFilterLM2IUC2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToBinaryImageFilterLM2IUC2 in _itkLabelMapToBinaryImageFilterPython:
_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_swigregister(itkLabelMapToBinaryImageFilterLM2IUC2)
itkLabelMapToBinaryImageFilterLM2IUC2___New_orig__ = _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2___New_orig__
itkLabelMapToBinaryImageFilterLM2IUC2_cast = _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUC2_cast


def itkLabelMapToBinaryImageFilterLM2IUS2_New():
    return itkLabelMapToBinaryImageFilterLM2IUS2.New()

class itkLabelMapToBinaryImageFilterLM2IUS2(itk.itkLabelMapFilterPython.itkLabelMapFilterLM2IUS2):
    r"""


    Convert a LabelMap to a binary image.

    LabelMapToBinaryImageFilter to a binary image. All the objects in the
    image are used as foreground. The background values of the original
    binary image can be restored by passing this image to the filter with
    the SetBackgroundImage() method.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   LabelMapToLabelImageFilter, LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUS2_Clone)
    SetBackgroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUS2_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUS2_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUS2_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUS2_GetForegroundValue)
    SetBackgroundImage = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUS2_SetBackgroundImage)
    GetBackgroundImage = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUS2_GetBackgroundImage)
    SetInput1 = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUS2_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUS2_SetInput2)
    __swig_destroy__ = _itkLabelMapToBinaryImageFilterPython.delete_itkLabelMapToBinaryImageFilterLM2IUS2
    cast = _swig_new_static_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToBinaryImageFilterLM2IUS2

        Create a new object of the class itkLabelMapToBinaryImageFilterLM2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToBinaryImageFilterLM2IUS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToBinaryImageFilterLM2IUS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToBinaryImageFilterLM2IUS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToBinaryImageFilterLM2IUS2 in _itkLabelMapToBinaryImageFilterPython:
_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUS2_swigregister(itkLabelMapToBinaryImageFilterLM2IUS2)
itkLabelMapToBinaryImageFilterLM2IUS2___New_orig__ = _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUS2___New_orig__
itkLabelMapToBinaryImageFilterLM2IUS2_cast = _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM2IUS2_cast


def itkLabelMapToBinaryImageFilterLM3IUC3_New():
    return itkLabelMapToBinaryImageFilterLM3IUC3.New()

class itkLabelMapToBinaryImageFilterLM3IUC3(itk.itkLabelMapFilterPython.itkLabelMapFilterLM3IUC3):
    r"""


    Convert a LabelMap to a binary image.

    LabelMapToBinaryImageFilter to a binary image. All the objects in the
    image are used as foreground. The background values of the original
    binary image can be restored by passing this image to the filter with
    the SetBackgroundImage() method.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   LabelMapToLabelImageFilter, LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_Clone)
    SetBackgroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_GetForegroundValue)
    SetBackgroundImage = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetBackgroundImage)
    GetBackgroundImage = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_GetBackgroundImage)
    SetInput1 = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_SetInput2)
    __swig_destroy__ = _itkLabelMapToBinaryImageFilterPython.delete_itkLabelMapToBinaryImageFilterLM3IUC3
    cast = _swig_new_static_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToBinaryImageFilterLM3IUC3

        Create a new object of the class itkLabelMapToBinaryImageFilterLM3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToBinaryImageFilterLM3IUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToBinaryImageFilterLM3IUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToBinaryImageFilterLM3IUC3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToBinaryImageFilterLM3IUC3 in _itkLabelMapToBinaryImageFilterPython:
_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_swigregister(itkLabelMapToBinaryImageFilterLM3IUC3)
itkLabelMapToBinaryImageFilterLM3IUC3___New_orig__ = _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3___New_orig__
itkLabelMapToBinaryImageFilterLM3IUC3_cast = _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUC3_cast


def itkLabelMapToBinaryImageFilterLM3IUS3_New():
    return itkLabelMapToBinaryImageFilterLM3IUS3.New()

class itkLabelMapToBinaryImageFilterLM3IUS3(itk.itkLabelMapFilterPython.itkLabelMapFilterLM3IUS3):
    r"""


    Convert a LabelMap to a binary image.

    LabelMapToBinaryImageFilter to a binary image. All the objects in the
    image are used as foreground. The background values of the original
    binary image can be restored by passing this image to the filter with
    the SetBackgroundImage() method.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   LabelMapToLabelImageFilter, LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUS3_Clone)
    SetBackgroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUS3_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUS3_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUS3_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUS3_GetForegroundValue)
    SetBackgroundImage = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUS3_SetBackgroundImage)
    GetBackgroundImage = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUS3_GetBackgroundImage)
    SetInput1 = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUS3_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUS3_SetInput2)
    __swig_destroy__ = _itkLabelMapToBinaryImageFilterPython.delete_itkLabelMapToBinaryImageFilterLM3IUS3
    cast = _swig_new_static_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToBinaryImageFilterLM3IUS3

        Create a new object of the class itkLabelMapToBinaryImageFilterLM3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToBinaryImageFilterLM3IUS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToBinaryImageFilterLM3IUS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToBinaryImageFilterLM3IUS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToBinaryImageFilterLM3IUS3 in _itkLabelMapToBinaryImageFilterPython:
_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUS3_swigregister(itkLabelMapToBinaryImageFilterLM3IUS3)
itkLabelMapToBinaryImageFilterLM3IUS3___New_orig__ = _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUS3___New_orig__
itkLabelMapToBinaryImageFilterLM3IUS3_cast = _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM3IUS3_cast


def itkLabelMapToBinaryImageFilterLM4IUC4_New():
    return itkLabelMapToBinaryImageFilterLM4IUC4.New()

class itkLabelMapToBinaryImageFilterLM4IUC4(itk.itkLabelMapFilterPython.itkLabelMapFilterLM4IUC4):
    r"""


    Convert a LabelMap to a binary image.

    LabelMapToBinaryImageFilter to a binary image. All the objects in the
    image are used as foreground. The background values of the original
    binary image can be restored by passing this image to the filter with
    the SetBackgroundImage() method.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   LabelMapToLabelImageFilter, LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUC4___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUC4_Clone)
    SetBackgroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUC4_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUC4_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUC4_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUC4_GetForegroundValue)
    SetBackgroundImage = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUC4_SetBackgroundImage)
    GetBackgroundImage = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUC4_GetBackgroundImage)
    SetInput1 = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUC4_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUC4_SetInput2)
    __swig_destroy__ = _itkLabelMapToBinaryImageFilterPython.delete_itkLabelMapToBinaryImageFilterLM4IUC4
    cast = _swig_new_static_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUC4_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToBinaryImageFilterLM4IUC4

        Create a new object of the class itkLabelMapToBinaryImageFilterLM4IUC4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToBinaryImageFilterLM4IUC4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToBinaryImageFilterLM4IUC4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToBinaryImageFilterLM4IUC4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToBinaryImageFilterLM4IUC4 in _itkLabelMapToBinaryImageFilterPython:
_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUC4_swigregister(itkLabelMapToBinaryImageFilterLM4IUC4)
itkLabelMapToBinaryImageFilterLM4IUC4___New_orig__ = _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUC4___New_orig__
itkLabelMapToBinaryImageFilterLM4IUC4_cast = _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUC4_cast


def itkLabelMapToBinaryImageFilterLM4IUS4_New():
    return itkLabelMapToBinaryImageFilterLM4IUS4.New()

class itkLabelMapToBinaryImageFilterLM4IUS4(itk.itkLabelMapFilterPython.itkLabelMapFilterLM4IUS4):
    r"""


    Convert a LabelMap to a binary image.

    LabelMapToBinaryImageFilter to a binary image. All the objects in the
    image are used as foreground. The background values of the original
    binary image can be restored by passing this image to the filter with
    the SetBackgroundImage() method.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   LabelMapToLabelImageFilter, LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUS4___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUS4_Clone)
    SetBackgroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUS4_SetBackgroundValue)
    GetBackgroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUS4_GetBackgroundValue)
    SetForegroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUS4_SetForegroundValue)
    GetForegroundValue = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUS4_GetForegroundValue)
    SetBackgroundImage = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUS4_SetBackgroundImage)
    GetBackgroundImage = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUS4_GetBackgroundImage)
    SetInput1 = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUS4_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUS4_SetInput2)
    __swig_destroy__ = _itkLabelMapToBinaryImageFilterPython.delete_itkLabelMapToBinaryImageFilterLM4IUS4
    cast = _swig_new_static_method(_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUS4_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToBinaryImageFilterLM4IUS4

        Create a new object of the class itkLabelMapToBinaryImageFilterLM4IUS4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToBinaryImageFilterLM4IUS4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToBinaryImageFilterLM4IUS4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToBinaryImageFilterLM4IUS4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToBinaryImageFilterLM4IUS4 in _itkLabelMapToBinaryImageFilterPython:
_itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUS4_swigregister(itkLabelMapToBinaryImageFilterLM4IUS4)
itkLabelMapToBinaryImageFilterLM4IUS4___New_orig__ = _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUS4___New_orig__
itkLabelMapToBinaryImageFilterLM4IUS4_cast = _itkLabelMapToBinaryImageFilterPython.itkLabelMapToBinaryImageFilterLM4IUS4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def label_map_to_binary_image_filter(*args: itkt.ImageLike,  background_value: int=..., foreground_value: int=..., background_image: itkt.Image=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for LabelMapToBinaryImageFilter"""
    import itk

    kwarg_typehints = { 'background_value':background_value,'foreground_value':foreground_value,'background_image':background_image }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.LabelMapToBinaryImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def label_map_to_binary_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.LabelMapToBinaryImageFilter
    label_map_to_binary_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    label_map_to_binary_image_filter.__doc__ = filter_object.__doc__




