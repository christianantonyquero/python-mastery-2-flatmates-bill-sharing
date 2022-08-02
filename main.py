import webbrowser
from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill such as
    total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmates):
        # Compute total days all the flatmates stayed in the house.
        flatmates_total_days_in_house = 0
        for flatmate_instance in flatmates:
            flatmates_total_days_in_house += flatmate_instance.days_in_house

        # Compute weight for the  flatmate
        weight = self.days_in_house / flatmates_total_days_in_house

        # Total amount flatmate will pay
        to_pay = bill.amount * weight
        return to_pay


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

        # Generate PDF
        pdf.output(self.filename)

        # Open the pdf automatically
        # If Windows
        webbrowser.open(self.filename)

        # If Mac or Linux
        # webbrowser.open('file://' + os.path.realpath(self.filename))


the_bill = Bill(amount=120, period="April 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)
chris = Flatmate(name="Chris", days_in_house=15)

flatmate_list = [john, marry, chris]

pdf_report = PdfReport(filename="Report.pdf")
pdf_report.generate(flatmate_list, the_bill)
