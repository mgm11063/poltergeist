from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer


class Search(APIView):
    def get(self, request):
        search_word = request.query_params.get("search")
        all_products = Product.objects.filter(
            name__contains=search_word
        )  # __contains 단어포함
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data)
