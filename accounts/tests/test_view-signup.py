from django.test import TestCase
from django.urls import resolve
from django.core.urlresolvers import reverse
from ..views import signup
from django.contrib.auth.models import User
from ..forms import SignUpForm

class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = resolve('signup')    #得到url
        response = self.client.get(url) # 用get方式访问
        self.assertEquals(response.status_code,200) #访问后的结果的状态码是不是200,想要的的

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func,signup)
