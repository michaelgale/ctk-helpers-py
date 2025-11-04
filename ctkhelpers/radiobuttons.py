import customtkinter as ctk

from ctkhelpers import *


class RadioButtonFrame(ctk.CTkFrame, WidgetStyleMixin):

    def __init__(self, master, choices, title=None, notify=None, **kwargs):
        kwargs = WidgetStyleMixin.__init__(self, **kwargs)
        super().__init__(master, **kwargs)
        self.choices = choices
        self.frame = ctk.CTkFrame(master=self, width=self.frame_width)
        if title is not None:
            self.title = ctk.CTkLabel(
                master=self.frame,
                text=title,
                justify=self.horz_align,
                font=self.title_font,
            )
            self.title.pack(
                pady=self.pad_y, padx=self.pad_x, anchor="nw", fill="x", expand=True
            )
        self.var = ctk.IntVar(master=self.frame, value=0)
        self.buttons = []
        for i, choice in enumerate(choices):
            button = ctk.CTkRadioButton(
                master=self.frame,
                text=choice,
                command=self.button_clicked,
                variable=self.var,
                value=i,
            )
            button.pack(pady=self.pad_y, padx=self.pad_x, anchor="nw", fill="x")
            self.buttons.append(button)
        self.frame.pack(pady=self.pad_y, padx=self.pad_x, anchor="nw", fill="x")
        self.notify = notify

    def button_clicked(self):
        if self.notify is not None:
            self.notify()

    def choice(self):
        return self.var.get()

    def set_choice(self, value):
        self.var.set(value)
