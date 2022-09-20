from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *


# Create your views here.
def exam(request):
    if request.method == 'POST':
        print(request.POST)
        questions = Exam.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score / (total * 10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'tools/result.html', context)
    else:
        questions = Exam.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'tools/exam.html', context)


def addQuestion(request):
    if request.user.is_staff:
        form = addQuestionform()
        if (request.method == 'POST'):
            form = addQuestionform(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'tools/addQuestion.html', context)
    else:
        return redirect('exam')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = createuserform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        context = {
            'form': form,
        }
        return render(request, 'tools/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {}
        return render(request, 'tools/login.html', context)


def logoutPage(request):
    logout(request)
    return render(request, 'tools/home.html')


def home(request):
    return render(request, 'tools/home.html')


def edmodo(request):
    return render(request, 'tools/edmodo.html')


def wordpress(request):
    return render(request, 'tools/wordpress.html')


def prezi(request):
    return render(request, 'tools/prezi.html')


def dropbox(request):
    return render(request, 'tools/dropbox.html')


def teacher(request):
    return render(request, 'tools/teacher.html')
