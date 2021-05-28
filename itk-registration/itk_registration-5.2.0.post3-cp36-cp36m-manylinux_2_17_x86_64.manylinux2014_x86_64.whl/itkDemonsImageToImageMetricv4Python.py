# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKMetricsv4Python



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkDemonsImageToImageMetricv4Python
else:
    import _itkDemonsImageToImageMetricv4Python

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkDemonsImageToImageMetricv4Python.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkDemonsImageToImageMetricv4Python.SWIG_PyStaticMethod_New

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
import itk.itkImageToImageMetricv4Python
import itk.itkMatrixPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkCovariantVectorPython
import itk.itkPointPython
import itk.vnl_matrix_fixedPython
import itk.itkSpatialObjectBasePython
import itk.itkBoundingBoxPython
import itk.itkMapContainerPython
import itk.itkVectorContainerPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkContinuousIndexPython
import itk.itkIndexPython
import itk.itkSpatialObjectPropertyPython
import itk.itkRGBAPixelPython
import itk.itkAffineTransformPython
import itk.itkTransformBasePython
import itk.itkVariableLengthVectorPython
import itk.itkArrayPython
import itk.itkDiffusionTensor3DPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkOptimizerParametersPython
import itk.itkArray2DPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkImageRegionPython
import itk.itkDisplacementFieldTransformPython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkInterpolateImageFunctionPython
import itk.itkImageFunctionBasePython
import itk.itkFunctionBasePython
import itk.itkPointSetPython
import itk.itkObjectToObjectMetricBasePython
import itk.itkSingleValuedCostFunctionv4Python
import itk.itkCostFunctionPython
import itk.itkImageToImageFilterBPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.itkImageToImageFilterCommonPython

def itkDemonsImageToImageMetricv4ID2ID2_New():
    return itkDemonsImageToImageMetricv4ID2ID2.New()

class itkDemonsImageToImageMetricv4ID2ID2(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4D2D2):
    r"""


    Class implementing demons metric.

    The implementation is taken from itkDemonsRegistrationFunction.

    The metric derivative can be calculated using image derivatives either
    from the fixed or moving images. The default is to use fixed-image
    gradients. See ObjectToObjectMetric::SetGradientSource to change this
    behavior.

    An intensity threshold is used, below which image pixels are
    considered equal for the purpose of derivative calculation. The
    threshold can be changed by calling SetIntensityDifferenceThreshold.

    This metric supports only moving transforms with local support and
    with a number of local parameters that matches the moving image
    dimension. In particular, it's meant to be used with
    itkDisplacementFieldTransform and derived classes.  See
    DemonsImageToImageMetricv4GetValueAndDerivativeThreader::ProcessPoint
    for algorithm implementation.

    See:  itkImageToImageMetricv4 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID2ID2_Clone)
    GetIntensityDifferenceThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID2ID2_GetIntensityDifferenceThreshold)
    SetIntensityDifferenceThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID2ID2_SetIntensityDifferenceThreshold)
    GetDenominatorThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID2ID2_GetDenominatorThreshold)
    __swig_destroy__ = _itkDemonsImageToImageMetricv4Python.delete_itkDemonsImageToImageMetricv4ID2ID2
    cast = _swig_new_static_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkDemonsImageToImageMetricv4ID2ID2

        Create a new object of the class itkDemonsImageToImageMetricv4ID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDemonsImageToImageMetricv4ID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDemonsImageToImageMetricv4ID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDemonsImageToImageMetricv4ID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDemonsImageToImageMetricv4ID2ID2 in _itkDemonsImageToImageMetricv4Python:
_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID2ID2_swigregister(itkDemonsImageToImageMetricv4ID2ID2)
itkDemonsImageToImageMetricv4ID2ID2___New_orig__ = _itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID2ID2___New_orig__
itkDemonsImageToImageMetricv4ID2ID2_cast = _itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID2ID2_cast


def itkDemonsImageToImageMetricv4ID3ID3_New():
    return itkDemonsImageToImageMetricv4ID3ID3.New()

class itkDemonsImageToImageMetricv4ID3ID3(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4D3D3):
    r"""


    Class implementing demons metric.

    The implementation is taken from itkDemonsRegistrationFunction.

    The metric derivative can be calculated using image derivatives either
    from the fixed or moving images. The default is to use fixed-image
    gradients. See ObjectToObjectMetric::SetGradientSource to change this
    behavior.

    An intensity threshold is used, below which image pixels are
    considered equal for the purpose of derivative calculation. The
    threshold can be changed by calling SetIntensityDifferenceThreshold.

    This metric supports only moving transforms with local support and
    with a number of local parameters that matches the moving image
    dimension. In particular, it's meant to be used with
    itkDisplacementFieldTransform and derived classes.  See
    DemonsImageToImageMetricv4GetValueAndDerivativeThreader::ProcessPoint
    for algorithm implementation.

    See:  itkImageToImageMetricv4 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID3ID3_Clone)
    GetIntensityDifferenceThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID3ID3_GetIntensityDifferenceThreshold)
    SetIntensityDifferenceThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID3ID3_SetIntensityDifferenceThreshold)
    GetDenominatorThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID3ID3_GetDenominatorThreshold)
    __swig_destroy__ = _itkDemonsImageToImageMetricv4Python.delete_itkDemonsImageToImageMetricv4ID3ID3
    cast = _swig_new_static_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkDemonsImageToImageMetricv4ID3ID3

        Create a new object of the class itkDemonsImageToImageMetricv4ID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDemonsImageToImageMetricv4ID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDemonsImageToImageMetricv4ID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDemonsImageToImageMetricv4ID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDemonsImageToImageMetricv4ID3ID3 in _itkDemonsImageToImageMetricv4Python:
