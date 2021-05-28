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
    from . import _itkShapeKeepNObjectsLabelMapFilterPython
else:
    import _itkShapeKeepNObjectsLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkShapeKeepNObjectsLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkShapeKeepNObjectsLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkInPlaceLabelMapFilterPython
import itk.itkLabelMapFilterPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkStatisticsLabelObjectPython
import itk.itkShapeLabelObjectPython
import itk.itkLabelObjectPython
import itk.itkLabelObjectLinePython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkMatrixPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkCovariantVectorPython
import itk.itkImageRegionPython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkDiffusionTensor3DPython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkTransformBasePython
import itk.itkVariableLengthVectorPython
import itk.itkArray2DPython
import itk.itkHistogramPython
import itk.itkSamplePython
import itk.ITKLabelMapBasePython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython

def itkShapeKeepNObjectsLabelMapFilterLM2_New():
    return itkShapeKeepNObjectsLabelMapFilterLM2.New()

class itkShapeKeepNObjectsLabelMapFilterLM2(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    r"""


    Keep N objects according to their shape attributes.

    The ShapeKeepNObjectsLabelMapFilter keeps N objects in a label
    collection image with the highest (or lowest) attribute value. The
    attributes values are those of the ShapeLabelObject.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, BinaryShapeKeepNObjectsImageFilter,
    LabelStatisticsKeepNObjectsImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_Clone)
    SetReverseOrdering = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_SetReverseOrdering)
    GetReverseOrdering = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_GetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_ReverseOrderingOff)
    SetNumberOfObjects = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_SetNumberOfObjects)
    GetNumberOfObjects = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_GetNumberOfObjects)
    GetAttribute = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_SetAttribute)
    __swig_destroy__ = _itkShapeKeepNObjectsLabelMapFilterPython.delete_itkShapeKeepNObjectsLabelMapFilterLM2
    cast = _swig_new_static_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkShapeKeepNObjectsLabelMapFilterLM2

        Create a new object of the class itkShapeKeepNObjectsLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeKeepNObjectsLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapeKeepNObjectsLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapeKeepNObjectsLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeKeepNObjectsLabelMapFilterLM2 in _itkShapeKeepNObjectsLabelMapFilterPython:
_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_swigregister(itkShapeKeepNObjectsLabelMapFilterLM2)
itkShapeKeepNObjectsLabelMapFilterLM2___New_orig__ = _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2___New_orig__
itkShapeKeepNObjectsLabelMapFilterLM2_cast = _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM2_cast


def itkShapeKeepNObjectsLabelMapFilterLM3_New():
    return itkShapeKeepNObjectsLabelMapFilterLM3.New()

class itkShapeKeepNObjectsLabelMapFilterLM3(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    r"""


    Keep N objects according to their shape attributes.

    The ShapeKeepNObjectsLabelMapFilter keeps N objects in a label
    collection image with the highest (or lowest) attribute value. The
    attributes values are those of the ShapeLabelObject.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, BinaryShapeKeepNObjectsImageFilter,
    LabelStatisticsKeepNObjectsImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_Clone)
    SetReverseOrdering = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_SetReverseOrdering)
    GetReverseOrdering = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_GetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_ReverseOrderingOff)
    SetNumberOfObjects = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_SetNumberOfObjects)
    GetNumberOfObjects = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_GetNumberOfObjects)
    GetAttribute = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_SetAttribute)
    __swig_destroy__ = _itkShapeKeepNObjectsLabelMapFilterPython.delete_itkShapeKeepNObjectsLabelMapFilterLM3
    cast = _swig_new_static_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkShapeKeepNObjectsLabelMapFilterLM3

        Create a new object of the class itkShapeKeepNObjectsLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeKeepNObjectsLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapeKeepNObjectsLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapeKeepNObjectsLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeKeepNObjectsLabelMapFilterLM3 in _itkShapeKeepNObjectsLabelMapFilterPython:
_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_swigregister(itkShapeKeepNObjectsLabelMapFilterLM3)
itkShapeKeepNObjectsLabelMapFilterLM3___New_orig__ = _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3___New_orig__
itkShapeKeepNObjectsLabelMapFilterLM3_cast = _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM3_cast


def itkShapeKeepNObjectsLabelMapFilterLM4_New():
    return itkShapeKeepNObjectsLabelMapFilterLM4.New()

class itkShapeKeepNObjectsLabelMapFilterLM4(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4):
    r"""


    Keep N objects according to their shape attributes.

    The ShapeKeepNObjectsLabelMapFilter keeps N objects in a label
    collection image with the highest (or lowest) attribute value. The
    attributes values are those of the ShapeLabelObject.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, BinaryShapeKeepNObjectsImageFilter,
    LabelStatisticsKeepNObjectsImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4_Clone)
    SetReverseOrdering = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4_SetReverseOrdering)
    GetReverseOrdering = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4_GetReverseOrdering)
    ReverseOrderingOn = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4_ReverseOrderingOn)
    ReverseOrderingOff = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4_ReverseOrderingOff)
    SetNumberOfObjects = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4_SetNumberOfObjects)
    GetNumberOfObjects = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4_GetNumberOfObjects)
    GetAttribute = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4_GetAttribute)
    SetAttribute = _swig_new_instance_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4_SetAttribute)
    __swig_destroy__ = _itkShapeKeepNObjectsLabelMapFilterPython.delete_itkShapeKeepNObjectsLabelMapFilterLM4
    cast = _swig_new_static_method(_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkShapeKeepNObjectsLabelMapFilterLM4

        Create a new object of the class itkShapeKeepNObjectsLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShapeKeepNObjectsLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShapeKeepNObjectsLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShapeKeepNObjectsLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShapeKeepNObjectsLabelMapFilterLM4 in _itkShapeKeepNObjectsLabelMapFilterPython:
_itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4_swigregister(itkShapeKeepNObjectsLabelMapFilterLM4)
itkShapeKeepNObjectsLabelMapFilterLM4___New_orig__ = _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4___New_orig__
itkShapeKeepNObjectsLabelMapFilterLM4_cast = _itkShapeKeepNObjectsLabelMapFilterPython.itkShapeKeepNObjectsLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def shape_keep_n_objects_label_map_filter(*args: itkt.ImageLike,  reverse_ordering: bool=..., number_of_objects: int=..., attribute: int=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for ShapeKeepNObjectsLabelMapFilter"""
    import itk

    kwarg_typehints = { 'reverse_ordering':reverse_ordering,'number_of_objects':number_of_objects,'attribute':attribute }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.ShapeKeepNObjectsLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def shape_keep_n_objects_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.ShapeKeepNObjectsLabelMapFilter
    shape_keep_n_objects_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    shape_keep_n_objects_label_map_filter.__doc__ = filter_object.__doc__




