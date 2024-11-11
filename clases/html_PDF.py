import jinja2
import pdfkit

class ConvertPDF():
    def __init__(self, block, numOrder, enterprise, addressGathering, contact, phone, enterpriseDelivery, addressDelivery, series1, series2, cantPages):

        self._block = block
        self._numOrder = numOrder
        self._enterprise = enterprise
        self._addressGathering = addressGathering
        self._contact = contact
        self._phone = phone
        self._enterpriseDelivery = enterpriseDelivery
        self._addressDelivery = addressDelivery
        self._series1 = series1
        self._series2 = series2
        self._cantPages = cantPages

        self.dateGathering = f"Empresa entrega: {self._enterprise} Dirección: {self._addressGathering} <br>Contacto: {self._contact} <br>Phone: {self._phone}"
        self.dateDelivery = f"Empresa entrega: {self._enterpriseDelivery} Dirección: {self._addressDelivery}"
        
        self.context = {'block':self._block, 'numOrder':self._numOrder, 'enterprise':self._enterprise,'addressGathering':self._addressGathering, 
                        'contact':self._contact, 'phone':self._phone, 'dateGathering':self.dateGathering, 
                        'enterpriseDelivery':enterpriseDelivery, 'dateDelivery':self.dateDelivery, 'serials1':self._series1, 'serials2':self._series2, 'cantPages':self._cantPages}
        
    def generatePDF(self):
        self.template_loader = jinja2.FileSystemLoader('./')
        self.template_env = jinja2.Environment(loader=self.template_loader)

        self.html_template = 'plantilla.html'
        self.template = self.template_env.get_template(self.html_template)
        self.output_text = self.template.render(self.context)

        self.config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        self.output_pdf = 'pdf_generated.pdf'
        pdf =pdfkit.from_string(self.output_text,self.output_pdf, configuration=self.config, css='css/style.css')
        #print("SERIES 1")
        #print(self._series1)
        #print("SERIES 2")
        #print(self._series2)
        