from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Sample data
songs = [
    {"id": 1, "title": "Song 1", "artist": "Artist 1"},
    {"id": 2, "title": "Song 2", "artist": "Artist 2"},
    {"id": 3, "title": "Song 3", "artist": "Artist 3"}
]

@csrf_exempt
def get_songs(request):
    return JsonResponse(songs, safe=False)

@csrf_exempt
def add_song(request):
    if request.method == 'POST':
        new_song = {
            "id": len(songs) + 1,
            "title": request.POST.get('title'),
            "artist": request.POST.get('artist')
        }
        songs.append(new_song)
        return JsonResponse(new_song, status=201)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)

# Django URLs configuration
from django.urls import path

urlpatterns = [
    path('songs', get_songs),
    path('songs/add', add_song),
]
