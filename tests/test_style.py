import pytest
import math
import customtkinter as ctk

from ctkhelpers import *


class TestApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("640x480")
        self.title("Test App")


def double_value(v):
    return 2**v


def half_value(v):
    return math.log2(v)


def stars_str(v):
    if v >= 0 and v <= 5:
        return {
            0: "",
            1: "*",
            2: "**",
            3: "***",
            4: "****",
            5: "*****",
        }[v]
    return ""


def dummy_callback(event):
    print(event)


def test_widget_style():
    app = TestApp()
    w1 = LabelledComboFrame(
        app, "Combo label", ["First", "Second"], default_choice="Second"
    )
    v = w1.choice()
    assert v == "Second"
    w1.set_choice("First")
    v = w1.choice()
    assert v == "First"
    assert w1.pad_x == PAD_X
    assert w1.pad_y == PAD_Y

    w2 = LabelledSegmentFrame(app, "Entry test", ["First", "Second"], pad_x=10, pad_y=1)
    assert w2.pad_x == 10
    assert w2.pad_y == 1

    w3 = LabelledComboFrame(app, "Combo 2", ["This", "That"], callback=dummy_callback)
    assert "dummy_callback" in str(w3.combo._command)


def test_value_conversion():
    app = TestApp()
    w1 = LabelledSliderFrame(
        app, "Slider", min_val=-50, max_val=100, default_val=25, value_fmt="%.2f"
    )
    v = w1.value()
    assert v == 25
    w1.set_value(-33)
    v = w1.value()
    assert v == -33.0
    sv = w1.value_str()
    assert sv == "-33.00"

    w2 = LabelledSliderFrame(
        app,
        "Slider 2",
        min_val=1,
        max_val=8,
        default_val=1,
        value_fmt="%d",
        input_value_conversion=half_value,
        output_value_conversion=double_value,
    )
    v = w2.value()
    assert v == 2
    w2.set_value(16)
    v = w2.value()
    assert v == 16
    vs = w2.slider.get()
    assert vs == 4
    vs = w2.value_str()
    assert vs == "16"

    w3 = LabelledSliderFrame(app, "Stars", min_val=0, max_val=5, value_fmt=stars_str)
    w3.set_value(2)
    v = w3.value()
    assert v == 2
    sv = w3.value_str()
    assert sv == "**"
