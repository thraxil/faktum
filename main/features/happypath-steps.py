from lettuce import world, step


@step(u'there is an add fact form')
def there_is_an_add_fact_form(step):
    assert len(world.dom.cssselect("form.add-fact")) > 0
