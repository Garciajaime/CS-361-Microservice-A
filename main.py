import time
import json

while True:
    budgetCheck = input('Would you like to check to see if you are within your budget? (y/n): ')
    if budgetCheck == 'y':
        with open('BudgetTracker.txt','w',encoding='utf-8') as file:
            file.write('run')
            time.sleep(1)
        with open('BudgetTracker.txt','r', encoding='utf-8') as file:
            budgetInfo = json.load(file)