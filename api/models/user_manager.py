from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        if username is None:
            raise TypeError('Users should have a username')

        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
