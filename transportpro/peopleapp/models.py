from django.db import models


class People(models.Model):
    DISTINATION_LOCATION = [('PN', 'PUNE'), ('BPQ', 'BALLARSHAH'), ('MUM', 'MUMBAI')]
    PAYMENT_MODE = [('ON', 'Online Mode'), ('COD', "CASH ON DELIVERY")]
    people_name = models.CharField(max_length=20)
    distination_location = models.CharField(max_length=10, choices=DISTINATION_LOCATION)
    weight = models.IntegerField()
    price = models.IntegerField()
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE)
