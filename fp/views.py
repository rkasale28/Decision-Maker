from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt


# Create your views here.
def home(request):
    df=pd.read_excel('static/excel/IDC.xlsx',sheet_name='FP')
    x_test=np.array([140]).reshape(-1,1)
    y_pred=[]

    X=np.array(df['No. of responses'])
    Y=[np.array(df['DIP']),np.array(df['AIS']),np.array(df['SEO']),np.array(df['SA']),np.array(df['UE']),np.array(df['ACN'])]

    titles=['DIP','AIS','SEO','SA','UE','ACN']
    x1=X.tolist()
    num=0
    for y in Y:
        reg = LinearRegression().fit(X.reshape(-1,1), y)
        p=reg.predict(x_test)
        y_pred.append(round(p[0],0))
        y1=y.tolist()

        fig = plt.figure(figsize=(6,4))
        plt.plot(x1, y1,'o-b')
        
        plt.title(titles[num])

        plt.xticks([15,25,35,45,55,65])
        num+=1

        plt.xlabel('Total No. of Students')
        plt.ylabel('Students in favour')
        
        for i,j in zip(X,y):
            plt.annotate(str(round(j,0)),xy=(i-0.7,j+0.01))
        plt.tight_layout()
        fig.savefig('static/images/fp/'+titles[num-1]+'.jpg')
    
    fig, ax = plt.subplots(figsize=(12,4))
    plt.bar(titles, y_pred, color = 'b')
    plt.yticks([0,50,100])
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x()+(p.get_width()/2), p.get_height() * 1.01))

    plt.xlabel('Subject')
    plt.ylabel('Expected no. of Students in favour')
    plt.title('Prediction for total 140 students')
        
    plt.tight_layout()
    fig.savefig('static/images/fp/analysis.jpg')

    included=sum(y_pred)
    missed=(140-included)
    
    return render(request, 'fp_home.html',{'missed':missed,'included':included,'titles':titles})