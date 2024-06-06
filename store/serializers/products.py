from rest_framework import serializers
from rest_framework.status import *
from store.models import ProductDetails, Products

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'
    
    def create(self, validated_data):
        product_detail_dict = validated_data.pop('product_details', {})
        product_obj = Products(**validated_data)
        product_detail_list = []
        if product_detail_dict:
            for product_detail in product_detail_dict:
                product_detail_list.append(
                    ProductDetails(product=product_obj, **product_detail)
                )
            
            ProductDetails.objects.bulk_create(objs=product_detail_list)

            product_obj.save()
        else:
            raise serializers.ValidationError('Enter at least one item!!', code=HTTP_404_NOT_FOUND)
        

        return {}

# class Products(models.Model):
#     name = models.CharField(max_length=50)
#     descreption = models.TextField(max_length=200)
#     product_type = models.IntegerField(choices=ProductTypes.choices)
#     brand_type = models.IntegerField(choices=BrandTypes.choices)


# class ProductDeatils(models.Model):
#     product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_details')
#     name = models.CharField(max_length=50)
#     sku = models.CharField(max_length=100)
#     qr_code = models.IntegerField(max_length=10)
#     quantity = models.DecimalField(max_digits=8, decimal_places=3, default=0)
#     price = models.DecimalField(max_digits=8, decimal_places=3, default=0)
#     quality_type = models.IntegerField(choices=QualityType.choices, default=QualityType.COPY)
#     description = models.CharField(max_length=400)


# class Brand(models.Model):
#     name = models.CharField(max_length=50)
#     priority = models.IntegerField(max_length=50, default=0)
