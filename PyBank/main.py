
#Dependencies
import os
import csv

#csv directory

csvpath = os.path.join("Resources", "budget_data.csv")

#define average function:

def average(list):
    sum=0
    for x in list:
        sum += x
    return sum/len(list)

with open(csvpath, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile)

    #Store and iterate csv header
    csvheader = str(next(csvreader))

    #declare results dictioanry 

    results = {}

    #declare months and PnL changes list
    months = []
    changes_pnl = []


    #initialize net PnL
    net_pnl = int(0)

    #initialize PnL storage objects
    pnl_alpha = float(0)
    pnl_omega = float(0)

    #initialize alternating counter; allows storage of pnl_alpha and pnl_omega on alternating rows
    alt_counter = False
    first_row = True

    for row in csvreader:

        #Append to months list
        months.append(row[0])

        #Logical test to save change in PnL

        if first_row == True:

            pnl_alpha = float(row[1])
            first_row = False

        elif alt_counter == False:

            pnl_omega = float(row[1])

            #Stage and append changes
            change =  pnl_omega - pnl_alpha
            changes_pnl.append(change)

            #alternate counter to true
            alt_counter = True

        else: 
            
            pnl_alpha = float(row[1])

            #Stage and append changes
            change = pnl_alpha - pnl_omega
            changes_pnl.append(change)
            
            #alternate counter back to false
            alt_counter = False

        #Add to total PnL
        net_pnl += int(row[1])
        

    #------- Calculations of results

    #Total months calculated by length of list
    total_months = len(months)

    #Total Profit and Loss
    total_pnl = str(f"${net_pnl}")

    #Calculations of greatest increase/decrease in profits

        #initialize greatest and lowest objects

    greatest = changes_pnl[0]
    lowest = changes_pnl[0]

    #Calculate the amount and months of the greatest increase/decrease

    for row in changes_pnl:

        if row > greatest:
            greatest = row
            greatest_month_index = int(changes_pnl.index(row) + 1)
            greatest_month = months[greatest_month_index]
        
        elif row < lowest:
            lowest = row
            lowest_month_index = int(changes_pnl.index(row) + 1)
            lowest_month = months[lowest_month_index]


    #remove decimals by changing to integer
    greatest = int(greatest)
    lowest = int(lowest)

    #Store in strings

    greatest_increase = str(f"{greatest_month} (${greatest})")
    greatest_decrease = str(f"{lowest_month} (${lowest})")


    #Average change in Profit and Losses
    average_pnl_change = round(average(changes_pnl),2)

    #store in results dictionary

    results = {
    "Total Months":total_months, 
    "Total":total_pnl,
    "Average Change":average_pnl_change,
    "Greatest Increase in Profits": greatest_increase,
    "Greatest Decrease in Profits": greatest_decrease}


#print analysis to terminal
print("Financial Analysis")
print("----------------------------")
for i in results: 
    print(f"{i}: {results[i]}")

#Write results in txt file

outpath = os.path.join("analysis", "financial-analysis.txt")

with open(outpath, 'w') as output:

    writer = csv.writer(output)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])

    [writer.writerow([f"{i}: {results[i]}"]) for i in results]
