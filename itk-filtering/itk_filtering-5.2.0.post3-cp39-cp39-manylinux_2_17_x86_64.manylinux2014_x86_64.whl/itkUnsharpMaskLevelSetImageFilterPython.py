# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKLevelSetsPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkUnsharpMaskLevelSetImageFilterPython
else:
    import _itkUnsharpMaskLevelSetImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkUnsharpMaskLevelSetImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkUnsharpMaskLevelSetImageFilterPython.SWIG_PyStaticMethod_New

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
import itk.itkSparseFieldFourthOrderLevelSetImageFilterPython
import itk.itkSparseFieldLevelSetImageFilterPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkFiniteDifferenceImageFilterPython
import itk.itkFiniteDifferenceFunctionPython
import itk.itkCovariantVectorPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkFixedArrayPython
import itk.itkInPlaceImageFilterAPython
import itk.itkImageToImageFilterAPython
import itk.itkImageRegionPython
import itk.itkImagePython
import itk.itkRGBAPixelPython
import itk.itkPointPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBPixelPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageToImageFilterBPython
import itk.itkLevelSetFunctionPython

def itkUnsharpMaskLevelSetImageFilterID2ID2_New():
    return itkUnsharpMaskLevelSetImageFilterID2ID2.New()

class itkUnsharpMaskLevelSetImageFilterID2ID2(itk.itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterID2ID2):
    r"""


    This class implements a detail enhancing filter by making use of the
    4th-order level set isotropic diffusion (smoothing) PDE.

    INPUT and OUTPUT This is a volume to volume filter; however, it is
    meant to process (smooth) surfaces. The input surface is an isosurface
    of the input volume. The isosurface value to be processed can be set
    by calling SetIsoSurfaceValue (default is 0). The output surface is
    the 0-isosurface of the output volume, regardless of the input
    isosurface value. To visualize the input/output surfaces to this
    filter a mesh extraction method such as marching cubes can be used.

    be used for general purpose surface processing. It is motivated by
    unsharp masking from image processing which is a way of enhancing
    detail. This filter acts much like the
    IsotropicFourthOrderLevelSetImageFilter because it first smoothes the
    normal vectors via isotropic diffusion. However, as a post-processing
    step we extrapolate from the original normals in the direction
    opposite to the new processes normals. By refitting the surface to
    these extrapolated vectors we achieve detail enhancement. This process
    is not the same as running the isotropic diffusion process in reverse.
    IMPORTANT Because this filters enhances details on the surface, it
    will also amplify post-processing. Do not use it on noisy data.
    PARAMETERS As mentioned before, the IsoSurfaceValue parameter chooses
    which isosurface of the input to process. The MaxFilterIterations
    parameter determine the number of iterations for which this filter
    will run. Since, this filter enhances detail AND noise
    MaxFilterIterations above a couple of hundred are unreasonable.
    Finally NormalProcessUnsharpWeight controls the amount of
    extrapolation (or equivalently the amount of detail enhancement). This
    value should be in the range [0.1,1] for reasonable results. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_Clone)
    GetMaxFilterIteration = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_GetMaxFilterIteration)
    SetMaxFilterIteration = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_SetMaxFilterIteration)
    __swig_destroy__ = _itkUnsharpMaskLevelSetImageFilterPython.delete_itkUnsharpMaskLevelSetImageFilterID2ID2
    cast = _swig_new_static_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkUnsharpMaskLevelSetImageFilterID2ID2

        Create a new object of the class itkUnsharpMaskLevelSetImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnsharpMaskLevelSetImageFilterID2ID2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkUnsharpMaskLevelSetImageFilterID2ID2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkUnsharpMaskLevelSetImageFilterID2ID2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkUnsharpMaskLevelSetImageFilterID2ID2 in _itkUnsharpMaskLevelSetImageFilterPython:
_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_swigregister(itkUnsharpMaskLevelSetImageFilterID2ID2)
itkUnsharpMaskLevelSetImageFilterID2ID2___New_orig__ = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2___New_orig__
itkUnsharpMaskLevelSetImageFilterID2ID2_cast = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID2ID2_cast


def itkUnsharpMaskLevelSetImageFilterID3ID3_New():
    return itkUnsharpMaskLevelSetImageFilterID3ID3.New()

class itkUnsharpMaskLevelSetImageFilterID3ID3(itk.itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterID3ID3):
    r"""


    This class implements a detail enhancing filter by making use of the
    4th-order level set isotropic diffusion (smoothing) PDE.

    INPUT and OUTPUT This is a volume to volume filter; however, it is
    meant to process (smooth) surfaces. The input surface is an isosurface
    of the input volume. The isosurface value to be processed can be set
    by calling SetIsoSurfaceValue (default is 0). The output surface is
    the 0-isosurface of the output volume, regardless of the input
    isosurface value. To visualize the input/output surfaces to this
    filter a mesh extraction method such as marching cubes can be used.

    be used for general purpose surface processing. It is motivated by
    unsharp masking from image processing which is a way of enhancing
    detail. This filter acts much like the
    IsotropicFourthOrderLevelSetImageFilter because it first smoothes the
    normal vectors via isotropic diffusion. However, as a post-processing
    step we extrapolate from the original normals in the direction
    opposite to the new processes normals. By refitting the surface to
    these extrapolated vectors we achieve detail enhancement. This process
    is not the same as running the isotropic diffusion process in reverse.
    IMPORTANT Because this filters enhances details on the surface, it
    will also amplify post-processing. Do not use it on noisy data.
    PARAMETERS As mentioned before, the IsoSurfaceValue parameter chooses
    which isosurface of the input to process. The MaxFilterIterations
    parameter determine the number of iterations for which this filter
    will run. Since, this filter enhances detail AND noise
    MaxFilterIterations above a couple of hundred are unreasonable.
    Finally NormalProcessUnsharpWeight controls the amount of
    extrapolation (or equivalently the amount of detail enhancement). This
    value should be in the range [0.1,1] for reasonable results. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_Clone)
    GetMaxFilterIteration = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_GetMaxFilterIteration)
    SetMaxFilterIteration = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_SetMaxFilterIteration)
    __swig_destroy__ = _itkUnsharpMaskLevelSetImageFilterPython.delete_itkUnsharpMaskLevelSetImageFilterID3ID3
    cast = _swig_new_static_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkUnsharpMaskLevelSetImageFilterID3ID3

        Create a new object of the class itkUnsharpMaskLevelSetImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnsharpMaskLevelSetImageFilterID3ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkUnsharpMaskLevelSetImageFilterID3ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkUnsharpMaskLevelSetImageFilterID3ID3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkUnsharpMaskLevelSetImageFilterID3ID3 in _itkUnsharpMaskLevelSetImageFilterPython:
