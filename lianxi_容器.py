#有一个列表，[“北京”,”上海”,”广东”]
# 1)将中国所有省会城市添加到上述列表中

# a=["北京","上海","广东"]
# while True:
#     print("输入中国所有省会，输入”结束“，跳出：")
#     b=input()
#     a.append(b)
#     if b=="结束":
#         print()
#         break

# 2)广东成为第二大发达城市，将广东排在上海前面

# a=["北京","上海","广东"]
# b=[]
# for i in range(1,3):
#     b.append(a[1])
#     if i==1:
#         a[i] = a[i+1]
#     elif i==2:
#         a[i] = b[0]
#     else:
#         a[i]=a[i]
# print(a)

# 3)[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# 这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。
# a=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# sum=0
# for i in range(len(a)):
#     sum=sum+a[i]
# print(sum)
# print(sum/8)

#第二题：有以下一个列表，求其中是5的倍数的和
# a=[1,5,21,30,15,9,30,24]
# sum=0
# for i in range(len(a)):
#     if a[i]%5==0:
#         b=a[i]
#         sum+=b
# print(sum)

#第三题：有下列列表，请编程实现列表的数据翻转
# list1 = [1,2,3,4,5,6,7,8,9]
# list=[]
# for i in range(len(list1)):
#     if i<=8:
#         i=9-i
#         list.append(i)
# print(list1)
# print(list)

#第四题：请编程统计列表中的每个数字出现的次数
# list2= [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# for i in range(len(list2)):
#     n = 0
#     for j in range(len(list2)):
#         if list2[i]==list2[j]:
#             n+=1
#     print(list2[i],"出现次数为：",n)

# List = [1,2,3,4,5,6,7,8,9]
# print(List[-9])
# list=[]
# s=8
# for i in range(0,9):
#     list[s]=List[i]
#     list.append(list)
#     # print(List[i])
#     # print(list[s])
#     #list.append(list[s])
#     s=s-1
# print(list)

#公鸡5文钱一只，母鸡3文钱一只，小鸡3只一文钱，用100文钱买100只鸡，
# 其中公鸡、母鸡、小鸡多少只正好凑够100文钱

mydisc = {'key1':'123', 'key2':'234', 'key3':'345','key5':'123'}#字典内容
get_value = input('请输入要查值：')#输入值
if get_value in mydisc.values():#如果输入值在字典的值内容里
    for a in range(0,len(mydisc)):#从0到字典长度，一次赋值给a循环
        if list(mydisc.values())[a]==get_value:#如果字典值得列表第a个值与输入值完全相等
            print(list(mydisc.keys())[a])#输出字典中的字列表的第a个值
else:
    print('你要查询的值'+get_value+'不存在')