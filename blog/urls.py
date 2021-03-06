from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from posts import views
from posts.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    AboutListView,
    Privacy_policyListView,
    Terms_of_useListView,
    ContactView,
    like,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', PostListView.as_view(), name='list'),
    path('about/', AboutListView.as_view(), name='about'),
    path('privacy_policy/', Privacy_policyListView.as_view(), name='privacy_policy'),
    path('terms_of_use/', Terms_of_useListView.as_view(), name='terms_of_use'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<slug>/', PostDetailView.as_view(), name='detail'),
    path('<slug>/update/', PostUpdateView.as_view(), name='update'),
    path('<slug>/delete/', PostDeleteView.as_view(), name='delete'),
    path('like/<slug>/', like, name='like'),
    path('_ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)