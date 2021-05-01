from xml.dom.minidom import Document

from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic.base import View

from .forms import ProfileForm, PreferenceForm
from .models import Profile, Preference


class UserAccount(View):
    template_name = 'account/user_account.html'
    form = ProfileForm()
    formPreference = PreferenceForm()

    def get(self, request):
        profile = Profile.objects.filter(user=request.user).first()
        preference = Preference.objects.filter(user=request.user).first()
        if profile is None:
            average = 0
            return render(request, self.template_name, {"średnia": average})
        else:
            table_profile = [(field.name, getattr(profile, field.name)) for field in profile._meta.fields]
            table_preference = [(field.name, getattr(preference, field.name)) for field in preference._meta.fields]

            sum_fields = (len(table_profile) + len(table_preference) - 4)
            filled_in_fields = 0
            for field, value in (table_profile + table_preference):
                filled_in_fields += 1 if value != '' and field != 'id' and field != 'user' else 0

            average = round((filled_in_fields / sum_fields) * 100)
            return render(request, self.template_name, {"średnia": average, "fullname": profile.full_name(),
                                                        "date_of_birth": profile.date_of_birth_user(),
                                                        "contact_colors_star": profile.contact_fields_filled(),
                                                        'address_fields_filled': profile.address_fields_filled(),
                                                        'language_fields_filled': profile.language_fields_filled(),
                                                        'preference_fields_filled': preference.preference_fields_filled(),
                                                        'form': self.form,
                                                        'formPreference': self.formPreference})

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def post(self, request):
        "Profile."
        form = ProfileForm(request.POST or None, request.FILES, instance=self.get_object(), )
        if (request.POST.get('type') == 'basic_info'):
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
            else:
                print(form.errors)
        else:
            print('none basic info')
        #     Do zrobienia drugi formularz
        return redirect('./my_account')



def user_settings(request):
    return render(request, 'user_settings.html')
