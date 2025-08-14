from django.contrib import admin
from .models import Emp, Testimonial

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','emp_id')
    list_editable=('working',)
    search_fields=('emp_id',)
    list_filter=('working',)

admin.site.register(Emp, EmpAdmin)
admin.site.register(Testimonial)
