from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Candidatedirectory)

admin.site.register(Persona)
admin.site.register(Maritalstatus)
admin.site.register(Educationinstitution)
admin.site.register(Educationlevel)
admin.site.register(Educationqualification)
admin.site.register(Educationspecialization)
admin.site.register(Employeedirectory)
admin.site.register(Experiencelevel)
admin.site.register(Eventdetails)
admin.site.register(Jobposition)
admin.site.register(Jobrequisition)
admin.site.register(Screeningmode)
admin.site.register(Gender)
admin.site.register(City)
admin.site.register(Source)
admin.site.register(Sourcetype)
admin.site.register(Reasonforchange)