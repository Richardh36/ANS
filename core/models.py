from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin import edit_handlers as panels


class HomePage(Page):
    hero_title = models.CharField(max_length=255)
    hero_text = models.TextField(max_length=255)

    def get_contact_page(self):
        return ContactPage.objects.live().child_of(self).first()

    parent_page_types = []

    content_panels = Page.content_panels + [
        panels.FieldPanel('hero_title'),
        panels.FieldPanel('hero_text'),
    ]


class ContactPage(Page):
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=254)

    parent_page_types = [HomePage]

    content_panels = Page.content_panels + [
        panels.FieldPanel('phone_number'),
        panels.FieldPanel('email_address'),
    ]
