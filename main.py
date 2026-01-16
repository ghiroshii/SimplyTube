import os
import sys
import customtkinter
from pytubefix import YouTube
from pytubefix import Playlist
from tkinter import messagebox
import threading
from pytubefix.helpers import reset_cache
from tkinter import messagebox, filedialog
from customtkinter import CTkImage
from PIL import Image

c5 = '#051d17'
c6 = '#0d0d15'
c7 = '#1d1c28'
c8 = "#343341"


def resource_path(relative_path: str) -> str:

    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# Imagens
download_image = customtkinter.CTkImage(
    dark_image=Image.open(resource_path("Assets/download.png")), size=(30, 30))

file_image = customtkinter.CTkImage(
    dark_image=Image.open(resource_path("Assets/file.png")), size=(30, 30))

reload_image = customtkinter.CTkImage(
    dark_image=Image.open(resource_path("Assets/reload.png")), size=(30, 30))

iconapp_image = customtkinter.CTkImage(
    dark_image=Image.open(resource_path("Assets/iconapp.png")), size=(75, 60))

title_image = customtkinter.CTkImage(
    dark_image=Image.open(resource_path("Assets/title.png")), size=(300, 100))

ytlink_image = customtkinter.CTkImage(
    dark_image=Image.open(resource_path("Assets/ytlink.png")), size=(100, 19))

localsave_image = customtkinter.CTkImage(
    dark_image=Image.open(resource_path("Assets/localsave.png")), size=(80, 19))

mp4_image = customtkinter.CTkImage(
    dark_image=Image.open(resource_path("Assets/mp4.png")), size=(88, 35))

m4a_image = customtkinter.CTkImage(
    dark_image=Image.open(resource_path("Assets/m4a.png")), size=(88, 35))

features_image = customtkinter.CTkImage(
    dark_image=Image.open(resource_path("Assets/features.png")), size=(80, 19))

info_image = customtkinter.CTkImage(
    dark_image=Image.open(resource_path("Assets/info.png")), size=(15, 20))

playlist_image = customtkinter.CTkImage(
    dark_image=Image.open(resource_path("Assets/playlist.png")), size=(85, 23))

version_image = customtkinter.CTkImage(
    dark_image=Image.open(resource_path("Assets/version.png")), size=(88, 19))


