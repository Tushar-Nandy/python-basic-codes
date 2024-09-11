import tkinter as tk

km =0

def calc_km():
    mile = float(mile_input.get())
    global km 
    km = mile * 1.60934
    km_label.config(text=f"{km}")
    
window= tk.Tk()
window.title("Mile to km Convertor")
window.minsize(width=100, height= 75)
window.config(padx=5, pady=5)

mile_input = tk.Entry(width= 5)
mile_input.grid(row=0, column=1)
mile_label = tk.Label(text= 'Miles')
mile_label.grid(row=0, column= 2)
label = tk. Label(text='is eqaul to ')
label.grid(row=1, column=0)
km_label = tk.Label(text=f"{km}")
km_label.grid(row=1, column= 1)
unit_label = tk.Label(text='Km')
unit_label.grid(row=1, column=2)
button = tk.Button(text="Calculate", command= calc_km)
button.grid(row=2, column=1)



window.mainloop()