from django.shortcuts import render
from django.http import HttpResponse


def show_name(request):
    return HttpResponse('Hello, Cosmin!')


def students(request):
    context = {
        'all_students': [
            {
                'first_name': 'Mircea',
                'last_name': 'Popescu',
                'is_olympic': True
            },
            {
                'first_name': 'Alina',
                'last_name': 'Popescu',
                'is_olympic': False
            }
        ]
    }

    return render(request, 'intro/all_students.html', context)


def all_awesome_movies(request):
    movies = {
        'all_movies': [
            {
                'name': 'Lord of the rings',
                'release_date': '2001',
                'director': 'John Snow'
            },
            {
                'name': 'The hobbit',
                'release_date': '2015',
                'director': 'Ed Stark'
            },
            {
                'name': 'Alien',
                'release_date': '1990',
                'director': 'Tyrion Lannister'
            }
        ]
    }

    return render(request, 'intro/all_movies.html', movies)
