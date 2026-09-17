class Calculations:
    #Performs all consumption and cost calculations.

    ELECTRICITY_RATE = 12

    def daily_consumption(self, wattage, hours):
        #Returns the daily consumption in kWh.
        return (wattage * hours) / 1000

    def monthly_consumption(self, daily_kwh, days=30):
        #Returns the monthly consumption in kWh.
        return daily_kwh * days

    def monthly_cost(self, monthly_kwh, rate=None):
        #Returns the estimated monthly cost in pesos.
        if rate is None:
            rate = self.ELECTRICITY_RATE
        return monthly_kwh * rate

    def calculate_all(self, wattage, hours, rate=None):
        #Runs the three formulas and returns the results as a dictionary.
        daily = self.daily_consumption(wattage, hours)
        monthly = self.monthly_consumption(daily)
        cost = self.monthly_cost(monthly, rate)
        return {
            "daily_kwh": daily,
            "monthly_kwh": monthly,
            "monthly_cost": cost,
        }

    def compare_appliances(self, appliances):
        #Sorts appliances from highest to lowest monthly consumption.
        return sorted(
            appliances,
            key=lambda a: self.monthly_consumption(
                self.daily_consumption(a["wattage"], a["hours"])
            ),
            reverse=True,
        )

    def highest_consuming(self, appliances):
        #Returns the appliance with the highest monthly consumption.
        if not appliances:
            return None
        return max(
            appliances,
            key=lambda a: self.monthly_consumption(
                self.daily_consumption(a["wattage"], a["hours"])
            ),
        )