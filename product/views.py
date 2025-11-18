from rest_framework import generics
from .models import History, Food, Product, DebtHistory, User,Doc
from .serializers import (
    UserSerializer, FoodSerializer, ProductSerializer,
    HistorySerializer, DebtHistorySerializer,
    DocSerializer,ProductReadSerializer
)

# --------- USER -----------
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#----Doc---
class DocList(generics.ListCreateAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer

class DocCUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer

# --------- FOOD -----------
class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodCUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


# --------- PRODUCT -----------
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer


# --------- HISTORY (kirim/chiqim) ---------
class HistoryList(generics.ListCreateAPIView): 
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class HistoryCUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

# --------- DEBT -----------
class DebtHistoryList(generics.ListCreateAPIView):
    queryset = DebtHistory.objects.all()
    serializer_class = DebtHistorySerializer

class DebtHistoryCUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = DebtHistory.objects.all()
    serializer_class = DebtHistorySerializer
