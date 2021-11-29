from django import forms
from .models import Carrera, Alumno

class CarreraForm(forms.ModelForm):

    class Meta:
        model = Carrera
        fields = ('nombre', 'descripcion', 'alumno', )

    def __init__ (self, *args, **kwargs):
        super(CarreraForm, self).__init__(*args, **kwargs)
        self.fields["alumno"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["alumno"].help_text = "Ingrese los alumnos que va asignar"
        self.fields["alumno"].queryset = Alumno.objects.all()