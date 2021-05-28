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
    from . import _itkHuangThresholdCalculatorPython
else:
    import _itkHuangThresholdCalculatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkHuangThresholdCalculatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkHuangThresholdCalculatorPython.SWIG_PyStaticMethod_New

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
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.stdcomplexPython
import itk.itkRGBAPixelPython
import itk.itkFixedArrayPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkRGBPixelPython
import itk.itkCovariantVectorPython
import itk.itkArrayPython
import itk.itkHistogramPython
import itk.itkSamplePython

def itkHuangThresholdCalculatorHDD_New():
    return itkHuangThresholdCalculatorHDD.New()

class itkHuangThresholdCalculatorHDD(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD):
    r"""


    Computes the Huang's threshold for an image.

    This calculator computes the Huang's fuzzy threshold which separates
    an image into foreground and background components. Uses Shannon's
    entropy function (one can also use Yager's entropy function) Huang
    L.-K. and Wang M.-J.J. (1995) "Image Thresholding by Minimizing  the
    Measures of Fuzziness" Pattern Recognition, 28(1): 41-51
    Reimplemented (to handle 16-bit efficiently) by Johannes Schindelin
    Jan 31, 2011

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
    __New_orig__ = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDD___New_orig__)
    Clone = _swig_new_instance_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDD_Clone)
    __swig_destroy__ = _itkHuangThresholdCalculatorPython.delete_itkHuangThresholdCalculatorHDD
    cast = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDD_cast)

    def New(*args, **kargs):
        """New() -> itkHuangThresholdCalculatorHDD

        Create a new object of the class itkHuangThresholdCalculatorHDD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHuangThresholdCalculatorHDD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHuangThresholdCalculatorHDD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHuangThresholdCalculatorHDD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHuangThresholdCalculatorHDD in _itkHuangThresholdCalculatorPython:
_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDD_swigregister(itkHuangThresholdCalculatorHDD)
itkHuangThresholdCalculatorHDD___New_orig__ = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDD___New_orig__
itkHuangThresholdCalculatorHDD_cast = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDD_cast


def itkHuangThresholdCalculatorHDF_New():
    return itkHuangThresholdCalculatorHDF.New()

