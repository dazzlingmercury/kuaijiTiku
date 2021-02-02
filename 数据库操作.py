


from PyQt5.QtSql import QSqlDatabase,QSqlQuery,QSqlQueryModel


# id,question,answer,parsing = first.createDB()
# question0 = str(question).split('\n')[0]
# question1 = str(question).split('\n')[1]
# question2 = str(question).split('\n')[2]
# question3 = str(question).split('\n')[3]
# question4 = str(question).split('\n')[4]
# font = QtGui.QFont()
#         # 字体
#         font.setFamily('微软雅黑')
#         # 加粗
#         font.setBold(True)
#         # # 大小
#         font.setPointSize(13)
#         # font.setWeight(75)
#         # self.label.setFont(font)
#         # self.label.setText("<font color=%s>%s</font>" % ('#8968CD', "平凡之路"))
#         self.plainTextEdit.setFont(font)












# 数据库名称，传入数字，题包名字
def createDB(tiku,num_1,ti_bao):

    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('{}'.format(tiku))
    if not db.open():
        print("无法建立")
        return False

    query = QSqlQuery("select id,question,answer,parsing from {} limit {}-1,1;".format(ti_bao,num_1))

    if not query.exec_():
        query.lastError()
    else:
        while query.next():
            id = query.value(0)
            question = query.value(1)
            answer = query.value(2)
            parsing = query.value(3)
            db.close()

            return id,question,answer,parsing





#获取记录数
def getTotalRecordCount(tiku,ti_bao):
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('{}'.format(tiku))
    if not db.open():
        print("无法建立")
        return False
    queryModel = QSqlQueryModel()
    queryModel.setQuery("select * from {}".format(ti_bao))
    rowCount = queryModel.rowCount()
    return rowCount

#写入错题库
def xie_ru(tiku,ti_bao,id,question,answer,Parsing):
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('{}'.format(tiku))
    if not db.open():
        print("无法建立")
        return False
    query = QSqlQuery()
    # query.exec(
    #      "create table '错题1'('id' int PRIMARY KEY ,'question' Text ,'answer' Text ,'Parsing' Text )")
    # # query.exec("insert into people VALUES (1,'李宁','上海')")
    query.exec("insert into '{}'VALUES ({},'{}','{}','{}')".format(ti_bao,id,question,answer,Parsing))

    return True







