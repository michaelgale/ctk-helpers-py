# ctk-helpers-py

This repository contains a collection of helper functions and classes for writing [CustomTkinter](https://customtkinter.tomschimansky.com) [Github](https://github.com/tomschimansky/customtkinter) python apps.

Useful links:

- [CustomTkinter documentation](https://customtkinter.tomschimansky.com/documentation/)
- [tkinter-toolkit](https://github.com/Akascape/tkinter-toolkit)
- [ctk_components](https://github.com/rudymohammadbali/ctk_components)
- [CTkListbox](https://github.com/Akascape/CTkListbox)
- [CTkMessagebox](https://github.com/Akascape/CTkMessagebox)
- [CTkXYFrame](https://github.com/Akascape/CTkXYFrame)


## Minimum App

Minimum app template:

```python
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("640x480")
        self.title("Test App")

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
```

## Minimum App with Drag and Drop 

Minimum app template that includes drag and drop support:

```python
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_ALL

class CTk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

class App(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("640x480")
        self.title("Test App")

    def drop_target_callback(self, args):
        pass

def main():
    app = App()
    app.drop_target_register(DND_ALL)
    app.dnd_bind("<<Drop>>", app.drop_target_callback)
    app.mainloop()

if __name__ == "__main__":
    main()
```

## Handling Zoomable Content

```python

"""
   img stores the PIL image object loaded from a file
   image stores the CTkImage object
   image_frame is the container for the CTkImage

   zoom stores the zoom ratio
"""
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("640x480")
        self.title("Test App")

        self.image_frame = ctk.CTkLabel(
            self,
            width=400, 
            text="+ \nDrag & Drop your Image",
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["top_fg_color"],
        )
        self.img = Image.open(FILENAME)
        self.image = ctk.CTkImage(self.img)
        self.image_frame.configure(text="", image=self.image)
        self.image.configure(
            size=(self.image_frame.winfo_reqwidth(),
            self.image_frame.winfo_reqheight() * (self.img.size[1]/self.img.size[0])
            )
        )
        self.image_frame.pack(padx=(5, 5), pady=5, fill="both", side="right")
        self.image_frame.bind("<Configure>", self.resize_event)
        self.image_frame.bind("<MouseWheel>", lambda e: self.zoom_callback(e.delta))

    def zoom_callback(self, delta):
        if delta > 0:
            self.zoom += 1
        else:
            self.zoom -= 1
        if self.zoom <= 0 or self.zoom > 2:
            return
        self.image.configure(
            size=(
                self.image_frame.winfo_height() * self.zoom, 
                self.image_frame.winfo_height() * self.zoom * (self.img.size[1] / self.img.size[0])
            )
        )

    def resize_event(self, event):
        if self.zoom > 1:
             return
        if self.image is not None:
            self.image.configure(
                size=(
                    event.height, 
                    event.height * self.img.size[1] / self.img.size[0])
            )
            
        
```