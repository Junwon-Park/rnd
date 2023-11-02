

import torch
# from pororo import Pororo
import whisper

def getText(request):
    print("getText")
    print(torch.__version__)
    # print(Pororo.available_tasks())
    #
    # asr = Pororo(task='asr', lang='ko')
    # print(asr('../audio/ko_read_ko2.mp3'))
    model = whisper.load_model("base")
    result = model.transcribe("audio.wav")
    print(result)