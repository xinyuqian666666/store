#第一题：实现输入10个数字，并打印10个数的求和结果
# sum=0
# i=1
# while i<=10:
#     print("请输入",i,"个数字")
#     num = int(input())
#     i=i+1
#     sum=sum+num
# print(sum)
#第二题：从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# max=0
# average=0
# sum=0
# i=1
# while i<=10 :
#     print("请输入",i,"个数字")
#     num = int(input())
#     i=i+1
#     sum=sum+num
#     if max<num:
#         max=num
# average=sum/10
# print("最大值为",max)
# print(sum)
# print(average)

#第三题使用random模块，如何产生 50~150之间的数？
# import random
# shu=random.randint(50,150)
# print(shu)

#第四题：从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形
# （结果判断：等腰，等边，直角，普通，不能形成三角形。）
# a=int(input("请输入第一条边"))
# b=int(input("请输入第二条边"))
# c=int(input("请输入第三条边"))
# if a>0 or b>0 or c>0:
#     print("输入错误")
# elif a==b==c and (a+b>c or a+c>b or b+c>a) and (a-b<c or a-c<b or b-c<a):
#     print("等边三角形")
# elif (a==b or b==c or a==c) and (a+b>c or a+c>b or b+c>a) and (a-b<c or a-c<b or b-c<a):
#     print("等腰三角形")
# elif (a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a) and (a+b>c or a+c>b or b+c>a) and (a-b<c or a-c<b or b-c<a):
#     print("直角三角形")
# elif (a+b>c or a+c>b or b+c>a) and (a-b<c or a-c<b or b-c<a):
#     print("普通三角形")
# else:
#     print("不能构成三角形")

#第五题：有以下两个数，使用+，-号实现两个数的调换。
# A=56
# B=78
# 实现效果：
# A=78
# B=56

# A1=56
# print("A=",A1)
# B1=78
# print("B=",B1)
# A=A1+B1-A1
# print("A=",A)
# B=B1+A1-B1
# print("B=",B)

#第六题：实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# a=input("请输入用户名：")
# b=input("请输入密码：")
# username="root"
# password="admin"
# i=1
# while i<=3:
#     if b!=password:
#         input("请重新输入密码：")
#     i += 1

#第七题：编程实现下列图形的打印
# n=1
# m=1
# j=1
# i=1
# while i<=7:
#     while j<=7-i:
#         print(end=(" "))
#         j=j+1
#     j=1
#     while m<=i:
#         print("*",end=(" "))
#         m=m+1
#     m=1
#     print()
#     i=i+1

#第八题：使用while循环实现99乘法表的打印。
# i=1
# j=1
# while i<=9:
#     n=i*j
#     while j<=i:
#         n = i * j
#         print(j,"*",i,"=",n,end=" ")
#         j = j + 1
#     print()
#     j=1
#     i = i + 1


#第九题：编程实现99乘法表的倒叙打印
# i=9
# j=1
# while i>=0:
#     n=i*j
#     while j<=i:
#         n = i * j
#         print(j,"*",i,"=",n,end=" ")
#         j = j + 1
#     print()
#     j=1
#     i = i - 1

#第十题：一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，
# 问第几天能出来？请编程求出。
# a=20
# i=1
# baitian=3
# wanshang=2
# yitian=baitian-wanshang
# while True:
#     yitian+=1
#     if a-yitian==2:
#         print("第",yitian,"天能出来")
#         break

#第十一题：用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
# sum=0
# j=2
# i=1
# n=1
# while i<=20:
#     n=n*i
#     i = i +1
#     print(i,"的阶乘：",n)
#     sum=sum+n
# print("阶乘之和",sum)