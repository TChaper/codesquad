# U  가장 윗줄을 왼쪽으로 한 칸 밀기 RRW - RWR
# U' 가장 윗줄을 오른쪽으로 한 칸 밀기 RRW - WRR
# R  가장 오른쪽 줄을 위로 한 칸 밀기 WWB - WBW
# R' 가장 오른쪽 줄을 아래로 한 칸 밀기 WWB - BWW
# L  가장 왼쪽 줄을 아래로 한 칸 밀기 RGG - GRG (L의 경우 R과 방향이 반대임을 주의한다.)
# L' 가장 왼쪽 줄을 위로 한 칸 밀기 RGG - GGR
# B  가장 아랫줄을 오른쪽으로 한 칸 밀기 GBB - BGB (B의 경우도 U와 방향이 반대임을 주의한다.)
# B' 가장 아랫줄을 왼쪽으로 한 칸 밀기 GBB - BBG
# Q  Bye~를 출력하고 프로그램을 종료한다.
# R R W
# G C W
# G B B
def cube(array, ent):
    for i in array:
        for j in i:
            print(j, end = " ")
        print("")

def inven():
    array = [["R","R","W"],["G","C","W"],["G","B","B"]]
    cube(array, False)
    while True:
        entry = input().split()
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
                return
            cube(array,ent)
inven()