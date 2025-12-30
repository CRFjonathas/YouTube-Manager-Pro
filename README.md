# 🎬 Nicacio Media Downloader

> Uma aplicação Desktop moderna para download e conversão de vídeos do YouTube, desenvolvida em Python.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blueviolet?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 📄 Sobre o Projeto

O **Nicacio Media Downloader** é uma ferramenta desenvolvida para facilitar o download de materiais de estudo, playlists e tutoriais para visualização offline. Diferente de scripts simples de linha de comando, este projeto oferece uma **Interface Gráfica (GUI)** amigável com tema escuro (Dark Mode).

O principal desafio técnico deste projeto foi implementar **Multithreading** para garantir que a interface não congelasse durante o download (operação de I/O bloqueante), além da integração com processadores de mídia externos (FFmpeg).

### ✨ Funcionalidades
* **Interface Moderna:** Design limpo usando `CustomTkinter`.
* **Dual Mode:** Suporte para baixar Vídeo (MP4) ou extrair apenas o Áudio (MP3).
* **Feedback Visual:** Barra de progresso em tempo real e indicadores de status.
* **Processamento Paralelo:** O download roda em uma thread separada (Worker), mantendo a janela responsiva.
* **Conversão Automática:** Integração com FFmpeg para garantir a melhor qualidade de áudio.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Interface:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
* **Core de Download:** [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* **Manipulação de Sistema:** Bibliotecas `os` e `threading`.

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos
* Python instalado.
* **FFmpeg:** Essencial para a conversão de MP3. O executável `ffmpeg.exe` deve estar na raiz do projeto.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/nome-do-repo.git](https://github.com/SEU-USUARIO/nome-do-repo.git)
   cd nome-do-repo
