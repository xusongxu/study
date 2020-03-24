import time
print("https://www.cnblogs.com/Mr-choa/")
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("业精于勤而荒于嬉，勤劳一日，可得一日安眠；勤劳一生，可得幸福一生。因为，我们努力了；因为，天道酬勤。")


# def fib(n: int):
#     if n == 1 or n == 2:
#         return 1
#     if n > 2:
#         return fib(n - 1) + fib(n - 2)
#
#
# for i01 in range(1, 11):
#     print(fib(i01))
#
# for i02 in range(1,10):
#     for j02 in range(1,i02+1):
#         print(str(i02)+'*'+str(j02)+'='+str(i02*j02),end='\t')
#     print()
# for i03 in range(9,0,-1):
#     for j03 in range(1,i03+1):
#         print(str(i03)+'*'+str(j03)+'='+str(i03*j03),end='\t')
#     print()
#


#
#
# def fib01(n:int):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fib01(n-1)+fib01(n-2)
# print(fib01(7))

# print("hello world")
#
# a = [1, 'a']
# a[0] = 2
# print(a)

# age01 = int(input("输入年龄："))
# if age01 <= 10:
#     print("儿童")
# elif 10 < age01 <= 20:
#     print("青年")
# else:
#     print("小伙子")

# a01 = [1, 2, 3]
# b01 = a01[:]
# print(b01)
#
# a02 = 0
# while a02 < 2:
#     print("hello")
#     a02 += 1
#
# a03 = ["aa", "bb", "cc", "dd"]
# # for i in a03:
# #     print(i)
# # for i in range(1, 4):
# #     print(a03[i])
# for i in a03:
#     if i == "cc":
#         break
#     print(i)
# for i in a03:
#     if i == "cc":
#         continue
#     print(i)
#
# for i in range(1, 10):
#     print('')
#     for j in range(1, i + 1):
#         print("%d*%d=%d" % (i, j, i * j), end=' ')
# for i in range(9, 0, -1):
#     print('')
#     for j in range(1, i + 1):
#         print("%d*%d=%d" % (i, j, i * j), end=' ')
#
# print('')
#
#
# def abc() -> object:
#     print("abed")
#
#
# abc()
#
#
# def fun01(a04: object, b04: object) -> object:
#     if a04 < b04:
#         print("a<b")
#     else:
#         print("a>=b")
# fun01(3, 7)
# fun01(5, 4)
#
# import cgi
# cgi.closelog()
#
# file01 = open("D:/360Downloads/1.txt", 'r')
# data = file01.read()
# print(data)
# # print(file01.name)
# # file02 = open("D:/360Downloads/1.txt",'w')
# # file02.write(我们一起学Java)
# # print(data)
# file03 = open("D:/360Downloads/1.txt",'a+')
# file03.write("python")
# file03.seek(0)
# print(file03.read())

# try:
#     a = 0 / 0
# except Exception as ex:
#     print(ex)
#
# try:
#     file01 = open("D:/360Downloads/1.txt", 'w')
#     file01.write("此文件用于异常处理")
# except Exception as ex:
#     print(ex)
#     print("文件写入失败")
# else:
#     print("文件写入成功")
#     file01.close()
#
#
# class Person:
#     def __init__(self, name, age):
#         print("带参数的构造函数，name=" + name + ",age=" + age)
# c1 = Person("Tanglei", str(20))
# c2 = Person("Lisa", str(22))
#
#
# class User:
#     def __init__(self):
#         print("无构造函数")
# c3 = User()


# def func01():
#     print("aaa")
#
#
# class Rabbit:
#     def __init__(self, name: object, color: object) -> object:
#         self.name = name
#         self.color = color
#         print("带参数的构造函数，name=" + self.name + ",color=" + self.color)
#     def func01(self,weight):
#         print("这个兔子已经"+str(weight)+"千克了")
#
#     def func02(self,age):
#         print("这个兔子已经" + str(age) + "岁了")
#
#     def toString(self):
#         print("Rabbit [name=" + self.name + ", color=" + self.color + "]")
#
#
# r1 = Rabbit("流浪兔", "白色")
# r1.func01(4)
# r1.func02(3)
# r1.toString()

# class Father:
#     @staticmethod
#     def write():
#         print("写作")
# class Son(Father):
#     pass
# class Mother:
#     @staticmethod
#     def draw():
#         print("画画")
#     @staticmethod
#     def makeDinner():
#         print("做饭")
# class Daughter(Father,Mother):
#     def draw(self):
#         print("素描")
# son=Son()
# son.write()
#
# daughter=Daughter()
# daughter.write()
# daughter.draw()
# daughter.makeDinner()
#
#
# print("python\n" * 3)
# print("bbb")
# tmp01=input("请输入一个数字：")
# print(tmp01)
# print('')

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# number01=int(input("请输入一个整数："))
# result01=factorial(number01)
# print("%d的阶乘是%d" %(number01,result01))
#
# def fab(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
# number02=int(input("请输入正整数："))
# result02=fab(number02)
# print(result02)
# print("总共有"+str(result02)+"兔子")

# number03=3
# number04=5/3
# print(type(number03))
# print(number04)
# print(type(number04))
# str01='hello'
# str02="hello"
# print(type(str01))
# print(str02)
# str03="hello \"world\""
# print(str03)
# str04="hello 'world'"
# print(str04)
# str05="Jack:\nI Love You"
# print(str05)
# str06="""Lose:
# I Love You too"""
# print(str06)
# str07="abcdefg"
# print(str07[2])
# print(str07[0]+str07[1])
# print(str07[1:4])
# print(str07[4:])
# print(str07[:4])
# print(str07[::4])
# print(str07[::2])
# print(str07[::3])
# print(str07[-1])
# print(str06[-4:-1])
# str08="1234"
# print(id(str08))
# str09="1234"
# print(id(str09))
# t01=("Jack","19","male")
# help(t01)
# help(len(t01))
# print(t01)
# print(t01[1])
# print(t01[2])
# print(type(t01))
# print(len(t01))
# t02=(3,)
# print(t02)
# print(type(t02))
# print(len(t02))
# print(t02[0])
# print(len(str09))
# a, b, c = (1, 2, 3)

# print(a)
# print(b)
# print(c)
# list01= [12, 21, True, [1, 2, 3]]
# print(list01)
# print(list01[0])
# print(list01[1])
# print(list01[2])
# print(list01[3])
# print(type(list01))
# print(len(list01))
# list01[0]="lose"
# list01[1]=23
# print(list01)
# print(type(list01))
# list01.append(34)
# list01.append("abc")
# print(list01)
# list01.remove("abc")
# print(list01)
# list01.remove("lose")
# print(list01)
# print('')
# print("")
# print(list01)
# list02= [1, 2, 3, 4, 8]
# print(list02)
# help(list02)
# help(list02.append(7))
# print(list02)
# dict01 = {"name": "Jack", "age": "24", "gender": "male"}
# print(dict01)
# print(dict01["name"])
# print(dict01["age"])
# print(dict01["gender"])
# print(len(dict01))
# print(type(dict01))
# print(dict01.keys())
# print(dict01.values())
# print(dict01)
# dict01["phone"] = "15979052245"
# print(dict01)
# del dict01["name"]
# print(dict01)
# print(dict01.pop("age"))
# print(dict01)
# dict01["name"] = "Jack"
# print(dict01)
# dict01["age"] = "25"
# print(dict01)
#
# if 1 < 2:
#     print("1")
# if 2 > 1:
#     print("2")
# if True:
#     print("3")
# if 1+1:
#     print("4")
#
# print(range(1,10))
# print(range(1,10,2))
# print(range(5))
# arr01=['a','b','c','d']
# print(arr01)
# for i in arr01:
#     print(i)
# for i in range(len(arr01)):
#     print(arr01[i])
# num03=0
# for i in range(0,101):
#     num03+=1
# print(num03)
# for i in range(0,3):
#     print(i)
# else:
#     print("finish")
# dict02={"name":"Jack","age":"25"}
# for i in range(len(dict02)):
#     print(dict02)
# for k,v in dict02.items():
#     print(k,': '+v)
# dict03={1:111,2:222,3:333}
# print(dict03)
# for value in dict03:
#     print(dict03[value])
# for k,v in dict03.items():
#     print(k,v)
# def func01():
#     print("abc")
# func01()
#
#
# def func02(x, y):
#     print(x)
#     print(y)
# func02('a', 'b')
#
#
# def func03(x=5, y=6):
#     print("x=" + str(x) + ",y=" + str(y))
# func03(1, 3)
# func03()
#
#
# def func04(x, y=5):
#     print("x=" + str(x) + ",y=" + str(y))
# func04(3, 7)
# func04(4, 9)


# def func05():
#     x=input("请输入一个数字：")
#     print(x)
# func05()
# def func06():
#     global a
#     a = "good"
#     print(a)
# func06()
#
#
# def func07(x, y):
#     print("x=%s,y=%s" % (x, y))
# func07(1,2)
# func07(*(3,4))
# arr02=("Jack","25")
# arr03=(23,"hello")
# print(*arr02)
# func07(*arr02)
# func07(*arr03)
#
# dict03 = {"name": "Jack", "age": "25"}
#
#
# def func08(name, age):
#     print("name=%s,age=%s" % (name, age))
#
#
# def func09(name, age, gender):
#     print("name=%s,age=%s,gender=%s" % (name, age, gender))
#
#
# func08(**dict03)
# func08(dict03["name"], dict03["age"])
# dict03["name"] = "tangchao"
# print(dict03)
# func09(**dict03)


