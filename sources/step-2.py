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
def cube(array):
    for i in array:
        for j in i:
            print(i, end = " ")
        print("")