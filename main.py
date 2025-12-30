import customtkinter as ctk
import yt_dlp
import threading
import os

# Configuração Inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class YouTubeManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da Janela
        self.title("Nicacio Media Downloader")
        self.geometry("600x450")
        self.resizable(False, False)

        # Layout
        self.logo_label = ctk.CTkLabel(self, text="YouTube Manager Pro", font=("Roboto", 24, "bold"))
        self.logo_label.pack(pady=20)

        self.url_entry = ctk.CTkEntry(self, width=450, placeholder_text="Cole o link do vídeo aqui...")
        self.url_entry.pack(pady=10)

        self.download_btn = ctk.CTkButton(self, text="Iniciar Download", command=self.iniciar_download)
        self.download_btn.pack(pady=20)

        self.status_label = ctk.CTkLabel(self, text="Pronto para iniciar", text_color="gray")
        self.status_label.pack(pady=5)

    def iniciar_download(self):
        link = self.url_entry.get()
        if not link:
            self.status_label.configure(text="Erro: Link vazio!", text_color="red")
            return
        
        # Trava o botão e avisa o usuário
        self.download_btn.configure(state="disabled", text="Baixando...")
        self.status_label.configure(text="Iniciando conexão...", text_color="white")
        
        # Inicia a Thread para não travar a janela
        thread = threading.Thread(target=self._download_logic, args=(link,))
        thread.start()

    def _download_logic(self, link):
        try:
            # Opções básicas do yt-dlp
            ydl_opts = {
                'outtmpl': 'Downloads/%(title)s.%(ext)s', # Salva na pasta Downloads
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', # Tenta pegar a melhor qualidade MP4
            }

            # Cria a pasta se não existir
            if not os.path.exists('Downloads'):
                os.makedirs('Downloads')

            # O Download acontece aqui
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

            # Sucesso
            self.status_label.configure(text="Sucesso! Vídeo salvo na pasta Downloads.", text_color="green")
            
        except Exception as e:
            self.status_label.configure(text=f"Erro: {str(e)}", text_color="red")
        
        finally:
            # Reativa o botão quando terminar (seja sucesso ou erro)
            self.download_btn.configure(state="normal", text="Iniciar Download")

if __name__ == "__main__":
    app = YouTubeManager()
    app.mainloop()