# dict03["name"]="Bob"
# func08(**dict03)
# del dict03["name"]
# print(dict03)
# dict03["name"]="Bob"
# print(dict03)
# print(dict03.keys())
# print(dict03.values())
#
# def func10(x,*args):
#     print(x)
#     print(args)
# func10(2)
# func10(3,4,5,7,9,12)
# def func11(x, *args, **kwargs):
#     print(x)
#     print(args)
#     print(kwargs)
#
#
# func11(2, 3, 4, 5, 6, 7, y=3, z=4)
# func11(4, y=5)
#
# f6 = lambda x,y:x*y
# print(f6(3, 4))
#
# print(abs(-2))
# r01=range(12)
# print(max(r01))
# print(min(r01))
# print(r01)
# print(len(r01))
# print(len(divmod(5,4)))
# print(pow(2,10))
# print(type(r01))
# print(round(2.987654321,2))
# print(round(4,1))
# a01="1234"
# print(type(a01))
# print(a01)
# a01=int(a01)
# print(a01)
# print(type(a01))
# b01=99
# print(b01)
# print(str(b01))
# b01=str(b01)
# print(type(b01))
# b02=89
# print(hex(b02))
# list02=[1,2,3,4]
# print(list02)
# b03="abcaaaaaa"
# print(b03.capitalize())
# print(b03)
# print(b03.replace('a','F',5))
# b04="192.168.12.93"
# print(b04)
# b05=b04.split(".")
# b06=b04.split(".",-1)
# print(b05)
# print(b06)
# help(filter)

#
#
# def func12(x):
#     if x > 0:
#         return True
#     else:
#         return False
#
#
# r01 = [1, 2, -1]
# r02 = list(filter(func12, r01))
# print(r02)
#
# foo = [2, 3, 4, 5, 6, 7, 8]
# print(list(filter(lambda x: x % 2 == 0, range(8))))
# print(list(map(lambda x: x * 2, foo)))
# def square(x):
#     return pow(x,2)
# print(list(map(square,[1,2,3,4])))
#
# print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))
# result01 = map(lambda x: x * 2, [1, 2, 3, 4, 5])
# print(result01)
# print(list(result01))
# result02 = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# print(result02)
# r03 = [1, 4, 7, 9, 12]
# result03=filter(lambda x: x % 3==0, r03)
# result04=map(lambda x :x*3,r03)
# print(list(result03))
# print(result04)
# print(list(result04))
# def add(x,y):
#     return x+y
# result05=functools.reduce(add,[1,2,3])
# result06=functools.reduce(lambda x,y:x*y,[1,2,3,4])
# print(result05)
# print(result06)
#
# r04 = ["zhangsan", "lisi","wangwu"]
# r05 = ["北京", "上海", "广州"]
# r06 = [22, 23, 24]
# # zip将对象中的对应的元素打包成一个个元组，返回这些元组组成的列表
# ss01 = zip(r04, r05, r06)
# print(list(ss01))
# list02=list(ss01)
# print(len(list02))
# print(type(list02))
# print(list02)
# print(list02[2])
# list02.append(("zhaoliu","深圳","25"))
# print(list02)
# print(len(list02))
# print(list02[3])

# import re

#
# print(re.match('www', 'www.baidu.com'))
# print(re.match('www', 'www.biadu.com').span())
# print(re.match('www', 'www.baidu.com').group())
# print(re.match('w', 'www.biadu.com'))
#
# list03: str = "Cats are smarter than dogs"
# matchObj = re.match(r"(.*) are (.*?).*", list03, re.M | re.I)
# if matchObj:
#     print(matchObj)
#     print(matchObj.span())
#     print(matchObj.group(0))
#     print(matchObj.group(1))
#     print(matchObj.group(2))
# else:
#     print("matching failed")
# serchObj01 = re.search(r"are", list03, re.M | re.I)
# if serchObj01:
#     print(serchObj01.span())
#     print(serchObj01.group())
# else:
#     print("No match")
# print(re.search('www', 'www.baidu.com').span())
# print(re.search('b', 'www.baibu.com').group())
# serchObj02 = re.search(r'dogs', list03, re.M | re.I)
# print(serchObj02)
#
# phone = "2004-959-559 # 这是一个电话号码"
# num01 = re.sub("#.*$", '', phone)
# print(num01)
# num02 = re.sub("\D", "", phone)
# print(num02)
#
# help(re.compile)
# num03=re.compile(r'\d')
# print(num03.match("one1two2three3four4",3,10))
#
# def double(x):
#     value = int(x.group('value'))
#     return str(value * 2)
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))
#
# s01="12abcd3"
# s02="12abcd3"
# s03="12abcd@"
# result01=re.search('\D+',s01)
# result02=re.search('\d+',s02)
# print(result01)
# print(result02)
#
# c01=re.compile('\d+')
# print(c01.findall(s01))
# c02=c01.split(s01)
# c03=c01.findall('one1two2')
# c04=c01.match('one1two2')
# c05=c01.match('one1two2',3,10)
# print(c04)
# print(c02)
# print(type(c02))
# print(c03)
# print(c05)
#
# ss01=re.compile("hello")
# match01=ss01.match("hello world!")
# print(match01)
#
# p = re.compile('(\w+) (\w+)')
# s = 'i say , hello world!'
# print(p.sub(r'\2\1 ', s))
#
# ss02=re.compile("a\.b")
# match02=ss02.match("a.b")
# print(match02)
#
# ss02=re.compile("a")
# match02=ss02.match("abcd")
# print(match02)


# ss02=re.compile("\d+")
# match02=ss02.match("one1two2three3four4")
# print(match02)
# match02=ss02.match("one1two2three3four4",3,5)
# print(match02)
# print(match02.group())
# print(match02.start())
# print(match02.end())
# print(match02.span())
#
# ss03=re.compile('\d+')
# match03=ss03.findall('12abcd3')
# match04=ss03.findall("runoob 123 google 456")
# match05=ss03.findall("run88oob123google456",0,10)
# print(match03)
# print(match04)
# print(match05)
# import re
# mathch06=re.finditer('\d+',"12abcd3")
# print(list(mathch06)[1])
#
# print(re.split('\W+', 'abc,, runoob, wahaha, 1342'))       #split是相反的
# print(re.split('(\W+)', 'abc, runoob, wahaha, 1342'))
# print(re.split('\W+', 'abc, runoob, wahaha, 1342', 1))
# print(re.split('\d', 'hello world'))

# file02=open("D:/360Downloads/1.txt","r")
# print(file02.read())
# file01=open("D:/360Downloads/1.txt",'w+')
# file01.write("此文件用于测试12")
# file01.flush()
# file01.seek(0)
# print(file01.read())
# file03=open("D:/360Downloads/1.txt","a+")
# file03.write("haha")
# print(file03.read())
# file03.seek(0)
# print(file03.read())
#
# try:
#     file01 = open("D:/360Downloads/1.txt", 'w+')
#     file01.write("demo01")
#     file01.write("你好")
#     file01=open("D:/360Downloads/1.txt","r+")
#     print(file01.read())
# except Exception as ex:
#     print(ex)
#     print("文件写入失败")
# else:
#     print("文件写入成功")

# f = open("D:/360Downloads/1.txt","r")
# for line in f:
#     print(line)
# f.close()
#
# try:
#     file04=open("D:/360Downloads/1.txt","a+")
#     print(file04.read())
#     file04.seek(0)
#     print(file04.read())
# except Exception as ex:
#     print(ex)
# else:
#     print("文件写入成功")
#
# try:
#     f = open("D:/360Downloads/1.txt")
#     f.close()
# except OSError as err:
#     print("OSError")
# except RuntimeError:
#     print("RuntimeError")
# except NameError:
#     print("NameError")
# except:
#     print("Unexpected Error")
# else:
#     print("文件修改成功")
#
# try:
#     x = int(input("Please enter a number: "))
#     if x == 123:
#         raise NameError("You are kidding!")
# except NameError:
#     print("name error")
# except ValueError:
#     print("value error")
# except TypeError:
#     print("type error")
# finally:
#     print("Goodbye")
#
# class my01:
#     def __init__(self, name, age):
#         print("name=" + name + ",age=" + age)
#     def m1(self):
#         print("hello")
# c1 = my01("tang", "24")
# c1.m1()
#
# class My02:
#     def __init__(self):
#         print("初始化")
#     i=123
#     @staticmethod
#     def m2():
#         return "hello"
# x1=My02()
# x1.m2()
# print(x1.i)
# print(x1.m2())
#
# class Person01:
#     # def __init__(self):
#     #     print("无构造参数被调用")
#     def __init__(self,name,age):
#         print("带构造参数被调用")
#         self.name=name
#         self.age=age
#         print("name="+self.name+",age="+self.age)
#     def tostring(self):
#         print("person [name={0},age={1}]".format(self.name,self.age))
# p02=Person01("tang","24")
# p02.tostring()
# print(id(p02))
# print(p02.name)
# print(p02.age)
#
# class Employee:
#     employee=0
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         Employee.employee+=1
#     def Count(self):
#         print("Total count=%d" % Employee.employee)
#     def tostring(self):
#         print("employee[name={0},age={1},salary={2}]".format(self.name,self.age,self.salary))
# ee01=Employee("zhangsan","23","3000")
# ee02=Employee("lisi","24","4000")
# ee03=Employee("wangwu","25","5000")
# print("总共有%d人工作"%Employee.employee)
# print(ee01.name)
# print(ee01.Count())
# print(ee02.age)
# print(ee03.salary)
# print(Employee.__name__)
# print(Employee.__module__)
# ee01.tostring()
#
# s01=(ee01.name,ee01.age,ee01.salary)
# s02=(ee02.name,ee02.age,ee02.salary)
# s03=(ee03.name,ee03.age,ee03.salary)
# s04=zip(s01,s02,s03)
# print(s01)
# print(s02)
# print(s03)
# print(list(s04))
#
# class Leader(Employee):
#     def __init__(self):
#         print("继承")
# leader=Leader()
#
# class Father:
#     def sing(self):
#         print("我会唱歌")
#     def write(self):
#         print("我擅长粉笔字")
# class Mother:
#     def dance(self):
#         print("我会广场舞")
# class Son(Mother,Father):
#     def write(self):
#         print("我会毛笔字")
#     def dance(self):
#         print("我会街舞")
# son=Son()
# son.write()
# son.dance()
# son.sing()
#
# class Daughter:
#     name=""
#     _hight=0
#     __age=0
#     def __init__(self,name,hight,age):
#         self.name=name
#         self._hight=hight
#         self.__age=age
#     def Getname(self):
#         return self.name
#     def __Getage(self):
#         return self.__age
#     def Getage(self):
#         return self.__age
# daughter=Daughter("Lisa","165","25")
# print(daughter.name)
# print(daughter.Getname())
# print(daughter.Getage())
#



