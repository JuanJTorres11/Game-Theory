players = 0
tree = {}
with open("./data.txt") as dataFile:
    players = int(dataFile.readline().split(":")[1].strip())
    dataFile.readline()
    text = dataFile.readline()
    while text != "":
        arr = text.split(';')
        if arr[1] == 'F':
            tree[arr[0]] = {'isLeaf': 'F', 'children': arr[2][1:-1].split(','), 'player': int(arr[3].replace("\n",""))}
        elif arr[1] == 'T':
            tree[arr[0]] = {'isLeaf': 'T', 'payoffs': arr[2].replace("\n","")[1:-1].split(',')}
        text = dataFile.readline()

def induction(node:str) -> None :
    if (tree[node]['isLeaf'] == 'F'):
        pair = () # set of (best choice at the moment, payoff of that choice)
        for i in tree[node]['children']:
            induction(i)
            if len(pair) != 0:
                num1 = int(tree[i]['best'][1][tree[node]['player']-1])
                num2 = int(pair[1][tree[node]['player']-1])
                if ( num1 > num2 ):
                    pair = (i, tree[i]['best'][1])
            else:
                pair = (i, tree[i]['best'][1])
        tree[node]['best'] = pair
    else:
        tree[node]['best'] = (node, tree[node]['payoffs'])

def bestStrategy () -> str :
    msj = f"{'Node':^10}{'Player':^10}{'Best Option':^10}\n"
    node = tree['0']
    current = 0
    while node['isLeaf'] == 'F':
        msj += f"{current:^10}{node['player']:^10}{node['best'][0]:^10}\n"
        current = node['best'][0]
        node = tree[node['best'][0]]
    msj += f"The payoff is {node['best'][1]} in the node {current}"
    return msj

print('Wellcome to the Game theory application!!')
#print('Please input a node id:')
#node = input()
#while node not in tree:
#    print('Selected node is not a part of the tree')
#    print('Please input a valid node id:')
#    node = input()

#print("\nSelected node is ({})\n".format(node))
induction('0')
print(bestStrategy())
