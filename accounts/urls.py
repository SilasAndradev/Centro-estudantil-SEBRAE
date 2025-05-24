from django.urls import path


from .views import RegisterPage, LoginPage, LogoutUser, DashboardUser

from emprestimos.views import SolicitarEmprestimo, FazerDevolucao

urlpatterns = [
    path('registrar/', RegisterPage, name='register'),
    path('login/', LoginPage, name='login'),
    path('', DashboardUser, name='dashboard-aluno'),
    path('logout/', LogoutUser, name='logout'),
    path('solicitar/', SolicitarEmprestimo, name='solicitar'),
    path('devolver/<str:pk>', FazerDevolucao, name='devolver'),

]