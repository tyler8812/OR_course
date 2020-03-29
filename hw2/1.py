from pulp import *

# material cost s1
Mcost_tvp_11 = {
    "1": 10.5,
    "2": 10.4,
    "3": 10.3,
    "4": 10.2,
    "5": 10.1
}
Mcost_tvp_12 = {
    "1": 6.5,
    "2": 6.4,
    "3": 6.3,
    "4": 6.2,
    "5": 6.1
}
Mcost_tvp_13 = {
    "1": 8.5,
    "2": 8.4,
    "3": 8.3,
    "4": 8.2,
    "5": 8.1
}
# material cost s2
Mcost_tvp_21 = {
    "1": 20.5,
    "2": 20.4,
    "3": 20.3,
    "4": 20.2,
    "5": 20.1
}
Mcost_tvp_22 = {
    "1": 7.5,
    "2": 7.4,
    "3": 7.3,
    "4": 7.2,
    "5": 7.1
}
Mcost_tvp_23 = {
    "1": 7.5,
    "2": 7.4,
    "3": 7.3,
    "4": 7.2,
    "5": 7.1
}


# production cost
Pcost_tfg = {
    "f1": 0.4,
    "f2": 0.45
}

# transportation cost from supplier to facilities
VF_Tcost = 0.01

# transportation cost from facilities to warehouse
FW_Tcost = {
    "f1w1": 0.2,
    "f1w2": 0.3,
    "f2w1": 0.5,
    "f2w2": 0.1
}

# transportation cost from warehouse to customer
WC_Tcost = {
    "w1c1": 0.6,
    "w1c2": 0.4,
    "w1c3": 0.3,
    "w2c1": 0.3,
    "w2c2": 0.5,
    "w2c3": 0.4
}

# inventory cost of materials in facilities
FM_Icost = {
    "f1": 0.02,
    "f2": 0.01
}

# inventory cost of goods in facilities
FG_Icost ={
    "f1": 0.1,
    "f2": 0.09
}

# inventory cost of goods in warehouse
W_Icost = {
    "w1": 0.07,
    "w2": 0.05
}


# amount of meterial needed for producing goods
BOM = {
    "p1": 1,
    "p2": 2,
    "p3": 3
}

# demand of goods by customer at time
LC_tcg_c1 = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 30,
    "5": 55
}
LC_tcg_c2 = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 20,
    "5": 40
}
LC_tcg_c3 = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 10,
    "5": 50
}



# inventory of meterial in facility
LF_tfp_t1 = {
    "f1p1": 200,
    "f1p2": 300,
    "f1p3": 300,
    "f2p1": 100,
    "f2p2": 100,
    "f2p3": 100
}

time = {"1", "2", "3", "4", "5"}


prob = LpProblem("The Supply Chain Problem", LpMinimize)

# amount of metrial purchased by supplier p1 from s1
lvtvp_var_11 = LpVariable.dicts("lvtvp_var_11", time, lowBound = 0, upBound = 500, cat="Integer")
# amount of metrial purchased by supplier p2 from s1
lvtvp_var_12 = LpVariable.dicts("lvtvp_var_12", time, lowBound = 0, upBound = 500, cat="Integer")
# amount of metrial purchased by supplier p3 from s1
lvtvp_var_13 = LpVariable.dicts("lvtvp_var_13", time, lowBound = 0, upBound = 500, cat="Integer")
# amount of metrial purchased by supplier p1 from s2
lvtvp_var_21 = LpVariable.dicts("lvtvp_var_21", time, lowBound = 0, upBound = 500, cat="Integer")
# amount of metrial purchased by supplier p2 from s2
lvtvp_var_22 = LpVariable.dicts("lvtvp_var_22", time, lowBound = 0, upBound = 500, cat="Integer")
# amount of metrial purchased by supplier p3 from s2
lvtvp_var_23 = LpVariable.dicts("lvtvp_var_23", time, lowBound = 0, upBound = 500, cat="Integer")