# def is_palindrome(n):
#
#     N = str(n)
#
#     flag = True
#
#     if len(N) == 1:
#
#         return True
#
#     else:
#
#         for i in range(int(len(N)/2)):
#
#             if int(N[i]) != int(N[-i-1]):
#                 flag = False
#     return flag
#
# import pymysql
# import mysql.connector
# conn = mysql.connector.connect(user='root', password='123456', database='test')
# cursor = conn.cursor()
# sql = "insert into user_info(name, family, sword) values('%s', '%s', '%s')" % ('魏无羡', '云梦江氏', '随便')
# try:
#     # 执行SQL
#     cursor.execute(sql)
#     # 提交
#     conn.commit()
# except:
#     # 回滚
#     conn.rollback()
#     print("执行失败")
# finally:
#     # 关闭连接
#     conn.close()
# cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])

# import mysql.connector
# conn01=mysql.connector.connect(user='root',password='123456',database='test')
# cursor =conn01.cursor()
# cursor.execute('create table user_info (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user_info (id, name) values (%s, %s)',['1', 'Michael'])
# cursor.rowcount()
#
# import MySQLdb
# # 打开数据库连接
# db = MySQLdb.connect("localhost", "root", "123456", "TESTDB", charset='utf8' )
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
#
# print ("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()
#
# # 导入pymysql模块
# import pymysql
# name=input("请输入名字：")
# pwd=input("请输入密码：")
# # 连接database
# conn = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="123456",
#     database="day59",
#     charset="utf8")
# # 得到一个可以执行SQL语句的光标对象
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# #定义sql语句
# sql='select *from userinfo where name=%s and pwd=%s;'
# # 执行SQL语句
# result01=cursor.execute(sql,[name,pwd])
# if result01:
#     print("登入成功！")
#     add_name = input("请添加名字：")
#     add_pwd = input("请添加密码：")
#     # 添加操作
#     sql01 = 'insert into userinfo (name, pwd) values (%s, %s);'
#     # 执行sql语句
#     result02 = cursor.execute(sql01, [add_name, add_pwd])
#     #提交事务
#     if result02:
#         print("添加成功！")
#     conn.commit()
#     #关闭光标对象
#     cursor.close()
#     #关闭数据库连接
#     conn.close()
# else:
#     print("登入失败！")
#
# # 导入pymysql模块
# import pymysql
# name=input("请输入名字：")
# pwd=input("请输入密码：")
# # 连接database
# conn = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="123456",
#     database="day59",
#     charset="utf8")
# # 得到一个可以执行SQL语句的光标对象
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# # 定义要执行的SQL语句
# # sql = """
# # CREATE TABLE USER1 (
# # id INT auto_increment PRIMARY KEY ,
# # name CHAR(10) NOT NULL UNIQUE,
# # age TINYINT NOT NULL
# # )ENGINE=innodb DEFAULT CHARSET=utf8;
# # """
# #数据库登入
# sql='select *from userinfo where name=%s and pwd=%s;'
# # 执行SQL语句
# result01=cursor.execute(sql,[name,pwd])
# if result01:
#     print("登入成功！")
#     add_name = input("请添加名字：")
#     add_pwd = input("请添加密码：")
#     # add_bookname=input("请添加书名:")
#     # 添加表格操作
#     sql01 = 'insert into userinfo (name, pwd) values (%s, %s);'
#     sql02='insert into book (name) values (%s);'
#     #异常处理
#     try:
#         #执行SQL语句
#         cursor.execute(sql01, [add_name, add_pwd])
#         # cursor.execute(sql02,add_bookname)
#         #执行事务，提交
#         conn.commit()
#         #获取插入数据的id并打印
#         last_id=cursor.lastrowid
#         print("添加成功，没有异常！")
#         print("最后一条数据的id是：",last_id)
#     except Exception as ex:
#         print(ex)
#         print("添加失败！")
#         #插入数据失败回滚
#         conn.rollback()
#     #关闭光标对象
#     cursor.close()
#     #关闭数据库连接
#     conn.close()
# else:
#     print("登入失败！")
#
# # 导入pymysql模块
# import pymysql
# # 连接database
# conn = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="123456",
#     database="day59",
#     charset="utf8")
# # 得到一个可以执行SQL语句的光标对象
# cursor = conn.cursor()
# # 定义要执行的SQL语句
# # 批量添加表格操作
# sql01 = 'insert into demo01 (name, pwd) values (%s, %s);'
# data01 = {("tang03", "3"), ("tang02", "2"), ("tang01", "1")}
# # 异常处理
# try:
#     # 执行SQL语句
#     cursor.executemany(sql01, data01)
#     # 执行事务，提交
#     conn.commit()
#     # 获取插入数据的id并打印
#     last_id = cursor.lastrowid
#     print("添加成功，没有异常！")
#     print("最后一条数据的id是：", last_id)
# except Exception as ex:
#     print(ex)
#     # 插入数据失败回滚
#     conn.rollback()
# # 关闭光标对象
# cursor.close()
# # 关闭数据库连接
# conn.close()
#
# # 导入pymysql模块
# import pymysql
# # 连接database数据库
# conn=pymysql.connect(
#     host="127.0.0.1",
#     port=3306,
#     user="root",
#     password="123456",
#     database="day59",
#     charset="utf8"
# )
# # 获取一个光标
# cursor=conn.cursor()
# # 定义一个sql语句
# sql="select *from userinfo where id=4;"
# # 执行sql语句
# cursor.execute(sql)
# # 提取查询的结果
# result=cursor.fetchall()
# # 打印查询的结果
# print(result)
# # 关闭光标
# cursor.close()
# # 关闭连接
# conn.close()
#
# # 导入pymysql模块
# import pymysql
# # 连接database数据库
# conn=pymysql.connect(
#     host="127.0.0.1",
#     port=3306,
#     user="root",
#     password="123456",
#     database="day59",
#     charset="utf8"
# )
# # 获取一个光标
# cursor=conn.cursor()
# # 定义一个sql语句
# sql="select name,pwd,id from userinfo where id between 5 and 10;"
# # 执行sql语句
# cursor.execute(sql)
# # 提取查询的结果,取一条结果
# result01=cursor.fetchone()
# # 取3条结果
# result02=cursor.fetchmany(3)
# # 取全部的结果
# result=cursor.fetchall()
# # 相对移动，相对它当前的位置
# cursor.scroll(-1,mode="relative")
# # 取一条结果
# result03=cursor.fetchone()
# # 打印提取的结果
# # print(result)
# print(result01)
# print(result02)
# print(result03)
# # 关闭光标
# cursor.close()
# # 关闭连接
# conn.close()
#
# # 导入pymysql模块
# import pymysql
# # 连接database数据库
# coon=pymysql.connect(
#     host="127.0.0.1",
#     port=3306,
#     user="root",
#     password="123456",
#     database="day59",
#     charset="utf8"
# )
# # 获取一个光标
# cursor=coon.cursor()
# # 定义一个sql语句
# sql="select *from userinfo;"
# # 异常处理
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提取查询的结果
#     results=cursor.fetchall()
#     print("id","name","password")
#     # 对查询结果遍历
#     for row in results:
#         id=row[0]
#         name=row[1]
#         password=row[2]
#         print(id,name,password)
# except Exception as ex:
#     print(ex)
# finally:
#     # 关闭光标
#     cursor.close()
#     # 关闭连接
#     coon.close()
#
# # 导入pymysql模块
# import pymysql
# # 连接database数据库
# coon=pymysql.connect(
#     host="127.0.0.1",
#     port=3306,
#     user="root",
#     password="123456",
#     database="day59",
#     charset="utf8"
# )
# # 获得一个光标
# cursor=coon.cursor()
# # 定义一个sql语句，用于修改数据库
# sql="update userinfo set pwd=%s where name=%s;"
# name=input("请输入名字:")
# pwd=input("请输入修改密码:")
# # 异常处理
# try:
#     cursor.execute(sql,[pwd,name])
#     coon.commit()
# except Exception as ex:
#     print(ex)
#     print("提交失败！")
#     coon.rollback()
# else:
#     print("提交成功！")
# #光标关闭
# cursor.close()
# # 关闭连接
# coon.close()
#
# # 导入pymysql模块
# import  pymysql
# # 连接database数据库
# coon=pymysql.connect(
#         host="127.0.0.1",
#         port=3306,
#         user="root",
#         password="123456",
#         database="day59",
#         charset="utf8"
# )
# # 获取一个光标
# cursor=coon.cursor()
# # 定义一个sql语句
# sql="insert into user_info (name,family,swd) values (%s,%s,%s) ;"
# data=("tangchao","yuanjia","123456")
# try:
#     # 执行sql语句
#     cursor.execute(sql, data)
#     # 执行事务
#     coon.commit()
# except Exception as ex:
#     print("处理异常！")
#     print(ex)
# else:
#     print("添加成功！")
# finally:
#     # 关闭光标
#     cursor.close()
#     # 关闭连接
#     coon.close()
#
# # 导入pymysql模块
# import pymysql
# # 连接database数据库
# coon=pymysql.connect(
#     host="127.0.0.1",
#     port=3306,
#     user="root",
#     database="day59",
#     password="123456",
#     charset="utf8"
# )
# # 获取一个光标
# cursor=coon.cursor()
# # 定义一个sql语句
# sql="insert into user_info (name,family,swd) values ('%s','%s','%s');"
# data_list=[("tanglei","yuanjia","1"),("tangchao","yuanjia","2"),("shaozhong","yuanjia","3")]
# # 异常处理
# try:
#     # 遍历data_list
#     for data in data_list:
#         sql_data=sql % data
#         # 执行sql语句
#         cursor.execute(sql_data)
#         # 执行事务
#         coon.commit()
# except Exception as ex:
#     print("批量添加失败！")
#     print(ex)
#     # 回滚
#     coon.rollback()
# else:
#     print("批量添加成功！")
# finally:
#     # 关闭光标
#     cursor.close()
#     # 关闭连接
#     coon.close()
#
# # 导入pymysql模块
# import pymysql
# # 连接database数据库
# coon=pymysql.connect(
#     host="127.0.0.1",
#     port=3306,
#     user="root",
#     password="123456",
#     database="day59",
#     charset="utf8"
# )
# # 获取一个光标
# cursor=coon.cursor()
# # 定义一个sql语句
# sql="select *from user_info; "
# # 异常处理
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提取查询的所有结果
#     data=cursor.fetchall()
#     # print("id","name","family","swd")
#     # 方法一遍历查询的结果
#     for row in data:
#         id=row[0]
#         name=row[1]
#         family=row[2]
#         swd=row[3]
#         print(id,name,family,swd)
#     ##方法二遍历
#     # for row in data:
#     #     print("id=%s,name=%s,family=%s,swd=%s" % (row[0],row[1],row[2],row[3]))
# except Exception as ex:
#     print(ex)
#     print("查询失败！")
# finally:
#     # 关闭光标
#     cursor.close()
#     # 关闭连接
#     coon.close()
#
# # 导入socket模块
# import socket
# import sys
# # 创建socket对象
# server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host=socket.gethostname()
# port=9999
# # socket对象绑定地址和端口
# print(host)
# server_socket.bind((host,port))
# # 最大连接数2
# server_socket.listen(2)
# # 监听客户端连接
# while True:
#     print(1234)
#     # socket对象阻塞等待接受链接
#     clientsocket,addr = server_socket.accept()
#     print("客户端连接: %s" % str(addr))
#     msg = "Hello World"
#     # 发送信息给客户端或服务器
#     clientsocket.send(msg.encode("utf-8"))
#     # 关闭链接
#     clientsocket.close()
#
# # 导入socket模块
# import socket
# # 创建一个socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 与新浪网建立连接
# s.connect(("www.baidu.com.cn",80))
# #客户端发送请求
# s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com.cn\r\nConnection: close\r\n\r\n')
# # 接受数据
# buffer=[]
# while True:
#     # 一次最多接受1k字节
#     d=s.recv(1024)
#     if d:
#         buffer.append(d)
#         print(buffer)
#     else:
#         break
# #使用空字节连接，成为新的字节串
# data = b''.join(buffer)
# print(data)
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件:
# with open('baidu.html', 'wb') as f:
#     f.write(html)
#
#
# # from attr import attrs, attrib
# # from cattr import structure, unstructure
# import attr
# import cattr
#
# @attr.attrs
# class User(object):
#     name = attr.attrib()
#     age = attr.attrib()
# data = {
#     'name': 'Germey',
#     'age': 23
# }
# user = cattr.structure(data, User)
# print('user', user)
# json = cattr.unstructure(user)
# print('json', json)
#
# # 导入time模块
# import time
# # 定义f函数
# def f():
#     # 开始时间
#     start_time=time.time()
#     print("hello")
#     # 延时一秒
#     time.sleep(1)
#     print("world")
#     # 结束时间
#     end_time=time.time()
#     execution_time=(end_time-start_time)*1000
#     # 打印时间差
#     print("execution_time=%dms" % execution_time)
# f()
#
# # 导入time模块
# import time
# # 定义deco函数，参数是一个函数，返回值也是一个函数
# def deco(f):
#     # 定义wrapper函数
#     def wrapper():
#         # 开始时间
#         start_time = time.time()
#         # 调用f()函数
#         f()
#         # 结束时间
#         end_time = time.time()
#         execution_time = (end_time - start_time) * 1000
#         # 打印时间差
#         print("execution_time=%dms" % execution_time)
#     return wrapper
# # 类装饰器
# @deco
# def f():
#     print("hello")
#     # 延时1秒
#     time.sleep(1)
#     print("world")
# f()
#
# # 带固定参数的装饰器
# # 导入time模块
# import time
# #定义deco函数，参数是一个函数，返回值是一个函数
# def deco(f):
#     # 定义wrapper函数
#     def wrapper(a,b):
#         # 开始时间
#         start_time=time.time()
#         # 调用f函数
#         f(a,b)
#         # 结束时间
#         end_time=time.time()
#         execution_time=(end_time-start_time)*1000
#         # 打印程序执行时间
#         print("execution_time=%d" % execution_time)
#     # 返回值是一个函数
#     return wrapper
#
# # 类装饰器deco
# @deco
# # 定义f函数，参数是a，b
# def f(a,b):
#     print("hello")
#     # 延时1秒
#     time.sleep(1)
#     print("world")
#     # 打印结果
#     print("result=%d" % (a+b))
# # 执行f函数
# f(4,5)
#
# # 无固定参数的装饰器
# # 导入time模块
# import time
# # 定义deco函数，参数是一个函数，返回值是一个函数
# def deco(f):
#     # 定义wrapper函数，无固定参数
#     def wrapper(*args,**kwargs):
#         # 开始时间
#         start_time=time.time()
#         # 调用f函数
#         f(*args,**kwargs)
#         # 结束时间
#         end_time=time.time()
#         # 程序执行时间
#         execution_time=(end_time-start_time)*1000
#         # 打印程序执行时间
#         print("execution_time=%dms" % execution_time)
#     #返回值是wrapper函数
#     return wrapper
# # 类装饰器deco
# @deco
# # 定义f函数，两个参数a，b
# def f(a,b):
#     print("hello!")
#     # 延时1秒
#     time.sleep(1)
#     print("world!")
#     # 打印a+b的结果
#     print("result=%d" % (a+b))
# # 类装饰器deco
# @deco
# # 定义f2函数，三个参数a，b，c
# def f2(a,b,c):
#     print("haha!")
#     # 延时1秒
#     time.sleep(1)
#     print("nihao!")
#     # 打印a+b+c的结果
#     print("result=%d" % (a+b+c))
# # 执行f函数
# f(3,4)
# # 执行f2函数
# f2(3,4,5)
#
# # 用多个装饰器修饰一个函数
# # 导入time模块
# import time
# # 定义deco01函数，参数是一个函数，返回是一个函数
# def deco01(f):
#     # 定义wrapper函数
#     def wrapper(*args,**kwargs):
#         print("this is deco01")
#         # 开始时间
#         start_time=time.time()
#         # 调用f函数
#         f(*args,**kwargs)
#         # 结束时间
#         end_time=time.time()
#         # 执行时间
#         execution_time=(end_time-start_time)*1000
#         print("execution_time=%dms" % execution_time)
#         print("deco01 is end")
#     # 返回wrapper函数
#     return wrapper
#
# def deco02(f):
#     def wrapper(*args,**kwargs):
#         print("this is deco02")
#         f(*args,**kwargs)
#         print("deco02 is end")
#     return wrapper
# # 类修饰器deco02
# @deco02
# # 类修饰器deco01
# @deco01
# def f(a,b,c):
#     print("hello!")
#     time.sleep(1)
#     print("world!")
#     print("result=%d" % (a+b+c))
# # 执行f函数
# f(3,4,1)
#
# # 内置修饰器property
# class TestClass:
#     name="test"
#     def __init__(self,name):
#         self.name=name
#     @property
#     def sayHello(self):
#         print("hello",self.name)
# test=TestClass("file")
# print(test.name)
# test.sayHello
#
# # 内置修饰器staticmethod
# # 创建类TestClass
# class TestClass:
#     name="test"
#     def __init__(self,name):
#         self.name=name
#     # 添加静态修饰器，不需要创建实例，直接用类名引用
#     @staticmethod
#     def fun(x, y):
#         return x+y
# # 创建实例
# testClass=TestClass("file")
# # 用实例名引用
# print(testClass.name)
# # 用实例名引用
# print(testClass.fun(2,3))
# # 用类名引用
# print(TestClass.fun(2, 3))
#
# # 内置修饰器classmethod
# # 导入time模块
# import time
# # 创建Data类
# class Date:
#     #创建init初始化函数
#     def __init__(self,year,month,day):
#         # 创建变量，它是对象中的属性
#         self.year=year
#         self.month=month
#         self.day=day
#     # 添加classmethod类装饰器
#     @classmethod
#     # 定义now函数
#     def now(cls):
#         tim=time.localtime()
#         return  cls(tim.tm_year,tim.tm_mon,tim.tm_mday)
#     def __str__(self):
#         return '%s-%s-%s' % (self.year, self.month, self.day)
# date=Date.now()
# print(date)
#
# # 创建Cat类
# class Cat:
#     # 对象的初始化
#     def __init__(self,name,age):
#         # 创建变量，它是对象中的属性
#         self.name=name
#         self.age=age
#     # 创建str函数，返回对象的描述信息
#     def __str__(self):
#         return 'name=%s,age=%s' % (self.name,self.age)
#     # 创建eat函数
#     def eat(self):
#         print("%s在吃鱼" % self.name)
#     # 创建drink函数
#     def drink(self):
#         print("%s在喝水" % self.name)
#     # 创建introduce函数
#     def introduce(self):
#         print("name=%s,age=%s" % (self.name,self.age))
# # 创建一个对象
# cat=Cat("汤姆",24)
# print(cat)
# # 实例调用eat函数
# cat.eat()
# # 实例调用drink函数
# cat.drink()
# # 实例调用introduce函数
# cat.introduce()

