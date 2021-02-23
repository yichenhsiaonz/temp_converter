from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


# copied 900% from help gui


class Converter:
    def __init__(self):

        # Formatting variables
        background_color = "bisque"

        # Converter Main Screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=background_color, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading {row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Help button (row 1)
        self.help_button = Button(self.converter_frame, text="Calculation History",
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=self.history)
        self.help_button.grid(row=1)

    def history(self):
        print("You asked for history")
        get_help = History(self)
        get_help.help_text.configure(text="History text goes here")


class History:
    def __init__(self, partner):

        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie) help box
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()
        # Set up Help heading (row 0)
        self.help_label = Label(self.help_frame, text="Calculation History",
                                font=("Arial", "14", "bold"),
                                bg=background,
                                padx=10, pady=10)
        self.help_label.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40,
                               bg=background, wrap=250,)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to notmal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
