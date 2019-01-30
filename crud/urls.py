"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from employees import views,urls


urlpatterns = [
    path('admin/', admin.site.urls),

    # this is test url
    path('check/', views.Check.as_view(), name='check'),

    # main page
    path('', views.Main.as_view(), name='main'),

    # Employee Details
    path('employee/<int:pk>/employee_detail', views.employee_detail, name='employee_detail'),

    # edit Employees
    path('employee/<int:pk>/edit', views.employee_edit, name='employee_edit'),

    # Logout
    path('logout', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    
    # Login or Employee Login
    path('employee/login', views.login, name="login"),

    # Crete User or create Employee
    path('employee/cu', views.createUser, name='cr'),

    # Home page
    path('home/<int:pk>', views.index, name='home'),

    # student Details
    path('student/<int:pk>/student_detail', views.student_detail, name='student_detail'),

    # edit Student details
    path('student/<int:pk>/edit', views.student_edit, name='student_edit'),

    # create Student
    path('student/cs', views.createStudent, name='cs'),

    # list of Students
    path('student/list', views.studenList, name='sl'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
