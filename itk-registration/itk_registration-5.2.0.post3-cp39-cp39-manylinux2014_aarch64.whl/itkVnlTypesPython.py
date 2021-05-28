# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 6, 0):
    raise RuntimeError("Python 3.6 or later required")


from . import _ITKOptimizersv4Python



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkVnlTypesPython
else:
    import _itkVnlTypesPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkVnlTypesPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkVnlTypesPython.SWIG_PyStaticMethod_New

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
import itk.vnl_cost_functionPython
import itk.vnl_unary_functionPython
import itk.vnl_vectorPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_matrixPython
class vnl_nonlinear_minimizer(object):
    r"""Proxy of C++ vnl_nonlinear_minimizer class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkVnlTypesPython.delete_vnl_nonlinear_minimizer
    set_f_tolerance = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_set_f_tolerance)
    get_f_tolerance = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_get_f_tolerance)
    set_x_tolerance = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_set_x_tolerance)
    get_x_tolerance = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_get_x_tolerance)
    set_g_tolerance = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_set_g_tolerance)
    get_g_tolerance = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_get_g_tolerance)
    set_max_function_evals = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_set_max_function_evals)
    get_max_function_evals = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_get_max_function_evals)
    set_epsilon_function = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_set_epsilon_function)
    get_epsilon_function = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_get_epsilon_function)
    set_trace = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_set_trace)
    get_trace = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_get_trace)
    set_verbose = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_set_verbose)
    get_verbose = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_get_verbose)
    set_check_derivatives = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_set_check_derivatives)
    get_check_derivatives = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_get_check_derivatives)
    get_start_error = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_get_start_error)
    get_end_error = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_get_end_error)
    get_num_evaluations = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_get_num_evaluations)
    get_num_iterations = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_get_num_iterations)
    ReturnCodes_ERROR_FAILURE = _itkVnlTypesPython.vnl_nonlinear_minimizer_ReturnCodes_ERROR_FAILURE
    
    ReturnCodes_ERROR_DODGY_INPUT = _itkVnlTypesPython.vnl_nonlinear_minimizer_ReturnCodes_ERROR_DODGY_INPUT
    
    ReturnCodes_CONVERGED_FTOL = _itkVnlTypesPython.vnl_nonlinear_minimizer_ReturnCodes_CONVERGED_FTOL
    
    ReturnCodes_CONVERGED_XTOL = _itkVnlTypesPython.vnl_nonlinear_minimizer_ReturnCodes_CONVERGED_XTOL
    
    ReturnCodes_CONVERGED_XFTOL = _itkVnlTypesPython.vnl_nonlinear_minimizer_ReturnCodes_CONVERGED_XFTOL
    
    ReturnCodes_CONVERGED_GTOL = _itkVnlTypesPython.vnl_nonlinear_minimizer_ReturnCodes_CONVERGED_GTOL
    
    ReturnCodes_FAILED_TOO_MANY_ITERATIONS = _itkVnlTypesPython.vnl_nonlinear_minimizer_ReturnCodes_FAILED_TOO_MANY_ITERATIONS
    
    ReturnCodes_TOO_MANY_ITERATIONS = _itkVnlTypesPython.vnl_nonlinear_minimizer_ReturnCodes_TOO_MANY_ITERATIONS
    
    ReturnCodes_FAILED_FTOL_TOO_SMALL = _itkVnlTypesPython.vnl_nonlinear_minimizer_ReturnCodes_FAILED_FTOL_TOO_SMALL
    
    ReturnCodes_FAILED_XTOL_TOO_SMALL = _itkVnlTypesPython.vnl_nonlinear_minimizer_ReturnCodes_FAILED_XTOL_TOO_SMALL
    
    ReturnCodes_FAILED_GTOL_TOO_SMALL = _itkVnlTypesPython.vnl_nonlinear_minimizer_ReturnCodes_FAILED_GTOL_TOO_SMALL
    
    ReturnCodes_FAILED_USER_REQUEST = _itkVnlTypesPython.vnl_nonlinear_minimizer_ReturnCodes_FAILED_USER_REQUEST
    
    obj_value_reduced = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_obj_value_reduced)
    get_covariance = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_get_covariance)
    is_a = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_is_a)
    is_class = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_is_class)
    get_failure_code = _swig_new_instance_method(_itkVnlTypesPython.vnl_nonlinear_minimizer_get_failure_code)

    def __init__(self, *args):
        r"""
        __init__(self) -> vnl_nonlinear_minimizer
        __init__(self, arg0) -> vnl_nonlinear_minimizer

        Parameters
        ----------
        arg0: vnl_nonlinear_minimizer const &

        """
        _itkVnlTypesPython.vnl_nonlinear_minimizer_swiginit(self, _itkVnlTypesPython.new_vnl_nonlinear_minimizer(*args))

# Register vnl_nonlinear_minimizer in _itkVnlTypesPython:
_itkVnlTypesPython.vnl_nonlinear_minimizer_swigregister(vnl_nonlinear_minimizer)

class vnl_lbfgs(vnl_nonlinear_minimizer):
    r"""Proxy of C++ vnl_lbfgs class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    minimize = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgs_minimize)

    def __init__(self, *args):
        r"""
        __init__(self) -> vnl_lbfgs
        __init__(self, f) -> vnl_lbfgs

        Parameters
        ----------
        f: vnl_cost_function &

        __init__(self, arg0) -> vnl_lbfgs

        Parameters
        ----------
        arg0: vnl_lbfgs const &

        """
        _itkVnlTypesPython.vnl_lbfgs_swiginit(self, _itkVnlTypesPython.new_vnl_lbfgs(*args))
    __swig_destroy__ = _itkVnlTypesPython.delete_vnl_lbfgs

