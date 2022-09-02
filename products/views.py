from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status  # HTTP STATUSES
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

# Login Authentication imports
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# is auth or read only
from rest_framework.permissions import IsAuthenticated


# to be able to search well
from rest_framework import filters

from . import serializers, models
# from courses_app import permissions


class RegisterView(APIView):

    # guarantees the form of data inside
    serializer_class = serializers.UserProfileSerializer
    def post(self, request):
        """Register a new account"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            serializer.create(serializer.validated_data)

            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class UserLoginApiView(ObtainAuthToken):
    """handle creating auth tokens for user"""

    # ADD renderer to obtainauthtoken to be able to view it
    # it existed by default in modelviewset but not here
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProductViewSet(viewsets.ModelViewSet):
    """Handling Course List"""

    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all().order_by('price')

    # searching
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    
class OrderViewSet(viewsets.ModelViewSet):
    """Handling Course List"""

    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()

    # searching
    filter_backends = (filters.SearchFilter,)
    search_fields = ('product',)
    

class CartViewSet(viewsets.ModelViewSet):
    """Handling Course List"""

    serializer_class = serializers.CartSerializer
    queryset = models.Cart.objects.all()


    # searching
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user', 'created_on')
    
