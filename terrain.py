from lettuce.django import django_url
from lettuce import before, after, world, step
from django.test import client
from lxml import html

#from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.common.keys import Keys

@before.all
def setup_browser():
    world.client = client.Client()

@step(r'I access the url "(.*)"')
def access_url(step, url):
    response = world.client.get(django_url(url))
    world.dom = html.fromstring(response.content)

@step(u'I am not logged in')
def i_am_not_logged_in(step):
    world.client.logout()

@step(u'I am taken to a login screen')
def i_am_taken_to_a_login_screen(step):
    assert len(world.response.redirect_chain) > 0
    (url,status) = world.response.redirect_chain[0]
    assert status == 302, status
    assert "/login/" in url, "URL redirected to was %s" % url

@step(u'I am logged in')
def i_am_logged_in(step):
    world.client.login(username='testuser',password='test')

@step(u'the page title is "([^"]*)"')
def the_page_title_is(step, title):
    assert world.dom.find(".//title").text == title, world.dom.find(".//title").text

