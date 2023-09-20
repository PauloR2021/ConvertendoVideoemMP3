import os
from pytube import YouTube
from tkinter import messagebox


class ConverteMP4:

    def __init__(self, link, salvar, nome):
        self.LINK = link
        self.SALVAR = salvar
        self.NOME = nome

        yt = YouTube(self.LINK)

        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(
            output_path=self.SALVAR, filename=self.NOME + '.mp4')

        messagebox.showinfo("Download Concluido", "Download Concluido com Sucesso...")

