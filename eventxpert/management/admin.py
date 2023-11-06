from django.contrib import admin
from .models import TestModel,Category,OrganisationEvent
# Register your models here.

admin.site.register(TestModel)
admin.site.register(Category)
admin.site.register(OrganisationEvent)


