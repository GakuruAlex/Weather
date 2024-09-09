class Weather:
    def weather(self):
        with open("./weather_data.csv", "r") as weather_file:
            weather_data = weather_file.readlines()
        print(weather_data)
        return weather_data
    def man_weather_data(self):
        data_dict = []
        weather_data = self.weather()
        for data in weather_data:
            day, temp, condition = data.strip().split(",")
            data_dict.append({"day": day, "temp": temp, "condition": condition})
        return data_dict

