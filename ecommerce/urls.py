#criar urls
#primeira coisa: o projeto, o ecommerce
#segunda coisa: as APIS -> elas podem ter suas próprias urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')) #eu incluo a url da pasta API (api.urls)
] #toda vez que eu digitar api/ ele vai lá para a pasta api e vai procurar o arquivo urls.py
