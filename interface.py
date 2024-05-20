# Módulos
from tkinter import *
import customtkinter
import PIL.Image, PIL.ImageTk
from API import api_weather, hour_main

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
        self.theme_default = customtkinter.StringVar(value='System')

        # Criando a mudança de temas
        def theme(value):
            if value == 'Light':
                customtkinter.set_appearance_mode('light')
            elif value == 'Dark':
                customtkinter.set_appearance_mode('dark')
            else:
                customtkinter.set_appearance_mode('system')


        # Local da temperatura
        self.temperature = customtkinter.CTkLabel(self, text='', font=('Open Sans Light', 60), text_color=(gray, white))
        self.temperature.place(relx=0.5, rely=0.4, anchor=CENTER)

        # Local do símbolo
        self.symbol = customtkinter.CTkLabel(self, text='', font=('Open Sans Light', 30), text_color=(gray, white))
        self.symbol.place(relx=0.7, rely=0.35, anchor=CENTER)

        # Local do clima
        self.weather = customtkinter.CTkLabel(self, text='', font=('Open Sans Extra Bold', 20), text_color=(gray, white))
        self.weather.place(relx=0.55, rely=0.55, anchor=CENTER)

        # Funcionamento da api
        def fuction_api(event):
            api_weather(self.search.get(), self.temperature, self.weather, self.symbol)
            hour_main(self.cloud_place, self.sun, self.night, self.cloudy)

        # Barra de pesquisa
        self.search = customtkinter.CTkEntry(self, width=170, height=30, placeholder_text='City/State/Country', font=('Open Sans Extra Bold', 16))
        self.search.configure(text_color=(gray, white), corner_radius=20)
        self.search.grid(row=0, column=0, sticky='sw', padx=10, pady=300)
        self.search.bind('<Return>', fuction_api)

        # Menu da aparência
        self.menu_theme = customtkinter.CTkOptionMenu(self, values=['System', 'Light', 'Dark'], font=('Open Sans Extra Bold', 16), width=30, height=30, variable=self.theme_default, command=theme)
        self.menu_theme.configure(corner_radius=20, text_color=(gray, white), fg_color=(white, gray), button_color=(white, gray), button_hover_color=(white_2, gray_2))
        self.menu_theme.configure(dropdown_fg_color=(white, gray), dropdown_font=('Open Sans Extra Bold', 12))
        self.menu_theme.grid(row=0, column=0, sticky='se', padx=190, pady=300)

        # Imagem da localização
        self.location = customtkinter.CTkImage(dark_image=PIL.Image.open('imagens/location_dark.png'), light_image=PIL.Image.open('imagens/location_light.png'))
        self.location_place = customtkinter.CTkLabel(self, text='', image=self.location)
        self.location_place.place(relx=0.5, rely=0.1, anchor=CENTER)

        # Imagem do clima
        self.sun= customtkinter.CTkImage(dark_image=PIL.Image.open('imagens/sun_dark.png'), light_image=PIL.Image.open('imagens/sun_light.png'),size=(40, 40))
        self.cloudy = customtkinter.CTkImage(dark_image=PIL.Image.open('imagens/cloudy_dark.png'), light_image=PIL.Image.open('imagens/cloudy_light.png'),size=(40, 40))
        self.night = customtkinter.CTkImage(dark_image=PIL.Image.open('imagens/night_dark.png'), light_image=PIL.Image.open('imagens/night_light.png'),size=(40, 40))
        self.cloud_place = customtkinter.CTkLabel(self, text='')
        self.cloud_place.place(relx=0.26, rely=0.54, anchor=W)

    # Adicionando o icone
    def iconbitmap(self, bitmap):
        self._iconbitmap_method_called = False
        super().wm_iconbitmap('imagens\Weather1.ico')

if __name__ == "__main__":
    app = Weather()
    app.mainloop()