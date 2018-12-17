from . import _components
from ._components import *  # noqa
from ._version import __version__  # noqa

_js_dist = [
    {
        "relative_package_path": (
            "_components/dbc_custom_components.min.js"
        ),
        "namespace": "dbc_custom_components",
    }
]

_css_dist = []


for _component_name in _components.__all__:
    _component = getattr(_components, _component_name)
    _component._js_dist = _js_dist
    _component._css_dist = _css_dist
