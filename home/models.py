from django.db import models
from modelcluster.fields import ParentalKey
from django import forms
from wagtail.core import blocks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from streams.blocks import *


class HomePage(Page):
    template = 'home/home_page_last.html'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['menuitems'] = Page.objects.filter(
            live=True, show_in_menus=True)
        return context

    sub_title = models.CharField(blank=True,null=True, max_length=255)
    body = RichTextField(blank=True)
    head_background_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    content = StreamField(
        [
            # ("title_and_text", TitleAndTextBlock()),
            # ("full_richtext", RichTextBlock()),
            # ("simple_richtext", SimpleRichTextBlock()),
            # ('heading', blocks.CharBlock(form_classname="full title")),
            # ('paragraph', blocks.RichTextBlock()),
            # ('image', ImageChooserBlock()),
            ('services_cards', ServiceBlock()),
            ('cards', CardBlock()),


        ], null=True, blank=True)

    content_panels = Page.content_panels + [

        MultiFieldPanel([

            # FieldPanel('sub_title', classname="full"),
            # FieldPanel('body', classname="full"),
            # ImageChooserPanel('head_background_image'),
            # StreamFieldPanel('content'),
        ], heading="Home page content information"),

        InlinePanel('homepage_images', label="Carousel images"),

    ]


class HomePageGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='homepage_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=110)
    button_page = ParentalKey(Page, on_delete=models.CASCADE, related_name='button_page', blank=True, null=True)
    button_url = models.URLField(blank=True, null=True)
    button_text = models.CharField(max_length=20)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('desc'),
        FieldPanel('button_page'),
        FieldPanel('button_url'),
        FieldPanel('button_text'),
    ]

class SettingsPage(Page):
    template = 'home/settings_page.html'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['menuitems'] = Page.objects.filter(
            live=True, show_in_menus=True)
        return context



    content_panels = Page.content_panels + [

    ]


