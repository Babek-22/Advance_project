from core.models import Contact

from django import forms

class ContactForm (forms.ModelForm):

    class Meta:
        model = Contact
        fields='__all__'
        # fields = ('name','email','subject','message')
        # # widgets={
        #     message:forms.TextInput(attrs={'class':'form-control','placeholder:message'})
        #     name:forms.TextInput(attrs={'class':'form-control','placeholder:name'})
        #     email:forms.EmailInput(attrs={'class':'form-control','placeholder:email'})
        #     subject:forms.TextInput(attrs={'class':'form-control','placeholder:subject'})
        # }
    # def clean(self):
    #     cleaned_data=super(ContactForm,self).clean()
    #     name=cleaned_data.get('name')
    #     if name.title!=name:
    #         raise forms.ValidationError(
    #             'Birinci herf boyuk olmalidi'
    #         )