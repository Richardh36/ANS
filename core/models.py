from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin import edit_handlers as panels
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from core.blocks import BASIC_BLOCKS


class ANSPage(Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
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
    parent_page_types = []

    def get_contact_page(self):
        return ContactPage.objects.live().child_of(self).first()

    def get_context(self, request):
        context = super().get_context(request)
        context['products'] = ProductPage.objects.live()[:3]

        return context


class ContactPage(ANSPage):
    company_name = models.CharField(max_length=100)
    line1 = models.CharField("First line", max_length=50)
    line2 = models.CharField("Second line", max_length=50, blank=True)
    town = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=254)

    parent_page_types = [HomePage]

    content_panels = ANSPage.content_panels + [
        panels.MultiFieldPanel([
            panels.FieldPanel('company_name'),
            panels.FieldPanel('line1'),
            panels.FieldPanel('line2'),
            panels.FieldPanel('town'),
            panels.FieldPanel('county'),
            panels.FieldPanel('postcode'),
            panels.FieldPanel('country'),
        ], "Address"),
        panels.FieldPanel('phone_number'),
        panels.FieldPanel('email_address'),
    ]


class StandardPage(ANSPage):
    body = StreamField(BASIC_BLOCKS, blank=True)

    content_panels = ANSPage.content_panels + [
        panels.StreamFieldPanel('body'),
    ]


class ProductIndexPage(ANSPage):
    parent_page_types = [HomePage]

    def get_context(self, request):
        context = super().get_context(request)
        context['products'] = ProductPage.objects.live()

        return context


class ProductPage(ANSPage):
    body = StreamField(BASIC_BLOCKS, blank=True)

    content_panels = ANSPage.content_panels + [
        panels.StreamFieldPanel('body'),
    ]

    parent_page_types = [ProductIndexPage]
