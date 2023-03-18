#budget_data_read

# Import modules
import os
import csv

# Set Variables
total_months=0
total_pl=0
value=0
change=0
dates=[]
profits=[]


# creating file path
budget_data_csv=os.path.join('..','Resources','budget_data.csv')

#open and read file
with open(budget_data_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    
    #reading header row
    csv_header=next(csv_reader)
    print(f'Header:{csv_header}')

    #read first row
    first_row=next(csv_reader)
    total_months += 1
    total_pl += int(first_row[1])
    value=int(first_row[1])

    for row in csv_reader:
        #track dates
        dates.append(row[0])

        #calculate the change
        change =int(row[1])-value
        profits.append(change)
        value=int(row[1])

        #total months
        total_months +=1

        #total profit/lossses
        total_pl=total_pl+ int(row[1])

    
    #Greatese Increse
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date=dates[greatest_index]

    #greatest decrease
    greatest_decrease=min(profits)
    worst_index =profits.index(greatest_decrease)
    worst_date=dates[worst_index]

    #average change
    average_change =sum(profits)/len(profits)

#results
print('Financial Analysis')
print('-----------------------------------')
print(f'Total_months:{str(total_months)}')
print(f'Total: ${str(total_pl)}')
print(f'Average Change: ${str(round(average_change,2))}')
print(f'Greatest Increase: {greatest_date}(${str(greatest_increase)})')
print(f'Greatest_Decrease: {worst_date}(${str(greatest_decrease)})')


#expoert to .txt file
output=open("output.txt","w")

line1='Financial Analysis'
line2='---------------------'
line3=str(f"Total Months: {str(total_months)}")
line4=str(f'Total: ${str(total_pl)}')
line5=(f'Average Change: ${str(round(average_change,2))}')
line6=(f'Greatest Increase: {greatest_date}(${str(greatest_increase)})')
line7=(f'Greatest_Decrease: {worst_date}(${str(greatest_decrease)})')
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))