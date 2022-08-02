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
