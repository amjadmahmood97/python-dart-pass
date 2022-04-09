def function(number):
    my_list = []
    if (number > 0) and (number <= 10) :
        for i in range(number):
            temp = int(input())
            my_list.append(temp)

    for i in my_list:
        if i%2==0:
            print(i , "is even")
        else:
            print(i , "is odd")

n = int(input('Enter size of the list:'))
function(n)