# # py面试：考查列表和深浅copy
# def f(x,s=[]):
#     # 遍历
#     for i in range(x):
#         # 向列表s添加元素
#         s.append(i*i)
#     # 打印列表s
#     print(s)
# # 调用f，打印0,1
# f(2)
# # 调用f，打印1,2,4，0,1,4
# f(3,[1,2,4])

# # py面试：把123456789变成987654321
# # 考查切片知识，倒叙每一个数
# a="123456789"
# b=a[:-1]
# print(b)
#
# # python面试：简述re模块match() search()findall() compile()
# # 导入re模块
# import re
# # match函数只从字符串的开始匹配
# print(re.match('www','www.baidu.com').span())
# # search函数匹配整个字符串，直到匹配
# print(re.search('b', 'www.baibu.com').span())
# s01="12abcd3"
# # finall函数返回的是匹配所有结果的list
# print(re.findall('12|14','12abcd3'))
# # .匹配除换行以外的任意字符
# c=re.findall('张.丰',"张三丰,张四丰,张五丰")
# print(c)
#
# s = "Levi:1994,Sunny:1993"
# pattern = r"(\w+):(\d+)"
# # 创建对象，将字符串形式编译成patter实例
# regex = re.compile(pattern, flags=0)
# # 按照pattern实例匹配
# l = regex.findall(s, 0, 55)
# print(l)
#
#
# s = "hello world how are  you"
# pattern = r"\W+"
# l = re.split(pattern, s)
# print(l)
#
# # python面试：将a/b/.././c/test.jpg变成a/c/test.jpg
# # 定义s字符串
# s="a/b/.././c/test.jpg"
# # 碰到"/",就分割字符串
# s1=s.split("/")
# # 创建一个空的list
# l=[]
# print(s1)
# # 迭代s1，遍历
# for i in s1:
#     # pop()：删除key，返回value
#     if i=="..":
#         l.pop()
#     # continue：跳出本次剩余的语句，继续下一次循环
#     elif i==".":
#         continue
#     else:
#         # 向空的list添加元素
#         l.append(i)
# print(l)
#
# site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# pop_obj=site.pop('name')
# print (pop_obj)    # 输出 ：菜鸟教程
#
# # python面试：打印99乘法表
# for i in range (1,10):
#     for j in range(1,i+1):
#         # end=''表示不换行加空格
#         print("%d*%d=%d " % (i,j,i*j),end='')
#     # 换行
#     print('')
# # 一行代码打印99乘法表
# print('\n'.join([' '.join(['{}*{}={}'.format(y,x,y*x) for y in range(1, x+1)]) for x in range(1,10)]))
#
# # 找到1000以内的龙腾数，各个位数的和为5的数为龙腾数
# l=[]
# for i in range (0,1000):
#     # 获取百位数字，i//100相等于int（i/100）
#     a=i//100
#     # 获取十位数字
#     b=(i//10) % 10
#     # 获取个位数字
#     c=i % 10
#     if a+b+c==5:
#         # 找到龙腾数放入数组
#         l.append(i)
# # 打印数组
# print(l)
#
# #  # python面试：python给一个有序列表，求出插入值的索引
# # 定义一个函数：求出插入值的索引
# def index(nlist, k):
#     # 假如插入的元素比第一个元素小，则就直接插在第一个元素的位置，第一个元素的索引是0
#     if k < nlist[0]:
#         p = 0
#     # 假如插入的元素比最后一个元素大，则就直接插在最后元素的位置，最后一个元素的索引为len(l)
#     elif k > nlist[-1]:
#         p = len(nlist)
#     else:
#         # p=0归位
#         p = 0
#         # 然后对传过来的列表进行循环打印
#         for item in nlist:
#             # 判断插入的元素的大小
#             if k < item:
#                 # 直到插入的元素大于item了
#                 break
#             p += 1
#     return p
# # 给定有序列表
# lis = [1, 3, 5, 7, 8, 9, 11]
# # 调用index函数，返回索引值
# result = index(lis, 10)
# print(result)
#
# # python面试:s1="aabacbcccab"输出连续的最多的那个数
# s1="aabacbcccab"
# #记录当前元素第几次出现
# cur_number=1
# # 已知最大连续出现次数为1
# max_number=1
# # 记录上一个元素是什么
# pre_element=None
# # 遍历s1
# for i in s1:
#     # 遇到相同元素，计数器加一
#     if i==pre_element:
#         cur_number+=1
#         # 更新最大值
#         max_number=max(max_number,cur_number)
#     else:
#         # 遇到不同元素，刷新计数器
#         pre_element=i
#         # 重新赋值计数器
#         cur_number=1
# # 打印最大值
# print(max_number)
#
# # 创建一个s1字符串
# s1="aabacbcccab"
# # 创建一个空的list
# L= []
# # 计数器初始化
# count = 0
# # 遍历s1
# for i in list(s1):
#     # 如果L为空的列表，为真，L列表里增加s1的第一个数
#     if not L:
#         L.append(i)
#     # 判断s1的第一个数是否等于i，为真就添加
#     elif l[0] == i:
#         L.append(i)
#         if count < len(L):
#             s = [-1]
#             count = len(L)
#     else:
#         L=[]
#         L.append(i)
# print(count, s)
#
# # python面试：s=["a","b","c","d","e","f"]变成s1=["a","e","d","c","b","f"]
# s=["a","b","c","d","e","f"]
# s=s[-2:0:-1]
# print(s)
#
# # 导入xlsxwriter模块:主要用来修改表格的数据
# import xlsxwriter
# target_xlsx="D:/360Downloads/Software/py/demo01.xlsx"
# # 创建工作簿
# workbook=xlsxwriter.Workbook(target_xlsx)
# # 创建工作表
# worksheet=workbook.add_worksheet()
# # 设置工作簿的格式
# font=workbook.add_format({"font_size": 14})
# # 设置工作表的列宽
# worksheet.set_column=("A:A",20)
# # 写值
# worksheet.write(0,0,"Hello",font)
# # 写值
# worksheet.write(0,1,"World",font)
# # 写值
# worksheet.write(2,0, "123",font)
# # 写值
# worksheet.write(3, 0, "123.456", font)
# # 插入一张照片
# worksheet.insert_image("B5", "D:/360Downloads/python.jpg")
# # 关闭工作簿
# workbook.close()


