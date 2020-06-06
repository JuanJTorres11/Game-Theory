import math, pprint
players = 0
tree = {}
pp = pprint.PrettyPrinter(indent=2)
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

def induction(node):
    string = ""
    if (tree[node]['isLeaf'] == 'F'):
        pair = None
        for i in tree[node]['children']:
            induction(i)
            if pair != None:
                num1 = tree[i]['best'][1][tree[node]['player']-1]
                num2 = pair[1][tree[node]['player']-1]
                if ( num1 > num2 ):
                    pair = (i, tree[i]['best'][1])
            else:
                pair = (i, tree[i]['best'][1])
        tree[node]['best'] = pair
    else:
        tree[node]['best'] = (node, tree[node]['payoffs'])

print('Wellcome to the Game theory application!!')
#print('Please input a node id:')
#node = input()
#while node not in tree:
#    print('Selected node is not a part of the tree')
#    print('Please input a valid node id:')
#    node = input()

#print("\nSelected node is ({})\n".format(node))
induction('0')
pp.pprint(tree)
