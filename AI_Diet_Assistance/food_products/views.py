from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodProduct, ProductPrice
from .serializer import FoodProductsSerializer, FoodProductsPostSerializer
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.db.models import Prefetch
from datetime import datetime, timedelta
import pytz

class FoodProductsViewList(APIView):
    # permission_classes = [HasGroupPermission]
    # permission_classes = [IsAdminUser]
    # @method_decorator(cache_page(10*1))
    # def get(self, request):
    #     foodProducts = FoodProduct.objects.all().order_by('name')
    #     serializer_context = {
    #         'request': request,
    #     }
    #     foodProducts = FoodProductsSerializer(foodProducts, context=serializer_context, many=True)

    #     return Response(foodProducts.data)
    @method_decorator(cache_page(10*1))
    def get(self, request, bcode=None):
        if bcode is None:
            timelimit = datetime.now(pytz.UTC) - timedelta(days=5)
            prefetch = Prefetch("product_price", queryset=ProductPrice.objects.filter(date__gte=timelimit).order_by('-date'))
            foodProducts = FoodProduct.objects.prefetch_related(prefetch).order_by('name').all()
            serializer_context = {
                'request': request,
            }
            foodProducts = FoodProductsSerializer(foodProducts, context=serializer_context, many=True)

            return Response(foodProducts.data)
        else:
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