# # 导入xlrd模块：读取源文件的数据
# import xlrd
# # 导入xlsxwriter模块：修改表格的数据
# import xlsxwriter
# # 源文件
# source_xls = ["D:/360Downloads/1.xlsx", "D:/360Downloads/2.xlsx"]
# # 目标文件
# target_xls = "D:/360Downloads/3.xlsx"
# # 从源文件中读取数据
# data = []
# for i in source_xls:
#     wb = xlrd.open_workbook(i)
#     for sheet in wb.sheets():
#         for rownum in range(sheet.nrows):
#             data.append(sheet.row_values(rownum))
# print(data)
# # 创建工作簿写入数据
# workbook = xlsxwriter.Workbook(target_xls)
# # 创建工作表
# worksheet = workbook.add_worksheet()
# # 设置工作簿的格式
# font = workbook.add_format({"font_size":14})
# # 写入数据，遍历工作表的数据个数
# for i in range(len(data)):
#     # 遍历工作表数据的长度
#     for j in range(len(data[i])):
#         # 写入数据
#         worksheet.write(i, j, data[i][j], font)
# # 添加数据
# worksheet.write(4,0,"haha",font)
# # 关闭文件流，要注意关闭Excel表格，不然报错
# workbook.close()
#
# mpsql自连接
# # 导入pymysql模块
# import pymysql
# # 连接database
# conn = pymysql.connect(
#     host="127.0.0.1",
#     user="root",
#     password="123456",
#     database="day59",
#     charset="utf8")
# # 得到一个可以执行SQL语句的光标对象
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 定义sql语句：创建表格
# sql="""
# create table dept(
# deptno INT PRIMARY KEY,
# dname VARCHAR(14),
# loc VARCHAR(13)
# )ENGINE=innodb DEFAULT CHARSET=utf8;
# """
# # # 执行SQL语句
# # cursor.execute(sql)
# # sql="""
# # INSERT INTO dept VALUES
# # (20, 'Research', 'Dallas'),
# # (30, 'Sales', 'Chicago'),
# # (40, 'Operations', 'Boston'),
# # (50, 'Admin', 'Washing');
# # """
# # 定义sql语句：插入数据
# sql="""
# insert into emp values
# (7369, 'Smith',  '1980-12-17',800) ,
# (7499, 'Allen', '1981-2-20',1600) ,
# (7844, 'Turner',  '1981-9-8',1500) ,
# (7698, 'Tom', '1981-9-8',6100) ,
# (7876, 'Adams','1987-5-23',1100) ,
# (7900, 'James',  '1981-12-3',2400) ,
# (7902, 'Ford',  '1981-12-3',3000) ,
# (7901, 'Kik', '1981-12-3',1900);
# """
# # 定义sql语句：删除数据
# # sql="delete from emp where salary=800;"
# # 执行sql语句
# cursor.execute(sql)
# # 提交
# conn.commit()
# # 光标关闭
# cursor.close()
# # 连接关闭
# conn.close()

