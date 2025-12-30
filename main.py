import customtkinter as ctk
import yt_dlp
import threading
import os

# Configuração Visual
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class YouTubeManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Janela
        self.title("Nicacio Media Downloader")
        self.geometry("600x500")
        self.resizable(False, False)

        # 1. Logo
        self.logo_label = ctk.CTkLabel(self, text="YouTube Manager Pro", font=("Roboto", 24, "bold"))
        self.logo_label.pack(pady=20)

        # 2. Input de URL
        self.url_entry = ctk.CTkEntry(self, width=450, placeholder_text="Cole o link do YouTube aqui...")
        self.url_entry.pack(pady=10)

        # 3. Seletor de Formato (Vídeo ou Áudio)
        self.format_label = ctk.CTkLabel(self, text="Escolha o Formato:")
        self.format_label.pack(pady=(5, 0))
        
        self.format_option = ctk.CTkComboBox(self, values=["Vídeo (MP4)", "Áudio (MP3)"])
        self.format_option.set("Vídeo (MP4)")
        self.format_option.pack(pady=5)

        # 4. Botão
        self.download_btn = ctk.CTkButton(self, text="Baixar Agora", command=self.iniciar_download)
        self.download_btn.pack(pady=20)

        # 5. Barra de Progresso
        self.progress_bar = ctk.CTkProgressBar(self, width=450)
        self.progress_bar.set(0) # Começa zerada
        self.progress_bar.pack(pady=10)

        # 6. Status
        self.status_label = ctk.CTkLabel(self, text="Pronto para uso", text_color="gray")
        self.status_label.pack(pady=5)

    def iniciar_download(self):
        link = self.url_entry.get()
        if not link:
            self.status_label.configure(text="Erro: Link vazio!", text_color="red")
            return
        
        # Prepara a interface
        self.download_btn.configure(state="disabled", text="Processando...")
        self.progress_bar.set(0)
        self.status_label.configure(text="Iniciando...", text_color="white")
        
        # Inicia a thread
        threading.Thread(target=self._download_logic, args=(link,)).start()

    def _download_logic(self, link):
        try:
            opcao = self.format_option.get()
            
            # Opções do yt-dlp
            ydl_opts = {
                'outtmpl': 'Downloads/%(title)s.%(ext)s',
                'progress_hooks': [self.hook_progresso], # Chama a função da barra
                'quiet': True,
                'no_warnings': True,
            }

            # Configura MP3 ou MP4
            if "Áudio" in opcao:
                ydl_opts['format'] = 'bestaudio/best'
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            else:
                ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'

            if not os.path.exists('Downloads'):
                os.makedirs('Downloads')

            # Executa o download
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

            # Finalização Sucesso
            self.status_label.configure(text="Download Concluído com Sucesso!", text_color="#2CC985") # Verde Matrix
            self.progress_bar.set(1)
            
        except Exception as e:
            self.status_label.configure(text="Erro no Download (Verifique o Link)", text_color="red")
            print(e) # Imprime erro no terminal para debug
        
        finally:
            self.download_btn.configure(state="normal", text="Baixar Novamente")

    def hook_progresso(self, d):
        # Essa função roda centenas de vezes durante o download
        if d['status'] == 'downloading':
            try:
                # Pega a porcentagem do texto (ex: " 45.5% " -> 0.455)
                p_str = d.get('_percent_str', '0%').replace('%','').strip()
                progresso = float(p_str) / 100
                
                self.progress_bar.set(progresso)
                self.status_label.configure(text=f"Baixando: {p_str}%", text_color="white")
            except:
                pass

if __name__ == "__main__":
    app = YouTubeManager()
    app.mainloop()