from django.forms import ModelForm
from django import forms 
from fkip.models import Dosen, Staff, Mahasiswa

class FormDosen (ModelForm):
    class Meta:
        model = Dosen
        fields = '__all__'

        widgets = {
            'NIP' : forms.NumberInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'tanggal_lahir' : forms.TextInput({'class':'form-control'}),
            'photo' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'fakultas' : forms.TextInput({'class':'form-control'}),
            'prodi' : forms.TextInput({'class':'form-control'}),
            'alamat' : forms.TextInput({'class':'form-control'}),
        }
class FormStaff (ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

        widgets = {
            'NIP' : forms.NumberInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'tanggal_lahir' : forms.TextInput({'class':'form-control'}),
            'photo' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'unit' : forms.TextInput({'class':'form-control'}),
            'alamat' : forms.TextInput({'class':'form-control'}),
        }
class FormMahasiswa (ModelForm):
    class Meta:
        model = Mahasiswa
        fields = '__all__'

        widgets = {
            'NIM' : forms.NumberInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'tanggal_lahir' : forms.TextInput({'class':'form-control'}),
            'photo' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'fakultas' : forms.TextInput({'class':'form-control'}),
            'prodi' : forms.TextInput({'class':'form-control'}),
        }