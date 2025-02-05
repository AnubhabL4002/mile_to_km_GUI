from tkinter import Tk, ttk, PhotoImage
import sv_ttk

window = Tk()
window.title("M to KM Converter")
window.minsize(300,300)
icon = PhotoImage(file="icon_.png")
window.iconphoto(True, icon)

sv_ttk.set_theme("dark")

my_label = ttk.Label(text= "Convert the Value!", font=("Loved by the King",24, ""))
my_label.grid(row= 0,column=1, padx= 20, pady = (20,50))


def calculate():
    mile=int(input_box.get())
    km= mile * 1.609344
    label3.config(text=km)

input_box = ttk.Entry(font=("",18,""),width=10)
input_box.grid(row=1,column=1,pady=10)

label1=ttk.Label(text = "Miles", font=("",18,""))
label1.grid(row=1,column=2,pady=10)

label2=ttk.Label(text = "is equal to", font=("",18,""))
label2.grid(row=2,column=0,padx=(30,0),pady=20)

label3 = ttk.Label(text = "", font=("",18,"bold"))
label3.grid(row=2,column=1,padx=20, pady=20)

label4 = ttk.Label(text = "Kilometers", font=("",18,""))
label4.grid(row=2,column=2,padx=(0,30), pady=20)

button = ttk.Button(text= "Calculate",padding=(20,10),command=calculate)
button.grid(row=3,column=1,pady=20)

window.mainloop()