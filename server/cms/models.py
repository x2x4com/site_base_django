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
        context['sorted_pages'] = pages
        return context

    # 直接返回json
    # def serve(self, request, *args, **kwargs):
    #     return JsonResponse({
    #         'news': self.get_context(request)['sorted_pages'],
    #     })


class ContentPage(Page):
    date = models.DateField(_("release date"))
    intro = models.CharField(_("intro"), max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="图片"),
    ]

    # def serve(self, request, *args, **kwargs):
    #     return JsonResponse({
    #         'title': self.title,
    #         'body': self.body,
    #         'date': self.date,
    #
    #         # Resizes the image to 300px width and gets a URL to it
    #         # 'feed_image': self.feed_image.get_rendition('width-300').url,
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
