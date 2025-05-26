from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import CustomUserCreationForm
from users.models import CustomUser


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис!'
        message = 'Спасибо, что зарегистрировались в нашем сервисе'
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email, ]
        send_mail(subject, message, from_email, recipient_list)


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('catalog:home')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('catalog:home')


class UserDetailVew(DetailView):
    model = CustomUser
    template_name = 'users/user_detail.html'
    context_object_name = 'user'


class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/user_edit.html'

    def get_success_url(self):
        return reverse('users:user_detail', kwargs={'pk': self.object.pk})
