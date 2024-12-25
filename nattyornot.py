'''
Desafio Natt or Not: Associa conceitos de aplicações práticas da IA
- input: Ouvi e reconhece a fala do usuário;
- print: Executa um comando falado.
'''

print("testando...")

#Importa a boblioteca "Speech recognition" que usa o PLN-Processamento de Linguagem Natural
import speech recognition as sr

#Importa a boblioteca "os" que interage com elementos dentro do meu sistema operacional
import os

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
  #Habilita o microfone do usuario
  microfone = sr.Recognizer()

  #Usando o microfone
  with sr.Microphone() as source:
    
    #Chama um algoritmo de redução de ruidos no som
    microfone.adjust_for_ambient_noise(source)

    #Frase para o usuario dizer algo
    print("Diga alguma coisa: ")

    #Armazena o que foi dito numa variavel
    audio - microfone.listen(source) 

  Try:

      #Passa a variavel para o algoritmo reconhecer de padroes 
      frase = microfone.recognize_google(audio,language='pt-BR')

      if "navegador" in frase:
          os.system("start Chrome.exe")
          return False
  
      elif "Excel" in frase:
          os.system("start Excel.exe")
          return False
  
      elif "PowerPoint" in frase:
          os.system("start POWERPNT.exe")
          return False
  
      elif "Edge" in frase:
          os.system("start msedge.exe")
          return False
  
      elif "Fechar" in frase:
          os.system("exit")
          return True