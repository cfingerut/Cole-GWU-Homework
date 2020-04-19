# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 17:46:21 2020

@author: cfing
"""
import os
import csv



# List out all relevant variables
votetotal = 0

voterid = []
khanlist= []
lilist= []
correylist= []
otooleylist = []



csvpath = os.path.join('Resources','election_data.csv')
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) 
    
    for row in csvreader:
        voter_col= row[0]
        candidate_col = row[2]
        
    #The total number of votes cast
        votetotal = votetotal + 1
#A complete list of candidates who received votes
        if candidate_col == 'Khan' :
            khanlist.append(candidate_col)
        if candidate_col == "Li":
            lilist.append(candidate_col)
        if candidate_col == "Correy":
            correylist.append(candidate_col)
        if candidate_col == "O'Tooley":
            otooleylist.append(candidate_col)

Khan = len(khanlist) 
Li = len(lilist)           
Correy = len(correylist) 
Otooley = len(otooleylist) 

finalists = [Khan, Correy, Li, Otooley]
winner = max(finalists)
winner_supreme = ' '
if winner == Khan:
    winner_name = "Khan"
elif winner == Li:
    winner_name = "Li"
elif winner == Correy:
    winner_name = 'Correy'
else: winner_name = "O'Tooley"



 
#The percentage of votes each candidate won Take new variables used in "len" function and divide by votetotal?
Khanpercent = float(Khan / votetotal) 
Lipercent = float(Li / votetotal) 
Correypercent = float(Correy / votetotal) 
Otooleypercent = float(Otooley / votetotal)
#The total number of votes each candidate won

#The winner of the election based on popular vote.


output= os.path.join('pollingresults.txt')
with open(output,'w') as txt_file:
    results= (f'The Results are in...\n'
              f' The total amount of votes cast: {votetotal}\n'
              f'  Breakdown of votes by candidate: \n'
              f' \t\t Khan----{Khan}\n\t\t Li----{Li}\n\t\t Correy----{Correy}\n\t\t OTooley----{Otooley}\n'
              f'  Percentage of vote won by candidate: \n'
              f' \t\t Khan ({Khanpercent:,.2%}) \n\t\t Li ({Lipercent:,.2%}) \n\t\t Correy ({Correypercent:,.2%}) \n\t\t OTooley ({Otooleypercent:,.2%})\n'
              f' And your new Galactic Emporer is {winner_supreme}..........KHAAAAAAAAAAAAAAAAAAAN!')
    print(results)
    txt_file.write(results)
