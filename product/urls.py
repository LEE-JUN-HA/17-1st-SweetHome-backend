from django.urls import path

from .views import ProductView, ProductDetailView, ProductReviewView, CategoryView, ReviewLikeView, ProductCartView

urlpatterns = [
    path('', ProductView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/<int:product_id>/review', ProductReviewView.as_view()),
    path('/<int:product_id>/review-like', ReviewLikeView.as_view()),
    path('/cart', ProductCartView.as_view()),
    path('/category', CategoryView.as_view()),
]
