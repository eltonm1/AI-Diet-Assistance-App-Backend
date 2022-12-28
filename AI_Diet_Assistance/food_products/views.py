from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodProducts
from .serializer import FoodProductsSerializer
# Create your views here.


class FoodProductsViewList(APIView):
    # permission_classes = [HasGroupPermission]
    # permission_classes = [IsAdminUser]
    def get(self, request):
        mahjongSessions = FoodProducts.objects.all().order_by('name')
        serializer_context = {
            'request': request,
        }
        mahjongSessions = FoodProductsSerializer(mahjongSessions, context=serializer_context, many=True)
        # print(mahjongSessions.data)
        return Response(mahjongSessions.data)
        
    # def post(self, request):
    #     print(request.data)
    #     serializer = MahjongSessionPostSerializer(data=request.data)
        
    #     if serializer.is_valid(raise_exception=False):
    #         serializer.save()
    #         print(serializer.data)
    #         return Response(serializer.data)
    #     print(serializer.errors)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
