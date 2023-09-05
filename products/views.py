from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_202_ACCEPTED
from .models import Product
from .serializers import ProductSerializer


@api_view(["GET", "POST"])
def products(request):
    if request.method == "GET":
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response(
            {
                "ok": True,
                "products": serializer.data,
            }
        )
    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            new_product = serializer.save()
            return Response(
                ProductSerializer(new_product).data,
            )
        else:
            return Response(serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise NotFound

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ProductSerializer(
            product,
            data=request.data,
            partial=True,  # 데이터가 완벽하지 않을 수 도 있음을 정의
        )
        if serializer.is_valid():
            updated_product = serializer.save()
            return Response(ProductSerializer(updated_product).data)
        else:
            return Response(serializer.errors)

    elif request.method == "DELETE":
        product.delete()
        return Response(HTTP_202_ACCEPTED)
