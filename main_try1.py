import os
import csv
import pandas as pd
import numpy as np
import sys

# Importing the mean function
from statistics import mean

def total_votes():
    return str(len(bd))

def candidates_list(candidates):
    unique_candidates = []
    for x in candidates:
        if x not in unique_candidates:
            unique_candidates.append(x)
    for x in unique_candidates:
        print(x)

#def voting_stats():

def main():
    #Assign path components
    #creating path to collect data from PyPoll
    election_data = os.path.join('PyPoll', 'election_data.csv')
    #print joined path components
    #print election_data

    #Read election_data csv into Dictionary
    election_dict = {}
    with open(election_data, newline= '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            election_dict[row["Voter ID"]] = str(row["Candidate"])
    
    #Create DataFrame from Dicitonary
    election_df = pd.DataFrame.from_dict(list(election_dict.items()))
    election_df.columns = ["Voter ID", "County", "Candidate"]
    #print(election_df.head())

    #Create column for total_votes for total number of votes
    election_df["Count"] = 0
    for index, row in election_df.iterrows():
        if index == 0:
            election_df.at[index, "Count"]=0
        #else
        break
