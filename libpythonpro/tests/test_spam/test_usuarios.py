import pytest

from libpythonpro.spam.db import Conexao
from libpythonpro.spam.models import Usuario


@pytest.fixture
def conexao():
    return Conexao()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    return sessao_obj


def test_salvar_usuario(conexao, sessao):
    usuario = Usuario(nome='Diego')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuarios(conexao, sessao):
    usuarios = [Usuario(nome='Diego'), Usuario(nome='Aguiar')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
