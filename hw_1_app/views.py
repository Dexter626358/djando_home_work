import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Первая страница сайта")


def main(request):
    logger.info('Main page accessed')
    return HttpResponse("Добро пожаловать на мой персональный сайт")


def about(request):
    logger.info('About page accessed')
    return HttpResponse("Это страничка обо мне.\n Меня зовут Сергей,\n"
                        " я учусь на гикбрейнс на факультете разработки и хочу стать программистом")

# Create your views here.
