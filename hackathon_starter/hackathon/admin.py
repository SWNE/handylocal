from django.contrib import admin
from hackathon.models import UserProfile, Profile, Merchant, MerchantProfile, Area, Neighbourhood

# Register your models here.
class TwitterProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'twitter_user')


admin.site.register(UserProfile)
admin.site.register(Profile)
admin.site.register(MerchantProfile)
admin.site.register(Merchant)
admin.site.register(Area)
admin.site.register(Neighbourhood)