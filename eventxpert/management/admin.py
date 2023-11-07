from django.contrib import admin
from .models import TestModel,Category,OrganisationEvent,EventRegistration
# Register your models here.

admin.site.register(TestModel)
admin.site.register(Category)
admin.site.register(OrganisationEvent)
admin.site.register(EventRegistration)


