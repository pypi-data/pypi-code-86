# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKThresholdingPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkHistogramThresholdCalculatorPython
else:
    import _itkHistogramThresholdCalculatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkHistogramThresholdCalculatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkHistogramThresholdCalculatorPython.SWIG_PyStaticMethod_New

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
import itk.itkHistogramPython
import itk.itkSamplePython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkArrayPython
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkCovariantVectorPython

def itkHistogramThresholdCalculatorHDD_New():
    return itkHistogramThresholdCalculatorHDD.New()

class itkHistogramThresholdCalculatorHDD(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Base class to compute a threshold value based on the histogram of an
    image.

    Richard Beare. Department of Medicine, Monash University, Melbourne,
    Australia.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/811 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD_GetInput)
    GetOutput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD_GetOutput)
    GetThreshold = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD_GetThreshold)
    __swig_destroy__ = _itkHistogramThresholdCalculatorPython.delete_itkHistogramThresholdCalculatorHDD
    cast = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramThresholdCalculatorHDD

        Create a new object of the class itkHistogramThresholdCalculatorHDD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramThresholdCalculatorHDD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramThresholdCalculatorHDD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramThresholdCalculatorHDD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramThresholdCalculatorHDD in _itkHistogramThresholdCalculatorPython:
_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD_swigregister(itkHistogramThresholdCalculatorHDD)
itkHistogramThresholdCalculatorHDD___New_orig__ = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD___New_orig__
itkHistogramThresholdCalculatorHDD_cast = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD_cast


def itkHistogramThresholdCalculatorHDF_New():
    return itkHistogramThresholdCalculatorHDF.New()

class itkHistogramThresholdCalculatorHDF(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Base class to compute a threshold value based on the histogram of an
    image.

    Richard Beare. Department of Medicine, Monash University, Melbourne,
    Australia.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/811 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF_GetInput)
    GetOutput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF_GetOutput)
    GetThreshold = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF_GetThreshold)
    __swig_destroy__ = _itkHistogramThresholdCalculatorPython.delete_itkHistogramThresholdCalculatorHDF
    cast = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramThresholdCalculatorHDF

        Create a new object of the class itkHistogramThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramThresholdCalculatorHDF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramThresholdCalculatorHDF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramThresholdCalculatorHDF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramThresholdCalculatorHDF in _itkHistogramThresholdCalculatorPython:
_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF_swigregister(itkHistogramThresholdCalculatorHDF)
itkHistogramThresholdCalculatorHDF___New_orig__ = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF___New_orig__
itkHistogramThresholdCalculatorHDF_cast = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF_cast


def itkHistogramThresholdCalculatorHDSS_New():
    return itkHistogramThresholdCalculatorHDSS.New()

class itkHistogramThresholdCalculatorHDSS(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Base class to compute a threshold value based on the histogram of an
    image.

    Richard Beare. Department of Medicine, Monash University, Melbourne,
    Australia.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/811 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS_GetInput)
    GetOutput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS_GetOutput)
    GetThreshold = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS_GetThreshold)
    __swig_destroy__ = _itkHistogramThresholdCalculatorPython.delete_itkHistogramThresholdCalculatorHDSS
    cast = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramThresholdCalculatorHDSS

        Create a new object of the class itkHistogramThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramThresholdCalculatorHDSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramThresholdCalculatorHDSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramThresholdCalculatorHDSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramThresholdCalculatorHDSS in _itkHistogramThresholdCalculatorPython:
_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS_swigregister(itkHistogramThresholdCalculatorHDSS)
itkHistogramThresholdCalculatorHDSS___New_orig__ = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS___New_orig__
itkHistogramThresholdCalculatorHDSS_cast = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS_cast


def itkHistogramThresholdCalculatorHDUC_New():
    return itkHistogramThresholdCalculatorHDUC.New()

