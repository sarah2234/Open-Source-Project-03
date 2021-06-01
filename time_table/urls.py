from django.urls import path
from django.contrib import admin

from . import views

app_name = 'time_table'

urlpatterns = [
    path('load/', views.load, name='load'),
    # 학번, 비번 입력받고 블랙보드 공지사항 읽어오는 곳. 간단하게 확인가능
    path('crawling/', views.crawling, name='crawling'),
    path('', views.schedule, name='schedule'),
    path('<int:data_id>/delete', views.delete_assignment, name='delete_assignment'),
    path('assignment_schedule/<int:assignment_id>', views.assignment_schedule, name='assignment_schedule'),
    path('assignment_schedule/<int:assignment_id>/available_time', views.available_time, name='available_time'),
    path('add_schedule', views.add_schedule, name='add_schedule'),
    path('add_schedule/add', views.add_function, name='add_function'),
    path('edit_schedule/<int:data_id>', views.edit_schedule, name='edit_schedule'),
    path('edit_schedule/<int:data_id>/delete', views.delete_function, name='delete_function'),
    path('edit_schedule/<int:data_id>/edit', views.edit_function, name='edit_function'),
    path('setting', views.setting, name='setting'),
    path('setting/timetable/load', views.load_timetable, name='load_timetable'),
    path('setting/timetable/choose', views.choose_timetable, name='choose_timetable'),
    path('cieat_interest', views.cieat_interest, name='cieat_interest'),
    path('cieat_interest/load', views.load_interest, name='load_interest'),
    path('cieat_interest/submit', views.cieat_submit, name='cieat_submit'),
    path('admin/', admin.site.urls),
]