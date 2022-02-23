from schematics.models import Model
from schematics.types import URLType, StringType, ListType

class BookItem(Model):
    url = URLType(required=True)
    title = StringType(required=True)
    price = StringType(required=True)