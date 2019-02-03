import Tkinter

tk = Tkinter # Alternative to the messy 'from Tkinter import *' often seen

class ProgressBar(tk.Frame):
    """A simple progress bar that shows a percentage progress in
    the given colour."""

    def __init__(self, *args, **kwargs):
        apply(tk.Frame.__init__, (self,) + args, kwargs)
        self.canvas = tk.Canvas(self, height='20', width='60',
                                background='white', borderwidth=3)
        self.canvas.pack(fill=tk.X, expand=1)
        self.rect = self.text = None
        self.canvas.bind('<Configure>', self.paint)
        self.setProgressFraction(0.0)

    def setProgressFraction(self, fraction, color='blue'):
        self.fraction = fraction
        self.color = color
        self.paint()
        self.canvas.update_idletasks()

    def paint(self, *args):
        totalWidth = self.canvas.winfo_width()
        width = int(self.fraction * float(totalWidth))
        height = self.canvas.winfo_height()
        if self.rect is not None: self.canvas.delete(self.rect)
        if self.text is not None: self.canvas.delete(self.text)
        self.rect = self.canvas.create_rectangle(0, 0, width, height,
                                                 fill=self.color)
        percentString = "%3.0f%%" % (100.0 * self.fraction)
        self.text = self.canvas.create_text(totalWidth/2, height/2,
                                            anchor=tk.CENTER,
                                            text=percentString)
