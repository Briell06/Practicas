from django.contrib import admin

from .models import (
    Comment,
    Company,
    Item,
)

# Register your models here.

admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel"
admin.site.index_title = "Welcome to the Admin Panel"


admin.site.register(Item)
admin.site.register(Company)
admin.site.register(Comment)
