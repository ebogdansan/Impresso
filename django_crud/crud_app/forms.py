from django import forms
from .models import Membru, Trupa, MembruTrupa

class MembruForm(forms.ModelForm):
    class Meta:  #se foloseste pt a afisa formularul in functie de modelul creat, este un template
        model = Membru
        fields = ['nume', 'prenume', 'cnp', 'adresa']
        widgets = {
            'nume': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Numele de familie'
            }),
            'prenume': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prenumele'
            }),
            'cnp': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CNP (13 cifre)',
                'maxlength': '13'
            }),
            'adresa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adresa completă'
            }),
        }
        labels = {
            'nume': 'Nume',
            'prenume': 'Prenume',
            'cnp': 'CNP',
            'adresa': 'Adresa',
        }

    def clean_cnp(self):
        cnp = self.cleaned_data['cnp']
        if len(cnp) != 13:
            raise forms.ValidationError('CNP-ul trebuie să aibă exact 13 cifre.')
        if not cnp.isdigit():
            raise forms.ValidationError('CNP-ul trebuie să conțină doar cifre.')
        return cnp

class TrupaForm(forms.ModelForm):
    class Meta:
        model = Trupa
        fields = ['numetrupa', 'genmuzical', 'aninfiintare', 'tara']
        widgets = {
            'numetrupa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Numele trupei'
            }),
            'genmuzical': forms.Select(attrs={
                'class': 'form-control'
            }, choices=[
                ('', 'Selectează genul muzical'),
                ('Rock', 'Rock'),
                ('Pop', 'Pop'),
                ('Jazz', 'Jazz'),
                ('Folk', 'Folk'),
                ('Electronic', 'Electronic'),
                ('Classical', 'Classical'),
                ('Hip-Hop', 'Hip-Hop'),
                ('Alternative', 'Alternative'),
                ('Metal', 'Metal'),
                ('Country', 'Country'),
                ('Blues', 'Blues'),
                ('Reggae', 'Reggae'),
                ('R&B','R&B'),
                ('Altul', 'Altul'),
            ]),
            'aninfiintare': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anul înființării (ex: 2020)',
                'min': '1950',
                'max': '2025'
            }),
            'tara': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Țara de origine'
            }),
        }
        labels = {
            'numetrupa': 'Nume Trupă',
            'genmuzical': 'Gen Muzical',
            'aninfiintare': 'An Înființare',
            'tara': 'Țara',
        }

    def clean_aninfiintare(self):
        an = self.cleaned_data['aninfiintare']
        if an and (len(an) != 4 or not an.isdigit()):
            raise forms.ValidationError('Anul trebuie să fie în format YYYY (ex: 2020).')
        return an

class MembruTrupaForm(forms.ModelForm):
    class Meta:
        model = MembruTrupa
        fields = ['membru', 'trupa', 'rol', 'datainscriere', 'activitate']
        widgets = {
            'membru': forms.Select(attrs={
                'class': 'form-control'
            }),
            'trupa': forms.Select(attrs={
                'class': 'form-control'
            }),
            'rol': forms.Select(attrs={
                'class': 'form-control'
            }, choices=[
                ('', 'Selectează rolul'),
                ('Acordeonist','Acordeonist'),
                ('Vocalist', 'Vocalist'),
                ('Chitarist', 'Chitarist'),
                ('Basist', 'Basist'),
                ('Baterist', 'Baterist'),
                ('Banjo','Banjo'),
                ('Pianist', 'Pianist'),
                ('Saxofonist', 'Saxofonist'),
                ('Violonist', 'Violonist'),
                ('DJ', 'DJ'),
                ('Manager', 'Manager'),
                ('Producer', 'Producer'),
                ('Compozitor', 'Compozitor'),
                ('Percutionist}', 'Percutionist'),
                ('Sunetist', 'Sunetist'),
                ('Altul', 'Altul'),
            ]),
            'datainscriere': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'activitate': forms.Select(attrs={
                'class': 'form-control'
            }, choices=[
                ('', 'Selectează activitatea'),
                ('Activ', 'Activ'),
                ('Inactiv', 'Inactiv'),
                ('Suspendat', 'Suspendat'),
            ]),
        }
        # labels = {
        #     'idmembru': 'Membru',
        #     'idtrupa': 'Trupă',
        #     'rol': 'Rol în Trupă',
        #     'datainscriere': 'Data Înscriere',
        #     'activitate': 'Status Activitate',
        # }

    def __init__(self, *args, **kwargs): #se exectută la crearea formularului, unde args si kwargs primeste parametrii si ii trimite mai departe
        super().__init__(*args, **kwargs) #se apeleaza constructorul parintelui (ModelForm), fara el nu se obtin datele userilor
        self.fields['membru'].queryset = Membru.objects.all().order_by('nume', 'prenume') #dropdown window cu toti membrii, ordonati dupa nume & prenume
        self.fields['trupa'].queryset = Trupa.objects.all().order_by('numetrupa') #dropdown window cu toate trupele, ordonate dupa nume
        self.fields['membru'].empty_label = 'Selectează membru'
        self.fields['trupa'].empty_label = 'Selectează trupă'

