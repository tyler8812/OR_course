from pulp import *

facility = {"1", "2", "3", "4"}
# existing facility
existing_facility_x = {
    "1": 0,
    "2": 4,
    "3": 6,
    "4": 10

}

existing_facility_y = {
    "1": 2,
    "2": 0,
    "3": 8,
    "4": 4
    
}

weight_to_facility_1 = {
    "1": 5,
    "2": 3,
    "3": 0,
    "4": 0
}

weight_to_facility_2 = {
    "1": 0,
    "2": 1,
    "3": 8,
    "4": 4
}

one_to_two = 6





prob = LpProblem("The Supply Chain Problem", LpMinimize)


x1 = LpVariable('x1', lowBound = 0, cat='Integer')
x2 = LpVariable('x2', lowBound = 0, cat='Integer')
y1 = LpVariable('y1', lowBound = 0, cat='Integer')
y2 = LpVariable('y2', lowBound = 0, cat='Integer')

iteraction_p_x_1 = LpVariable('ipx1', lowBound = 0, cat='Integer')
iteraction_q_x_1 = LpVariable('iqx1', lowBound = 0, cat='Integer')
iteraction_p_x_2 = LpVariable('ipx2', lowBound = 0, cat='Integer')
iteraction_q_x_2 = LpVariable('iqx2', lowBound = 0, cat='Integer')

iteraction_p_y_1 = LpVariable('ipy1', lowBound = 0, cat='Integer')
iteraction_q_y_1 = LpVariable('iqy1', lowBound = 0, cat='Integer')
iteraction_p_y_2 = LpVariable('ipy2', lowBound = 0, cat='Integer')
iteraction_q_y_2 = LpVariable('iqy2', lowBound = 0, cat='Integer')

weight_x_r_1 = LpVariable.dicts("wxr1", facility, lowBound = 0, cat="Integer")
weight_x_s_1 = LpVariable.dicts("wxs1", facility, lowBound = 0, cat="Integer")
weight_x_r_2 = LpVariable.dicts("wxr2", facility, lowBound = 0, cat="Integer")
weight_x_s_2 = LpVariable.dicts("wxs2", facility, lowBound = 0, cat="Integer")

weight_y_r_1 = LpVariable.dicts("wyr1", facility, lowBound = 0, cat="Integer")
weight_y_s_1 = LpVariable.dicts("wys1", facility, lowBound = 0, cat="Integer")
weight_y_r_2 = LpVariable.dicts("wyr2", facility, lowBound = 0, cat="Integer")
weight_y_s_2 = LpVariable.dicts("wys2", facility, lowBound = 0, cat="Integer")

#加入目標式

prob += lpSum([
one_to_two / len(facility)  * (iteraction_p_x_1 + iteraction_q_x_1)          
+ one_to_two / len(facility)  * (iteraction_p_y_1 + iteraction_q_y_1)
+ weight_to_facility_1[i] * (weight_x_r_1[i] + weight_x_s_1[i])
+ weight_to_facility_1[i] * (weight_y_r_1[i] + weight_y_s_1[i])
+ weight_to_facility_2[i] * (weight_x_r_2[i] + weight_x_s_2[i])
+ weight_to_facility_2[i] * (weight_y_r_2[i] + weight_y_s_2[i])
for i in facility])

prob += x1 - iteraction_q_x_1 + iteraction_p_x_1 == x2
prob += x2 - iteraction_q_x_2 + iteraction_p_x_2 == x1
prob += y1 - iteraction_q_y_1 + iteraction_p_y_1 == y2
prob += y2 - iteraction_q_y_2 + iteraction_p_y_2 == y1

prob +=  x1 - weight_x_r_1["1"] + weight_x_s_1["1"] - existing_facility_x["1"]  == 0  
prob +=  x1 - weight_x_r_1["2"] + weight_x_s_1["2"] - existing_facility_x["2"]  == 0
prob +=  x1 - weight_x_r_1["3"] + weight_x_s_1["3"] - existing_facility_x["3"]  == 0
prob +=  x1 - weight_x_r_1["4"] + weight_x_s_1["4"] - existing_facility_x["4"]  == 0
prob +=  x2 - weight_x_r_2["1"] + weight_x_s_2["1"] - existing_facility_x["1"]  == 0  
prob +=  x2 - weight_x_r_2["2"] + weight_x_s_2["2"] - existing_facility_x["2"]  == 0
prob +=  x2 - weight_x_r_2["3"] + weight_x_s_2["3"] - existing_facility_x["3"]  == 0
prob +=  x2 - weight_x_r_2["4"] + weight_x_s_2["4"] - existing_facility_x["4"]  == 0


prob +=  y1 - weight_y_r_1["1"] + weight_y_s_1["1"] - existing_facility_y["1"]  == 0  
prob +=  y1 - weight_y_r_1["2"] + weight_y_s_1["2"] - existing_facility_y["2"]  == 0
prob +=  y1 - weight_y_r_1["3"] + weight_y_s_1["3"] - existing_facility_y["3"]  == 0
prob +=  y1 - weight_y_r_1["4"] + weight_y_s_1["4"] - existing_facility_y["4"]  == 0
prob +=  y2 - weight_y_r_2["1"] + weight_y_s_2["1"] - existing_facility_y["1"]  == 0  
prob +=  y2 - weight_y_r_2["2"] + weight_y_s_2["2"] - existing_facility_y["2"]  == 0
prob +=  y2 - weight_y_r_2["3"] + weight_y_s_2["3"] - existing_facility_y["3"]  == 0
prob +=  y2 - weight_y_r_2["4"] + weight_y_s_2["4"] - existing_facility_y["4"]  == 0




prob.solve()
#查看目前解的狀態
print("Status:", LpStatus[prob.status])

# int type
#印出解及目標值
for v in prob.variables():
    print(v.name, "=", v.varValue)
print('cost=',value(prob.objective))





# test1 = {
#     "1": 1,
#     "2": 2,
#     "3": 3,
#     "4": 4

# }

# test2 = {
#     "1": 1,
#     "2": 2,
#     "3": 3,
#     "4": 4

# }
# for i in facility:
#     print(test1[i], test2[i])

