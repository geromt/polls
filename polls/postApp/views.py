from django.http import JsonResponse
from rest_framework import generics, viewsets

from .serializer import ChoiceSerializer, PollSerializerWithChoices
from main.models import Poll, Choice


class PollsAPICreate(generics.CreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializerWithChoices

    def perform_create(self, serializer):
        choices = self.request.data.pop('choices', [])
        poll = serializer.save()
        for ch in choices:
            Choice.objects.create(poll=poll, **ch)


class PollsAPIRetrieve(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializerWithChoices


class ChoiceAPISet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


def vote(request, choice_uuid):
    try:
        choice = Choice.objects.get(id=choice_uuid)
        choice.votes += 1
        choice.save()
        return JsonResponse({'status': 'success',
                             'votes': choice.votes,
                             'choice_id': choice_uuid,
                             'choice_text': choice.choice_text})
    except Choice.DoesNotExist:
        return JsonResponse({'status': 'error',
                             'message': 'Choice not found'},
                            status=404)

