


shopping_list =[["1","apple","5000"],["2","macbook","10000"],["3","bike","800"],["4","book","20"],["5","glass","80"],["6","bed","1000"]]
shopping_market=[]
salary = int(input("please input your salary:"))

while salary>0:
    print("shopping list is:")
    i=1
    for temp in shopping_list:
        print(i,temp)
        i+=1
    shopping_num = int(input("please input the things num you want to buy:"))
    shopping_things_money = int(shopping_list[shopping_num-1][2])


    if shopping_list[shopping_num-1] in shopping_market:
        press=input("you have buy it ,you can buy others,or press n to exit:")
        if press == "n":
            break
    elif shopping_things_money<=salary :
        shopping_market.append(shopping_list[shopping_num-1])
        salary=salary-shopping_things_money
        print("You have buy it,and your salary now is : %d"%salary)
        press =input("you can buy others,or press n to exit:")
        if press == "n" :
            break
    else:
        press=input("Your salary is not enough,please buy others, or press n to exit:")
        if press == "n" :
            break

i=1
for temp in shopping_market:
    print("The things you buyyed is:")
    print(i,temp)
    i+=1
    print("and your salary is %d"%salary)