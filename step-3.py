3단계: 루빅스 큐브 구현하기
참고 링크를 참고해서 루빅스 큐브를 구현한다.
큐브는 W, B, G, Y, O, R의 6가지 색깔을 가지고 있다.
입력: 각 조작법을 한 줄로 입력받는다.
출력: 큐브의 6면을 펼친 상태로 출력한다.
Q를 입력받으면 프로그램을 종료하고, 조작 받은 명령의 갯수를 출력시킨다.

def inven():
  def inven():
    array = [[['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B'],
['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R'],
['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O'],
['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'],
['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', ‘W’],
[‘G’, 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']]]
    cube(array, False)
    while True:
        entry = input("CUBE>
for i in array:
  for j in i:
    for k in j:
      print(k, end = " ")