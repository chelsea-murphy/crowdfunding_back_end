from django.contrib import admin
from .models import Fundraiser, Pledge

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