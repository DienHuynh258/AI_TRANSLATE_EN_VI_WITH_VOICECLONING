from django.shortcuts import render
from .models import Post  # Import model Post
from .services import transcribe_audio_with_whisper
from django.http import JsonResponse
# Create your views here.
# core/views.py

def index(request):
    return render(request, 'core/index.html')

def speech_to_text(request):
    return render(request, 'core/speech_to_text.html')

def transcript(request):
    return render(request, 'core/transcript.html')

def index(request):
    # Lấy tất cả các đối tượng Post từ database
    # Nhờ có 'ordering' trong Model, chúng đã được sắp xếp sẵn
    posts = Post.objects.all()

    # Tạo một dictionary để truyền dữ liệu sang template
    context = {
        'posts': posts
    }

    # Render template và truyền context vào
    return render(request, 'core/index.html', context)


# ... các view khác ...

def transcribe_view(request):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        language = request.POST.get('language', 'vi')  # lấy language từ FormData
        transcribed_text = transcribe_audio_with_whisper(
            request.FILES['audio_file'], 
            language=language
        )
        return JsonResponse({'text': transcribed_text})
    return JsonResponse({'error': 'Invalid request'}, status=400)