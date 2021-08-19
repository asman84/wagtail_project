from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel, PageChooserPanel, TabbedInterface, ObjectList
from wagtail.contrib.settings.models import BaseSetting
from django.db import models
from wagtail.contrib.settings.registry import register_setting


@register_setting
class SocialMediaSettings(BaseSetting):
    facebook = models.URLField(blank=True, null=True, )
    twitter = models.URLField(blank=True, null=True, )
    instagram = models.URLField(blank=True, null=True, )
    youtube = models.URLField(blank=True, null=True, )

    panels = [

        MultiFieldPanel([
            FieldPanel('facebook'),
            FieldPanel('twitter'),
            FieldPanel('instagram'),
            FieldPanel('youtube'),
        ], heading="Social Media Settings")

    ]

    """
    Для регистрация Base settings:
    1.Add installed apps: 'wagtail.contrib.settings'
    1.Add template context_processor: 'wagtail.contrib.settings.context_processors.settings'


    """

@register_setting
class ImportantPages(BaseSetting):
    donate_page = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL, related_name='+')
    sign_up_page = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        PageChooserPanel('donate_page'),
        PageChooserPanel('sign_up_page'),
    ]


@register_setting
class MySettings(BaseSetting):
    field_1 = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL, related_name='+')

    field_2 = models.ForeignKey(
        'wagtailcore.Page', null=True, on_delete=models.SET_NULL, related_name='+')

    first_tab_panels = [
        FieldPanel('field_1'),
    ]
    second_tab_panels = [
        FieldPanel('field_2'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(first_tab_panels, heading='First tab'),
        ObjectList(second_tab_panels, heading='Second tab'),
    ])