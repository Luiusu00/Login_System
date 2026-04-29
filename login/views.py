from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def telaLogin(request):
    if request.method == 'GET':
        return render(request, 'telaLogin.html')
    
    if request.method == 'POST':
        acao = request.POST.get('acao')

        if acao == 'login':
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            
            try:
                usuario = Usuario.objects.get(email=email)
                if check_password(senha, usuario.senha):
                    request.session['usuario_nome'] = usuario.nome
                    request.session['usuario_email'] = usuario.email
                    return redirect('sistema')
                else:
                    messages.error(request, 'Senha incorreta!')
                    return redirect('telaLogin')
            except Usuario.DoesNotExist:
                messages.error(request, 'Usuário não cadastrado!')
                return redirect('telaLogin')

        if acao == 'cadastro':
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            nome = request.POST.get('nome')
            confirmar_senha = request.POST.get('confirmar_senha')
      
            if Usuario.objects.filter(email=email).exists():
                messages.error(request, 'E-mail encontra-se cadastrado')
                return redirect('telaLogin')
            else:
                if senha == confirmar_senha:
                    usuario = Usuario.objects.create(nome=nome, email=email, senha=make_password(senha))
                    usuario.save()
                    messages.success(request, 'Conta criada com sucesso!')
                    return redirect('telaLogin')
                else:
                    messages.error(request, 'Senhas diferentes!')
                    return redirect('telaLogin')
            
def newPassword(request):
    if request.method == 'GET':
        return render(request, 'new_password.html')
    
    if request.method == 'POST':
        acao = request.POST.get('acao')

        if acao == 'verificar_email':
            email = request.POST.get('email')
            if Usuario.objects.filter(email=email).exists():
                return render(request, 'new_password.html', {'step': 2, 'email': email})
            else:
                messages.error(request, 'Email não cadastrado')
                return render(request, 'new_password.html', {'step': 1})
        
        if acao == 'verificar_codigo':
            email = request.POST.get('email')
            codigo = request.POST.get('codigo')
            if len(codigo) == 6:
                return render(request, 'new_password.html', {'step': 3, 'email': email})
            else:
                messages.error(request, 'Digite todos os 6 dígitos')
                return render(request, 'new_password.html', {'step': 2, 'email': email})
        
        if acao == 'red_senha':
            new_senha = request.POST.get('senha')
            conf_senha = request.POST.get('conf_senha')
            email = request.POST.get('email')
            if len(new_senha) < 8:
                messages.error(request, 'A senha deve ter pelo menos 8 caracteres')
                return render(request, 'new_password.html', {'step': 3, 'email': email})
            if new_senha != conf_senha:
                messages.error(request, 'As senhas não coincidem')
                return render(request, 'new_password.html', {'step': 3, 'email': email})
            try:
                usuario = Usuario.objects.get(email=email)
                usuario.senha = make_password(new_senha)
                usuario.save()
                messages.success(request, 'Senha redefinida com sucesso!')
                request.session['usuario_nome'] = usuario.nome
                request.session['usuario_email'] = usuario.email
                return redirect('sistema')
            except Usuario.DoesNotExist:
                messages.error(request, 'Usuário não encontrado')
                return render(request, 'new_password.html', {'step': 1})



def sistema(request):
    if request.method == 'GET':
        nome = request.session.get('usuario_nome','')
        email = request.session.get('usuario_email','')
        return render(request, 'sistema.html', {'nome': nome, 'email': email})
    
    if request.method == 'POST':
        acao = request.POST.get('acao')
        if acao != 'alterar_senha':
            return redirect('sistema')
        email = request.session.get('usuario_email', '')
        nome = request.session.get('usuario_nome','')
        senha_atual = request.POST.get('senha_atual')
        nova_senha = request.POST.get('nova_senha')
        conf_senha = request.POST.get('conf_senha')
        usuario = Usuario.objects.get(email=email)
        if check_password(senha_atual, usuario.senha):
            if nova_senha == conf_senha:
                usuario.senha = make_password(nova_senha)
                usuario.save()
                messages.success(request, 'Senha redefinida com sucesso!')
                return render(request, 'sistema.html', {'nome': nome, 'email': email})
            else:
                messages.error(request, 'As senhas não coincidem!')
                return render(request, 'sistema.html', {'nome': nome, 'email': email})
        else:
            messages.error(request, 'A senha atual não coincide!')
            return render(request, 'sistema.html', {'nome': nome, 'email': email})

def logout(request):
    request.session.flush()
    return redirect('telaLogin')
