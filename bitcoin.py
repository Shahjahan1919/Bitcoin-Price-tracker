import requests
import tkinter as tk
from datetime import datetime





def trackbit():
    url="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"

    response= requests.get(url).json()
    price=response["USD"]
    time= datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text=str(price) + "$")
    labelTime.config(text= "Updated at:" + time)

    canvas.after(1000,trackbit)
canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Bitcoin")


f1 = ("poppins", 24 ,"bold")
f2 = ("poppins", 22 ,"bold")
f3 = ("poppins", 18 ,"normal")

label = tk.Label(canvas,text = "Bitcoin price", font=f1)
label.pack(pady=20)

labelPrice= tk.Label(canvas, font=f2)
labelPrice.pack(pady=20)

labelTime= tk.Label(canvas, font=f2)
labelTime.pack(pady=20)


trackbit()


canvas.mainloop()
