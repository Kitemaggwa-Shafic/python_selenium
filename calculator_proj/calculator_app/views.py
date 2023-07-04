from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .models import Computation
from .forms import *

# Create your views here.

def index(request):
    return render(request, "index.html")

def calculate(request):
    answer = ''
    data = Computation.objects.all()

    form = CalculatorForm(request.POST)   
    if request.method == "POST":
           
        if form.is_valid():
            first_number = request.POST.get("first_number")
            operand = request.POST.get("operation")
            second_number = request.POST.get("second_number")
            if operand == "+":
                answer = int(first_number) + int(second_number)
            elif operand == "-":
                answer = int(first_number) - int(second_number)
            elif operand == "/":
                answer = int(first_number) / int(second_number)
            elif operand == "*":
                answer = int(first_number) * int(second_number)
            #return answer
            
            data = Computation(first_number=first_number, operation=operand, second_number=second_number, answer=answer)
            data.save()
            data = Computation.objects.last()
            #form.save()


        context = {
            'form': form,
            'data': data,
            'answer': answer,
            }
        #return redirect("index")
        #return HttpResponseRedirect(reverse("index"))

    return render(request, "index.html", {'answer': answer})

def read_history(request):
    computations = Computation.objects.order_by("-id")[:5]
    #return redirect("index")
    return render(request, "index.html", {"computations":computations})