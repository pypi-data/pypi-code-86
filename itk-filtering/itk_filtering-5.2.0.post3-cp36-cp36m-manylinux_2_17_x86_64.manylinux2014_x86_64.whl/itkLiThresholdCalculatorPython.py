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
    from . import _itkLiThresholdCalculatorPython
else:
    import _itkLiThresholdCalculatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLiThresholdCalculatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLiThresholdCalculatorPython.SWIG_PyStaticMethod_New

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
import itk.itkVectorPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_matrixPython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.itkRGBAPixelPython
import itk.itkCovariantVectorPython
import itk.ITKCommonBasePython
import itk.itkArrayPython
import itk.itkRGBPixelPython
import itk.itkHistogramPython
import itk.itkSamplePython

def itkLiThresholdCalculatorHDD_New():
    return itkLiThresholdCalculatorHDD.New()

class itkLiThresholdCalculatorHDD(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDD):
    r"""


    Computes the Li threshold for an image. Aka intermeans.

    Implements Li's Minimum Cross Entropy thresholding method This
    implementation is based on the iterative version (Ref. 2) of the
    algorithm. 1) Li C.H. and Lee C.K. (1993) "Minimum Cross Entropy
    Thresholding" Pattern Recognition, 26(4): 617-625 2) Li C.H. and Tam
    P.K.S. (1998) "An Iterative Algorithm for Minimum     Cross Entropy
    Thresholding"Pattern Recognition Letters, 18(8): 771-776 3) Sezgin M.
    and Sankur B. (2004) "Survey over Image Thresholding     Techniques
    and Quantitative Performance Evaluation" Journal of Electronic
    Imaging, 13(1): 146-165http://citeseer.ist.psu.edu/sezgin04survey.html

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
    __New_orig__ = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDD___New_orig__)
    Clone = _swig_new_instance_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDD_Clone)
    __swig_destroy__ = _itkLiThresholdCalculatorPython.delete_itkLiThresholdCalculatorHDD
    cast = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDD_cast)

    def New(*args, **kargs):
        """New() -> itkLiThresholdCalculatorHDD

        Create a new object of the class itkLiThresholdCalculatorHDD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLiThresholdCalculatorHDD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLiThresholdCalculatorHDD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLiThresholdCalculatorHDD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLiThresholdCalculatorHDD in _itkLiThresholdCalculatorPython:
_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDD_swigregister(itkLiThresholdCalculatorHDD)
itkLiThresholdCalculatorHDD___New_orig__ = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDD___New_orig__
itkLiThresholdCalculatorHDD_cast = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDD_cast


def itkLiThresholdCalculatorHDF_New():
    return itkLiThresholdCalculatorHDF.New()

class itkLiThresholdCalculatorHDF(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDF):
    r"""


    Computes the Li threshold for an image. Aka intermeans.

    Implements Li's Minimum Cross Entropy thresholding method This
    implementation is based on the iterative version (Ref. 2) of the
    algorithm. 1) Li C.H. and Lee C.K. (1993) "Minimum Cross Entropy
    Thresholding" Pattern Recognition, 26(4): 617-625 2) Li C.H. and Tam
    P.K.S. (1998) "An Iterative Algorithm for Minimum     Cross Entropy
    Thresholding"Pattern Recognition Letters, 18(8): 771-776 3) Sezgin M.
    and Sankur B. (2004) "Survey over Image Thresholding     Techniques
    and Quantitative Performance Evaluation" Journal of Electronic
    Imaging, 13(1): 146-165http://citeseer.ist.psu.edu/sezgin04survey.html

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
    __New_orig__ = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDF___New_orig__)
    Clone = _swig_new_instance_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDF_Clone)
    __swig_destroy__ = _itkLiThresholdCalculatorPython.delete_itkLiThresholdCalculatorHDF
    cast = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDF_cast)

    def New(*args, **kargs):
        """New() -> itkLiThresholdCalculatorHDF

        Create a new object of the class itkLiThresholdCalculatorHDF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLiThresholdCalculatorHDF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLiThresholdCalculatorHDF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLiThresholdCalculatorHDF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLiThresholdCalculatorHDF in _itkLiThresholdCalculatorPython:
