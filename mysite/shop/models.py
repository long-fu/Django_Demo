from django.db import models

# Create your models here.
class Shop(models.Model):
    c_shop_name = models.CharField("店铺名称",max_length=128)
    c_address = models.CharField("店铺位置",max_length=256)
    c_location = models.CharField("店铺位置",max_length=256)
    i_type = models.IntegerField("店铺类型")
    c_pay_qr_code = models.CharField("店铺支付二维码",max_length=512)
    c_description = models.CharField("店铺描述",max_length=1024)
    c_images = models.CharField("店铺图片", max_length=1024)
    d_create_time = models.DateTimeField("店铺创建时间")

    def __str__(self):
        return self.c_shop_name
