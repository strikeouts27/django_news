Django For Beginners Reference Material:

Django has a built in model called User that has some fields already created.
User model: https://docs.djangoproject.com/en/4.2/ref/contrib/auth/#django.contrib.auth.models.User

The second approach, to create a custom user model, is recommended in the official Django
documentation158. We can extend AbstractUser159 to create a custom user model that behaves
identically to the default User model but provides the option for customization in the future.

This chapter will use AbstractUser to create a custom user model for a new Newspaper website
project. The choice of a newspaper app pays homage to Django’s roots as a web framework built
for editors and journalists at the Lawrence Journal-World.

The first step is to create a new Django project from the command line. We need to do our familiar
steps of creating and navigating to a new directory called news and installing and activating a new
virtual environment called .venv

# macOS

$ cd ~/desktop/code
$ mkdir news
$ cd news
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $

Next, install Django and Black, create a new Django project called django_project, and make a
new app called accounts.

(.venv) $ python -m pip install django~=4.2.0
(.venv) $ python -m pip install black
(.venv) $ django-admin startproject django_project .
(.venv) $ python manage.py startapp accounts

# Forms.py

---

How would Users be created in our program? When a user creates a new account and when an admin creates an account. We use UserCreationForm and UserChangeForm which are built in Django Forms for this purpose.

We can override the buit in fields and how they are configured by using the meta class and overwriting it with new instructions.

Also we can add on data to be shown using the plus symbol.

A list of the default fields is shown here: https://docs.djangoproject.com/en/4.2/ref/contrib/auth/#django.contrib.auth.models.User

The final step is to update our admin.py file since the admin is tightly coupled to the default
User model. We will extend the existing UserAdmin class to use our new CustomUser model.

To control which fields are listed, we use list_display170. But to actually edit new custom fields,
like age, we must add fieldsets171. And to include a new custom field in the section for creating a
new user we rely on add_fieldsets.

# tests.py

get_user_model()¶

At the top, we import get_user_model()176, so we can test our user registration. Then we also
import TestCase to run tests that touch the database and reverse so we can verify the URL and
view work properly.
# https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#django.contrib.auth.get_user_model

Our class of tests is called UsersManagersTests and extends TestCase. The first unit test, test\_-
create_user, checks that a regular user displays expected behavior.

The second unit test, test\_-create_superuser, does the same, albeit for a superuser account.


# news
# django_news
# django_news_app

# testing push# django_news
# django_news
# django_news
