from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

# At the top, we import reverse177 to verify that the URL and view work properly

# Create your tests here.


class UsersManagersTests(TestCase):
    # get_user_model is used so we can test our user registration.

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass1234",
        )
        # on these next lines of code we are checking that what the user type in is equal to what we have in our database
        # for the respective field value.
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        # on these next lines of code we are testing if the use is
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="testpass234",
        )
        self.assertEqual(admin_user.username, "testsuperuser")
        self.assertEqual(admin_user.email, "testsuperuser@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


# if we want to test that our signup page is at the correct url.
class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    # this test will test the view, reverses the signup which is a url name, and than confirms aa 200 status code
    # and that our signup.html template is being used.

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    # the test sign up form checks our form by sending a post request to fill it out. after the form is submitted,
    # we confirm the expected 302 redirect and confirm that there  is now one user in the test database.

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@email.com")
