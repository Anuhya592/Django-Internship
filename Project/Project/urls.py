"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('ht/',views.html),
    path('user/<str:uname>/',views.username),
    path('userage/<str:un>/<int:age>/',views.usernameage),
    path('emp/<str:empid>/<int:eage>/<str:ename>/',views.employeedetails),
    path('qw/',views.htm),
    path('yt/<str:name>/',views.ytname),
    path('pt/<int:id>/<str:ename>/',views.empname),
    path('stud/',views.student),
    path('internalJS/',views.internaljs),
    path('myform/',views.myform,name='myform'),#name --to make interface b/w templates and urls
    path('signup/',views.signup,name='signup'),
    path('btstrp/',views.bootstrapfun),
    path('btrg/',views.btregi,name="btr"),
    path('register/',views.register),
    path('register1/',views.register1),
    path('showdetails/',views.showdetails,name='showdetails'),
    path('view/<int:id>/',views.viewinfo,name='viewinfo'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
