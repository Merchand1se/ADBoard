from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, TemplateView
from content.models import User



class ConfirmUser(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'invalid_code.html')
        return redirect('account_login')


class MyAccount(LoginRequiredMixin, TemplateView):
    template_name = 'ProfileUser.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
#        context['is_author'] = self.request.user.groups.filter(name='authors').exists()
#        return context

