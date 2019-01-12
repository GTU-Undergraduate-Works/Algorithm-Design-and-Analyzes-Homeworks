
# n : number of job to schedule
# time : times array to complete jobs
# weight : weight array of jobs
def maximizeWeightedSum(n, time, weight):
    assert n == len(time) == len(weight) and n > 0, "Invalid input"
    schdule_arr = [0]*n
    for i in range(n):
        schdule_arr[i] = i

    for i in range(len(schdule_arr)):
        key_schedule = schdule_arr[i]
        key_weight = weights[i]
        key_time = times[i]

        j = i-1
        while j >= 0 and float(key_weight/key_time) > weights[j]/times[j]:
            schdule_arr[j+1] = schdule_arr[j]
            weights[j+1] = weights[j]
            times[j+1] = times[j]
            j -= 1
        schdule_arr[j+1] = key_schedule
        weights[j+1] = key_weight
        times[j+1] = key_time
    return schdule_arr




# time array of jobs
# weight array of jobs
def calculateWeghtedSum(time, weight):

    assert len(time) == len(weight) and len(time) > 0, "Invalid Input"
    c = [0]*len(time)
    c[0] = time[0]
    weight_sum = c[0]*weight[0]
    for i in range(1, len(time)):
        c[i] = time[i] + c[i-1]
        weight_sum += c[i]*weight[i]
    return weight_sum



weights = [100, 19, 27, 25, 15, 12, 35, 26]
times = [2,1,2,1,3,4,5,7]



schdule_arr = maximizeWeightedSum(len(times), times, weights)
print("Optimal Scheduling Sequence : ", schdule_arr)
print("Weights of jobs : ", weights)
print("Times to complete jobs : ", times)
print("Weighted Sum of Scheduling :", calculateWeghtedSum(times, weights))