# # 测试[]的作用
# list1=['physics','chemistry',1997,2000]
# list2=[1,2,3,4,5,6,7]
# print("list1[0]:",list1[0])
# print("list2[1:5]",list2[1:5])
# print("list2[-2]",list2[-2])

# #创建一个二维列表,有5列4行:list_2d = [[0 for col in range(cols)] for row in range(rows)]
# # col表示列，row表示行
# list_2d=[[0 for i in range(5)] for j in range(4)]
# print(list_2d)
# list_2d[0].append(2)
# list_2d[0].append(4)
# list_2d[0].append(6)
# list_2d[2].append(7)
# print(list_2d)

# #a和a[:]是不同的
# a=[1,2,3]
# print(id(a))
# print(id(a[:]))
#
# #导入operator模块
# import operator
# a=[1,2,5]
# # 创建对象b，获取第3个域的值
# b=operator.itemgetter(2)
# # 打印第二个域的值
# print(b(a))
# # 创建对象b，获取第2个域和第1个域的值
# b=operator.itemgetter(1,0)
# # 打印第一个和第零个域的值
# print(b(a))
#
# #导入operator模块
# import operator
# # 定义students列表,是由元组构成的列表
# students=[("John","A",15),("Jane","D",12),("Dave","C",10)]
# #根据第三个域的值排序，并打印结果
# print(sorted(students,key=operator.itemgetter(2)))
#
# #sorted（key=lambda）
# a=[1,5,3,2,7]
# print(a[::-1])
# # 对列表a进行排序并打印
# print(sorted(a))
# # append用于末尾追加新的对象
# a.append(3)
# print(a)
# # insert用于对象插入列表中
# a.insert(3,"A")
# print(a)
# # 重新赋值
# a[0:2]=[12,78]
# print(a)
# # 删除remove
# a.remove("A")
# print(a)
# # 删除del
# del a[0]
# print(a)
# #pop用于移除列表中一个元素，返回删除值，不填数字默认删除最后一个元素
# b=a.pop(0)
# print(a)
# # pop在字典中：删除给定key值和对应的值，返回被删除的值
# site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# print(site.pop("name"))
# print(site)
#
# names=["tangchao","tanglei","deming"]
# scores=[90,89,88]
# # zip打包为元组的列表
# person=zip(names,scores)
# print(list(person))
# # 创建一个dict使用键值（key-value）存储，查找速度快
# d={"tangchao":90,"tanglei":89,"deming":88}
# print(d["tangchao"])
# # 把数据存入dict中
# d["shaozhong"]=87
# print(d)
# # 多次修改就会覆盖前面的值
# d["shaozhong"]=86
# print(d)
# # 测试Tom是否在dict中
# var = "tangchao" in d
# # 返回False表示没有，返回True表示有
# print(var)
# # get函数：返回None或者对应的value
# s=d.get("tangchao")
# print(s)
# # 使用pop：删除key，返回对应的value，在dict中key-value都被删除
# s01=d.pop("tangchao")
# # 打印value
# print(s01)
# print(d)
#
# key=[1,2,3]
# # 错误：key不可以哈希
# d[key]='a list'
#
# # 创建set，需要一个，list作为输入
# s = set([1, 2, 3])
# print(s)
# # set和dict同样,key不可以重复，重复元素被过滤
# s=set([1,2,3,4,1,2,2])
# print(s)
# # add（key）添加元素到set中，可以重复添加但没有效果
# s.add(8)
# print(s)
# # add重复添加没有效果
# s.add(4)
# print(s)
# # remove（key）删除元素
# s.remove(8)
# print(s)
# # s1={1,2,3}
# s1=set([1,2,3])
# # s2={3,5,6}
# s2=set([3,5,6])
# # s1和s2做数字意义上的交集
# s3=s1 & s2
# print(s3)
# # s1和s2做数字意义上的并集
# s4=s1 | s2
# print(s4)
# a=['b','c','a']
# # 对列表a的元素进行排序
# a.sort()
# print(a)
# a="abc"
# # 将'abc'改成'Abc',但没有改变列表a的内容
# b=a.replace("a","A")
# print(b)
# print(a)
#
# # 迭代（Iteration）：给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代
# # 定义d字典
# d={'a':1,'b':2,'c':3}
# # 字典可迭代，做个遍历
# for key in d:
#     # 打印key
#     print(key)
#     # 打印value
#     print(d[key])
# # 字符串也是可迭代对象
# for i in 'ABC':
#     print(i)
#
# # 如何判断一个对象是可迭代对象
# #导入collections.abc模块中的Iterable对象
# import collections.abc
# # 判断str是否可迭代
# a=isinstance('abc',collections.abc.Iterable)
# # 打印迭代结果
# print(a)
# # 导入collections.abc模块
# import collections.abc
# # 判断str是否可迭代
# a=isinstance('abc',collections.abc.Iterable)
# # 打印迭代结果
# print(a)

# # enumerate函数把一个list变成索引-元素对
# # 遍历
# for i,value in enumerate("abc"):
#     # 打印索引-元素值
#     print(i,value)

