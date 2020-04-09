from pulp import *
import math
import time
import matplotlib.pyplot as plt
p = {
    "1": 8,
    "2": 8,
    "3": 8,
    "4": 8,
    "5": 9,
    "6": 9,
    "7": 9,
    "8": 9,
    "9": 9,
    "10": 18,
    "11": 18,
    "12": 18
}
q = {
    "1": 16,
    "2": 16,
    "3": 16,
    "4": 16,
    "5": 9,
    "6": 9,
    "7": 9,
    "8": 9,
    "9": 9,
    "10": 3,
    "11": 3,
    "12": 3
}

rel = {
    "12", "13", "14", "15", "16", "17", "18", "19", "110", "111", "112",
    "23", "24", "25", "26", "27", "28", "29", "210", "211","212",
    "34", "35", "36", "37", "38", "39", "310", "311","312",
    "45", "46", "47", "48", "49", "410", "411","412",
    "56", "57", "58", "59", "510", "511","512",
    "67", "68", "69", "610", "611","612",
    "78", "79", "710", "711","712",
    "89", "810", "811","812",
    "910", "911","912",
    "1011","1012",
    "1112",
}
num = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"}

M = 170
ans_x = []
ans_y = []
ans_z = []
count = 0
start = 5
end = 20
middle = 4

for i in range(start, end, middle):
    prob = LpProblem("The Cutting-stock Problem", LpMinimize)

    x = LpVariable('x', lowBound = 0, cat='Integer')
    y = LpVariable('y', lowBound = 0, cat='Integer')

    xr = LpVariable.dicts('xr', num, lowBound = 0, cat='Integer')
    yr = LpVariable.dicts('yr', num, lowBound = 0, cat='Integer')
    sr = LpVariable.dicts('sr', num, lowBound = 0, upBound = 1, cat='Integer')

    u = LpVariable.dicts('u', rel, lowBound = 0, upBound = 1, cat='Integer')
    v = LpVariable.dicts('v', rel, lowBound = 0, upBound = 1, cat='Integer')
    space = i
    print(i)
    if M%space == 0:
        big_m = int(M/space)-1
    else: 
        big_m = int(M/space)
    ux = LpVariable.dicts('ux', range(2, big_m+1), lowBound = 0, upBound = 1, cat='Integer')
    wx = LpVariable.dicts('wx', range(2, big_m+1), lowBound = 0, cat='Integer')
    uy = LpVariable.dicts('uy', range(2, big_m+1), lowBound = 0, upBound = 1, cat='Integer')
    wy = LpVariable.dicts('wy', range(2, big_m+1), lowBound = 0, cat='Integer')



    l = []


    for i in range(1, big_m):
        l.append((math.log(i*space+1, 10) - math.log((i-1)*space+1, 10))/space)

    prob += lpSum(math.log(1, 10) + l[0] * (x - 1) / (big_m-2)
    + (l[i-1] - l[i-2]) * ((1+(i-1)*space) * ux[i] + x - (1+(i-1)*space) - wx[i])
    + math.log(1, 10) + l[0] * (y - 1) / (big_m-2)
    + (l[i-1] - l[i-2]) * ((1+(i-1)*space) * uy[i] + y - (1+(i-1)*space) - wy[i])
    for i in range(2, big_m)
    )

    for i in range (2, big_m+1):
        prob += (-M) * ux[i] <= x - (i)
        prob += (M) * (1 - ux[i]) >= x - (i)
        prob += (-M) * ux[i] <= wx[i]
        prob += (M) * ux[i] >= wx[i]
        prob += (M) * (ux[i] - 1) + x <= wx[i]
        prob += (M) * (1 - ux[i]) + x >= wx[i]
    

        prob += (-M) * uy[i] <= y - (i)
        prob += (M) * (1 - uy[i]) >= y - (i)
        prob += (-M) * uy[i] <= wy[i]
        prob += (M) * uy[i] >= wy[i]
        prob += (M) * (uy[i] - 1) + y <= wy[i]
        prob += (M) * (1 - uy[i]) + y >= wy[i]


    for i in range (3, big_m+1):
        prob += ux[i] >= ux[i-1]
        prob += uy[i] >= uy[i-1]


    for i in num:
        temp = int(i)
        for j in range (temp + 1, 13):    
            t1 = str(i)
            t2 = str(j)
            t3 = t1+t2
            prob += xr[t1] - xr[t2] + u[t3] * M + v[t3] * M >= (p[t1] * sr[t1] + q[t1] * (1 - sr[t1]) + p[t2] * sr[t2] + q[t2] * (1 - sr[t2]))/2
            prob += yr[t1] - yr[t2] + u[t3] * M + (1 - v[t3]) * M >= (p[t1] * (1 - sr[t1]) + q[t1] * sr[t1] + p[t2] * (1 - sr[t2]) + q[t2] * sr[t2])/2

    for i in num:
        temp = int(i)
        for j in range (temp-1, 0, -1):
            t1 = str(i)
            t2 = str(j)
            t3 = t2+t1
            prob += xr[t1] - xr[t2] + (1 - u[t3]) * M + v[t3] * M >= (p[t2] * sr[t2] + q[t2] * (1 - sr[t2]) + p[t1] * sr[t1] + q[t1] * (1 - sr[t1]))/2
            prob += yr[t1] - yr[t2] + (1 - u[t3]) * M + (1 - v[t3]) * M >= (p[t2] * (1 - sr[t2]) + q[t2] * sr[t2] + p[t1] * (1 - sr[t1]) + q[t1] * sr[t1])/2

    prob += x <= M
    for i in num:
        prob += x >= xr[i] + (p[i] * sr[i] + q[i] * (1 - sr[i]))/2
        prob += y >= yr[i] + (p[i] * (1 - sr[i]) + q[i] * sr[i])/2
        prob += xr[i] >= (p[i] * sr[i] + q[i] * (1 - sr[i]))/2
        prob += yr[i] >= (p[i] * (1 - sr[i]) + q[i] * sr[i])/2

    tic = time.clock()
    prob.solve()
    toc = time.clock()
    # #查看目前解的狀態
    # print("Status:", LpStatus[prob.status])

    # # int type
    # #印出解及目標值
    # for v in prob.variables():
    #     print(v.name, "=", v.varValue)
    
    print('cost=',value(prob.objective))
    print(x, "=", x.value())
    print(y, "=", y.value())
    print("change:")
    print(x, "=", x.value()-1)
    print(y, "=", y.value()-1)
    print('cost=',(x.value()-1)*(y.value()-1)) 
    print("time:",toc-tic)
    ans_x.append((x.value()-1)*(y.value()-1))
    ans_y.append(count*middle+start)
    ans_z.append(toc-tic)
    count = count + 1

plt.plot(ans_y, ans_x)
plt.show()
plt.plot(ans_y, ans_z)
plt.show()