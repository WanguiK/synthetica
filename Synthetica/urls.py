from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('project/', views.ProjectDetailView.as_view(), name='project'),

    path('generation/<int:pk>', views.GenerateDetailView.as_view(), name='generate'),

    # path('newproject/', views.ProjectCreate.as_view(), name="new-project"),

    # path('generate/<int:pk>/', views.generate, name="generate"),

    # path('workspace/<int:pk>', views.GenerateUpdate.as_view(), name="workspace"),

    path('workspace/', views.ProjectGenerateCreate.as_view(), name="workspace"),

    # path('auth/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),

    # path('generate/', views.GenerateCreate.as_view(), name="generate"),
] 