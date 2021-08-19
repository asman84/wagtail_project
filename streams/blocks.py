from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = 'streams/title_and_text_block.html'
        icon = 'edit'
        label = 'Title & Text'


class RichTextBlock(blocks.RichTextBlock):
    class Meta:
        template = 'streams/rich_text_block.html'
        icon = 'doc-full'
        label = 'Rich Text Field'


class SimpleRichTextBlock(blocks.RichTextBlock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.features = [
            'bold', 'italic', 'link'
        ]

    class Meta:
        template = 'streams/rich_text_block.html'
        icon = 'doc-full'
        label = 'Simple Rich Text Field'


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('text', blocks.TextBlock(required=True)),
                ('image', ImageChooserBlock(required=True)),
                ('button_page', blocks.PageChooserBlock(required=False)),
                ('button_url', blocks.URLBlock(required=False))
            ]
        )
    )

    class Meta:
        template = 'streams/card_block.html'
        icon = 'placeholder'
        label = 'Card block'


class ServiceBlock(blocks.StructBlock):
    header = blocks.CharBlock(required=True)

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('icon', blocks.TextBlock(required=True)),
                ('card_title', blocks.TextBlock(required=True)),
                ('card_desc', blocks.TextBlock(required=True)),
                ('button_page', blocks.PageChooserBlock(required=True)),
                ('button_url', blocks.URLBlock(required=False))
            ]
        )
    )

    class Meta:
        template = 'streams/service_card.html'
        icon = 'placeholder'
        label = 'Service Card block'