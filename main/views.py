import json
from .models import *
import glob
from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse
from django.template import Context, Template
from django.core.paginator import Paginator


LANGUAGES = {
    "en": "English",
    "ar": "Arabian",
    "bg": "Bulgarian",
    "cs": "Czech",
    "nl": "Dutch",
    "de": "German",
    "el": "Greek",
    "es": "Spanish",
    "fi": "Finnish",
    "fr": "French",
    "hr": "Croatian",
    "it": "Italian",
    "he": "Hebrew",
    "ja": "Japan",
    "ko": "Korean",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "nl": "Dutch",
    "no": "Norwegian",
    "pl": "Polish",
    "pt": "Portuguese ",
    "ro": "Romanian",
    "sr": "Serbian",
    "sv": "Swedish",
    "th": "Thai",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "et": "Estonian",
    "sk": "Slovak",
}


def fill_database(request):
    Page.objects.all().delete()
    # languages = tuple(LANGUAGES.keys())
    # file = open(r"C:\Users\user\Desktop\Sites\sources\ru_data.json", "r")
    # data = json.load(file)
    # for page in data:
    #     page_for_save = Page(
    #         title=page.get("title"),
    #         categories=page.get("categories"),
    #         description=page.get("description"),
    #         keywords=page.get("keywords"),
    #         content=page.get("content"),
    #         image=page.get("image"),
    #         images=page.get("images"),
    #         language=page.get("language"),
    #     )
    #     page_for_save.save()
    # file.close()
    for index, lang_code in enumerate(LANGUAGES):
        file = open(fr"C:\Users\user\Desktop\Sites\sources\data\{lang_code}_data.json", "r")
        data = json.load(file)
        for page in data:
            page_for_save = Page(
                title=page.get("title"),
                categories=page.get("categories"),
                description=page.get("description"),
                keywords=page.get("keywords"),
                content=page.get("content"),
                image=page.get("image"),
                images=page.get("images"),
                language=page.get("language"),
            )
            page_for_save.save()
        file.close()
        if index == 4: break
    return HttpResponse("Всё норм")


class IndexView(generic.TemplateView):
    template_name = "main/languages.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["languages"] = LANGUAGES
        return context


class PageListView(generic.ListView):
    model = Page
    # paginate_by = 15
    def get_context_data(self, **kwargs):
        context = super(PageListView, self).get_context_data(**kwargs)
        page = Paginator(Page.objects.filter(language=self.kwargs["language_code"]), 15)
        context["page_list"] = page.page(self.request.GET.get("page", 1))
        print(self.request.GET.get("page", 1))
        if page:
            context["is_paginated"] = 1
        else:
            context["is_paginated"] = 0
        context["page_obj"] = page.get_page(self.request.GET.get("page", 1))
        context["language"] = self.kwargs["language_code"]

        return context


class PageDetailView(generic.DetailView):
    model = Page

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        context["images"] = (
            self.object.images.replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .split(", ")
        )
        return context
