# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DownloadButton(Component):
    """A DownloadButton component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- id (string; optional): The ID used to identify this component in Dash callbacks.
- className (string; optional): Often used with CSS to style elements with common properties.
- hidden (string; optional): Prevents rendering of given element, while keeping child elements, e.g. script elements, active.
- target (string; optional): Defines a default value which will be displayed in the element on page load."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, hidden=Component.UNDEFINED, target=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'hidden', 'target']
        self._type = 'DownloadButton'
        self._namespace = 'download_button'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'hidden', 'target']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DownloadButton, self).__init__(children=children, **args)
