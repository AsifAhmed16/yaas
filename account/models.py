from django.db import models


class Userrole(models.Model):
    role_name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = 'Userrole'


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=250, unique=True)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    designation_name = models.CharField(max_length=100)
    is_active = models.CharField(max_length=1, default=0)
    activation_code = models.CharField(max_length=10)
    user_role = models.ForeignKey('Userrole', on_delete=models.CASCADE, blank=True, null=True)
    # projectrole = models.ForeignKey(Projectroles, on_delete=models.CASCADE, blank=True, null=True)
    project = models.CharField(max_length=1000, blank=True, null=True)
    project_role = models.CharField(max_length=1000, blank=True, null=True)
    created_by_id = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(null=True, blank=True)
    modified_by_id = models.CharField(max_length=20, blank=True, null=True)
    modified_by = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.first_name, self.username)

    def login_json(self):
        return dict(
            id=str(self.id),
            email=str(self.email),
            username=str(self.username),
            first_name=str(self.first_name),
            is_active=str(self.is_active),
        )

    class Meta:
        db_table = 'User'
