import pytest

from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['diego.fernandes.aguiar@gmail.com', 'dieguinho.uft@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(
        destinatario,
        'aguiardafa@decea.gov.br',
        'Assunto E-mail',
        'Corpo do E-mail'
    )
    assert destinatario in resultado
