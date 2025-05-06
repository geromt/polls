from rest_framework import serializers
from main.models import Poll, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes']
        name = 'choices'


class PollSerializerWithChoices(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Poll
        fields = '__all__'
