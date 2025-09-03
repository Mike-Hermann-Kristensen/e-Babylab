import os
from django.conf import settings
from django.http import FileResponse, Http404

def serve_upload(request, path):
    full_path = os.path.join(settings.MEDIA_ROOT, 'uploads', path)
    if os.path.exists(full_path) and os.path.isfile(full_path):
        return FileResponse(open(full_path, 'rb'))
    raise Http404("Not found")

