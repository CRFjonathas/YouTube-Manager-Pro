import customtkinter as ctk
import threading
import os

# configuração inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class YouTubeManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configuração da janela
        self.title("Nicacio Media Downloader")
        self.geometry("600x450")
        self.resizable(False,False)

        # layout
        self.logo_label = ctk.CTkLabel(self, text="YouTube Menager Pro", font=("Roboto", 24, "bold"))
        self.logo_label.pack(pady=20)

        self.url_entry = ctk.CTkEntry(self, width=450, placeholder_text="Cole o link do vídeo aqui...")
        self.url_entry.pack(pady=10)

        self.download_btn = ctk.CTkButton(self, text="Iniciar Download", command=self.iniciar_download)
        self.download_btn.pack(pady=20)

        self.status_label = ctk.CTkLabel(self, text="Pronto para iniciar", text_color="gray")
        self.status_label.pack(pady=5)

    def iniciar_download(self):
        print("Botão clicado (Lógica ainda não implementada)")

if __name__ == "__main__":
    app = YouTubeManager()
    app.mainloop()