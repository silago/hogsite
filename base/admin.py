from django.contrib import admin
from base.models import BlogEntry, SceneFeature
#from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
#from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from django import forms

#class BlogEntryAdmin(admin.ModelAdmin):
#        pass


class SceneFeatureForm(forms.ModelForm):
    class Meta:
        model = SceneFeature
        widgets = {
            'text' : TinyMCE(attrs={'cols': 100, 'rows': 15}),
        }
        fields = "__all__"

class SceneFeatureAdmin(admin.ModelAdmin):
    form = SceneFeatureForm

class BlogEntryForm(forms.ModelForm):
    class Meta:
        model = BlogEntry
        widgets = {
            'text' : TinyMCE(attrs={'cols': 100, 'rows': 15}),
        }
        fields = "__all__"


class BlogEntryAdmin(admin.ModelAdmin):
    form = BlogEntryForm

admin.site.register(BlogEntry,BlogEntryAdmin)
admin.site.register(SceneFeature,SceneFeatureAdmin)


# Register your models here.

#class PageForm(FlatpageForm):
#    class Meta:
#        model = FlatPage
#        widgets = {
#            'content' : TinyMCE(attrs={'cols': 100, 'rows': 15}),
#        }
#        fields = "__all__"
#
#
#class PageAdmin(FlatPageAdmin):
#    """
#    Page Admin
#    """
#    form = PageForm
#
#admin.site.unregister(FlatPage)
#admin.site.register(FlatPage, PageAdmin)
