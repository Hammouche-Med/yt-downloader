from pytube import YouTube
from pytube.cli import on_progress
from simple_term_menu import TerminalMenu
import datetime
import os

v_link = input("gimme deh link:   ")


try:
    video = YouTube(v_link, on_progress_callback=on_progress )
    print("Title: ",video.title,"|| Number of views: ","{:,}".format(video.views), "|| Duration: ",str(datetime.timedelta(seconds=video.length)),"min")
    
    def main():
        global options
        global menu_entry_index

        options = ["video", "audio"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

    if __name__ == "__main__":
        main()

    if options[menu_entry_index] == "video":
        stream = video.streams.get_highest_resolution()
        print("Downlaoding...")
        stream.download("./video")
        print("Downlaoding Finished")

    elif options[menu_entry_index] == "audio" :
        stream = video.streams.get_audio_only()
        print(stream)
        print("Downlaoding...")
        audio_file = stream.download("./audio")
        base, ext = os.path.splitext(audio_file)
        audio_file_mp3 = base + '.mp3'
        os.rename(audio_file, audio_file_mp3)
        print("Downlaoding Finished")

except:
    print("An error occurred")





    