from django.db import models


class Role(models.Model):
    role = models.CharField(max_length=300)

    def __str__(self):
        return self.role

    class Meta:
        db_table = 'Role'


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=250, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username

    def login_json(self):
        return dict(
            id=str(self.id),
            email=str(self.email),
            username=str(self.username),
        )

    class Meta:
        db_table = 'User'
