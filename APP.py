# Importando as Bibliotecas
import ConverMP4
import ConverMP3
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

# Váriavel para salvar o caminho dos dados
SALVAR_ARQUIVOS = ''

""" Desenvolvendo o APP"""

# Cores do APP
branco = "#FFFFFF"
neve = "#FFFAFA"
azul_neve = "#F0FFFF"
alice_blue = "#F0F8FF"
fastama_branco = "#F8F8FF"


# Criando as Funções do (APLICATIVO)

# função para Baixar video em MP4
def conver_mp4():
    # Função que dá o comando no Botão para Baixar
    def Diretorio():

        # Utilizando a Biblioteca para acessar as pastas do PC
        salvar_arquivos = filedialog.askdirectory()
        # Salvando o Caminho das Pastas
        SALVAR_ARQUIVOS = salvar_arquivos

        # Salvando a Váriavel aonde captura o link digitado
        LINK = link_video_inserir.get()

        # Salvando a Váriavel aonde caputura o nome para o Arquivo
        NOME = nome_inserir.get()

        # Criando uma condição dentro da Váriavel NOME
        if not NOME:
            # Se NOME estiver vazio então apresenta a mensagem de erro
            messagebox.showerror('Error', "Error! Insira um nome no arquivo")
        else:
            # Se NOME estiver preenchido então ele executa os comandos

            # Criando a Label para Mostrar ao Usuário os dados preenchidos
            txt_resultado = Label(frame, text='', background=alice_blue)
            txt_resultado.place(y=220, x=50)

            # Criando uma mensgem informando que a Transferência começou
            messagebox.showinfo("Download Inciado", "Download Iniciado...")

            # Mostrando o resultados dos dados preenchidos
            txt_resultado['text'] = f'DADOS DA CONVERSAO: \n' \
                                    f'{LINK}\n' \
                                    f'{NOME}\n' \
                                    f'{SALVAR_ARQUIVOS}'

            # Chamando a Clase para baixar o Video
            # Passando os dados para executar a classe
            teste = ConverMP4.ConverteMP4(LINK, SALVAR_ARQUIVOS, NOME)
            print(teste)

    # Solicitando ao Usuário um nome para salvar o arquivo
    nome = Label(frame, text='Insira o Nome do Arquivo:', compound=LEFT, bg=alice_blue, relief=FLAT, anchor='center',
                 border=20)
    nome.place(y=130, x=2)

    nome_inserir = Entry(frame, width=30, bd='2')
    nome_inserir.place(y=145, x=170)

    # Solicitando ao Usuário um Local para Salvar o Video baixado
    salvar = Label(frame, text='Salvar: ', compound=LEFT, bg=alice_blue, relief=FLAT, anchor='center', border=20)
    salvar.place(y=170, x=2)

    salvar_inserir = Button(frame, text='SALVAR', command=Diretorio, background=alice_blue)
    salvar_inserir.place(y=185, x=140)

    txt_resultado = Label(frame, text="CONVERTENDO EM MP4", background=alice_blue)
    txt_resultado.place(y=120, x=20)

# Função para Baixar e Converter os Videos em MP3
def conver_mp3():
    # Função que dá o comando no Botão para Baixar
    def Diretorio():
        # Utilizando a Biblioteca para acessar as pastas do PC
        salvar_arquivos = filedialog.askdirectory()
        # Salvando o Caminho das Pastas
        SALVAR_ARQUIVOS = salvar_arquivos

        # Salvando a Váriavel aonde captura o link digitado
        LINK = link_video_inserir.get()

        # Salvando a Váriavel aonde caputura o nome para o Arquivo
        NOME = nome_inserir.get()

        # Criando uma condição dentro da Váriavel NOME
        if not NOME:
            # Se NOME estiver vazio então apresenta a mensagem de erro
            messagebox.showerror('Error', "Error! Insira um nome no arquivo")
        else:
            # Se NOME estiver preenchido então ele executa os comandos

            # Criando a Label para Mostrar ao Usuário os dados preenchidos
            txt_resultado = Label(frame, text='', background=alice_blue)
            txt_resultado.place(y=220, x=50)

            # Criando uma mensgem informando que a Transferência começou
            messagebox.showinfo("Download Inciado", "Download Iniciado...")

            # Mostrando o resultados dos dados preenchidos
            txt_resultado['text'] = f'DADOS DA CONVERSAO: \n' \
                                    f'{LINK}\n' \
                                    f'{NOME}\n' \
                                    f'{SALVAR_ARQUIVOS}'

            # Chamando a Clase para baixar o Video
            # Passando os dados para executar a classe
            teste = ConverMP3.ConverteMP4(LINK, SALVAR_ARQUIVOS, NOME)
            print(teste)


    # Solicitando ao Usuário um nome para salvar o arquivo
    nome = Label(frame, text='Insira o Nome do Arquivo:', compound=LEFT, bg=alice_blue, relief=FLAT,
                     anchor='center',
                     border=20)
    nome.place(y=130, x=2)

    nome_inserir = Entry(frame, width=30, bd='2')
    nome_inserir.place(y=145, x=170)

    # Solicitando ao Usuário um Local para Salvar o Video baixado
    salvar = Label(frame, text='Salvar: ', compound=LEFT, bg=alice_blue, relief=FLAT, anchor='center', border=20)
    salvar.place(y=170, x=2)

    salvar_inserir = Button(frame, text='SALVAR', command=Diretorio, background=alice_blue)
    salvar_inserir.place(y=185, x=140)

    txt_resultado = Label(frame, text="CONVERTENDO EM MP3", background=alice_blue)
    txt_resultado.place(y=120, x=20)

# Criando a Janela do (APLICATIVO)

app = Tk()
app.title('Download Video')
app.geometry('500x300')
app.configure(bg=fastama_branco)

# Configurando o Frame do Aplicativo

frame = Frame(app,
              )
frame.grid(row=1, column=0)

# Colocando o Icone no APP

imagem = Image.open('imagem/icone.png')
imagem = imagem.resize((50, 50))
imagem = ImageTk.PhotoImage(imagem)

label_icone = Label(frame, image=imagem, compound=LEFT, bg=fastama_branco)
label_icone.place(y=10, x=400)

# Inserindo Os Objetos na Tela

link_video = Label(frame, text='Digite o LINK :', compound=LEFT, bg=alice_blue, relief=FLAT, anchor='center', border=20)
link_video.place(y=10, x=2)

link_video_inserir = Entry(frame, width=40, bd='2')
link_video_inserir.place(y=25, x=110)

# Inserindo os Botões

# Botão Para Converter em MP4
mp4 = Button(frame, text='MP4', command=conver_mp4, background=alice_blue)
mp4.place(y=80, x=30)

# Botão para Convereter em MP3
mp3 = Button(frame, text='MP3', command=conver_mp3, background=alice_blue)
mp3.place(y=80, x=110)

# Chamando a Função do TKinter para manter o Aplicativo aberto
app.mainloop()
