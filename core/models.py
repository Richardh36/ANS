from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin import edit_handlers as panels
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class ANSPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    intro = models.TextField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        panels.FieldPanel('intro'),
    ]


    is_abstract = True

    class Meta:
        abstract = True


class HomePage(ANSPage):
    def get_contact_page(self):
        return ContactPage.objects.live().child_of(self).first()

    parent_page_types = []


class ContactPage(ANSPage):
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=254)

    parent_page_types = [HomePage]

    content_panels = ANSPage.content_panels + [
        panels.FieldPanel('phone_number'),
        panels.FieldPanel('email_address'),
    ]


class StandardPage(ANSPage):
    pass


class ProductIndexPage(Page):
    parent_page_types = [HomePage]


class ProductPage(Page):
    parent_page_types = [ProductIndexPage]
