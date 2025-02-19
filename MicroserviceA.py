import json

while True:
    with open('BudgetTracker.txt','r',encoding='utf-8') as file:
        budgetFile = file.read()
        if budgetFile == 'run':
            with open('ShoppingList.txt','r',encoding='utf-8') as shopFile:
                shoppingListDict = json.load(shopFile)
                budget = shoppingListDict['Budget']
                totalCost = 0
                newShoppingDict = {}
                shoppingListCount = 0
                # calculate shopping list cost
                for key in shoppingListDict:
                    if key != 'Budget':
                        shoppingListCount += 1                       # count number of items in the shopping list
                        totalCost += shoppingListDict[key]           # get total cost of all shopping items
                        newShoppingDict[key] = shoppingListDict[key] # exclude budget from new dictionary
                # calculate if over/under budget
                budgetCalc = budget - totalCost
                # top 3 items or less in the shopping list
                topItemsList = []
                if shoppingListCount > 3:
                    shoppingListCount = 3   # ensures we get only top 3 items
                for i in range(0,shoppingListCount):
                    shoppingListTopItem = max(newShoppingDict,key=newShoppingDict.get)
                    print(shoppingListTopItem)
                    topItemsList.append(shoppingListTopItem)
                    newShoppingDict.pop(shoppingListTopItem) # pop item from dictionary
                # create object to send to client
                if budgetCalc < 0:
                    budgetTracker = 'Sorry you went over budget :('
                else:
                    budgetTracker = 'Congratulations you are within your budget :)'
                budgetObject = { 'Budget': budgetTracker,
                                 'Top Items': topItemsList

                }
            # write budget object to the Budget Tracker text file
            with open('BudgetTracker.txt','w',encoding='utf-8') as budgetFile:
                json.dump(budgetObject,budgetFile)





