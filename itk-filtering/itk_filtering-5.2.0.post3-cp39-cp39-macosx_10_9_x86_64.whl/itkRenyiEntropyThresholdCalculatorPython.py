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
    from . import _itkRenyiEntropyThresholdCalculatorPython
else:
    import _itkRenyiEntropyThresholdCalculatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRenyiEntropyThresholdCalculatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRenyiEntropyThresholdCalculatorPython.SWIG_PyStaticMethod_New

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
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.itkHistogramThresholdCalculatorPython
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkCovariantVectorPython

def itkRenyiEntropyThresholdCalculatorHDD_New():
    return itkRenyiEntropyThresholdCalculatorHDD.New()

class itkRenyiEntropyThresholdCalculatorHDD(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD):
    r"""


    Computes the RenyiEntropy's threshold for an image.

    Kapur J.N., Sahoo P.K., and Wong A.K.C. (1985) "A New Method for
    Gray-Level Picture Thresholding Using the Entropy of the Histogram"
    Graphical Models and Image Processing, 29(3): 273-285 M. Emre Celebi
    06.15.2007

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
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDD___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDD_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHDD
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDD_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHDD

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHDD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHDD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHDD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRenyiEntropyThresholdCalculatorHDD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHDD in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDD_swigregister(itkRenyiEntropyThresholdCalculatorHDD)
itkRenyiEntropyThresholdCalculatorHDD___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDD___New_orig__
itkRenyiEntropyThresholdCalculatorHDD_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDD_cast


def itkRenyiEntropyThresholdCalculatorHDF_New():
    return itkRenyiEntropyThresholdCalculatorHDF.New()

class itkRenyiEntropyThresholdCalculatorHDF(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    r"""


    Computes the RenyiEntropy's threshold for an image.

    Kapur J.N., Sahoo P.K., and Wong A.K.C. (1985) "A New Method for
    Gray-Level Picture Thresholding Using the Entropy of the Histogram"
    Graphical Models and Image Processing, 29(3): 273-285 M. Emre Celebi
    06.15.2007

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
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDF___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDF_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHDF
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDF_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHDF

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHDF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHDF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRenyiEntropyThresholdCalculatorHDF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHDF in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDF_swigregister(itkRenyiEntropyThresholdCalculatorHDF)
itkRenyiEntropyThresholdCalculatorHDF___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDF___New_orig__
itkRenyiEntropyThresholdCalculatorHDF_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDF_cast


def itkRenyiEntropyThresholdCalculatorHDSS_New():
    return itkRenyiEntropyThresholdCalculatorHDSS.New()

class itkRenyiEntropyThresholdCalculatorHDSS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    r"""


    Computes the RenyiEntropy's threshold for an image.

    Kapur J.N., Sahoo P.K., and Wong A.K.C. (1985) "A New Method for
    Gray-Level Picture Thresholding Using the Entropy of the Histogram"
    Graphical Models and Image Processing, 29(3): 273-285 M. Emre Celebi
    06.15.2007

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
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDSS___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDSS_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHDSS
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDSS_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHDSS

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHDSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHDSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRenyiEntropyThresholdCalculatorHDSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHDSS in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDSS_swigregister(itkRenyiEntropyThresholdCalculatorHDSS)
itkRenyiEntropyThresholdCalculatorHDSS___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDSS___New_orig__
itkRenyiEntropyThresholdCalculatorHDSS_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDSS_cast


def itkRenyiEntropyThresholdCalculatorHDUC_New():
    return itkRenyiEntropyThresholdCalculatorHDUC.New()

class itkRenyiEntropyThresholdCalculatorHDUC(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    r"""


    Computes the RenyiEntropy's threshold for an image.

    Kapur J.N., Sahoo P.K., and Wong A.K.C. (1985) "A New Method for
    Gray-Level Picture Thresholding Using the Entropy of the Histogram"
    Graphical Models and Image Processing, 29(3): 273-285 M. Emre Celebi
    06.15.2007

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
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUC___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUC_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHDUC
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUC_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHDUC

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHDUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHDUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRenyiEntropyThresholdCalculatorHDUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHDUC in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUC_swigregister(itkRenyiEntropyThresholdCalculatorHDUC)
itkRenyiEntropyThresholdCalculatorHDUC___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUC___New_orig__
itkRenyiEntropyThresholdCalculatorHDUC_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUC_cast


def itkRenyiEntropyThresholdCalculatorHDUS_New():
    return itkRenyiEntropyThresholdCalculatorHDUS.New()

class itkRenyiEntropyThresholdCalculatorHDUS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS):
    r"""


    Computes the RenyiEntropy's threshold for an image.

    Kapur J.N., Sahoo P.K., and Wong A.K.C. (1985) "A New Method for
    Gray-Level Picture Thresholding Using the Entropy of the Histogram"
    Graphical Models and Image Processing, 29(3): 273-285 M. Emre Celebi
    06.15.2007

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
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUS___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUS_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHDUS
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUS_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHDUS

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHDUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHDUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHDUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRenyiEntropyThresholdCalculatorHDUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHDUS in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUS_swigregister(itkRenyiEntropyThresholdCalculatorHDUS)
itkRenyiEntropyThresholdCalculatorHDUS___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUS___New_orig__
itkRenyiEntropyThresholdCalculatorHDUS_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHDUS_cast


def itkRenyiEntropyThresholdCalculatorHFD_New():
    return itkRenyiEntropyThresholdCalculatorHFD.New()

class itkRenyiEntropyThresholdCalculatorHFD(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD):
    r"""


    Computes the RenyiEntropy's threshold for an image.

    Kapur J.N., Sahoo P.K., and Wong A.K.C. (1985) "A New Method for
    Gray-Level Picture Thresholding Using the Entropy of the Histogram"
    Graphical Models and Image Processing, 29(3): 273-285 M. Emre Celebi
    06.15.2007

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
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFD___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFD_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHFD
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFD_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHFD

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHFD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHFD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHFD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRenyiEntropyThresholdCalculatorHFD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHFD in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFD_swigregister(itkRenyiEntropyThresholdCalculatorHFD)
itkRenyiEntropyThresholdCalculatorHFD___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFD___New_orig__
itkRenyiEntropyThresholdCalculatorHFD_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFD_cast


