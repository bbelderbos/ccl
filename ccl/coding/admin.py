from django.contrib import admin

from .models import Exercise, Submission


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "added"]
    search_fields = ["title", "description"]


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ["user", "exercise", "added"]
