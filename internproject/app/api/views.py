from rest_framework import viewsets
from app.api.serializers import SimpleFormSerializer
from app.models import SimpleForm
class apiview(viewsets.ModelViewSet):
    queryset=SimpleForm.objects.all()
    serializer_class=SimpleFormSerializer