_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID3ID3_swigregister(itkDemonsImageToImageMetricv4ID3ID3)
itkDemonsImageToImageMetricv4ID3ID3___New_orig__ = _itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID3ID3___New_orig__
itkDemonsImageToImageMetricv4ID3ID3_cast = _itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID3ID3_cast


def itkDemonsImageToImageMetricv4ID4ID4_New():
    return itkDemonsImageToImageMetricv4ID4ID4.New()

class itkDemonsImageToImageMetricv4ID4ID4(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4D4D4):
    r"""


    Class implementing demons metric.

    The implementation is taken from itkDemonsRegistrationFunction.

    The metric derivative can be calculated using image derivatives either
    from the fixed or moving images. The default is to use fixed-image
    gradients. See ObjectToObjectMetric::SetGradientSource to change this
    behavior.

    An intensity threshold is used, below which image pixels are
    considered equal for the purpose of derivative calculation. The
    threshold can be changed by calling SetIntensityDifferenceThreshold.

    This metric supports only moving transforms with local support and
    with a number of local parameters that matches the moving image
    dimension. In particular, it's meant to be used with
    itkDisplacementFieldTransform and derived classes.  See
    DemonsImageToImageMetricv4GetValueAndDerivativeThreader::ProcessPoint
    for algorithm implementation.

    See:  itkImageToImageMetricv4 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID4ID4_Clone)
    GetIntensityDifferenceThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID4ID4_GetIntensityDifferenceThreshold)
    SetIntensityDifferenceThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID4ID4_SetIntensityDifferenceThreshold)
    GetDenominatorThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID4ID4_GetDenominatorThreshold)
    __swig_destroy__ = _itkDemonsImageToImageMetricv4Python.delete_itkDemonsImageToImageMetricv4ID4ID4
    cast = _swig_new_static_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkDemonsImageToImageMetricv4ID4ID4

        Create a new object of the class itkDemonsImageToImageMetricv4ID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDemonsImageToImageMetricv4ID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDemonsImageToImageMetricv4ID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDemonsImageToImageMetricv4ID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDemonsImageToImageMetricv4ID4ID4 in _itkDemonsImageToImageMetricv4Python:
_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID4ID4_swigregister(itkDemonsImageToImageMetricv4ID4ID4)
itkDemonsImageToImageMetricv4ID4ID4___New_orig__ = _itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID4ID4___New_orig__
itkDemonsImageToImageMetricv4ID4ID4_cast = _itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4ID4ID4_cast


def itkDemonsImageToImageMetricv4IF2IF2_New():
    return itkDemonsImageToImageMetricv4IF2IF2.New()

class itkDemonsImageToImageMetricv4IF2IF2(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4F2F2):
    r"""


    Class implementing demons metric.

    The implementation is taken from itkDemonsRegistrationFunction.

    The metric derivative can be calculated using image derivatives either
    from the fixed or moving images. The default is to use fixed-image
    gradients. See ObjectToObjectMetric::SetGradientSource to change this
    behavior.

    An intensity threshold is used, below which image pixels are
    considered equal for the purpose of derivative calculation. The
    threshold can be changed by calling SetIntensityDifferenceThreshold.

    This metric supports only moving transforms with local support and
    with a number of local parameters that matches the moving image
    dimension. In particular, it's meant to be used with
    itkDisplacementFieldTransform and derived classes.  See
    DemonsImageToImageMetricv4GetValueAndDerivativeThreader::ProcessPoint
    for algorithm implementation.

    See:  itkImageToImageMetricv4 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF2IF2_Clone)
    GetIntensityDifferenceThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF2IF2_GetIntensityDifferenceThreshold)
    SetIntensityDifferenceThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF2IF2_SetIntensityDifferenceThreshold)
    GetDenominatorThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF2IF2_GetDenominatorThreshold)
    __swig_destroy__ = _itkDemonsImageToImageMetricv4Python.delete_itkDemonsImageToImageMetricv4IF2IF2
    cast = _swig_new_static_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkDemonsImageToImageMetricv4IF2IF2

        Create a new object of the class itkDemonsImageToImageMetricv4IF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDemonsImageToImageMetricv4IF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDemonsImageToImageMetricv4IF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDemonsImageToImageMetricv4IF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDemonsImageToImageMetricv4IF2IF2 in _itkDemonsImageToImageMetricv4Python:
_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF2IF2_swigregister(itkDemonsImageToImageMetricv4IF2IF2)
itkDemonsImageToImageMetricv4IF2IF2___New_orig__ = _itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF2IF2___New_orig__
itkDemonsImageToImageMetricv4IF2IF2_cast = _itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF2IF2_cast


def itkDemonsImageToImageMetricv4IF3IF3_New():
    return itkDemonsImageToImageMetricv4IF3IF3.New()

class itkDemonsImageToImageMetricv4IF3IF3(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4F3F3):
    r"""


    Class implementing demons metric.

    The implementation is taken from itkDemonsRegistrationFunction.

    The metric derivative can be calculated using image derivatives either
    from the fixed or moving images. The default is to use fixed-image
    gradients. See ObjectToObjectMetric::SetGradientSource to change this
    behavior.

    An intensity threshold is used, below which image pixels are
    considered equal for the purpose of derivative calculation. The
    threshold can be changed by calling SetIntensityDifferenceThreshold.

    This metric supports only moving transforms with local support and
    with a number of local parameters that matches the moving image
    dimension. In particular, it's meant to be used with
    itkDisplacementFieldTransform and derived classes.  See
    DemonsImageToImageMetricv4GetValueAndDerivativeThreader::ProcessPoint
    for algorithm implementation.

    See:  itkImageToImageMetricv4 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF3IF3_Clone)
    GetIntensityDifferenceThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF3IF3_GetIntensityDifferenceThreshold)
    SetIntensityDifferenceThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF3IF3_SetIntensityDifferenceThreshold)
    GetDenominatorThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF3IF3_GetDenominatorThreshold)
    __swig_destroy__ = _itkDemonsImageToImageMetricv4Python.delete_itkDemonsImageToImageMetricv4IF3IF3
    cast = _swig_new_static_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkDemonsImageToImageMetricv4IF3IF3

        Create a new object of the class itkDemonsImageToImageMetricv4IF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDemonsImageToImageMetricv4IF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDemonsImageToImageMetricv4IF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDemonsImageToImageMetricv4IF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDemonsImageToImageMetricv4IF3IF3 in _itkDemonsImageToImageMetricv4Python:
_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF3IF3_swigregister(itkDemonsImageToImageMetricv4IF3IF3)
itkDemonsImageToImageMetricv4IF3IF3___New_orig__ = _itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF3IF3___New_orig__
itkDemonsImageToImageMetricv4IF3IF3_cast = _itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF3IF3_cast


def itkDemonsImageToImageMetricv4IF4IF4_New():
    return itkDemonsImageToImageMetricv4IF4IF4.New()

class itkDemonsImageToImageMetricv4IF4IF4(itk.itkImageToImageMetricv4Python.itkImageToImageMetricv4F4F4):
    r"""


    Class implementing demons metric.

    The implementation is taken from itkDemonsRegistrationFunction.

    The metric derivative can be calculated using image derivatives either
    from the fixed or moving images. The default is to use fixed-image
    gradients. See ObjectToObjectMetric::SetGradientSource to change this
    behavior.

    An intensity threshold is used, below which image pixels are
    considered equal for the purpose of derivative calculation. The
    threshold can be changed by calling SetIntensityDifferenceThreshold.

    This metric supports only moving transforms with local support and
    with a number of local parameters that matches the moving image
    dimension. In particular, it's meant to be used with
    itkDisplacementFieldTransform and derived classes.  See
    DemonsImageToImageMetricv4GetValueAndDerivativeThreader::ProcessPoint
    for algorithm implementation.

    See:  itkImageToImageMetricv4 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF4IF4_Clone)
    GetIntensityDifferenceThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF4IF4_GetIntensityDifferenceThreshold)
    SetIntensityDifferenceThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF4IF4_SetIntensityDifferenceThreshold)
    GetDenominatorThreshold = _swig_new_instance_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF4IF4_GetDenominatorThreshold)
    __swig_destroy__ = _itkDemonsImageToImageMetricv4Python.delete_itkDemonsImageToImageMetricv4IF4IF4
    cast = _swig_new_static_method(_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkDemonsImageToImageMetricv4IF4IF4

        Create a new object of the class itkDemonsImageToImageMetricv4IF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDemonsImageToImageMetricv4IF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDemonsImageToImageMetricv4IF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDemonsImageToImageMetricv4IF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDemonsImageToImageMetricv4IF4IF4 in _itkDemonsImageToImageMetricv4Python:
_itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF4IF4_swigregister(itkDemonsImageToImageMetricv4IF4IF4)
itkDemonsImageToImageMetricv4IF4IF4___New_orig__ = _itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF4IF4___New_orig__
itkDemonsImageToImageMetricv4IF4IF4_cast = _itkDemonsImageToImageMetricv4Python.itkDemonsImageToImageMetricv4IF4IF4_cast



