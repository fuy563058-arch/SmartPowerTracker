class ApplianceManager:
    #Keeps the list of appliance records.

    def __init__(self, appliances=None):
        #Starts with the given records, or an empty list.
        self.appliances = appliances if appliances is not None else []

    def add_appliance(self, name, wattage, hours):
        #Creates a new appliance record and adds it to the list.
        appliance = {"name": name, "wattage": wattage, "hours": hours}
        self.appliances.append(appliance)
        return appliance

    def view_appliances(self):
        #Returns the list of saved appliance records.
        return self.appliances

    def search_appliance(self, keyword):
        #Finds appliances whose name contains the keyword.
        keyword = keyword.strip().lower()
        matches = []
        for index, appliance in enumerate(self.appliances):
            if keyword in appliance["name"].lower():
                matches.append((index, appliance))
        return matches

    def delete_appliance(self, index):
        #Removes the appliance at the given position, or returns None.
        if 0 <= index < len(self.appliances):
            return self.appliances.pop(index)
        return None