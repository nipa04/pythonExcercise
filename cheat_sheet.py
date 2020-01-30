#############################
#           List            #
#############################
# Creating
data = []

# Adding to list
data.append(100)
data.append(23)
data.append(23)
data.append(43)
data.append(54)
data.append(26)
data.append(557)
print(data)

# check if item exist
if 54 in data:
    print("found")


# Find item. Loop it
for item in data:
    if item == 1:
        print("Found")

# Use range to loop
for index in range(0, len(data)):
    print(data[index])

# Sort data
# sortedData = sorted(xList, key=lambda item: item.name)
sortedData = sorted(data)
print(sortedData)

#############################
#           Stack           #
#############################
# Creating
stack = []

# Adding to Stack
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# Delete or pop from stack
stack.pop()
print(stack)

#############################
#           Queue           #
#############################
# Creating
queue = []

# Adding to Queue
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# Deleting from Queue
queue.pop(0)
print(queue)

#############################
#           Dictionary      #
#############################
# Creating
dataDict = {}

# Adding to dictionary
dataDict[5] = "Five"
dataDict[1] = "One"
dataDict[2] = "Two"
dataDict[3] = "Three"
print(dataDict)

# Get a value from dictionary
v = dataDict[1]
print(v)

# Delete from dictionary
del dataDict[1]
print(dataDict)

# Check if data exist in dictionary
if 2 in dataDict:
    print("Found")

# Loop through dictionary
for k, v in dataDict.items():
    print(k, v)

# Sort dictionary by key
for key in sorted(dataDict.keys()):
    print(key, " ::", dataDict[key])

# Sort dictionary by value
# sorted_x = sorted(x.items(), key=lambda kv: kv[1])
for elem in sorted(dataDict.items()):
    print(elem[0], " ::", elem[1])
