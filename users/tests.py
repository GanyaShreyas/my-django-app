from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserRegistrationForm, LoginForm, UserEditForm, ProfileEditForm
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.profile = Profile.objects.get(user=self.user)

    def test_profile_creation(self):
        """Test if profile is automatically created with user"""
        self.assertIsNotNone(self.profile)
        self.assertEqual(self.profile.user, self.user)

    def test_profile_str_method(self):
        """Test profile string representation"""
        self.assertEqual(str(self.profile), 'testuser')

class UserViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.profile = Profile.objects.get(user=self.user)

    def test_register_view(self):
        """Test user registration view"""
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpass123',
            'password2': 'newpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='newuser').exists())
        # Check if profile was automatically created for new user
        new_user = User.objects.get(username='newuser')
        self.assertTrue(Profile.objects.filter(user=new_user).exists())

    def test_login_view(self):
        """Test user login view"""
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login

    def test_logout_view(self):
        """Test user logout view"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect to login page
        self.assertEqual(response.url, reverse('login'))  # Verify redirect to login page

    def test_edit_view(self):
        """Test profile edit view"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('edit'))
        self.assertEqual(response.status_code, 200)

        # Test profile update
        test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',
            content_type='image/jpeg'
        )
        response = self.client.post(reverse('edit'), {
            'first_name': 'Updated',
            'last_name': 'User',
            'photo': test_image
        })
        self.assertEqual(response.status_code, 200)

    def test_index_view_requires_login(self):
        """Test that index view requires login"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

class UserFormsTest(TestCase):
    def test_user_registration_form(self):
        """Test user registration form validation"""
        form_data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'newpass123',
            'password2': 'newpass123'
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form(self):
        """Test login form validation"""
        form_data = {
            'username': 'testuser',
            'password': 'testpass123'
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_edit_form(self):
        """Test user edit form validation"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        profile = Profile.objects.get(user=user)
        form_data = {
            'first_name': 'Updated',
            'last_name': 'User',
            'email': 'updated@example.com'
        }
        form = UserEditForm(instance=user, data=form_data)
        self.assertTrue(form.is_valid())