_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDF_swigregister(itkLiThresholdCalculatorHDF)
itkLiThresholdCalculatorHDF___New_orig__ = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDF___New_orig__
itkLiThresholdCalculatorHDF_cast = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDF_cast


def itkLiThresholdCalculatorHDSS_New():
    return itkLiThresholdCalculatorHDSS.New()

class itkLiThresholdCalculatorHDSS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDSS):
    r"""


    Computes the Li threshold for an image. Aka intermeans.

    Implements Li's Minimum Cross Entropy thresholding method This
    implementation is based on the iterative version (Ref. 2) of the
    algorithm. 1) Li C.H. and Lee C.K. (1993) "Minimum Cross Entropy
    Thresholding" Pattern Recognition, 26(4): 617-625 2) Li C.H. and Tam
    P.K.S. (1998) "An Iterative Algorithm for Minimum     Cross Entropy
    Thresholding"Pattern Recognition Letters, 18(8): 771-776 3) Sezgin M.
    and Sankur B. (2004) "Survey over Image Thresholding     Techniques
    and Quantitative Performance Evaluation" Journal of Electronic
    Imaging, 13(1): 146-165http://citeseer.ist.psu.edu/sezgin04survey.html

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
    __New_orig__ = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDSS___New_orig__)
    Clone = _swig_new_instance_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDSS_Clone)
    __swig_destroy__ = _itkLiThresholdCalculatorPython.delete_itkLiThresholdCalculatorHDSS
    cast = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDSS_cast)

    def New(*args, **kargs):
        """New() -> itkLiThresholdCalculatorHDSS

        Create a new object of the class itkLiThresholdCalculatorHDSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLiThresholdCalculatorHDSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLiThresholdCalculatorHDSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLiThresholdCalculatorHDSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLiThresholdCalculatorHDSS in _itkLiThresholdCalculatorPython:
_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDSS_swigregister(itkLiThresholdCalculatorHDSS)
itkLiThresholdCalculatorHDSS___New_orig__ = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDSS___New_orig__
itkLiThresholdCalculatorHDSS_cast = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDSS_cast


def itkLiThresholdCalculatorHDUC_New():
    return itkLiThresholdCalculatorHDUC.New()

class itkLiThresholdCalculatorHDUC(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUC):
    r"""


    Computes the Li threshold for an image. Aka intermeans.

    Implements Li's Minimum Cross Entropy thresholding method This
    implementation is based on the iterative version (Ref. 2) of the
    algorithm. 1) Li C.H. and Lee C.K. (1993) "Minimum Cross Entropy
    Thresholding" Pattern Recognition, 26(4): 617-625 2) Li C.H. and Tam
    P.K.S. (1998) "An Iterative Algorithm for Minimum     Cross Entropy
    Thresholding"Pattern Recognition Letters, 18(8): 771-776 3) Sezgin M.
    and Sankur B. (2004) "Survey over Image Thresholding     Techniques
    and Quantitative Performance Evaluation" Journal of Electronic
    Imaging, 13(1): 146-165http://citeseer.ist.psu.edu/sezgin04survey.html

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
    __New_orig__ = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDUC___New_orig__)
    Clone = _swig_new_instance_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDUC_Clone)
    __swig_destroy__ = _itkLiThresholdCalculatorPython.delete_itkLiThresholdCalculatorHDUC
    cast = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDUC_cast)

    def New(*args, **kargs):
        """New() -> itkLiThresholdCalculatorHDUC

        Create a new object of the class itkLiThresholdCalculatorHDUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLiThresholdCalculatorHDUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLiThresholdCalculatorHDUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLiThresholdCalculatorHDUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLiThresholdCalculatorHDUC in _itkLiThresholdCalculatorPython:
