from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodProduct
from .serializer import FoodProductsSerializer, FoodProductsPostSerializer
# Create your views here.


class FoodProductsViewList(APIView):
    # permission_classes = [HasGroupPermission]
    # permission_classes = [IsAdminUser]
    def get(self, request):
        foodProducts = FoodProduct.objects.all().order_by('name')
        serializer_context = {
            'request': request,
        }
        foodProducts = FoodProductsSerializer(foodProducts, context=serializer_context, many=True)

        return Response(foodProducts.data)
        
    def post(self, request):
        print(request.data)
        serializer = FoodProductsPostSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
