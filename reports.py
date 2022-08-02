import os
import webbrowser

from fpdf import FPDF


class PdfReport:
    """
    Creates a Pdf file that contains data about
    the flatmates such as their names, their due
    amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmates, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("./files/house.png", w=40, h=40)

        # Insert Title
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C', ln=1)

        # Insert Period label and value
        pdf.cell(w=100, h=40, txt="Period", border=0)
        pdf.cell(w=0, h=40, txt=bill.period, border=0, ln=1)

        # Insert flatmates
        pdf.set_font(family='Times', size=12)
        for flatmate_instance in flatmates:
            pdf.cell(w=100, h=25, txt=flatmate_instance.name, border=0)

            flatmate_needs_to_pay = str(round(flatmate_instance.pays(bill, flatmates), 2))
            print(flatmate_instance.name, " pays: ", flatmate_needs_to_pay)
            pdf.cell(w=0, h=25, txt=flatmate_needs_to_pay, border=0, ln=1)

        # Change directory to files
        os.chdir("files")

        # Generate PDF
        pdf.output(self.filename)

        # Open the pdf automatically
        # If Windows
        webbrowser.open(self.filename)

        # If Mac or Linux
        # webbrowser.open('file://' + os.path.realpath(self.filename))
