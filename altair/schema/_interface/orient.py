# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T


class Orient(T.Enum):
    """
    One of ['horizontal', 'vertical']
    """
    def __init__(self, default_value=T.Undefined, **metadata):
        super(Orient, self).__init__(['horizontal', 'vertical'],
                                    default_value=default_value,
                                    **metadata)