_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_swigregister(itkUnsharpMaskLevelSetImageFilterID3ID3)
itkUnsharpMaskLevelSetImageFilterID3ID3___New_orig__ = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3___New_orig__
itkUnsharpMaskLevelSetImageFilterID3ID3_cast = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID3ID3_cast


def itkUnsharpMaskLevelSetImageFilterID4ID4_New():
    return itkUnsharpMaskLevelSetImageFilterID4ID4.New()

class itkUnsharpMaskLevelSetImageFilterID4ID4(itk.itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterID4ID4):
    r"""


    This class implements a detail enhancing filter by making use of the
    4th-order level set isotropic diffusion (smoothing) PDE.

    INPUT and OUTPUT This is a volume to volume filter; however, it is
    meant to process (smooth) surfaces. The input surface is an isosurface
    of the input volume. The isosurface value to be processed can be set
    by calling SetIsoSurfaceValue (default is 0). The output surface is
    the 0-isosurface of the output volume, regardless of the input
    isosurface value. To visualize the input/output surfaces to this
    filter a mesh extraction method such as marching cubes can be used.

    be used for general purpose surface processing. It is motivated by
    unsharp masking from image processing which is a way of enhancing
    detail. This filter acts much like the
    IsotropicFourthOrderLevelSetImageFilter because it first smoothes the
    normal vectors via isotropic diffusion. However, as a post-processing
    step we extrapolate from the original normals in the direction
    opposite to the new processes normals. By refitting the surface to
    these extrapolated vectors we achieve detail enhancement. This process
    is not the same as running the isotropic diffusion process in reverse.
    IMPORTANT Because this filters enhances details on the surface, it
    will also amplify post-processing. Do not use it on noisy data.
    PARAMETERS As mentioned before, the IsoSurfaceValue parameter chooses
    which isosurface of the input to process. The MaxFilterIterations
    parameter determine the number of iterations for which this filter
    will run. Since, this filter enhances detail AND noise
    MaxFilterIterations above a couple of hundred are unreasonable.
    Finally NormalProcessUnsharpWeight controls the amount of
    extrapolation (or equivalently the amount of detail enhancement). This
    value should be in the range [0.1,1] for reasonable results. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID4ID4___New_orig__)
    Clone = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID4ID4_Clone)
    GetMaxFilterIteration = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID4ID4_GetMaxFilterIteration)
    SetMaxFilterIteration = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID4ID4_SetMaxFilterIteration)
    __swig_destroy__ = _itkUnsharpMaskLevelSetImageFilterPython.delete_itkUnsharpMaskLevelSetImageFilterID4ID4
    cast = _swig_new_static_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID4ID4_cast)

    def New(*args, **kargs):
        """New() -> itkUnsharpMaskLevelSetImageFilterID4ID4

        Create a new object of the class itkUnsharpMaskLevelSetImageFilterID4ID4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnsharpMaskLevelSetImageFilterID4ID4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkUnsharpMaskLevelSetImageFilterID4ID4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkUnsharpMaskLevelSetImageFilterID4ID4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkUnsharpMaskLevelSetImageFilterID4ID4 in _itkUnsharpMaskLevelSetImageFilterPython:
