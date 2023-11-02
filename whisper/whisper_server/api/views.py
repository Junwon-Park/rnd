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
    fs = FileSystemStorage(location="audio/")
    saved_file = fs.save(file.name, file)

    print("Request", request)
    print("Request", request.FILES['audio'])

    model = whisper.load_model("base")
    result = model.transcribe("audio/" + str(saved_file), fp16=False)

    return Response(result["text"])