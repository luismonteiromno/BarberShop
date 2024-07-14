import requests
from decouple import config


class DadosDeMercado:
    def __init__(self, api_key=None):
        """
        Define os valores(Url, Chave e Headers) padrões do modulo
        """
        self.url_base = 'https://api.dadosdemercado.com.br/v1'
        if api_key is None:
            api_key = config('MERCADO_API_KEY')
        self.headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {api_key}',
        }

    def _request(self, url_metodo, params=None):
        """
        Concatena a url da API com a url enviado pelo metódo
        Faz a requisição GET com a url e os headers
        """
        url = self.url_base + url_metodo
        print(url, params)
        print(self.headers)
        try:
            response = requests.get(url, headers=self.headers, params=params)
            return response.json()
        except:
            return

    def cotacoes(self, ticker_symbol, period_init=None, period_end=None):
        """
        Pegar as cotações do ativo
        :param period_init: Pegar a cotação do ativo a partir de certa data
        :param period_end: Pegar a cotação do ativo até certa data
        """
        url_metodo = f'/tickers/{ticker_symbol}/quotes/'

        parametros = {}
        if period_init:
            parametros['period_init'] = period_init
        if period_end:
            parametros['period_end'] = period_end

        try:
            response = self._request(url_metodo, params=parametros)
            return response
        except:
            return

    def dividendos(self, ticker_symbol, date_from=None):
        """
        Pega todos os dividendos do nome do ativo passado no parâmetro
        :param date_from: Retorna os dividendos com base na data informada ou em datas posteriores,
        considerando a data de pagamento, a data de registro e a data ex-dividendos.
        """
        url_metodo = f'/companies/{ticker_symbol}/dividends'

        parametros = {}
        if date_from:
            parametros['date_from'] = date_from

        try:
            response = self._request(url_metodo, params=parametros)
            return response
        except:
            return

    def desdobramentos(self, ticker_symbol):
        """
        Pega todos os desdobramentos do ativo passado no parâmetro
        """
        url_metodo = f'/companies/{ticker_symbol}/splits'

        try:
            response = self._request(url_metodo)
            return response
        except:
            return

    def lista_de_ativos(self, tipo_do_ativo=None):
        """
        Lista todos os ativos
        :param tipo_do_ativo: Filtro o ativo pelo seu tipo, ex: stock, reit etc...
        """
        url_metodo = '/tickers'

        parametros = {}
        if tipo_do_ativo:
            parametros['ticker_type'] = tipo_do_ativo

        try:
            response = self._request(url_metodo, params=parametros)
            return response
        except:
            return
