from django.shortcuts import render
import pymysql.connections
import pandas as pd
# Create your views here.

mydb = pymysql.Connect(
    host="sql6.freesqldatabase.com",
    user="sql6422998",
    password="LRTwDMwFpC",
    database="sql6422998"
)

mycursor = mydb.cursor()


mycursor.execute("SELECT * FROM datalog where OPC_IOT_FLOW_TIMESTAMP > now() - interval 1 hour ")


myresult = mycursor.fetchall()
datalist = list(myresult)
df = pd.DataFrame(datalist, columns=['ID', 'CHEFF', 'ENERGY', 'FLOW', 'TIME', 'LEVEL', 'PRESS', 'TEMP'])


def output(request):
    datatohtml = []
    for i in range(df.shape[0]):
        temp = df.loc[i]
        datatohtml.append(dict(temp))

    return render(request, 'index.html', {'arr_users': datatohtml})


