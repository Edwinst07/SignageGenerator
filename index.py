import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog 
from tkinter import messagebox
from PIL import ImageTk, Image
from clases import seriesFile
from clases import html_PDF

root = tk.Tk()
root.geometry("940x717")
root.title("Generador de rotulos")
root.config(bg="#2c122b")
root.iconbitmap("img/icon.ico")

photo = Image.open("img/icon.png")
img = ImageTk.PhotoImage(photo)

file_path = ""

def select_File():
    global file_path

    file_path = filedialog.askopenfilename(
		title= "Selecciona archivos", 
		filetypes=[("txt files","*.txt")]
		)
    
def generateRotulos():

    try:
         
        series = seriesFile.Series(str(file_path))

        block = textBlock.get("1.0", "end-1c").strip("\n")
        block = textBlock.get("1.0", "end-1c").strip("\t")
        numOrder = textNumOrder.get("1.0", "end-1c").strip("\n")
        numOrder = textNumOrder.get("1.0", "end-1c").strip("\t")
        enterprise= textEnterprise.get("1.0", "end-1c").strip("\n")
        enterprise= textEnterprise.get("1.0", "end-1c").strip("\t")
        addressGathering = textAddressGathering.get("1.0", "end-1c").strip("\n")
        addressGathering = textAddressGathering.get("1.0", "end-1c").strip("\t")
        contact = textContact.get("1.0", "end-1c").strip("\n")
        contact = textContact.get("1.0", "end-1c").strip("\t")
        phone = textPhone.get("1.0", "end-1c").strip("\n")
        phone = textPhone.get("1.0", "end-1c").strip("\t")
        enterpriseDelivery = textEnterpriseDelivery.get("1.0", "end-1c").strip("\n")
        enterpriseDelivery = textEnterpriseDelivery.get("1.0", "end-1c").strip("\t")
        addressDelivery = textAddressDelivery.get("1.0", "end-1c").strip("\n")
        addressDelivery = textAddressDelivery.get("1.0", "end-1c").strip("\t")
        
        if not block:
            messagebox.showinfo('Error', 'El campo "bloque" está vacío !!.')
        elif not enterprise:
            messagebox.showinfo('Error', 'El campo "Empresa que entrega" está vacío !!.')
        elif not addressGathering:
            messagebox.showinfo('Error', 'El campo "Dirección Empresa que entrega" está vacío !!.')
        elif not contact:
            messagebox.showinfo('Error', 'El campo "Nombre de quien va a recibir" está vacío !!.')
        elif not phone:
            messagebox.showinfo('Error', 'El campo "Telefono o Móvil que va a recibir" está vacío !!.')
        elif not enterpriseDelivery:
            messagebox.showinfo('Error', 'El campo "Empresa que recibe" está vacío !!.')
        elif not addressDelivery:
            messagebox.showinfo('Error', 'El campo "Dirección de empresa que recibe" está vacío !!.')
        
        if block and enterprise and addressGathering and contact and phone and enterpriseDelivery and addressDelivery:
            generator = html_PDF.ConvertPDF(block, numOrder, enterprise, addressGathering, contact, phone, enterpriseDelivery, addressDelivery, series.arraySeries1(), series.arraySeries2(), series.cantPages)
            generator.generatePDF()

    except FileNotFoundError:
        messagebox.showinfo('Error', 'Debe ingresar el txt de los seriales !!.')


