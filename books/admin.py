from django.contrib import admin

from dockit.admin.documentadmin import DocumentAdmin
#from dockit.admin.views import SchemaFieldView, SchemaListFieldView

from models import Book, Publisher, Author, Address, ComplexObject, SubComplexOne, SubComplexTwo

class BookAdmin(DocumentAdmin):
    list_display = ('title', 'authors_list', 'publisher', 'year')

    def authors_list(self, obj):
        return ', '.join([unicode(author) for author in obj.authors])

class PublisherAdmin(DocumentAdmin):
    list_display = ('name', 'city_and_region')

    def city_and_region(self, obj):
        return obj.address.city + ', ' + obj.address.region

class AuthorAdmin(DocumentAdmin):
    list_display = ('internal_id', 'user')

admin.site.register([Book], BookAdmin)
admin.site.register([Publisher], PublisherAdmin)
admin.site.register([Author], AuthorAdmin)

class ComplexObjectAdmin(DocumentAdmin):
    pass

admin.site.register([ComplexObject], ComplexObjectAdmin)


import hyperadmin
from dockitresource.resources import DocumentResource

class BookResource(DocumentResource):
    list_display = ('title', 'authors_list', 'publisher', 'year')

    def authors_list(self, obj):
        return ', '.join([unicode(author) for author in obj.authors])

class PublisherResource(DocumentResource):
    list_display = ('name', 'city_and_region')

    def city_and_region(self, obj):
        return obj.address.city + ', ' + obj.address.region

class AuthorResource(DocumentResource):
    list_display = ('internal_id', 'user')

hyperadmin.site.register(Book, BookResource, app_name='books')
hyperadmin.site.register(Publisher, PublisherResource, app_name='books')
hyperadmin.site.register(Author, AuthorResource, app_name='books')

class ComplexObjectResource(DocumentResource):
    pass

hyperadmin.site.register(ComplexObject, ComplexObjectResource, app_name='books')
