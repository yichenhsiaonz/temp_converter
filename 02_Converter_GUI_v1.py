from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Converter:
    def __init__(self):
        # Formatting variables
        background_color = "bisque"

        # Converter Frame
        self.converter_frame = Frame(width=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading {row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Arial", 16, "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Temperature Conversion Heading {row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be "
                                                  "converted and then push "
                                                  "one of the buttons below...",
                                             font="Arial, 10", wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font=("Arial", 14, "bold"))
        self.to_convert_entry.grid(row=2)

        # Conversion buttons frame (row 3)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font=("Arial", 10, "bold"),
                                  bg="Khaki1", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font=("Arial", 10, "bold"),
                                  bg="Orchid1", padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)

        self.temp_answer_label = Label(self.converter_frame,
                                             text="Conversion will appear here...",
                                             font=("Arial", 14), wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10, fg="indianred1")
        self.temp_answer_label.grid(row=4)

        # Help button / history (row 5)
        self.history_help_frame= Frame(self.converter_frame)
        self.history_help_frame.grid(row=5, pady=10)

        self.history_button = Button(self.history_help_frame, text="Calculation History",
                                  font=("Arial", 10, "bold"),
                                  padx=10, pady=5)
        self.history_button.grid(row=5, column=0)

        self.help_button = Button(self.history_help_frame, text="Help",
                                  font=("Arial", 10, "bold"),
                                  padx=10, pady=5)
        self.help_button.grid(row=5, column=1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Conversion Calculator")
    something = Converter()
    root.mainloop()
