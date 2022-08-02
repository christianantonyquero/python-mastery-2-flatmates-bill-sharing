from bill import Bill
from flatmate import Flatmate
from reports import PdfReport

# Enter bill information
bill_amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the billing period? E.g. December 2022: ")
the_bill = Bill(amount=bill_amount, period=period)

# Enter flatmate details
number_of_flat_mates = int(input("Number of flatmates?: "))
flatmate_list = []

for number in range(1, number_of_flat_mates + 1):
    name = input("Enter flatmate " + str(number) + " name: ")
    days_in_house = int(input("Enter how many days" + name + "stayed in the house during the bill period: "))

    flatmate = Flatmate(name, days_in_house)
    flatmate_list.append(flatmate)

pdf_report = PdfReport(filename=f"{the_bill.period}_Report.pdf")
pdf_report.generate(flatmate_list, the_bill)
