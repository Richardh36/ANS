from wagtail.wagtailcore import blocks


BASIC_BLOCKS = (
    ('heading', blocks.CharBlock(template='core/blocks/heading.html')),
    ('paragraph', blocks.TextBlock(template='core/blocks/paragraph.html')),
)
