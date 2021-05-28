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
    from . import _itkMomentsThresholdCalculatorPython
else:
    import _itkMomentsThresholdCalculatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMomentsThresholdCalculatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMomentsThresholdCalculatorPython.SWIG_PyStaticMethod_New

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
import itk.itkHistogramThresholdCalculatorPython
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkRGBAPixelPython
import itk.itkFixedArrayPython
import itk.pyBasePython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkArrayPython
import itk.itkCovariantVectorPython
import itk.ITKCommonBasePython
import itk.itkRGBPixelPython
import itk.itkHistogramPython
import itk.itkSamplePython

def itkMomentsThresholdCalculatorHDD_New():
    return itkMomentsThresholdCalculatorHDD.New()

class itkMomentsThresholdCalculatorHDD(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD):
    r"""


    Computes the Moments's threshold for an image.

    W. Tsai, "Moment-preserving thresholding: a new approach," Computer
    Vision, Graphics, and Image Processing, vol. 29, pp. 377-393, 1985.

    This class is templated over the input histogram type. WARNING:  This
    calculator assumes that the input histogram has only one dimension.

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
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDD___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDD_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHDD
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDD_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHDD

        Create a new object of the class itkMomentsThresholdCalculatorHDD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHDD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHDD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMomentsThresholdCalculatorHDD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHDD in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDD_swigregister(itkMomentsThresholdCalculatorHDD)
itkMomentsThresholdCalculatorHDD___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDD___New_orig__
itkMomentsThresholdCalculatorHDD_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDD_cast


def itkMomentsThresholdCalculatorHDF_New():
    return itkMomentsThresholdCalculatorHDF.New()

class itkMomentsThresholdCalculatorHDF(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    r"""


    Computes the Moments's threshold for an image.

    W. Tsai, "Moment-preserving thresholding: a new approach," Computer
    Vision, Graphics, and Image Processing, vol. 29, pp. 377-393, 1985.

    This class is templated over the input histogram type. WARNING:  This
    calculator assumes that the input histogram has only one dimension.

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
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHDF
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHDF

        Create a new object of the class itkMomentsThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHDF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHDF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMomentsThresholdCalculatorHDF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHDF in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_swigregister(itkMomentsThresholdCalculatorHDF)
itkMomentsThresholdCalculatorHDF___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF___New_orig__
itkMomentsThresholdCalculatorHDF_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDF_cast


def itkMomentsThresholdCalculatorHDSS_New():
    return itkMomentsThresholdCalculatorHDSS.New()

class itkMomentsThresholdCalculatorHDSS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    r"""


    Computes the Moments's threshold for an image.

    W. Tsai, "Moment-preserving thresholding: a new approach," Computer
    Vision, Graphics, and Image Processing, vol. 29, pp. 377-393, 1985.

    This class is templated over the input histogram type. WARNING:  This
    calculator assumes that the input histogram has only one dimension.

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
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHDSS
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHDSS

        Create a new object of the class itkMomentsThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHDSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHDSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMomentsThresholdCalculatorHDSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHDSS in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_swigregister(itkMomentsThresholdCalculatorHDSS)
itkMomentsThresholdCalculatorHDSS___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS___New_orig__
itkMomentsThresholdCalculatorHDSS_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDSS_cast


def itkMomentsThresholdCalculatorHDUC_New():
    return itkMomentsThresholdCalculatorHDUC.New()

class itkMomentsThresholdCalculatorHDUC(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    r"""


    Computes the Moments's threshold for an image.

    W. Tsai, "Moment-preserving thresholding: a new approach," Computer
    Vision, Graphics, and Image Processing, vol. 29, pp. 377-393, 1985.

    This class is templated over the input histogram type. WARNING:  This
    calculator assumes that the input histogram has only one dimension.

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
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHDUC
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHDUC

        Create a new object of the class itkMomentsThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHDUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHDUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMomentsThresholdCalculatorHDUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHDUC in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_swigregister(itkMomentsThresholdCalculatorHDUC)
itkMomentsThresholdCalculatorHDUC___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC___New_orig__
itkMomentsThresholdCalculatorHDUC_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUC_cast


def itkMomentsThresholdCalculatorHDUS_New():
    return itkMomentsThresholdCalculatorHDUS.New()

class itkMomentsThresholdCalculatorHDUS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS):
    r"""


    Computes the Moments's threshold for an image.

    W. Tsai, "Moment-preserving thresholding: a new approach," Computer
    Vision, Graphics, and Image Processing, vol. 29, pp. 377-393, 1985.

    This class is templated over the input histogram type. WARNING:  This
    calculator assumes that the input histogram has only one dimension.

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
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUS___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUS_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHDUS
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUS_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHDUS

        Create a new object of the class itkMomentsThresholdCalculatorHDUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHDUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHDUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMomentsThresholdCalculatorHDUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHDUS in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUS_swigregister(itkMomentsThresholdCalculatorHDUS)
itkMomentsThresholdCalculatorHDUS___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUS___New_orig__
itkMomentsThresholdCalculatorHDUS_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHDUS_cast


def itkMomentsThresholdCalculatorHFD_New():
    return itkMomentsThresholdCalculatorHFD.New()

class itkMomentsThresholdCalculatorHFD(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD):
    r"""


    Computes the Moments's threshold for an image.

    W. Tsai, "Moment-preserving thresholding: a new approach," Computer
    Vision, Graphics, and Image Processing, vol. 29, pp. 377-393, 1985.

    This class is templated over the input histogram type. WARNING:  This
    calculator assumes that the input histogram has only one dimension.

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
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFD___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFD_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHFD
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFD_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHFD

        Create a new object of the class itkMomentsThresholdCalculatorHFD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHFD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHFD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMomentsThresholdCalculatorHFD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHFD in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFD_swigregister(itkMomentsThresholdCalculatorHFD)
