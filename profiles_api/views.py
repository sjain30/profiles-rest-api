from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a lost of APIViews features"""
        an_apiview = [
            'Use HTTP methods',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handling updating object"""
    
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        """Handling partial updating object"""
    
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Handling deleting object"""
    
        return Response({'method': 'DELETE'})