def display():
    root.columnconfigure(0, weight=1)
    root.columnconfigure(2, weight=4)
    #root.rowconfigure(1, weight=2)
    #root.rowconfigure(0, weight=4)
    rowEmpty0 = Label(root, text="empty", fg="#2c122b", bg="#2c122b")  # Row empty
    rowEmpty0.grid(column=0, row=0, sticky=E, padx=5, pady=5)

    labelIcon = Label(root, image=img)
    labelIcon.image = img
    labelIcon.grid(column=0, row=1, sticky=E, padx=5, pady=5)
    labelTitle = Label(root, text="Generador de rotulos", font=("Segoe UI", 16, "bold"), fg="white", bg="#2c122b") 
    labelTitle.grid(column=1, row=1, sticky=W, padx=5, pady=5)

    rowEmpty1 = Label(root, text="empty", fg="#2c122b", bg="#2c122b")  # Row empty
    rowEmpty1.grid(column=0, row=2, sticky=E, padx=5, pady=5)

    labelBlock = Label(root, text="Bloque: ", font=("Segoe UI", 12), fg="white", bg="#2c122b")  
    labelBlock.grid(column=0, row=3, sticky=E, padx=5, pady=5)
    global textBlock
    textBlock = Text(root, height=1, width=25, font=("Segoe UI", 12))
    textBlock.grid(column=1, row=3, sticky=W, padx=5, pady=5)

    global textNumOrder
    labelNumOrder = Label(root, text="Número de orden: ", font=("Segoe UI", 12), fg="white", bg="#2c122b")  
    labelNumOrder.grid(column=0, row=4, sticky=E, padx=5, pady=5)
    textNumOrder = Text(root, height=1, width=25, font=("Segoe UI", 12))
    textNumOrder.grid(column=1, row=4, sticky=W, padx=5, pady=5)

    global textEnterprise
    labelEnterprise = Label(root, text="Empresa que entrega: ", font=("Segoe UI", 12), fg="white", bg="#2c122b")  
    labelEnterprise.grid(column=0, row=5, sticky=E, padx=5, pady=5)
    textEnterprise = Text(root, height=1, width=50, font=("Segoe UI", 12))
    textEnterprise.grid(column=1, columnspan=2, row=5, sticky=W, padx=5, pady=5)

    global textAddressGathering
    labelAddressGathering = Label(root, text="Dirección Empresa que entrega: ", font=("Segoe UI", 12), fg="white", bg="#2c122b") 
    labelAddressGathering.grid(column=0, row=6, sticky=E, padx=5, pady=5) 
    textAddressGathering = Text(root, height=2, width=80, font=("Segoe UI", 12))
    textAddressGathering.grid(column=1, columnspan=3, row=6, sticky=W, padx=5, pady=5)

    global textContact
    labelContact = Label(root, text="Nombre de quien va a recibir: ", font=("Segoe UI", 12), fg="white", bg="#2c122b") 
    labelContact.grid(column=0, row=7, sticky=E, padx=5, pady=5)
    textContact = Text(root, height=1, width=35, font=("Segoe UI", 12))
    textContact.grid(column=1, row=7, sticky=W, padx=5, pady=5)

    global textPhone
    labelPhone = Label(root, text="Telefono o Móvil que va a recibir: ", font=("Segoe UI", 12), fg="white", bg="#2c122b")
    labelPhone.grid(column=0, row=8, sticky=E, padx=5, pady=5)
    textPhone = Text(root, height=1, width=25, font=("Segoe UI", 12))
    textPhone.grid(column=1, row=8, sticky=W, padx=5, pady=5)

    global textEnterpriseDelivery
    labelEnterpriseDelivery = Label(root, text="Empresa que recibe: ", font=("Segoe UI", 12), fg="white", bg="#2c122b")
    labelEnterpriseDelivery.grid(column=0, row=9, sticky=E, padx=5, pady=5)
    textEnterpriseDelivery = Text(root, height=1, width=50, font=("Segoe UI", 12))
    textEnterpriseDelivery.grid(column=1, row=9, sticky=W, padx=5, pady=5)

    global textAddressDelivery
    labelAddressDelivery = Label(root, text="Dirección de empresa que recibe: ", font=("Segoe UI", 12), fg="white", bg="#2c122b")
    labelAddressDelivery.grid(column=0, row=10, sticky=E, padx=5, pady=5)
    textAddressDelivery = Text(root, height=2, width=80, font=("Segoe UI", 12))
    textAddressDelivery.grid(column=1, columnspan=3, row=10, sticky=W, padx=5, pady=5)

    labelAdjuntarFile = Label(root, text="Adjuntar series en txt: ", font=("Segoe UI", 12), fg="white", bg="#2c122b")
    labelAdjuntarFile.grid(column=0, row=11, sticky=E, padx=5, pady=5)
    buttonAdjuntar = Button(root, text="Adjuntar", command=select_File, fg="#2c122b",font=("Segoe UI", 12, "bold"), bg="white")
    buttonAdjuntar.grid(column=1, row=11, sticky=W, padx=5, pady=5)

    rowEmpty2 = Label(root, text="empty", fg="#2c122b", bg="#2c122b")  # Row empty
    rowEmpty2.grid(column=0, row=12, sticky=E, padx=5, pady=5)

    global buttonGenerator
    buttonGenerator = Button(root, text="Generar Rotulos", command=generateRotulos, fg="#2c122b",font=("Segoe UI", 12, "bold"), bg="white")
    buttonGenerator.grid(column=1, row=13, sticky=EW, padx=5, pady=5)

    rowEmpty2 = Label(root, text="empty", fg="#2c122b", bg="#2c122b")  # Row empty
    rowEmpty2.grid(column=0, row=14, sticky=E, padx=5, pady=5)

    labelAutor = Label(root, text="@2024 Edwin Stiven Lozada Mahecha - edwinst98@gmail.com", fg="#2c122b",font=("Segoe UI", 10), bg="white")
    labelAutor.grid(column=0, columnspan=3, row=15, sticky=EW, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    display()