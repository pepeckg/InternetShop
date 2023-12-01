from django.contrib import admin
from products.models import Product, Review, Category, HashTag

@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'rate', 'created_date']
    list_editable = ['rate']
    list_filter = ['hashtags']
    list_per_page = 8
    search_fields = ['title', 'content', 'hashtags__title']

    def has_add_permission(self, request):
        return True


admin.site.register(HashTag)
admin.site.register(Review)
admin.site.register(Category)