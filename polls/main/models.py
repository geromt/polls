from django.db import models
import uuid


class Poll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=255, verbose_name="Poll Question")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Poll Publication Date")

    class Meta:
        db_table = "poll"
        verbose_name = "Poll"
        verbose_name_plural = "Polls"

    def __str__(self):
        return self.question


class Choice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=255, verbose_name="Choice Text")
    votes = models.IntegerField(default=0, verbose_name="Votes")

    class Meta:
        db_table = "choice"
        verbose_name = "Choice"
        verbose_name_plural = "Choices"

    def __str__(self):
        return self.choice_text