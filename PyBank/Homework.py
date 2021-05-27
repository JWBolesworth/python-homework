import pandas as pd
from pathlib import Path

csvpath = Path('../PyBank/budget_data.csv')


budgetDataFrame = pd.read_csv(csvpath)

budgetDataFrame.head()

budgetDataFrame = budgetDataFrame.dropna (how = 'any', axis=0)
budgetDataFrame.head()

print('--------------Financial Analysis----------------')

(totalMonths) = budgetDataFrame.count()[0]
print("Total Months:" + str(totalMonths))


total = sum(budgetDataFrame['Profit/Losses'])
print('Total:' + str(total))


budgetDataFrame['shifted'] = budgetDataFrame['Profit/Losses'].shift(1)

budgetDataFrame['difference'] = budgetDataFrame['Profit/Losses'] - budgetDataFrame['shifted']

print(budgetDataFrame.head)

budgetDataFrame = budgetDataFrame.dropna (how = 'any', axis=0)
print(budgetDataFrame.head)

averageDelta = sum(budgetDataFrame['difference']) / totalMonths

print(averageDelta)

maxDelta = budgetDataFrame['difference'].max()
print('Greatest increase:' + str(maxDelta))

minDelta = budgetDataFrame['difference'].min()

print('Greatest decrease: ' + str(minDelta))





f = open("summaryOutput.txt", "a")


print('--------------Final Answers----------------', file=f)

print("Total Months:" + str(totalMonths), file=f)
print('Total:' + str(total), file=f)
print('Average Change:' + str(averageDelta), file=f)
print('Greatest increase:' + str(maxDelta), file=f)
print('Greatest decrease: ' + str(minDelta), file=f)




f.close()