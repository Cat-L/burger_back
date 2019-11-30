from django.db import models


# Create your models here.

class Order(models.Model):
    ID = models.BigAutoField(primary_key=True)

    Meat = models.IntegerField()
    Cheese = models.IntegerField()
    Salad = models.IntegerField()
    Bacon = models.IntegerField()

    Fee = models.IntegerField()
    Date = models.DateTimeField()
    Note = models.TextField()

    consigneeName = models.CharField(max_length=20)
    consigneeAddress = models.TextField()
    consigneeTel = models.IntegerField()

    def __str__(self):
        return 'Order(ID={},\n  ' \
               'Ingredients:\n Meat={}  Cheese={} Salad={} Bacon={} \n ' \
               'FEE={} Date={} Note={}\n' \
               'consignee information:\n Name={} Address={} Tel={} )'.format(
            self.ID, self.Meat, self.Cheese, self.Salad, self.Bacon, self.Fee, self.Date, self.Note, self.consigneeName,
            self.consigneeAddress, self.consigneeTel)
