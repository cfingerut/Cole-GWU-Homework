import os
import csv

cereal_csv = os.path.join("../Resources", "cereal.csv")


with open(cereal_csv) as file:
    cereal_reader= csv.reader(file)
    next (cereal_reader, None)
    
    for x in cereal_reader:
        cereal_id= x[0]
        fiber_amount = x[7]
        if float(fiber_amount) >= 5:
            print (f'{cereal_id} has {fiber_amount} grams of tasty fiber')
            