# # for循环引入两个变量
# for x,y in [(1,2),(1,8)]:
#     # 打印
#     print(x,y)
#
# #定义Findmax_list，使用迭代查找list最大值和最小值，返回一个tuple
# def Findmax_list(L:list):
#     max_number = L[0]
#     min_number = L[0]
#     # list可迭代，做遍历，查找最大值和最小值
#     for i in L:
#         max_number=max(max_number,i)
#         min_number=min(min_number,i)
#     # 返回一个tuple
#     return max_number, min_number
# # 定义一个list
# test_list=[1,6,2,3,4,8]
# # 调用Findmax_list
# result=Findmax_list(test_list)
# # 打印tuple结果
# print(result)
# # 测试返回结果
# print(type(result))
#
# #生成一个list
# list1=list(range(1,11))
# print(list1)
#
# L=[]
# # 创建一个list:生成一个[1,2*2,......,10*10]的列表
# for i in range(1,11):
#     # 向L列表添加元素
#     L.append(i*i)
# print(L)
#
# # 创建一个list：生成一个[1,2*2,.......,10*10]的列表
# L=[x*x for x in range(1,11)]
# print(L)
# # 创建一个list：两层循环生成全排列
# L1=[m+n for m in 'ABC' for n in 'xyz']
# print(L1)
# # 创建一个list：筛选出列表中偶数
# L2=[i for i in range(1,11) if 0 == i % 2]
# print(L2)
#
# # 导入os模块
# import os
# # 创建一个list：列出当前目录下的所有文件名和目录名
# L=[d for d in os.listdir('.')]
# print(L)
#
# # 定义一个dict
# d={"A":1,"B":2,"C":3}
# # dict的items可以同时迭代key和value
# for x,y in d.items():
#     print(x,y)
# # dict的items可以同时迭代key和value
# L=[k+'='+str(v) for k,v in d.items()]
# print(L)
#
# # 定义一个list
# L=["HellO","World","Apple"]
# # 调用lower把list中所有的字母变成小写，如有整数会报错
# L1=[i.lower() for i in L]
# print(L1)
#
#
# x="123"
# y=123
# # isinstance可以判断一个变量是字符串，结果返回True和False
# result=isinstance(x,str)
# # 判断一个变量是否是int
# result2=isinstance(y,int)
# # 打印结果
# print(result)
# # 打印结果
# print(result2)
#
# # 定义一个列表
# L1=["Hello","World",18,"Apple",None]
# # 迭代L1，筛选字符串
# L2=[i for i in L1 if type(i)==str]
# print(L2)
#
# # 创建一个列表用[],
# L=[i for i in range(1,11)]
# print(L)
# # 创建一个生成器generator用（）
# L1=(i for i in range(1,11))
# # next函数返回的生成器的下一个值,实际上值已经抛出生成器
# print(next(L1))
# print(next(L1))
# print(next(L1))
# print(next(L1))
# print(next(L1))
# print(next(L1))
# print(next(L1))
# print(next(L1))
# print(next(L1))
# # print(next(L1))
# # # 没有元素返回，抛出StopIteration停止迭代错误
# print(next(L1))
# #此时 L1是空的
# print(list(L1))
# # 创建一个generator生成器
# L=(i for i in range(1,11))
# # generator是可迭代对象
# for i in L:
#     print(i)
# #导入collection.abc模块
# import collections.abc
# # 判断generator是可迭代对象，返回True和False
# a=isinstance(L,collections.abc.Iterable)
# # 打印结果
# print(a)
#
# #定义一个生成器
# def odd():
#     print("step1")
#     # 每次调用next，遇到yield语句返回，再执行next从上次返回的yield继续执行，打印的是返回值
#     yield 1
#     # 从上次next执行
#     print("step2")
#     # 从上次next执行
#     yield 3
#     print("step3")
#     # 从上次next执行
#     yield 5
# # 创建对象（生成器）
# gener=odd()
# # next返回的是生成器下一个值，实际上值已经抛出生成器
# print(next(gener))
# print(next(gener))
# print(next(gener))
# # 第四次调用next报错，抛出停止迭代错误
# print(next(gener))
# # 生成器可迭代
# for i in gener:
#     # 打印
#     print(i)
#
# # python实现杨辉三角形
# def yanghui():
#     # 定义第一行列表为[1]
#     line = [1]
#     while True:
#         # yield的作用：把一个函数变成生成器，同时返回一个list，下次从yield的下条语句执行
#         yield line
#         # 设上一个为[1],通过式子可得[1,1],继而[1,2,1]......
#         line = [1] + [line[i] + line[i + 1] for i in range(len(line) - 1)] + [1]
#
# # 输入杨辉三角形的行数
# n = int(input("请输入行数："))
# # 定义一个结束的变量
# flag = 0
# # 生成器可迭代，做个遍历
# for i in yanghui():
#     # 打印每行的列表的元素，用空格连接
#     print(" ".join(str(j) for j in i))
#     # 打印完一行，flag+1
#     flag += 1
#     # 如果变量flag等于输入的行数，跳出for循环
#     if flag == n:
#         # 跳出循环
#         break
#
# # 定义f函数，返回的是x*x
# def f(x):
#     return x*x
# # 调用map（），根据传入的函数和list，依次作用于每个元素
# s=map(f,[1,2,3,4,5])
# # 打印返回的迭代器的值
# print(list(s))
# # 查看类型
# print(type(s))
#
# # 定义一个列表
# l=[1,2,3,4,5]
# #()用于创建一个list，结果依次返回列表l的元素的平方，返回list
# s=[i*i for i in l]
# # 打印列表s
# print(s)
# # []用于创建一个生成器，结果依次返回列表l的元素的平方，返回generator
# s1=(i*i for i in l)
# # 以列表形式打印generator的元素值
# print(list(s1))
# # 查看s1的类型
# print(type(s1))

# # 导入requests模块
# import requests
# #定义一个对象，这个对象类型是一个响应，获取网页源码 post:请求服务器接受所指定的文档作为对所标识的URI的新的从属实体
# response = requests.post('https://www.cnblogs.com/Mr-choa/post')
# #调用text：以unicode表示响应内容
# print(response.text)
# # 打印对象的类型:requests.models.Response
# print(type(response))
# # 打印response.textd的类型：str
# print(type(response.text))
# #
# print(response.content)
# print(response.cookies)
# print(response.headers)


#
# import requests
#
#
# def download(url, num_retries=2, user_agent='wswp', proxies=None):
#     '''下载一个指定的URL并返回网页内容
#         参数：
#             url(str): URL
#         关键字参数：
#             user_agent(str):用户代理（默认值：wswp）
#             proxies（dict）： 代理（字典）: 键：‘http’'https'
#             值：字符串（‘http(s)://IP’）
#             num_retries(int):如果有5xx错误就重试（默认：2）
#             #5xx服务器错误，表示服务器无法完成明显有效的请求。
#             #https://zh.wikipedia.org/wiki/HTTP%E7%8A%B6%E6%80%81%E7%A0%81
#     '''
#     print('==========================================')
#     print('Downloading:', url)
#     headers = {'User-Agent': user_agent} #头部设置，默认头部有时候会被网页反扒而出错
#     try:
#         resp = requests.get(url, headers=headers, proxies=proxies) #简单粗暴，.get(url)
#         html = resp.text #获取网页内容，字符串形式
#         if resp.status_code >= 400: #异常处理，4xx客户端错误 返回None
#             print('Download error:', resp.text)
#             html = None
#             if num_retries and 500 <= resp.status_code < 600:
#                 # 5类错误
#                 return download(url, num_retries - 1)#如果有服务器错误就重试两次
#
#     except requests.exceptions.RequestException as e: #其他错误，正常报错
#         print('Download error:', e)
#         html = None
#     return html #返回html
#
# print(download('http://www.baidu.com'))
#
# 导入requests模块
# import requests
# # 获取一个网页响应对象
# response = requests.get("https://www.baidu.com")
# # 打印响应的类型:requests.models.Response'
# print(type(response))
# #打印响应的状态代码:200
# print(response.status_code)
# # 打印响应的文本的类型:str
# print(type(response.text))
# # .text返回的是unicode类型
# print(response.text)
# response.encoding("utf-8")
# print("-----")
# print(response.text.encode("utf-8"))
# print("----")
# print(response.content)
# print(response.content.decode("utf-8"))
# print(response.text)
# print("-----------------------------")
# response.enconding = "utf-8'
# print(response.text)
#
# print(response.cookies)
#
# print(response.content)
# print(response.content.decode("utf-8"))
#
# import requests
# url = 'http://httpbin.org/get'
# data = {
#     'name': 'zhangsan',
#     'age': '25'
# }
# response = requests.get(url, params=data)
# print(response.url)
# print(response.text)






# import requests
# r=requests.post('https://www.cnblogs.com/Mr-choa/')
# print(r.text)
# print("----------------------")
# r=requests.put('https://www.cnblogs.com/Mr_choa/put')
# print(r.text)
# r=requests.delete('https://www.cnblogs.com/Mr_choa/delete')
# print(r.text)
# r=requests.head('https://www.cnblogs.com/Mr_choa/head')
# print(r.text)
# # requests.options('http://www.cnblogs.com/Mr_choa/get')

# #导入requests模块
# import requests
# # 导入json解析模块
# import json
# #传入一个headers
# headers = {
#  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
# }
# #请求指定的页面信息，并返回实体主体
# response=requests.get('https://www.zhihu.com/explore', headers=headers)
# #以字符串形式返回
# print(response.text)
#
# #导入requests模块
# import requests
# # 导入json模块
# import json
# # 定义一个dict
# data={"name":"Mr_choa1","age":24}
# # post请求
# response=requests.post("http://httpbin.org/post",data=data)
# # 以字符串形式返回
# print(response.text)

# # 导入requests模块
# import requests
# # get请求
# response = requests.get('http://www.jianshu.com')
# # 状态代码类型：int 状态代码是403
# print(type(response.status_code), response.status_code)
# # headers类型：requests.structures.CaseInsensitiveDict
# print(type(response.headers), response.headers)
# # cookies类型：requests.cookies.RequestsCookieJar
# print(type(response.cookies), response.cookies)
# # url类型：str
# print(type(response.url), response.url)
# # history类型：list
# print(type(response.history), response.history)
#
# # 导入requests模块
# import requests
# # get请求
# response=requests.get("https://fanyi.baidu.com")
# # 获取cookies
# print(response.cookies)
# # 获取cookies信息
# print(tuple(response.cookies))
# # 调用items，遍历一个dict的key和value
# for key,value in response.cookies.items():
#     print(key+"="+value)
#
# # 导入requests模块
# import requests
# # get请求
# response= requests.get('http://fanyi.baidu.com')
# # 访问cookies的值
# print(response.cookies['BAIDUID'])
# # 以元组形式返回cookies
# print(tuple(response.cookies))
# # 导入requests模块
# import requests
# # 定义cookies
# cookies = {'testCookies_1': 'Hello_Python3', 'testCookies_2': 'Hello_Requests'}
# # 在Cookie Version 0中规定空格、方括号、圆括号、等于号、逗号、双引号、斜杠、问号、@，冒号，分号等特殊符号都不能作为Cookie的内容。
# r = requests.get("http://httpbin.org/cookies", cookies=cookies)
# #以字符串返回
# print(r.text)

# # 导入requests模块
# import requests
# # 导入json模块
# import json
# # 定义cookies，dict形式
# cookies={"number":"1234567"}
# # get请求，加上
# response=requests.get("http://httpbin.org/cookies",cookies=cookies)
# # 以字符串形式返回
# print(response.text)

