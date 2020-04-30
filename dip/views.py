from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt


# Create your views here.
def home(request):
    df=pd.read_excel('static/excel/IDC.xlsx')
    x_test=np.array([140]).reshape(-1,1)
    y_pred=[]

    X=np.array(df['No. of responses'])
    Y=[np.array(df['1st Pref']),np.array(df['2nd Pref']),np.array(df['3rd Pref']),np.array(df['4th Pref']),np.array(df['5th Pref']),np.array(df['6th Pref'])]

    x1=X.tolist()
    num=1
    for y in Y:
        reg = LinearRegression().fit(X.reshape(-1,1), y)
        p=reg.predict(x_test)
        y_pred.append(p[0])
        y1=y.tolist()

        fig = plt.figure(figsize=(12,4))
        plt.bar(x1, y1,color = 'b', width = 2)
        
        if (num==1):
            plt.title('DIP as 1st Preference')
        elif (num==2):
            plt.title('DIP as 2nd Preference')
        elif (num==3):
            plt.title('DIP as 3rd Preference')
        else:
            plt.title('DIP as '+str(num)+'th Preference')

        plt.xticks([0,20,40])
        num+=1

        plt.xlabel('Total No. of Students')
        plt.ylabel('Students in favour')
        
        for i,j in zip(X,y):
            plt.annotate(str(round(j,0)),xy=(i-0.7,j))
        plt.tight_layout()
        fig.savefig('static/images/pref_num_'+str(num-1)+'.jpg')


    x_test=[1,2,3,4,5,6]
    
    fig = plt.figure()
    plt.plot(x_test, y_pred, 'o-b')
    for i,j in zip(x_test,y_pred):
        plt.annotate(str(int(j)),xy=(i-0.07,j+0.9))

    plt.xlabel('Preference No.')
    plt.ylabel('Expected no. of Students in favour')
    plt.title('Prediction for total 140 students')
        
    plt.tight_layout()
    fig.savefig('static/images/analysis.jpg')
    return render(request, 'home.html')