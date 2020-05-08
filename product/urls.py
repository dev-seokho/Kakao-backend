from django.urls import path

from .views import (
	ProductView,
	HomeView,
	HotImageView,
	NewImageView,
	NewProductView,
	SaleProductView,
	MainSaleProductView,
	ProductInformationView,
	CategoryView,
	SubCategoryView
)


urlpatterns = [
    path('/home', HomeView.as_view()),
    path('', ProductView.as_view()),
    path('/hot', HotImageView.as_view()),
    path('/new', NewImageView.as_view()),
    path('/newProduct', NewProductView.as_view()),
    path('/saleProduct', SaleProductView.as_view()),
    path('/mainSaleProduct', MainSaleProductView.as_view()),
    path('/kind', CategoryView.as_view()),
    path('/<str:products_id>', ProductInformationView.as_view()),
    path('/subCategory/<str:sub_id>', SubCategoryView.as_view()),
]

