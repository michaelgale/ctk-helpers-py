import customtkinter as ctk

from ctkhelpers import *


def set_entry_text(widget, text):
    """A convenience function to replace text in a CTkEntry widget"""
    widget.delete(0, ctk.END)
    widget.insert(0, text)


def set_label_text(widget, text):
    """A convenience function to replace text in a CTkLabel widget"""
    widget.configure(text=text)


def set_image(widget, image):
    """A convenience function to replace widget with an image"""
    img = ctk.CTkImage(light_image=image, dark_image=image, size=image.size)
    widget.configure(image=img)
    widget.configure(width=image.size[0])
    widget.configure(height=image.size[1])
