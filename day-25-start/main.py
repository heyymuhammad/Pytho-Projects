# # with open(".\day-25-start\weather_data.csv") as weather_data:
# #     data = weather_data.readlines()
# #     print(data)

# # import csv

# # with open(".\day-25-start\weather_data.csv") as weather_data:
# #     data = csv.reader(weather_data)
# #     temperature = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperature.append(int(row[1]))
# #     print(temperature)

# import pandas 

# data = pandas.read_csv(".\day-25-start\weather_data.csv")
# # print(type(data))
# # print(data["temp"])

# temp_list = data["temp"].to_list()

# # average_temp = sum(temp_list)/ len(temp_list)
# # print(average_temp)

# # print(data["temp"].mean()) ## average value of temperature
# # print(data["temp"].max()) ## max value in temperature column
# # print(data["temp"].min()) ## min value in temperature column

# ##Get data in row
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data["temp"].max()])

# ##Get specific row's specific column
# # monday= data[data.day == "Monday"]
# # print(monday.condition)

# ##Celcius into Farenheit
# # monday= data[data.day == "Monday"]
# # farhenheit = (monday.temp * 9/5) + 32
# # print(farhenheit)

# ##Dataframes from Scratch
# data_dict = {
#     "students": ["Amy", "Flora", "Pris"],
#     "scores": [72, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)

# data.to_csv(".\day-25-start\new_csv.csv")

import pandas

data = pandas.read_csv("./day-25-start/Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)


data_dict = {
    "Fur COlor": ["Gray", "Cinnamon","Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