class itkHistogramThresholdCalculatorHDUC(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Base class to compute a threshold value based on the histogram of an
    image.

    Richard Beare. Department of Medicine, Monash University, Melbourne,
    Australia.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/811 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC_GetInput)
    GetOutput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC_GetOutput)
    GetThreshold = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC_GetThreshold)
    __swig_destroy__ = _itkHistogramThresholdCalculatorPython.delete_itkHistogramThresholdCalculatorHDUC
    cast = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramThresholdCalculatorHDUC

        Create a new object of the class itkHistogramThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramThresholdCalculatorHDUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramThresholdCalculatorHDUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramThresholdCalculatorHDUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramThresholdCalculatorHDUC in _itkHistogramThresholdCalculatorPython:
_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC_swigregister(itkHistogramThresholdCalculatorHDUC)
itkHistogramThresholdCalculatorHDUC___New_orig__ = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC___New_orig__
itkHistogramThresholdCalculatorHDUC_cast = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC_cast


def itkHistogramThresholdCalculatorHDUS_New():
    return itkHistogramThresholdCalculatorHDUS.New()

class itkHistogramThresholdCalculatorHDUS(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Base class to compute a threshold value based on the histogram of an
    image.

    Richard Beare. Department of Medicine, Monash University, Melbourne,
    Australia.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/811 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS_GetInput)
    GetOutput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS_GetOutput)
    GetThreshold = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS_GetThreshold)
    __swig_destroy__ = _itkHistogramThresholdCalculatorPython.delete_itkHistogramThresholdCalculatorHDUS
    cast = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramThresholdCalculatorHDUS

        Create a new object of the class itkHistogramThresholdCalculatorHDUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramThresholdCalculatorHDUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramThresholdCalculatorHDUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramThresholdCalculatorHDUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramThresholdCalculatorHDUS in _itkHistogramThresholdCalculatorPython:
_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS_swigregister(itkHistogramThresholdCalculatorHDUS)
itkHistogramThresholdCalculatorHDUS___New_orig__ = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS___New_orig__
itkHistogramThresholdCalculatorHDUS_cast = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS_cast


def itkHistogramThresholdCalculatorHFD_New():
    return itkHistogramThresholdCalculatorHFD.New()

class itkHistogramThresholdCalculatorHFD(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Base class to compute a threshold value based on the histogram of an
    image.

    Richard Beare. Department of Medicine, Monash University, Melbourne,
    Australia.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/811 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD_GetInput)
    GetOutput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD_GetOutput)
    GetThreshold = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD_GetThreshold)
    __swig_destroy__ = _itkHistogramThresholdCalculatorPython.delete_itkHistogramThresholdCalculatorHFD
    cast = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramThresholdCalculatorHFD

        Create a new object of the class itkHistogramThresholdCalculatorHFD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramThresholdCalculatorHFD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramThresholdCalculatorHFD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramThresholdCalculatorHFD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramThresholdCalculatorHFD in _itkHistogramThresholdCalculatorPython:
_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD_swigregister(itkHistogramThresholdCalculatorHFD)
itkHistogramThresholdCalculatorHFD___New_orig__ = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD___New_orig__
itkHistogramThresholdCalculatorHFD_cast = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD_cast


def itkHistogramThresholdCalculatorHFF_New():
    return itkHistogramThresholdCalculatorHFF.New()

class itkHistogramThresholdCalculatorHFF(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Base class to compute a threshold value based on the histogram of an
    image.

    Richard Beare. Department of Medicine, Monash University, Melbourne,
    Australia.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/811 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF_GetInput)
    GetOutput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF_GetOutput)
    GetThreshold = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF_GetThreshold)
    __swig_destroy__ = _itkHistogramThresholdCalculatorPython.delete_itkHistogramThresholdCalculatorHFF
    cast = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramThresholdCalculatorHFF

        Create a new object of the class itkHistogramThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramThresholdCalculatorHFF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramThresholdCalculatorHFF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramThresholdCalculatorHFF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramThresholdCalculatorHFF in _itkHistogramThresholdCalculatorPython:
_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF_swigregister(itkHistogramThresholdCalculatorHFF)
itkHistogramThresholdCalculatorHFF___New_orig__ = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF___New_orig__
itkHistogramThresholdCalculatorHFF_cast = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF_cast


