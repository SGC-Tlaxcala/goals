#-*- coding: utf-8 -*-
#       app: cmi.distribucion
#      desc: Generación de formularios para el indicador "Productividad"

# Modelos
from core.models import PUESTOS, SITIO, Pipol
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from .models import MetasSPE, Evidencia

# Formularios y Widgets
from django import forms
from django.forms.extras import widgets
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput
from django.utils.safestring import mark_safe
from django.forms.widgets import RadioFieldRenderer

from django.contrib.auth import get_user_model
User = get_user_model()

from django.utils.safestring import mark_safe

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class PipolForm(forms.Form):
    class Meta:
        model = Pipol
    # Para crear el usuario
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'username o login'
            },
        ),
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nombre del Usuario'
            },
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Apellidos'
            },
        ),
    )
    email = forms.EmailField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Correo Electrónico'
            },
        ),
    )
    password1=forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'contraseña'
            },
        )
    ) #render_value=False
    password2=forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'repetir contraseña'
            },
        ))

    # Para crear el perfil
    sitio = forms.ChoiceField(
        widget=widgets.Select(
            attrs={'class':'form-control'}
        ),
        choices=SITIO)
    is_active = forms.BooleanField(initial=True, required=False)
    puesto = forms.ChoiceField(
        widget=widgets.Select(
            attrs={'class':'form-control'}
        ),
        choices=PUESTOS
    )

    def __init__ (self, *args, **kwargs):
        edit = kwargs.pop('edit', None)
        initial = kwargs.pop('kwargs', None)
        super (PipolForm, self).__init__(*args, **kwargs)
        if edit:
            del self.fields['password1']
            del self.fields['password2']

    def clean_username(self): # check if username dos not exist before
        try:
            User.objects.get(username=self.cleaned_data['username']) #get user from user model
        except User.DoesNotExist :
            return self.cleaned_data['username']
        raise forms.ValidationError("El usuarios ya existe")

    def clean(self): # check if password 1 and password2 match each other
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:#check if both pass first validation
            if self.cleaned_data['password1'] != self.cleaned_data['password2']: # check if they match each other
                raise forms.ValidationError("Las contraseñas no coinciden")
        return self.cleaned_data

    def save(self): # create new user
        new_user=User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name  = self.cleaned_data['last_name']
        new_user.is_active  = self.cleaned_data['is_active']
        new_user.sitio      = self.cleaned_data['sitio']
        new_user.puesto     = self.cleaned_data['puesto']
        new_user.save()
        return new_user


from django.contrib.auth.forms import UserChangeForm
class PipolFormEdit(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
    # Para crear el usuario
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'username o login'
            },
        ),
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nombre del Usuario'
            },
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Apellidos'
            },
        ),
    )
    email = forms.EmailField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Correo Electrónico'
            },
        ),
    )
    password1=forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'contraseña'
            },
        )
    ) #render_value=False
    password2=forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'repetir contraseña'
            },
        ))

    # Para crear el perfil
    sitio = forms.ChoiceField(
        widget=widgets.Select(
            attrs={'class':'form-control'}
        ),
        choices=SITIO)
    is_active = forms.BooleanField(initial=True, required=False)
    puesto = forms.ChoiceField(
        widget=widgets.Select(
            attrs={'class':'form-control'}
        ),
        choices=PUESTOS
    )

    def __init__(self, *args, **kwargs):
        super(PipolFormEdit, self).__init__(*args, **kwargs)
        self.fields.pop('password1')
        self.fields.pop('password2')
        self.fields.pop('last_login')
        self.fields.pop('date_joined')


# ### Control de Metas del SPE ### #

class FormularioMetas(forms.ModelForm):
    class Meta:
        model = MetasSPE
    # Configuración de campos
    puesto = forms.ChoiceField(
        widget=widgets.Select(
            attrs={'class':'form-control'}
        ),
        choices=PUESTOS
    )
    clave = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Clave de la Meta'
            },
        ),
    )
    nom_corto = forms.CharField(
        max_length=100,
        label = 'Identificación',
        help_text = 'Escribe un nombre descriptivo corto para la meta',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Nombre corto para la meta'
            },
        ),
    )
    year = forms.CharField(
        max_length=20,
        label = 'Año',
        help_text = 'Año en el que aplica la meta',
        initial = 2015,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'type': 'number',
                'placeholder':'2015'
            },
        ),
    )
    ciclos = forms.CharField(
        max_length=20,
        label = 'Repeticiones',
        help_text = ' Número de veces que se repite la meta, no se refiere al <strong>nivel esperado</strong>',
        widget=forms.TextInput(
            attrs={
                'type': 'number',
                'class':'form-control',
            },
        ),
    )
    descripcion  = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':4,'label':'Contenido',}
            )
        )
    ejemplo = forms.FileField(
        max_length=20,
        required = False,
        label = 'Ejemplo',
        help_text = 'Puedes subir un ejemplo de las evidencias para homogenizarlas',
        widget=forms.FileInput(
            attrs={
                'type': 'file'
            },
        ),
    )
    eval = forms.BooleanField(initial=True, required=False)


class FormEvidenciaBase(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        m = kwargs.pop('qmeta', None)
        # p = kwargs.pop('qpipol', None)
        super(FormEvidenciaBase, self).__init__(*args, **kwargs)
        self.fields['meta'].queryset = MetasSPE.objects.filter(pk=m.id)
        self.fields['meta'].widget.attrs['class'] = 'form-control'
        self.fields['miembro'].queryset = Pipol.objects.filter(puesto=m.puesto)
        self.fields['miembro'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Evidencia
    fecha = forms.DateField (
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.TextInput(
            attrs={'class': 'form-control',}
        )
    )
    eval = forms.BooleanField(initial=True, required=False)
