from import_export import resources
from .models import Foods


class ReportResource(resources.ModelResource):
    class Meta:
        model = Foods
