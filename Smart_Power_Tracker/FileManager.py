class FileManager:
    #Reads and writes appliance records to a text file.

    def __init__(self, filename="appliances.txt"):
        #Sets the file used to store the records.
        self.filename = filename

    def save_data(self, appliances):
        #Rewrites the file with the current list of appliances.
        with open(self.filename, "w") as file:
            for appliance in appliances:
                record = f"{appliance['name']},{appliance['wattage']},{appliance['hours']}"
                file.write(record + "\n")

    def load_data(self):
        #Reads the saved records, or returns an empty list if the file is missing.
        appliances = []
        try:
            with open(self.filename, "r") as file:
                records = file.readlines()
            for record in records:
                record = record.strip()
                if not record:
                    continue
                name, wattage, hours = record.split(",")
                appliances.append({
                    "name": name,
                    "wattage": float(wattage),
                    "hours": float(hours),
                })
        except FileNotFoundError:
            print("No saved records found. Starting with an empty list.")
        return appliances