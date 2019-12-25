# import libraries 
import os
import csv

# file path for csv 
csvpath = os.path.join("Resources", "budget_data.csv")

# declare variables: months, profit losses, month changes, increases, greatest month increaes
total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
month_change = 0
total_month_change = 0
average_month_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_increase_month = ""

# csv open 
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")   
    csv_header = next(csvreader)
# begin for loop  
    for row in csvreader:
        total_months += 1
        
        total_profit_loss += int(row[1])
        
        if total_months > 1:
            month_change = int(row[1]) - prev_profit_loss
            
        total_month_change += month_change   
        prev_profit_loss = int(row[1])
        
        if month_change > greatest_increase:
            greatest_increase = month_change
            greatest_increase_month = row[0]
        
        if month_change < greatest_decrease:
            greatest_decrease = month_change
            greatest_decrease_month = row[0]

# divide for average change between months        
average_month_change = total_month_change / (total_months - 1)

# terminal print w/lines for visual 
print("Financial Analysis")
print("----------------------------")        
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit_loss))
print("Average Change: $" + str(format(average_month_change, '.2f')))
print("Greatest Increase in Profits: " + greatest_increase_month 
      + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_month 
      + " ($" + str(greatest_decrease) + ")")

# print to file in PyBank folder
f = open("analysis.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")        
f.write("Total Months: " + str(total_months) + "\n")
f.write("Total: $" + str(total_profit_loss) + "\n")
f.write("Average Change: $" + str(format(average_month_change, '.2f')) + "\n")
f.write("Greatest Increase in Profits: " + greatest_increase_month 
      + " ($" + str(greatest_increase) + ")\n")
f.write("Greatest Decrease in Profits: " + greatest_decrease_month 
      + " ($" + str(greatest_decrease) + ")\n")
f.close()
