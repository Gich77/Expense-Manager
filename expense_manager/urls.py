from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from expenses import views  # Assuming your app is named 'expenses'

urlpatterns = [

    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('expenses/', views.expense_list, name='expense_list'),
    
    path('', views.home, name='home'),  # Default home route
    path('expenses/add/', views.create_expense, name='create_expense'),
    path('expenses/<int:expense_id>/edit/', views.update_expense, name='update_expense'),
    path('expenses/<int:expense_id>/delete/', views.delete_expense, name='delete_expense'),

]
