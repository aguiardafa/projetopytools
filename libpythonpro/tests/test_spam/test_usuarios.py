from libpythonpro.spam.models import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Diego')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Diego'), Usuario(nome='Aguiar')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
