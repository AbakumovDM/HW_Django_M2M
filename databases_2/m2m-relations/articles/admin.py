from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Chapter, ArticleChapter

class ChapterInlineFormset(BaseInlineFormSet):
    def clean(self):
        base_chapter_count = 0
        for form in self.forms:
            base_chapter_count += form.cleaned_data['basechapter']
        if base_chapter_count != 1:
            raise ValidationError('Основной раздел только один')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ChapterInLine(admin.TabularInline):
    model = ArticleChapter
    formset = ChapterInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ChapterInLine]

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['text']

@admin.register(ArticleChapter)
class ArticleChapterAdmin(admin.ModelAdmin):
    list_display = ['article', 'chapter']