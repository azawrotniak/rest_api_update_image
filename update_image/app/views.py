from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Image, Person
from .serializers import BasicImageSerializer, PremiumImageSerializer, EnterpriseImageSerializer


class ImageView(APIView):
    def get(self, request, *args, **kwargs):
        serializer_class = BasicImageSerializer
        person = Person.objects.get(user=request.user)

        if person.account.name == 'Premium':
            serializer_class = PremiumImageSerializer
        elif person.account.name == 'Enterprise':
            serializer_class = EnterpriseImageSerializer

        queryset = Image.objects.filter(user=person)
        serializer = serializer_class(queryset, many=True, context={"request":request})

        return Response(serializer.data)


class UploadImageView(viewsets.ModelViewSet):
    serializer_class = {
        'Basic': BasicImageSerializer,
        'Premium': PremiumImageSerializer,
        'Enterprise': EnterpriseImageSerializer
    }
    default_serializer_class = BasicImageSerializer 

    def get_serializer_class(self):
        person = Person.objects.get(user=self.request.user)
        print(person.account.name)
        if person.account.name == 'Premium':
            return PremiumImageSerializer
        elif person.account.name == 'Enterprise':
            return EnterpriseImageSerializer
        return BasicImageSerializer

    def post(self, request):
        person = Person.objects.get(user=request.user)
        if person.account.name == 'Basic':
            serializer = self.serializer_class['Basic'](data = request.data)
        elif person.account.name == 'Premium':
            serializer = self.serializer_class['Premium'](data = request.data)
        elif person.account.name == 'Enterprise':
            serializer = self.serializer_class['Enterprise'](data = request.data)

        if serializer.is_valid():
            serializer.save(user=person)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
