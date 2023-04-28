from django import forms
from .models import UserProfile
from .models import ContactUs




class ContactUsForms(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        label='نام و نام خانوادگی :',
        error_messages={
            'required':'پر کردن این فیلد الزامی است',
            'max_length': 'تعداد کاراکتر ها بیش از حد مجاز است'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خوانوادگی'
        })

    )
    #------------------------------
    email = forms.EmailField(
        label= 'ایمیل :',
        max_length=100,
        error_messages={
            'required': 'پر کردن این فیلد الزامی است',
            'max_length': 'تعداد کاراکتر ها بیش از حد مجاز است'
        },
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
        })
    )
    # ------------------------------
    subject = forms.CharField(
        max_length=50,
        label='موضوع :',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'موضوع'
        }),
        error_messages={
            'required': 'پر کردن این فیلد الزامی است',
            'max_length': 'تعداد کاراکتر ها بیش از حد مجاز است'
        },
    )
    # ------------------------------
    text = forms.CharField(
        label='متن پیام :',
        error_messages={
            'required': 'پر کردن این فیلد الزامی است'
        },
        widget=forms.Textarea(attrs={
            'placeholder': 'متن پیام',
            'class': 'form-control',
            'rows': 8,
            'id': 'message'
        })
    )

#---------------------------------------------------------------------------
class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'title', 'mail', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'mail': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'row': 8,
                'id': 'message'
            })
        }
        labels = {
            'name': 'نام و نام خانوادگی:',
            'title': 'موضوع پیام:',
            'message': 'متن پیام:',
            'mail': 'ایمیل:'
        }
        error_messages = {
            'name': {
                'required': 'نام و نام خانوادگی اجباری است',
                'max_length': 'تعداد کاراکتر ها بیش از حد مجاز است'
            }
        }

#---------------------------------------------------------------------------
class ProfileForm(forms.Form):
    user_image = forms.ImageField(label='تصویر')

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

