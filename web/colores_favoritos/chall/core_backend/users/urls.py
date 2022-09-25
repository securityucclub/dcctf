from django.urls import path
from .views import MakeQuery

urlpatterns = [
    path('query/', MakeQuery.as_view()),
]
