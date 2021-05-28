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
    from . import _itkInPlaceLabelMapFilterPython
else:
    import _itkInPlaceLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkInPlaceLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkInPlaceLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.ITKLabelMapBasePython
import itk.itkImageRegionPython
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
import itk.itkLabelMapFilterPython

def itkInPlaceLabelMapFilterLM2_New():
    return itkInPlaceLabelMapFilterLM2.New()

class itkInPlaceLabelMapFilterLM2(itk.itkLabelMapFilterPython.itkLabelMapFilterLM2LM2):
    r"""


    Base class for filters that takes an image as input and overwrites
    that image as the output.

    InPlaceLabelMapFilter is the base class for all process objects whose
    output image data is constructed by overwriting the input image data.
    In other words, the output bulk data is the same block of memory as
    the input bulk data. This filter provides the mechanisms for in place
    image processing while maintaining general pipeline mechanics.
    InPlaceLabelMapFilters use less memory than standard
    ImageToImageFilters because the input buffer is reused as the output
    buffer. However, this benefit does not come without a cost. Since the
    filter overwrites its input, the ownership of the bulk data is
    transitioned from the input data object to the output data object.
    When a data object has multiple consumers with one of the consumers
    being an in place filter, the in place filter effectively destroys the
    bulk data for the data object. Upstream filters will then have to re-
    execute to regenerate the data object's bulk data for the remaining
    consumers.

    Since an InPlaceLabelMapFilter reuses the input bulk data memory for
    the output bulk data memory, the input image type must match the
    output image type. If the input and output image types are not
    identical, the filter reverts to a traditional ImageToImageFilter
    behaviour where an output image is allocated. In place operation can
    also be controlled (when the input and output image type match) via
    the methods InPlaceOn() and InPlaceOff().

    Subclasses of InPlaceLabelMapFilter must take extra care in how they
    manage memory using (and perhaps overriding) the implementations of
    ReleaseInputs() and AllocateOutputs() provided here.

    This code was contributed in the Insight Journal paper: "Label object
    representation and manipulation with ITK" by Lehmann
    G.https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   LabelMapToBinaryImageFilter, LabelMapToLabelImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_Clone)
    SetInPlace = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_SetInPlace)
    GetInPlace = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_GetInPlace)
    InPlaceOn = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_InPlaceOn)
    InPlaceOff = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_InPlaceOff)
    CanRunInPlace = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_CanRunInPlace)
    __swig_destroy__ = _itkInPlaceLabelMapFilterPython.delete_itkInPlaceLabelMapFilterLM2
    cast = _swig_new_static_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkInPlaceLabelMapFilterLM2

        Create a new object of the class itkInPlaceLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInPlaceLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkInPlaceLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkInPlaceLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkInPlaceLabelMapFilterLM2 in _itkInPlaceLabelMapFilterPython:
_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_swigregister(itkInPlaceLabelMapFilterLM2)
itkInPlaceLabelMapFilterLM2___New_orig__ = _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2___New_orig__
itkInPlaceLabelMapFilterLM2_cast = _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM2_cast


def itkInPlaceLabelMapFilterLM3_New():
    return itkInPlaceLabelMapFilterLM3.New()

class itkInPlaceLabelMapFilterLM3(itk.itkLabelMapFilterPython.itkLabelMapFilterLM3LM3):
    r"""


    Base class for filters that takes an image as input and overwrites
    that image as the output.

    InPlaceLabelMapFilter is the base class for all process objects whose
    output image data is constructed by overwriting the input image data.
    In other words, the output bulk data is the same block of memory as
    the input bulk data. This filter provides the mechanisms for in place
    image processing while maintaining general pipeline mechanics.
    InPlaceLabelMapFilters use less memory than standard
    ImageToImageFilters because the input buffer is reused as the output
    buffer. However, this benefit does not come without a cost. Since the
    filter overwrites its input, the ownership of the bulk data is
    transitioned from the input data object to the output data object.
    When a data object has multiple consumers with one of the consumers
    being an in place filter, the in place filter effectively destroys the
    bulk data for the data object. Upstream filters will then have to re-
    execute to regenerate the data object's bulk data for the remaining
    consumers.

    Since an InPlaceLabelMapFilter reuses the input bulk data memory for
    the output bulk data memory, the input image type must match the
    output image type. If the input and output image types are not
    identical, the filter reverts to a traditional ImageToImageFilter
    behaviour where an output image is allocated. In place operation can
    also be controlled (when the input and output image type match) via
    the methods InPlaceOn() and InPlaceOff().

    Subclasses of InPlaceLabelMapFilter must take extra care in how they
    manage memory using (and perhaps overriding) the implementations of
    ReleaseInputs() and AllocateOutputs() provided here.

    This code was contributed in the Insight Journal paper: "Label object
    representation and manipulation with ITK" by Lehmann
    G.https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   LabelMapToBinaryImageFilter, LabelMapToLabelImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_Clone)
    SetInPlace = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_SetInPlace)
    GetInPlace = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_GetInPlace)
    InPlaceOn = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_InPlaceOn)
    InPlaceOff = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_InPlaceOff)
    CanRunInPlace = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_CanRunInPlace)
    __swig_destroy__ = _itkInPlaceLabelMapFilterPython.delete_itkInPlaceLabelMapFilterLM3
    cast = _swig_new_static_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkInPlaceLabelMapFilterLM3

        Create a new object of the class itkInPlaceLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInPlaceLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkInPlaceLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkInPlaceLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkInPlaceLabelMapFilterLM3 in _itkInPlaceLabelMapFilterPython:
_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_swigregister(itkInPlaceLabelMapFilterLM3)
itkInPlaceLabelMapFilterLM3___New_orig__ = _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3___New_orig__
itkInPlaceLabelMapFilterLM3_cast = _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM3_cast


def itkInPlaceLabelMapFilterLM4_New():
    return itkInPlaceLabelMapFilterLM4.New()

class itkInPlaceLabelMapFilterLM4(itk.itkLabelMapFilterPython.itkLabelMapFilterLM4LM4):
    r"""


    Base class for filters that takes an image as input and overwrites
    that image as the output.

    InPlaceLabelMapFilter is the base class for all process objects whose
    output image data is constructed by overwriting the input image data.
    In other words, the output bulk data is the same block of memory as
    the input bulk data. This filter provides the mechanisms for in place
    image processing while maintaining general pipeline mechanics.
    InPlaceLabelMapFilters use less memory than standard
    ImageToImageFilters because the input buffer is reused as the output
    buffer. However, this benefit does not come without a cost. Since the
    filter overwrites its input, the ownership of the bulk data is
    transitioned from the input data object to the output data object.
    When a data object has multiple consumers with one of the consumers
    being an in place filter, the in place filter effectively destroys the
    bulk data for the data object. Upstream filters will then have to re-
    execute to regenerate the data object's bulk data for the remaining
    consumers.

    Since an InPlaceLabelMapFilter reuses the input bulk data memory for
    the output bulk data memory, the input image type must match the
    output image type. If the input and output image types are not
    identical, the filter reverts to a traditional ImageToImageFilter
    behaviour where an output image is allocated. In place operation can
    also be controlled (when the input and output image type match) via
    the methods InPlaceOn() and InPlaceOff().

    Subclasses of InPlaceLabelMapFilter must take extra care in how they
    manage memory using (and perhaps overriding) the implementations of
    ReleaseInputs() and AllocateOutputs() provided here.

    This code was contributed in the Insight Journal paper: "Label object
    representation and manipulation with ITK" by Lehmann
    G.https://www.insight-journal.org/browse/publication/176

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.

    See:   LabelMapToBinaryImageFilter, LabelMapToLabelImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4_Clone)
    SetInPlace = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4_SetInPlace)
    GetInPlace = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4_GetInPlace)
    InPlaceOn = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4_InPlaceOn)
    InPlaceOff = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4_InPlaceOff)
    CanRunInPlace = _swig_new_instance_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4_CanRunInPlace)
    __swig_destroy__ = _itkInPlaceLabelMapFilterPython.delete_itkInPlaceLabelMapFilterLM4
    cast = _swig_new_static_method(_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkInPlaceLabelMapFilterLM4

        Create a new object of the class itkInPlaceLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkInPlaceLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkInPlaceLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkInPlaceLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkInPlaceLabelMapFilterLM4 in _itkInPlaceLabelMapFilterPython:
_itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4_swigregister(itkInPlaceLabelMapFilterLM4)
itkInPlaceLabelMapFilterLM4___New_orig__ = _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4___New_orig__
itkInPlaceLabelMapFilterLM4_cast = _itkInPlaceLabelMapFilterPython.itkInPlaceLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def in_place_label_map_filter(*args: itkt.ImageLike, **kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for InPlaceLabelMapFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.InPlaceLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def in_place_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.InPlaceLabelMapFilter
    in_place_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    in_place_label_map_filter.__doc__ = filter_object.__doc__




