import tkinter

window = tkinter.Tk()
window.title("Mile to km Converter")
window.minsize(width=50, height=80)
window.config(padx=50,pady=80)

Input = tkinter.Entry(width=10)
Input.grid(row=0, column=1)

miles = tkinter.Label(text="Miles")
miles.grid(row=0, column=2)

is_equal = tkinter.Label(text="is equal to")
is_equal.grid(row=1, column=0)

answer = tkinter.Label(text=0)
answer.grid(row=1,column=1)

km = tkinter.Label(text="km")
km.grid(row=1, column=2)

button = tkinter.Button(text="Calculate")
button.grid(row=2,column=1)

def on_click():
    user_km = float(Input.get())
    user_miles = round(user_km *1.609344, ndigits=6)
    answer.config(text=user_miles)

button.config(command=on_click)


tkinter.mainloop()