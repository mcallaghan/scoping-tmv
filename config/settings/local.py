from .base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)

SECRET_KEY = env('SECRET_KEY',default='%3ijor=4_je6ry!%u*-m&rh5q8oj6tzy!-nn$3f37_tu@*^smm')
#SECRET_KEY = '$3ijor=4_je6ry!%u*-m&rh5q8oj6tzy!-nn$3f37_tu@*^smm'
