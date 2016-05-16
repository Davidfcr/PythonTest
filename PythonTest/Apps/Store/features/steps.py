from lettuce import *
from lettuce.django import django_url
from Store.models import stores

@step(u'I go to the "(.*)" URL')
def i_go_to_the_url(step, url):
    world.response = world.browser.visit(django_url(url))

@step(u'I fill in "(.*)" with "(.*)"')
def i_fill_in_name(step, field, value):
    world.browser.fill(field, value)

@step(u'I fill in "(.*)" with "(.*)"')
def i_fill_in_address(step, field, value):
    world.browser.fill(field, value)

@step(u'I press "(.*)" button')
def i_press_in_send(step, field, value):
    world.browser.press(field, value)

@step(u'I have the following data to be inserted:')
def stores_in_database(step):
    for stores_dict in step.hashes:
        store = stores(**stores_dict)
        store.save()
