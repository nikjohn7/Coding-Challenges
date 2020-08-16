def organizingContainers(container):
    eachContainer = []
    eachType = []
    n = len(container)
    for i in range(0,n):
        eachContainer.append(sum(container[i]))
        j = 0
        tot = 0
        for j in range(0,n):
            tot += container[j][i]
        eachType.append(tot)
    eachContainer.sort()
    eachType.sort()
    if eachContainer==eachType:
        return "Possible"
    else:
        return "Impossible"