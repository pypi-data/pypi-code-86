# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKCommonPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkDiffusionTensor3DPython
else:
    import _itkDiffusionTensor3DPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkDiffusionTensor3DPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkDiffusionTensor3DPython.SWIG_PyStaticMethod_New

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
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkCovariantVectorPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.itkPointPython
class itkDiffusionTensor3DD(itk.itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3):
    r"""


    Represent a diffusion tensor as used in DTI images.

    This class implements a 3D symmetric tensor as it is used for
    representing diffusion of water molecules in Diffusion Tensor Images.

    This class derives from the SymmetricSecondRankTensor, inheriting most
    of the Tensor-related behavior. At this level we add the methods that
    are specific to 3D and that are closely related to the concept of
    diffusion.

    Jeffrey Duda from School of Engineering at University of Pennsylvania

    Torsten Rohlfing from SRI International Neuroscience Program.  This
    class was mostly based on files that Jeffrey Duda, Torsten Rohlfing
    and Martin Styner contributed to the ITK users list during a
    discussion on support for DiffusionTensorImages. A discussion on the
    design of this class can be found in the WIKI pages of NAMIC:

    http://www.na-mic.org/Wiki/index.php/NAMIC_Wiki:DTI:ITK-
    DiffusionTensorPixelType

    This work is part of the National Alliance for Medical Image Computing
    (NAMIC), funded by the National Institutes of Health through the NIH
    Roadmap for Medical Research, Grant U54 EB005149. Information on the
    National Centers for Biomedical Computing can be obtained
    fromhttp://commonfund.nih.gov/bioinformatics.

    Contributions by Torsten Rohlfing were funded by the following NIH
    grants  Alcohol, HIV and the Brain, NIAAA AA12999, PI: A. Pfefferbaum

    Normal Aging of Brain Structure and Function NIA AG 17919, PI: E.V.
    Sullivan.

    References E. R. Melhem, S. Mori, G. Mukundan, M. A. Kraut, M. G.
    Pomper, and P. C. M. van Zijl, "Diffusion tensor MR imaging of the
    brain and white matter tractography," Am. J. Roentgenol., vol. 178,
    pp. 3-16, 2002.

    See:   SymmetricSecondRankTensor 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    GetTrace = _swig_new_instance_method(_itkDiffusionTensor3DPython.itkDiffusionTensor3DD_GetTrace)
    GetFractionalAnisotropy = _swig_new_instance_method(_itkDiffusionTensor3DPython.itkDiffusionTensor3DD_GetFractionalAnisotropy)
    GetRelativeAnisotropy = _swig_new_instance_method(_itkDiffusionTensor3DPython.itkDiffusionTensor3DD_GetRelativeAnisotropy)
    GetInnerScalarProduct = _swig_new_instance_method(_itkDiffusionTensor3DPython.itkDiffusionTensor3DD_GetInnerScalarProduct)

    def __init__(self, *args):
        r"""
        __init__(self) -> itkDiffusionTensor3DD
        __init__(self, r) -> itkDiffusionTensor3DD

        Parameters
        ----------
        r: itkSymmetricSecondRankTensorD3 const &

        __init__(self, r) -> itkDiffusionTensor3DD

        Parameters
        ----------
        r: double const &

        __init__(self, r) -> itkDiffusionTensor3DD

        Parameters
        ----------
        r: double const *

        __init__(self, arg0) -> itkDiffusionTensor3DD

        Parameters
        ----------
        arg0: itkDiffusionTensor3DD const &



        Represent a diffusion tensor as used in DTI images.

        This class implements a 3D symmetric tensor as it is used for
        representing diffusion of water molecules in Diffusion Tensor Images.

        This class derives from the SymmetricSecondRankTensor, inheriting most
        of the Tensor-related behavior. At this level we add the methods that
        are specific to 3D and that are closely related to the concept of
        diffusion.

        Jeffrey Duda from School of Engineering at University of Pennsylvania

        Torsten Rohlfing from SRI International Neuroscience Program.  This
        class was mostly based on files that Jeffrey Duda, Torsten Rohlfing
        and Martin Styner contributed to the ITK users list during a
        discussion on support for DiffusionTensorImages. A discussion on the
        design of this class can be found in the WIKI pages of NAMIC:

        http://www.na-mic.org/Wiki/index.php/NAMIC_Wiki:DTI:ITK-
        DiffusionTensorPixelType

        This work is part of the National Alliance for Medical Image Computing
        (NAMIC), funded by the National Institutes of Health through the NIH
        Roadmap for Medical Research, Grant U54 EB005149. Information on the
        National Centers for Biomedical Computing can be obtained
        fromhttp://commonfund.nih.gov/bioinformatics.

        Contributions by Torsten Rohlfing were funded by the following NIH
        grants  Alcohol, HIV and the Brain, NIAAA AA12999, PI: A. Pfefferbaum

        Normal Aging of Brain Structure and Function NIA AG 17919, PI: E.V.
        Sullivan.

        References E. R. Melhem, S. Mori, G. Mukundan, M. A. Kraut, M. G.
        Pomper, and P. C. M. van Zijl, "Diffusion tensor MR imaging of the
        brain and white matter tractography," Am. J. Roentgenol., vol. 178,
        pp. 3-16, 2002.

        See:   SymmetricSecondRankTensor 
        """
        _itkDiffusionTensor3DPython.itkDiffusionTensor3DD_swiginit(self, _itkDiffusionTensor3DPython.new_itkDiffusionTensor3DD(*args))
    __swig_destroy__ = _itkDiffusionTensor3DPython.delete_itkDiffusionTensor3DD

# Register itkDiffusionTensor3DD in _itkDiffusionTensor3DPython:
_itkDiffusionTensor3DPython.itkDiffusionTensor3DD_swigregister(itkDiffusionTensor3DD)

class itkDiffusionTensor3DF(itk.itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3):
    r"""


    Represent a diffusion tensor as used in DTI images.

    This class implements a 3D symmetric tensor as it is used for
    representing diffusion of water molecules in Diffusion Tensor Images.

    This class derives from the SymmetricSecondRankTensor, inheriting most
    of the Tensor-related behavior. At this level we add the methods that
    are specific to 3D and that are closely related to the concept of
    diffusion.

    Jeffrey Duda from School of Engineering at University of Pennsylvania

    Torsten Rohlfing from SRI International Neuroscience Program.  This
    class was mostly based on files that Jeffrey Duda, Torsten Rohlfing
    and Martin Styner contributed to the ITK users list during a
    discussion on support for DiffusionTensorImages. A discussion on the
    design of this class can be found in the WIKI pages of NAMIC:

    http://www.na-mic.org/Wiki/index.php/NAMIC_Wiki:DTI:ITK-
    DiffusionTensorPixelType

    This work is part of the National Alliance for Medical Image Computing
    (NAMIC), funded by the National Institutes of Health through the NIH
    Roadmap for Medical Research, Grant U54 EB005149. Information on the
    National Centers for Biomedical Computing can be obtained
    fromhttp://commonfund.nih.gov/bioinformatics.

    Contributions by Torsten Rohlfing were funded by the following NIH
    grants  Alcohol, HIV and the Brain, NIAAA AA12999, PI: A. Pfefferbaum

    Normal Aging of Brain Structure and Function NIA AG 17919, PI: E.V.
    Sullivan.

    References E. R. Melhem, S. Mori, G. Mukundan, M. A. Kraut, M. G.
    Pomper, and P. C. M. van Zijl, "Diffusion tensor MR imaging of the
    brain and white matter tractography," Am. J. Roentgenol., vol. 178,
    pp. 3-16, 2002.

    See:   SymmetricSecondRankTensor 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    GetTrace = _swig_new_instance_method(_itkDiffusionTensor3DPython.itkDiffusionTensor3DF_GetTrace)
    GetFractionalAnisotropy = _swig_new_instance_method(_itkDiffusionTensor3DPython.itkDiffusionTensor3DF_GetFractionalAnisotropy)
    GetRelativeAnisotropy = _swig_new_instance_method(_itkDiffusionTensor3DPython.itkDiffusionTensor3DF_GetRelativeAnisotropy)
    GetInnerScalarProduct = _swig_new_instance_method(_itkDiffusionTensor3DPython.itkDiffusionTensor3DF_GetInnerScalarProduct)

    def __init__(self, *args):
        r"""
        __init__(self) -> itkDiffusionTensor3DF
        __init__(self, r) -> itkDiffusionTensor3DF

        Parameters
        ----------
        r: itkSymmetricSecondRankTensorF3 const &

        __init__(self, r) -> itkDiffusionTensor3DF

        Parameters
        ----------
        r: float const &

        __init__(self, r) -> itkDiffusionTensor3DF

        Parameters
        ----------
        r: float const *

        __init__(self, arg0) -> itkDiffusionTensor3DF

        Parameters
        ----------
        arg0: itkDiffusionTensor3DF const &



        Represent a diffusion tensor as used in DTI images.

        This class implements a 3D symmetric tensor as it is used for
        representing diffusion of water molecules in Diffusion Tensor Images.

        This class derives from the SymmetricSecondRankTensor, inheriting most
        of the Tensor-related behavior. At this level we add the methods that
        are specific to 3D and that are closely related to the concept of
        diffusion.

        Jeffrey Duda from School of Engineering at University of Pennsylvania

        Torsten Rohlfing from SRI International Neuroscience Program.  This
        class was mostly based on files that Jeffrey Duda, Torsten Rohlfing
        and Martin Styner contributed to the ITK users list during a
        discussion on support for DiffusionTensorImages. A discussion on the
        design of this class can be found in the WIKI pages of NAMIC:

        http://www.na-mic.org/Wiki/index.php/NAMIC_Wiki:DTI:ITK-
        DiffusionTensorPixelType

        This work is part of the National Alliance for Medical Image Computing
        (NAMIC), funded by the National Institutes of Health through the NIH
        Roadmap for Medical Research, Grant U54 EB005149. Information on the
        National Centers for Biomedical Computing can be obtained
        fromhttp://commonfund.nih.gov/bioinformatics.

        Contributions by Torsten Rohlfing were funded by the following NIH
        grants  Alcohol, HIV and the Brain, NIAAA AA12999, PI: A. Pfefferbaum

        Normal Aging of Brain Structure and Function NIA AG 17919, PI: E.V.
        Sullivan.

        References E. R. Melhem, S. Mori, G. Mukundan, M. A. Kraut, M. G.
        Pomper, and P. C. M. van Zijl, "Diffusion tensor MR imaging of the
        brain and white matter tractography," Am. J. Roentgenol., vol. 178,
        pp. 3-16, 2002.

        See:   SymmetricSecondRankTensor 
        """
        _itkDiffusionTensor3DPython.itkDiffusionTensor3DF_swiginit(self, _itkDiffusionTensor3DPython.new_itkDiffusionTensor3DF(*args))
    __swig_destroy__ = _itkDiffusionTensor3DPython.delete_itkDiffusionTensor3DF

# Register itkDiffusionTensor3DF in _itkDiffusionTensor3DPython:
_itkDiffusionTensor3DPython.itkDiffusionTensor3DF_swigregister(itkDiffusionTensor3DF)



