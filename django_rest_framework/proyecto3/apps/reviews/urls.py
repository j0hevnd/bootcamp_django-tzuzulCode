from django.urls import path

from apps.reviews.views import ReviewUpdateApiView

app_name = 'reviews'
urlpatterns = [
    path('update-comment/<int:pk>/', ReviewUpdateApiView.as_view()),
]
