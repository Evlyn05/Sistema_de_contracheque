from django.urls import path
from .views import index, listar_contracheques, criar_contracheque, editar_contracheque, deletar_contracheque, detalhe_contracheque

urlpatterns = [
    path('', index, name="home"),
    path('contracheques/', listar_contracheques, name='listar-contracheques'),
    path('contracheques/cadastrar/', criar_contracheque, name='cadastrar-contracheques'),
    path('contracheques/<int:id>/editar/', editar_contracheque, name='editar-contracheque'),
    path('contracheques/<int:id>/deletar/', deletar_contracheque, name='deletar-contracheque'),
    path('contracheques/<int:id>/', detalhe_contracheque, name='detalhe-contracheque')
]