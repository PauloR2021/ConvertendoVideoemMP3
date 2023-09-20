
import os
from pytube import YouTube
from tkinter import messagebox

class ConverteMP4:

    def __init__(self,link,salvar,nome):

        self.LINK = link
        self.SALVAR = salvar
        self.NOME = nome

        yt = YouTube(self.LINK)

        video = yt.streams.filter(only_audio=True).first()

        download_arquivo = video.download(output_path=self.SALVAR,filename=self.NOME + '.mp3')

