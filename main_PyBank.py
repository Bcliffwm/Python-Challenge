import os
import csv

# Importing the mean function
from statistics import mean

#creating path to collect data from PyBank
budget_data = os.path.join('PyBank', 'budget_data.csv')

# defining the function
def print_analysis(profits_losses):
# assign values to the variables
    #dates = str(bank_data[0])
    bank_data = []
    bank_data = profits_losses

    # Calculating total months with len in range(bank_data)
    months = len(profit_loss_list)
    print(f'Total number of months is {months}')


    # Calculating the total net amount over entire period
    net_amount = sum(bank_data)
    print(f'Net total is {net_amount}')

    # Calculating total average of changes over entire period
    net_change = mean(profit_loss_list)
    print(f'Net change over period is {net_change}')

    # Finding greatest increase in profits
    profit_maximum = max(profit_loss_list)
    print(f'Greatest increase in profit is {profit_maximum}')

    # Finding greatest decrease in profits/greatest losses
    profit_minimum = min(profit_loss_list)
    print(f'Greatest decrease in profit is {profit_minimum}')

#reading csv file 
with open(budget_data, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
#creating lists
    with open('budget_data2.csv', 'w') as new_file:
        fieldnames = ['Date', 'Profit/Losses']
#separating lines using tabs
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()
        profit_loss_list = []

        for line in csv_reader:
        #loop through the data in csv_reader
        #for each line print out the "Date" and "Profit/Loss"
           # print_analysis(line)
           profit_loss_list.append(int(line["Profit/Losses"]))

           #print (line['Date'], line['Profit/Losses'])
            #csv_writer.writerow(line)
            #profit_loss_list = profit_loss_list.insert(line - 1)- need to fill profit/loss list

        print(profit_loss_list)

        print_analysis(profit_loss_list)
            #break