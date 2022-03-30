from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.ejmp.models import Product
from apps.ejmp.serializers import ProductSerializer, ProductSerializer2
# Create your views here.


class ProductAPIView(APIView):
    
    def get(self, request):
        product = Product.objects.all()
        product_serializer = ProductSerializer(product, many=True)

        return Response(product_serializer.data)

        

@api_view(['GET', 'POST'])
def product_view_all(request):

    if request.method == 'GET':
        product = Product.objects.filter(public=True)
        product_serializer =  ProductSerializer(product, many=True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        product_serializer = ProductSerializer2(data=request.data)
        
        if product_serializer.is_valid():
            product_serializer.save() # Calls the create method of the serializers
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)
            
        else: return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        """
        request.POST, request.FILES -> request.data
        request.GET -> request.query_params
        """


"""
-> PUT, DELETE, GET(retrieve, detail)
"""

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, pk):
    try:
        # queryset
        product = Product.objects.filter(public=True).get(id=pk)

        # if product is None:
        #     raise Product.DoesNotExist('Product matching query does not exist.')

        # get
        if request.method == 'GET':
                product_serializer = ProductSerializer2(product)
                return Response(product_serializer.data, status=status.HTTP_200_OK)

        # update
        if request.method == 'PUT':
            product_serializer = ProductSerializer2(instance=product, data=request.data)

            if product_serializer.is_valid():
                product_serializer.save() # llama al método update del serializer
                return Response(product_serializer.data, status=status.HTTP_200_OK)

        # delete
        if request.method == 'DELETE':
            product.public = False
            product.save()
            return Response({'message_success': 'Product removed successfully'}, status=status.HTTP_204_NO_CONTENT)

    except Product.DoesNotExist as e:
        return Response({"message_error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # except AttributeError  as e:
    #     return Response({"message_error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
