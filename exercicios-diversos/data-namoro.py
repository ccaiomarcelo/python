
import customtkinter
from datetime import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("600x400")

data_namoro = datetime(2023, 10, 29)
data_atual = datetime.today()
diferença = data_atual - data_namoro

meses_completos = diferença.days // 30

texto = customtkinter.CTkLabel(janela, text="RELANTIONSHIP SAVER 🤫")
texto.pack(padx=5, pady=5)

dt_namoro = customtkinter.CTkLabel(janela, text="Data do namoro: 29/10/2023")
dt_namoro.pack(padx=5, pady=5)

dias = customtkinter.CTkLabel(janela, text=f"Dias: {diferença.days}")
dias.pack(padx=5, pady=5)

meses = customtkinter.CTkLabel(janela, text=f"Meses: {meses_completos}")
meses.pack(padx=5, pady=5)


janela.mainloop()