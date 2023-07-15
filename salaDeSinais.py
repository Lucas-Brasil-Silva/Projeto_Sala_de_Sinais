import requests
from datetime import datetime
from time import sleep
import os

def enviar_imagem(chat_id, links_imagens, caption):
    token = 'TOKEN DO BOT'
    for photo in links_imagens:
      urlApi = requests.get(
          f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={photo}&caption={caption}')

preco_venda = True
preco_compra = True
while True:
    resultado = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    cotacao_dolar = float(resultado.json()['USDBRL']['ask'])
    data = datetime.today().strftime('%d/%m/%Y - %H:%M')

    if cotacao_dolar >= 4.8710 and preco_venda == True:
        imagem_sell = ['https://i.ibb.co/NKbXFhx/sell-seta.png']
        mensagem = f'📢Dólar chegando em uma zona de venda.📢{os.linesep}💲Dólar: {cotacao_dolar}💲{os.linesep}🕒Data: {data}🕒{os.linesep}📟link: www.linkparavenderdolar.com📟'
        enviar_imagem(chat_id='-1001932641659',links_imagens=imagem_sell,caption=mensagem)
        preco_venda = False

    if cotacao_dolar <= 4.87 and preco_compra == True:
        imagem_buy = ['https://i.ibb.co/RbPnKNL/buy-seta.png']
        mensagem = f'📢Dólar chegando em uma zona de compra.📢{os.linesep}💲Dólar: {cotacao_dolar}💲{os.linesep}🕒Data: {data}🕒{os.linesep}📟link: www.linkparacomprardolar.com📟'
        enviar_imagem(chat_id='-1001932641659',links_imagens=imagem_buy,caption=mensagem)
        preco_compra = False
    sleep(10)