import random
import re
import time
import os
import requests


respostas_secas = ['Sim', 'Não']

respostas_felizes = ['Claro que sim!', 'óbvio né hahaha', 'Simmmm!!!']

respostas_bravas = ['Óbvio que não!!', 'Nããooo!!!!', 'Você esta louco ou algo assim??']

respostas_positivas = ['A Tá bom vai!', 'Vamos la né', 'Dessa vez sim']

respostas_perguntas = ['Como você sabe??', 'Não falo sobre mim...', 'Não gosto de falar sobre mim...', 'Desculpe, essa não posso te responder']

respostas_nao_definidas = ['Nessa você me pegou hahaha', 'Não sei te responde essa...', 'Dessa vez você que manda!']


pergunta =input('Faça sua pergunta:\n\n>> ')

if 'correr' and 'role' and 'caminhar' in pergunta.lower():
    API_KEY = 'f90946e0798b36114441a2b458d4bfcd'
    cidade = 'São carlos'
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}'
    request = requests.get(link)    
    request.dic = request.json()
    temperatura = request.dic['main']['temp'] - 273.15

    if temperatura < 20:

        resptemp = random.choice(respostas_bravas)

        print (f'{resptemp} olha a temperatura que esta! {temperatura}°C')

    if temperatura > 20:

        resptemp = random.choice(respostas_positivas)

        print (f'{respostas_positivas}')

elif 'me matar' and 'me suicidar' and 'cometer suicidio' and 'quero morrer' and 'não quero viver' in pergunta.lower():
    respbrava = random.choice(respostas_bravas)
    print(f'{respbrava}, Você pode ficar desapontado se falhar, mas você está certamente condenado se não tentar')
    print('Posso te dar alguns motivos para viver?')
    op = input('Sim ou claro?\n>> ')
    print(''' 
Tomar banho de chuva outra vez;
Ouvir um Eu te amo;
Poder dizer isso de volta;
Roubar um chocolate, ou esconder o meu só pra mim;
Passar um dia inteiro longe de casa;
Viajar para conhecer alguém;
Tomar banhos quentes;
Ver pessoas sorrindo
E mesmo sem vontade, acabar sorrindo com elas;
Mudar a vida de alguém;
Superar uma decepção;
Assistir filme com amigos por ligação de vídeo;
Ouvir sua música favorita pela milésima vez;
Dormir em uma ligação;
Achar fotos antigas e ver como você melhorou;
Conhecer novas pessoas;
Conquistar algo de valor;
Plantar algo e ver florescendo;
Fazer uma tatuagem, nem que seja de Henna;
Aprender a cozinhar;
Tirar fotos engraçadas;
Cantar em um Karaôke;
Dançar feito maluco(a);
Fazer a própria versão de uma música;
Ter piadas internas;
Ver raios;
Ver a lua;
Se apaixonar;
Olhar pela janela do carro;
Sentir o cheiro do mar;
Vídeogames;
Fazer memórias;
Sentir a brisa em um dia quente;
Mudar o corte de cabelo;
Encarar seus medos;
Fazer algo que valeu a pena;
Ajudar alguém;
Dormir;
Acordar e sentir o cheiro do café;
Estalar uma parte do corpo;
Usar meias engraçadas;
Tirar nota máxima em algo;
Fazer algo que você realmente queira;
Passar o dia sem fazer nada (adoro);
Ver vídeos durante a madrugada;
Virar o travesseiro para o lado frio;
Ter um animal de estimação;
Ver a loucurinha dele quando você chega;
Chorar no ombro de alguém;
Chorar loucamente no final de um filme;
Secar as lágrimas e seguir depois como se nada tivesse acontecido;
Assistir aos fogos de ano novo;
Seu próximo aniversário (estar lá é importante);
Olhar as nuvens;
Andar de barco (ainda quero);
Encontrar um lugar no mundo onde você se encaixe;
Ir a festas, mesmo sem querer, e depois amar ter ido;
Experimentar a vida;
Estar simplesmente vivo ainda, quando muitos não estão mais;
Ver a si mesmo(a) se recuperando quando parecia impossível; (amei)
Ser uma inspiração;
VOCÊ É IMPORTANTE;
VOCÊ faz outras pessoas felizes, ainda que só uma;
Só existe um VOCÊ em todo mundo;
Suas cicatrizes sararão;
Existe uma solução;
Você nunca estará só;
A tendência é melhorar, aguenta mais um pouco;
Seus amigos;
Seus irmãos;
Seus pais;
Seus avós;
Peça ajuda;
EU TE QUERO VIVO(A);
O MUNDO NÃO SERIA O MESMO SEM VOCÊ E SEM MIM;
''')
    print('Tá bom, eu sei que isso foi meio clichê')
    time.slee(3)
    print('Toma umas frases motivacionais então')
    time.sleep(2)
    print('''
"Sonhe como se fosse viver para sempre, viva como se você fosse morrer hoje." ~ James Dean

"Você pode ficar desapontado se falhar, mas você está certamente condenado se não tentar." ~ Beverly Sills

"O mundo abre caminho para o homem que sabe para onde está indo." ~ Ralph Waldo Emerson

"Ou você vai avançar em crescimento, ou você vai recuar em segurança". ~ Abraham H. Maslow

"Se você esperar para fazer tudo até ter certeza de que está certo, você provavelmente nunca irá fazer muita coisa." ~ Win Borden

"Nós vivemos uma vida com aquilo que temos, mas fazemos uma vida por aquilo que damos." ~ Winston Churchill

"A única boa sorte que alguém pode nascer com ela é a habilidade e determinação para superar má sorte." ~ Channing Pollock

"A vida é como andar de bicicleta. Você só não corre risco de cair se estiver parado. ". ~ Claude D. Pimenta

"Um homem que ousa desperdiçar uma hora do tempo não descobriu o valor da vida." ~ Charles Darwin

"O sentido da vida é desconhecido a menos que você descubra isso sozinho." ~ WS Gilbert

"Quanto mais vivemos pela nossa razão, menos que entendemos o significado da vida". ~ Leo Tolstoy

"Todo mundo vive tentando fazer algo grande, que não percebe que a vida é feita de pequenas coisas." ~ Frank A. Clark

"A vida é a soma de todas as suas escolhas." ~ Albert Camus

"No livro da vida, as respostas não estão na parte de trás." ~ Charlie Brown

"Todo homem morre. Nem todo homem realmente vive ". ~ William Wallace 
''')


else:
    resptemp = random.choice(respostas_nao_definidas)
    print(resptemp)