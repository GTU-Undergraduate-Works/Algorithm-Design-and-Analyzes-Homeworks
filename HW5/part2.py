# n : number of months
# M : switch cost
# N : array of New York operating cost
# S : array of San Francisco operating cost
def findMinimumCost(n, M, N, S):
    assert n == len(N) == len(S), "Invalid Input"
    OPT_n = [0]*n
    OPT_s = [0]*n
    OPT_n[0] = N[0]
    OPT_s[0] = S[0]
    plan_n = ["NY"]*n
    plan_s = ["SF"]*n
    for i in range(1,n):
        OPT_n[i] = N[i] + min(OPT_n[i-1], M + OPT_s[i-1])
        OPT_s[i] = S[i] + min(OPT_s[i-1], M + OPT_n[i-1])

    for i in range(1,n):
        if OPT_n[i-1] < M + OPT_s[i-1]:
            OPT_n[i] = N[i] + OPT_n[i-1]
            plan_n[i-1] = "NY"
        else:
            OPT_n[i] = N[i] + M + OPT_s[i-1]
            plan_n[i-1] = "SF"

        if OPT_s[i-1] < M + OPT_n[i-1]:
            OPT_s[i-1] = S[i] + OPT_s[i-1]
            plan_s[i-1] = "SF"
        else:
            OPT_s[i] = S[i] + M + OPT_n[i-1]
            plan_s[i-1] = "NY"


    if OPT_n[n-1] < OPT_s[n-1]:
        return OPT_n[n-1], plan_n
    return OPT_s[n-1], plan_s




S = [50, 39, 45, 2, 3, 150, 75]
N = [20, 3, 4, 50, 100, 1, 20]
M = 10

minimum_cost, optimum_plan = findMinimumCost(len(N), M, N, S)

print("Moving Cost : ", M)
print("Operation Cost of New York by months : ", N)
print("Operation Cost of San Francisco by months : ", S)

print("Optimal Plan with minimum cost : ", optimum_plan)
print("Cost of optimal plan : ", minimum_cost)


