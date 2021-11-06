# Press the green button in the gutter to run the script.
import pandas

if __name__ == '__main__':
    data = pandas.read_csv("weather_data.csv")
    print(data["temp"].max())
    d=data[data.day == "Monday"]
    print(d)

    m = data[data.temp.max() == data.temp]

    print(m)


















 #   with open("weather_data.csv") as data_file:
  #      temperatures = []
  #      data = csv.reader(data_file)
   #     for d in data:
    #        temperatures.append(d[1])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
