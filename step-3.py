# 3단계: 루빅스 큐브 구현하기
# 참고 링크를 참고해서 루빅스 큐브를 구현한다.
# 큐브는 W, B, G, Y, O, R의 6가지 색깔을 가지고 있다.
# 입력: 각 조작법을 한 줄로 입력받는다.
# 출력: 큐브의 6면을 펼친 상태로 출력한다.
# Q를 입력받으면 프로그램을 종료하고, 조작 받은 명령의 갯수를 출력시킨다.
def cube(array, ent):
  for i in array:
    for j in i:
      for k in j:
       print(k, end = " ")
    print("")
    
def inven():
  array = {
  U : [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
  D : [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']], 
  F : [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
  B : [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],
  L : [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
  R : [[‘G’, 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]
  }
  cube(array, False)
  while True:
    entry = input("CUBE>").split()
    for ent in entry:
       if ent == "U":
                array['F'][0][0], array['R'][0][0], array['B'][0][0], array['L'][0][0] = array['L'][0][0], array['F'][0][0], array['R'][0][0], array['B'][0][0]
                array['F'][0][1], array['R'][0][1], array['B'][0][1], array['L'][0][1] = array['L'][0][1], array['F'][0][1], array['R'][0][1], array['B'][0][1]
                array['F'][0][2], array['R'][0][2], array['B'][0][2], array['L'][0][2] = array['L'][0][2], array['F'][0][2], array['R'][0][2], array['B'][0][2]
            elif ent == "U'":
                array['F'][0][0], array['L'][0][0], array['B'][0][0], array['R'][0][0] = array['R'][0][0], array['F'][0][0], array['L'][0][0], array['B'][0][0]
                array['F'][0][1], array['L'][0][1], array['B'][0][1], array['R'][0][1] = array['R'][0][1], array['F'][0][1], array['L'][0][1], array['B'][0][1]
                array['F'][0][2], array['L'][0][2], array['B'][0][2], array['R'][0][2] = array['R'][0][2], array['F'][0][2], array['L'][0][2], array['B'][0][2]     
            elif ent == "R":
                array['F'][0][2], array['U'][0][2], array['B'][0][2], array['D'][0][2] = array['D'][0][2], array['F'][0][2], array['U'][0][2], array['B'][0][2]
                array['F'][1][2], array['U'][1][2], array['B'][1][2], array['D'][0][2] = array['D'][1][2], array['F'][1][2], array['U'][1][2], array['B'][1][2]
                array['F'][2][2], array['U'][2][2], array['B'][2][2], array['D'][0][2] = array['D'][2][2], array['F'][2][2], array['U'][2][2], array['B'][2][2]
            elif ent == "R'":
                array['F'][0][2], array['U'][0][2], array['B'][0][2], array['D'][0][2] = array['U'][0][2], array['B'][0][2], array['D'][0][2], array['F'][0][2]
                array['F'][1][2], array['U'][1][2], array['B'][1][2], array['D'][0][2] = array['U'][1][2], array['B'][1][2], array['D'][1][2], array['F'][1][2]
                array['F'][2][2], array['U'][2][2], array['B'][2][2], array['D'][0][2] = array['U'][2][2], array['B'][2][2], array['D'][2][2], array['F'][2][2]
            elif ent == "L":
                array['F'][0][0], array['U'][0][0], array['B'][0][0], array['D'][0][0] = array['U'][0][0], array['B'][0][0], array['D'][0][0], array['F'][0][0]
                array['F'][1][0], array['U'][1][0], array['B'][1][0], array['D'][1][0] = array['U'][1][0], array['B'][1][0], array['D'][1][0], array['F'][1][0]
                array['F'][2][0], array['U'][2][0], array['B'][2][0], array['D'][2][0] = array['U'][2][0], array['B'][2][0], array['D'][2][0], array['F'][2][0]
            elif ent == "L'":
                array['F'][0][0], array['U'][0][0], array['B'][0][0], array['D'][0][0] = array['D'][0][0], array['F'][0][0], array['U'][0][0], array['B'][0][0]
                array['F'][1][0], array['U'][1][0], array['B'][1][0], array['D'][1][0] = array['D'][1][0], array['F'][1][0], array['U'][1][0], array['B'][1][0]
                array['F'][2][0], array['U'][2][0], array['B'][2][0], array['D'][2][0] = array['D'][2][0], array['F'][2][0], array['U'][2][0], array['B'][2][0]
            elif ent == "B":
                array['U'][0][0], array['L'][0][0], array['D'][0][0], array['R'][0][2] = array['R'][0][2], array['U'][0][0], array['L'][0][0], array['D'][0][0]
                array['U'][0][1], array['L'][1][0], array['D'][0][1], array['R'][1][2] = array['R'][1][2], array['U'][0][1], array['L'][1][0], array['D'][0][1]
                array['U'][0][2], array['L'][2][0], array['D'][0][2], array['R'][2][2] = array['R'][2][2], array['U'][0][2], array['L'][2][0], array['D'][0][2]
            elif ent == "B'":
                array['U'][0][0], array['L'][0][0], array['D'][0][0], array['R'][0][2] = array['L'][0][0], array['D'][0][0], array['R'][0][2], array['U'][0][0]
                array['U'][0][1], array['L'][1][0], array['D'][0][1], array['R'][1][2] = array['L'][1][0], array['D'][0][1], array['R'][1][2], array['U'][0][1]
                array['U'][0][2], array['L'][2][0], array['D'][0][2], array['R'][2][2] = array['L'][2][0], array['D'][0][2], array['R'][2][2], array['U'][0][2]
            elif ent == "F":
                array['U'][2][0], array['L'][0][2], array['D'][2][0], array['R'][0][0] = array['L'][0][2], array['D'][2][0], array['R'][0][0], array['U'][2][0]
                array['U'][2][1], array['L'][1][2], array['D'][2][1], array['R'][1][0] = array['L'][1][2], array['D'][2][1], array['R'][1][0], array['U'][2][1]
                array['U'][2][2], array['L'][2][2], array['D'][2][2], array['R'][2][0] = array['L'][2][2], array['D'][2][2], array['R'][2][0], array['U'][2][2]
            elif ent == "F'":
                array['U'][2][0], array['L'][0][0], array['D'][2][0], array['R'][0][2] = array['R'][0][0], array['U'][2][0], array['L'][0][2], array['D'][2][0]
                array['U'][2][1], array['L'][1][2], array['D'][2][1], array['R'][1][0] = array['R'][1][0], array['U'][2][1], array['L'][1][2], array['D'][2][1]
                array['U'][2][2], array['L'][2][2], array['D'][2][2], array['R'][2][0] = array['R'][2][0], array['U'][2][2], array['L'][2][2], array['D'][2][2]
            elif ent == "D":
                array['F'][2][0], array['R'][2][0], array['B'][2][0], array['L'][2][0] = array['L'][2][0], array['F'][2][0], array['R'][2][0], array['B'][2][0]
                array['F'][2][1], array['R'][2][1], array['B'][2][1], array['L'][2][1] = array['L'][2][1], array['F'][2][1], array['R'][2][1], array['B'][2][1]
                array['F'][2][2], array['R'][2][2], array['B'][2][2], array['L'][2][2] = array['L'][2][2], array['F'][2][2], array['R'][2][2], array['B'][2][2]
            elif ent == "D'":
                array['F'][2][0], array['L'][2][0], array['B'][2][0], array['R'][2][0] = array['R'][2][0], array['F'][2][0], array['L'][2][0], array['B'][2][0]
                array['F'][2][1], array['L'][2][1], array['B'][2][1], array['R'][2][1] = array['R'][2][1], array['F'][2][1], array['L'][2][1], array['B'][2][1]
                array['F'][2][2], array['L'][2][2], array['B'][2][2], array['R'][2][2] = array['R'][2][2], array['F'][2][2], array['L'][2][2], array['B'][2][2]
            elif ent == "Q":
                print("BYE~")
                return
            cube(array,ent)
inven()
