from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http.response import HttpResponse
from .models import Membru, Trupa, MembruTrupa
from .forms import MembruForm, TrupaForm, MembruTrupaForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# ===================== FUNCTII PENTRU AUTENTIFICARE =====================
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bine ai venit, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Username sau parolă incorectă.')
        else:
            messages.error(request, 'Date de autentificare invalide.')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# View pentru logout
def logout_view(request):
    logout(request)
    messages.info(request, 'Ai fost deconectat cu succes.')
    return redirect('login')


# ===================== FUNCTII PENTRU MEMBRI =====================
def membru_list(request):
    membri = Membru.objects.all() #afisare totala + ordonare
    paginator = Paginator(membri, 10) #imparte membrii in pagini/10
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) #obtine pagina curenta
    return render(request, 'membru_list.html', {'page_obj': page_obj}) #randeaza membru_list.html pe care -> page_obj

def membru_detail(request, pk):
    membru = get_object_or_404(Membru, pk=pk) #returneaza eroare daca nu gaseste membrul cu id-ul specificat
    trupe_membre = MembruTrupa.objects.filter(membru=membru).select_related('idtrupa') #filtreaza trupele dupa id-ul membrului + join cu tabela trupe pt optimizare
    return render(request, 'membru_detail.html', {
        'membru': membru,  #trimite datele membrului si trupele din care face parte
        'trupe_membre': trupe_membre
    })

@login_required
def membru_create(request):
    if request.method == 'POST':  #daca a fost trimis formularul
        form = MembruForm(request.POST) #creeaza formularul cu datele trimise
        if form.is_valid(): #daca se respecta cerintele din forms, se salveaza
            form.save() 
            messages.success(request, 'Membrul a fost adăugat cu succes!')
            return redirect('membru_list')
    else:
        form = MembruForm() #altfel creeaza un formular gol
    return render(request, 'membru_form.html', {'form': form, 'title': 'Adaugă Membru'})
pass
@login_required
def membru_update(request, pk):
    membru = get_object_or_404(Membru, pk=pk)
    if request.method == 'POST':
        form = MembruForm(request.POST, instance=membru) #deschide formularul gol 
        if form.is_valid():
            form.save() #daca e valid, salveaza modificarile si da redirect la detaliile membrului
            messages.success(request, 'Membrul a fost modificat cu succes!')
            return redirect('membru_detail', pk=membru.pk)
    else:
        form = MembruForm(instance=membru)  # altfel afiseaza formularul cu datele existente
    return render(request, 'membru_form.html', {
        'form': form, 
        'title': 'Modifică Membru',
        'membru': membru   # fata de create, aici apare formularul pentru modificare
    })
pass

@login_required
def membru_delete(request, pk):
    membru = get_object_or_404(Membru, pk=pk) #obtine membrul care trebuie sters || eroare
    if request.method == 'POST':  #important! Verifica daca s-a apasat submit pentru stergere
        membru.delete()
        messages.success(request, 'Membrul a fost șters cu succes!')
        return redirect('membru_list')
    return render(request, 'membru_confirm_delete.html', {'membru': membru}) #pt GET se va afisa pagina de confirmare a stergerii
pass

# ===================== FUNCTII PENTRU TRUPE (analog, ca la MEMBRI) =====================
def trupa_list(request):
    trupe = Trupa.objects.all().order_by('numetrupa')
    paginator = Paginator(trupe, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'trupa_list.html', {'page_obj': page_obj})

def trupa_detail(request, pk):
    trupa = get_object_or_404(Trupa, pk=pk) 
    membri_trupa = MembruTrupa.objects.filter(trupa=trupa).select_related('idmembru')
    return render(request, 'trupa_detail.html', {
        'trupa': trupa,
        'membri_trupa': membri_trupa
    })

@login_required
def trupa_create(request):
    if request.method == 'POST':
        form = TrupaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trupa a fost adăugată cu succes!')
            return redirect('trupa_list')
    else:
        form = TrupaForm()
    return render(request, 'trupa_form.html', {'form': form, 'title': 'Adaugă Trupa'})
