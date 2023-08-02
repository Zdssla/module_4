from django.contrib import admin
from .models import Advertisement

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'auction']
    list_filter = ['auction', 'created_at', 'price']
    actions = ['make_auction_as_false', 'make_auction_as_True']
    
    @admin.action(description='Добавить возможность торга')
    def make_auction_as_True(self, request, queryset):
        queryset.update(auction=True)

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

admin.site.register(Advertisement, AdvertisementAdmin)