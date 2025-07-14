import moviepy
# vedio to audio

# tinker --> file location where vdo i there
from tkinter.filedialog import *

vid = askopenfilename()
# this is from tinker module

video = moviepy.editor.VideoFileClip(vid)

aud = video.audio
aud.write_audiofile("demo.mp3")

print("--task completed")