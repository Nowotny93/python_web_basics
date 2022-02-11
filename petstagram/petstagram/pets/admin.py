from django.contrib import admin

from petstagram.pets.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'age')
    list_filter = ('type', 'age')

    def likes_count(self, obj):
        return obj.like_set.count()


admin.site.register(Pet, PetAdmin)
