from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodProduct
from .serializer import FoodProductsSerializer, FoodProductsPostSerializer
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class FoodProductsViewList(APIView):
    # permission_classes = [HasGroupPermission]
    # permission_classes = [IsAdminUser]
    @method_decorator(cache_page(10*1))
    def get(self, request):
        foodProducts = FoodProduct.objects.all().order_by('name')
        serializer_context = {
            'request': request,
        }
        foodProducts = FoodProductsSerializer(foodProducts, context=serializer_context, many=True)

        return Response(foodProducts.data)
    
    def get(self, request, bcode):
        foodProducts = FoodProduct.objects.get(barcode=bcode)
        serializer_context = {
            'request': request,
        }
        foodProducts = FoodProductsSerializer(foodProducts, context=serializer_context, many=False)

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

    def put(self, request, pk):
        print(request.data)
        food_product = FoodProduct.objects.get(id=pk)
        serializer = FoodProductsPostSerializer(instance=food_product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            print(serializer.data)
            return Response(FoodProductsSerializer(food_product, many=False, context={"request": request}).data)#serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
