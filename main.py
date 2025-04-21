#MapPlot.py
#Name: Daud Daud
#Date: 4/20/25
#Assignment: Lab 10

import food
import pandas
import matplotlib.pyplot as plt
report = food.get_report()


#print(report[0]["Data"]["Fat"]["Total Lipid"])

Values = []
Keys = []

for item in report:
    Key = item["Data"]["Vitamins"]["Vitamin B12"]
    Value = item["Data"]["Fat"]["Total Lipid"]
    if  Keys != 0:
     Keys.append(Key)
     Values.append(Value)
    #print(Value, Key)

df = pandas.DataFrame({"Key": Keys,
                        "Value": Values})   

print(df)
df.plot(kind = 'scatter', x = 'Key', y = 'Value')

plt.savefig("Output")