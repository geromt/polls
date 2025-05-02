from django.contrib import admin

from .models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date')
    search_fields = ('question',)
    list_filter = ('pub_date',)
    ordering = ('-pub_date',)
    date_hierarchy = 'pub_date'
    inlines = (ChoiceInline,)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    fields = ('poll', 'choice_text', 'votes')
    list_display = ('poll', 'choice_text', 'votes')
    search_fields = ('choice_text',)
    list_filter = ('poll',)
    ordering = ('-votes',)
