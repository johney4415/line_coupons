from django.db import models

# Create your models here.

class User(models.Model):
    class Meta:
        db_table = 'user'

    line_user_id = models.TextField(default='0')
    display_name = models.TextField()
    picture_url = models.TextField()
    status_message = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_login_time = models.DateTimeField()