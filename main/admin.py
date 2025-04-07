from django.contrib import admin

from .models import (
    Comment,
    Company,
    Item,
)

# Register your models here.


admin.site.register(Item)
admin.site.register(Company)
admin.site.register(Comment)
