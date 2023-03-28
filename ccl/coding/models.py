from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Exercise(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    start_code = models.TextField()
    solution_code = models.TextField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Submission(models.Model):
    """
    M2M table: user can do many exercises, exercises can be
    done by many users.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    code = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    passed = models.BooleanField(default=False)

    def __str__(self):
        status = "passed" if self.passed else "did not pass"
        return f"{self.user} {status} exercise {self.exercise}"
