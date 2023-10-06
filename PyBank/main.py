import os
import csv

#Set Path
csvpath = os.path.join("C:/Users/Owner/git/python-challenge/PyBank/Resources/budget_data.csv")

#Set Variables
months = []
profit_loss = []
profit_loss_change = []

#Read CSV
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

#Skip Header Row
    csv_header = next(csvreader)

#Append Total Months and Total Profit
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

#Find Total Profit Change
    for x in range(1, len(profit_loss)):
        profit_loss_change.append(profit_loss[x] - (profit_loss[x-1]))

#Find The Average Change
average_change = round(sum(profit_loss_change) / len(profit_loss_change), 2)

#Find Greatest Profit Increase/Decrease
greatest_increase = max(profit_loss_change)
greatest_decrease = min(profit_loss_change)

#Index For Corresponding Month to Profit(received help from tutor[Bigyan])
max_index = profit_loss_change.index(max(profit_loss_change))
max_month = months[max_index + 1]

min_index = profit_loss_change.index(min(profit_loss_change))
min_month = months[min_index + 1]

#Print Analysis
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: $ {sum(profit_loss)}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {max_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {min_month} (${greatest_decrease})")


#Set Text Path
textpath = os.path.join("C:/Users/Owner/git/python-challenge/PyBank/analysis/output.txt")

#Write Text File
with open(textpath, 'w') as textfile:
    
    textfile.write("Financial Analysis\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Months: {len(months)}\n")
    textfile.write(f"Total: $ {sum(profit_loss)}\n")
    textfile.write(f"Average Change: {average_change}\n")
    textfile.write(f"Greatest Increase in Profits: {max_month} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {min_month} (${greatest_decrease})\n")

     
