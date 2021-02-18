from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


def num_checker(input_number, minimum):
    if input_number.lstrip("-").replace(".", "", 1).isnumeric():
        number = float(input_number)
        if number >= minimum:
            return True
    else:
        return False


def rounding(num_to_round):
    if num_to_round % 1 != 0:
        return round(num_to_round, 1)
    else:
        return int(num_to_round)


def to_c(temp):
    c = ((temp - 32) * 5 / 9)
    return rounding(c)


def to_f(temp):
    f = (temp * 9 / 5 + 32)
    return rounding(f)


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

        self.instructions = "Type in the amount to be converted and then push one of the buttons below..."

        self.temp_instructions_label = Label(self.converter_frame,
                                             text=self.instructions,
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
                                  bg="Khaki1", padx=10, pady=10,
                                  command=lambda: self.convert("fahrenheit"))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font=("Arial", 10, "bold"),
                                  bg="Orchid1", padx=10, pady=10,
                                  command=lambda: self.convert("celsius"))
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)

        self.temp_answer_label = Label(self.converter_frame,
                                       text="Conversion will appear here...",
                                       font=("Arial", 14), wrap=250,
                                       justify=LEFT, bg=background_color,
                                       padx=10, pady=10, fg="indianred1")
        self.temp_answer_label.grid(row=4)

        # Help button / history (row 5)
        self.history_help_frame = Frame(self.converter_frame)
        self.history_help_frame.grid(row=5, pady=10)

        self.history_button = Button(self.history_help_frame, text="Calculation History",
                                     font=("Arial", 10, "bold"),
                                     padx=10, pady=5)
        self.history_button.grid(row=5, column=0)

        self.help_button = Button(self.history_help_frame, text="Help",
                                  font=("Arial", 10, "bold"),
                                  padx=10, pady=5,
                                  command=self.help)
        self.help_button.grid(row=5, column=1)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

    def convert(self, unit):

        error = "#ffafaf"
        converted_number = ""

        # Unit to check if temp is celsius or fahrenheit

        number = self.to_convert_entry.get()

        if unit == "celsius":
            other_unit = "fahrenheit"
            if num_checker(number, -273.15):
                converted_number = to_f(float(number))
        else:
            other_unit = "celsius"
            if num_checker(number, -459.67):
                converted_number = to_c(float(number))
        if converted_number != "":

            answer_text = "{} degrees {} is {} degrees {}".format(number, unit, converted_number, other_unit)

            self.temp_answer_label.config(text=answer_text)
            self.temp_instructions_label.config(text=self.instructions)
            self.to_convert_entry.config(bg="#FFF")

            global calculation_history
            calculation_history.append(answer_text)

        else:
            self.to_convert_entry.config(bg=error)
            self.temp_instructions_label.config(text="Please enter a valid integer or float")


class Help:
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
        self.help_label = Label(self.help_frame, text="Help / Instructions",
                                font=("Arial", "14", "bold"),
                                bg=background,
                                padx=10, pady=10)
        self.help_label.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40,
                               bg=background, wrap=250, )
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine

calculation_history = []

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Conversion Calculator")
    something = Converter()
    root.mainloop()
