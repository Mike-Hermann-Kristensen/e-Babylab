import os
from django.conf import settings
from django.http import FileResponse, Http404

def serve_report(request, filename):
    file_path = os.path.join(settings.REPORTS_ROOT, filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True)
    raise Http404("Report not found")
