from django.contrib import admin
from. import models

# Register your models here.
@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','score')


@admin.register(models.Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','date','is_active')


@admin.register(models.Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)


@admin.register(models.ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time')


@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
