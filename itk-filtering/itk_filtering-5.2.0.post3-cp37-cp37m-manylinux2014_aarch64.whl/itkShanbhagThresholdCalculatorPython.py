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
    from . import _itkShanbhagThresholdCalculatorPython
else:
    import _itkShanbhagThresholdCalculatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkShanbhagThresholdCalculatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkShanbhagThresholdCalculatorPython.SWIG_PyStaticMethod_New

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
import itk.itkHistogramPython
import itk.itkArrayPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkSamplePython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.ITKCommonBasePython
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkCovariantVectorPython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython

def itkShanbhagThresholdCalculatorHDD_New():
    return itkShanbhagThresholdCalculatorHDD.New()

class itkShanbhagThresholdCalculatorHDD(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD):
    r"""


    Computes the Shanbhag threshold for an image. Aka intermeans.

    Shanhbag A.G. (1994) "Utilization of Information Measure as a Means
    of  Image Thresholding" Graphical Models and Image Processing, 56(5):
    414-419

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
    __New_orig__ = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDD___New_orig__)
    Clone = _swig_new_instance_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDD_Clone)
    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHDD
    cast = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDD_cast)

    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHDD

        Create a new object of the class itkShanbhagThresholdCalculatorHDD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHDD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHDD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShanbhagThresholdCalculatorHDD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShanbhagThresholdCalculatorHDD in _itkShanbhagThresholdCalculatorPython:
_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDD_swigregister(itkShanbhagThresholdCalculatorHDD)
itkShanbhagThresholdCalculatorHDD___New_orig__ = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDD___New_orig__
itkShanbhagThresholdCalculatorHDD_cast = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDD_cast


def itkShanbhagThresholdCalculatorHDF_New():
    return itkShanbhagThresholdCalculatorHDF.New()

class itkShanbhagThresholdCalculatorHDF(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    r"""


    Computes the Shanbhag threshold for an image. Aka intermeans.

    Shanhbag A.G. (1994) "Utilization of Information Measure as a Means
    of  Image Thresholding" Graphical Models and Image Processing, 56(5):
    414-419

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
    __New_orig__ = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF___New_orig__)
    Clone = _swig_new_instance_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF_Clone)
    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHDF
    cast = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF_cast)

    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHDF

        Create a new object of the class itkShanbhagThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHDF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHDF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShanbhagThresholdCalculatorHDF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShanbhagThresholdCalculatorHDF in _itkShanbhagThresholdCalculatorPython:
_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF_swigregister(itkShanbhagThresholdCalculatorHDF)
itkShanbhagThresholdCalculatorHDF___New_orig__ = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF___New_orig__
itkShanbhagThresholdCalculatorHDF_cast = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDF_cast


def itkShanbhagThresholdCalculatorHDSS_New():
    return itkShanbhagThresholdCalculatorHDSS.New()

class itkShanbhagThresholdCalculatorHDSS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    r"""


    Computes the Shanbhag threshold for an image. Aka intermeans.

    Shanhbag A.G. (1994) "Utilization of Information Measure as a Means
    of  Image Thresholding" Graphical Models and Image Processing, 56(5):
    414-419

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
    __New_orig__ = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS___New_orig__)
    Clone = _swig_new_instance_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS_Clone)
    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHDSS
    cast = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS_cast)

    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHDSS

        Create a new object of the class itkShanbhagThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHDSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHDSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShanbhagThresholdCalculatorHDSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShanbhagThresholdCalculatorHDSS in _itkShanbhagThresholdCalculatorPython:
_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS_swigregister(itkShanbhagThresholdCalculatorHDSS)
itkShanbhagThresholdCalculatorHDSS___New_orig__ = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS___New_orig__
itkShanbhagThresholdCalculatorHDSS_cast = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDSS_cast


def itkShanbhagThresholdCalculatorHDUC_New():
    return itkShanbhagThresholdCalculatorHDUC.New()

class itkShanbhagThresholdCalculatorHDUC(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    r"""


    Computes the Shanbhag threshold for an image. Aka intermeans.

    Shanhbag A.G. (1994) "Utilization of Information Measure as a Means
    of  Image Thresholding" Graphical Models and Image Processing, 56(5):
    414-419

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
    __New_orig__ = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC___New_orig__)
    Clone = _swig_new_instance_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC_Clone)
    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHDUC
    cast = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC_cast)

    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHDUC

        Create a new object of the class itkShanbhagThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHDUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHDUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShanbhagThresholdCalculatorHDUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShanbhagThresholdCalculatorHDUC in _itkShanbhagThresholdCalculatorPython:
