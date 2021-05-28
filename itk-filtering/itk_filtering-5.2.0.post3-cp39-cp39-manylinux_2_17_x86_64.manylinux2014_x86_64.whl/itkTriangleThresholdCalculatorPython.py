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
    from . import _itkTriangleThresholdCalculatorPython
else:
    import _itkTriangleThresholdCalculatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkTriangleThresholdCalculatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkTriangleThresholdCalculatorPython.SWIG_PyStaticMethod_New

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

def itkTriangleThresholdCalculatorHDD_New():
    return itkTriangleThresholdCalculatorHDD.New()

class itkTriangleThresholdCalculatorHDD(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD):
    r"""


    Computes the Triangle's threshold for an image.

    This calculator computes the Triangle's threshold which separates an
    image into foreground and background components. The method relies on
    a histogram of image intensities. A line is drawn between the peak
    point in the hist and the furthest zero point (robustly estimated as
    the 1% or 99% point). The threshold is the position of maximum
    difference between the line and the original histogram.

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
    __New_orig__ = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDD___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDD_Clone)
    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHDD
    cast = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDD_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHDD

        Create a new object of the class itkTriangleThresholdCalculatorHDD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHDD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHDD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleThresholdCalculatorHDD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleThresholdCalculatorHDD in _itkTriangleThresholdCalculatorPython:
_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDD_swigregister(itkTriangleThresholdCalculatorHDD)
itkTriangleThresholdCalculatorHDD___New_orig__ = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDD___New_orig__
itkTriangleThresholdCalculatorHDD_cast = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDD_cast


def itkTriangleThresholdCalculatorHDF_New():
    return itkTriangleThresholdCalculatorHDF.New()

class itkTriangleThresholdCalculatorHDF(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    r"""


    Computes the Triangle's threshold for an image.

    This calculator computes the Triangle's threshold which separates an
    image into foreground and background components. The method relies on
    a histogram of image intensities. A line is drawn between the peak
    point in the hist and the furthest zero point (robustly estimated as
    the 1% or 99% point). The threshold is the position of maximum
    difference between the line and the original histogram.

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
    __New_orig__ = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF_Clone)
    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHDF
    cast = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHDF

        Create a new object of the class itkTriangleThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHDF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHDF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleThresholdCalculatorHDF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleThresholdCalculatorHDF in _itkTriangleThresholdCalculatorPython:
_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF_swigregister(itkTriangleThresholdCalculatorHDF)
itkTriangleThresholdCalculatorHDF___New_orig__ = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF___New_orig__
itkTriangleThresholdCalculatorHDF_cast = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDF_cast


def itkTriangleThresholdCalculatorHDSS_New():
    return itkTriangleThresholdCalculatorHDSS.New()

class itkTriangleThresholdCalculatorHDSS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    r"""


    Computes the Triangle's threshold for an image.

    This calculator computes the Triangle's threshold which separates an
    image into foreground and background components. The method relies on
    a histogram of image intensities. A line is drawn between the peak
    point in the hist and the furthest zero point (robustly estimated as
    the 1% or 99% point). The threshold is the position of maximum
    difference between the line and the original histogram.

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
    __New_orig__ = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS_Clone)
    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHDSS
    cast = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHDSS

        Create a new object of the class itkTriangleThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHDSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHDSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleThresholdCalculatorHDSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleThresholdCalculatorHDSS in _itkTriangleThresholdCalculatorPython:
_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS_swigregister(itkTriangleThresholdCalculatorHDSS)
itkTriangleThresholdCalculatorHDSS___New_orig__ = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS___New_orig__
itkTriangleThresholdCalculatorHDSS_cast = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDSS_cast


def itkTriangleThresholdCalculatorHDUC_New():
    return itkTriangleThresholdCalculatorHDUC.New()

class itkTriangleThresholdCalculatorHDUC(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    r"""


    Computes the Triangle's threshold for an image.

    This calculator computes the Triangle's threshold which separates an
    image into foreground and background components. The method relies on
    a histogram of image intensities. A line is drawn between the peak
    point in the hist and the furthest zero point (robustly estimated as
    the 1% or 99% point). The threshold is the position of maximum
    difference between the line and the original histogram.

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
    __New_orig__ = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC_Clone)
    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHDUC
    cast = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHDUC

        Create a new object of the class itkTriangleThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHDUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHDUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleThresholdCalculatorHDUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleThresholdCalculatorHDUC in _itkTriangleThresholdCalculatorPython:
