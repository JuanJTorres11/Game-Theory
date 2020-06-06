
players = 0
tree = {}

with open("./data.txt") as dataFile:
    players = int(dataFile.readline().split(":")[1].strip())
    dataFile.readline()
    text = dataFile.readline()
    while text != "":
        arr = text.split(';')
        if arr[1] == 'F':
            tree[arr[0]] = {'isLeaf': 'F', 'children': arr[2][1:-1].split(','), 'player': arr[3].replace("\n","")}
        elif arr[1] == 'T':
            tree[arr[0]] = {'isLeaf': 'T', 'payoffs': arr[2].replace("\n","")[1:-1].split(',')}
        text = dataFile.readline()
    
print(tree)
