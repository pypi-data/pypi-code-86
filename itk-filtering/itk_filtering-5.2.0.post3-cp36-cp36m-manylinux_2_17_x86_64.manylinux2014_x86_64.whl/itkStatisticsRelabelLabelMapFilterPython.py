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
    from . import _itkStatisticsRelabelLabelMapFilterPython
else:
    import _itkStatisticsRelabelLabelMapFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkStatisticsRelabelLabelMapFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkStatisticsRelabelLabelMapFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkShapeRelabelLabelMapFilterPython
import itk.itkInPlaceLabelMapFilterPython
import itk.itkLabelMapFilterPython
import itk.itkStatisticsLabelObjectPython
import itk.itkPointPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.vnl_vector_refPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.itkHistogramPython
import itk.itkSamplePython
import itk.itkArrayPython
import itk.itkShapeLabelObjectPython
import itk.itkLabelObjectPython
import itk.itkIndexPython
import itk.itkSizePython
import itk.itkOffsetPython
import itk.itkLabelObjectLinePython
import itk.itkImageRegionPython
import itk.itkAffineTransformPython
import itk.itkMatrixPython
import itk.itkCovariantVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkTransformBasePython
import itk.itkVariableLengthVectorPython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkOptimizerParametersPython
import itk.itkArray2DPython
import itk.itkMatrixOffsetTransformBasePython
import itk.ITKLabelMapBasePython
import itk.itkImageSourceCommonPython
import itk.itkImageSourcePython
import itk.itkVectorImagePython
import itk.itkImagePython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkImageToImageFilterCommonPython

def itkStatisticsRelabelLabelMapFilterLM2_New():
    return itkStatisticsRelabelLabelMapFilterLM2.New()

class itkStatisticsRelabelLabelMapFilterLM2(itk.itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM2):
    r"""


    relabel objects according to their shape attributes

    StatisticsRelabelLabelMapFilter relabel a label collection image
    according to the statistics attributes of the objects. The label
    produced are always consecutives.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   StatisticsLabelObject, RelabelComponentImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2_Clone)
    __swig_destroy__ = _itkStatisticsRelabelLabelMapFilterPython.delete_itkStatisticsRelabelLabelMapFilterLM2
    cast = _swig_new_static_method(_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsRelabelLabelMapFilterLM2

        Create a new object of the class itkStatisticsRelabelLabelMapFilterLM2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsRelabelLabelMapFilterLM2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStatisticsRelabelLabelMapFilterLM2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStatisticsRelabelLabelMapFilterLM2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsRelabelLabelMapFilterLM2 in _itkStatisticsRelabelLabelMapFilterPython:
_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2_swigregister(itkStatisticsRelabelLabelMapFilterLM2)
itkStatisticsRelabelLabelMapFilterLM2___New_orig__ = _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2___New_orig__
itkStatisticsRelabelLabelMapFilterLM2_cast = _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM2_cast


def itkStatisticsRelabelLabelMapFilterLM3_New():
    return itkStatisticsRelabelLabelMapFilterLM3.New()

class itkStatisticsRelabelLabelMapFilterLM3(itk.itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM3):
    r"""


    relabel objects according to their shape attributes

    StatisticsRelabelLabelMapFilter relabel a label collection image
    according to the statistics attributes of the objects. The label
    produced are always consecutives.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   StatisticsLabelObject, RelabelComponentImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3_Clone)
    __swig_destroy__ = _itkStatisticsRelabelLabelMapFilterPython.delete_itkStatisticsRelabelLabelMapFilterLM3
    cast = _swig_new_static_method(_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsRelabelLabelMapFilterLM3

        Create a new object of the class itkStatisticsRelabelLabelMapFilterLM3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsRelabelLabelMapFilterLM3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStatisticsRelabelLabelMapFilterLM3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStatisticsRelabelLabelMapFilterLM3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsRelabelLabelMapFilterLM3 in _itkStatisticsRelabelLabelMapFilterPython:
_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3_swigregister(itkStatisticsRelabelLabelMapFilterLM3)
itkStatisticsRelabelLabelMapFilterLM3___New_orig__ = _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3___New_orig__
itkStatisticsRelabelLabelMapFilterLM3_cast = _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM3_cast


def itkStatisticsRelabelLabelMapFilterLM4_New():
    return itkStatisticsRelabelLabelMapFilterLM4.New()

class itkStatisticsRelabelLabelMapFilterLM4(itk.itkShapeRelabelLabelMapFilterPython.itkShapeRelabelLabelMapFilterLM4):
    r"""


    relabel objects according to their shape attributes

    StatisticsRelabelLabelMapFilter relabel a label collection image
    according to the statistics attributes of the objects. The label
    produced are always consecutives.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/176

    See:   StatisticsLabelObject, RelabelComponentImageFilter 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM4___New_orig__)
    Clone = _swig_new_instance_method(_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM4_Clone)
    __swig_destroy__ = _itkStatisticsRelabelLabelMapFilterPython.delete_itkStatisticsRelabelLabelMapFilterLM4
    cast = _swig_new_static_method(_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM4_cast)

    def New(*args, **kargs):
        """New() -> itkStatisticsRelabelLabelMapFilterLM4

        Create a new object of the class itkStatisticsRelabelLabelMapFilterLM4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkStatisticsRelabelLabelMapFilterLM4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkStatisticsRelabelLabelMapFilterLM4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkStatisticsRelabelLabelMapFilterLM4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkStatisticsRelabelLabelMapFilterLM4 in _itkStatisticsRelabelLabelMapFilterPython:
_itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM4_swigregister(itkStatisticsRelabelLabelMapFilterLM4)
itkStatisticsRelabelLabelMapFilterLM4___New_orig__ = _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM4___New_orig__
itkStatisticsRelabelLabelMapFilterLM4_cast = _itkStatisticsRelabelLabelMapFilterPython.itkStatisticsRelabelLabelMapFilterLM4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def statistics_relabel_label_map_filter(*args: itkt.ImageLike,  reverse_ordering: bool=..., attribute: Union[int, str]=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for StatisticsRelabelLabelMapFilter"""
    import itk

    kwarg_typehints = { 'reverse_ordering':reverse_ordering,'attribute':attribute }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.StatisticsRelabelLabelMapFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def statistics_relabel_label_map_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLabelMap.StatisticsRelabelLabelMapFilter
    statistics_relabel_label_map_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    statistics_relabel_label_map_filter.__doc__ = filter_object.__doc__