def itkHistogramThresholdCalculatorHFSS_New():
    return itkHistogramThresholdCalculatorHFSS.New()

class itkHistogramThresholdCalculatorHFSS(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Base class to compute a threshold value based on the histogram of an
    image.

    Richard Beare. Department of Medicine, Monash University, Melbourne,
    Australia.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/811 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS_GetInput)
    GetOutput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS_GetOutput)
    GetThreshold = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS_GetThreshold)
    __swig_destroy__ = _itkHistogramThresholdCalculatorPython.delete_itkHistogramThresholdCalculatorHFSS
    cast = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramThresholdCalculatorHFSS

        Create a new object of the class itkHistogramThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramThresholdCalculatorHFSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramThresholdCalculatorHFSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramThresholdCalculatorHFSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramThresholdCalculatorHFSS in _itkHistogramThresholdCalculatorPython:
_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS_swigregister(itkHistogramThresholdCalculatorHFSS)
itkHistogramThresholdCalculatorHFSS___New_orig__ = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS___New_orig__
itkHistogramThresholdCalculatorHFSS_cast = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS_cast


def itkHistogramThresholdCalculatorHFUC_New():
    return itkHistogramThresholdCalculatorHFUC.New()

class itkHistogramThresholdCalculatorHFUC(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Base class to compute a threshold value based on the histogram of an
    image.

    Richard Beare. Department of Medicine, Monash University, Melbourne,
    Australia.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/811 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC_GetInput)
    GetOutput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC_GetOutput)
    GetThreshold = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC_GetThreshold)
    __swig_destroy__ = _itkHistogramThresholdCalculatorPython.delete_itkHistogramThresholdCalculatorHFUC
    cast = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramThresholdCalculatorHFUC

        Create a new object of the class itkHistogramThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramThresholdCalculatorHFUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramThresholdCalculatorHFUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramThresholdCalculatorHFUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramThresholdCalculatorHFUC in _itkHistogramThresholdCalculatorPython:
_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC_swigregister(itkHistogramThresholdCalculatorHFUC)
itkHistogramThresholdCalculatorHFUC___New_orig__ = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC___New_orig__
itkHistogramThresholdCalculatorHFUC_cast = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC_cast


def itkHistogramThresholdCalculatorHFUS_New():
    return itkHistogramThresholdCalculatorHFUS.New()

class itkHistogramThresholdCalculatorHFUS(itk.ITKCommonBasePython.itkProcessObject):
    r"""


    Base class to compute a threshold value based on the histogram of an
    image.

    Richard Beare. Department of Medicine, Monash University, Melbourne,
    Australia.

    Gaetan Lehmann. Biologie du Developpement et de la Reproduction, INRA
    de Jouy-en-Josas, France.  This implementation was taken from the
    Insight Journal paper:https://www.insight-
    journal.org/browse/publication/811 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS_GetInput)
    GetOutput = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS_GetOutput)
    GetThreshold = _swig_new_instance_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS_GetThreshold)
    __swig_destroy__ = _itkHistogramThresholdCalculatorPython.delete_itkHistogramThresholdCalculatorHFUS
    cast = _swig_new_static_method(_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramThresholdCalculatorHFUS

        Create a new object of the class itkHistogramThresholdCalculatorHFUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramThresholdCalculatorHFUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHistogramThresholdCalculatorHFUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHistogramThresholdCalculatorHFUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramThresholdCalculatorHFUS in _itkHistogramThresholdCalculatorPython:
_itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS_swigregister(itkHistogramThresholdCalculatorHFUS)
itkHistogramThresholdCalculatorHFUS___New_orig__ = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS___New_orig__
itkHistogramThresholdCalculatorHFUS_cast = _itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def histogram_threshold_calculator(*args, **kwargs):
    """Functional interface for HistogramThresholdCalculator"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.HistogramThresholdCalculator.New(*args, **kwargs)
    return instance.__internal_call__()

def histogram_threshold_calculator_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKThresholding.HistogramThresholdCalculator
    histogram_threshold_calculator.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    histogram_threshold_calculator.__doc__ = filter_object.__doc__