_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDUC_swigregister(itkLiThresholdCalculatorHDUC)
itkLiThresholdCalculatorHDUC___New_orig__ = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDUC___New_orig__
itkLiThresholdCalculatorHDUC_cast = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDUC_cast


def itkLiThresholdCalculatorHDUS_New():
    return itkLiThresholdCalculatorHDUS.New()

class itkLiThresholdCalculatorHDUS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHDUS):
    r"""


    Computes the Li threshold for an image. Aka intermeans.

    Implements Li's Minimum Cross Entropy thresholding method This
    implementation is based on the iterative version (Ref. 2) of the
    algorithm. 1) Li C.H. and Lee C.K. (1993) "Minimum Cross Entropy
    Thresholding" Pattern Recognition, 26(4): 617-625 2) Li C.H. and Tam
    P.K.S. (1998) "An Iterative Algorithm for Minimum     Cross Entropy
    Thresholding"Pattern Recognition Letters, 18(8): 771-776 3) Sezgin M.
    and Sankur B. (2004) "Survey over Image Thresholding     Techniques
    and Quantitative Performance Evaluation" Journal of Electronic
    Imaging, 13(1): 146-165http://citeseer.ist.psu.edu/sezgin04survey.html

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
    __New_orig__ = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDUS___New_orig__)
    Clone = _swig_new_instance_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDUS_Clone)
    __swig_destroy__ = _itkLiThresholdCalculatorPython.delete_itkLiThresholdCalculatorHDUS
    cast = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDUS_cast)

    def New(*args, **kargs):
        """New() -> itkLiThresholdCalculatorHDUS

        Create a new object of the class itkLiThresholdCalculatorHDUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLiThresholdCalculatorHDUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLiThresholdCalculatorHDUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLiThresholdCalculatorHDUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLiThresholdCalculatorHDUS in _itkLiThresholdCalculatorPython:
_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDUS_swigregister(itkLiThresholdCalculatorHDUS)
itkLiThresholdCalculatorHDUS___New_orig__ = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDUS___New_orig__
itkLiThresholdCalculatorHDUS_cast = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHDUS_cast


def itkLiThresholdCalculatorHFD_New():
    return itkLiThresholdCalculatorHFD.New()

class itkLiThresholdCalculatorHFD(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFD):
    r"""


    Computes the Li threshold for an image. Aka intermeans.

    Implements Li's Minimum Cross Entropy thresholding method This
    implementation is based on the iterative version (Ref. 2) of the
    algorithm. 1) Li C.H. and Lee C.K. (1993) "Minimum Cross Entropy
    Thresholding" Pattern Recognition, 26(4): 617-625 2) Li C.H. and Tam
    P.K.S. (1998) "An Iterative Algorithm for Minimum     Cross Entropy
    Thresholding"Pattern Recognition Letters, 18(8): 771-776 3) Sezgin M.
    and Sankur B. (2004) "Survey over Image Thresholding     Techniques
    and Quantitative Performance Evaluation" Journal of Electronic
    Imaging, 13(1): 146-165http://citeseer.ist.psu.edu/sezgin04survey.html

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
    __New_orig__ = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFD___New_orig__)
    Clone = _swig_new_instance_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFD_Clone)
    __swig_destroy__ = _itkLiThresholdCalculatorPython.delete_itkLiThresholdCalculatorHFD
    cast = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFD_cast)

    def New(*args, **kargs):
        """New() -> itkLiThresholdCalculatorHFD

        Create a new object of the class itkLiThresholdCalculatorHFD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLiThresholdCalculatorHFD.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLiThresholdCalculatorHFD.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLiThresholdCalculatorHFD.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLiThresholdCalculatorHFD in _itkLiThresholdCalculatorPython:
_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFD_swigregister(itkLiThresholdCalculatorHFD)
itkLiThresholdCalculatorHFD___New_orig__ = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFD___New_orig__
itkLiThresholdCalculatorHFD_cast = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFD_cast


def itkLiThresholdCalculatorHFF_New():
    return itkLiThresholdCalculatorHFF.New()

