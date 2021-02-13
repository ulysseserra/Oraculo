import requests
import time
import json

class TelegramBot:
    def __init__(self):
        token = '1374813849:AAHauYQ2ikM4E-fTYOsZDNFZ-uOf39TecEM'
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            mensagens = atualizacao["result"]
            if mensagens:
                for mensagen in mensagens:
                    update_id = mensagen['update_id']
                    mensagem = str(mensagem["message"]["text"])
                    chat_id = mensagem["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        mensagem["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)
    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)
    # Criar uma resposta
    def criar_resposta(self):
      return 'Olá Bem Vindo a Nosso Grupo!'
    # Responder
    def reponder(self,resposta,chat_id):
      # enviar
      link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
      requests.get(link_de_envio)

bot = TelegramBot()
bot.Iniciar()  