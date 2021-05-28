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
    from . import _itkLabelMapToLabelImageFilterPython
else:
    import _itkLabelMapToLabelImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLabelMapToLabelImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLabelMapToLabelImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.ITKLabelMapBasePython
import itk.itkImageRegionPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkStatisticsLabelObjectPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkShapeLabelObjectPython
import itk.itkLabelObjectPython
import itk.itkLabelObjectLinePython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkArray2DPython
import itk.itkVariableLengthVectorPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkDiffusionTensor3DPython
import itk.itkTransformBasePython
import itk.itkHistogramPython
import itk.itkSamplePython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImagePython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython

def itkLabelMapToLabelImageFilterLM2IUC2_New():
    return itkLabelMapToLabelImageFilterLM2IUC2.New()

class itkLabelMapToLabelImageFilterLM2IUC2(itk.itkLabelMapFilterPython.itkLabelMapFilterLM2IUC2):
    r"""


    Converts a LabelMap to a labeled image.

    LabelMapToBinaryImageFilter to a label image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   LabelMapToBinaryImageFilter, LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_Clone)
    SameDimensionCheck = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_SameDimensionCheck
    
    __swig_destroy__ = _itkLabelMapToLabelImageFilterPython.delete_itkLabelMapToLabelImageFilterLM2IUC2
    cast = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToLabelImageFilterLM2IUC2

        Create a new object of the class itkLabelMapToLabelImageFilterLM2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToLabelImageFilterLM2IUC2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToLabelImageFilterLM2IUC2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToLabelImageFilterLM2IUC2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToLabelImageFilterLM2IUC2 in _itkLabelMapToLabelImageFilterPython:
_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_swigregister(itkLabelMapToLabelImageFilterLM2IUC2)
itkLabelMapToLabelImageFilterLM2IUC2___New_orig__ = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2___New_orig__
itkLabelMapToLabelImageFilterLM2IUC2_cast = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUC2_cast


def itkLabelMapToLabelImageFilterLM2IUS2_New():
    return itkLabelMapToLabelImageFilterLM2IUS2.New()

class itkLabelMapToLabelImageFilterLM2IUS2(itk.itkLabelMapFilterPython.itkLabelMapFilterLM2IUS2):
    r"""


    Converts a LabelMap to a labeled image.

    LabelMapToBinaryImageFilter to a label image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   LabelMapToBinaryImageFilter, LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_Clone)
    SameDimensionCheck = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_SameDimensionCheck
    
    __swig_destroy__ = _itkLabelMapToLabelImageFilterPython.delete_itkLabelMapToLabelImageFilterLM2IUS2
    cast = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToLabelImageFilterLM2IUS2

        Create a new object of the class itkLabelMapToLabelImageFilterLM2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToLabelImageFilterLM2IUS2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToLabelImageFilterLM2IUS2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToLabelImageFilterLM2IUS2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToLabelImageFilterLM2IUS2 in _itkLabelMapToLabelImageFilterPython:
_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_swigregister(itkLabelMapToLabelImageFilterLM2IUS2)
itkLabelMapToLabelImageFilterLM2IUS2___New_orig__ = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2___New_orig__
itkLabelMapToLabelImageFilterLM2IUS2_cast = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM2IUS2_cast


def itkLabelMapToLabelImageFilterLM3IUC3_New():
    return itkLabelMapToLabelImageFilterLM3IUC3.New()

class itkLabelMapToLabelImageFilterLM3IUC3(itk.itkLabelMapFilterPython.itkLabelMapFilterLM3IUC3):
    r"""


    Converts a LabelMap to a labeled image.

    LabelMapToBinaryImageFilter to a label image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   LabelMapToBinaryImageFilter, LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_Clone)
    SameDimensionCheck = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_SameDimensionCheck
    
    __swig_destroy__ = _itkLabelMapToLabelImageFilterPython.delete_itkLabelMapToLabelImageFilterLM3IUC3
    cast = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToLabelImageFilterLM3IUC3

        Create a new object of the class itkLabelMapToLabelImageFilterLM3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToLabelImageFilterLM3IUC3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToLabelImageFilterLM3IUC3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToLabelImageFilterLM3IUC3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToLabelImageFilterLM3IUC3 in _itkLabelMapToLabelImageFilterPython:
_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_swigregister(itkLabelMapToLabelImageFilterLM3IUC3)
itkLabelMapToLabelImageFilterLM3IUC3___New_orig__ = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3___New_orig__
itkLabelMapToLabelImageFilterLM3IUC3_cast = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUC3_cast


def itkLabelMapToLabelImageFilterLM3IUS3_New():
    return itkLabelMapToLabelImageFilterLM3IUS3.New()

class itkLabelMapToLabelImageFilterLM3IUS3(itk.itkLabelMapFilterPython.itkLabelMapFilterLM3IUS3):
    r"""


    Converts a LabelMap to a labeled image.

    LabelMapToBinaryImageFilter to a label image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   LabelMapToBinaryImageFilter, LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_Clone)
    SameDimensionCheck = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_SameDimensionCheck
    
    __swig_destroy__ = _itkLabelMapToLabelImageFilterPython.delete_itkLabelMapToLabelImageFilterLM3IUS3
    cast = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToLabelImageFilterLM3IUS3

        Create a new object of the class itkLabelMapToLabelImageFilterLM3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToLabelImageFilterLM3IUS3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToLabelImageFilterLM3IUS3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToLabelImageFilterLM3IUS3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToLabelImageFilterLM3IUS3 in _itkLabelMapToLabelImageFilterPython:
_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_swigregister(itkLabelMapToLabelImageFilterLM3IUS3)
itkLabelMapToLabelImageFilterLM3IUS3___New_orig__ = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3___New_orig__
itkLabelMapToLabelImageFilterLM3IUS3_cast = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM3IUS3_cast


def itkLabelMapToLabelImageFilterLM4IUC4_New():
    return itkLabelMapToLabelImageFilterLM4IUC4.New()

class itkLabelMapToLabelImageFilterLM4IUC4(itk.itkLabelMapFilterPython.itkLabelMapFilterLM4IUC4):
    r"""


    Converts a LabelMap to a labeled image.

    LabelMapToBinaryImageFilter to a label image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   LabelMapToBinaryImageFilter, LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM4IUC4___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM4IUC4_Clone)
    SameDimensionCheck = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM4IUC4_SameDimensionCheck
    
    __swig_destroy__ = _itkLabelMapToLabelImageFilterPython.delete_itkLabelMapToLabelImageFilterLM4IUC4
    cast = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM4IUC4_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToLabelImageFilterLM4IUC4

        Create a new object of the class itkLabelMapToLabelImageFilterLM4IUC4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToLabelImageFilterLM4IUC4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToLabelImageFilterLM4IUC4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToLabelImageFilterLM4IUC4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToLabelImageFilterLM4IUC4 in _itkLabelMapToLabelImageFilterPython:
_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM4IUC4_swigregister(itkLabelMapToLabelImageFilterLM4IUC4)
itkLabelMapToLabelImageFilterLM4IUC4___New_orig__ = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM4IUC4___New_orig__
itkLabelMapToLabelImageFilterLM4IUC4_cast = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM4IUC4_cast


def itkLabelMapToLabelImageFilterLM4IUS4_New():
    return itkLabelMapToLabelImageFilterLM4IUS4.New()

class itkLabelMapToLabelImageFilterLM4IUS4(itk.itkLabelMapFilterPython.itkLabelMapFilterLM4IUS4):
    r"""


    Converts a LabelMap to a labeled image.

    LabelMapToBinaryImageFilter to a label image.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   LabelMapToBinaryImageFilter, LabelMapMaskImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM4IUS4___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM4IUS4_Clone)
    SameDimensionCheck = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM4IUS4_SameDimensionCheck
    
    __swig_destroy__ = _itkLabelMapToLabelImageFilterPython.delete_itkLabelMapToLabelImageFilterLM4IUS4
    cast = _swig_new_static_method(_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM4IUS4_cast)

    def New(*args, **kargs):
        """New() -> itkLabelMapToLabelImageFilterLM4IUS4

        Create a new object of the class itkLabelMapToLabelImageFilterLM4IUS4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelMapToLabelImageFilterLM4IUS4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLabelMapToLabelImageFilterLM4IUS4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLabelMapToLabelImageFilterLM4IUS4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelMapToLabelImageFilterLM4IUS4 in _itkLabelMapToLabelImageFilterPython:
_itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM4IUS4_swigregister(itkLabelMapToLabelImageFilterLM4IUS4)
itkLabelMapToLabelImageFilterLM4IUS4___New_orig__ = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM4IUS4___New_orig__
itkLabelMapToLabelImageFilterLM4IUS4_cast = _itkLabelMapToLabelImageFilterPython.itkLabelMapToLabelImageFilterLM4IUS4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def label_map_to_label_image_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for LabelMapToLabelImageFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.LabelMapToLabelImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def label_map_to_label_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.LabelMapToLabelImageFilter
    label_map_to_label_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    label_map_to_label_image_filter.__doc__ = filter_object.__doc__