_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC_swigregister(itkShanbhagThresholdCalculatorHDUC)
itkShanbhagThresholdCalculatorHDUC___New_orig__ = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC___New_orig__
itkShanbhagThresholdCalculatorHDUC_cast = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUC_cast


def itkShanbhagThresholdCalculatorHDUS_New():
    return itkShanbhagThresholdCalculatorHDUS.New()

class itkShanbhagThresholdCalculatorHDUS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS):
    r"""


    Computes the Shanbhag threshold for an image. Aka intermeans.

    Shanhbag A.G. (1994) "Utilization of Information Measure as a Means
    of  Image Thresholding" Graphical Models and Image Processing, 56(5):
    414-419

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
    __New_orig__ = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUS___New_orig__)
    Clone = _swig_new_instance_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUS_Clone)
    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHDUS
    cast = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUS_cast)

    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHDUS

        Create a new object of the class itkShanbhagThresholdCalculatorHDUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHDUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHDUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShanbhagThresholdCalculatorHDUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShanbhagThresholdCalculatorHDUS in _itkShanbhagThresholdCalculatorPython:
_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUS_swigregister(itkShanbhagThresholdCalculatorHDUS)
itkShanbhagThresholdCalculatorHDUS___New_orig__ = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUS___New_orig__
itkShanbhagThresholdCalculatorHDUS_cast = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHDUS_cast


def itkShanbhagThresholdCalculatorHFD_New():
    return itkShanbhagThresholdCalculatorHFD.New()

class itkShanbhagThresholdCalculatorHFD(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD):
    r"""


    Computes the Shanbhag threshold for an image. Aka intermeans.

    Shanhbag A.G. (1994) "Utilization of Information Measure as a Means
    of  Image Thresholding" Graphical Models and Image Processing, 56(5):
    414-419

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
    __New_orig__ = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFD___New_orig__)
    Clone = _swig_new_instance_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFD_Clone)
    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHFD
    cast = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFD_cast)

    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHFD

        Create a new object of the class itkShanbhagThresholdCalculatorHFD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHFD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHFD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShanbhagThresholdCalculatorHFD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShanbhagThresholdCalculatorHFD in _itkShanbhagThresholdCalculatorPython:
_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFD_swigregister(itkShanbhagThresholdCalculatorHFD)
itkShanbhagThresholdCalculatorHFD___New_orig__ = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFD___New_orig__
itkShanbhagThresholdCalculatorHFD_cast = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFD_cast


def itkShanbhagThresholdCalculatorHFF_New():
    return itkShanbhagThresholdCalculatorHFF.New()

class itkShanbhagThresholdCalculatorHFF(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    r"""


    Computes the Shanbhag threshold for an image. Aka intermeans.

    Shanhbag A.G. (1994) "Utilization of Information Measure as a Means
    of  Image Thresholding" Graphical Models and Image Processing, 56(5):
    414-419

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
    __New_orig__ = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF___New_orig__)
    Clone = _swig_new_instance_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF_Clone)
    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHFF
    cast = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF_cast)

    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHFF

        Create a new object of the class itkShanbhagThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHFF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHFF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShanbhagThresholdCalculatorHFF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShanbhagThresholdCalculatorHFF in _itkShanbhagThresholdCalculatorPython:
_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF_swigregister(itkShanbhagThresholdCalculatorHFF)
itkShanbhagThresholdCalculatorHFF___New_orig__ = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF___New_orig__
itkShanbhagThresholdCalculatorHFF_cast = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFF_cast


def itkShanbhagThresholdCalculatorHFSS_New():
    return itkShanbhagThresholdCalculatorHFSS.New()

class itkShanbhagThresholdCalculatorHFSS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    r"""


    Computes the Shanbhag threshold for an image. Aka intermeans.

    Shanhbag A.G. (1994) "Utilization of Information Measure as a Means
    of  Image Thresholding" Graphical Models and Image Processing, 56(5):
    414-419

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
    __New_orig__ = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS___New_orig__)
    Clone = _swig_new_instance_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS_Clone)
    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHFSS
    cast = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS_cast)

    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHFSS

        Create a new object of the class itkShanbhagThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHFSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHFSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShanbhagThresholdCalculatorHFSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShanbhagThresholdCalculatorHFSS in _itkShanbhagThresholdCalculatorPython:
