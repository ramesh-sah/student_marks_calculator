from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def Marksheet(request):
    name = None
    english = None
    maths = None
    science = None
    computerscience = None
    socialstudies = None
    total = None
    percentage = None
    grade = None
    data = {}
    if request.method == "POST":
        name = request.POST.get('name')
        english = int(request.POST.get("english"))
        maths = int(request.POST.get("maths"))
        science = int(request.POST.get("science"))
        computerscience = int(request.POST.get("computerscience"))
        socialstudies = int(request.POST.get("socialstudies"))

    try:
        if (english < 100, maths < 100, science < 100, computerscience < 100, socialstudies < 100):
            total = english+maths+science+computerscience+socialstudies
            percentage = total*100/500
            try:
                if (percentage <= 100 and percentage >= 80):
                    grade = "A Grade"
                elif (percentage < 80 and percentage >= 60):
                    grade = "B Grade"
                elif (percentage < 60 and percentage >= 40):
                    grade = "C Grade"
                elif (percentage < 40 and percentage >= 20):
                    grade = "D Grade"
                else:
                    grade = "E Grade"
            except:
                pass
        print(name, english, maths, science, computerscience,
              socialstudies, total, percentage, grade)
        data = {'name': name, 'english': english, 'maths': maths, 'science': science, 'computerscience': computerscience,
                'socialstudies': socialstudies, 'total': total, 'percentage': percentage, 'grade': grade}

    except:
        pass

    return render(request, "index.html", data)
