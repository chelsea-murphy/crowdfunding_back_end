from django.contrib import admin
from django.contrib import admin
from .models import Fundraiser, Pledge
from django.contrib.auth import get_user_model

User = get_user_model()

# Register Fundraiser
@admin.register(Fundraiser)
class FundraiserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'goal', 'is_open', 'date_created')
    list_filter = ('is_open', 'date_created')
    search_fields = ('title', 'description', 'owner__username')
    ordering = ('-date_created',)

# Register Pledge
@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'fundraiser', 'supporter', 'amount', 'anonymous', 'date_created')
    list_filter = ('anonymous', 'date_created')
    search_fields = ('fundraiser__title', 'supporter__username', 'comment')
    ordering = ('-date_created',)

# Register User (if using custom user model)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)