from django.shortcuts import get_object_or_404, render

from .models import Exercise


def exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)

    context = {
        "exercise": exercise,
    }
    return render(request, "coding/index.html", context)
