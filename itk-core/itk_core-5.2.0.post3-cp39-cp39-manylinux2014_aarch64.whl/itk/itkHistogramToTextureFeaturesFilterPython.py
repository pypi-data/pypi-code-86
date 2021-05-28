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
    from . import _itkHistogramToTextureFeaturesFilterPython
else:
    import _itkHistogramToTextureFeaturesFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkHistogramToTextureFeaturesFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkHistogramToTextureFeaturesFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkRGBAPixelPython
import itk.itkFixedArrayPython
import itk.itkRGBPixelPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkArrayPython
import itk.itkCovariantVectorPython
import itk.itkHistogramPython
import itk.itkSamplePython
class itkHistogramToTextureFeaturesFilterEnums(object):
    r"""Proxy of C++ itkHistogramToTextureFeaturesFilterEnums class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    TextureFeature_Energy = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_Energy
    
    TextureFeature_Entropy = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_Entropy
    
    TextureFeature_Correlation = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_Correlation
    
    TextureFeature_InverseDifferenceMoment = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_InverseDifferenceMoment
    
    TextureFeature_Inertia = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_Inertia
    
    TextureFeature_ClusterShade = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_ClusterShade
    
    TextureFeature_ClusterProminence = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_ClusterProminence
    
    TextureFeature_HaralickCorrelation = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_HaralickCorrelation
    
    TextureFeature_InvalidFeatureName = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_InvalidFeatureName
    

    def __init__(self, *args):
        r"""
        __init__(self) -> itkHistogramToTextureFeaturesFilterEnums
        __init__(self, arg0) -> itkHistogramToTextureFeaturesFilterEnums

        Parameters
        ----------
        arg0: itkHistogramToTextureFeaturesFilterEnums const &

        """
        _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_swiginit(self, _itkHistogramToTextureFeaturesFilterPython.new_itkHistogramToTextureFeaturesFilterEnums(*args))
    __swig_destroy__ = _itkHistogramToTextureFeaturesFilterPython.delete_itkHistogramToTextureFeaturesFilterEnums

# Register itkHistogramToTextureFeaturesFilterEnums in _itkHistogramToTextureFeaturesFilterPython:
_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_swigregister(itkHistogramToTextureFeaturesFilterEnums)


def itkHistogramToTextureFeaturesFilterHD_New():
    return itkHistogramToTextureFeaturesFilterHD.New()

class itkHistogramToTextureFeaturesFilterHD(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    This class computes texture feature coefficients from a grey level co-
    occurrence matrix.

    This class computes features that summarize image texture, given a
    grey level co-occurrence matrix (generated by a
    ScalarImageToCooccurrenceMatrixFilter or related class).

    The features calculated are as follows (where $ g(i, j) $ is the
    element in cell i, j of a a normalized GLCM):

    "Energy" $ = f_1 = \\sum_{i,j}g(i, j)^2 $

    "Entropy" $ = f_2 = -\\sum_{i,j}g(i, j) \\log_2 g(i, j)$, or 0
    if $g(i, j) = 0$

    "Correlation" $ = f_3 = \\sum_{i,j}\\frac{(i - \\mu)(j -
    \\mu)g(i, j)}{\\sigma^2} $

    "Difference Moment" $= f_4 = \\sum_{i,j}\\frac{1}{1 + (i -
    j)^2}g(i, j) $

    "Inertia" $ = f_5 = \\sum_{i,j}(i - j)^2g(i, j) $ (sometimes
    called "contrast.")

    "Cluster Shade" $ = f_6 = \\sum_{i,j}((i - \\mu) + (j -
    \\mu))^3 g(i, j) $

    "Cluster Prominence" $ = f_7 = \\sum_{i,j}((i - \\mu) + (j -
    \\mu))^4 g(i, j) $

    "Haralick's Correlation" $ = f_8 = \\frac{\\sum_{i,j}(i, j) g(i,
    j) -\\mu_t^2}{\\sigma_t^2} $ where $\\mu_t$ and $\\sigma_t$
    are the mean and standard deviation of the row (or column, due to
    symmetry) sums.

    Above, $ \\mu = $ (weighted pixel average) $ = \\sum_{i,j}i
    \\cdot g(i, j) = \\sum_{i,j}j \\cdot g(i, j) $ (due to matrix
    symmetry), and

    $ \\sigma = $ (weighted pixel variance) $ = \\sum_{i,j}(i -
    \\mu)^2 \\cdot g(i, j) = \\sum_{i,j}(j - \\mu)^2 \\cdot g(i,
    j) $ (due to matrix symmetry)

    A good texture feature set to use is the Conners, Trivedi and Harlow
    set: features 1, 2, 4, 5, 6, and 7. There is some correlation between
    the various features, so using all of them at the same time is not
    necessarily a good idea.

    NOTA BENE: The input histogram will be forcibly normalized! This
    algorithm takes three passes through the input histogram if the
    histogram was already normalized, and four if not.

    Web references:

    http://www.cssip.uq.edu.au/meastex/www/algs/algs/algs.htmlhttp://www.u
    calgary.ca/~mhallbey/texture/texture_tutorial.html

    Print references:

    Haralick, R.M., K. Shanmugam and I. Dinstein. 1973. Textural Features
    for Image Classification. IEEE Transactions on Systems, Man and
    Cybernetics. SMC-3(6):610-620.

    Haralick, R.M. 1979. Statistical and Structural Approaches to Texture.
    Proceedings of the IEEE, 67:786-804.

    R.W. Conners and C.A. Harlow. A Theoretical Comaprison of Texture
    Algorithms. IEEE Transactions on Pattern Analysis and Machine
    Intelligence, 2:204-222, 1980.

    R.W. Conners, M.M. Trivedi, and C.A. Harlow. Segmentation of a High-
    Resolution Urban Scene using Texture Operators. Computer Vision,
    Graphics and Image Processing, 25:273-310, 1984.

    See:   ScalarImageToCooccurrenceMatrixFilter

    See:   ScalarImageToTextureFeaturesFilter  Author: Zachary Pincus 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInput)
    GetEnergy = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEnergy)
    GetEnergyOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEnergyOutput)
    GetEntropy = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEntropy)
    GetEntropyOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEntropyOutput)
    GetCorrelation = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetCorrelation)
    GetCorrelationOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetCorrelationOutput)
    GetInverseDifferenceMoment = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInverseDifferenceMoment)
    GetInverseDifferenceMomentOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInverseDifferenceMomentOutput)
    GetInertia = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInertia)
    GetInertiaOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInertiaOutput)
    GetClusterShade = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterShade)
    GetClusterShadeOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterShadeOutput)
    GetClusterProminence = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterProminence)
    GetClusterProminenceOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterProminenceOutput)
    GetHaralickCorrelation = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetHaralickCorrelation)
    GetHaralickCorrelationOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetHaralickCorrelationOutput)
    GetFeature = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetFeature)
    __swig_destroy__ = _itkHistogramToTextureFeaturesFilterPython.delete_itkHistogramToTextureFeaturesFilterHD
    cast = _swig_new_static_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramToTextureFeaturesFilterHD

        Create a new object of the class itkHistogramToTextureFeaturesFilterHD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramToTextureFeaturesFilterHD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramToTextureFeaturesFilterHD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramToTextureFeaturesFilterHD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramToTextureFeaturesFilterHD in _itkHistogramToTextureFeaturesFilterPython:
_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_swigregister(itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD___New_orig__ = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD___New_orig__
itkHistogramToTextureFeaturesFilterHD_cast = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_cast


def itkHistogramToTextureFeaturesFilterHF_New():
    return itkHistogramToTextureFeaturesFilterHF.New()

class itkHistogramToTextureFeaturesFilterHF(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    This class computes texture feature coefficients from a grey level co-
    occurrence matrix.

    This class computes features that summarize image texture, given a
    grey level co-occurrence matrix (generated by a
    ScalarImageToCooccurrenceMatrixFilter or related class).

    The features calculated are as follows (where $ g(i, j) $ is the
    element in cell i, j of a a normalized GLCM):

    "Energy" $ = f_1 = \\sum_{i,j}g(i, j)^2 $

    "Entropy" $ = f_2 = -\\sum_{i,j}g(i, j) \\log_2 g(i, j)$, or 0
    if $g(i, j) = 0$

    "Correlation" $ = f_3 = \\sum_{i,j}\\frac{(i - \\mu)(j -
    \\mu)g(i, j)}{\\sigma^2} $

    "Difference Moment" $= f_4 = \\sum_{i,j}\\frac{1}{1 + (i -
    j)^2}g(i, j) $

    "Inertia" $ = f_5 = \\sum_{i,j}(i - j)^2g(i, j) $ (sometimes
    called "contrast.")

    "Cluster Shade" $ = f_6 = \\sum_{i,j}((i - \\mu) + (j -
    \\mu))^3 g(i, j) $

    "Cluster Prominence" $ = f_7 = \\sum_{i,j}((i - \\mu) + (j -
    \\mu))^4 g(i, j) $

    "Haralick's Correlation" $ = f_8 = \\frac{\\sum_{i,j}(i, j) g(i,
    j) -\\mu_t^2}{\\sigma_t^2} $ where $\\mu_t$ and $\\sigma_t$
    are the mean and standard deviation of the row (or column, due to
    symmetry) sums.

    Above, $ \\mu = $ (weighted pixel average) $ = \\sum_{i,j}i
    \\cdot g(i, j) = \\sum_{i,j}j \\cdot g(i, j) $ (due to matrix
    symmetry), and

    $ \\sigma = $ (weighted pixel variance) $ = \\sum_{i,j}(i -
    \\mu)^2 \\cdot g(i, j) = \\sum_{i,j}(j - \\mu)^2 \\cdot g(i,
    j) $ (due to matrix symmetry)

    A good texture feature set to use is the Conners, Trivedi and Harlow
    set: features 1, 2, 4, 5, 6, and 7. There is some correlation between
    the various features, so using all of them at the same time is not
    necessarily a good idea.

    NOTA BENE: The input histogram will be forcibly normalized! This
    algorithm takes three passes through the input histogram if the
    histogram was already normalized, and four if not.

    Web references:

    http://www.cssip.uq.edu.au/meastex/www/algs/algs/algs.htmlhttp://www.u
    calgary.ca/~mhallbey/texture/texture_tutorial.html

    Print references:

    Haralick, R.M., K. Shanmugam and I. Dinstein. 1973. Textural Features
    for Image Classification. IEEE Transactions on Systems, Man and
    Cybernetics. SMC-3(6):610-620.

    Haralick, R.M. 1979. Statistical and Structural Approaches to Texture.
    Proceedings of the IEEE, 67:786-804.

    R.W. Conners and C.A. Harlow. A Theoretical Comaprison of Texture
    Algorithms. IEEE Transactions on Pattern Analysis and Machine
    Intelligence, 2:204-222, 1980.

    R.W. Conners, M.M. Trivedi, and C.A. Harlow. Segmentation of a High-
    Resolution Urban Scene using Texture Operators. Computer Vision,
    Graphics and Image Processing, 25:273-310, 1984.

    See:   ScalarImageToCooccurrenceMatrixFilter

    See:   ScalarImageToTextureFeaturesFilter  Author: Zachary Pincus 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInput)
    GetEnergy = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEnergy)
    GetEnergyOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEnergyOutput)
    GetEntropy = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEntropy)
    GetEntropyOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEntropyOutput)
    GetCorrelation = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetCorrelation)
    GetCorrelationOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetCorrelationOutput)
    GetInverseDifferenceMoment = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInverseDifferenceMoment)
    GetInverseDifferenceMomentOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInverseDifferenceMomentOutput)
    GetInertia = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInertia)
    GetInertiaOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInertiaOutput)
    GetClusterShade = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterShade)
    GetClusterShadeOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterShadeOutput)
    GetClusterProminence = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterProminence)
    GetClusterProminenceOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterProminenceOutput)
    GetHaralickCorrelation = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetHaralickCorrelation)
    GetHaralickCorrelationOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetHaralickCorrelationOutput)
    GetFeature = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetFeature)
    __swig_destroy__ = _itkHistogramToTextureFeaturesFilterPython.delete_itkHistogramToTextureFeaturesFilterHF
    cast = _swig_new_static_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramToTextureFeaturesFilterHF

        Create a new object of the class itkHistogramToTextureFeaturesFilterHF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramToTextureFeaturesFilterHF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramToTextureFeaturesFilterHF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramToTextureFeaturesFilterHF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramToTextureFeaturesFilterHF in _itkHistogramToTextureFeaturesFilterPython:
_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_swigregister(itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF___New_orig__ = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF___New_orig__
itkHistogramToTextureFeaturesFilterHF_cast = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def histogram_to_texture_features_filter(*args, **kwargs):
    """Functional interface for HistogramToTextureFeaturesFilter"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.HistogramToTextureFeaturesFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def histogram_to_texture_features_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKStatistics.HistogramToTextureFeaturesFilter
    histogram_to_texture_features_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    histogram_to_texture_features_filter.__doc__ = filter_object.__doc__




