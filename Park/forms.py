from django import forms
from .models import Gas, Car, Maintenance


class CarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pasport_date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'dd-mm-yyyy',
                'class': 'form-control', 'style': 'width:200px'
            }
        )
        self.fields['registration_date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'dd-mm-yyyy',
                'class': 'form-control', 'style': 'width:200px'
            }
        )
        self.fields['mark'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['mark'].label = 'Марка и модель'
        self.fields['type'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['type'].label = 'Тип'
        self.fields['organization'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['organization'].label = 'Организация'
        self.fields['photo'].widget.attrs['style'] = 'width:300px; height: 30px'
        self.fields['photo'].label = 'Фото'
        self.fields['registration_number'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['registration_number'].label = 'Рег.Номер'
        self.fields['registration_date'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['registration_date'].label = 'Дата регистрации'
        self.fields['start_mileage'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['start_mileage'].label = 'Начальный пробег'
        self.fields['current_mileage'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['current_mileage'].label = 'Текущий пробег'
        self.fields['VIN'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['board_number'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['board_number'].label = 'Номер кузова'
        self.fields['passport_number'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['passport_number'].label = 'Номер тех.паспорта'
        self.fields['pasport_date'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['pasport_date'].label = 'Дата выдачи тех.паспорта'
        self.fields['board_color'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['board_color'].label = 'Цвет кузова'
        self.fields['year'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['year'].label = 'Год выпуска'
    class Meta:
        model = Car
        fields = '__all__'


class GasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_g'].widget = forms.widgets.DateInput(

            attrs={
                'type': 'date', 'placeholder': 'dd-mm-yyyy',
                'class': 'form-control', 'style': 'width:200px'
            }
        )
        self.fields['gas_type'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['Car_g'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['date_g'].label = 'Дата'
        self.fields['Car_g'].label = 'Авто'
        self.fields['gas_type'].label = 'Вид топлива'
        self.fields['RBF'].label = 'Остаток'
        self.fields['ammount'].label = 'Количество'
        self.fields['price'].label = 'Цена за л.'


    class Meta:
        model = Gas
        fields = "__all__"


class MaintenceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_m'].widget = forms.widgets.DateInput(

            attrs={
                'type': 'date', 'placeholder': 'dd-mm-yyyy',
                'class': 'form-control', 'style': 'width:200px'
            }
        )
        self.fields['description'].widget = forms.widgets.Textarea(

        )
        self.fields['Car_m'].widget.attrs['style'] = 'width:200px; height: 30px'
        self.fields['Car_m'].label = 'Авто'
        self.fields['date_m'].label = 'Дата'
        self.fields['type_m'].label = 'Вид ТО'
        self.fields['millage'].label = 'пробег'
        self.fields['spare_parts'].label = 'Запчасти'
        self.fields['description'].label = 'Доп.Информация'
        self.fields['price_of_work'].label = 'Цена работы'
        self.fields['price_of_spare_parts'].label = 'Цена запчастей'
        self.fields['file'].label = 'Акт/Счёт'

    class Meta:
        model = Maintenance
        fields = '__all__'