obj, num, lr = input().split()
length = len(obj)
num = int(num)
if num == 0:
    print(obj)
elif num > 0:
    num = num % length
else:
    num = abs(num) % length
    if lr == "L" or lr == "l":
        lr = "R"
    elif lr == "R" or lr == "r":
        lr = "L"

if lr == "L" or lr == "l":
    result = obj[num:] + obj[:num]
elif lr == "R" or lr == "r":
    result = obj[-num:] + obj[:-num]
print(result)