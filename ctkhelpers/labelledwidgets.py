import customtkinter as ctk

from ctkhelpers import *


class LabelledComboFrame(ctk.CTkFrame, WidgetStyleMixin):

    def __init__(
        self, master, label, values, callback=None, default_choice=None, **kwargs
    ):
        kwargs = WidgetStyleMixin.__init__(self, **kwargs)
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        self.label = ctk.CTkLabel(
            master=self, width=self.label_width, text=label, justify=self.horz_align
        )
        self.combo = ctk.CTkComboBox(master=self, values=values, command=callback)

        self.label.grid(row=0, column=0, pady=self.pad_y, padx=self.pad_x)
        self.combo.grid(row=0, column=1, pady=self.pad_y, padx=self.pad_x)

        if len(values) > 0:
            if default_choice is not None:
                self.combo.set(default_choice)
            else:
                self.combo.set(values[0])

    def choice(self):
        return self.combo.get()

    def set_choice(self, value):
        self.combo.set(value)


class LabelledSliderFrame(ctk.CTkFrame, WidgetStyleMixin):

    def __init__(
        self,
        master,
        label,
        callback=None,
        min_val=0,
        max_val=100,
        default_val=None,
        **kwargs
    ):
        kwargs = WidgetStyleMixin.__init__(self, **kwargs)
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)

        self.label = ctk.CTkLabel(
            self, width=self.label_width, text=label, justify=self.horz_align
        )
        self.slider = ctk.CTkSlider(self, from_=min_val, to=max_val, command=callback)
        self.value_label = ctk.CTkLabel(self, text="")

        self.label.grid(row=0, column=0, padx=self.pad_x, pady=self.pad_y, sticky="w")
        self.slider.grid(row=0, column=1, padx=self.pad_x, pady=self.pad_y, sticky="we")
        self.value_label.grid(
            row=0, column=2, padx=self.pad_x, pady=self.pad_y, sticky="we"
        )

        if default_val is not None:
            self.set_value(default_val)

    def value(self):
        return self.output_value_conversion(self.slider.get())

    def set_value(self, value):
        self.slider.set(self.input_value_conversion(value))
        self.value_label.configure(text=self.value_str())

    def value_str(self):
        if isinstance(self.value_fmt, str):
            return self.value_fmt % (self.value())
        return self.value_fmt(self.value())


class LabelledEntryFrame(ctk.CTkFrame, WidgetStyleMixin):

    def __init__(self, master, label, units_label=None, **kwargs):
        kwargs = WidgetStyleMixin.__init__(self, **kwargs)
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        if units_label is not None:
            self.grid_columnconfigure(2, weigth=1)

        self.label = ctk.CTkLabel(
            self, width=self.label_width, text=label, justify=self.horz_align
        )
        self.entry = ctk.CTkEntry(self, width=self.def_width)
        if units_label is not None:
            self.units = ctk.CTkLabel(
                self, width=self.units_width, text=units_label, justify=ctk.LEFT
            )

        self.label.grid(row=0, column=0, padx=self.pad_x, pady=self.pad_y, sticky="w")
        self.entry.grid(row=0, column=1, padx=self.pad_x, pady=self.pad_y, sticky="w")

        if units_label is not None:
            self.units.grid(
                row=0, column=2, padx=self.pad_x, pady=self.pad_y, sticky="w"
            )

    def content(self):
        return self.entry.get()

    def set_content(self, text):
        set_entry_text(self, text=text)


class LabelledSegmentFrame(ctk.CTkFrame, WidgetStyleMixin):

    def __init__(self, master, label, values, callback=None, **kwargs):
        kwargs = WidgetStyleMixin.__init__(self, **kwargs)
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        self.label = ctk.CTkLabel(
            self, width=self.label_width, text=label, justify=self.horz_align
        )
        self.segment = ctk.CTkSegmentedButton(self, values=values, command=callback)

        self.label.grid(row=0, column=0, padx=self.pad_x, pady=self.pad_y, sticky="w")
        self.segment.grid(row=0, column=1, padx=self.pad_x, pady=self.pad_y, sticky="w")

    def choice(self):
        return self.segment.get()

    def set_choice(self, value):
        self.segment.set(value)
