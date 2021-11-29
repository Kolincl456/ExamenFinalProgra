from django import forms
from .models import Carrera, Alumno


class CarreraForm(forms.ModelForm):

    class Meta:
        model = Carrera
        fields = ('nombre', 'edad', 'direccion')

    def __init__ (self, *args, **kwargs):
        super(CarreraForm, self).__init__(*args, **kwargs)
        self.fields["actores"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["actores"].help_text = "Ingrese los alumnos que va asignar"
        self.fields["actores"].queryset = Alumno.objects.all()