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

    def pays(self, bill, other_flatmate):
        flatmates_total_days_in_house = 0
        flatmates_total_days_in_house += other_flatmate.days_in_house
        weight = self.days_in_house / (self.days_in_house + flatmates_total_days_in_house)
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

        # Insert Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align='C', ln=1)

        # Insert Period label and value
        pdf.cell(w=100, h=40, txt="Period", border=1)
        pdf.cell(w=0, h=40, txt=bill.period, border=1, ln=1)

        # Insert flatmate
        pdf.cell(w=200, h=40, txt=flatmates.name, border=1)
        pdf.cell(w=200, h=40, txt=str(flatmates.days_in_house), border=1, ln=1)

        # Generate PDF
        pdf.output(self.filename)


the_bill = Bill(amount=120, period="April 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print(john.name, " pays: ", john.pays(bill=the_bill, other_flatmate=marry))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(john, the_bill)
