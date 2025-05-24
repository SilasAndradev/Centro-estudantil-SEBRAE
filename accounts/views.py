from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from .forms import UserProfileForm
from .models import UserProfile
from moderator.models import Pedido
from emprestimos.models import Emprestimo
# Create your views here.

def RegisterPage(request):
    form = UserCreationForm()
    alunoForm = UserProfileForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        alunoForm = UserProfileForm(request.POST)
        
        if form.is_valid() and alunoForm.is_valid():

            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            aluno = alunoForm.save(commit=False)
            aluno.user = user
            aluno.save()


            login(request, user)
            return redirect('dashboard-aluno')
        else:
            messages.error(request, 'Ocorreu um erro durante o registro!')


    context = {
        'form':form,
        'alunoForm': alunoForm,
    }
    return render(request, 'accounts/cadastrar.html', context)


def LoginPage(request):

    if request.user.is_authenticated:
        return redirect('dashboard-aluno')

    if request.method == 'POST':
        matricula = request.POST.get('matricula')
        password = request.POST.get('password')

        try:
            username = UserProfile.objects.get(matricula=matricula).user.username
        except Exception as _:
            messages.error(request, 'Usuário não existe!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard-aluno')
        else:
            messages.error(request, 'Nome de usuário OU senha estão erradas!')

    context = {

    }
    return render(request, "accounts/login.html", context)


@login_required(login_url='/login/')
def LogoutUser(request):
    logout(request)
    return redirect('dashboard-aluno')


@login_required(login_url='/login/')
def DashboardUser(request):
    aluno = UserProfile.objects.get(user=request.user)
    context = {
            'pedidos_pendentes':Pedido.objects.filter(
                aluno=aluno, 
                pendência=True
                ),
            'pedidos_respondidos':Pedido.objects.filter(
                aluno=aluno, 
                pendência=False,
                ),
            'emprestimos':Emprestimo.objects.filter(
                aluno=aluno, 
                ),
       }
    return render(request, "accounts/dashboard.html", context)