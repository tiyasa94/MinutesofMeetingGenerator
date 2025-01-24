from moviepy.video.io.VideoFileClip import VideoFileClip
# from moviepy.editor import VideoFileClip
import torch
import whisper
import os

device = "cuda:0" if torch.cuda.is_available() else "cpu"
print('Device using: ',device)
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
model = whisper.load_model("large-v3", device=device)


def video_to_text(video_path):

    '''Video to Text Generation.'''
    
    video=VideoFileClip(video_path)
    ap = os.path.join(os.getcwd(), 'output', 'audio_file.mp3')
    if os.path.exists(ap):
        os.remove(ap)
    video.audio.write_audiofile(ap)
    result = model.transcribe(ap)
    texts = result['text']

    tp = os.path.join(os.getcwd(), 'output', 'transcript.txt')
    with open(tp, 'w') as f:
        f.write(texts)
    return "Complete",tp