from lettuce.django import django_url
from lettuce import before, after, world, step
from django.test import client
from lxml import html

@step(u'there is an add fact form')
def there_is_an_add_fact_form(step):
    assert len(world.dom.cssselect("form.add-fact")) > 0


