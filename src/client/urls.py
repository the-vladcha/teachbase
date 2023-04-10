from django.urls import path
from client.endpoint import views

urlpatterns = [
    path('teachbase/courses/', views.CoursesListApiView.as_view()),
    path('teachbase/courses/<int:course_id>/', views.CourseApiView.as_view()),
    path('teachbase/users/create/', views.UserApiView.as_view()),
    path('teachbase/course_sessions/<int:session_id>/register/', views.CourseSessionApiView.as_view()),
    path('teachbase/courses/<int:course_id>/course_sessions/', views.CourseSessionsListApiView.as_view()),

    path('courses/', views.CourseView.as_view({'get': 'list'})),
    path('courses/<int:pk>/', views.CourseView.as_view({'get': 'retrieve'})),
]
