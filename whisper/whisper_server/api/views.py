from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

import torch
import whisper


@api_view(('POST',))
def getText(request):
    print(torch.__version__)

    if request.method != "POST":
        return HttpResponse(status=400)

    file = request.FILES['audio']
    fs = FileSystemStorage(location="audio/") # audio 디렉토리에 저장
    saved_file = fs.save(file.name, file) # 해당 파일 이름으로 위에서 지정한 audio/ 디렉토리에 파일 저장

    print("Request", request)
    print("Request", request.FILES['audio'])

    model = whisper.load_model("base") # base Model 사용
    result = model.transcribe("audio/" + str(saved_file), fp16=False, language="ko")
    # fp16=False 옵션 적용하지 않으면 경고 발생 -> warnings.warn("FP16 is not supported on CPU; using FP32 instead")
    # 옵션으로 언어 지정 가능
    print(result["text"])

    return Response(result["text"])