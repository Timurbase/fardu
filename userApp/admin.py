from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from userApp.models import Xodim


class XodimAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Info", {"fields":("first_name", "last_name", "email", "unvoni", "tel", "lavozim", "logo", "bio")})
    )
    list_display = ("username", "lavozim", "tel")

admin.site.register(Xodim, XodimAdmin)
