import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.geometry("933x560")
root.title("Generador de rotulos")
root.config(bg="#2c122b")
root.iconbitmap("img/icon.ico")

def display():
    root.columnconfigure(0, weight=1)
    root.columnconfigure(2, weight=4)
    #root.rowconfigure(1, weight=2)
    #root.rowconfigure(0, weight=4)
    rowEmpty0 = Label(root, text="empty", fg="#2c122b", bg="#2c122b")  # Row empty
    rowEmpty0.grid(column=0, row=0, sticky=E, padx=5, pady=5)

    labelTitle = Label(root, text="Generador de rotulos", font=("Segoe UI", 16, "bold"), fg="white", bg="#2c122b") 
    labelTitle.grid(column=0, row=1, sticky=EW, padx=5, pady=5)

    rowEmpty1 = Label(root, text="empty", fg="#2c122b", bg="#2c122b")  # Row empty
    rowEmpty1.grid(column=0, row=2, sticky=E, padx=5, pady=5)

    labelBlock = Label(root, text="Block: ", font=("Segoe UI", 12), fg="white", bg="#2c122b")  
    labelBlock.grid(column=0, row=3, sticky=E, padx=5, pady=5)
    textBlock = Text(root, height=1, width=25)
    textBlock.grid(column=1, row=3, sticky=W, padx=5, pady=5)

    labelNumOrder = Label(root, text="Número de orden: ", font=("Segoe UI", 12), fg="white", bg="#2c122b")  
    labelNumOrder.grid(column=0, row=4, sticky=E, padx=5, pady=5)
    textNumOrder = Text(root, height=1, width=25)
    textNumOrder.grid(column=1, row=4, sticky=W, padx=5, pady=5)

    labelEnterprise = Label(root, text="Empresa que entrega: ", font=("Segoe UI", 12), fg="white", bg="#2c122b")  
    labelEnterprise.grid(column=0, row=5, sticky=E, padx=5, pady=5)
    textEnterprise = Text(root, height=1, width=50)
    textEnterprise.grid(column=1, columnspan=2, row=5, sticky=W, padx=5, pady=5)

    labelAddressGathering = Label(root, text="Dirección Empresa que entrega: ", font=("Segoe UI", 12), fg="white", bg="#2c122b") 
    labelAddressGathering.grid(column=0, row=6, sticky=E, padx=5, pady=5) 
    textAddressGathering = Text(root, height=2, width=80)
    textAddressGathering.grid(column=1, columnspan=3, row=6, sticky=W, padx=5, pady=5)

    labelContact = Label(root, text="Nombre de quien va a recibir: ", font=("Segoe UI", 12), fg="white", bg="#2c122b") 
    labelContact.grid(column=0, row=7, sticky=E, padx=5, pady=5)
    textContact = Text(root, height=1, width=35)
    textContact.grid(column=1, row=7, sticky=W, padx=5, pady=5)

    labelPhone = Label(root, text="Telefono o Móvil que va a recibir: ", font=("Segoe UI", 12), fg="white", bg="#2c122b")
    labelPhone.grid(column=0, row=8, sticky=E, padx=5, pady=5)
    textPhone = Text(root, height=1, width=25)
    textPhone.grid(column=1, row=8, sticky=W, padx=5, pady=5)

    labelEnterpriseDelivery = Label(root, text="Empresa que recibe: ", font=("Segoe UI", 12), fg="white", bg="#2c122b")
    labelEnterpriseDelivery.grid(column=0, row=9, sticky=E, padx=5, pady=5)
    textEnterpriseDelivery = Text(root, height=1, width=50)
    textEnterpriseDelivery.grid(column=1, row=9, sticky=W, padx=5, pady=5)

    labelAddressDelivery = Label(root, text="Dirección de empresa que recibe: ", font=("Segoe UI", 12), fg="white", bg="#2c122b")
    labelAddressDelivery.grid(column=0, row=10, sticky=E, padx=5, pady=5)
    textAddressDelivery = Text(root, height=2, width=80)
    textAddressDelivery.grid(column=1, columnspan=3, row=10, sticky=W, padx=5, pady=5)

    root.mainloop()

display()