from django.shortcuts import render

def calculator(request):
    ans = ''
    c = ""
    try:
        if request.method == "POST":
            if request.POST['num1'] == "":
                return render (request,"calculator.html",{'error':True})
            n1 = eval(request.POST['num1'])
            n2 = eval(request.POST['num2'])
            opr = request.POST['opr']
            if opr == "+":
                ans = n1+n2
            elif opr == "-":
                ans = n1-n2
            elif opr == "*":
                ans = n1*n2
            elif opr == "/":
                ans = n1/n2
    except:
        c = "You Provide Invalid Data Format"
    data = {
        'output':ans,
        'c':c
    }
    return render(request,'calculator.html',data)