from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField


class HomePage(Page):
    body = RichTextField(_("body"), blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]


class ContentIndexPage(Page):
    intro = RichTextField(_("intro"), blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        # 将上下文更新为仅包含发布了的博客文章，并以 时间逆序 进行排序
        context = super().get_context(request)
        pages = self.get_children().live().order_by('-first_published_at')
        # context['sorted_pages'] = [{'id': _p.id} for _p in pages]
        # print(pages)
        context['sorted_pages'] = pages
        return context

    # 直接返回json
    # def serve(self, request, *args, **kwargs):
    #     return JsonResponse({
    #         'news': self.get_context(request)['sorted_pages'],
    #     })


class ContentPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ContentPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class ContentPage(Page):
    date = models.DateField(_("release date"))
    intro = models.CharField(_("intro"), max_length=250)
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('related_links', label="Related links"),
        ImageChooserPanel('feed_image'),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('feed_image'),
    ]

    def get_url(self, request=None, current_site=None):
        _url = super().get_url(request=request, current_site=current_site)
        print(_url)
        return _url

    api_fields = [
        APIField('date'),
        APIField('body'),
        APIField('gallery_images'),
        # APIField('gallery_images_thumbnail', serializer=ImageRenditionField('fill-100x100', source='gallery_images')),
    ]

    # def serve(self, request, *args, **kwargs):
    #     return JsonResponse({
    #         'title': self.title,
    #         'body': self.body,
    #         'date': self.date,
    #         # Resizes the image to 300px width and gets a URL to it
    #         # 'gallery_images': self.gallery_images.get_rendition('width-300').url,
    #     })


class ContentPageGalleryImage(Orderable):
    page = ParentalKey(ContentPage, on_delete=models.CASCADE, related_name="gallery_images")
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class ContentPageRelatedLink(Orderable):
    page = ParentalKey(ContentPage, on_delete=models.CASCADE, related_name='related_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]
