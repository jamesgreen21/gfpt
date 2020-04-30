from django.db import models


class Testimonials(models.Model):
    TRAINING_OPTIONS = [
        ('Lose Weight', 'Lose Weight'),
        ('Get Lean', 'Get Lean'),
        ('Improve Performance', 'Improve Performance'),
        ('Muscle Gains', 'Muscle Gains'),
    ]

    title = models.CharField(max_length=50)
    goal = models.CharField(max_length=50, choices=TRAINING_OPTIONS)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    image = models.ImageField(upload_to='main_img')

    def __str__(self):
        return self.title
    