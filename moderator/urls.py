from django.urls import path


from .views import (
    AceitarDevolucao, 
    AceitarPedido, 
    BloquearUsuarios, 
    DashboardAdmin, 
    GerenciarAlunos, 
    RecusarPedido, 
    RemoverMateriais, 
    VerMateriais, 
    VerTodosOsEmprestimos,
    )

urlpatterns = [
    path('dashboard/', DashboardAdmin, name='dashboard'),
    path('ver-materiais/', VerMateriais, name='ver-materiais'),
    path('remover-materiais/<str:pk>', RemoverMateriais, name='remover-material'),
    path('aceitar-devolucao/<str:pk>', AceitarDevolucao, name='aceitar-devolucao'),
    path('aceitar-pedido/<str:pk>', AceitarPedido, name='aceitar-pedido'),
    path('recusar-pedido/<str:pk>', RecusarPedido, name='recusar-pedido'),
    path('todos-emprestimos/', VerTodosOsEmprestimos, name='todos-emprestimos'),

    path('gerenciar-alunos/', GerenciarAlunos, name='gerenciar-alunos'),
    path('bloquear-usuarios/<str:pk>', BloquearUsuarios, name='bloquear-usuarios'),
]