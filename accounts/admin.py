from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

""" The final step is to update our admin.py file since the admin is tightly coupled to the default
User model. We will extend the existing UserAdmin class to use our new CustomUser model.
To control which fields are listed, we use list_display. But to actually edit new custom fields,
like age, we must add fieldsets. And to include a new custom field in the section for creating a
new user we rely on add_fieldsets.""" 
# 
# Register your models here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)

# be sure to only have one set of paranetheses not two. 
admin.site.register(CustomUser, CustomUserAdmin)
