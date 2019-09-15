##PyBank

# Dependencies
import csv
import os

# file input 
PyBank = os.path.join("Resources", "budget_data.csv")

# Variables & Counters
profit_loss=[]
total=0
total_months=0
subtract_MoM=0
tot_MoM=0
Avg_MoM=0

with open(PyBank) as csvfile:
    budget_reader=csv.reader(csvfile,delimiter=',')
    next(budget_reader)
    
    for line in budget_reader:
        profit_loss.append(line)
        # The total net amount of "Profit/Losses" 
        total+=int(line[1])
        # The total number of months included in the dataset
        total_months+=1
       

    # Max increase and Max decrease values with latest increase/decrease value
    max_decrease=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])
    max_increase=int(profit_loss[total_months-1][1])-int(profit_loss[total_months-2][1])
    
    # Changes in "Profit/Losses" between months 
    for i in range(total_months,1,-1):
        subtract_MoM=int(profit_loss[i-1][1])-int(profit_loss[i-2][1])
        
        # Greatest Increase (max_increase) and Greatest Decrease (max_decrease)
        if subtract_MoM < max_decrease:
            min_month_yr=profit_loss[i-1][0]
            max_decrease=subtract_MoM
        elif subtract_MoM > max_increase:
            max_increase=subtract_MoM
            max_month_yr=profit_loss[i-1][0]
        
        # Total amount change in "Profit/Losses" between months
        tot_MoM=tot_MoM+subtract_MoM
        # print(tot_MoM)
    
    #Average change in "Profit/Losses" between months   
    Avg_MoM=tot_MoM/(total_months-1)     
    # print(Avg_MoM)


# Terminal Results
print("----------------------------------------------------------")
print('Financial Analysis')
print("----------------------------------------------------------")
print('Total Months: '+str(total_months))
print('Total: $'+str(total))
print('Average  Change: $'+str(Avg_MoM))
print('Greatest Increase in Profits: '+max_month_yr+' ($'+str(max_increase)+')')
print('Greatest Decrease in Profits: '+min_month_yr+' ($'+str(max_decrease)+')')
print("----------------------------------------------------------")

# Text File Results
with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------")
    text.write("  Financial Analysis"+ "")
    text.write("----------------------------------------------------------")
    text.write('Total Months: '+str(total_months))
    text.write('Total: $'+str(total))
    text.write('Average  Change: $'+str(Avg_MoM))
    text.write('Greatest Increase in Profits: '+max_month_yr+' ($'+str(max_increase)+')')
    text.write('Greatest Decrease in Profits: '+min_month_yr+' ($'+str(max_decrease)+')')
    text.write("----------------------------------------------------------")