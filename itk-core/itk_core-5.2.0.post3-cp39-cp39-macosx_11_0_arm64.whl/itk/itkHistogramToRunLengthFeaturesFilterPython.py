# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKStatisticsPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkHistogramToRunLengthFeaturesFilterPython
else:
    import _itkHistogramToRunLengthFeaturesFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkHistogramToRunLengthFeaturesFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkHistogramToRunLengthFeaturesFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkHistogramPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkSamplePython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkRGBPixelPython
import itk.itkCovariantVectorPython
import itk.itkRGBAPixelPython
class itkHistogramToRunLengthFeaturesFilterEnums(object):
    r"""Proxy of C++ itkHistogramToRunLengthFeaturesFilterEnums class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    RunLengthFeature_ShortRunEmphasis = _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterEnums_RunLengthFeature_ShortRunEmphasis
    
    RunLengthFeature_LongRunEmphasis = _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterEnums_RunLengthFeature_LongRunEmphasis
    
    RunLengthFeature_GreyLevelNonuniformity = _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterEnums_RunLengthFeature_GreyLevelNonuniformity
    
    RunLengthFeature_RunLengthNonuniformity = _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterEnums_RunLengthFeature_RunLengthNonuniformity
    
    RunLengthFeature_LowGreyLevelRunEmphasis = _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterEnums_RunLengthFeature_LowGreyLevelRunEmphasis
    
    RunLengthFeature_HighGreyLevelRunEmphasis = _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterEnums_RunLengthFeature_HighGreyLevelRunEmphasis
    
    RunLengthFeature_ShortRunLowGreyLevelEmphasis = _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterEnums_RunLengthFeature_ShortRunLowGreyLevelEmphasis
    
    RunLengthFeature_ShortRunHighGreyLevelEmphasis = _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterEnums_RunLengthFeature_ShortRunHighGreyLevelEmphasis
    
    RunLengthFeature_LongRunLowGreyLevelEmphasis = _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterEnums_RunLengthFeature_LongRunLowGreyLevelEmphasis
    
    RunLengthFeature_LongRunHighGreyLevelEmphasis = _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterEnums_RunLengthFeature_LongRunHighGreyLevelEmphasis
    

    def __init__(self, *args):
        r"""
        __init__(self) -> itkHistogramToRunLengthFeaturesFilterEnums
        __init__(self, arg0) -> itkHistogramToRunLengthFeaturesFilterEnums

        Parameters
        ----------
        arg0: itkHistogramToRunLengthFeaturesFilterEnums const &

        """
        _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterEnums_swiginit(self, _itkHistogramToRunLengthFeaturesFilterPython.new_itkHistogramToRunLengthFeaturesFilterEnums(*args))
    __swig_destroy__ = _itkHistogramToRunLengthFeaturesFilterPython.delete_itkHistogramToRunLengthFeaturesFilterEnums

# Register itkHistogramToRunLengthFeaturesFilterEnums in _itkHistogramToRunLengthFeaturesFilterPython:
_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterEnums_swigregister(itkHistogramToRunLengthFeaturesFilterEnums)


def itkHistogramToRunLengthFeaturesFilterHD_New():
    return itkHistogramToRunLengthFeaturesFilterHD.New()

class itkHistogramToRunLengthFeaturesFilterHD(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    This class computes texture feature coefficients from a grey level
    run-length matrix.

    By default, run length features are computed for each spatial
    direction and then averaged afterward, so it is possible to access the
    standard deviations of the texture features. These values give a clue
    as to texture anisotropy. However, doing this is much more work,
    because it involved computing one for each offset given. To compute a
    single matrix using the first offset, call FastCalculationsOn(). If
    this is called, then the texture standard deviations will not be
    computed (and will be set to zero), but texture computation will be
    much faster.

    This class is templated over the input histogram type.

    Print references: M. M. Galloway. Texture analysis using gray level
    run lengths. Computer Graphics and Image Processing, 4:172-179, 1975.

    A. Chu, C. M. Sehgal, and J. F. Greenleaf. Use of gray value
    distribution of run lengths for texture analysis. Pattern Recognition
    Letters, 11:415-420, 1990.

    B. R. Dasarathy and E. B. Holder. Image characterizations based on
    joint gray-level run-length distributions. Pattern Recognition
    Letters, 12:490-502, 1991.

    IJ article:https://www.insight-journal.org/browse/publication/231

    See:   ScalarImageToRunLengthFeaturesFilter

    See:   ScalarImageToRunLengthMatrixFilter

    See:   HistogramToRunLengthFeaturesFilter

    : Nick Tustison 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetInput)
    GetShortRunEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetShortRunEmphasis)
    GetShortRunEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetShortRunEmphasisOutput)
    GetLongRunEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetLongRunEmphasis)
    GetLongRunEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetLongRunEmphasisOutput)
    GetGreyLevelNonuniformity = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetGreyLevelNonuniformity)
    GetGreyLevelNonuniformityOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetGreyLevelNonuniformityOutput)
    GetRunLengthNonuniformity = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetRunLengthNonuniformity)
    GetRunLengthNonuniformityOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetRunLengthNonuniformityOutput)
    GetLowGreyLevelRunEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetLowGreyLevelRunEmphasis)
    GetLowGreyLevelRunEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetLowGreyLevelRunEmphasisOutput)
    GetHighGreyLevelRunEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetHighGreyLevelRunEmphasis)
    GetHighGreyLevelRunEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetHighGreyLevelRunEmphasisOutput)
    GetShortRunLowGreyLevelEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetShortRunLowGreyLevelEmphasis)
    GetShortRunLowGreyLevelEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetShortRunLowGreyLevelEmphasisOutput)
    GetShortRunHighGreyLevelEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetShortRunHighGreyLevelEmphasis)
    GetShortRunHighGreyLevelEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetShortRunHighGreyLevelEmphasisOutput)
    GetLongRunLowGreyLevelEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetLongRunLowGreyLevelEmphasis)
    GetLongRunLowGreyLevelEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetLongRunLowGreyLevelEmphasisOutput)
    GetLongRunHighGreyLevelEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetLongRunHighGreyLevelEmphasis)
    GetLongRunHighGreyLevelEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetLongRunHighGreyLevelEmphasisOutput)
    GetTotalNumberOfRuns = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetTotalNumberOfRuns)
    GetFeature = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_GetFeature)
    __swig_destroy__ = _itkHistogramToRunLengthFeaturesFilterPython.delete_itkHistogramToRunLengthFeaturesFilterHD
    cast = _swig_new_static_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramToRunLengthFeaturesFilterHD

        Create a new object of the class itkHistogramToRunLengthFeaturesFilterHD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramToRunLengthFeaturesFilterHD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramToRunLengthFeaturesFilterHD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramToRunLengthFeaturesFilterHD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramToRunLengthFeaturesFilterHD in _itkHistogramToRunLengthFeaturesFilterPython:
_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_swigregister(itkHistogramToRunLengthFeaturesFilterHD)
itkHistogramToRunLengthFeaturesFilterHD___New_orig__ = _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD___New_orig__
itkHistogramToRunLengthFeaturesFilterHD_cast = _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHD_cast


def itkHistogramToRunLengthFeaturesFilterHF_New():
    return itkHistogramToRunLengthFeaturesFilterHF.New()

class itkHistogramToRunLengthFeaturesFilterHF(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    This class computes texture feature coefficients from a grey level
    run-length matrix.

    By default, run length features are computed for each spatial
    direction and then averaged afterward, so it is possible to access the
    standard deviations of the texture features. These values give a clue
    as to texture anisotropy. However, doing this is much more work,
    because it involved computing one for each offset given. To compute a
    single matrix using the first offset, call FastCalculationsOn(). If
    this is called, then the texture standard deviations will not be
    computed (and will be set to zero), but texture computation will be
    much faster.

    This class is templated over the input histogram type.

    Print references: M. M. Galloway. Texture analysis using gray level
    run lengths. Computer Graphics and Image Processing, 4:172-179, 1975.

    A. Chu, C. M. Sehgal, and J. F. Greenleaf. Use of gray value
    distribution of run lengths for texture analysis. Pattern Recognition
    Letters, 11:415-420, 1990.

    B. R. Dasarathy and E. B. Holder. Image characterizations based on
    joint gray-level run-length distributions. Pattern Recognition
    Letters, 12:490-502, 1991.

    IJ article:https://www.insight-journal.org/browse/publication/231

    See:   ScalarImageToRunLengthFeaturesFilter

    See:   ScalarImageToRunLengthMatrixFilter

    See:   HistogramToRunLengthFeaturesFilter

    : Nick Tustison 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetInput)
    GetShortRunEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetShortRunEmphasis)
    GetShortRunEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetShortRunEmphasisOutput)
    GetLongRunEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetLongRunEmphasis)
    GetLongRunEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetLongRunEmphasisOutput)
    GetGreyLevelNonuniformity = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetGreyLevelNonuniformity)
    GetGreyLevelNonuniformityOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetGreyLevelNonuniformityOutput)
    GetRunLengthNonuniformity = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetRunLengthNonuniformity)
    GetRunLengthNonuniformityOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetRunLengthNonuniformityOutput)
    GetLowGreyLevelRunEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetLowGreyLevelRunEmphasis)
    GetLowGreyLevelRunEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetLowGreyLevelRunEmphasisOutput)
    GetHighGreyLevelRunEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetHighGreyLevelRunEmphasis)
    GetHighGreyLevelRunEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetHighGreyLevelRunEmphasisOutput)
    GetShortRunLowGreyLevelEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetShortRunLowGreyLevelEmphasis)
    GetShortRunLowGreyLevelEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetShortRunLowGreyLevelEmphasisOutput)
    GetShortRunHighGreyLevelEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetShortRunHighGreyLevelEmphasis)
    GetShortRunHighGreyLevelEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetShortRunHighGreyLevelEmphasisOutput)
    GetLongRunLowGreyLevelEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetLongRunLowGreyLevelEmphasis)
    GetLongRunLowGreyLevelEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetLongRunLowGreyLevelEmphasisOutput)
    GetLongRunHighGreyLevelEmphasis = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetLongRunHighGreyLevelEmphasis)
    GetLongRunHighGreyLevelEmphasisOutput = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetLongRunHighGreyLevelEmphasisOutput)
    GetTotalNumberOfRuns = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetTotalNumberOfRuns)
    GetFeature = _swig_new_instance_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_GetFeature)
    __swig_destroy__ = _itkHistogramToRunLengthFeaturesFilterPython.delete_itkHistogramToRunLengthFeaturesFilterHF
    cast = _swig_new_static_method(_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramToRunLengthFeaturesFilterHF

        Create a new object of the class itkHistogramToRunLengthFeaturesFilterHF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramToRunLengthFeaturesFilterHF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramToRunLengthFeaturesFilterHF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramToRunLengthFeaturesFilterHF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramToRunLengthFeaturesFilterHF in _itkHistogramToRunLengthFeaturesFilterPython:
_itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_swigregister(itkHistogramToRunLengthFeaturesFilterHF)
itkHistogramToRunLengthFeaturesFilterHF___New_orig__ = _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF___New_orig__
itkHistogramToRunLengthFeaturesFilterHF_cast = _itkHistogramToRunLengthFeaturesFilterPython.itkHistogramToRunLengthFeaturesFilterHF_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def histogram_to_run_length_features_filter(*args, **kwargs):
    """Functional interface for HistogramToRunLengthFeaturesFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.HistogramToRunLengthFeaturesFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def histogram_to_run_length_features_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKStatistics.HistogramToRunLengthFeaturesFilter
    histogram_to_run_length_features_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    histogram_to_run_length_features_filter.__doc__ = filter_object.__doc__




