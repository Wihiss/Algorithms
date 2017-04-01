dataArray = [8,1,3,0,4,2,9,7,6,5]
print("Insertion Sort")
print("Source Array:")
print(dataArray)
for i in range(1, len(dataArray)):
    j = i
    #print("j=", j)
    while (j > 0 and (dataArray[j] < dataArray[j - 1])):
           tmp = dataArray[j]
           dataArray[j] = dataArray[j - 1]
           dataArray[j - 1] = tmp
           j = j-1
    #print("After Iteration", i, ":")
print("Sorted Array:")
print(dataArray)

