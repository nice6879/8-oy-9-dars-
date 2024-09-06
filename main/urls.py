from django.urls import path
from django.contrib.auth import views as auth_views
from .  import views

urlpatterns = [
    path('', views.quizList, name='quizList'),
    
    path('quiz-detail/<slug:slug>/', views.quizDetail, name='quizDetail'),
    path('quiz/<slug:slug>/', views.take_quiz, name='take-quiz'),
    path('quiz-results/<slug:slug>/', views.quiz_results, name='quiz-results'),
    
    
    path('questionDelete/<int:id>/<int:pk>/', views.questionDelete, name='questionDelete'),
    path('optionDelete/<int:ques>/<int:option>/', views.deleteOption, name='optionDelete'),
    path('question-detail/<int:id>/', views.questionDetail, name='questionDetail'),
    
    path('create-quiz/', views.createQuiz, name='createQuiz'),
    path('create-question/<int:id>/', views.questionCreate, name='questionCreate'),
    
    path('detail/', views.detail, name='detail'),
    path('results-detail/<slug:slug>/', views.results_detail, name='results-detail'),
    path('participant-results/<slug:slug>/', views.participant_results, name='participant-results'),
    path('participant-detail/<slug:slug>/<int:user_id>/', views.participant_detail, name='participant_detail'),
    
    path('quiz/<slug:slug>/export/excel/', views.export_results_to_excel, name='export-results-excel'),
    path('quiz/<slug:slug>/export/word/', views.export_results_to_word, name='export-results-word'),
    
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('force-404/', views.error_handler, name='force_404'),
    path('force-500/', views.error_handler, name='force_500'),
]

handler404 = 'main.views.error_handler'
handler500 = 'main.views.error_handler'

