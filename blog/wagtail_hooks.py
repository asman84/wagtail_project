
from wagtail.contrib.modeladmin.options import modeladmin_register, ModelAdmin

from blog.models import BlogPage


class BlogPageModelAdmin(ModelAdmin):
    model = BlogPage
    menu_label = 'BlogPage'  # ditch this to use verbose_name_plural from model
    menu_icon = 'user'  # change as required
    list_display = ('id', 'intro', 'body', 'date' )
    list_filter = ('id', )
    search_fields = ('id',)


modeladmin_register(BlogPageModelAdmin)
