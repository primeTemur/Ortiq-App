from rest_framework import serializers
from .models import Food, Product, History, DebtHistory, User, Doc


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
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

        # History uchun faqat status va order
        status = request.get("status")
        order = request.get("order")

        # Faqat status va order ni olib tashlaymiz
        for key in ["status", "order"]:
            validated_data.pop(key, None)

        # Product yaratish (amount, change_price, all_price saqlanadi)
        product = Product.objects.create(**validated_data)

        # History yozish (amount, change_price, all_price History uchun requestdan olinadi)
        History.objects.create(
            product=product,
            status=status,
            order=order,
            amount=request.get("amount", 0),
            change_price=request.get("change_price", 0),
            all_price=request.get("all_price", 0),
        )

        return product

    def update(self, instance, validated_data):
        request = self.context["request"].data

        # History uchun faqat status va order
        status = request.get("status")
        order = request.get("order")

        # Faqat status va order ni olib tashlaymiz
        for key in ["status", "order"]:
            validated_data.pop(key, None)

        # Productni yangilash (amount, change_price, all_price saqlanadi)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # History yozish
        History.objects.create(
            product=instance,
            status=status,
            order=order,
            amount=request.get("amount", 0),
            change_price=request.get("change_price", 0),
            all_price=request.get("all_price", 0),
        )

        return instance
