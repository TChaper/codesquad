def cube(array, ent):
    if ent:
        print("{}".format(ent))
    for i in array:
        for j in i:
            print(j, end = " ")
        print("")

def inven():
    array = [["R","R","W"],["G","C","W"],["G","B","B"]]
    cube(array, False)
    while True:
        print("")
        entry = input("CUBE>" ).split()
        for ent in entry:
            if ent == "U":
                array[0][0], array[0][1], array[0][2] = array[0][1], array[0][2], array[0][0]
            elif ent == "U'":
                array[0][0], array[0][1], array[0][2] = array[0][2], array[0][0], array[0][1]
            elif ent == "R":
                array[0][2], array[1][2], array[2][2] = array[1][2], array[2][2], array[0][2]
            elif ent == "R'":
                array[0][2], array[1][2], array[2][2] = array[2][2], array[0][2], array[1][2]
            elif ent == "L":
                array[0][0], array[1][0], array[2][0] = array[2][0], array[0][0], array[1][0]
            elif ent == "L'":
                array[0][0], array[1][0], array[2][0] = array[1][0], array[2][0], array[0][0]
            elif ent == "B":
                array[2][0], array[2][1], array[2][2] = array[2][2], array[2][0], array[2][1]
            elif ent == "B'":
                array[2][0], array[2][1], array[2][2] = array[2][1], array[2][2], array[2][0]
            elif ent == "Q":
                print("Bye~")
                return
            print("")
            cube(array,ent)
inven()