# raw material transported from suppliers to s1 f1 p1
Rtvfp_var_111 = LpVariable.dicts("Rtvfp_var_111", time, lowBound = 0, cat="Integer")
# raw material transported from suppliers to s1 f1 p2
Rtvfp_var_112 = LpVariable.dicts("Rtvfp_var_112", time, lowBound = 0, cat="Integer")
# raw material transported from suppliers to s1 f1 p3
Rtvfp_var_113 = LpVariable.dicts("Rtvfp_var_113", time, lowBound = 0, cat="Integer")
# raw material transported from suppliers to s1 f2 p1
Rtvfp_var_121 = LpVariable.dicts("Rtvfp_var_121", time, lowBound = 0, cat="Integer")
# raw material transported from suppliers to s1 f2 p2
Rtvfp_var_122 = LpVariable.dicts("Rtvfp_var_122", time, lowBound = 0, cat="Integer")
# raw material transported from suppliers to s1 f2 p3
Rtvfp_var_123 = LpVariable.dicts("Rtvfp_var_123", time, lowBound = 0, cat="Integer")
# raw material transported from suppliers to s2 f1 p1
Rtvfp_var_211 = LpVariable.dicts("Rtvfp_var_211", time, lowBound = 0, cat="Integer")
# raw material transported from suppliers to s2 f1 p2
Rtvfp_var_212 = LpVariable.dicts("Rtvfp_var_212", time, lowBound = 0, cat="Integer")
# raw material transported from suppliers to s2 f1 p3
Rtvfp_var_213 = LpVariable.dicts("Rtvfp_var_213", time, lowBound = 0, cat="Integer")
# raw material transported from suppliers to s2 f2 p1
Rtvfp_var_221 = LpVariable.dicts("Rtvfp_var_221", time, lowBound = 0, cat="Integer")
# raw material transported from suppliers to s2 f2 p2
Rtvfp_var_222 = LpVariable.dicts("Rtvfp_var_222", time, lowBound = 0, cat="Integer")
# raw material transported from suppliers to s2 f2 p3
Rtvfp_var_223 = LpVariable.dicts("Rtvfp_var_223", time, lowBound = 0, cat="Integer")



# amount of goods which f1 produced at time
Rtfg_var_1 = LpVariable.dicts("Rtfg_var_1", time, lowBound = 0, upBound = 70, cat="Integer")
# amount of goods which f2 produced at time
Rtfg_var_2 = LpVariable.dicts("Rtfg_var_2", time, lowBound = 0, upBound = 35, cat="Integer")

# inventory of p1 in f1
LFtfp_var_11 = LpVariable.dicts("LFtfp_var_11", time, lowBound = 0, cat="Integer")
# inventory of p2 in f1
LFtfp_var_12 = LpVariable.dicts("LFtfp_var_12", time, lowBound = 0, cat="Integer")
# inventory of p3 in f1
LFtfp_var_13 = LpVariable.dicts("LFtfp_var_13", time, lowBound = 0, cat="Integer")
# inventory of p1 in f2
LFtfp_var_21 = LpVariable.dicts("LFtfp_var_21", time, lowBound = 0, cat="Integer")
# inventory of p2 in f2
LFtfp_var_22 = LpVariable.dicts("LFtfp_var_22", time, lowBound = 0, cat="Integer")
# inventory of p3 in f2
LFtfp_var_23 = LpVariable.dicts("LFtfp_var_23", time, lowBound = 0, cat="Integer")


# INventory of goods in f1
LFtfg_var_1 = LpVariable.dicts("LFtfg_var_1", time, lowBound = 0, cat="Integer")
# INventory of goods in f2
LFtfg_var_2 = LpVariable.dicts("LFtfg_var_2", time, lowBound = 0, cat="Integer")

# inventory of goods in w1
LWtwg_var_1 = LpVariable.dicts("LWtwg_var_1", time, lowBound = 0, upBound = 400, cat="Integer")
# inventory of goods in w2
LWtwg_var_2 = LpVariable.dicts("LWtwg_var_2", time, lowBound = 0, upBound = 500, cat="Integer")

# amount of goods transported from f1 to w1
Rtfwg_11 = LpVariable.dicts("Rtfwg_11", time, lowBound = 0, cat="Integer")
# amount of goods transported from f1 to w2
Rtfwg_12 = LpVariable.dicts("Rtfwg_12", time, lowBound = 0, cat="Integer")
# amount of goods transported from f2 to w1
Rtfwg_21 = LpVariable.dicts("Rtfwg_21", time, lowBound = 0, cat="Integer")
# amount of goods transported from f2 to w2
Rtfwg_22 = LpVariable.dicts("Rtfwg_22", time, lowBound = 0, cat="Integer")

