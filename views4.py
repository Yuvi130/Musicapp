# views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

@login_required
def my_protected_view(request):
    # View logic
    pass

class MyProtectedView(LoginRequiredMixin, View):
    # View logic
    pass
