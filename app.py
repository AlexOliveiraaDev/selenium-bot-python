import random
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()

options.add_argument("--headless")  # make run in background
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
options.add_argument(f"user-agent={user_agent}")
options.add_argument("--disable-blink-features=AutomationControlled")  # Remove rastros do Selenium

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://discord.com/login")
time.sleep(2)  # wait page loading

EMAIL = "email@email.com"
SENHA = "pass"
current_time = ""

email_input = driver.find_element(By.NAME, "email")
email_input.send_keys(EMAIL)

senha_input = driver.find_element(By.NAME, "password")
senha_input.send_keys(SENHA)
senha_input.send_keys(Keys.RETURN)
print("login done")

time.sleep(3)  # wait login

# Acessar o canal desejado
CANAL_URL = "https://discord.com/channels/1154389285718462514/1154389286192427051" # cria channel geral
driver.get(CANAL_URL)
time.sleep(2)
print("loaded page")

last_time = 0

# Lista de frases aleatórias
frasesbak = [
    "????????????",
    "como estamos?",
    "tem que acelerar isso aí!",
    "qual o prazo?",
    "nada está funcionando...",
    "será que vamos conseguir terminar?",
    "vamos focar mais!",
    "ainda estamos longe do objetivo!",
    "o tempo está passando...",
    "tá devagar demais!",
    "a plataforma não vai se fazer sozinha!",
    "precisamos de progresso!",
    "isso precisa sair do papel!",
    "quem vai tomar a frente disso?",
    "parece que está parado!",
    "vamos agilizar isso!",
    "já podemos testar alguma coisa?",
    "qual a atualização de hoje?",
    "ninguém está trabalhando nisso?",
    "precisamos de um sprint forte essa semana!",
    "estamos esperando há um tempo já...",
    "o que está pegando?",
    "precisamos resolver isso logo!",
    "não dá para enrolar mais!",
    "isso deveria estar pronto ontem!",
    "o prazo está cada vez mais apertado...",
    "ninguém quer assumir isso?",
    "alguma novidade ou seguimos sem progresso?",
    "tá na hora de sair do papel!",
    "o relógio não para!",
    "até quando vamos empurrar isso?",
    "já deu tempo suficiente, né?",
    "isso aqui está arrastado demais!",
    "vamos parar de empurrar com a barriga!",
    "precisamos de mais ação e menos conversa!",
    "se não andar agora, depois vai ser tarde!",
    "alguma previsão realista?",
    "não quero mais desculpas, quero resultados!",
    "alguém tem alguma solução ou só problemas?",
    "tá todo mundo dormindo?",
    "o projeto não anda sozinho!",
    "a prioridade parece ser outra...",
    "o tempo está voando e nada acontece!",
    "já passou da hora de resolver isso!",
    "vai sair ou vamos continuar só falando?",
    "isso está virando lenda...",
    "precisamos de entrega, não de promessa!",
    "parece que ninguém se importa com isso...",
    "estamos esperando um milagre?",
    "não adianta empurrar para depois!",
    "Será que alguém aí acordou hoje ou tá tudo no piloto automático?",
    "O ritmo tá de dar sono, hein! 😴",
    "Vamos parar de fingir que tá tudo bem e fazer algo útil?",
    "Esse projeto tá mais perdido que agulha no palheiro!",
    "O prazo tá rindo da nossa cara, sabia?",
    "Tá na hora de parar de enrolar e meter a mão na massa!",
    "Alguém viu o progresso por aí ou ele fugiu?",
    "Isso tá mais lento que tartaruga manca!",
    "Se depender desse ritmo, a gente entrega em 2050!",
    "Cadê a energia, pessoal? Tá parecendo velório!",
    "?????????? Alguém me explica por que tá tudo parado?",
    "O chefe já tá com cara de quem vai explodir!",
    "Vamos mexer esse traseiro ou vai ficar só na promessa?",
    "Tá todo mundo de brincadeira ou eu que tô vendo coisa?",
    "Esse projeto tá mais enrolado que novelo de lã!",
    "O que falta? Vergonha na cara ou competência?",
    "Tá na hora de parar de chorar e começar a fazer!",
    "O relógio tá correndo e a gente tá andando pra trás!",
    "Será que alguém aí sabe o que é prazo ou é tudo ilusão?",
    "Ninguém quer sujar as mãos, né? Só ficar na zona de conforto!",
    "Isso tá mais bagunçado que quarto de adolescente!",
    "Vamos parar de lero-lero e mostrar serviço!",
    "O tempo não espera preguiçoso, acorda!",
    "Tá todo mundo esperando o gênio da lâmpada aparecer?",
    "Se continuar assim, esse projeto vira piada!",
    "Cadê o gás? Tá parecendo fogão sem chama!",
    "?????????? Será que alguém se toca ou vamos afundar?",
    "O prazo tá mais apertado que calça de lycra!",
    "Vamos parar de fazer corpo mole e correr atrás!",
    "Isso tá andando ou tá só fingindo movimento?",
    "Tá na hora de alguém assumir o volante dessa bagunça!",
    "O progresso tá tão escondido que nem binóculo acha!",
    "Se não acelerar, vai sobrar pra todo mundo!",
    "Tá todo mundo jogando pro alto ou eu que tô louco?",
    "O que tá faltando? Café ou vontade mesmo?",
    "Esse ritmo tá me dando vontade de gritar! 😡",
    "Vamos parar de enrolação e botar pra quebrar!",
    "O prazo tá mais perto que o chão do abismo!",
    "Tá todo mundo de férias mentais ou o quê?",
    "Isso tá mais devagar que fila de banco!",
    "Cadê a atitude? Tá todo mundo anestesiado?",
    "Se não correr agora, depois só choro!",
    "O projeto tá gritando por ajuda e ninguém ouve!",
    "Vamos parar de empurrar com a bunda e resolver logo!",
    "Tá na hora de parar de mimimi e entregar algo!",
    "O tempo tá passando e a paciência acabando!",
    "Será que alguém aí lembra o que é urgência?",
    "Tá todo mundo com preguiça ou é só impressão?",
    "Isso tá mais parado que estátua no museu!",
    "Vamos acordar antes que o chefe venha com o chicote!",
    "O prazo tá tão perto que dá pra sentir o cheiro!",
    "Tá na hora de parar de sonhar e começar a fazer!",
    "?????????? Cadê a vergonha na cara, gente?",
    "Isso tá mais lento que internet discada!",
    "Vamos parar de ficar olhando pro teto e agir!",
    "O progresso tá mais perdido que ovo em ninho de cobra!",
    "Tá todo mundo esperando o milagre ou só eu vejo isso?",
    "Se não andar logo, vira caso de polícia!",
    "O relógio não perdoa, mas a gente parece que sim!",
    "Vamos parar de enrolar ou querem virar meme?",
    "Tá na hora de alguém gritar ‘bora!’ e fazer acontecer!",
    "O prazo tá mais quente que panela no fogo!",
    "Tá todo mundo de braços cruzados ou é só impressão?",
    "Isso tá mais arrastado que carroça quebrada!",
    "Cadê o foco? Tá parecendo circo sem lona!",
    "Vamos acelerar ou querem levar bronca?",
    "O tempo tá voando e a gente tá plantado!",
    "Tá na hora de parar de conversa fiada e entregar!",
    "?????????? Será que alguém tá trabalhando ou é só teatro?",
    "O projeto tá mais parado que água de poço!",
    "Vamos parar de fazer de conta e resolver essa droga!",
    "O prazo tá rindo e a gente chorando!",
    "Tá todo mundo esperando o Papai Noel trazer a solução?",
    "Se não correr agora, depois não adianta reclamar!",
    "Isso tá mais devagar que lesma em férias!",
    "Cadê o esforço? Tá todo mundo no modo zumbi?",
    "Vamos parar de ficar coçando e fazer algo decente!",
    "O tempo tá esgotando e a paciência também!",
    "Tá na hora de alguém botar ordem nesse caos!",
    "O progresso tá mais sumido que agulha no oceano!",
    "Vamos acelerar ou querem virar piada no escritório?",
    "?????????? Alguém viu o ritmo por aí?",
    "O prazo tá mais apertado que cinto depois do almoço!",
    "Tá todo mundo dormindo em pé ou é só comigo?",
    "Isso tá mais enrolado que cabo de fone no bolso!",
    "Vamos parar de fingir esforço e mostrar resultado!",
    "O relógio tá correndo e a gente tá de boa?",
    "Tá na hora de parar de blá-blá-blá e entregar logo!",
    "O projeto tá mais perdido que turista sem mapa!",
    "Cadê a pressa? Tá parecendo feriado eterno!",
    "Se não mexer agora, depois só resta chorar!",
    "Tá todo mundo esperando o mundo girar sozinho?",
    "Vamos parar de enrolar e botar pra frente!",
    "O prazo tá mais perto que o fim do expediente!",
    "Isso tá mais lento que mula empacada!",
    "Cadê o ânimo? Tá todo mundo com cara de segunda-feira!",
    "?????????? Será que alguém quer trabalhar hoje?",
    "O progresso tá mais escondido que ouro em caverna!",
    "Vamos parar de ficar boiando e nadar de uma vez!",
    "O tempo tá acabando e a gente tá de brincadeira?",
    "Tá na hora de alguém pegar esse touro pelos chifres!",
    "O projeto tá mais parado que poste na calçada!",
    "Vamos acelerar ou querem virar lenda urbana?",
    "O prazo tá tão em cima que dá pra ouvir ele rindo!",
    "Tá todo mundo de palhaçada ou eu que tô vendo errado?",
    "Isso tá mais bagunçado que gaveta de bagunceiro!",
    "Vamos parar de ficar de ladinho e correr atrás!",
    "O relógio não para, mas a gente parece que sim!",
    "Tá na hora de parar de sonhar acordado e fazer!",
    "O progresso tá mais lento que fila de SUS!",
    "?????????? Cadê a vontade de vencer, gente?",
    "O prazo tá mais quente que brasa na mão!",
    "Tá todo mundo esperando o café ficar pronto pra começar?",
    "Isso tá mais devagar que carro sem gasolina!",
    "Vamos parar de enrolar ou querem levar esporro?",
    "O tempo tá voando e a gente tá plantando bananeira!",
    "Tá na hora de alguém botar a cara no sol!",
    "O projeto tá mais perdido que cego em tiroteio!",
    "Cadê o ritmo? Tá parecendo valsa fúnebre!",
    "Se não correr agora, depois só resta o arrependimento!",
    "Tá todo mundo esperando o santo descer do céu?",
    "Vamos parar de fazer graça e entregar algo!",
    "O prazo tá mais perto que o fim do mundo!",
    "Isso tá mais parado que pedra no deserto!",
    "?????????? Será que alguém aí tá vivo?",
    "O progresso tá mais sumido que chave na bagunça!",
    "Vamos acelerar ou querem virar história de fracasso?",
    "O relógio tá rindo da nossa cara e ninguém vê?",
    "Tá na hora de parar de ficar de mimimi e agir!",
    "O projeto tá mais lento que boi no pasto!",
    "Cadê o esforço? Tá todo mundo no modo tartaruga?",
    "Vamos parar de ficar de papinho e resolver isso!",
    "O tempo tá esgotando e a gente tá de boa?",
    "Tá na hora de alguém assumir essa bomba!",
    "O prazo tá mais apertado que sapato novo!",
    "Tá todo mundo de brincadeira ou é só comigo?",
    "Isso tá mais enrolado que novela das oito!",
    "Vamos parar de ficar olhando pro nada e fazer!",
    "O progresso tá mais devagar que procissão de domingo!",
    "?????????? Cadê a energia, pessoal?",
    "O relógio tá correndo e a gente tá de férias?",
    "Tá na hora de parar de enrolação e botar pra quebrar!",
    "O projeto tá mais parado que trânsito na chuva!",
    "Vamos acelerar ou querem virar motivo de piada?",
    "O prazo tá mais em cima que chefe chato!",
    "Tá todo mundo esperando o milagre ou só eu vejo isso?",
    "Isso tá mais lento que melaço em dia frio!",
    "Cadê a atitude? Tá parecendo velório de novo!",
    "Vamos parar de ficar de blablablá e entregar logo!",
    "O tempo acabou, agora é correr ou chorar! 😭"
]