# amount of goods transport from w1 to c1
Rtwcg_11 = LpVariable.dicts("Rtwcg_11", time, lowBound = 0, cat="Integer")
# amount of goods transport from w1 to c2
Rtwcg_12 = LpVariable.dicts("Rtwcg_12", time, lowBound = 0, cat="Integer")
# amount of goods transport from w1 to c3
Rtwcg_13 = LpVariable.dicts("Rtwcg_13", time, lowBound = 0, cat="Integer")
# amount of goods transport from w2 to c1
Rtwcg_21 = LpVariable.dicts("Rtwcg_21", time, lowBound = 0, cat="Integer")
# amount of goods transport from w2 to c2
Rtwcg_22 = LpVariable.dicts("Rtwcg_22", time, lowBound = 0, cat="Integer")
# amount of goods transport from w2 to c3
Rtwcg_23 = LpVariable.dicts("Rtwcg_23", time, lowBound = 0, cat="Integer")



#加入目標式

prob += lpSum([Mcost_tvp_11[i] * lvtvp_var_11[i] + Mcost_tvp_12[i] * lvtvp_var_12[i] + Mcost_tvp_13[i] * lvtvp_var_13[i] + Mcost_tvp_21[i] * lvtvp_var_21[i] + Mcost_tvp_22[i] * lvtvp_var_22[i] + Mcost_tvp_23[i] * lvtvp_var_23[i]
+ VF_Tcost * (Rtvfp_var_111[i] + Rtvfp_var_112[i] + Rtvfp_var_113[i] + Rtvfp_var_121[i] + Rtvfp_var_122[i] + Rtvfp_var_123[i] + Rtvfp_var_211[i] + Rtvfp_var_212[i] + Rtvfp_var_213[i] + Rtvfp_var_221[i] + Rtvfp_var_222[i] + Rtvfp_var_223[i])
+ Pcost_tfg["f1"] * Rtfg_var_1[i] + Pcost_tfg["f2"] * Rtfg_var_2[i] 
+ FM_Icost["f1"] * (LFtfp_var_11[i] + LFtfp_var_12[i] + LFtfp_var_13[i]) + FM_Icost["f2"] * (LFtfp_var_21[i] + LFtfp_var_22[i] + LFtfp_var_23[i])
+ FG_Icost["f1"] * LFtfg_var_1[i] + FG_Icost["f2"] * LFtfg_var_2[i]
+ W_Icost["w1"] * LWtwg_var_1[i] + W_Icost["w2"] * LWtwg_var_2[i]
+ FW_Tcost["f1w1"] * Rtfwg_11[i] + FW_Tcost["f1w2"] * Rtfwg_12[i] + FW_Tcost["f2w1"] * Rtfwg_21[i] + FW_Tcost["f2w2"] * Rtfwg_22[i]
+ WC_Tcost["w1c1"] * Rtwcg_11[i] + WC_Tcost["w1c2"] * Rtwcg_12[i] + WC_Tcost["w1c3"] * Rtwcg_13[i] + WC_Tcost["w2c1"] * Rtwcg_21[i] + WC_Tcost["w2c2"] * Rtwcg_22[i] + WC_Tcost["w2c3"] * Rtwcg_23[i]
for i in time])

prob += LFtfp_var_11["1"] == 200
prob += LFtfp_var_12["1"] == 300
prob += LFtfp_var_13["1"] == 300
prob += LFtfp_var_21["1"] == 100
prob += LFtfp_var_22["1"] == 100
prob += LFtfp_var_23["1"] == 100

prob += LFtfg_var_1["1"] == 0
prob += LFtfg_var_2["1"] == 0

prob += LWtwg_var_1["1"] == 0
prob += LWtwg_var_2["1"] == 0


