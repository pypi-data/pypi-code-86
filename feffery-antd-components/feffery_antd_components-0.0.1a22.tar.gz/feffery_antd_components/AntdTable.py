# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdTable(Component):
    """An AntdTable component.


Keyword arguments:

- id (string; optional)

- bordered (boolean; default False)

- className (string; optional)

- columns (list of dicts; optional)

    `columns` is a list of dicts with keys:

    - align (string; optional)

    - dataIndex (string; required)

    - editable (boolean; optional)

    - ellipsis (boolean | number | string | dict | list; optional)

    - fixed (string; optional)

    - render (boolean | number | string | dict | list; optional)

    - renderOptions (dict; optional)

        `renderOptions` is a dict with keys:

        - renderLinkText (string; optional)

        - renderType (string; optional)

    - sorter (boolean | number | string | dict | list; optional)

    - title (string; required)

    - width (number | string; optional)

- currentData (list; optional)

- data (list of dicts; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- maxHeight (number; optional)

- pagination (dict; optional)

    `pagination` is a dict with keys:

    - current (number; optional)

    - pageSize (number; optional)

    - pageSizeOptions (list of numbers; optional)

    - position (string; optional)

    - showQuickJumper (boolean; optional)

    - showTotalPrefix (string; optional)

    - showTotalSuffix (string; optional)

- recentlyChangedRow (dict; optional)

- sortOptions (dict; default {    sortDataIndexes: []})

    `sortOptions` is a dict with keys:

    - multiple (boolean; optional)

    - sortDataIndexes (list of strings; optional)

- style (dict; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, columns=Component.UNDEFINED, data=Component.UNDEFINED, sortOptions=Component.UNDEFINED, pagination=Component.UNDEFINED, bordered=Component.UNDEFINED, maxHeight=Component.UNDEFINED, currentData=Component.UNDEFINED, recentlyChangedRow=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'bordered', 'className', 'columns', 'currentData', 'data', 'loading_state', 'maxHeight', 'pagination', 'recentlyChangedRow', 'sortOptions', 'style']
        self._type = 'AntdTable'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'bordered', 'className', 'columns', 'currentData', 'data', 'loading_state', 'maxHeight', 'pagination', 'recentlyChangedRow', 'sortOptions', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdTable, self).__init__(**args)
