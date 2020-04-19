# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:38:42 2020

@author: cfing
"""

import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = 0
profit_loss = 0
greatestincrease = ['', 0]
greatestdecrease = ['', 999999999999999999]
netchangelist = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    firstrow = next(csvreader)
    total_months = total_months + 1
    profit_loss = profit_loss + int(firstrow[1])
    prevnetchange = int(firstrow[1])

    for row in csvreader:
        date_col = row[0]
        Profloss_col = int(row[1])
       
        total_months = total_months + 1
        profit_loss = profit_loss + Profloss_col
        netchange = Profloss_col - prevnetchange
        netchangelist.append(netchange)
        prevnetchange == Profloss_col
        # The greatest increase in profits (date and amount) over the entire period
        if netchange > greatestincrease[1]:
            greatestincrease = [date_col, Profloss_col]
        # The greatest decrease in losses (date and amount) over the entire period
        if netchange < greatestdecrease[1]:
            greatestdecrease = [date_col, Profloss_col]
            
            
total_change = sum(netchangelist)
avg_change = int(total_change /total_months)




output= os.path.join("bank.txt")
with open(output, 'w') as txt_file: 
      financial_analysis = (
    f"\n\n--------------------------Financial Analyis-------------------------------\n"
    f'Total Months: {total_months}\n'
    f'Total $: ${profit_loss:,d}\n'
    f'Average Change: ${avg_change:,d}\n'
    f'Greatest increase profit: ${greatestincrease[1]:,d} in {greatestincrease[0]} \n'
    f'Greatest increase loss: ${greatestdecrease[1]:,d} in {greatestdecrease[0]} \n'
    f'++                                 ++                                    ++\n'
    f'-----------------------------End Analysis----------------------------------\n')
      print(financial_analysis, end="")
      txt_file.write(financial_analysis)