prob += Rtvfp_var_111["1"] + Rtvfp_var_121["1"] == lvtvp_var_11["1"]
prob += Rtvfp_var_111["2"] + Rtvfp_var_121["2"] == lvtvp_var_11["2"]
prob += Rtvfp_var_111["3"] + Rtvfp_var_121["3"] == lvtvp_var_11["3"]
prob += Rtvfp_var_111["4"] + Rtvfp_var_121["4"] == lvtvp_var_11["4"]
prob += Rtvfp_var_111["5"] + Rtvfp_var_121["5"] == lvtvp_var_11["5"]
prob += Rtvfp_var_112["1"] + Rtvfp_var_122["1"] == lvtvp_var_12["1"]
prob += Rtvfp_var_112["2"] + Rtvfp_var_122["2"] == lvtvp_var_12["2"]
prob += Rtvfp_var_112["3"] + Rtvfp_var_122["3"] == lvtvp_var_12["3"]
prob += Rtvfp_var_112["4"] + Rtvfp_var_122["4"] == lvtvp_var_12["4"]
prob += Rtvfp_var_112["5"] + Rtvfp_var_122["5"] == lvtvp_var_12["5"]
prob += Rtvfp_var_113["1"] + Rtvfp_var_123["1"] == lvtvp_var_13["1"]
prob += Rtvfp_var_113["2"] + Rtvfp_var_123["2"] == lvtvp_var_13["2"]
prob += Rtvfp_var_113["3"] + Rtvfp_var_123["3"] == lvtvp_var_13["3"]
prob += Rtvfp_var_113["4"] + Rtvfp_var_123["4"] == lvtvp_var_13["4"]
prob += Rtvfp_var_113["5"] + Rtvfp_var_123["5"] == lvtvp_var_13["5"]
prob += Rtvfp_var_211["1"] + Rtvfp_var_221["1"] == lvtvp_var_21["1"]
prob += Rtvfp_var_211["2"] + Rtvfp_var_221["2"] == lvtvp_var_21["2"]
prob += Rtvfp_var_211["3"] + Rtvfp_var_221["3"] == lvtvp_var_21["3"]
prob += Rtvfp_var_211["4"] + Rtvfp_var_221["4"] == lvtvp_var_21["4"]
prob += Rtvfp_var_211["5"] + Rtvfp_var_221["5"] == lvtvp_var_21["5"]
prob += Rtvfp_var_212["1"] + Rtvfp_var_222["1"] == lvtvp_var_22["1"]
prob += Rtvfp_var_212["2"] + Rtvfp_var_222["2"] == lvtvp_var_22["2"]
prob += Rtvfp_var_212["3"] + Rtvfp_var_222["3"] == lvtvp_var_22["3"]
prob += Rtvfp_var_212["4"] + Rtvfp_var_222["4"] == lvtvp_var_22["4"]
prob += Rtvfp_var_212["5"] + Rtvfp_var_222["5"] == lvtvp_var_22["5"]
prob += Rtvfp_var_213["1"] + Rtvfp_var_223["1"] == lvtvp_var_23["1"]
prob += Rtvfp_var_213["2"] + Rtvfp_var_223["2"] == lvtvp_var_23["2"]
prob += Rtvfp_var_213["3"] + Rtvfp_var_223["3"] == lvtvp_var_23["3"]
prob += Rtvfp_var_213["4"] + Rtvfp_var_223["4"] == lvtvp_var_23["4"]
prob += Rtvfp_var_213["5"] + Rtvfp_var_223["5"] == lvtvp_var_23["5"]


# prob += Rtvfp_var_12["1"] + Rtvfp_var_22["1"] == lvtvp_var_12["1"] + lvtvp_var_22["1"]
# prob += Rtvfp_var_12["2"] + Rtvfp_var_22["2"] == lvtvp_var_12["2"] + lvtvp_var_22["2"]
# prob += Rtvfp_var_12["3"] + Rtvfp_var_22["3"] == lvtvp_var_12["3"] + lvtvp_var_22["3"]
# prob += Rtvfp_var_12["4"] + Rtvfp_var_22["4"] == lvtvp_var_12["4"] + lvtvp_var_22["4"]
# prob += Rtvfp_var_12["5"] + Rtvfp_var_22["5"] == lvtvp_var_12["5"] + lvtvp_var_22["5"]

# prob += Rtvfp_var_13["1"] + Rtvfp_var_23["1"] == lvtvp_var_13["1"] + lvtvp_var_23["1"]
# prob += Rtvfp_var_13["2"] + Rtvfp_var_23["2"] == lvtvp_var_13["2"] + lvtvp_var_23["2"]
# prob += Rtvfp_var_13["3"] + Rtvfp_var_23["3"] == lvtvp_var_13["3"] + lvtvp_var_23["3"]
# prob += Rtvfp_var_13["4"] + Rtvfp_var_23["4"] == lvtvp_var_13["4"] + lvtvp_var_23["4"]
# prob += Rtvfp_var_13["5"] + Rtvfp_var_23["5"] == lvtvp_var_13["5"] + lvtvp_var_23["5"]


