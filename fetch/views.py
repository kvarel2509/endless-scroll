from django.views import generic
from rest_framework import generics
from .models import Word
from .serializers import WordSerializer


class BaseView(generic.TemplateView):
	template_name = 'fetch/base.html'


class WordApiView(generics.ListCreateAPIView):
	queryset = Word.objects.all()
	serializer_class = WordSerializer
