from django.urls import path
from soccer.views import HomePageView, DetailPageView

app_name = 'soccer'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<str:team_name>/', DetailPageView.as_view(), name='detail'),
    # path('/new/', NewWikiView.as_view(), name='new-wiki'),

]