pass

@login_required
def trupa_update(request, pk):
    trupa = get_object_or_404(Trupa, pk=pk)
    if request.method == 'POST':
        form = TrupaForm(request.POST, instance=trupa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trupa a fost modificată cu succes!')
            return redirect('trupa_detail', pk=trupa.pk)
    else:
        form = TrupaForm(instance=trupa)
    return render(request, 'trupa_form.html', {
        'form': form, 
        'title': 'Modifică Trupa',
        'trupa': trupa
    })
pass

@login_required
def trupa_delete(request, pk):
    trupa = get_object_or_404(Trupa, pk=pk)
    if request.method == 'POST':
        trupa.delete()
        messages.success(request, 'Trupa a fost ștearsă cu succes!')
        return redirect('trupa_list')
    return render(request, 'trupa_confirm_delete.html', {'trupa': trupa})
pass

# ===================== FUNCTII PENTRU MEMBRU-TRUPA =====================
def membrutrupa_list(request):
    membri_trupe = MembruTrupa.objects.all().select_related('membru', 'trupa').order_by('membru__nume') # aici ma fol de join pt a unii toate cele 3 tabele
    paginator = Paginator(membri_trupe, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'membrutrupa_list.html', {'page_obj': page_obj})

def membrutrupa_detail(request, pk):
    membru_trupa = get_object_or_404(MembruTrupa, pk=pk)  #aici nu e nevoie de join, stiind deja id-ul unic al relatiei
    return render(request, 'membrutrupa_detail.html', {'membru_trupa': membru_trupa})

@login_required
def membrutrupa_create(request):
    # Form-ul va avea dropdown pentru membri si dropdown pentru trupe
    if request.method == 'POST':
        form = MembruTrupaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Relația membru-trupă a fost adăugată cu succes!')
            return redirect('membrutrupa_list')
    else:
        form = MembruTrupaForm()
    return render(request, 'membrutrupa_form.html', {'form': form, 'title': 'Adaugă Membru în Trupă'})
pass

@login_required
def membrutrupa_update(request, pk):
    membru_trupa = get_object_or_404(MembruTrupa, pk=pk)
    if request.method == 'POST':         #daca a fost trimis formularul 
        form = MembruTrupaForm(request.POST, instance=membru_trupa) #populeaza formularul cu datele noi
        if form.is_valid():
            form.save()
            messages.success(request, 'Relația membru-trupă a fost modificată cu succes!')
            return redirect('membrutrupa_detail', pk=membru_trupa.pk) #intoarce te la detaliile asocierii
    else:
        form = MembruTrupaForm(instance=membru_trupa) #altfel deschide formularul cu datele deja existente
    return render(request, 'membrutrupa_form.html', {
        'form': form, 
        'title': 'Modifică Relația Membru-Trupă',
        'membru_trupa': membru_trupa
    })
pass

@login_required
def membrutrupa_delete(request, pk):
    membru_trupa = get_object_or_404(MembruTrupa, pk=pk)
    if request.method == 'POST':
        membru_trupa.delete()
        messages.success(request, 'Relația membru-trupă a fost ștearsă cu succes!')
        return redirect('membrutrupa_list')
    return render(request, 'membrutrupa_confirm_delete.html', {'membru_trupa': membru_trupa})
pass

# ===================== VIEW HOME =====================
def home(request):
    total_membri = Membru.objects.count()
    total_trupe = Trupa.objects.count()
    total_asocieri = MembruTrupa.objects.count()
    
    context = {
        'membri_recenti': Membru.objects.order_by('-idmembru')[:5], #afisez doar cele mai recente 5 intrari
        'trupe_recente': Trupa.objects.order_by('-idtrupa')[:5],
        'total_membri': total_membri,
        'total_trupe': total_trupe,
        'total_asocieri' : total_asocieri,
       
    }
    return render(request, 'home.html', context)