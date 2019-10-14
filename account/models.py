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
    phone = models.CharField(max_length=13)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

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


class Privileged(models.Model):
    # module = models.ForeignKey(Modulename, on_delete=models.CASCADE)
    # moduleurl = models.ForeignKey(Modulurl, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # userrole = models.ForeignKey(Userrole, on_delete=models.CASCADE)
    # menuname = models.ForeignKey(Menuname, on_delete=models.CASCADE)
    # type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, blank=True)
    # sidemenu = models.ForeignKey(Sidemenu, on_delete=models.CASCADE)
    delete = models.IntegerField(null=True, blank=True)
    created_by_id = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(null=True, blank=True)
    modified_by_id = models.CharField(max_length=20, blank=True, null=True)
    modified_by = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'Privileged'
