from django import forms
from .models import Profissional
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfissionalRegistrationForm(UserCreationForm):
    nome = forms.CharField(max_length=50)
    area = forms.ChoiceField(choices=Profissional.AREA_CHOICES)
    preco = forms.DecimalField(max_digits=10, decimal_places=2)
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    nacionalidade = forms.CharField(max_length=50, initial='Brasileiro (a)')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nome', 'area', 'preco', 'data_nascimento', 'nacionalidade']

    def save(self, commit=True):
        user = super(ProfissionalRegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['nome']
        if commit:
            user.save()
            profissional = Profissional.objects.create(
                user=user,
                nome=self.cleaned_data['nome'],
                area=self.cleaned_data['area'],
                preco=self.cleaned_data['preco'],
                data_nascimento=self.cleaned_data['data_nascimento'],
                nacionalidade=self.cleaned_data['nacionalidade']
            )
            profissional.save()
        return user