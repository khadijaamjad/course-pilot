from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'coursePilot'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=views.CourseListView.as_view(), name='index'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    # ex: /coursePilot/5/
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    # ex: /enroll/5/
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # submit view
    path('<int:course_id>/submit/', views.submit, name="submit"),
    # show_test_result view
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_test_result, name="test_result"),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
