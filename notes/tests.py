from django.urls import path, include

from .views import NoteList, NoteDetail
# from .views import UploadViewSet

from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'upload', UploadViewSet, basename="upload")

urlpatterns = [
 path('', NoteList.as_view()),
 path('<int:pk>/', NoteDetail.as_view()),
 # path('', include(router.urls)),
]