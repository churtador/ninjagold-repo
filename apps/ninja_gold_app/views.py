from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    request.session['gold']
    context = {
        "gold": request.session['gold'],
        "act": request.session['activities']
    }
    return render(request, 'index.html', context)

def process_money(request):
    # print(request.POST)
    # print(request.POST['quest'])
    # print("*"*10)
    if request.POST['quest'] == 'farm' and request.session['gold'] >= 0:
        print("*"*20)
        earnGold = random.randint(10,20)
        print(f"Earned {earnGold} from the {request.POST['quest']}!")
        request.session['gold'] += earnGold
        print("*"*20)
    elif request.POST['quest'] == 'cave' and request.session['gold'] >= 0:
        print("*"*20)
        earnGold = random.randint(5,10)
        print(f"Earned {earnGold} from the {request.POST['quest']}!")
        request.session['gold'] += earnGold
        print("*"*20)
    elif request.POST['quest'] == 'house' and request.session['gold'] >= 0:
        print("*"*20)
        earnGold = random.randint(2,5)
        print(f"Earned {earnGold} from the {request.POST['quest']}!")
        request.session['gold'] += earnGold
        print("*"*20)
    elif request.POST['quest'] == 'casino' and request.session['gold'] >= 0:
        print("*"*20)
        earnGold = random.randint(-50,50)
        request.session['gold'] += earnGold
        if request.session['gold'] < 0:
            request.session['gold'] = 0
            earnGold = 0
        print(f"Earned {earnGold} from the {request.POST['quest']}!")
        print("*"*20)

    request.session['activities'] += f"Earned {earnGold} from the {request.POST['quest']}!\n"
    return redirect("/")

def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = ""
    return redirect("/")