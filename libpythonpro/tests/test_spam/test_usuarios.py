import pytest

from libpythonpro.spam.db import Conexao
from libpythonpro.spam.models import Usuario


@pytest.fixture
def conexao():
    # setup
    conexao_obj = Conexao()
    yield conexao_obj
    # tear down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    # setup
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    # tear down
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Diego')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Diego'), Usuario(nome='Aguiar')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
