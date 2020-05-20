from django.contrib import admin
from .models import (
    Designer,
    DimensionalPrinter,
    PersonalInfo,

)


admin.site.register(Designer)
admin.site.register(DimensionalPrinter)
admin.site.register(PersonalInfo)

