from django.contrib import admin
from .models import News
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(News)
class UserAdmin(admin.ModelAdmin):
    model = News
    list_display = ('id', 'title', 'publication_date', 'author',)
    list_display_links = ('id', 'title')
    ordering = ()
    filter_horizontal = ()
    list_filter = ()
    search_fields = ()
    readonly_fields = ['publication_date', 'author']
    fieldsets = (
        (News, {
            "fields": (
                'title',
                'content',
                'publication_date',
                'author',
            ),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()