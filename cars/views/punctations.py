from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cars.serializers.punctations import PunctationCreateSerializer
from cars.models.punctation import Punctation


class PunctationsViewSet(ModelViewSet):
    serializer_class = PunctationCreateSerializer
    queryset = Punctation.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
