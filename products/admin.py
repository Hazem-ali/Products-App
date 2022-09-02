from django.contrib import admin

from . import models
# Register your models here.

# makes userprofile accessible on admin interface
admin.site.register(models.UserProfile)
admin.site.register(models.Order)
admin.site.register(models.Cart)
admin.site.register(models.Product)
# admin.site.register(models.OrderProduct)
