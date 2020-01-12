import os
import csv

# Importing the mean function
from statistics import mean

#creating path to collect data from PyBank
election_data = os.path.join('election_data.csv')

# defining the function
def print_analysis(voting_data):
 # Assigning values to variables with descriptive names
    #voting_count = 0
    #Candidate_names = str(fieldnames[2])

    # Calculating total number of votes with len in range(election_data)
    total_votes = len(voting_data)
    print(f'Total number of votes is {total_votes}.')

    # Assigning values to variables with descriptive names
    voting_count = 0
    #Candidate_names = str(fieldnames[2])
    

#reading csv file 
with open(election_data, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
#creating lists
    with open('election_data2.csv', 'w') as new_file:
        fieldnames = ['Voter ID', 'County', 'Candidate']
#separating lines using tabs
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()
        voting_stats_list = []

        for line in csv_reader:
        #loop through the data in csv_reader
        #for each line print out the "Voter ID", "County" and "Candidate"
            #print_analysis(line)
            voting_stats_list.append(str(line["Candidate"]))
            
            # Tabulating votes for each candidate
            if voting_stats_list == line[1]:
                voting_count = voting_count + 1

            else: voting_count = 0

           
            csv_writer.writerow(line)
            
        print_analysis(voting_stats_list)

    #print_analysis(voting_stats_list)
            #break