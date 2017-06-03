from django.conf.urls import url
from core.views import almaty, detail
urlpatterns = [
    url(r'^$', almaty),
    url(r'(?P<product_id>[0-9]+)/', detail, name='product_detail')
]
