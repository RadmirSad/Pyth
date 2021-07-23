from django.conf.urls import url
from WebApp import views


urlpatterns = [
    url(r'^teacher$', views.teach_api),
    url(r'^teacher/([0-9]+)$', views.teach_api),

    url(r'^web$', views.web_api),
    url(r'^web/([0-9]+)$', views.web_api),

    url(r'^course$', views.course_api),
    url(r'^course/([0-9]+)$', views.course_api),

    url(r'^cost$', views.cost_api),
    url(r'^cost/([0-9]+)$', views.cost_api),

    url(r'^salary$', views.get_salary_api)
]
