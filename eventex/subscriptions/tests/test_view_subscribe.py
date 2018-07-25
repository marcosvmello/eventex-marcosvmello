from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """" Get /inscricao/ must return ststus code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        #""" Must use subscriptions/subscription_form.html """
        response = self.client.get('/inscricao/')
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """ Html must contain input tags"""
        tags = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="email"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text', 3)
        self.assertContains(self.resp, 'type="email')
        self.assertContains(self.resp, 'type="submit"')


    def test_csrd(self):
        """" Html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='12345678901',
                    email='henrique@bastos.net', phone='21-99618-6180')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """Valid POST should redirect to /inscricao/ """
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

class SubscribePostInvalid(TestCase):

    def setUp(self):
        self.resp = self.client.post('inscricao', {})

    def test_post(self):
        """ Invalid Post should not redirect"""
        response = self.client.post('/inscricao/', {})
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

class SubscribeSuccesMessage(TestCase):
    def test_message(self):
        data =dict(name='Henrique Bastos', cpf='12345678901',
                   email='henrique@bastos.net', phone='21-99618-6180')

        response = self.client.post('/inscricao/', data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso!')