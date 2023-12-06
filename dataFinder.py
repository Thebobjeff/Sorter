# Created by Devonte Edward 17/02/2023.
# The following program will be used to assit in sorting though invontory.
import pandas as pd

#Calling file into script
data = pd.read_csv('Inventory-WearHouse.csv')
file = pd.DataFrame(data)

#Function used to find items 
def finder(sku, info):
    count = 0
    # file = pd.DataFrame(info)
    for index,row in info.iterrows():
        if row['SKU']== sku:
            print(file.iloc[count])
            break
        else:
            count = count +1

print(finder("764608051610", data))

