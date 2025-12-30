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
        link = self.url_entry.get()
        if not link:
            self.status_label.configure(text="Erro: Link vazio!", text_color="red")
            return
        
        self.download_btn.configure(state="disabled", text="Baixando...")
        self.status_label.configure(text="Iniciando conexão...", text_color="white")
        
        # Inicia a Thread para não travar a GUI
        thread = threading.Thread(target=self._download_logic, args=(link,))
        thread.start()

    def _download_logic(self, link):
        try:
            ydl_opts = {
                'outtmpl': 'Downloads/%(title)s.%(ext)s',
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            }

            if not os.path.exists('Downloads'):
                os.makedirs('Downloads')

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

            self.status_label.configure(text="Sucesso! Vídeo salvo na pasta Downloads.", text_color="green")
            
        except Exception as e:
            self.status_label.configure(text=f"Erro: {str(e)}", text_color="red")
        
        finally:
            self.download_btn.configure(state="normal", text="Iniciar Download")

if __name__ == "__main__":
    app = YouTubeManager()
    app.mainloop()