# prob += lpSum([Rtvfp_var_11[i] + Rtvfp_var_21[i] for i in time]) == lpSum([lvtvp_var_11[i] + lvtvp_var_21[i] for i in time])
# prob += lpSum([Rtvfp_var_12[i] + Rtvfp_var_22[i] for i in time]) == lpSum([lvtvp_var_12[i] + lvtvp_var_22[i] for i in time])
# prob += lpSum([Rtvfp_var_13[i] + Rtvfp_var_23[i] for i in time]) == lpSum([lvtvp_var_13[i] + lvtvp_var_23[i] for i in time])


prob += LFtfp_var_11["1"] - Rtfg_var_1["1"] * BOM["p1"] == LFtfp_var_11["2"]
prob += LFtfp_var_12["1"] - Rtfg_var_1["1"] * BOM["p2"] == LFtfp_var_12["2"]
prob += LFtfp_var_13["1"] - Rtfg_var_1["1"] * BOM["p3"] == LFtfp_var_13["2"]
prob += LFtfp_var_21["1"] - Rtfg_var_2["1"] * BOM["p1"] == LFtfp_var_21["2"]
prob += LFtfp_var_22["1"] - Rtfg_var_2["1"] * BOM["p2"] == LFtfp_var_22["2"]
prob += LFtfp_var_23["1"] - Rtfg_var_2["1"] * BOM["p3"] == LFtfp_var_23["2"]


prob += LFtfp_var_11["2"] - Rtfg_var_1["2"] * BOM["p1"] + Rtvfp_var_111["1"] + Rtvfp_var_211["1"] == LFtfp_var_11["3"]
prob += LFtfp_var_11["3"] - Rtfg_var_1["3"] * BOM["p1"] + Rtvfp_var_111["2"] + Rtvfp_var_211["2"] == LFtfp_var_11["4"]
prob += LFtfp_var_11["4"] - Rtfg_var_1["4"] * BOM["p1"] + Rtvfp_var_111["3"] + Rtvfp_var_211["3"] == LFtfp_var_11["5"]
prob += LFtfp_var_12["2"] - Rtfg_var_1["2"] * BOM["p2"] + Rtvfp_var_112["1"] + Rtvfp_var_212["1"] == LFtfp_var_12["3"]
prob += LFtfp_var_12["3"] - Rtfg_var_1["3"] * BOM["p2"] + Rtvfp_var_112["2"] + Rtvfp_var_212["2"] == LFtfp_var_12["4"]
prob += LFtfp_var_12["4"] - Rtfg_var_1["4"] * BOM["p2"] + Rtvfp_var_112["3"] + Rtvfp_var_212["3"] == LFtfp_var_12["5"]
prob += LFtfp_var_13["2"] - Rtfg_var_1["2"] * BOM["p3"] + Rtvfp_var_113["1"] + Rtvfp_var_213["1"] == LFtfp_var_13["3"]
prob += LFtfp_var_13["3"] - Rtfg_var_1["3"] * BOM["p3"] + Rtvfp_var_113["2"] + Rtvfp_var_213["2"] == LFtfp_var_13["4"]
prob += LFtfp_var_13["4"] - Rtfg_var_1["4"] * BOM["p3"] + Rtvfp_var_113["3"] + Rtvfp_var_213["3"] == LFtfp_var_13["5"]
prob += LFtfp_var_21["2"] - Rtfg_var_2["2"] * BOM["p1"] + Rtvfp_var_121["1"] + Rtvfp_var_221["1"] == LFtfp_var_21["3"]
prob += LFtfp_var_21["3"] - Rtfg_var_2["3"] * BOM["p1"] + Rtvfp_var_121["2"] + Rtvfp_var_221["2"] == LFtfp_var_21["4"]
prob += LFtfp_var_21["4"] - Rtfg_var_2["4"] * BOM["p1"] + Rtvfp_var_121["3"] + Rtvfp_var_221["3"] == LFtfp_var_21["5"]
prob += LFtfp_var_22["2"] - Rtfg_var_2["2"] * BOM["p2"] + Rtvfp_var_122["1"] + Rtvfp_var_222["1"] == LFtfp_var_22["3"]
prob += LFtfp_var_22["3"] - Rtfg_var_2["3"] * BOM["p2"] + Rtvfp_var_122["2"] + Rtvfp_var_222["2"] == LFtfp_var_22["4"]
prob += LFtfp_var_22["4"] - Rtfg_var_2["4"] * BOM["p2"] + Rtvfp_var_122["3"] + Rtvfp_var_222["3"] == LFtfp_var_22["5"]
prob += LFtfp_var_23["2"] - Rtfg_var_2["2"] * BOM["p3"] + Rtvfp_var_123["1"] + Rtvfp_var_223["1"] == LFtfp_var_23["3"]
prob += LFtfp_var_23["3"] - Rtfg_var_2["3"] * BOM["p3"] + Rtvfp_var_123["2"] + Rtvfp_var_223["2"] == LFtfp_var_23["4"]
prob += LFtfp_var_23["4"] - Rtfg_var_2["4"] * BOM["p3"] + Rtvfp_var_123["3"] + Rtvfp_var_223["3"] == LFtfp_var_23["5"]


