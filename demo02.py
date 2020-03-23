menu = ['1.添加新书', '2.修改书柜', '3.删除书柜', '4.查询书架', '5.退出系统']
books = {'侠客风云传': {'id': 1, 'price': 100}, '金庸群侠转': {'id': 2, 'price': 200}, '射雕英雄传': {'id': 3, 'price': 300},
         '倚天屠龙记': {'id': 4, 'price': 400}, '鹿鼎记': {'id': 5, 'price': 500}}


def choose(*args, func='nothing'):
    # 判断选择菜单的情况
    if func == 'caidan':
        choosenum = input('\n\n请选择一个功能：')

        # 添加新书
        if choosenum == '1':
            bookname = input('\n请输入书的名称：')
            # 判断书名存在，则返回菜单列表
            if ifexist(bookname=bookname):
                print('有这本书了，不用瞎折腾了！\n')
                return choose()

            # 判断书的id存在，换一个书柜，或者选择0退出
            bookid = input('\n请输入放入的书柜：')
            while True:
                if ifexist(bookid=bookid):
                    bookid = int(input('\n这个书柜被占用了，换一个书柜放吧，按0退出！'))
                    if bookid == 0:
                        return choose()
                    else:
                        continue
                else:
                    break

            bookprice = int(input('\n请输入新书的价格：'))
            newbook = {'id': bookid, 'price': bookprice}
            newboos(bookname, **newbook)
        # 修改书
        elif choosenum == '2':
            updatebook(bookname=input('\n\n请输入你想要修改的书名：\n\n'))

        # 删除书架
        elif choosenum == '3':
            bookname = input('\n\n请输入您需要删除的书名：\n\n')
            deletebook(bookname=bookname)
        # 查询书架
        elif choosenum == '4':
            showboos(**books)
        # 退出系统
        elif choosenum == '5':
            print('\n\n退出系统成功，欢迎下次光临!\n\n')
            pass
        # 输入异常
        else:
            if isinstance(choosenum, str):
                raise TypeError('输入参数错误')
            else:
                return

    # 判断选择的是通用情况
    elif func == 'nothing':
        input('\n 请按任意键+回车继续')
        domenu(*menu)

    else:
        pass


# 判断是否存在书名或者书的id
def ifexist(*args, bookname='', bookid=''):
    # 判断传入的是书名还是 id
    if bookname != '':
        # 检查是否存在同样的书并返回，存在返回True，不存在返回False
        if bookname in books:
            return True
        else:
            return False

    else:
        # 遍历books，检查是否存在相同的id，存在返回true,不存在返回false
        for x in books:
            if int(bookid) == books[x]['id']:
                return True
        return False


# 系统启动  +  菜单展示
def domenu(*args):
    print('''
        //////////////////////////////////////
        ///////  欢迎使用图书管理系统  ///////
        //////////////////////////////////////


    ''')
    print('               ******************')
    for x in args:
        print('               **  %s  **\n' % x)
    print('               ******************')
    choose(func='caidan')


# 展示书柜列表
def showboos(**kw):
    print('''
    /////////////////////////////////////////////////////////////
    /////////////////////图书列表////////////////////////////////
    /////////////////////////////////////////////////////////////
    '''
          )
    for x in kw:
        print('     ////《%s》   --->   第 %2d 个书柜中   ---> 价格 %d 元' % (x, books[x]['id'], float(books[x]['price'])))

    print('''
    /////////////////////////////////////////////////////////////
    '''
          )
    choose()


# 添加新书
def newboos(bookname, **kw):
    # 将新书存入书架
    books[bookname] = kw
    print('\n添加成功了！\n')
    return showboos(**books)


# 删除书
def deletebook(*args, bookname):
    if ifexist(bookname=bookname):
        books.pop(bookname)
        print('\n\n《%s》已删除！\n\n' % bookname)
        return choose()
    else:
        print('\n\n老铁，没有这本书啊\n')
        return choose()


# 修改书
def updatebook(*args, bookname):
    if ifexist(bookname=bookname):
        choosenum = int(input('\n\n想改什么？ 1:书柜号  2:价格  3:其它按键退出'))
        # 改书柜号
        if choosenum == 1:
            while True:
                newnum = int(input('\n\n你想将书放在第几个书柜？\n\n'))
                if ifexist(bookid=newnum):
                    print('\n\n此书柜已经被其它书占用了！\n')
                    x = input('按1选择其它书柜，按其它按键退出修改\n')
                    if x == '1':
                        continue
                    else:
                        return choose()
                else:
                    books[bookname]['id'] = newnum
                    print('\n\n《%s》已经成功移动到第%d个书柜了！\n\n' % (bookname, newnum))
                    return showboos(**books)
        elif choosenum == 2:
            newprice = int(input('\n\n请输入《%s》新的价格：' % bookname))
            books[bookname]['price'] = newprice
            print('\n\n《%s》以经将价格修改为%d' % (bookname, newprice))
            return showboos(**books)
    else:
        print('\n\n并没有这个书，你再想想？？\n\n')
        return choose()


domenu(*menu)