# Register vnl_lbfgs in _itkVnlTypesPython:
_itkVnlTypesPython.vnl_lbfgs_swigregister(vnl_lbfgs)

class vnl_lbfgsb(vnl_nonlinear_minimizer):
    r"""Proxy of C++ vnl_lbfgsb class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    minimize = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgsb_minimize)
    set_bound_selection = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgsb_set_bound_selection)
    get_bound_selection = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgsb_get_bound_selection)
    set_lower_bound = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgsb_set_lower_bound)
    get_lower_bound = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgsb_get_lower_bound)
    set_upper_bound = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgsb_set_upper_bound)
    get_upper_bound = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgsb_get_upper_bound)
    set_max_variable_metric_corrections = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgsb_set_max_variable_metric_corrections)
    get_max_variable_metric_corrections = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgsb_get_max_variable_metric_corrections)
    set_cost_function_convergence_factor = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgsb_set_cost_function_convergence_factor)
    get_cost_function_convergence_factor = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgsb_get_cost_function_convergence_factor)
    set_projected_gradient_tolerance = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgsb_set_projected_gradient_tolerance)
    get_projected_gradient_tolerance = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgsb_get_projected_gradient_tolerance)
    get_inf_norm_projected_gradient = _swig_new_instance_method(_itkVnlTypesPython.vnl_lbfgsb_get_inf_norm_projected_gradient)

    def __init__(self, *args):
        r"""
        __init__(self, f) -> vnl_lbfgsb

        Parameters
        ----------
        f: vnl_cost_function &

        __init__(self, arg0) -> vnl_lbfgsb

        Parameters
        ----------
        arg0: vnl_lbfgsb const &

        """
        _itkVnlTypesPython.vnl_lbfgsb_swiginit(self, _itkVnlTypesPython.new_vnl_lbfgsb(*args))
    __swig_destroy__ = _itkVnlTypesPython.delete_vnl_lbfgsb

# Register vnl_lbfgsb in _itkVnlTypesPython:
_itkVnlTypesPython.vnl_lbfgsb_swigregister(vnl_lbfgsb)



