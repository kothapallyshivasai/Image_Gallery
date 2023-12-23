from django.contrib import admin
from .models import Image, Comments, Deleted_Comments
# Register your models here.


# admin.site.register(Image)
admin.site.register(Comments)
admin.site.register(Deleted_Comments)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'user', 'caption', 'visible', 'username_visible', 'private')
    list_filter = ('visible', 'username_visible', 'private', 'user__username')
    search_fields = ('caption', 'user__username')

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        try:
            user_id = int(search_term)
            queryset |= self.model.objects.filter(user__id=user_id)
        except ValueError:
            pass

        return queryset, use_distinct