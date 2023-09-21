from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer


class Search(APIView):
    ### 통합검색기능으로 만들어야함 serializer를 만들어서 여러 모델 데이터 정규화 필요 ###

    def search_product(self, request):
        search_word = request.query_params.get("search")
        return Product.objects.filter(name__contains=search_word)  # __contains 단어포함

    def get(self, request):
        serializer = ProductSerializer(self.search_product(request), many=True)
        return Response(serializer.data)
