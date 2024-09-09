import pandas as pd
class Weather:
    def weather(self):
        data = pd.read_csv("./weather_data.csv")
        print(data)
     