# prob += lpSum([LFtfp_var_12[i] - Rtfg_var_1[i] * BOM["p2"] for i in time2]) + lpSum([Rtvfp_var_12[i] for i in time4]) == lpSum([LFtfp_var_12[i] for i in time3])
# prob += lpSum([LFtfp_var_13[i] - Rtfg_var_1[i] * BOM["p3"] for i in time2]) + lpSum([Rtvfp_var_13[i] for i in time4]) == lpSum([LFtfp_var_13[i] for i in time3])
# prob += lpSum([LFtfp_var_21[i] - Rtfg_var_2[i] * BOM["p1"] for i in time2]) + lpSum([Rtvfp_var_21[i] for i in time4]) == lpSum([LFtfp_var_21[i] for i in time3])
# prob += lpSum([LFtfp_var_22[i] - Rtfg_var_2[i] * BOM["p2"] for i in time2]) + lpSum([Rtvfp_var_22[i] for i in time4]) == lpSum([LFtfp_var_22[i] for i in time3])
# prob += lpSum([LFtfp_var_23[i] - Rtfg_var_2[i] * BOM["p3"] for i in time2]) + lpSum([Rtvfp_var_23[i] for i in time4]) == lpSum([LFtfp_var_23[i] for i in time3])

prob += LFtfg_var_1["1"] - Rtfwg_11["1"] - Rtfwg_12["1"] == LFtfg_var_1["2"]
prob += LFtfg_var_2["1"] - Rtfwg_21["1"] - Rtfwg_22["1"] == LFtfg_var_2["2"]

prob += LFtfg_var_1["2"] - Rtfwg_11["2"] - Rtfwg_12["2"] + Rtfg_var_1["1"] == LFtfg_var_1["3"]
prob += LFtfg_var_1["3"] - Rtfwg_11["3"] - Rtfwg_12["3"] + Rtfg_var_1["2"] == LFtfg_var_1["4"]
prob += LFtfg_var_1["4"] - Rtfwg_11["4"] - Rtfwg_12["4"] + Rtfg_var_1["3"] == LFtfg_var_1["5"]
prob += LFtfg_var_2["2"] - Rtfwg_21["2"] - Rtfwg_22["2"] + Rtfg_var_2["1"] == LFtfg_var_2["3"]
prob += LFtfg_var_2["3"] - Rtfwg_21["3"] - Rtfwg_22["3"] + Rtfg_var_2["2"] == LFtfg_var_2["4"]
prob += LFtfg_var_2["4"] - Rtfwg_21["4"] - Rtfwg_22["4"] + Rtfg_var_2["3"] == LFtfg_var_2["5"]

# prob += lpSum([LFtfg_var_1[i] - Rtfwg_11[i] - Rtfwg_12[i] for i in time2]) + lpSum([Rtfg_var_1[i] for i in time4]) == lpSum([LFtfg_var_1[i] for i in time3])
# prob += lpSum([LFtfg_var_2[i] - Rtfwg_21[i] - Rtfwg_22[i] for i in time2]) + lpSum([Rtfg_var_2[i] for i in time4]) == lpSum([LFtfg_var_2[i] for i in time3])





