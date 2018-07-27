from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Marcos Santos', cpf='12345678901',
                    email='mvmello27@gmail.com', phone='21-12345-6789')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'mvmello27@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Marcos Santos',
            '12345678901',
            'mvmello27@gmail.com',
            '21-12345-6789',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