_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC_swigregister(itkTriangleThresholdCalculatorHDUC)
itkTriangleThresholdCalculatorHDUC___New_orig__ = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC___New_orig__
itkTriangleThresholdCalculatorHDUC_cast = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUC_cast


def itkTriangleThresholdCalculatorHDUS_New():
    return itkTriangleThresholdCalculatorHDUS.New()

class itkTriangleThresholdCalculatorHDUS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS):
    r"""


    Computes the Triangle's threshold for an image.

    This calculator computes the Triangle's threshold which separates an
    image into foreground and background components. The method relies on
    a histogram of image intensities. A line is drawn between the peak
    point in the hist and the furthest zero point (robustly estimated as
    the 1% or 99% point). The threshold is the position of maximum
    difference between the line and the original histogram.

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
    __New_orig__ = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUS___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUS_Clone)
    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHDUS
    cast = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUS_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHDUS

        Create a new object of the class itkTriangleThresholdCalculatorHDUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHDUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHDUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleThresholdCalculatorHDUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleThresholdCalculatorHDUS in _itkTriangleThresholdCalculatorPython:
_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUS_swigregister(itkTriangleThresholdCalculatorHDUS)
itkTriangleThresholdCalculatorHDUS___New_orig__ = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUS___New_orig__
itkTriangleThresholdCalculatorHDUS_cast = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHDUS_cast


def itkTriangleThresholdCalculatorHFD_New():
    return itkTriangleThresholdCalculatorHFD.New()

class itkTriangleThresholdCalculatorHFD(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD):
    r"""


    Computes the Triangle's threshold for an image.

    This calculator computes the Triangle's threshold which separates an
    image into foreground and background components. The method relies on
    a histogram of image intensities. A line is drawn between the peak
    point in the hist and the furthest zero point (robustly estimated as
    the 1% or 99% point). The threshold is the position of maximum
    difference between the line and the original histogram.

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
    __New_orig__ = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFD___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFD_Clone)
    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHFD
    cast = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFD_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHFD

        Create a new object of the class itkTriangleThresholdCalculatorHFD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHFD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHFD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleThresholdCalculatorHFD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleThresholdCalculatorHFD in _itkTriangleThresholdCalculatorPython:
_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFD_swigregister(itkTriangleThresholdCalculatorHFD)
itkTriangleThresholdCalculatorHFD___New_orig__ = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFD___New_orig__
itkTriangleThresholdCalculatorHFD_cast = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFD_cast


def itkTriangleThresholdCalculatorHFF_New():
    return itkTriangleThresholdCalculatorHFF.New()

class itkTriangleThresholdCalculatorHFF(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    r"""


    Computes the Triangle's threshold for an image.

    This calculator computes the Triangle's threshold which separates an
    image into foreground and background components. The method relies on
    a histogram of image intensities. A line is drawn between the peak
    point in the hist and the furthest zero point (robustly estimated as
    the 1% or 99% point). The threshold is the position of maximum
    difference between the line and the original histogram.

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
    __New_orig__ = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF_Clone)
    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHFF
    cast = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHFF

        Create a new object of the class itkTriangleThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHFF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHFF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleThresholdCalculatorHFF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleThresholdCalculatorHFF in _itkTriangleThresholdCalculatorPython:
_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF_swigregister(itkTriangleThresholdCalculatorHFF)
itkTriangleThresholdCalculatorHFF___New_orig__ = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF___New_orig__
itkTriangleThresholdCalculatorHFF_cast = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFF_cast


def itkTriangleThresholdCalculatorHFSS_New():
    return itkTriangleThresholdCalculatorHFSS.New()

class itkTriangleThresholdCalculatorHFSS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    r"""


    Computes the Triangle's threshold for an image.

    This calculator computes the Triangle's threshold which separates an
    image into foreground and background components. The method relies on
    a histogram of image intensities. A line is drawn between the peak
    point in the hist and the furthest zero point (robustly estimated as
    the 1% or 99% point). The threshold is the position of maximum
    difference between the line and the original histogram.

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
    __New_orig__ = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS_Clone)
    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHFSS
    cast = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHFSS

        Create a new object of the class itkTriangleThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHFSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHFSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleThresholdCalculatorHFSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleThresholdCalculatorHFSS in _itkTriangleThresholdCalculatorPython:
_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS_swigregister(itkTriangleThresholdCalculatorHFSS)
itkTriangleThresholdCalculatorHFSS___New_orig__ = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS___New_orig__
itkTriangleThresholdCalculatorHFSS_cast = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFSS_cast


def itkTriangleThresholdCalculatorHFUC_New():
    return itkTriangleThresholdCalculatorHFUC.New()

class itkTriangleThresholdCalculatorHFUC(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    r"""


    Computes the Triangle's threshold for an image.

    This calculator computes the Triangle's threshold which separates an
    image into foreground and background components. The method relies on
    a histogram of image intensities. A line is drawn between the peak
    point in the hist and the furthest zero point (robustly estimated as
    the 1% or 99% point). The threshold is the position of maximum
    difference between the line and the original histogram.

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
    __New_orig__ = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC_Clone)
    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHFUC
    cast = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHFUC

        Create a new object of the class itkTriangleThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHFUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHFUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleThresholdCalculatorHFUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleThresholdCalculatorHFUC in _itkTriangleThresholdCalculatorPython:
_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC_swigregister(itkTriangleThresholdCalculatorHFUC)
itkTriangleThresholdCalculatorHFUC___New_orig__ = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC___New_orig__
itkTriangleThresholdCalculatorHFUC_cast = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUC_cast


def itkTriangleThresholdCalculatorHFUS_New():
    return itkTriangleThresholdCalculatorHFUS.New()

class itkTriangleThresholdCalculatorHFUS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS):
    r"""


    Computes the Triangle's threshold for an image.

    This calculator computes the Triangle's threshold which separates an
    image into foreground and background components. The method relies on
    a histogram of image intensities. A line is drawn between the peak
    point in the hist and the furthest zero point (robustly estimated as
    the 1% or 99% point). The threshold is the position of maximum
    difference between the line and the original histogram.

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
    __New_orig__ = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUS___New_orig__)
    Clone = _swig_new_instance_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUS_Clone)
    __swig_destroy__ = _itkTriangleThresholdCalculatorPython.delete_itkTriangleThresholdCalculatorHFUS
    cast = _swig_new_static_method(_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUS_cast)

    def New(*args, **kargs):
        """New() -> itkTriangleThresholdCalculatorHFUS

        Create a new object of the class itkTriangleThresholdCalculatorHFUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTriangleThresholdCalculatorHFUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkTriangleThresholdCalculatorHFUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkTriangleThresholdCalculatorHFUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTriangleThresholdCalculatorHFUS in _itkTriangleThresholdCalculatorPython:
_itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUS_swigregister(itkTriangleThresholdCalculatorHFUS)
itkTriangleThresholdCalculatorHFUS___New_orig__ = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUS___New_orig__
itkTriangleThresholdCalculatorHFUS_cast = _itkTriangleThresholdCalculatorPython.itkTriangleThresholdCalculatorHFUS_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def triangle_threshold_calculator(*args, **kwargs):
    """Functional interface for TriangleThresholdCalculator"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.TriangleThresholdCalculator.New(*args, **kwargs)
    return instance.__internal_call__()

def triangle_threshold_calculator_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKThresholding.TriangleThresholdCalculator
    triangle_threshold_calculator.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    triangle_threshold_calculator.__doc__ = filter_object.__doc__




