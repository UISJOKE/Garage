from django.db import models
from django.contrib.auth.models import AbstractUser


class Organisation(models.Model):
    FORMS = (
        ('ООО', 'ООО'),
        ('ОAО', 'ОAО'),
        ('ИП', 'ИП'),
        ('ЧП', 'ЧП'),
        ('АКБ', 'АКБ'),
        ('ЗАО', 'ЗАО'),
        ('НПО', 'НПО'),
        ('НПП', 'НПП'),
        ('ТОО', 'ТОО'),
        ('ГУП', 'ГУП'),
    )

    ACTIVE = (
        ('Да', 'Да'),
        ('Нет', 'Нет'),
    )

    name = models.CharField(max_length=250)
    form = models.CharField(choices=FORMS, max_length=250, blank=True)
    active = models.CharField(choices=ACTIVE, max_length=250, blank=True)

    def __str__(self):
        return self.form + '"' + self.name + '"'


class CarMark(models.Model):
    name = models.CharField(max_length=250, blank=True)
    model = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name + ' - ' + str(self.model)


class Car(models.Model):
    CLS = (
        ('Легковая', 'Легковая'),
        ('Грузовая', 'Грузовая'),
        ('Прицеп', 'Прицеп'),
    )
    id = models.IntegerField(editable=False, blank=False, null=False, primary_key=True, auto_created=True)
    photo = models.ImageField(blank=True, upload_to='media/car_photo')
    organization = models.ForeignKey(Organisation, blank=True, on_delete=models.CASCADE)
    type = models.CharField(choices=CLS, max_length=250, blank=True)
    mark = models.ForeignKey(CarMark, blank=True, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=8, blank=True)
    start_mileage = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    current_mileage = models.DecimalField(max_digits=15, decimal_places=2,null=True, blank=True)
    VIN = models.CharField(max_length=30, blank=True, null=True)
    board_number = models.CharField(max_length=30, blank=True, null=True)
    passport_number = models.CharField(max_length=30, blank=True, null=True)
    pasport_date = models.DateField(blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    board_color = models.CharField(max_length=15, blank=True)
    year = models.IntegerField(blank=True, null=True)

    def save(self, *args,**kwargs):
        self.current_mileage = self.start_mileage
        super().save(*args,**kwargs)

    def __str__(self):
        return "|" + self.registration_number + "| " + str(self.mark) + " (" + str(self.organization) + ")" + "|" \
            + self.board_color


class Gas(models.Model):
    GAS = (
        ('АИ-80','АИ-80'),
        ('АИ-92', 'АИ-92'),
        ('АИ-95', 'АИ-95'),
        ('АИ-95+', 'АИ-95+'),
        ('АИ-98', 'АИ-98'),
        ('АИ-100', 'АИ-100'),
        ('ДТ', 'ДТ'),
    )
    Car_g = models.ForeignKey(Car, blank=True, on_delete=models.CASCADE)
    date_g = models.DateField(blank=True)
    gas_type = models.CharField(choices=GAS,max_length=25, blank=True)
    RBF = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    ammount = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    summ_g = models.DecimalField(editable=False, max_digits=5, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.summ_g = self.ammount * self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.date_g) + ' ' + self.Car_g.registration_number + " summ: " + str(self.summ_g) + "Br."


class Maintenance(models.Model):
    Car_m = models.ForeignKey(Car, blank=True, on_delete=models.CASCADE)
    date_m = models.DateField(blank=True)
    type_m = models.CharField(max_length=50, blank=True)
    millage = models.IntegerField(blank=True)
    spare_parts = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=1500, blank=True)
    price_of_work = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    price_of_spare_parts = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    summ = models.DecimalField(editable=False,max_digits=10, decimal_places=2, blank=True)
    file = models.FileField(upload_to='media/files', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.summ = self.price_of_work + self.price_of_spare_parts
        if self.Car_m.current_mileage < self.millage:
            self.Car_m.current_mileage = self.millage
            self.Car_m.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return '|' + str(self.Car_m.registration_number) + '| ' + str(self.date_m) + ' ' + str(self.type_m) + ' ' + str(
            self.summ) + 'Br.'


class User(AbstractUser):

    company = models.ForeignKey(Organisation, on_delete=models.CASCADE, blank=True,null=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)



    def __str__(self):
        return self.username + ' | ' + str(self.company)