# # 导入requests模块
# import requests
# # 建立session对象
# session = requests.session()
# # get请求
# response = session.get('http://httpbin.org/cookies/set/number/1234567')
# # 以字符串形式返回
# print(response.text)

# # 导入requests模块
# import requests
# # get请求,关闭证书验证
# response = requests.get('https://www.12306.cn',verify=False)
# # 在请求https时，request会进行证书的验证，如果验证失败则会抛出异常
# print(response.status_code)

# # 导入requests模块
# import requests
# # get请求
# response = requests.get('https://www.12306.cn',cert=('/path/server.crt', '/path/key'))
# # 返回状态代码
# print(response.json())

# # 导入requests模块
# import requests
# # get请求
# response= requests.get('https://www.baidu.com')
# # 以元组形式返回cookies
# print(tuple(response.cookies))
# print(response.cookies)
#
# # 导入xlsxwriter模块
# import xlsxwriter
# # 目标文件
# target_xlsx="D:/360Downloads/test01.xlsx"
# # 创建工作簿
# workbook=xlsxwriter.Workbook(target_xlsx)
# # 创建名叫person的工作表
# worksheet=workbook.add_worksheet("person")
# # 设置工作簿的格式
# font=workbook.add_format({"font_size": 14})
# # 设置工作表的列宽
# worksheet.set_column=("A:A",20)
# # 设置表头
# headings=["name","testA","testB"]
# # 自己造的数据
# data=[
#     ["Mr_choa","Mr_lai","Mr_z",'Mr_r',"Mr_d"],
#     [90,80,70,87,56],
#     [100,50,40,45,68]
# ]
# # 表头按行写入数据
# worksheet.write_row(0,0,headings)
# #造的数据按列写入数据
# worksheet.write_column("A2",data[0])
# worksheet.write_column("B2",data[1])
# worksheet.write_column('C2',data[2])
# # 创建折线图
# workchart=workbook.add_chart({'type':'scatter'})
# # 给图表设置格式
# workchart.add_series(
#     {
#         # 折线名称
#         'name':'=person!$B$1',
#         'categories':'=person!$A$2:$A$6',
#         # 折线的值
#         'values':'=person!$B$2:$B$6',
#         # 折线颜色
#         'line':{'color':'red'}
#     }
# )
# workchart.add_series(
#     {
#         # 折线名称
#         'name':'=person!$C$1',
#         'categories':'=person!$A$2:$A$6',
#         # 折线的值
#         'values':'=person!$C$2:$C$6',
#         # 折线的颜色
#         'line':{'color':'blue'}
#     }
# )
# # 设置图表的表头
# workchart.set_title({'name':'测试'})
# workchart.set_x_axis({'name':'x轴'})
# workchart.set_y_axis({'name':'y轴'})
# # 设置图表样式类型
# workchart.set_style(1)
# # 设置图表的位置
# worksheet.insert_chart('A10',workchart,{'x_offset':25,'y_offset':10})
# # 关闭文件流，要注意关闭Excel表格，不然报错
# workbook.close()


# # 创建一个dict，存放图书
# books={"倚天屠龙记":{"id":1,"price":100.00},
#        "好吗好的":{"id":2,"price":200.00},
#        "告别薇安":{"id":3,"price":300.00},
#        "穆斯林的葬礼":{"id":4,"price":400.00}
#        }
# # 创建一个list
# menu=["1、添加新书","2、修改书架","3、删除书架","4、查询书架","5、退出系统"]
#
# # 系统启动+菜单展示
# def start():
#     print("欢迎使用图书馆管理系统")
#     # 菜单展示
#     for i in menu:
#         print("**%s**" % i)
#     choose()
#
# # 功能选择
# def choose():
#     choosenum = input("请选择一个功能：")
#     # 添加新书
#     if choosenum=="1":
#         print("添加新书中....")
#         while True:
#             add_bookname = input("输入要添加的书名：")
#             # 如果图书馆已经有这本书
#             if ifexist(bookname=add_bookname):
#                 s=input("已经有这本书了！\n请输入0重新选择功能，输入1继续添加新书：")
#                 # 输入0回到choose（）
#                 if s=="0":
#                     return choose()
#                 # 输入1停止剩余的语句，继续下一次的循环
#                 elif s=="1":
#                     continue
#                 else:
#                     print("输入有误，已退出！")
#                     # 退出系统
#                     exit()
#             # 如果图书馆没有这本书，跳出while循环
#             else:
#                 break
#         while True:
#             add_bookid = input("请输入要放得书架号：")
#             # 如果书架号已经被占用
#             if ifexist(bookid=add_bookid):
#                 s=input("这个书架已经被占用了！\n请输入0重新选择功能，输入1继续添加书架：")
#                 if s=="0":
#                     return choose()
#                 elif s=="1":
#                     continue
#                 else:
#                     print("输入有误，已退出！")
#                     exit()
#             # 如果书架号没有被占用，跳出while循环
#             else:
#                 break
#         # 输入书的价格
#         add_bookprice=input("请输入书的价格：")
#         # 创建一个dict
#         add_bookidprice={"id":add_bookid,"price":add_bookprice}
#         # 往图书馆中添加新书
#         newbook(add_bookname,**add_bookidprice)
#         # 展示所有的图书
#         showbooks(**books)
#     # 修改书架
#     elif choosenum=="2":
#         # 输入书名
#         update_bookname=input("请输入要修改的书名：")
#         # 对着书名，修改其书架号和价格
#         updatebook(update_bookname)
#     # 删除书架
#     elif choosenum=="3":
#         # 输入书名
#         del_bookname = input("请选择要删除的书名：")
#         # 删除这本书的所有的记录
#         deletebook(del_bookname)
#     # 查询书架
#     elif choosenum=="4":
#         # 展示所有的图书
#         showbooks(**books)
#     # 退出系统
#     elif choosenum=="5":
#         print("退出系统！")
#         # 退出系统
#         exit()
#     else:
#         # 输入的功能不是1、2、3、4、5，抛出“输入的参数有误”
#         if isinstance(choosenum, str):
#             raise TypeError("输入参数有误！")
#         else:
#             # 退出系统
#             exit()
#
# # 修改书架
# def updatebook(bookname):
#     # 查看书本是否已经存在
#     if ifexist(bookname=bookname):
#         num=input("你想修改什么呢？输入1修改书架号，输入2修改价格,输入其他退出：")
#         # 修改书的书架号
#         if num=="1":
#             while True:
#                 updatebook_id=input("你想放几号书架？：")
#                 # 查看书架号是否被占用
#                 if ifexist(bookid=updatebook_id):
#                     print("这个书架已经满了！")
#                     # 停止剩下的语句，继续下一次循环
#                     continue
#                 else:
#                     # 修改书架号
#                     books[bookname]["id"]=int(updatebook_id)
#                     print("成功修改书架号！")
#                     # 展示所有的图书
#                     showbooks(**books)
#         # 修改书的价格
#         elif num=="2":
#             updatebook_price=float(input("输入新的价格："))
#             # 修改输的价格
#             books[bookname]["price"]=updatebook_price
#             print("成功修改价格！")
#             # 展示所有的图书
#             showbooks(**books)
#         else:
#             # 退出系统
#             exit()
#     # 图书馆没有这本书，返回主键面
#     else:
#         print("图书馆没有这本书！")
#         return choose()
# #删除书架
# def deletebook(bookname):
#     # 查看图书馆是否有这本书
#     if ifexist(bookname=bookname):
#         # 删除这本书
#         books.pop(bookname)
#         print("已删除%s" % bookname)
#         # 返回主键面
#         return choose()
#     else:
#         print("图书馆没有这本书！")
#         return choose()
#
# # 新书存入图书馆
# def newbook(bookname,**kwargs):
#     # 新书存入图书馆中
#     books[bookname]=kwargs
#     print("添加成功了！")
#
# # 展示图书馆的所有的图书
# def showbooks(**kwargs):
#     # 遍历books
#     for i in kwargs:
#         print("name=%s,id=%d,price=%.2f" % (i,int(books[i]["id"]),float(books[i]["price"])))
#     # 遍历完返回主键面
#     return choose()
#
# # 判断书名或者id是否存在于图书馆系统中
# def ifexist(bookname='',bookid=''):
#     # 书名不为空
#     if bookname != '':
#         # 如果图书馆有这本书，返回True
#         if bookname in books:
#             return True
#         # 图书馆没有这本书，返回False
#         else:
#             return False
#     else:
#         # 遍历一个dict
#         for i in books:
#             # 如果输入参数bookid等于某个图书馆书架的id，返回True
#             if int(bookid)==books[i]['id']:
#                 return True
#         return False
# # 程序启动
# start()

# # 定义一个列表
# l=[1,2,3,4,5]
# #[]用于创建一个list，结果依次返回列表l的元素的平方，返回list
# s=[i*i for i in l]
# # 打印列表s
# print(s)
# # ()用于创建一个生成器，结果依次返回列表l的元素的平方，返回generator
# s1=(i*i for i in l)
# # 以列表形式打印generator的元素值
# print(list(s1))
# # 查看s1的类型
# print(type(s1))

# 导入functools模块
import functools
# 求序列和
def add(x,y):
    return x+y
# 效果就是（（（（（1+2）+3）+4）+5）+6）=21
print(functools.reduce(add,[1,2,3,4,5,6]))




