Custom Users
============

Referring to a (Potentially) Custom User
----------------------------------------

### Background ###
If you reference `User` directly (e.g., as a foreign key ref), your code will 
not work if `AUTH_USER_MODEL` has been changed to a different user model.

### Solution ###
Django provides a couple of ways to get to the custom user model:

#### Code that's Executed at Import Time ####
For example, foreign key definitions, connecting to signals sent by the User 
model.

Use `settings.AUTH_USER_MODEL` (in `django.conf`).

Example 1: `blog/models.py`
```python
from django.conf import settings


class Article(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
```

Example 2: `blog/signals.py`
```python
from django.conf import settings


def post_save_receiver(sender, instance, created, **kwargs):
    # do something


post_save.connect(post_save_receiver,
                  sender=settings.AUTH_USER_MODEL)
```

#### Other Code ####

Use `get_user_model()` (in `django.contrib.auth`)

Example: `accounts/tests/test_models.py`
```python
from django.contrib.auth import get_user_model


User = get_user_model()


class UserModelTest(TestCase):

    def test_user_is_valid_with_email_only(self):
        user = User(email='a@b.com')
        user.full_clean()  # should not raise
```

