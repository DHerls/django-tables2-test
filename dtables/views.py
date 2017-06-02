# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django_tables2 import SingleTableMixin

from dtables.models import Person
from dtables.tables import TestTable


class TestView(SingleTableMixin, TemplateView):

    template_name = "test.html"
    table_data = Person.objects.all().order_by("name")
    table_class = TestTable
