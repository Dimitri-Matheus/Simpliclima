# Módulos
import tkinter
from tkinter import *
import customtkinter
import PIL.Image, PIL.ImageTk

# Cores
white = '#feffff'
white_2 = '#f9f9fa'
gray = '#343638'
gray_2 = '#333432'

# A janela
class Weather(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Propriedades da janela
        self.title('Weather')
        self.geometry('320x350')
        self.resizable(width=False, height=False)

        # Configuração do tema padrão
        customtkinter.set_default_color_theme('dark-blue')
        self.theme_default = customtkinter.StringVar(value='Sistema')

        # Criando a mudança de temas
        def theme(value):
            if value == 'Claro':
                customtkinter.set_appearance_mode('light')
            elif value == 'Escuro':
                customtkinter.set_appearance_mode('dark')
            else:
                customtkinter.set_appearance_mode('system')

        # Local da temperatura
        self.temperature = customtkinter.CTkLabel(self, text='34', font=('Open Sans Light', 60), text_color=(gray, white))
        self.temperature.place(relx=0.5, rely=0.4, anchor=CENTER)

        # Local do símbolo
        self.symbol = customtkinter.CTkLabel(self, text='°C', font=('Open Sans Light', 30), text_color=(gray, white))
        self.symbol.place(relx=0.65, rely=0.35, anchor=CENTER)

        # Local do clima
        self.weather = customtkinter.CTkLabel(self, text='Cloudy', font=('Open Sans Extra Bold', 20), text_color=(gray, white))
        self.weather.place(relx=0.5, rely=0.55, anchor=CENTER)

        # Pesquisar
        self.search = customtkinter.CTkEntry(self, width=170, height=30, placeholder_text='Clima', font=('Open Sans Extra Bold', 16))
        self.search.configure(text_color=(gray, white), corner_radius=20)
        self.search.grid(row=0, column=0, sticky='sw', padx=10, pady=300)

        # Menu da aparência
        self.menu_theme = customtkinter.CTkOptionMenu(self, values=['Sistema', 'Claro', 'Escuro'], font=('Open Sans Extra Bold', 16), width=30, height=30, variable=self.theme_default, command=theme)
        self.menu_theme.configure(corner_radius=20, text_color=(gray, white), fg_color=(white, gray), button_color=(white, gray), button_hover_color=(white_2, gray_2))
        self.menu_theme.configure(dropdown_fg_color=(white, gray), dropdown_font=('Open Sans Extra Bold', 12))
        self.menu_theme.grid(row=0, column=0, sticky='se', padx=190, pady=300)

        # Imagem da localização
        self.location = customtkinter.CTkImage(dark_image=PIL.Image.open('imagens/location_dark.png'), light_image=PIL.Image.open('imagens/location_light.png'))
        self.location_place = customtkinter.CTkLabel(self, text='', image=self.location)
        self.location_place.place(relx=0.5, rely=0.1, anchor=CENTER)

        # Imagem do clima
        self.cloud_1 = customtkinter.CTkImage(dark_image=PIL.Image.open('imagens/sun_dark.png'), light_image=PIL.Image.open('imagens/sun_light.png'),size=(40, 40))
        self.cloud_2 = customtkinter.CTkImage(dark_image=PIL.Image.open('imagens/cloudy_dark.png'), light_image=PIL.Image.open('imagens/cloudy_light.png'),size=(40, 40))
        self.cloud_3 = customtkinter.CTkImage(dark_image=PIL.Image.open('imagens/night_dark.png'), light_image=PIL.Image.open('imagens/night_light.png'),size=(40, 40))
        self.cloud_place = customtkinter.CTkLabel(self, text='', image=self.cloud_1)
        self.cloud_place.place(relx=0.26, rely=0.54, anchor=W)


if __name__ == "__main__":
    app = Weather()
    app.mainloop()