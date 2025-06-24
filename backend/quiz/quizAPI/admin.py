from django.contrib import admin
from . import models
from django.contrib.admin.widgets import AdminTextareaWidget


# Instead of showing an <input type="text"> HTML element show a <textare> element
# Since it allows us to write multiple lines of markdown
class CardAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):  # type: ignore[reportIncomptaibleMethodOverride]
        if db_field.name in ["front", "back"]:
            kwargs["widget"] = AdminTextareaWidget
        return super().formfield_for_dbfield(db_field, **kwargs)


admin.site.register(models.Quiz)
admin.site.register(models.QuizDetails)
admin.site.register(models.Card, CardAdmin)
