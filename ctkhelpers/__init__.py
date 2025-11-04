"""ctk-helpers-py - A python library of helper widgets and functions for custom Tk GUI apps."""

import os

# fmt: off
__project__ = 'ctkhelpers'
__version__ = '0.1.0'
# fmt: on

VERSION = __project__ + "-" + __version__

from .constants import *
from .helpers import set_entry_text, set_label_text, set_image
from .style import WidgetStyleMixin
from .widgets.meter import Meter
from .widgets.jogwheel import Jogwheel
from .widgets.ctk_xyframe import CTkXYFrame
from .widgets.ctk_code_box import CTkCodeBox
from .radiobuttons import RadioButtonFrame
from .labelledwidgets import (
    LabelledComboFrame,
    LabelledSliderFrame,
    LabelledEntryFrame,
    LabelledSegmentFrame,
)