_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS_swigregister(itkShanbhagThresholdCalculatorHFSS)
itkShanbhagThresholdCalculatorHFSS___New_orig__ = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS___New_orig__
itkShanbhagThresholdCalculatorHFSS_cast = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFSS_cast


def itkShanbhagThresholdCalculatorHFUC_New():
    return itkShanbhagThresholdCalculatorHFUC.New()

class itkShanbhagThresholdCalculatorHFUC(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    r"""


    Computes the Shanbhag threshold for an image. Aka intermeans.

    Shanhbag A.G. (1994) "Utilization of Information Measure as a Means
    of  Image Thresholding" Graphical Models and Image Processing, 56(5):
    414-419

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
    __New_orig__ = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC___New_orig__)
    Clone = _swig_new_instance_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC_Clone)
    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHFUC
    cast = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC_cast)

    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHFUC

        Create a new object of the class itkShanbhagThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHFUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHFUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShanbhagThresholdCalculatorHFUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShanbhagThresholdCalculatorHFUC in _itkShanbhagThresholdCalculatorPython:
_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC_swigregister(itkShanbhagThresholdCalculatorHFUC)
itkShanbhagThresholdCalculatorHFUC___New_orig__ = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC___New_orig__
itkShanbhagThresholdCalculatorHFUC_cast = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUC_cast


def itkShanbhagThresholdCalculatorHFUS_New():
    return itkShanbhagThresholdCalculatorHFUS.New()

class itkShanbhagThresholdCalculatorHFUS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS):
    r"""


    Computes the Shanbhag threshold for an image. Aka intermeans.

    Shanhbag A.G. (1994) "Utilization of Information Measure as a Means
    of  Image Thresholding" Graphical Models and Image Processing, 56(5):
    414-419

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
    __New_orig__ = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUS___New_orig__)
    Clone = _swig_new_instance_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUS_Clone)
    __swig_destroy__ = _itkShanbhagThresholdCalculatorPython.delete_itkShanbhagThresholdCalculatorHFUS
    cast = _swig_new_static_method(_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUS_cast)

    def New(*args, **kargs):
        """New() -> itkShanbhagThresholdCalculatorHFUS

        Create a new object of the class itkShanbhagThresholdCalculatorHFUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkShanbhagThresholdCalculatorHFUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkShanbhagThresholdCalculatorHFUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkShanbhagThresholdCalculatorHFUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkShanbhagThresholdCalculatorHFUS in _itkShanbhagThresholdCalculatorPython:
_itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUS_swigregister(itkShanbhagThresholdCalculatorHFUS)
itkShanbhagThresholdCalculatorHFUS___New_orig__ = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUS___New_orig__
itkShanbhagThresholdCalculatorHFUS_cast = _itkShanbhagThresholdCalculatorPython.itkShanbhagThresholdCalculatorHFUS_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def shanbhag_threshold_calculator(*args, **kwargs):
    """Functional interface for ShanbhagThresholdCalculator"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.ShanbhagThresholdCalculator.New(*args, **kwargs)
    return instance.__internal_call__()

def shanbhag_threshold_calculator_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKThresholding.ShanbhagThresholdCalculator
    shanbhag_threshold_calculator.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    shanbhag_threshold_calculator.__doc__ = filter_object.__doc__




