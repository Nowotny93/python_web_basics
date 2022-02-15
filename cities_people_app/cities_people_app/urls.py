from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include('untitled1.cities.urls')),
    path('', include('untitled1.people.urls'))

    # path ('cities/', index)
    # path ('cities/phones', list_phones)
]
