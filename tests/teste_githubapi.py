from unittest import TestCase

from libpythonpro import githubapi


class TesteGitHubApi(TestCase):
    def teste_busca_avatar(self):
        usuario = 'aguiardafa'

        url_obtida = githubapi.buscar_avatar(usuario)
        url_esperada = "https://avatars0.githubusercontent.com/u/16319889?v=4"

        self.assertEqual(url_esperada, url_obtida)