_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID4ID4_swigregister(itkUnsharpMaskLevelSetImageFilterID4ID4)
itkUnsharpMaskLevelSetImageFilterID4ID4___New_orig__ = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID4ID4___New_orig__
itkUnsharpMaskLevelSetImageFilterID4ID4_cast = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterID4ID4_cast


def itkUnsharpMaskLevelSetImageFilterIF2IF2_New():
    return itkUnsharpMaskLevelSetImageFilterIF2IF2.New()

class itkUnsharpMaskLevelSetImageFilterIF2IF2(itk.itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterIF2IF2):
    r"""


    This class implements a detail enhancing filter by making use of the
    4th-order level set isotropic diffusion (smoothing) PDE.

    INPUT and OUTPUT This is a volume to volume filter; however, it is
    meant to process (smooth) surfaces. The input surface is an isosurface
    of the input volume. The isosurface value to be processed can be set
    by calling SetIsoSurfaceValue (default is 0). The output surface is
    the 0-isosurface of the output volume, regardless of the input
    isosurface value. To visualize the input/output surfaces to this
    filter a mesh extraction method such as marching cubes can be used.

    be used for general purpose surface processing. It is motivated by
    unsharp masking from image processing which is a way of enhancing
    detail. This filter acts much like the
    IsotropicFourthOrderLevelSetImageFilter because it first smoothes the
    normal vectors via isotropic diffusion. However, as a post-processing
    step we extrapolate from the original normals in the direction
    opposite to the new processes normals. By refitting the surface to
    these extrapolated vectors we achieve detail enhancement. This process
    is not the same as running the isotropic diffusion process in reverse.
    IMPORTANT Because this filters enhances details on the surface, it
    will also amplify post-processing. Do not use it on noisy data.
    PARAMETERS As mentioned before, the IsoSurfaceValue parameter chooses
    which isosurface of the input to process. The MaxFilterIterations
    parameter determine the number of iterations for which this filter
    will run. Since, this filter enhances detail AND noise
    MaxFilterIterations above a couple of hundred are unreasonable.
    Finally NormalProcessUnsharpWeight controls the amount of
    extrapolation (or equivalently the amount of detail enhancement). This
    value should be in the range [0.1,1] for reasonable results. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_Clone)
    GetMaxFilterIteration = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_GetMaxFilterIteration)
    SetMaxFilterIteration = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_SetMaxFilterIteration)
    __swig_destroy__ = _itkUnsharpMaskLevelSetImageFilterPython.delete_itkUnsharpMaskLevelSetImageFilterIF2IF2
    cast = _swig_new_static_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkUnsharpMaskLevelSetImageFilterIF2IF2

        Create a new object of the class itkUnsharpMaskLevelSetImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnsharpMaskLevelSetImageFilterIF2IF2.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkUnsharpMaskLevelSetImageFilterIF2IF2.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkUnsharpMaskLevelSetImageFilterIF2IF2.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkUnsharpMaskLevelSetImageFilterIF2IF2 in _itkUnsharpMaskLevelSetImageFilterPython:
_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_swigregister(itkUnsharpMaskLevelSetImageFilterIF2IF2)
itkUnsharpMaskLevelSetImageFilterIF2IF2___New_orig__ = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2___New_orig__
itkUnsharpMaskLevelSetImageFilterIF2IF2_cast = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF2IF2_cast


def itkUnsharpMaskLevelSetImageFilterIF3IF3_New():
    return itkUnsharpMaskLevelSetImageFilterIF3IF3.New()

class itkUnsharpMaskLevelSetImageFilterIF3IF3(itk.itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterIF3IF3):
    r"""


    This class implements a detail enhancing filter by making use of the
    4th-order level set isotropic diffusion (smoothing) PDE.

    INPUT and OUTPUT This is a volume to volume filter; however, it is
    meant to process (smooth) surfaces. The input surface is an isosurface
    of the input volume. The isosurface value to be processed can be set
    by calling SetIsoSurfaceValue (default is 0). The output surface is
    the 0-isosurface of the output volume, regardless of the input
    isosurface value. To visualize the input/output surfaces to this
    filter a mesh extraction method such as marching cubes can be used.

    be used for general purpose surface processing. It is motivated by
    unsharp masking from image processing which is a way of enhancing
    detail. This filter acts much like the
    IsotropicFourthOrderLevelSetImageFilter because it first smoothes the
    normal vectors via isotropic diffusion. However, as a post-processing
    step we extrapolate from the original normals in the direction
    opposite to the new processes normals. By refitting the surface to
    these extrapolated vectors we achieve detail enhancement. This process
    is not the same as running the isotropic diffusion process in reverse.
    IMPORTANT Because this filters enhances details on the surface, it
    will also amplify post-processing. Do not use it on noisy data.
    PARAMETERS As mentioned before, the IsoSurfaceValue parameter chooses
    which isosurface of the input to process. The MaxFilterIterations
    parameter determine the number of iterations for which this filter
    will run. Since, this filter enhances detail AND noise
    MaxFilterIterations above a couple of hundred are unreasonable.
    Finally NormalProcessUnsharpWeight controls the amount of
    extrapolation (or equivalently the amount of detail enhancement). This
    value should be in the range [0.1,1] for reasonable results. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_Clone)
    GetMaxFilterIteration = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_GetMaxFilterIteration)
    SetMaxFilterIteration = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_SetMaxFilterIteration)
    __swig_destroy__ = _itkUnsharpMaskLevelSetImageFilterPython.delete_itkUnsharpMaskLevelSetImageFilterIF3IF3
    cast = _swig_new_static_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkUnsharpMaskLevelSetImageFilterIF3IF3

        Create a new object of the class itkUnsharpMaskLevelSetImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnsharpMaskLevelSetImageFilterIF3IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkUnsharpMaskLevelSetImageFilterIF3IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkUnsharpMaskLevelSetImageFilterIF3IF3.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkUnsharpMaskLevelSetImageFilterIF3IF3 in _itkUnsharpMaskLevelSetImageFilterPython:
