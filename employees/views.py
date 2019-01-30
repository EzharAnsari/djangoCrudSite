from django.shortcuts import render,redirect
from django.views.generic import TemplateView, CreateView
from .forms import UserLogin,UserRegister,StudentRegister
from django.shortcuts import get_list_or_404, get_object_or_404
from.models import UserAdd, Student
from django.contrib.auth.decorators import login_required




class Check(TemplateView):
    template_name = 'base.html'


class Main(TemplateView):
    template_name = 'main.html'


def login(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            first_person = UserAdd.objects.all()
            t = 1
            pk = 0
            for users in first_person:
                if username == users.username:
                    if password == users.password:
                        pk = users.pk
                        t = t + 1
            if t == 1:
                print('Username or password is wrong')
            else:
                print('True')
                t = 'home/' + str(pk)
                return redirect('home', pk)
    else:
        form = UserLogin()
    return render(request, 'login/login.html', {'form': form})

def createUser(request):
    if request.method =='POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            post = form.save(commit = 'false')
            post.save()
            t = str(post.pk)+'/employee_detail'
            # return employee_detail(request,post.pk)
            return redirect(t, pk=post.pk)
    else:
        form = UserRegister()
    return render(request, 'createUser/cr.html', {'form': form})


# Employee Details view files
def employee_detail(request, pk):
    post = get_object_or_404(UserAdd, pk = pk)
    return render(request, 'createUser/employee_detail.html', {'post':post})



# Employee edit
def employee_edit(request, pk):
    post = get_object_or_404(UserAdd, pk=pk)
    if request.method == "POST":
        form = UserRegister(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('employee_detail', pk=post.pk)
    else:
        form = UserRegister(instance=post)
    return render(request, 'createUser/cr.html', {'form': form})



# Home page after user Login
@login_required
def index(request, pk):
    post = get_object_or_404(UserAdd, pk=pk)
    return render(request, 'home/home.html', {'post':post})



# Add Students
def createStudent(request):
    if request.method =='POST':
        form = StudentRegister(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = 'false')
            post.save()
            t = str(post.pk)+'/student_detail'
            # return employee_detail(request,post.pk)
            return redirect(t, pk=post.pk)
    else:
        form = StudentRegister()
    return render(request, 'studentDetail/cs.html', {'form': form})


# Student Details
def student_detail(request, pk):
    post = get_object_or_404(Student, pk = pk)
    return render(request, 'studentDetail/student_detail.html', {'post':post})


# Student detail Edit
def student_edit(request, pk):
    post = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentRegister(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('student_detail', pk=post.pk)
    else:
        form = StudentRegister(instance=post)
    return render(request, 'studentDetail/cs.html', {'form': form})



# Student list

def studenList(request):
    student = Student.objects.all()
    return render(request, 'listPage/student_list.html', {'st':student})
