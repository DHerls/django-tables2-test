import django_tables2 as tables
import sys

from dtables.models import Person


class TestTable(tables.Table):

    name = tables.Column()
    age = tables.Column()

    def before_render(self, request):
        self.columns.hide('name')
        print >>sys.stderr, "BEFORE RENDER"

    class Meta:
        model = Person
        fields = ('name', 'age')