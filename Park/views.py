import pandas as pd
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView,UpdateView, DeleteView
from .models import Car, Gas, Maintenance, Organisation, CarMark
from .admin import CarResource, GasResource, MaintenceResource
from .forms import CarForm, GasForm, MaintenceForm
from django.shortcuts import render


class MaiCreateView(CreateView):
    model = Maintenance
    form_class = MaintenceForm
    template_name = 'add_maintence.html'
    # success_url = reverse_lazy('listofcars')

    def get_success_url(self):
        carid = self.request.POST['Car_m']
        return reverse_lazy('car_info', kwargs={'pk': carid})


class GasCreateView(CreateView):
    model = Gas
    form_class = GasForm
    template_name = 'add_gas.html'
    # success_url = reverse_lazy('listofcars')

    def get_success_url(self):
        carid = self.request.POST['Car_g']
        return reverse_lazy('car_info', kwargs={'pk': carid})


class CarCreateView(CreateView):
    form_class = CarForm
    template_name = 'add_car.html'
    success_url = reverse_lazy('listofcars')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mark']= CarMark.objects.all()
        return context



class CarsListView(ListView):
    model = Car
    template_name = 'main.html'
    context_object_name = 'cars'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_info.html'
    context_object_name = 'car_inf'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gas"] = Gas.objects.filter(Car_g=self.object.id)
        context['maintance'] = Maintenance.objects.filter(Car_m=self.object.id)

        return context


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'UpdateCar.html'
    success_url = reverse_lazy('listofcars')

    def get_success_url(self):
        Carid = self.kwargs['pk']
        return reverse_lazy('car_info', kwargs={'pk': Carid})


class GasDeleteView(DeleteView):
    model = Gas

    def get_success_url(self):
        gasid = self.kwargs['pk']
        carid = Car.objects.get(gas__id=gasid)
        return reverse_lazy('car_info', kwargs={'pk': carid.id})


class MaiDeleteView(DeleteView):
    model = Maintenance

    def get_success_url(self):
        maiid = self.kwargs['pk']
        carid = Car.objects.get(maintenance__id=maiid)
        return reverse_lazy('car_info', kwargs={'pk': carid.id})


def export_xlsx(request, pk):
    selects = request.POST.get('select_value')
    datasetCar = CarResource().export()
    ds = pd.read_excel(datasetCar.xlsx)
    for i in range(0, len(datasetCar)):
        if i != pk - 1:
            ds = ds.drop(i, axis=0)
    ds.at[pk-1, 'organization'] = Organisation.objects.get(id=ds.at[pk-1, 'organization']).name
    ds.at[pk-1, 'mark'] = CarMark.objects.get(id=ds.at[pk-1, 'mark']).name + ' ' + CarMark.objects.get(
        id=ds.at[pk-1, 'mark']).model
    datasetGas = GasResource().export()
    ds_gas = pd.read_excel(datasetGas.xlsx)
    for i in range(0, len(datasetGas)):
        if ds_gas.at[i, 'Car_g'] != pk:
            ds_gas = ds_gas.drop(i, axis=0)
    ds_gas = ds_gas.drop(labels=['Car_g'], axis=1)
    datasetMaintence = MaintenceResource().export()
    ds_maintence = pd.read_excel(datasetMaintence.xlsx)
    for i in range(0, len(datasetMaintence)):
        if ds_maintence.at[i, 'Car_m'] != pk:
            ds_maintence = ds_maintence.drop(i, axis=0)
    ds_maintence = ds_maintence.drop(labels=['Car_m'], axis=1)
    data_file = open('XLSX_DATA.XLS', "wb")
    if selects == 'Car':
        pd.DataFrame.to_excel(ds, excel_writer=data_file)
        name = 'Info_of_car'+': '+ds.at[pk-1, 'registration_number']
    elif selects == 'Maintence':
        pd.DataFrame.to_excel(ds_maintence, excel_writer=data_file)
        name = 'TO_of_car'+': '+ds.at[pk-1, 'registration_number']
    elif selects == 'Gas':
        pd.DataFrame.to_excel(ds_gas, excel_writer=data_file)
        name = 'Gas_of_car' +': ' + ds.at[pk-1, 'registration_number']
    else:
        df1 = ds
        df2 = ds_maintence
        df3 = ds_gas
        df = pd.concat([df1, df2, df3])
        pd.DataFrame.to_excel(df, excel_writer=data_file)
        name = 'Full_info_of_car'+': '+ds.at[pk-1, 'registration_number']
    data_file.close()
    with open('XLSX_DATA.XLS', 'rb') as f:
        file_data = f.read()
    response = HttpResponse(file_data, content_type='application/csv')
    response['Content-Disposition'] = ('attachment; filename="%s.xls"' % name)
    return response



def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)