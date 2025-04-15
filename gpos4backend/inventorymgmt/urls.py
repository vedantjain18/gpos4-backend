from django.urls import path
from .views import home, StockRegisterApi, PhysicalStockTakingPendingApi, PriceTagsPrintingApi, ItemMasterApi, CompanyApi, ItemBrandApi, ItemCategoryApi, ItemGroupApi, ItemSubGroupApi, OpeningStockApi, ItemIngredientsMasterApi, StockManipulationTypeApi, StockManipulationApi, ItemBarcodeApi

urlpatterns = [
    path('', home, name='home'),
    path('stock-register-all/', StockRegisterApi.as_view(), name='stock-register-all'),
    path('physical-stock-taking-pending/', PhysicalStockTakingPendingApi.as_view(), name='physical-stock-taking-pending'),
    path('price-tags-printing/', PriceTagsPrintingApi.as_view(), name='price-tags-printing'),
    path('item-master/', ItemMasterApi.as_view(), name='item-master'),
    path('company/', CompanyApi.as_view(), name='company'),
    path('item-brand/', ItemBrandApi.as_view(), name='item-brand'),
    path('item-category/', ItemCategoryApi.as_view(), name='item-category'),
    path('item-group/', ItemGroupApi.as_view(), name='item-group'),
    path('item-sub-group/', ItemSubGroupApi.as_view(), name='item-sub-group'),
    path('opening-stock/', OpeningStockApi.as_view(), name='opening-stock'),
    path('item-ingredients-master/', ItemIngredientsMasterApi.as_view(), name='item-ingredients-master'),
    path('stock-manipulation-type/', StockManipulationTypeApi.as_view(), name='stock-manipulation-type'),
    path('stock-manipulation/', StockManipulationApi.as_view(), name='stock-manipulation'),
    path('item-barcode/', ItemBarcodeApi.as_view(), name='item-barcode'),
]