from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.TeacherLoginView.as_view(),name='login'),
]