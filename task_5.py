def sorting(value):
    return int("".join(sorted([i for i in str(value)], reverse = True)))
def KaprekarsConstant(num):
    count = 0
    new_numb = 0
    while new_numb != 6174:
        new_numb = num - int(str(num)[::-1])
        num = sorting(new_numb)
        count+=1
        if new_numb == 0:
            return "бесконечный цикл"
    return count
user = str(sorting(input()))
if len(user) == 4 and int(user)-int(user[::-1]) !=0:
    print(KaprekarsConstant(int(user)))