class itkLiThresholdCalculatorHFF(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFF):
    r"""


    Computes the Li threshold for an image. Aka intermeans.

    Implements Li's Minimum Cross Entropy thresholding method This
    implementation is based on the iterative version (Ref. 2) of the
    algorithm. 1) Li C.H. and Lee C.K. (1993) "Minimum Cross Entropy
    Thresholding" Pattern Recognition, 26(4): 617-625 2) Li C.H. and Tam
    P.K.S. (1998) "An Iterative Algorithm for Minimum     Cross Entropy
    Thresholding"Pattern Recognition Letters, 18(8): 771-776 3) Sezgin M.
    and Sankur B. (2004) "Survey over Image Thresholding     Techniques
    and Quantitative Performance Evaluation" Journal of Electronic
    Imaging, 13(1): 146-165http://citeseer.ist.psu.edu/sezgin04survey.html

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
    __New_orig__ = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFF___New_orig__)
    Clone = _swig_new_instance_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFF_Clone)
    __swig_destroy__ = _itkLiThresholdCalculatorPython.delete_itkLiThresholdCalculatorHFF
    cast = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFF_cast)

    def New(*args, **kargs):
        """New() -> itkLiThresholdCalculatorHFF

        Create a new object of the class itkLiThresholdCalculatorHFF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLiThresholdCalculatorHFF.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLiThresholdCalculatorHFF.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLiThresholdCalculatorHFF.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLiThresholdCalculatorHFF in _itkLiThresholdCalculatorPython:
_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFF_swigregister(itkLiThresholdCalculatorHFF)
itkLiThresholdCalculatorHFF___New_orig__ = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFF___New_orig__
itkLiThresholdCalculatorHFF_cast = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFF_cast


def itkLiThresholdCalculatorHFSS_New():
    return itkLiThresholdCalculatorHFSS.New()

class itkLiThresholdCalculatorHFSS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFSS):
    r"""


    Computes the Li threshold for an image. Aka intermeans.

    Implements Li's Minimum Cross Entropy thresholding method This
    implementation is based on the iterative version (Ref. 2) of the
    algorithm. 1) Li C.H. and Lee C.K. (1993) "Minimum Cross Entropy
    Thresholding" Pattern Recognition, 26(4): 617-625 2) Li C.H. and Tam
    P.K.S. (1998) "An Iterative Algorithm for Minimum     Cross Entropy
    Thresholding"Pattern Recognition Letters, 18(8): 771-776 3) Sezgin M.
    and Sankur B. (2004) "Survey over Image Thresholding     Techniques
    and Quantitative Performance Evaluation" Journal of Electronic
    Imaging, 13(1): 146-165http://citeseer.ist.psu.edu/sezgin04survey.html

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
    __New_orig__ = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFSS___New_orig__)
    Clone = _swig_new_instance_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFSS_Clone)
    __swig_destroy__ = _itkLiThresholdCalculatorPython.delete_itkLiThresholdCalculatorHFSS
    cast = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFSS_cast)

    def New(*args, **kargs):
        """New() -> itkLiThresholdCalculatorHFSS

        Create a new object of the class itkLiThresholdCalculatorHFSS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLiThresholdCalculatorHFSS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLiThresholdCalculatorHFSS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLiThresholdCalculatorHFSS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLiThresholdCalculatorHFSS in _itkLiThresholdCalculatorPython:
_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFSS_swigregister(itkLiThresholdCalculatorHFSS)
itkLiThresholdCalculatorHFSS___New_orig__ = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFSS___New_orig__
itkLiThresholdCalculatorHFSS_cast = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFSS_cast


def itkLiThresholdCalculatorHFUC_New():
    return itkLiThresholdCalculatorHFUC.New()

