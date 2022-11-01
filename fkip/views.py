from django.shortcuts import render
from . models import Dosen, Mahasiswa, Staff
from fkip.forms import FormDosen, FormStaff, FormMahasiswa

# Create your views here.
def prodi6(request):
    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fkip/index.html', konteks)

def tambah_staff (request):
    if request.POST:
        form = FormStaff(request.POST)
        if form.is_valid():
            form.save()
            form = FormStaff()
            pesan = "Data Tersimpan"
            konteks = {
                'form':form,
                'pesan':pesan,
            }
            return render(request, 'tambah-staff.html', konteks)
    else:
        form = FormStaff()

        konteks = {
            'form':form,
        }

        return render(request, 'tambah-staff.html', konteks)

def tambah_dosen (request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data Tersimpan"
            konteks = {
                'form':form,
                'pesan':pesan,
            }
            return render(request, 'tambah-dosen.html', konteks)
    else:
        form = FormDosen()

        konteks = {
            'form':form,
        }

        return render(request, 'tambah-dosen.html', konteks)

def tambah_mahasiswa (request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormMahasiswa()
            pesan = "Data Tersimpan"
            konteks = {
                'form':form,
                'pesan':pesan,
            }
            return render(request, 'tambah-mahasiswa.html', konteks)
    else:
        form = FormMahasiswa()

        konteks = {
            'form':form,
        }

        return render(request, 'tambah-mahasiswa.html', konteks)

