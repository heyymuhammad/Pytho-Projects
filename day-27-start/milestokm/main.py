import tkinter

window = tkinter.Tk()
window.title("Miles To Km Converter")
window.minsize(width=50,height=80)
window.config(padx=50, pady=80)


#entry
Input = tkinter.Entry(width=10,) #input build
Input.grid(column=1,row=0)



#Labels
miles = tkinter.Label(text="Miles") #label build
miles.grid(column=2,row=0)


is_equal = tkinter.Label(text="is equal to") #label build
is_equal.grid(column=0,row=1)

answer = tkinter.Label(text=0) #label build
answer.grid(column=1,row=1)

km = tkinter.Label(text="km") #label build
km.grid(column=2,row=1)



#button
def onclick():
    user_Miles = int(Input.get()) #get value
    user_kilometers = 1.609344
    calculate = user_Miles*user_kilometers
    answer.config(text=calculate) #change using .config()

button = tkinter.Button(text="Calculate", command=onclick) #button build
# button.pack() #to display
button.grid(column=1,row=2)



window.mainloop()