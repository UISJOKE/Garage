from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .ajax import companydeleteitem
from .views import page_not_found_view,CarDetailView,CarUpdateView, CarsListView,MaiDeleteView, GasCreateView,GasDeleteView, CarCreateView, MaiCreateView, export_xlsx

urlpatterns = [
                  path('car/<int:pk>/', CarDetailView.as_view(), name='car_info'),
                  path('car/export/<int:pk>', export_xlsx, name='export'),
                  path('', CarsListView.as_view(), name='listofcars'),
                  path('car/add/', CarCreateView.as_view(), name='add_car'),
                  path('gas/add/', GasCreateView.as_view(), name='add_gas'),
                  path('maintence/add/', MaiCreateView.as_view(), name='add_m'),
                  path('car/update/<int:pk>', CarUpdateView.as_view(), name='car_update'),
                  path('gas/delete/<int:pk>', GasDeleteView.as_view(), name='delete_gas'),
                  path('/companydeleteitem/', companydeleteitem, name='companydeleteitem')
                  # path('maintence/delete/', delete_maintenance, name='delete_mai'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = page_not_found_view