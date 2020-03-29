from pulp import *
food = ['bread', 'peanut', 'jelly', 'cracker', 'milk', 'juice']
costs = {'bread': 5,
         'peanut': 4,
         'jelly': 7,
         'cracker': 8,
         'milk': 15,
         'juice': 35}

protein = {'bread': 3,
           'peanut': 4,
           'jelly': 0,
           'cracker': 1,
           'milk': 8,
           'juice': 1}

vitamin_c = {'bread': 0,
              'peanut': 0,
              'jelly': 3,
              'cracker': 0,
              'milk': 2,
              'juice': 120}

calories = {'bread': 70,
            'peanut': 100,
            'jelly': 50,
            'cracker': 60,
            'milk': 150,
            'juice': 100}

fat = { 'bread': 10,
        'peanut': 75,
        'jelly': 0,
        'cracker': 20,
        'milk': 70,
        'juice': 0}


prob = LpProblem("The child Problem", LpMinimize)

food_vars = LpVariable.dicts("Food", food, cat="Integer")
#加入目標式
prob += lpSum([costs[i] * food_vars[i] for i in food])

prob += lpSum([calories[i] * food_vars[i] for i in food]) >= 400
prob += lpSum([calories[i] * food_vars[i] for i in food]) <= 600
prob += lpSum([vitamin_c[i] * food_vars[i] for i in food]) >= 60 
prob += lpSum([protein[i] * food_vars[i] for i in food]) >= 12
prob += lpSum(food_vars[food[0]]) == 2
prob += lpSum([food_vars[food[1]] - 2 * food_vars[food[2]]]) >= 0
prob += lpSum([food_vars[food[4]] +  food_vars[food[5]]]) >= 1
prob += lpSum([-11 * food_vars[food[0]] + 45 * food_vars[food[1]] - 15 * food_vars[food[2]] + 2 * food_vars[food[3]] + 25 * food_vars[food[4]] - 30 * food_vars[food[5]]]) <= 0

prob.solve()
#查看目前解的狀態
print("Status:", LpStatus[prob.status])

# int type
#印出解及目標值
for v in prob.variables():
    print(v.name, "=", v.varValue)
print('cost=',value(prob.objective))

###################################################################


prob = LpProblem("The child Problem", LpMinimize)

food_vars = LpVariable.dicts("Food", food, 0)

prob += lpSum([costs[i] * food_vars[i] for i in food])

prob += lpSum([calories[i] * food_vars[i] for i in food]) >= 400
prob += lpSum([calories[i] * food_vars[i] for i in food]) <= 600
prob += lpSum([vitamin_c[i] * food_vars[i] for i in food]) >= 60 
prob += lpSum([protein[i] * food_vars[i] for i in food]) >= 12
prob += lpSum(food_vars[food[0]]) == 2
prob += lpSum([food_vars[food[1]] - 2 * food_vars[food[2]]]) >= 0
prob += lpSum([food_vars[food[4]] +  food_vars[food[5]]]) >= 1
prob += lpSum([-11 * food_vars[food[0]] + 45 * food_vars[food[1]] - 15 * food_vars[food[2]] + 2 * food_vars[food[3]] + 25 * food_vars[food[4]] - 30 * food_vars[food[5]]]) <= 0

prob.solve()

#查看目前解的狀態
print("Status:", LpStatus[prob.status])

# continuous type
#解的另一種方式
for i in food:
    print(food_vars[i],"=",food_vars[i].value())
print('cost=',value(prob.objective))
