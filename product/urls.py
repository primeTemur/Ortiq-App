from django.urls import path
from .views import (
    UserList, UserCUD,
    FoodList, FoodCUD,
    ProductList, ProductCUD,
    HistoryList, HistoryCUD,
    DebtHistoryList, DebtHistoryCUD,
    DocList,DocCUD
)

urlpatterns = [
    # User
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserCUD.as_view(), name='user-detail'),

    # Food
    path('foods/', FoodList.as_view(), name='food-list'),
    path('foods/<int:pk>/', FoodCUD.as_view(), name='food-detail'),

    # Product
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductCUD.as_view(), name='product-detail'),

    # History
    path('history/', HistoryList.as_view(), name='history-list'),
    path('history/<int:pk>/', HistoryCUD.as_view(), name='history-detail'),

    # DebtHistory
    path('debt-history/', DebtHistoryList.as_view(), name='debt-history-list'),
    path('debt-history/<int:pk>/', DebtHistoryCUD.as_view(), name='debt-history-detail'),

    path('docs/', DocList.as_view(), name='doc-list'),
    path('docs/<int:pk>/', DocCUD.as_view(), name='doc-detail'),
]
