import customtkinter as ctk

from ctkhelpers import *


class WidgetStyleMixin:

    def __init__(self, **kwargs):
        self.pad_x = PAD_X
        self.pad_y = PAD_Y
        self.def_width = DEF_WIDTH
        self.label_width = DEF_WIDTH_LABEL
        self.units_width = DEF_WIDTH_UNITS
        self.frame_width = DEF_WIDTH_FRAME
        self.horz_align = ctk.LEFT
        self.title_font = TITLE_FONT
        self.def_font = None
        self.value_fmt = "%d"
        self.input_value_conversion = self.def_input_conversion
        self.output_value_conversion = self.def_output_conversion
        for k, _ in self.__dict__.items():
            if k in kwargs:
                self.__dict__[k] = kwargs.pop(k)
        return kwargs

    def def_input_conversion(self, value):
        return value

    def def_output_conversion(self, value):
        return value

# grid = [
#     [w1, w2, w3],
#     [w4],
#     [[w5, w6, w7], w8, w9],
# ]
# def assign_grid(frame, grid):
#     n_rows = len(grid)
#     n_cols = 0
#     for row in grid:
#         n_cols = max(n_cols, len(row))
#     for i, row in enumerate(grid):
#         for j, col in enumerate(row):
#             col.grid(row=i, column=j, )

#  self.title_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
#         self.address_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
#         self.parcel_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
#         self.service_frame.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
#         self.line_items_title.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
#         self.line_items.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")