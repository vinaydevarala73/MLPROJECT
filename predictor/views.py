from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, "predictor/home.html")
def predict_diabetes(request):
    if request.method == "POST":
        age = int(request.POST.get("age"))
        glucose = float(request.POST.get("glucose"))
        bmi = float(request.POST.get("bmi"))

        # Example logic: Simple diabetes prediction rule
        if glucose > 140 or bmi > 30:
            prediction = "You may be at risk for diabetes. Please consult a doctor."
        else:
            prediction = "You are not at significant risk for diabetes."

        return render(request, "predictor/predict.html", {"prediction": prediction})
    
    return render(request, "predictor/predict.html")
