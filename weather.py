import csv
class Weather:
    def weather(self):
        temperatures =[]
        with open("./weather_data.csv") as weather_file:
            data = csv.reader(weather_file)
            for row in data:
                if row[1] != "temp":
                    temperatures.append(int(row[1]))
        print(temperatures)
     

