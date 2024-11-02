import jinja2
import pdfkit
from datetime import datetime

block = "EOL-00001522.0001-228"
numOrder = "0021 8000012976-01"
enterprise = "ISA INTERCONEXION ELECTRICA S.A. E.S.P."
addressGathering = "Sede ANCON - Calle 84 Sur No. 40 - 61 (Km1 variante a Caldas) Sabaneta, Antioquia"
contact = "Sindy Lorena Florez "
phone = "+57 3112431683 "
dateGathering = f"Empresa entrega: {enterprise} Dirección: {addressGathering} <br>Contacto: {contact} <br>Phone: {phone}"
enterpriseDelivery ="BTR Colombia SAS "
addressDelivery = " Autopista Medellin Km. 3.5 Costado Sur modulo 3 Bodega 26 Terminal Terrestre de Carga Cota, Cundinamarca, Colombia"
dateDelivery = f"Empresa entrega: {enterpriseDelivery} Dirección: {addressDelivery}"
serial = "6CM94715BH (ISAH5675M)"

context = {'block':block, 'numOrder':numOrder, 'enterprise':enterprise,'addressGathering':addressGathering, 
           'contact':contact, 'phone':phone, 'dateGathering':dateGathering, 
           'enterpriseDelivery':enterpriseDelivery, 'dateDelivery':dateDelivery, 'serial':serial}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'plantilla.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
output_pdf = 'pdf_generated.pdf'
pdfkit.from_string(output_text,output_pdf, configuration=config, css='css/style.css')

