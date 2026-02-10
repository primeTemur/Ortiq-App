from rest_framework import serializers
from .models import Food, Product, History, DebtHistory, User, Doc,ReturnedProduct


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class DebtHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DebtHistory
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class DocSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Javobda to'liq user ma'lumotlari
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True, source='user'
    )

    class Meta:
        model = Doc
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        request = self.context["request"].data

        status = request.get("status")
        order = request.get("order")

        # Product yaratamiz
        product = Product.objects.create(**validated_data)

        # History yaratamiz
        History.objects.create(
            name=product.food.name,                 # ✔ to‘g‘rilandi
            status=status,
            order=order,
            amount=request.get("amount", 0),
            change_price=request.get("change_price", 0),
            all_price=request.get("all_price", 0),
        )

        return product

    def update(self, instance, validated_data):
        request = self.context["request"].data

        status = request.get("status")
        order = request.get("order")

        # Productni yangilaymiz
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # History yaratamiz
        History.objects.create(
            name=instance.food.name,              
            status=status,
            order=order,
            amount=request.get("amount", 0),
            change_price=request.get("change_price", 0),
            all_price=request.get("all_price", 0),
        )

        return instance
    

class ProductReadSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

    
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'

class ReturnedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnedProduct
        fields = '__all__'