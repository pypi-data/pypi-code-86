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
    from . import _itkMergeLabelMapFilterPython
else:
    import _itkMergeLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMergeLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMergeLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkInPlaceLabelMapFilterPython
import itk.ITKLabelMapBasePython
import itk.itkImageToImageFilterCommonPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkImagePython
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
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkImageSourceCommonPython
import itk.itkStatisticsLabelObjectPython
import itk.itkHistogramPython
import itk.itkArrayPython
import itk.itkSamplePython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkArray2DPython
import itk.itkTransformBasePython
import itk.itkOptimizerParametersPython
import itk.itkDiffusionTensor3DPython
import itk.itkVariableLengthVectorPython
import itk.itkShapeLabelObjectPython
import itk.itkLabelObjectPython
import itk.itkLabelObjectLinePython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkLabelMapFilterPython
class itkMergeLabelMapFilterEnums(object):
    r"""Proxy of C++ itkMergeLabelMapFilterEnums class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    ChoiceMethod_KEEP = _itkMergeLabelMapFilterPython.itkMergeLabelMapFilterEnums_ChoiceMethod_KEEP
    
    ChoiceMethod_AGGREGATE = _itkMergeLabelMapFilterPython.itkMergeLabelMapFilterEnums_ChoiceMethod_AGGREGATE
    
    ChoiceMethod_PACK = _itkMergeLabelMapFilterPython.itkMergeLabelMapFilterEnums_ChoiceMethod_PACK
    
    ChoiceMethod_STRICT = _itkMergeLabelMapFilterPython.itkMergeLabelMapFilterEnums_ChoiceMethod_STRICT
    

    def __init__(self, *args):
        r"""
        __init__(self) -> itkMergeLabelMapFilterEnums
        __init__(self, arg0) -> itkMergeLabelMapFilterEnums

        Parameters
        ----------
        arg0: itkMergeLabelMapFilterEnums const &

        """
        _itkMergeLabelMapFilterPython.itkMergeLabelMapFilterEnums_swiginit(self, _itkMergeLabelMapFilterPython.new_itkMergeLabelMapFilterEnums(*args))
    __swig_destroy__ = _itkMergeLabelMapFilterPython.delete_itkMergeLabelMapFilterEnums

# Register itkMergeLabelMapFilterEnums in _itkMergeLabelMapFilterPython:
_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterEnums_swigregister(itkMergeLabelMapFilterEnums)


def itkMergeLabelMapFilterLM2_New():
    return itkMergeLabelMapFilterLM2.New()

class itkMergeLabelMapFilterLM2(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2):
    r"""


    Merges several Label Maps.

    This filter takes one or more input Label Map and merges them.

    SetMethod() can be used to change how the filter manage the labels
    from the different label maps. KEEP (0): MergeLabelMapFilter do its
    best to keep the label unchanged, but if a label is already used in a
    previous label map, a new label is assigned. AGGREGATE (1): If the
    same label is found several times in the label maps, the label objects
    with the same label are merged. PACK (2): MergeLabelMapFilter relabel
    all the label objects by order of processing. No conflict can occur.
    STRICT (3): MergeLabelMapFilter keeps the labels unchanged and raises
    an exception if the same label is found in several images.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter
    example{Filtering/LabelMap/MergeLabelMaps,Merge LabelMaps} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM2_Clone)
    SetMethod = _swig_new_instance_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM2_SetMethod)
    GetMethod = _swig_new_instance_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM2_GetMethod)
    __swig_destroy__ = _itkMergeLabelMapFilterPython.delete_itkMergeLabelMapFilterLM2
    cast = _swig_new_static_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkMergeLabelMapFilterLM2

        Create a new object of the class itkMergeLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMergeLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMergeLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMergeLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMergeLabelMapFilterLM2 in _itkMergeLabelMapFilterPython:
