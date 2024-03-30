import csv

class csvFile():
    def __init__(self, file_name):
        self.x_value = 0
        self.y_value = 0
        self.field_names = ["x_value", "y_value"]
        self.file_name = file_name
        
        with open(self.file_name, "w") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.field_names)
            csv_writer.writeheader()

    def append(self, x, y):
        with open(self.file_name,"a") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.field_names)

            info  = {
                "x_value": self.x_value,
                "y_value": self.y_value
            }
            self.x_value = x
            self.y_value = y
            csv_writer.writerow(info)