class itkHuangThresholdCalculatorHDF(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    r"""


    Computes the Huang's threshold for an image.

    This calculator computes the Huang's fuzzy threshold which separates
    an image into foreground and background components. Uses Shannon's
    entropy function (one can also use Yager's entropy function) Huang
    L.-K. and Wang M.-J.J. (1995) "Image Thresholding by Minimizing  the
    Measures of Fuzziness" Pattern Recognition, 28(1): 41-51
    Reimplemented (to handle 16-bit efficiently) by Johannes Schindelin
    Jan 31, 2011

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
    __New_orig__ = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDF___New_orig__)
    Clone = _swig_new_instance_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDF_Clone)
    __swig_destroy__ = _itkHuangThresholdCalculatorPython.delete_itkHuangThresholdCalculatorHDF
    cast = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDF_cast)

    def New(*args, **kargs):
        """New() -> itkHuangThresholdCalculatorHDF

        Create a new object of the class itkHuangThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHuangThresholdCalculatorHDF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHuangThresholdCalculatorHDF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHuangThresholdCalculatorHDF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHuangThresholdCalculatorHDF in _itkHuangThresholdCalculatorPython:
_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDF_swigregister(itkHuangThresholdCalculatorHDF)
itkHuangThresholdCalculatorHDF___New_orig__ = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDF___New_orig__
itkHuangThresholdCalculatorHDF_cast = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDF_cast


def itkHuangThresholdCalculatorHDSS_New():
    return itkHuangThresholdCalculatorHDSS.New()

class itkHuangThresholdCalculatorHDSS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    r"""


    Computes the Huang's threshold for an image.

    This calculator computes the Huang's fuzzy threshold which separates
    an image into foreground and background components. Uses Shannon's
    entropy function (one can also use Yager's entropy function) Huang
    L.-K. and Wang M.-J.J. (1995) "Image Thresholding by Minimizing  the
    Measures of Fuzziness" Pattern Recognition, 28(1): 41-51
    Reimplemented (to handle 16-bit efficiently) by Johannes Schindelin
    Jan 31, 2011

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
    __New_orig__ = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDSS___New_orig__)
    Clone = _swig_new_instance_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDSS_Clone)
    __swig_destroy__ = _itkHuangThresholdCalculatorPython.delete_itkHuangThresholdCalculatorHDSS
    cast = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDSS_cast)

    def New(*args, **kargs):
        """New() -> itkHuangThresholdCalculatorHDSS

        Create a new object of the class itkHuangThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHuangThresholdCalculatorHDSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHuangThresholdCalculatorHDSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHuangThresholdCalculatorHDSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHuangThresholdCalculatorHDSS in _itkHuangThresholdCalculatorPython:
_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDSS_swigregister(itkHuangThresholdCalculatorHDSS)
itkHuangThresholdCalculatorHDSS___New_orig__ = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDSS___New_orig__
itkHuangThresholdCalculatorHDSS_cast = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDSS_cast


def itkHuangThresholdCalculatorHDUC_New():
    return itkHuangThresholdCalculatorHDUC.New()

class itkHuangThresholdCalculatorHDUC(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    r"""


    Computes the Huang's threshold for an image.

    This calculator computes the Huang's fuzzy threshold which separates
    an image into foreground and background components. Uses Shannon's
    entropy function (one can also use Yager's entropy function) Huang
    L.-K. and Wang M.-J.J. (1995) "Image Thresholding by Minimizing  the
    Measures of Fuzziness" Pattern Recognition, 28(1): 41-51
    Reimplemented (to handle 16-bit efficiently) by Johannes Schindelin
    Jan 31, 2011

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
    __New_orig__ = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDUC___New_orig__)
    Clone = _swig_new_instance_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDUC_Clone)
    __swig_destroy__ = _itkHuangThresholdCalculatorPython.delete_itkHuangThresholdCalculatorHDUC
    cast = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDUC_cast)

    def New(*args, **kargs):
        """New() -> itkHuangThresholdCalculatorHDUC

        Create a new object of the class itkHuangThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHuangThresholdCalculatorHDUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHuangThresholdCalculatorHDUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHuangThresholdCalculatorHDUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHuangThresholdCalculatorHDUC in _itkHuangThresholdCalculatorPython:
_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDUC_swigregister(itkHuangThresholdCalculatorHDUC)
itkHuangThresholdCalculatorHDUC___New_orig__ = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDUC___New_orig__
itkHuangThresholdCalculatorHDUC_cast = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDUC_cast


def itkHuangThresholdCalculatorHDUS_New():
    return itkHuangThresholdCalculatorHDUS.New()

class itkHuangThresholdCalculatorHDUS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS):
    r"""


    Computes the Huang's threshold for an image.

    This calculator computes the Huang's fuzzy threshold which separates
    an image into foreground and background components. Uses Shannon's
    entropy function (one can also use Yager's entropy function) Huang
    L.-K. and Wang M.-J.J. (1995) "Image Thresholding by Minimizing  the
    Measures of Fuzziness" Pattern Recognition, 28(1): 41-51
    Reimplemented (to handle 16-bit efficiently) by Johannes Schindelin
    Jan 31, 2011

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
    __New_orig__ = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDUS___New_orig__)
    Clone = _swig_new_instance_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDUS_Clone)
    __swig_destroy__ = _itkHuangThresholdCalculatorPython.delete_itkHuangThresholdCalculatorHDUS
    cast = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDUS_cast)

    def New(*args, **kargs):
        """New() -> itkHuangThresholdCalculatorHDUS

        Create a new object of the class itkHuangThresholdCalculatorHDUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHuangThresholdCalculatorHDUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHuangThresholdCalculatorHDUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHuangThresholdCalculatorHDUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHuangThresholdCalculatorHDUS in _itkHuangThresholdCalculatorPython:
_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDUS_swigregister(itkHuangThresholdCalculatorHDUS)
itkHuangThresholdCalculatorHDUS___New_orig__ = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDUS___New_orig__
itkHuangThresholdCalculatorHDUS_cast = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHDUS_cast


def itkHuangThresholdCalculatorHFD_New():
    return itkHuangThresholdCalculatorHFD.New()

class itkHuangThresholdCalculatorHFD(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD):
    r"""


    Computes the Huang's threshold for an image.

    This calculator computes the Huang's fuzzy threshold which separates
    an image into foreground and background components. Uses Shannon's
    entropy function (one can also use Yager's entropy function) Huang
    L.-K. and Wang M.-J.J. (1995) "Image Thresholding by Minimizing  the
    Measures of Fuzziness" Pattern Recognition, 28(1): 41-51
    Reimplemented (to handle 16-bit efficiently) by Johannes Schindelin
    Jan 31, 2011

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
    __New_orig__ = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFD___New_orig__)
    Clone = _swig_new_instance_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFD_Clone)
    __swig_destroy__ = _itkHuangThresholdCalculatorPython.delete_itkHuangThresholdCalculatorHFD
    cast = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFD_cast)

    def New(*args, **kargs):
        """New() -> itkHuangThresholdCalculatorHFD

        Create a new object of the class itkHuangThresholdCalculatorHFD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHuangThresholdCalculatorHFD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHuangThresholdCalculatorHFD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHuangThresholdCalculatorHFD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHuangThresholdCalculatorHFD in _itkHuangThresholdCalculatorPython:
_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFD_swigregister(itkHuangThresholdCalculatorHFD)
itkHuangThresholdCalculatorHFD___New_orig__ = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFD___New_orig__
itkHuangThresholdCalculatorHFD_cast = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFD_cast


def itkHuangThresholdCalculatorHFF_New():
    return itkHuangThresholdCalculatorHFF.New()

class itkHuangThresholdCalculatorHFF(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    r"""


    Computes the Huang's threshold for an image.

    This calculator computes the Huang's fuzzy threshold which separates
    an image into foreground and background components. Uses Shannon's
    entropy function (one can also use Yager's entropy function) Huang
    L.-K. and Wang M.-J.J. (1995) "Image Thresholding by Minimizing  the
    Measures of Fuzziness" Pattern Recognition, 28(1): 41-51
    Reimplemented (to handle 16-bit efficiently) by Johannes Schindelin
    Jan 31, 2011

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
    __New_orig__ = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFF___New_orig__)
    Clone = _swig_new_instance_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFF_Clone)
    __swig_destroy__ = _itkHuangThresholdCalculatorPython.delete_itkHuangThresholdCalculatorHFF
    cast = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFF_cast)

    def New(*args, **kargs):
        """New() -> itkHuangThresholdCalculatorHFF

        Create a new object of the class itkHuangThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHuangThresholdCalculatorHFF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHuangThresholdCalculatorHFF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHuangThresholdCalculatorHFF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHuangThresholdCalculatorHFF in _itkHuangThresholdCalculatorPython:
_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFF_swigregister(itkHuangThresholdCalculatorHFF)
itkHuangThresholdCalculatorHFF___New_orig__ = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFF___New_orig__
itkHuangThresholdCalculatorHFF_cast = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFF_cast


def itkHuangThresholdCalculatorHFSS_New():
    return itkHuangThresholdCalculatorHFSS.New()

class itkHuangThresholdCalculatorHFSS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    r"""


    Computes the Huang's threshold for an image.

    This calculator computes the Huang's fuzzy threshold which separates
    an image into foreground and background components. Uses Shannon's
    entropy function (one can also use Yager's entropy function) Huang
    L.-K. and Wang M.-J.J. (1995) "Image Thresholding by Minimizing  the
    Measures of Fuzziness" Pattern Recognition, 28(1): 41-51
    Reimplemented (to handle 16-bit efficiently) by Johannes Schindelin
    Jan 31, 2011

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
    __New_orig__ = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFSS___New_orig__)
    Clone = _swig_new_instance_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFSS_Clone)
    __swig_destroy__ = _itkHuangThresholdCalculatorPython.delete_itkHuangThresholdCalculatorHFSS
    cast = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFSS_cast)

    def New(*args, **kargs):
        """New() -> itkHuangThresholdCalculatorHFSS

        Create a new object of the class itkHuangThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHuangThresholdCalculatorHFSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHuangThresholdCalculatorHFSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHuangThresholdCalculatorHFSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHuangThresholdCalculatorHFSS in _itkHuangThresholdCalculatorPython:
_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFSS_swigregister(itkHuangThresholdCalculatorHFSS)
itkHuangThresholdCalculatorHFSS___New_orig__ = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFSS___New_orig__
itkHuangThresholdCalculatorHFSS_cast = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFSS_cast


def itkHuangThresholdCalculatorHFUC_New():
    return itkHuangThresholdCalculatorHFUC.New()

class itkHuangThresholdCalculatorHFUC(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    r"""


    Computes the Huang's threshold for an image.

    This calculator computes the Huang's fuzzy threshold which separates
    an image into foreground and background components. Uses Shannon's
    entropy function (one can also use Yager's entropy function) Huang
    L.-K. and Wang M.-J.J. (1995) "Image Thresholding by Minimizing  the
    Measures of Fuzziness" Pattern Recognition, 28(1): 41-51
    Reimplemented (to handle 16-bit efficiently) by Johannes Schindelin
    Jan 31, 2011

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
    __New_orig__ = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFUC___New_orig__)
    Clone = _swig_new_instance_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFUC_Clone)
    __swig_destroy__ = _itkHuangThresholdCalculatorPython.delete_itkHuangThresholdCalculatorHFUC
    cast = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFUC_cast)

    def New(*args, **kargs):
        """New() -> itkHuangThresholdCalculatorHFUC

        Create a new object of the class itkHuangThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHuangThresholdCalculatorHFUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHuangThresholdCalculatorHFUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHuangThresholdCalculatorHFUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHuangThresholdCalculatorHFUC in _itkHuangThresholdCalculatorPython:
_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFUC_swigregister(itkHuangThresholdCalculatorHFUC)
itkHuangThresholdCalculatorHFUC___New_orig__ = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFUC___New_orig__
itkHuangThresholdCalculatorHFUC_cast = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFUC_cast


def itkHuangThresholdCalculatorHFUS_New():
    return itkHuangThresholdCalculatorHFUS.New()

class itkHuangThresholdCalculatorHFUS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS):
    r"""


    Computes the Huang's threshold for an image.

    This calculator computes the Huang's fuzzy threshold which separates
    an image into foreground and background components. Uses Shannon's
    entropy function (one can also use Yager's entropy function) Huang
    L.-K. and Wang M.-J.J. (1995) "Image Thresholding by Minimizing  the
    Measures of Fuzziness" Pattern Recognition, 28(1): 41-51
    Reimplemented (to handle 16-bit efficiently) by Johannes Schindelin
    Jan 31, 2011

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
    __New_orig__ = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFUS___New_orig__)
    Clone = _swig_new_instance_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFUS_Clone)
    __swig_destroy__ = _itkHuangThresholdCalculatorPython.delete_itkHuangThresholdCalculatorHFUS
    cast = _swig_new_static_method(_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFUS_cast)

    def New(*args, **kargs):
        """New() -> itkHuangThresholdCalculatorHFUS

        Create a new object of the class itkHuangThresholdCalculatorHFUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHuangThresholdCalculatorHFUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkHuangThresholdCalculatorHFUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkHuangThresholdCalculatorHFUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHuangThresholdCalculatorHFUS in _itkHuangThresholdCalculatorPython:
_itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFUS_swigregister(itkHuangThresholdCalculatorHFUS)
itkHuangThresholdCalculatorHFUS___New_orig__ = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFUS___New_orig__
itkHuangThresholdCalculatorHFUS_cast = _itkHuangThresholdCalculatorPython.itkHuangThresholdCalculatorHFUS_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def huang_threshold_calculator(*args, **kwargs):
    """Functional interface for HuangThresholdCalculator"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.HuangThresholdCalculator.New(*args, **kwargs)
    return instance.__internal_call__()

def huang_threshold_calculator_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKThresholding.HuangThresholdCalculator
    huang_threshold_calculator.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    huang_threshold_calculator.__doc__ = filter_object.__doc__




