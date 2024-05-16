import os
import csv
#establishing path to resources folder and csv data file 

budget_csv = os.path.join("Resources","budget_data.csv")
#declaring variables
total_months = 0
total_profit = 0 #sum of monthly profits

monthly_difference = 0
total_differences = 0 #sum of differences

profit_diff_max = 0 #min and max for monthly profit differences 
profit_diff_min = 0

last_profit = 0

date_max = ""
date_min = ""

#opens csv file, skipping header
with open(budget_csv, encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")
    csv_header = next(csv_reader)
    
    
    #reading through rows in file
    for row in csv_reader:

        monthly_profit = int(row[1])
        total_months += 1
        total_profit += monthly_profit
        if total_months > 1:
            monthly_difference = monthly_profit - last_profit

        total_differences += monthly_difference
        #checking for new max and min and their dates
        if monthly_difference > profit_diff_max:
            profit_diff_max = monthly_difference
            date_max = str(row[0])
        elif (monthly_difference < profit_diff_min):
            profit_diff_min = monthly_difference
            date_min = str(row[0])
        
        last_profit = monthly_profit

#total average of profit and average of differences in monthly profit
average_differences = total_differences / (total_months - 1)

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}") 
print(f"Total: ${total_profit}") 
print(f"Average Change: ${average_differences:.2f}") 
print(f"Greatest Increase In Profits: {date_max} (${profit_diff_max})") 
print(f"Greatest Decrease in Profits: {date_min} (${profit_diff_min})") 