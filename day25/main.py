# with open("weather_data.csv", "r") as data_file:
#    data = data_file.readlines()
#    print(data) 

#Another oprtion using CSV format ( Comma Separated Values)
# import csv
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)
        
#Another option in order to manage more data is importing Pandas Library
#It is not an inbuilt library we need to install it.
#Always work with Pandas for csv data
# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# #Series data
# temp_list = data["temp"].to_list()
# print(len(temp_list))

# #To calculate the average temperature we use the mean() function
# print(data["temp"].mean())

# #To get the max value we use the max() function
# print(data["temp"].max())

# #Get data in Columns
# print(data["condition"])

# #Another way to get the data in Columns, Pandas converts the condition in atributes
# print(data.condition)

#Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# #convert temperature from farenheit to Celsius
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# #Create a DataFrame from Scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "Scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


#Working with Squirrel data 
import pandas

data = pandas.read_csv("squirrel_data.csv")
gray_squirrel_color_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_color_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrel_color_count, cinnamon_squirrel_color_count, black_squirrel_color_count],
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")