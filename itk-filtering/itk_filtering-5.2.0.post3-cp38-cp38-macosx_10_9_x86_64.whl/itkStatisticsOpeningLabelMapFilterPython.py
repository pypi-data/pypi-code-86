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
    from . import _itkStatisticsOpeningLabelMapFilterPython
else:
    import _itkStatisticsOpeningLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkStatisticsOpeningLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkStatisticsOpeningLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkShapeOpeningLabelMapFilterPython
import itk.itkInPlaceLabelMapFilterPython
import itk.itkLabelMapFilterPython
import itk.itkStatisticsLabelObjectPython
import itk.itkHistogramPython
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

def itkStatisticsOpeningLabelMapFilterLM2_New():
    return itkStatisticsOpeningLabelMapFilterLM2.New()

class itkStatisticsOpeningLabelMapFilterLM2(itk.itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM2):
    r"""


    remove the objects according to the value of their statistics
    attribute

    StatisticsOpeningLabelMapFilter removes the objects in a label
    collection image with an attribute value smaller or greater than a
    threshold called Lambda. The attributes are the ones of the
    StatisticsLabelObject.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   StatisticsLabelObject, BinaryStatisticsOpeningImageFilter,
    LabelShapeOpeningImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM2_Clone)
    __swig_destroy__ = _itkStatisticsOpeningLabelMapFilterPython.delete_itkStatisticsOpeningLabelMapFilterLM2
    cast = _swig_new_static_method(_itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsOpeningLabelMapFilterLM2

        Create a new object of the class itkStatisticsOpeningLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsOpeningLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStatisticsOpeningLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStatisticsOpeningLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsOpeningLabelMapFilterLM2 in _itkStatisticsOpeningLabelMapFilterPython:
_itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM2_swigregister(itkStatisticsOpeningLabelMapFilterLM2)
itkStatisticsOpeningLabelMapFilterLM2___New_orig__ = _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM2___New_orig__
itkStatisticsOpeningLabelMapFilterLM2_cast = _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM2_cast


def itkStatisticsOpeningLabelMapFilterLM3_New():
    return itkStatisticsOpeningLabelMapFilterLM3.New()

class itkStatisticsOpeningLabelMapFilterLM3(itk.itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM3):
    r"""


    remove the objects according to the value of their statistics
    attribute

    StatisticsOpeningLabelMapFilter removes the objects in a label
    collection image with an attribute value smaller or greater than a
    threshold called Lambda. The attributes are the ones of the
    StatisticsLabelObject.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   StatisticsLabelObject, BinaryStatisticsOpeningImageFilter,
    LabelShapeOpeningImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM3_Clone)
    __swig_destroy__ = _itkStatisticsOpeningLabelMapFilterPython.delete_itkStatisticsOpeningLabelMapFilterLM3
    cast = _swig_new_static_method(_itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsOpeningLabelMapFilterLM3

        Create a new object of the class itkStatisticsOpeningLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsOpeningLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStatisticsOpeningLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStatisticsOpeningLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsOpeningLabelMapFilterLM3 in _itkStatisticsOpeningLabelMapFilterPython:
_itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM3_swigregister(itkStatisticsOpeningLabelMapFilterLM3)
itkStatisticsOpeningLabelMapFilterLM3___New_orig__ = _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM3___New_orig__
itkStatisticsOpeningLabelMapFilterLM3_cast = _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM3_cast


def itkStatisticsOpeningLabelMapFilterLM4_New():
    return itkStatisticsOpeningLabelMapFilterLM4.New()

class itkStatisticsOpeningLabelMapFilterLM4(itk.itkShapeOpeningLabelMapFilterPython.itkShapeOpeningLabelMapFilterLM4):
    r"""


    remove the objects according to the value of their statistics
    attribute

    StatisticsOpeningLabelMapFilter removes the objects in a label
    collection image with an attribute value smaller or greater than a
    threshold called Lambda. The attributes are the ones of the
    StatisticsLabelObject.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   StatisticsLabelObject, BinaryStatisticsOpeningImageFilter,
    LabelShapeOpeningImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM4_Clone)
    __swig_destroy__ = _itkStatisticsOpeningLabelMapFilterPython.delete_itkStatisticsOpeningLabelMapFilterLM4
    cast = _swig_new_static_method(_itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsOpeningLabelMapFilterLM4

        Create a new object of the class itkStatisticsOpeningLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsOpeningLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStatisticsOpeningLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStatisticsOpeningLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsOpeningLabelMapFilterLM4 in _itkStatisticsOpeningLabelMapFilterPython:
_itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM4_swigregister(itkStatisticsOpeningLabelMapFilterLM4)
itkStatisticsOpeningLabelMapFilterLM4___New_orig__ = _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM4___New_orig__
itkStatisticsOpeningLabelMapFilterLM4_cast = _itkStatisticsOpeningLabelMapFilterPython.itkStatisticsOpeningLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def statistics_opening_label_map_filter(*args: itkt.ImageLike,  reverse_ordering: bool=..., attribute: Union[str, int]=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for StatisticsOpeningLabelMapFilter"""
    import itk

    kwarg_typehints = { 'reverse_ordering':reverse_ordering,'attribute':attribute }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.StatisticsOpeningLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def statistics_opening_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.StatisticsOpeningLabelMapFilter
    statistics_opening_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    statistics_opening_label_map_filter.__doc__ = filter_object.__doc__




