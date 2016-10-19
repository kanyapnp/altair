# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject
from .aggregateop import AggregateOp
from .axis import Axis
from .bin import Bin
from .scale import Scale
from .sortfield import SortField
from .sortorder import SortOrder
from .timeunit import TimeUnit
from .type import Type


class PositionChannelDef(BaseObject):
    """Wrapper for Vega-Lite PositionChannelDef definition.
    
    Attributes
    ----------
    aggregate: AggregateOp
        Aggregation function for the field .
    axis: Union(Bool, Axis)
        
    bin: Union(Bool, Bin)
        Flag for binning a `quantitative` field, or a bin property object for binning parameters.
    field: Unicode
        Name of the field from which to pull a data value.
    scale: Scale
        
    sort: Union(SortField, SortOrder)
        
    timeUnit: TimeUnit
        Time unit for a `temporal` field .
    title: Unicode
        Title for axis or legend.
    type: Type
        The encoded field's type of measurement.
    value: Union(CFloat, Unicode, Bool)
        A constant value in visual domain.
    """
    aggregate = AggregateOp(allow_none=True, default_value=None, help="""Aggregation function for the field .""")
    axis = T.Union([T.Bool(allow_none=True, default_value=None), T.Instance(Axis, allow_none=True, default_value=None)])
    bin = T.Union([T.Bool(allow_none=True, default_value=None), T.Instance(Bin, allow_none=True, default_value=None)])
    field = T.Unicode(allow_none=True, default_value=None, help="""Name of the field from which to pull a data value.""")
    scale = T.Instance(Scale, allow_none=True, default_value=None)
    sort = T.Union([T.Instance(SortField, allow_none=True, default_value=None), SortOrder(allow_none=True, default_value=None)])
    timeUnit = TimeUnit(allow_none=True, default_value=None, help="""Time unit for a `temporal` field .""")
    title = T.Unicode(allow_none=True, default_value=None, help="""Title for axis or legend.""")
    type = Type(allow_none=True, default_value=None, help="""The encoded field's type of measurement.""")
    value = T.Union([T.CFloat(allow_none=True, default_value=None), T.Unicode(allow_none=True, default_value=None), T.Bool(allow_none=True, default_value=None)])
    
    def __init__(self, aggregate=None, axis=None, bin=None, field=None, scale=None, sort=None, timeUnit=None, title=None, type=None, value=None, **kwargs):
        kwds = dict(aggregate=aggregate, axis=axis, bin=bin, field=field, scale=scale, sort=sort, timeUnit=timeUnit, title=title, type=type, value=value)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(PositionChannelDef, self).__init__(**kwargs)