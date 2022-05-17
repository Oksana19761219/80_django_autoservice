from django.db import models



class Model(models.Model):
    car_brand = models.CharField(
        'car brand',
        max_length=100,
        null=False,
        help_text='Enter car brand (for example, Toyota)'
    )
    car_model = models.CharField(
        'car model',
        max_length=100,
        null=False,
        help_text='Enter car model (for example, Corolla)'
    )
    year = models.IntegerField(
        'year',
        null=True,
        help_text='Enter car production year'
    )

    def __repr__(self):
        return f'{self.car_brand}, {self.car_model}'


class Car(models.Model):
    number = models.CharField(
        'number',
        max_length=10,
        null=False,
        help_text='Enter car number'
    )
    model_id = models.ForeignKey(
        Model,
        on_delete=models.CASCADE,
        null=False
    )
    vin_number = models.CharField(
        'VIN number',
        max_length=17,
        null=False,
        help_text='17 symbols <a href="https://www.autodna.com/vin-number">VIN number</a>'
    )
    client = models.CharField(
        'client',
        max_length=250,
        null=False,
        help_text='Enter client name'
    )
    def __repr__(self):
        return f'{self.number}, {self.vin_number}, {self.client}'


class Order(models.Model):
    data = models.DateField(
        'order data',
        null=False,
        blank=False
    )
    car_id = models.ForeignKey(
        Car,
        null=False,
        on_delete=models.CASCADE,
    )
    # amount = models.FloatField(
    #     'amount',
    #     null=False,
    #     help_text='enter order amount'
    # )

    def __repr__(self):
        return f'{self.car_id}, {self.data}'


class Service(models.Model):
    name = models.CharField(
        max_length=100,
        default='1',
        help_text='Service name'
    )
    price = models.FloatField(
        'price',
        null=False,
        help_text='service price'
    )

    def __repr__(self):
        return f'{self.name}, {self.price}'


class OrderLine(models.Model):
    service_id = models.ForeignKey(
        Service,
        null=False,
        on_delete=models.CASCADE,
    )
    order_id = models.ForeignKey(
        Order,
        null=False,
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(
        'quantity',
        null=False,
        help_text='service quantity'
    )

    def __repr__(self):
        return f'{self.service_id}, {self.order_id}, {self.quantity}'