from django.apps import AppConfig

# class AccountConfig(AppConfig):
#     name = 'account'


class RidesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rides'
    # verbose_name = 'Riders'


class MeasurementsConfig(AppConfig):
    # name = 'measurements'
    name = 'rides'
    verbose_name = 'Measurement between 2 locations'




