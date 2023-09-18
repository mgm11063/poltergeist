from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Product
from .serializers import ProductSerializer


class Products(APIView):
    def get(self, request):
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_submit_data = request.data
        serializer = ProductSerializer(user_submit_data)
        if serializer.is_valid():
            new_product = serializer.save()
            return Response(ProductSerializer(new_product).data)
        else:
            return Response(serializer.errors)


class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        serializer = ProductSerializer(self.get_object(pk=pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = ProductSerializer(
            self.get_object(pk, data=request.data, partial=True)
        )
        if serializer.is_valid():
            updated_product = serializer.save()
            return Response(updated_product).data

    def delete(self, pk):
        self.get_object(pk).delete()


# dawonsaranghae
