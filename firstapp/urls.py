from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('crud',views.crud,name="crud"),
    path('add',views.add,name="add"),
    path('addrec',views.addrec,name="addrec"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name='update'),  
    path('update/uprec/<int:id>',views.uprec,name="uprec"),

]

