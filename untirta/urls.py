"""untirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from faperta.views import prodi1
from feb.views import prodi2
from fh.views import prodi3
from fisip.views import prodi4
from fk.views import prodi5
from fkip.views import *
from ft.views import prodi7
from pascasarjana.views import prodi8

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faperta/', prodi1),
    path('feb/', prodi2),
    path('fh/', prodi3),
    path('fisip/', prodi4),
    path('fk/', prodi5),
    path('fkip/', prodi6, name='fkip'),
    path('ft/', prodi7),
    path('pascasarjana/', prodi8),
    path('tambah-dosen/', tambah_dosen, name='tambah_dosen'),
    path('tambah-staff/', tambah_staff, name='tambah_staff'),
    path('tambah-mahasiswa/', tambah_mahasiswa, name='tambah_mahasiswa'),
    path ('dosen/ubah/<int:id_buku>', ubah_dosen, name='ubah_dosen'),
    path ('mahasiswa/ubah/<int:id_mahasiswa>', ubah_mahasiswa, name='ubah_mahasiswa'),
    path ('staff/ubah/<int:id_staff>', ubah_staff, name='ubah_staff'),
    path ('dosen/hapus/<int:id_dosen>', hapus_dosen, name='hapus_dosen'),
    path ('mahasiswa/hapus/<int:id_mahasiswa>', hapus_mahasiswa, name='hapus_mahasiswa'),
    path ('staff/hapus/<int:id_staff>', hapus_staff, name='hapus_staff'),

]
