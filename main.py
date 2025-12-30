import customtkinter as ctk
import yt_dlp
import threading
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class YouTubeManager(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Jonathas Media Downloader")
        self.geometry("600x500") # Aumentei um pouco a altura
        self.resizable(False, False)

        self.logo_label = ctk.CTkLabel(self, text="YouTube Manager Pro", font=("Roboto", 24, "bold"))
        self.logo_label.pack(pady=20)

        self.url_entry = ctk.CTkEntry(self, width=450, placeholder_text="Cole o link do vídeo aqui...")
        self.url_entry.pack(pady=10)

        # --- NOVO: Seletor de Formato ---
        self.format_label = ctk.CTkLabel(self, text="Formato:")
        self.format_label.pack(pady=(5, 0))
        self.format_option = ctk.CTkComboBox(self, values=["Vídeo (MP4)", "Áudio (MP3)"])
        self.format_option.set("Vídeo (MP4)")
        self.format_option.pack(pady=5)
        # -------------------------------

        self.download_btn = ctk.CTkButton(self, text="Iniciar Download", command=self.iniciar_download)
        self.download_btn.pack(pady=20)

        # --- NOVO: Barra de Progresso ---
        self.progress_bar = ctk.CTkProgressBar(self, width=450)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)
        # -------------------------------

        self.status_label = ctk.CTkLabel(self, text="Pronto", text_color="gray")
        self.status_label.pack(pady=5)

    def iniciar_download(self):
        link = self.url_entry.get()
        if not link:
            self.status_label.configure(text="Erro: Link vazio!", text_color="red")
            return
        
        self.download_btn.configure(state="disabled", text="Baixando...")
        self.progress_bar.set(0) # Reseta a barra
        
        thread = threading.Thread(target=self._download_logic, args=(link,))
        thread.start()

    def _download_logic(self, link):
        try:
            opcao = self.format_option.get()
            
            # Hook adicionado nas opções
            ydl_opts = {
                'outtmpl': 'Downloads/%(title)s.%(ext)s',
                'progress_hooks': [self.hook_progresso], 
            }

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

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

            self.status_label.configure(text="Download Concluído!", text_color="green")
            self.progress_bar.set(1) # Garante que a barra encha no final
            
        except Exception as e:
            self.status_label.configure(text=f"Erro: {str(e)}", text_color="red")
        
        finally:
            self.download_btn.configure(state="normal", text="Iniciar Download")

    # --- NOVO: Função que atualiza a barra ---
    def hook_progresso(self, d):
        if d['status'] == 'downloading':
            try:
                p = d.get('_percent_str', '0%').replace('%','').strip()
                progresso = float(p) / 100
                self.progress_bar.set(progresso)
                self.status_label.configure(text=f"Baixando: {p}%", text_color="white")
            except:
                pass