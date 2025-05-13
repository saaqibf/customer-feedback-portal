from django.db import models

class Feedback(models.Model):   # ✅ THIS CLASS MUST BE NAMED Feedback
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[('open', 'Open'), ('resolved', 'Resolved')],
        default='open'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.status}"
