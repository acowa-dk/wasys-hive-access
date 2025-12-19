from django.db import models
from django.conf import settings
import redis

# Create your models here.
class Unit(models.Model):
    gekko_id = models.BigAutoField(primary_key=True)
    sigfox_logger_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    scada_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gps_latitude = models.CharField(max_length=100)
    gps_longitude = models.CharField(max_length=100)
    imei = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    input_type_id = models.IntegerField()

    def __str__(self):
        return self.name if self.name is not None else '' + '; ' + self.ip_address if self.ip_address is not None else '' + '; ' + self.imei if self.imei is not None else '' + ';'

    def unit_type(self):
        match self.input_type_id:
            case 1:
                return 'SCADA STATION'
            case 2:
                return 'GEKKO'
            case 3:
                return 'FIREFLY'
            case 4:
                return 'SPIDER'
            case 5:
                return 'REST API'
            case 6:
                return 'PUMA'
        return ''


    def save(self, *args, **kwargs):
        r = redis.from_url(settings.REDIS_URL)
        r.delete('4g-gekkos')

        super(Unit, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'input_gekko"."gekko'
