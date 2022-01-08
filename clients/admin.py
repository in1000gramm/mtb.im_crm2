from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Client

#admin.site.register(Client)

# Клиенты
class ClientAdmin(admin.ModelAdmin):
    list_display = ('c_name', 'c_surname', 'c_email', 'c_phone', 'c_birthday', 'get_small_image',)
    list_display_links = ('c_name', 'c_surname')
    search_fields = ('c_name', 'c_surname', 'c_email', 'c_phone',)
    list_filter = ('c_birthday',)
    list_editable = ('c_phone',)
    fileds = ('c_image',)
    readonly_fields =  ('get_image',)
    list_per_page = 20
    list_max_show_all = 60

# подключение внешнего класса
#    @admin.register(Book)
#    class BookAdmin(admin.ModelAdmin):
#        list_display = ('title', 'author', 'display_genre')
#        inlines = [BooksInstanceInline]

# вывод мини картинки в списке клиентов
    def get_small_image(self, obj):
        if obj.c_image:
            return mark_safe(f'<a href="{obj.c_image.url}"><img src="{obj.c_image.url}" height="40px"></a>')
        else:
            return 'нет картинки'

# вывод картинки в карточке клиента
    def get_image(self, obj):
        if obj.c_image:
            return mark_safe(f'<a href="{obj.c_image.url}"><img src="{obj.c_image.url}" height="180px"></a>')
        else:
            return 'нет картинки'

    get_image.short_description = 'Фото'
    get_small_image.short_description = 'Фото'

# Register the admin class with the associated model
admin.site.register(Client, ClientAdmin)