_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM2_swigregister(itkMergeLabelMapFilterLM2)
itkMergeLabelMapFilterLM2___New_orig__ = _itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM2___New_orig__
itkMergeLabelMapFilterLM2_cast = _itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM2_cast


def itkMergeLabelMapFilterLM3_New():
    return itkMergeLabelMapFilterLM3.New()

class itkMergeLabelMapFilterLM3(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3):
    r"""


    Merges several Label Maps.

    This filter takes one or more input Label Map and merges them.

    SetMethod() can be used to change how the filter manage the labels
    from the different label maps. KEEP (0): MergeLabelMapFilter do its
    best to keep the label unchanged, but if a label is already used in a
    previous label map, a new label is assigned. AGGREGATE (1): If the
    same label is found several times in the label maps, the label objects
    with the same label are merged. PACK (2): MergeLabelMapFilter relabel
    all the label objects by order of processing. No conflict can occur.
    STRICT (3): MergeLabelMapFilter keeps the labels unchanged and raises
    an exception if the same label is found in several images.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter
    example{Filtering/LabelMap/MergeLabelMaps,Merge LabelMaps} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM3_Clone)
    SetMethod = _swig_new_instance_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM3_SetMethod)
    GetMethod = _swig_new_instance_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM3_GetMethod)
    __swig_destroy__ = _itkMergeLabelMapFilterPython.delete_itkMergeLabelMapFilterLM3
    cast = _swig_new_static_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkMergeLabelMapFilterLM3

        Create a new object of the class itkMergeLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMergeLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMergeLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMergeLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMergeLabelMapFilterLM3 in _itkMergeLabelMapFilterPython:
_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM3_swigregister(itkMergeLabelMapFilterLM3)
itkMergeLabelMapFilterLM3___New_orig__ = _itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM3___New_orig__
itkMergeLabelMapFilterLM3_cast = _itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM3_cast


def itkMergeLabelMapFilterLM4_New():
    return itkMergeLabelMapFilterLM4.New()

class itkMergeLabelMapFilterLM4(itk.itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4):
    r"""


    Merges several Label Maps.

    This filter takes one or more input Label Map and merges them.

    SetMethod() can be used to change how the filter manage the labels
    from the different label maps. KEEP (0): MergeLabelMapFilter do its
    best to keep the label unchanged, but if a label is already used in a
    previous label map, a new label is assigned. AGGREGATE (1): If the
    same label is found several times in the label maps, the label objects
    with the same label are merged. PACK (2): MergeLabelMapFilter relabel
    all the label objects by order of processing. No conflict can occur.
    STRICT (3): MergeLabelMapFilter keeps the labels unchanged and raises
    an exception if the same label is found in several images.

    This implementation was taken from the Insight Journal
    paper:https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   ShapeLabelObject, RelabelComponentImageFilter
    example{Filtering/LabelMap/MergeLabelMaps,Merge LabelMaps} 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM4_Clone)
    SetMethod = _swig_new_instance_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM4_SetMethod)
    GetMethod = _swig_new_instance_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM4_GetMethod)
    __swig_destroy__ = _itkMergeLabelMapFilterPython.delete_itkMergeLabelMapFilterLM4
    cast = _swig_new_static_method(_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkMergeLabelMapFilterLM4

        Create a new object of the class itkMergeLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMergeLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMergeLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMergeLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMergeLabelMapFilterLM4 in _itkMergeLabelMapFilterPython:
_itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM4_swigregister(itkMergeLabelMapFilterLM4)
itkMergeLabelMapFilterLM4___New_orig__ = _itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM4___New_orig__
itkMergeLabelMapFilterLM4_cast = _itkMergeLabelMapFilterPython.itkMergeLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def merge_label_map_filter(*args: itkt.ImageLike,  method=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for MergeLabelMapFilter"""
    import itk

    kwarg_typehints = { 'method':method }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.MergeLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def merge_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.MergeLabelMapFilter
    merge_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    merge_label_map_filter.__doc__ = filter_object.__doc__




