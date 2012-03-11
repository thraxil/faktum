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
    world.response = world.client.get(django_url(url))
    world.dom = html.fromstring(world.response.content)

@step(u'I am not logged in')
def i_am_not_logged_in(step):
    world.client.logout()

@step(u'I am redirected to a login screen')
def i_am_redirected_to_a_login_screen(step):
    assert len(world.response.redirect_chain) > 0
    (url,status) = world.response.redirect_chain[0]
    assert status == 302, status
    assert "/login/" in url, "URL redirected to was %s" % url
    
@step(u'there is a login form')
def there_is_a_login_form(step):
    assert len(world.dom.cssselect("form.login")) > 0

@step(u'I am logged in')
def i_am_logged_in(step):
    world.client.login(username='testuser',password='test')

@step(u'the page title is "([^"]*)"')
def the_page_title_is(step, title):
    assert world.dom.find(".//title").text == title, world.dom.find(".//title").text

@step(u'there is a login link')
def there_is_a_login_link(step):
    assert len(world.dom.cssselect("a.loginlink")) > 0

@step(u'I click on the login link')
def i_click_on_the_login_link(step):
    link = world.dom.cssselect("a.loginlink")[0].attrib['href']
    world.response = world.client.get(django_url(link),follow=True)
    world.dom = html.fromstring(world.response.content)

@step(u'the text "([^"]*)" is present')
def the_text_is_present(step, text):
    assert text in world.response.content, world.response.content

@step(u'there is no login link')
def there_is_no_login_link(step):
    assert len(world.dom.cssselect("a.loginlink")) == 0

@step(u'there is no logout link')
def there_is_no_logout_link(step):
    assert len(world.dom.cssselect("a.logoutlink")) == 0

@step(u'there is a logout link')
def there_is_a_logout_link(step):
    assert len(world.dom.cssselect("a.logoutlink")) > 0

@step(u'there is a "([^"]*)" form field')
def there_is_a_form_field(step, label):
    labels = world.dom.cssselect("label")
    found = False
    for l in labels:
        if l.text.strip() == label:
            if l.cssselect("input"):
                found = True
    assert found

@step(u'there is a "([^"]*)" textarea')
def there_is_a_textarea(step, label):
    labels = world.dom.cssselect("label")
    found = False
    for l in labels:
        if l.text.strip() == label:
            if l.cssselect("textarea"):
                found = True
    assert found


@step(u'there is a "([^"]*)" submit button')
def there_is_a_group1_submit_button(step, group1):
    assert False, 'This step must be implemented'

