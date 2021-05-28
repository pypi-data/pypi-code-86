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
    from . import _itkHistogramPython
else:
    import _itkHistogramPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkHistogramPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkHistogramPython.SWIG_PyStaticMethod_New

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
import itk.itkSamplePython
import itk.itkFixedArrayPython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.vnl_matrixPython
import itk.itkVectorPython
import itk.vnl_vector_refPython

def itkHistogramD_New():
    return itkHistogramD.New()

class itkHistogramD(itk.itkSamplePython.itkSampleAD):
    r"""


    This class stores measurement vectors in the context of n-dimensional
    histogram.

    Histogram represents an ND histogram. Histogram bins can be regularly
    or irregularly spaced. The storage for the histogram is managed via
    the FrequencyContainer specified by the template argument. The default
    frequency container is a DenseFrequencyContainer. A
    SparseFrequencyContainer can be used as an alternative.

    Frequencies of a bin ( SetFrequency(), IncreaseFrequency()) can be
    specified by measurement, index, or instance identifier.

    Measurements can be queried by bin index or instance identifier. In
    this case, the measurement returned is the centroid of the histogram
    bin.

    The Initialize() method is used to specify the number of bins for each
    dimension of the histogram. An overloaded version also allows for
    regularly spaced bins to defined. To define irregularly sized bins,
    use the SetBinMin()/SetBinMax() methods.

    If you do not know the length of the measurement vector at compile
    time, you should use the VariableDimensionHistogram class, instead of
    the Histogram class.

    If you know the length of the measurement vector at compile time, it
    can conveniently be obtained from MeasurementVectorTraits. For
    instance, instantiate a histogram as below:

    See:   Sample, DenseFrequencyContainer, SparseFrequencyContainer,
    VariableDimensionHistogram 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramPython.itkHistogramD___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_Clone)
    Initialize = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_Initialize)
    SetToZero = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_SetToZero)
    GetIndex = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetIndex)
    GetClipBinsAtEnds = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetClipBinsAtEnds)
    SetClipBinsAtEnds = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_SetClipBinsAtEnds)
    IsIndexOutOfBounds = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_IsIndexOutOfBounds)
    GetInstanceIdentifier = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetInstanceIdentifier)
    GetSize = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetSize)
    GetBinMin = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetBinMin)
    GetBinMax = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetBinMax)
    SetBinMin = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_SetBinMin)
    SetBinMax = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_SetBinMax)
    GetBinMinFromValue = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetBinMinFromValue)
    GetBinMaxFromValue = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetBinMaxFromValue)
    GetDimensionMins = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetDimensionMins)
    GetDimensionMaxs = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetDimensionMaxs)
    GetMins = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetMins)
    GetMaxs = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetMaxs)
    GetHistogramMinFromIndex = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetHistogramMinFromIndex)
    GetHistogramMaxFromIndex = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetHistogramMaxFromIndex)
    SetFrequency = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_SetFrequency)
    SetFrequencyOfIndex = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_SetFrequencyOfIndex)
    SetFrequencyOfMeasurement = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_SetFrequencyOfMeasurement)
    IncreaseFrequency = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_IncreaseFrequency)
    IncreaseFrequencyOfIndex = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_IncreaseFrequencyOfIndex)
    IncreaseFrequencyOfMeasurement = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_IncreaseFrequencyOfMeasurement)
    GetMeasurementVector = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetMeasurementVector)
    GetMeasurement = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetMeasurement)
    GetFrequency = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_GetFrequency)
    Quantile = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_Quantile)
    Mean = _swig_new_instance_method(_itkHistogramPython.itkHistogramD_Mean)
    __swig_destroy__ = _itkHistogramPython.delete_itkHistogramD
    cast = _swig_new_static_method(_itkHistogramPython.itkHistogramD_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramD

        Create a new object of the class itkHistogramD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramD in _itkHistogramPython:
_itkHistogramPython.itkHistogramD_swigregister(itkHistogramD)
itkHistogramD___New_orig__ = _itkHistogramPython.itkHistogramD___New_orig__
itkHistogramD_cast = _itkHistogramPython.itkHistogramD_cast


def itkHistogramF_New():
    return itkHistogramF.New()

class itkHistogramF(itk.itkSamplePython.itkSampleAF):
    r"""


    This class stores measurement vectors in the context of n-dimensional
    histogram.

    Histogram represents an ND histogram. Histogram bins can be regularly
    or irregularly spaced. The storage for the histogram is managed via
    the FrequencyContainer specified by the template argument. The default
    frequency container is a DenseFrequencyContainer. A
    SparseFrequencyContainer can be used as an alternative.

    Frequencies of a bin ( SetFrequency(), IncreaseFrequency()) can be
    specified by measurement, index, or instance identifier.

    Measurements can be queried by bin index or instance identifier. In
    this case, the measurement returned is the centroid of the histogram
    bin.

    The Initialize() method is used to specify the number of bins for each
    dimension of the histogram. An overloaded version also allows for
    regularly spaced bins to defined. To define irregularly sized bins,
    use the SetBinMin()/SetBinMax() methods.

    If you do not know the length of the measurement vector at compile
    time, you should use the VariableDimensionHistogram class, instead of
    the Histogram class.

    If you know the length of the measurement vector at compile time, it
    can conveniently be obtained from MeasurementVectorTraits. For
    instance, instantiate a histogram as below:

    See:   Sample, DenseFrequencyContainer, SparseFrequencyContainer,
    VariableDimensionHistogram 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramPython.itkHistogramF___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_Clone)
    Initialize = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_Initialize)
    SetToZero = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_SetToZero)
    GetIndex = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetIndex)
    GetClipBinsAtEnds = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetClipBinsAtEnds)
    SetClipBinsAtEnds = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_SetClipBinsAtEnds)
    IsIndexOutOfBounds = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_IsIndexOutOfBounds)
    GetInstanceIdentifier = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetInstanceIdentifier)
    GetSize = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetSize)
    GetBinMin = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetBinMin)
    GetBinMax = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetBinMax)
    SetBinMin = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_SetBinMin)
    SetBinMax = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_SetBinMax)
    GetBinMinFromValue = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetBinMinFromValue)
    GetBinMaxFromValue = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetBinMaxFromValue)
    GetDimensionMins = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetDimensionMins)
    GetDimensionMaxs = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetDimensionMaxs)
    GetMins = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetMins)
    GetMaxs = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetMaxs)
    GetHistogramMinFromIndex = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetHistogramMinFromIndex)
    GetHistogramMaxFromIndex = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetHistogramMaxFromIndex)
    SetFrequency = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_SetFrequency)
    SetFrequencyOfIndex = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_SetFrequencyOfIndex)
    SetFrequencyOfMeasurement = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_SetFrequencyOfMeasurement)
    IncreaseFrequency = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_IncreaseFrequency)
    IncreaseFrequencyOfIndex = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_IncreaseFrequencyOfIndex)
    IncreaseFrequencyOfMeasurement = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_IncreaseFrequencyOfMeasurement)
    GetMeasurementVector = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetMeasurementVector)
    GetMeasurement = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetMeasurement)
    GetFrequency = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_GetFrequency)
    Quantile = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_Quantile)
    Mean = _swig_new_instance_method(_itkHistogramPython.itkHistogramF_Mean)
    __swig_destroy__ = _itkHistogramPython.delete_itkHistogramF
    cast = _swig_new_static_method(_itkHistogramPython.itkHistogramF_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramF

        Create a new object of the class itkHistogramF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramF in _itkHistogramPython:
_itkHistogramPython.itkHistogramF_swigregister(itkHistogramF)
itkHistogramF___New_orig__ = _itkHistogramPython.itkHistogramF___New_orig__
itkHistogramF_cast = _itkHistogramPython.itkHistogramF_cast


def itkSimpleDataObjectDecoratorHD_New():
    return itkSimpleDataObjectDecoratorHD.New()

class itkSimpleDataObjectDecoratorHD(itk.ITKCommonBasePython.itkDataObject):
    r"""


    Decorates any "simple" data type (data types without smart pointers)
    with a DataObject API.

    SimpleDataObjectDecorator decorates an object with a DataObject API.
    This allows simple objects to be encapsulated into objects that can be
    passed as down the pipeline. This decorator is intended to be used on
    native types (float, int, etc.) or any objects not derived from
    itkObject. To decorate a subclass of itkObject, see
    DataObjectDecorator.

    The decorator provides two methods Set() and Get() to access the
    decorated object (referred internally as the component).

    Note that when an instance of SimpleDataObjectDecorator is created,
    the component is initialized with its default constructor.

    SimpleDataObjectDecorator can decorate any simple data type. Two other
    decorators are provided for decorating pointers. DataObjectDecorator
    will decorate pointers to subclasses of itkObject (internally storing
    the pointer in a SmartPointer). AutoPointerDataObjectDecorator will
    decorate any other pointer and manage the memory deallocating of the
    component.

    See:  DataObjectDecorator

    See:  AutoPointerDataObjectDecorator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramPython.itkSimpleDataObjectDecoratorHD___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramPython.itkSimpleDataObjectDecoratorHD_Clone)
    Set = _swig_new_instance_method(_itkHistogramPython.itkSimpleDataObjectDecoratorHD_Set)
    Get = _swig_new_instance_method(_itkHistogramPython.itkSimpleDataObjectDecoratorHD_Get)
    __swig_destroy__ = _itkHistogramPython.delete_itkSimpleDataObjectDecoratorHD
    cast = _swig_new_static_method(_itkHistogramPython.itkSimpleDataObjectDecoratorHD_cast)

    def New(*args, **kargs):
        """New() -> itkSimpleDataObjectDecoratorHD

        Create a new object of the class itkSimpleDataObjectDecoratorHD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimpleDataObjectDecoratorHD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSimpleDataObjectDecoratorHD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSimpleDataObjectDecoratorHD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSimpleDataObjectDecoratorHD in _itkHistogramPython:
_itkHistogramPython.itkSimpleDataObjectDecoratorHD_swigregister(itkSimpleDataObjectDecoratorHD)
itkSimpleDataObjectDecoratorHD___New_orig__ = _itkHistogramPython.itkSimpleDataObjectDecoratorHD___New_orig__
itkSimpleDataObjectDecoratorHD_cast = _itkHistogramPython.itkSimpleDataObjectDecoratorHD_cast


def itkSimpleDataObjectDecoratorHF_New():
    return itkSimpleDataObjectDecoratorHF.New()

class itkSimpleDataObjectDecoratorHF(itk.ITKCommonBasePython.itkDataObject):
    r"""


    Decorates any "simple" data type (data types without smart pointers)
    with a DataObject API.

    SimpleDataObjectDecorator decorates an object with a DataObject API.
    This allows simple objects to be encapsulated into objects that can be
    passed as down the pipeline. This decorator is intended to be used on
    native types (float, int, etc.) or any objects not derived from
    itkObject. To decorate a subclass of itkObject, see
    DataObjectDecorator.

    The decorator provides two methods Set() and Get() to access the
    decorated object (referred internally as the component).

    Note that when an instance of SimpleDataObjectDecorator is created,
    the component is initialized with its default constructor.

    SimpleDataObjectDecorator can decorate any simple data type. Two other
    decorators are provided for decorating pointers. DataObjectDecorator
    will decorate pointers to subclasses of itkObject (internally storing
    the pointer in a SmartPointer). AutoPointerDataObjectDecorator will
    decorate any other pointer and manage the memory deallocating of the
    component.

    See:  DataObjectDecorator

    See:  AutoPointerDataObjectDecorator 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramPython.itkSimpleDataObjectDecoratorHF___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramPython.itkSimpleDataObjectDecoratorHF_Clone)
    Set = _swig_new_instance_method(_itkHistogramPython.itkSimpleDataObjectDecoratorHF_Set)
    Get = _swig_new_instance_method(_itkHistogramPython.itkSimpleDataObjectDecoratorHF_Get)
    __swig_destroy__ = _itkHistogramPython.delete_itkSimpleDataObjectDecoratorHF
    cast = _swig_new_static_method(_itkHistogramPython.itkSimpleDataObjectDecoratorHF_cast)

    def New(*args, **kargs):
        """New() -> itkSimpleDataObjectDecoratorHF

        Create a new object of the class itkSimpleDataObjectDecoratorHF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimpleDataObjectDecoratorHF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkSimpleDataObjectDecoratorHF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkSimpleDataObjectDecoratorHF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSimpleDataObjectDecoratorHF in _itkHistogramPython:
_itkHistogramPython.itkSimpleDataObjectDecoratorHF_swigregister(itkSimpleDataObjectDecoratorHF)
itkSimpleDataObjectDecoratorHF___New_orig__ = _itkHistogramPython.itkSimpleDataObjectDecoratorHF___New_orig__
itkSimpleDataObjectDecoratorHF_cast = _itkHistogramPython.itkSimpleDataObjectDecoratorHF_cast



