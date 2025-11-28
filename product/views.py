from rest_framework import generics,filters
from .models import History, Food, Product, DebtHistory, User,Doc
from .serializers import (
    UserSerializer, FoodSerializer, ProductSerializer,
    HistorySerializer, DebtHistorySerializer,
    DocSerializer,ProductReadSerializer
)

# --------- USER -----------
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class UserCUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

#----Doc---
class DocList(generics.ListCreateAPIView):
    queryset = Doc.objects.all().order_by('-id')
    serializer_class = DocSerializer

class DocCUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doc.objects.all().order_by('-id')
    serializer_class = DocSerializer

# --------- FOOD -----------
class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all().order_by('id')
    serializer_class = FoodSerializer

class FoodCUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all().order_by('id')
    serializer_class = FoodSerializer


# --------- PRODUCT -----------
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class ProductCUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductReadSerializer

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ProductSerializer 
        return ProductReadSerializer 

# --------- HISTORY (kirim/chiqim) ---------
class HistoryList(generics.ListCreateAPIView): 
    queryset = History.objects.all().order_by('-id')
    serializer_class = HistorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["order"]

class HistoryCUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all().order_by('-id')
    serializer_class = HistorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["order"]

# --------- DEBT -----------
class DebtHistoryList(generics.ListCreateAPIView):
    queryset = DebtHistory.objects.all().order_by('-id')
    serializer_class = DebtHistorySerializer

class DebtHistoryCUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = DebtHistory.objects.all().order_by('-id')
    serializer_class = DebtHistorySerializer
    