frases = [
  "?????????",
  "?????????????????",
  "??????",
  "?????????????????????????????????",
  "?????????????????????????????????????????",
  "?????????????????????????",
  "????????",
  "??????????????????????????????????????????????????",
  "??????????????????????",
  "?????????????",
  "?????????????????????????????????????????????????????????????????",
  "????????????????????????????????????????????",
  "??????????????",
  "?????????????????????????????????????????????????????????????????????????????????????",
  "?????????????????????????????????????????????????????????????????????????????????????????????????????????????????",
  "??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????",
  "???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????",
  "??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????"
]
def enviar_mensagem():
    try:
        mensagem_box = driver.find_element(By.XPATH, "//div[@role='textbox']")
        frase = random.choice(frases) 
        mensagem = f"{frase} @.srdaniel @italo19"
        mensagem_box.send_keys(mensagem)
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.RETURN).perform()
        mensagem_box.send_keys(Keys.RETURN)
        current_time = datetime.now().strftime("%H:%M:%S")
        print("\n {current_time} : Mensagem enviada:", mensagem)
    except Exception as e:
        print("Erro ao enviar mensagem:", e)

while True:
    enviar_mensagem()
    last_time = random.randint(400, 4000) #in seconds
    minutes = last_time / 60
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"{current_time} : Prox msg:{minutes} minutos")
    time.sleep(last_time) 
