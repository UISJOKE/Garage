from django.contrib import admin
from .models import CarMark,Car, Organisation, Gas, Maintenance, User
from django.contrib.auth.admin import UserAdmin
from import_export import resources

admin.site.register(Car)

admin.site.register(CarMark)

admin.site.register(Organisation)

admin.site.register(Gas)

admin.site.register(Maintenance)

admin.site.register(User)


class CarResource(resources.ModelResource):

    class Meta:
        model = Car
        fields = ('id_car','organization', 'type','mark',  'registration_number', 'start_mileage', 'current_mileage', 'VIN', 'board_number', 'passport_number', 'registration_date', 'board_color', 'year' )

class GasResource(resources.ModelResource):

    class Meta:
        model = Gas
        fields = ('Car_g', 'date_g', 'gas_type', 'RBF', 'ammount', 'price', 'summ_g')

class MaintenceResource(resources.ModelResource):

    class Meta:
        model = Maintenance
        fields = ('Car_m', 'date_m', 'type_m', 'millage', 'spare_parts', 'description', 'price_of_work', 'price_of_spare_parts', 'summ')