class App (customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('800x600')
        self.title('SimplyTube')
        self._set_appearance_mode('dark')
        self.resizable(False, False)
        self.dw_progress = False
        self.interface()
        self.iconbitmap(resource_path("Assets/icon3.ico"))

    def interface(self):
        # // _Interface Frames_ //
        self.left_frame = customtkinter.CTkFrame(
            self, width=130, height=600, corner_radius=5, border_width=2, fg_color=c6)
        self.left_frame.pack(side='left', padx=0, pady=0)

        self.center_frame = customtkinter.CTkFrame(
            self, width=800, height=600, corner_radius=5, border_width=2, fg_color=c6)
        self.center_frame.pack(padx=0, pady=0, anchor='center')

        self.title_image = customtkinter.CTkLabel(
            self.center_frame, image=title_image, text='')
        self.title_image.place(x=330, y=60, anchor='center')

        self.icon_app = customtkinter.CTkLabel(
            self.left_frame, image=iconapp_image, text='', corner_radius=1)
        self.icon_app.place(x=30, y=20)
        # // LEFT FRAME

        self.playlist_label = customtkinter.CTkLabel(
            self.left_frame, image=playlist_image, text='')
        self.playlist_label.place(x=40, y=500)

        self.version_label = customtkinter.CTkLabel(
            self.left_frame, image=version_image, text='')
        self.version_label.place(x=40, y=570)

        self.info_button = customtkinter.CTkButton(
            self.left_frame, text='', fg_color=c7, hover_color=c8, height=10, width=10, border_width=1, image=info_image, command=self.show_info)
        self.info_button.place(x=90, y=569)

        # // _CENTER FRAME_ //

        self.link_label = customtkinter.CTkLabel(
            self.center_frame, text='', image=ytlink_image)
        self. link_label.place(x=325, y=150, anchor='center')

        self.local_label = customtkinter.CTkLabel(
            self.center_frame, text='', image=localsave_image)
        self. local_label.place(x=325, y=240, anchor='center')

        self.link_entry = customtkinter.CTkEntry(self.center_frame, width=400)
        self.link_entry.place(relx=0.5, rely=0.3, anchor='center')

        self.path_entry = customtkinter.CTkEntry(self.center_frame, width=400)
        self.path_entry.place(relx=0.5, rely=0.45, anchor='center')

        self.select_folder_button = customtkinter.CTkButton(
            self.center_frame,
            text='...',
            width=45,
            command=self.select_folder,
            fg_color=c7,
            hover_color=c8
        )
        self.select_folder_button.place(relx=0.85, rely=0.45, anchor='center')

        # __Checkbox__
        self.check_var_mp4 = customtkinter.StringVar(value="on")
        self.check_var_m4a = customtkinter.StringVar(value="off")
        self.check_var_playlist = customtkinter.StringVar(value="off")

        self.mp4_img = customtkinter.CTkLabel(self.center_frame, text='', image=mp4_image)
        self.mp4_img.place(x=245, y=298)
        self.checkbox_mp4 = customtkinter.CTkCheckBox(self.center_frame, fg_color=c7, hover_color=c8, text="", variable=self.check_var_mp4, onvalue="on", offvalue="off", width=20, height=15)
        self.checkbox_mp4.place(x=220, y=300)


        self.m4a_img = customtkinter.CTkLabel(self.center_frame, text='', image=m4a_image)
        self.m4a_img.place(x=370, y=298)
        self.checkbox_m4a = customtkinter.CTkCheckBox(self.center_frame, font=customtkinter.CTkFont(
            family="System"), fg_color=c7, hover_color=c8, text='', variable=self.check_var_m4a, onvalue="on", offvalue="off", width=20, height=15)
        self.checkbox_m4a.place(x=345, y=300)

        self.checkbox_playlist = customtkinter.CTkCheckBox(
            self.left_frame, text='', fg_color=c7, hover_color=c8, variable=self.check_var_playlist, onvalue="on", offvalue="off", width=20, height=20)
        self.checkbox_playlist.place(x=15, y=500)

        self.download_button = customtkinter.CTkButton(
            self.center_frame, fg_color=c7, hover_color=c8, height=50, width=60, border_width=1, image=download_image, text='', command=self.playlist_check)
        self.download_button.place(x=300, y=355)

        self.openfolder_button = customtkinter.CTkButton(
            self.center_frame, text='', fg_color=c7, hover_color=c8, height=50, width=60, border_width=1, image=file_image, command=self.open_folder)
        self.openfolder_button.place(x=220, y=355)

        self.clearcacher_button = customtkinter.CTkButton(
            self.center_frame, text='', fg_color=c7, hover_color=c8, height=50, width=60, border_width=1, image=reload_image, command=self.clear_cache)
        self.clearcacher_button.place(x=380, y=355)

        self.progress_bar = customtkinter.CTkProgressBar(
            self.center_frame, fg_color=c8, progress_color=c7, width=655, height=20)
        self.progress_bar.place(relx=0.011, rely=0.96)
        self.progress_bar.set(0)

        # Status
        self.download_status = customtkinter.CTkLabel(
            self.center_frame, text="Ready to download :) ", text_color='white')
        self.download_status.place(relx=0.49, rely=0.93, anchor="center")
# // INFO

    def show_info(self):
        messagebox.showinfo("Thanks for downloading",
                            "\nCreated by Gabriel Sudo_ \n\ngithub.com/ghiroshii")
# // FOLDER

    def select_folder(self):
        folder_selected = filedialog.askdirectory()

        if folder_selected:
            # Limpa o conteúdo atual
            self.path_entry.delete(0, 'end')
            # Insere o novo caminho selecionado
            self.path_entry.insert(0, folder_selected)

    def open_folder(self):
        # LEMBRETE DE TRABALHAR MELHOR NISSO DEPOIS
        folder_path = self.path_entry.get()

        if os.path.exists(folder_path):
            os.startfile(folder_path)

        else:
            self.select_folder()

    def playlist_check(self):
        if self.check_var_playlist.get() == "on":
            self.download_threading_playlist()

        if self.check_var_playlist.get() == "off":
            self.download_threading()

            
    def clear_cacher(self):
        reset_cache()
        self.download_status.configure(text="Ready to download again :) ")
        messagebox.showinfo(
            "Complete", "The cache was successfully cleared :)")

# // ON PROGRESS

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        self.progress_bar.set(percentage / 100)
        self.download_status.configure(
            text=f"Downloading... {percentage:.1f}%")
        self.update_idletasks()

    def validar(self):
        mylink = self.link_entry.get()
        if not mylink:
            messagebox.showerror("Error", "Please enter a YouTube link")
            return False
        if not mylink.startswith(("https://www.youtube.com/", "https://youtu.be/", "www.youtube.com/",
                                  "https://youtube.com/", "youtube.com/", "youtu.be/", "https://youtube.com/playlist")):
            messagebox.showerror("Error", "Please enter a valid YouTube link")
            return False
        if self.check_var_mp4.get() == "off" and self.check_var_m4a.get() == "off":
            messagebox.showerror(
                "Error", "Select at least one format (MP4 or M4a)")
            return False

        return True

    def download(self):
        try:
            if not self.validar():
                return

            mylink = self.link_entry.get()
            mypath = self.path_entry.get()
            self.dw_progress = True

            if self.check_var_mp4.get() == "on" and self.check_var_m4a.get() == "on":
                # guardar link do youtube primeiro
                self.dw_progress = True
                yt = YouTube(mylink, on_progress_callback=self.on_progress)
                # Mudar status do download, primeiro baixar o mp4 e depois o m4a
                self.download_status.configure(
                    text=f"Downloading MP4: {yt.title}")
                ys = yt.streams.get_highest_resolution()
                ys.download(output_path=mypath)

                # M4A
                self.download_status.configure(
                    text=f"Downloading MPA: {yt.title}")
                ys = yt.streams.get_audio_only()
                ys.download(output_path=mypath)

            elif self.check_var_mp4.get() == "on":
                #
                self.dw_progress = True
                yt = YouTube(mylink, on_progress_callback=self.on_progress)
                self.download_status.configure(
                    text=f"Downloading MP4: {yt.title}")
                ys = yt.streams.get_highest_resolution()
                ys.download(output_path=mypath)
#
            elif self.check_var_m4a.get() == "on":
                yt = YouTube(mylink, on_progress_callback=self.on_progress)
                self.download_status.configure(
                    text=f"Downloading M4A: {yt.title}")
                ys = yt.streams.get_audio_only()
                ys.download(output_path=mypath)

        except Exception as e:
            self.download_status.configure(
                text='An error occurred.')
            messagebox.showerror("Erro", f"An error occurred.: {str(e)}")
            return False
        finally:
            self.dw_progress = False
            self.update_idletasks()
            reset_cache()
        self.dw_progress = False
        self.download_status.configure(text="Complete")

        messagebox.showinfo("Complete", "Download complete")

    def download_threading(self):
        if self.dw_progress:
            return
        thread = threading.Thread(target=self.download)
        thread.daemon = True
        thread.start()

    def clear_cache(self):
        reset_cache()
        mylink = self.link_entry.get()

        if mylink:
            # Limpa o conteúdo atual
            self.link_entry.delete(0, 'end')
            self.download_status.configure(text="Ready to download again :) ")
        messagebox.showinfo(
            "Complete", "The link field and cache have been cleared. :)")

    # // PLAYLIST #

    def on_progress_playlist(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        self.progress_bar.set(percentage / 100)
        self.download_status.configure(
            text=f"Downloading {stream.default_filename[:30]}... {percentage:.1f}%")
        self.update_idletasks()

    # playlist threading
    def download_threading_playlist(self):
        if self.dw_progress:
            return
        thread = threading.Thread(target=self.download_playlist)
        thread.daemon = True
        thread.start()

    def download_playlist(self):
        try:
            if not self.validar():
                return

            mylink = self.link_entry.get()
            mypath = self.path_entry.get()
            self.dw_progress = True

            playlist = Playlist(mylink)
            total_videos = len(playlist.video_urls)

            if total_videos == 0:
                messagebox.showerror(
                    "Error", "No videos found in playlist or playlist is private")
                return

            if self.check_var_mp4.get() == "on" and self.check_var_m4a.get() == "on":
                # Baixar MP4 primeiro
                self.download_status.configure(
                    text=f"Downloading Playlist MP4 ({total_videos} videos)")
                self.update_idletasks()

                for i, video_url in enumerate(playlist.video_urls):
                    try:
                        yt = YouTube(
                            video_url, on_progress_callback=self.on_progress_playlist)
                        self.download_status.configure(
                            text=f"Downloading MP4 {i+1}/{total_videos}: {yt.title[:40]}...")
                        ys = yt.streams.get_highest_resolution()
                        ys.download(output_path=mypath)
                    except Exception as e:
                        print(f"Error downloading video {i+1}: {str(e)}")
                        continue

                # Depois baixar M4A
                self.download_status.configure(
                    text=f"Downloading Playlist M4A ({total_videos} videos)")
                self.update_idletasks()

                for i, video_url in enumerate(playlist.video_urls):
                    try:
                        yt = YouTube(
                            video_url, on_progress_callback=self.on_progress_playlist)
                        self.download_status.configure(
                            text=f"Downloading M4A {i+1}/{total_videos}: {yt.title[:40]}...")
                        ys = yt.streams.get_audio_only()
                        ys.download(output_path=mypath)
                    except Exception as e:
                        print(f"Error downloading audio {i+1}: {str(e)}")
                        continue

            elif self.check_var_mp4.get() == "on":
                self.download_status.configure(
                    text=f"Downloading Playlist MP4 ({total_videos} videos)")
                self.update_idletasks()

                for i, video_url in enumerate(playlist.video_urls):
                    try:
                        yt = YouTube(
                            video_url, on_progress_callback=self.on_progress_playlist)
                        self.download_status.configure(
                            text=f"Downloading MP4 {i+1}/{total_videos}: {yt.title[:40]}...")
                        ys = yt.streams.get_highest_resolution()
                        ys.download(output_path=mypath)
                    except Exception as e:
                        print(f"Error downloading video {i+1}: {str(e)}")
                        continue

            elif self.check_var_m4a.get() == "on":
                self.download_status.configure(
                    text=f"Downloading Playlist M4A ({total_videos} videos)")
                self.update_idletasks()

                for i, video_url in enumerate(playlist.video_urls):
                    try:
                        yt = YouTube(
                            video_url, on_progress_callback=self.on_progress_playlist)
                        self.download_status.configure(
                            text=f"Downloading M4A {i+1}/{total_videos}: {yt.title[:40]}...")
                        ys = yt.streams.get_audio_only()
                        ys.download(output_path=mypath)
                    except Exception as e:
                        print(f"Error downloading audio {i+1}: {str(e)}")
                        continue

        except Exception as e:
            self.download_status.configure(text='An error occurred.')
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            return False
        finally:
            self.dw_progress = False
            self.update_idletasks()
            reset_cache()

        self.download_status.configure(text="Complete")
        messagebox.showinfo("Complete", "Playlist download complete")

app = App()
app.mainloop()
