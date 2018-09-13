from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Marcos Santos',
            slug='marcos-santos',
            photo='http://encurtador.com.br/zLS13',
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, Kind=Contact.EMAIL,
                                        value='contato@marcosvmello.com.br')

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, Kind=Contact.PHONE,
                                        value='21-123456789')

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should Limited to E or P"""
        contact = Contact(speaker=self.speaker, Kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, Kind=Contact.EMAIL,
                         value='contato@marcosvmello.com.br')
        self.assertEqual('contato@marcosvmello.com.br', str(contact))

class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name = 'Marcos Santos',
            slug = 'marcos-santos',
            photo = 'http://hbn.link/hb-pic'
        )

        s.contact_set.create(Kind=Contact.EMAIL, value='marcos@santos.com')
        s.contact_set.create(Kind=Contact.PHONE, value='21-123456789')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['marcos@santos.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['21-123456789']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
