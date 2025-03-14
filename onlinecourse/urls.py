"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from my_app import views

app_name = 'onlinecourse'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onlinecourse/', include('onlinecourse.urls')),

     path(route='', view=views.CourseListView.as_view(), name='index'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    # ex: /onlinecourse/5/
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    # ex: /enroll/5/
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # <HINT> Create a route for submit view
    path('<int:course_id>/submit/', views.submit, name='submit'),
    # <HINT> Create a route for show_exam_result view
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)