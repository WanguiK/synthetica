from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project'),

    path('metadata/<int:pk>', views.GenerateDetailView.as_view(), name='metadata'),

    path('generate/<int:pk>', views.generate, name="generate"),

    path('workspace/', views.ProjectGenerateCreate.as_view(), name="workspace"),
] 