def itkRenyiEntropyThresholdCalculatorHFF_New():
    return itkRenyiEntropyThresholdCalculatorHFF.New()

class itkRenyiEntropyThresholdCalculatorHFF(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    r"""


    Computes the RenyiEntropy's threshold for an image.

    Kapur J.N., Sahoo P.K., and Wong A.K.C. (1985) "A New Method for
    Gray-Level Picture Thresholding Using the Entropy of the Histogram"
    Graphical Models and Image Processing, 29(3): 273-285 M. Emre Celebi
    06.15.2007

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
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFF___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFF_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHFF
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFF_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHFF

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHFF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHFF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRenyiEntropyThresholdCalculatorHFF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHFF in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFF_swigregister(itkRenyiEntropyThresholdCalculatorHFF)
itkRenyiEntropyThresholdCalculatorHFF___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFF___New_orig__
itkRenyiEntropyThresholdCalculatorHFF_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFF_cast


def itkRenyiEntropyThresholdCalculatorHFSS_New():
    return itkRenyiEntropyThresholdCalculatorHFSS.New()

class itkRenyiEntropyThresholdCalculatorHFSS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    r"""


    Computes the RenyiEntropy's threshold for an image.

    Kapur J.N., Sahoo P.K., and Wong A.K.C. (1985) "A New Method for
    Gray-Level Picture Thresholding Using the Entropy of the Histogram"
    Graphical Models and Image Processing, 29(3): 273-285 M. Emre Celebi
    06.15.2007

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
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFSS___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFSS_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHFSS
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFSS_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHFSS

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHFSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHFSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRenyiEntropyThresholdCalculatorHFSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHFSS in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFSS_swigregister(itkRenyiEntropyThresholdCalculatorHFSS)
itkRenyiEntropyThresholdCalculatorHFSS___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFSS___New_orig__
itkRenyiEntropyThresholdCalculatorHFSS_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFSS_cast


def itkRenyiEntropyThresholdCalculatorHFUC_New():
    return itkRenyiEntropyThresholdCalculatorHFUC.New()

class itkRenyiEntropyThresholdCalculatorHFUC(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    r"""


    Computes the RenyiEntropy's threshold for an image.

    Kapur J.N., Sahoo P.K., and Wong A.K.C. (1985) "A New Method for
    Gray-Level Picture Thresholding Using the Entropy of the Histogram"
    Graphical Models and Image Processing, 29(3): 273-285 M. Emre Celebi
    06.15.2007

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
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUC___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUC_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHFUC
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUC_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHFUC

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHFUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHFUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRenyiEntropyThresholdCalculatorHFUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHFUC in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUC_swigregister(itkRenyiEntropyThresholdCalculatorHFUC)
itkRenyiEntropyThresholdCalculatorHFUC___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUC___New_orig__
itkRenyiEntropyThresholdCalculatorHFUC_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUC_cast


def itkRenyiEntropyThresholdCalculatorHFUS_New():
    return itkRenyiEntropyThresholdCalculatorHFUS.New()

class itkRenyiEntropyThresholdCalculatorHFUS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS):
    r"""


    Computes the RenyiEntropy's threshold for an image.

    Kapur J.N., Sahoo P.K., and Wong A.K.C. (1985) "A New Method for
    Gray-Level Picture Thresholding Using the Entropy of the Histogram"
    Graphical Models and Image Processing, 29(3): 273-285 M. Emre Celebi
    06.15.2007

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
    __New_orig__ = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUS___New_orig__)
    Clone = _swig_new_instance_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUS_Clone)
    __swig_destroy__ = _itkRenyiEntropyThresholdCalculatorPython.delete_itkRenyiEntropyThresholdCalculatorHFUS
    cast = _swig_new_static_method(_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUS_cast)

    def New(*args, **kargs):
        """New() -> itkRenyiEntropyThresholdCalculatorHFUS

        Create a new object of the class itkRenyiEntropyThresholdCalculatorHFUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRenyiEntropyThresholdCalculatorHFUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRenyiEntropyThresholdCalculatorHFUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRenyiEntropyThresholdCalculatorHFUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRenyiEntropyThresholdCalculatorHFUS in _itkRenyiEntropyThresholdCalculatorPython:
_itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUS_swigregister(itkRenyiEntropyThresholdCalculatorHFUS)
itkRenyiEntropyThresholdCalculatorHFUS___New_orig__ = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUS___New_orig__
itkRenyiEntropyThresholdCalculatorHFUS_cast = _itkRenyiEntropyThresholdCalculatorPython.itkRenyiEntropyThresholdCalculatorHFUS_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def renyi_entropy_threshold_calculator(*args, **kwargs):
    """Functional interface for RenyiEntropyThresholdCalculator"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.RenyiEntropyThresholdCalculator.New(*args, **kwargs)
    return instance.__internal_call__()

def renyi_entropy_threshold_calculator_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKThresholding.RenyiEntropyThresholdCalculator
    renyi_entropy_threshold_calculator.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    renyi_entropy_threshold_calculator.__doc__ = filter_object.__doc__




