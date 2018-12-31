def optimal_stop(input):
    hotel = input
    best_path = [None]*len(hotel)
    stop =  [None]*len(hotel)
    for i in range(len(hotel)):
        best_path[i] = int(pow(200-hotel[i], 2))
        stop[i] = 0
        for j in range(i):
            if best_path[j] + pow((200 - (hotel[i] - hotel[j])), 2) < best_path[i]:
                best_path[i] = int(best_path[j] + pow((200 - (hotel[i] - hotel[j])),2))
                stop[i] = j+1



    print("Minimal penalty : ", best_path[len(hotel)-1])
    final_path = ""
    index = len(stop)-1
    while index >= 0:
        final_path = str(index+1) + " " + final_path
        index = stop[index]-1
    print(stop)
    print("Stop at: " + final_path)




input = [190, 220, 410, 580, 640, 770, 950, 1100, 1350]
optimal_stop(input)