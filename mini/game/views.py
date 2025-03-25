from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from .models import Quiz, Question, Answer
import json
from django.views.decorators.csrf import csrf_exempt
import random


def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'game/quiz_list.html', {'quizzes': quizzes})

def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    return render(request, 'game/quiz.html', {'quiz': quiz, 'questions': questions})


@csrf_exempt
def check_answer(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        option_selected = body.get('option')
        question_id = body.get('question_id')
        question = get_object_or_404(Question, id=question_id)
        correct_answer = question.answers.filter(is_correct=True).first()

        if option_selected == correct_answer.answer_text:
            response = {'result': 'Correct answer! Points increased.', 'correct': True, 'correct_answer': correct_answer.answer_text}
        else:
            response = {'result': 'Incorrect answer!', 'correct': False, 'correct_answer': correct_answer.answer_text}

        return JsonResponse(response)

    return JsonResponse({'result': 'Invalid request.'})

def home_view(request):
    return render(request, 'game/Home.html')

def about_view(request):
    return render(request, 'game/About.html')

def TTT(request):
    return render(request, 'game/TicTacToe.html')

def hangman_view(request):
    return render(request, 'game/hangman.html')

def story(request):
    return render(request, 'game/story.html')

def sania(request):
    return render(request, 'game/sania.html')

def rihaan(request):
    return render(request, 'game/rihaan.html')

def videos(request):
    return render(request, 'game/videos.html')