itkMomentsThresholdCalculatorHFD___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFD___New_orig__
itkMomentsThresholdCalculatorHFD_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFD_cast


def itkMomentsThresholdCalculatorHFF_New():
    return itkMomentsThresholdCalculatorHFF.New()

class itkMomentsThresholdCalculatorHFF(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    r"""


    Computes the Moments's threshold for an image.

    W. Tsai, "Moment-preserving thresholding: a new approach," Computer
    Vision, Graphics, and Image Processing, vol. 29, pp. 377-393, 1985.

    This class is templated over the input histogram type. WARNING:  This
    calculator assumes that the input histogram has only one dimension.

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
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHFF
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHFF

        Create a new object of the class itkMomentsThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHFF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHFF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMomentsThresholdCalculatorHFF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHFF in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_swigregister(itkMomentsThresholdCalculatorHFF)
itkMomentsThresholdCalculatorHFF___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF___New_orig__
itkMomentsThresholdCalculatorHFF_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFF_cast


def itkMomentsThresholdCalculatorHFSS_New():
    return itkMomentsThresholdCalculatorHFSS.New()

class itkMomentsThresholdCalculatorHFSS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    r"""


    Computes the Moments's threshold for an image.

    W. Tsai, "Moment-preserving thresholding: a new approach," Computer
    Vision, Graphics, and Image Processing, vol. 29, pp. 377-393, 1985.

    This class is templated over the input histogram type. WARNING:  This
    calculator assumes that the input histogram has only one dimension.

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
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHFSS
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHFSS

        Create a new object of the class itkMomentsThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHFSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHFSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMomentsThresholdCalculatorHFSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHFSS in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_swigregister(itkMomentsThresholdCalculatorHFSS)
itkMomentsThresholdCalculatorHFSS___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS___New_orig__
itkMomentsThresholdCalculatorHFSS_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFSS_cast


def itkMomentsThresholdCalculatorHFUC_New():
    return itkMomentsThresholdCalculatorHFUC.New()

class itkMomentsThresholdCalculatorHFUC(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    r"""


    Computes the Moments's threshold for an image.

    W. Tsai, "Moment-preserving thresholding: a new approach," Computer
    Vision, Graphics, and Image Processing, vol. 29, pp. 377-393, 1985.

    This class is templated over the input histogram type. WARNING:  This
    calculator assumes that the input histogram has only one dimension.

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
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHFUC
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHFUC

        Create a new object of the class itkMomentsThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHFUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHFUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMomentsThresholdCalculatorHFUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHFUC in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_swigregister(itkMomentsThresholdCalculatorHFUC)
itkMomentsThresholdCalculatorHFUC___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC___New_orig__
itkMomentsThresholdCalculatorHFUC_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUC_cast


def itkMomentsThresholdCalculatorHFUS_New():
    return itkMomentsThresholdCalculatorHFUS.New()

class itkMomentsThresholdCalculatorHFUS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS):
    r"""


    Computes the Moments's threshold for an image.

    W. Tsai, "Moment-preserving thresholding: a new approach," Computer
    Vision, Graphics, and Image Processing, vol. 29, pp. 377-393, 1985.

    This class is templated over the input histogram type. WARNING:  This
    calculator assumes that the input histogram has only one dimension.

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
    __New_orig__ = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUS___New_orig__)
    Clone = _swig_new_instance_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUS_Clone)
    __swig_destroy__ = _itkMomentsThresholdCalculatorPython.delete_itkMomentsThresholdCalculatorHFUS
    cast = _swig_new_static_method(_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUS_cast)

    def New(*args, **kargs):
        """New() -> itkMomentsThresholdCalculatorHFUS

        Create a new object of the class itkMomentsThresholdCalculatorHFUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMomentsThresholdCalculatorHFUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkMomentsThresholdCalculatorHFUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkMomentsThresholdCalculatorHFUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMomentsThresholdCalculatorHFUS in _itkMomentsThresholdCalculatorPython:
_itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUS_swigregister(itkMomentsThresholdCalculatorHFUS)
itkMomentsThresholdCalculatorHFUS___New_orig__ = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUS___New_orig__
itkMomentsThresholdCalculatorHFUS_cast = _itkMomentsThresholdCalculatorPython.itkMomentsThresholdCalculatorHFUS_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def moments_threshold_calculator(*args, **kwargs):
    """Functional interface for MomentsThresholdCalculator"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.MomentsThresholdCalculator.New(*args, **kwargs)
    return instance.__internal_call__()

def moments_threshold_calculator_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKThresholding.MomentsThresholdCalculator
    moments_threshold_calculator.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    moments_threshold_calculator.__doc__ = filter_object.__doc__




