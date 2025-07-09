from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OcorrenciaForm
from django.contrib import messages


@login_required
def registrar_ocorrencia(request):
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST)
        if form.is_valid():
            ocorrencia = form.save()
            send_mail(
                subject=f"[OCORRÊNCIA] {ocorrencia.titulo}",
                message=f"Imóvel: {ocorrencia.imovel.nome}\n\n{ocorrencia.descricao}",
                from_email='meuemail44allan@gmail.com',
                recipient_list=['allankevin@sou.faccat.br',
                                'vitorotto@sou.faccat.br', 'fabiomnascimento@sou.faccat.br'],
                fail_silently=False,
            )

            ocorrencia.enviado = True
            ocorrencia.save()
            messages.success(
                request, "Ocorrência enviada para a equipe de assistência.")
            return redirect('imoveis:lista', campo="cliente")
    form = OcorrenciaForm()
    dados = {'form': form}
    return render(request, 'ocorrencias/registrar.html', dados)
