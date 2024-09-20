from django.shortcuts import render

from django.http import HttpResponse

from joblib import load
model = load('./savedModels/model4.joblib')

def predictor(request):
    if request.method == 'POST':
        Pclass = request.POST['Pclass']
        Sex = request.POST['Sex']
        Age = float(request.POST['Age'])
     
        Embarked = request.POST['Embarked']

        y_pred = model.predict([[ Pclass,Sex,Age,Embarked]])
        if y_pred[0] == 0:
            y_pred = 'Not Survived'
        elif y_pred[0] == 1:
            y_pred = 'Survived'
        else:
            y_pred = 'Virginica'
        return render(request, 'result.html', {'result' : y_pred})
    return render(request, 'main.html')

def su(request,mata):
    return HttpResponse(mata)