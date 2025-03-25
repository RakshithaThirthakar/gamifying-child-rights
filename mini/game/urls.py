
from django.urls import path
from game import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('quizList/', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_view, name='quiz_view'),
    path('check_answer/', views.check_answer, name='check_answer'),
    path('hangman/', views.hangman_view, name='hangman_view'),
    path('story/', views.story, name='story'),
    path('tictactoe/', views.TTT, name='TicTacToe'),
    path('Saniastory/',views.sania, name='Sanstory'),
    path('Rihaanstory/',views.rihaan, name='Rihstory'),
    path('Videos/', views.videos, name='vids')
]
