from django.contrib import admin

from education.models import Education, Degree, Organization

admin.site.register(Education)
admin.site.register(Degree)
admin.site.register(Organization)