_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_swigregister(itkUnsharpMaskLevelSetImageFilterIF3IF3)
itkUnsharpMaskLevelSetImageFilterIF3IF3___New_orig__ = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3___New_orig__
itkUnsharpMaskLevelSetImageFilterIF3IF3_cast = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF3IF3_cast


def itkUnsharpMaskLevelSetImageFilterIF4IF4_New():
    return itkUnsharpMaskLevelSetImageFilterIF4IF4.New()

class itkUnsharpMaskLevelSetImageFilterIF4IF4(itk.itkSparseFieldFourthOrderLevelSetImageFilterPython.itkSparseFieldFourthOrderLevelSetImageFilterIF4IF4):
    r"""


    This class implements a detail enhancing filter by making use of the
    4th-order level set isotropic diffusion (smoothing) PDE.

    INPUT and OUTPUT This is a volume to volume filter; however, it is
    meant to process (smooth) surfaces. The input surface is an isosurface
    of the input volume. The isosurface value to be processed can be set
    by calling SetIsoSurfaceValue (default is 0). The output surface is
    the 0-isosurface of the output volume, regardless of the input
    isosurface value. To visualize the input/output surfaces to this
    filter a mesh extraction method such as marching cubes can be used.

    be used for general purpose surface processing. It is motivated by
    unsharp masking from image processing which is a way of enhancing
    detail. This filter acts much like the
    IsotropicFourthOrderLevelSetImageFilter because it first smoothes the
    normal vectors via isotropic diffusion. However, as a post-processing
    step we extrapolate from the original normals in the direction
    opposite to the new processes normals. By refitting the surface to
    these extrapolated vectors we achieve detail enhancement. This process
    is not the same as running the isotropic diffusion process in reverse.
    IMPORTANT Because this filters enhances details on the surface, it
    will also amplify post-processing. Do not use it on noisy data.
    PARAMETERS As mentioned before, the IsoSurfaceValue parameter chooses
    which isosurface of the input to process. The MaxFilterIterations
    parameter determine the number of iterations for which this filter
    will run. Since, this filter enhances detail AND noise
    MaxFilterIterations above a couple of hundred are unreasonable.
    Finally NormalProcessUnsharpWeight controls the amount of
    extrapolation (or equivalently the amount of detail enhancement). This
    value should be in the range [0.1,1] for reasonable results. 
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF4IF4___New_orig__)
    Clone = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF4IF4_Clone)
    GetMaxFilterIteration = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF4IF4_GetMaxFilterIteration)
    SetMaxFilterIteration = _swig_new_instance_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF4IF4_SetMaxFilterIteration)
    __swig_destroy__ = _itkUnsharpMaskLevelSetImageFilterPython.delete_itkUnsharpMaskLevelSetImageFilterIF4IF4
    cast = _swig_new_static_method(_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF4IF4_cast)

    def New(*args, **kargs):
        """New() -> itkUnsharpMaskLevelSetImageFilterIF4IF4

        Create a new object of the class itkUnsharpMaskLevelSetImageFilterIF4IF4 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkUnsharpMaskLevelSetImageFilterIF4IF4.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkUnsharpMaskLevelSetImageFilterIF4IF4.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkUnsharpMaskLevelSetImageFilterIF4IF4.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkUnsharpMaskLevelSetImageFilterIF4IF4 in _itkUnsharpMaskLevelSetImageFilterPython:
_itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF4IF4_swigregister(itkUnsharpMaskLevelSetImageFilterIF4IF4)
itkUnsharpMaskLevelSetImageFilterIF4IF4___New_orig__ = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF4IF4___New_orig__
itkUnsharpMaskLevelSetImageFilterIF4IF4_cast = _itkUnsharpMaskLevelSetImageFilterPython.itkUnsharpMaskLevelSetImageFilterIF4IF4_cast


from itk.support import helpers
import itk.support.types as itkt
from typing import Sequence, Tuple, Union

@helpers.accept_array_like_xarray_torch
def unsharp_mask_level_set_image_filter(*args: itkt.ImageLike,  max_filter_iteration: int=..., max_refit_iteration: int=..., max_normal_iteration: int=..., curvature_band_width: float=..., rms_change_normal_process_trigger: float=..., normal_process_type: int=..., normal_process_conductance: float=..., normal_process_unsharp_flag: bool=..., normal_process_unsharp_weight: float=..., level_set_function=..., number_of_layers: int=..., iso_surface_value: float=..., interpolate_surface_location: bool=..., difference_function=..., number_of_iterations: int=..., use_image_spacing: bool=..., maximum_rms_error: float=..., rms_change: float=..., manual_reinitialization: bool=..., is_initialized: bool=...,**kwargs)-> itkt.ImageSourceReturn:
    """Functional interface for UnsharpMaskLevelSetImageFilter"""
    import itk

    kwarg_typehints = { 'max_filter_iteration':max_filter_iteration,'max_refit_iteration':max_refit_iteration,'max_normal_iteration':max_normal_iteration,'curvature_band_width':curvature_band_width,'rms_change_normal_process_trigger':rms_change_normal_process_trigger,'normal_process_type':normal_process_type,'normal_process_conductance':normal_process_conductance,'normal_process_unsharp_flag':normal_process_unsharp_flag,'normal_process_unsharp_weight':normal_process_unsharp_weight,'level_set_function':level_set_function,'number_of_layers':number_of_layers,'iso_surface_value':iso_surface_value,'interpolate_surface_location':interpolate_surface_location,'difference_function':difference_function,'number_of_iterations':number_of_iterations,'use_image_spacing':use_image_spacing,'maximum_rms_error':maximum_rms_error,'rms_change':rms_change,'manual_reinitialization':manual_reinitialization,'is_initialized':is_initialized }
    specified_kwarg_typehints = { k:v for (k,v) in kwarg_typehints.items() if kwarg_typehints[k] is not ... }
    kwargs.update(specified_kwarg_typehints)

    instance = itk.UnsharpMaskLevelSetImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def unsharp_mask_level_set_image_filter_init_docstring():
    import itk
    from itk.support import template_class

    filter_class = itk.ITKLevelSets.UnsharpMaskLevelSetImageFilter
    unsharp_mask_level_set_image_filter.process_object = filter_class
    is_template = isinstance(filter_class, template_class.itkTemplate)
    if is_template:
        filter_object = filter_class.values()[0]
    else:
        filter_object = filter_class

    unsharp_mask_level_set_image_filter.__doc__ = filter_object.__doc__




