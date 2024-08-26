from django.contrib import admin

from main.models import SupplierNetwork, Product


@admin.register(SupplierNetwork)
class SupplierNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'supplier', 'debt_to_supplier', 'created_at')
    list_filter = ('city',)
    search_fields = ('name', 'city', 'email')

    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        """
        Функция обновляет поле 'debt_to_supplier' для выбранных объектов и
        отображает сообщение о количестве обновленных объектов.
        """
        updated_count = queryset.update(debt_to_supplier=0.00)
        self.message_user(request, f'Задолженность очищена для {updated_count} объектов.')

    clear_debt.short_description = "Очистить задолженность перед поставщиком"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'network')
    search_fields = ('name', 'model')
    list_filter = ('network', 'release_date')
    ordering = ('release_date',)
