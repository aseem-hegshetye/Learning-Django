from django.contrib import admin
import nested_admin
from .models import *


class LessonAdmin(nested_admin.NestedStackedInline):
    model = Lesson


class SubjectAdmin(nested_admin.NestedStackedInline):
    model = Subject
    inlines = [LessonAdmin]


class GradeAdmin(nested_admin.NestedModelAdmin):
    inlines = [SubjectAdmin]


admin.site.register(Grade, GradeAdmin)
admin.site.register(School)
admin.site.register(Campus)
