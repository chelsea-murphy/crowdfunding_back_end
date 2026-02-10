from django.urls import path
from . import views
from .views import RegisterView, CurrentUserView

urlpatterns = [
    path('fundraisers/', views.FundraiserList.as_view()),
    path('fundraisers/<int:pk>/', views.FundraiserDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledges/<int:pk>/', views.PledgeDetail.as_view()),
    path('', views.FundraiserList.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/me/', CurrentUserView.as_view(), name='current-user'),
]