class itkLiThresholdCalculatorHFUC(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUC):
    r"""


    Computes the Li threshold for an image. Aka intermeans.

    Implements Li's Minimum Cross Entropy thresholding method This
    implementation is based on the iterative version (Ref. 2) of the
    algorithm. 1) Li C.H. and Lee C.K. (1993) "Minimum Cross Entropy
    Thresholding" Pattern Recognition, 26(4): 617-625 2) Li C.H. and Tam
    P.K.S. (1998) "An Iterative Algorithm for Minimum     Cross Entropy
    Thresholding"Pattern Recognition Letters, 18(8): 771-776 3) Sezgin M.
    and Sankur B. (2004) "Survey over Image Thresholding     Techniques
    and Quantitative Performance Evaluation" Journal of Electronic
    Imaging, 13(1): 146-165http://citeseer.ist.psu.edu/sezgin04survey.html

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
    __New_orig__ = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFUC___New_orig__)
    Clone = _swig_new_instance_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFUC_Clone)
    __swig_destroy__ = _itkLiThresholdCalculatorPython.delete_itkLiThresholdCalculatorHFUC
    cast = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFUC_cast)

    def New(*args, **kargs):
        """New() -> itkLiThresholdCalculatorHFUC

        Create a new object of the class itkLiThresholdCalculatorHFUC and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLiThresholdCalculatorHFUC.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLiThresholdCalculatorHFUC.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLiThresholdCalculatorHFUC.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLiThresholdCalculatorHFUC in _itkLiThresholdCalculatorPython:
_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFUC_swigregister(itkLiThresholdCalculatorHFUC)
itkLiThresholdCalculatorHFUC___New_orig__ = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFUC___New_orig__
itkLiThresholdCalculatorHFUC_cast = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFUC_cast


def itkLiThresholdCalculatorHFUS_New():
    return itkLiThresholdCalculatorHFUS.New()

class itkLiThresholdCalculatorHFUS(itk.itkHistogramThresholdCalculatorPython.itkHistogramThresholdCalculatorHFUS):
    r"""


    Computes the Li threshold for an image. Aka intermeans.

    Implements Li's Minimum Cross Entropy thresholding method This
    implementation is based on the iterative version (Ref. 2) of the
    algorithm. 1) Li C.H. and Lee C.K. (1993) "Minimum Cross Entropy
    Thresholding" Pattern Recognition, 26(4): 617-625 2) Li C.H. and Tam
    P.K.S. (1998) "An Iterative Algorithm for Minimum     Cross Entropy
    Thresholding"Pattern Recognition Letters, 18(8): 771-776 3) Sezgin M.
    and Sankur B. (2004) "Survey over Image Thresholding     Techniques
    and Quantitative Performance Evaluation" Journal of Electronic
    Imaging, 13(1): 146-165http://citeseer.ist.psu.edu/sezgin04survey.html

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
    __New_orig__ = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFUS___New_orig__)
    Clone = _swig_new_instance_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFUS_Clone)
    __swig_destroy__ = _itkLiThresholdCalculatorPython.delete_itkLiThresholdCalculatorHFUS
    cast = _swig_new_static_method(_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFUS_cast)

    def New(*args, **kargs):
        """New() -> itkLiThresholdCalculatorHFUS

        Create a new object of the class itkLiThresholdCalculatorHFUS and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLiThresholdCalculatorHFUS.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLiThresholdCalculatorHFUS.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLiThresholdCalculatorHFUS.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLiThresholdCalculatorHFUS in _itkLiThresholdCalculatorPython:
_itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFUS_swigregister(itkLiThresholdCalculatorHFUS)
itkLiThresholdCalculatorHFUS___New_orig__ = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFUS___New_orig__
itkLiThresholdCalculatorHFUS_cast = _itkLiThresholdCalculatorPython.itkLiThresholdCalculatorHFUS_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def li_threshold_calculator(*args, **kwargs):
    """Functional interface for LiThresholdCalculator"""
    import itk

    kwarg_typehints = {  }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.LiThresholdCalculator.New(*args, **kwargs)
    return instance.__internal_call__()

def li_threshold_calculator_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKThresholding.LiThresholdCalculator
    li_threshold_calculator.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    li_threshold_calculator.__doc__ = filter_object.__doc__