prob += LWtwg_var_1["1"] - Rtwcg_11["1"] - Rtwcg_12["1"] - Rtwcg_13["1"] == LWtwg_var_1["2"] 
prob += LWtwg_var_2["1"] - Rtwcg_21["1"] - Rtwcg_22["1"] - Rtwcg_23["1"] == LWtwg_var_2["2"] 



prob += LWtwg_var_1["2"] - Rtwcg_11["2"] - Rtwcg_12["2"] - Rtwcg_13["2"] + Rtfwg_11["1"] + Rtfwg_21["1"] == LWtwg_var_1["3"]
prob += LWtwg_var_1["3"] - Rtwcg_11["3"] - Rtwcg_12["3"] - Rtwcg_13["3"] + Rtfwg_11["2"] + Rtfwg_21["2"] == LWtwg_var_1["4"]
prob += LWtwg_var_1["4"] - Rtwcg_11["4"] - Rtwcg_12["4"] - Rtwcg_13["4"] + Rtfwg_11["3"] + Rtfwg_21["3"] == LWtwg_var_1["5"]
prob += LWtwg_var_2["2"] - Rtwcg_21["2"] - Rtwcg_22["2"] - Rtwcg_23["2"] + Rtfwg_12["1"] + Rtfwg_22["1"] == LWtwg_var_2["3"]
prob += LWtwg_var_2["3"] - Rtwcg_21["3"] - Rtwcg_22["3"] - Rtwcg_23["3"] + Rtfwg_12["2"] + Rtfwg_22["2"] == LWtwg_var_2["4"]
prob += LWtwg_var_2["4"] - Rtwcg_21["4"] - Rtwcg_22["4"] - Rtwcg_23["4"] + Rtfwg_12["3"] + Rtfwg_22["3"] == LWtwg_var_2["5"]

# prob += lpSum([LWtwg_var_2[i] - Rtwcg_12[i] - Rtwcg_22[i] - Rtwcg_23[i] for i in time2]) + lpSum([Rtfwg_21[i] + Rtfwg_22[i] for i in time4]) == lpSum([LWtwg_var_2[i] for i in time3])



prob += Rtwcg_11["1"] + Rtwcg_21["1"] == LC_tcg_c1["2"]
prob += Rtwcg_11["2"] + Rtwcg_21["2"] == LC_tcg_c1["3"]
prob += Rtwcg_11["3"] + Rtwcg_21["3"] == LC_tcg_c1["4"]
prob += Rtwcg_11["4"] + Rtwcg_21["4"] == LC_tcg_c1["5"]
prob += Rtwcg_12["1"] + Rtwcg_22["1"] == LC_tcg_c2["2"]
prob += Rtwcg_12["2"] + Rtwcg_22["2"] == LC_tcg_c2["3"]
prob += Rtwcg_12["3"] + Rtwcg_22["3"] == LC_tcg_c2["4"]
prob += Rtwcg_12["4"] + Rtwcg_22["4"] == LC_tcg_c2["5"]
prob += Rtwcg_13["1"] + Rtwcg_23["1"] == LC_tcg_c3["2"]
prob += Rtwcg_13["2"] + Rtwcg_23["2"] == LC_tcg_c3["3"]
prob += Rtwcg_13["3"] + Rtwcg_23["3"] == LC_tcg_c3["4"]
prob += Rtwcg_13["4"] + Rtwcg_23["4"] == LC_tcg_c3["5"]



# prob += lpSum([Rtwcg_11[i] + Rtwcg_21[i] for i in time4]) == lpSum([LC_tcg_c1[i] for i in time2])
# prob += lpSum([Rtwcg_12[i] + Rtwcg_22[i] for i in time4]) == lpSum([LC_tcg_c2[i] for i in time2])
# prob += lpSum([Rtwcg_13[i] + Rtwcg_23[i] for i in time4]) == lpSum([LC_tcg_c3[i] for i in time2])



prob.solve()
#查看目前解的狀態
print("Status:", LpStatus[prob.status])

# int type
#印出解及目標值
for v in prob.variables():
    print(v.name, "=", v.varValue)
print('cost=',value(prob.objective))

