class Suggestions:
    #Generates an energy-saving tip for an appliance.

    def energy_suggestion(self, appliance, calculations, hours_to_cut=2):
        #Returns a tip and the estimated monthly savings.
        current = calculations.calculate_all(appliance["wattage"], appliance["hours"])

        if appliance["hours"] > hours_to_cut:
            reduced_hours = appliance["hours"] - hours_to_cut
            reduced = calculations.calculate_all(appliance["wattage"], reduced_hours)
            savings = current["monthly_cost"] - reduced["monthly_cost"]
            return (
                f"Reduce usage by {hours_to_cut} hours/day to lower your \n"
                f"estimated bill by about P{savings:.2f}/month."
            )

        return "Usage is already low. Consider an energy-efficient model for further savings."