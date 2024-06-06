from django.db import models

class ProductTypes(models.IntegerChoices):
    LCD = 1, 'Lcds'
    PARTS = 2, 'Parts'
    CASES = 3, 'Cases'
    SCREEN_PROTECTOR = 4, 'Screen Protector'
    CABLES = 5, 'Cables'
    CHARGER = 6, 'Charger'
    VAPES = 7, 'Vapes'
    SPEAKER = 8, 'Speaker'
    HEADPHONE = 9, 'Headphone'
    HANDSFREE = 10, 'Handsfree'
    LAPTOP_PARTS = 11, 'Laptop Parts'
    HEATER = 12, 'Heater'
    FAN = 13, 'Fan'
    EXTENTION = 14, 'Extention'
    ADOPTER = 15, 'Adopter'
    HOLDER = 16, 'Holder'
    BATTERY = 17, 'Battery'


class BrandTypes(models.IntegerChoices):
    ANG = 1, 'Ang'
    HOCO = 2, 'Hoco'
    BAKU = 3, 'Baku'
    VENDENS = 4, 'Vendens'
    BUDI = 5, 'Budi'
    SAMSUNG = 6, 'Samsung'
    IPHONE = 7, 'Iphone'
    HUWAI = 8, 'Huwai'
    MOTO = 9, 'Moto'
    NOKIA = 10, 'Nokia'
    SONY = 11, 'Sony'
    LG = 12, 'LG'


class QualityType(models.IntegerChoices):
    ORIGINAL = 1, 'Original'
    COPY = 2, 'Copy'
    SEMI_COPY = 3, 'Semi Copy'
    PREMIUM = 4, 'Premium'
    SEMI_ORIGINAL = 5, 'Semi Original'
    PULL_OUT = 6, 'Pull-Out'
    