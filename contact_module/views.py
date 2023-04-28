
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import ContactUsModelForm
from .models import UserProfile
from .forms import ProfileModelForm

class ContactUsView(CreateView):
    template_name = 'contact_us.html'
    form_class = ContactUsModelForm
    success_url = '/'

class CreateProfileView(CreateView):
    template_name = 'profile/profile.html'
    form_class = ProfileModelForm
    success_url = '/contact-us/profile'

#-------------------------------
# to show uploaded images :
class ProfilesListView(ListView):
    model = UserProfile
    template_name = 'profile/profile_images_list.html'
    context_object_name = 'profiles'

