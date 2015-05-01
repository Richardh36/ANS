from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin import edit_handlers as panels
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class HomePage(Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    hero_title = models.CharField(max_length=255, blank=True)
    hero_text = models.TextField(max_length=255, blank=True)

    def get_contact_page(self):
        return ContactPage.objects.live().child_of(self).first()

    parent_page_types = []

    content_panels = Page.content_panels + [
        ImageChooserPanel('hero_image'),
        panels.FieldPanel('hero_title'),
        panels.FieldPanel('hero_text'),
    ]


class ContactPage(Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=254)

    parent_page_types = [HomePage]

    content_panels = Page.content_panels + [
        ImageChooserPanel('hero_image'),
        panels.FieldPanel('phone_number'),
        panels.FieldPanel('email_address'),
    ]


class StandardPage(Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    intro = models.TextField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('hero_image'),
        panels.FieldPanel('intro'),
    ]


class ProductIndexPage(Page):
    parent_page_types = [HomePage]
