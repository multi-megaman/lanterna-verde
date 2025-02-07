from django.urls import path

from lanternaverde_web.notificacaoAdm import notificacao_lida
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path("analista/add", views.cadastro_analista, name='criar_analista'),
    path("analista/update", views.alterar_analista, name='alterar cadastro'),
    path("analista/detail", views.detalhar_analista, name='detalhar_analista'),

    path('user', views.get_logged_usuario, name='test_permission'),
    path('user/admin', views.get_logged_administrador, name='get_admin'),
    path('user/analista', views.get_logged_analista, name='get_anal'),
    path('user/empresa', views.get_logged_empresa, name='get_empresa'),
    path('user/password/change', views.alterar_senha, name='alterar_senha'),

    path('perguntas', views.get_questoes, name='questoes'),
    path('perguntas/add', views.create_questao, name='create_questoes'),

    path('solicitacoesAnalise', views.get_solicitacoes, name='get_solicitacoes'),
    path('solicitacoesAnalise/add', views.create_solicitacao, name="Criar Solicitação de Análise"),
    path('solicitacoesAnalise/detail', views.get_solicitacao, name='Get Solicitação Análise'),
    path('solicitacoesAnalise/analises', views.get_analysis_by_request, name='get_analysis_by_request'),

    path('analise', views.listar_analises, name='listar_analises'),
    path('analise/empresa', views.listar_analises_empresa, name='listar_analises_empresa'),
    path('analise/add', views.criar_analise, name='criar_analise'),
    path('analise/detail', views.detalhar_analise, name='detalhar_analise'),
    path('analise/update', views.atualizar_analise, name='atualizar_analise'),
    path('analise/finish', views.finalizar_analise, name='concluir_analise'),

    path('empresa/add', views.cadastro_empresa, name='cadastro_empresa'),
    path('empresa/update', views.alterar_empresa, name='alterar_empresa'),
    path('empresa/assign-package', views.assinar_pacote, name='assinar_pacote'),
    path('empresa/analises', views.listar_analises_empresa, name='listar_analises_empresa'),
    path('empresa/analises/not-reanalyzed', views.listar_analises_passiveis_reanalise, name='listar_analises_empresa'),
    path('empresa/analise/<str:pk>', views.get_info_analise_empresa, name='get_info_analise_empresa'),
    path('empresa/analise/<str:pk>/solicitar-reanalise', views.solicitar_reanalise, name='solicitar_reanalise'),
    path('empresa/ranking', views.get_ranking, name='get_ranking'),
    #path('empresa/<str:id>', views.get_empresa, name='get_empresa'),
    path('empresa/report', views.compilar_relatorio_geral_empresa, name='compilar_relatorio_geral_empresa'),
    path('empresa', views.listar_empresas, name='listar_empresas'),
    path('empresa/detail', views.detalhar_empresa, name='detalhar_empresa'),

    path('relatorio', views.get_relatorios, name='get_relatorios'),
    path('relatorio/comment', views.comment_relatorio, name='comment_relatorio'),
    path('relatorio/empresa', views.get_relatorios_por_empresa, name='get_relatorios_por_empresa'),

    path('notificacoes', views.listar_notificacoesAdm, name='listar_norificacoes'),
    path('notificacoes/read', views.notificacao_lida, name='notificacao_lida'),

    path('public/empresa', views.listar_empresas_public, name='listar_empresas'),
    path('public/empresa/detail', views.detalhar_empresa_public, name='detalhar_empresa'),

]
