from unittest.mock import Mock

from libpythonpro import githubapi


def test_buscar_avatar():
    """
    Exemplo de Teste em Python utilizando o framework Pytest
    Assim NÃO sendo necessário importação

    Utilizando ainda a lib Mock do unittest para isolar o teste em um teste unitário
    simulando o comportamento da API para testar simplesmente o método buscar
    ou seja, o teste independe da integração com a API
    """
    usuario = 'aguiardafa'
    url_esperada = 'https://avatars0.githubusercontent.com/u/16319889?v=4'

    resp_mock = Mock()
    resp_mock.json.return_value = {
        'avatar_url': url_esperada
    }
    githubapi.requests.get = Mock(return_value=resp_mock)

    url_obtida = githubapi.buscar_avatar(usuario)

    assert url_esperada == url_obtida
