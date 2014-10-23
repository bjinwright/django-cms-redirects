from cms.forms import PageSelectFormField
from cms.models import Page

class PageField(models.ForeignKey):
    default_form_class = PageSelectFormField
    default_model_class = Page

    def formfield(self, **kwargs):
        defaults = {
            'form_class': self.default_form_class,
        }
        defaults.update(kwargs)
        return super(PageField, self).formfield(**defaults)

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.related.ForeignKey"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)
