# 1단계: 단어 밀어내기 구현하기
# 입력: 사용자로부터 단어 하나, 정수 숫자 하나( -100 <= N < 100) , L 또는 R을 입력받는다. L 또는 R은 대소문자 모두 입력 가능하다.
# 주어진 단어를 L이면 주어진 숫자 갯수만큼 왼쪽으로, R이면 오른쪽으로 밀어낸다.
# 밀려나간 단어는 반대쪽으로 채워진다
# apple 3 L 
# leapp

array = input().split()
obj = array[0]
num = int(array[1])
direction = array[2]
