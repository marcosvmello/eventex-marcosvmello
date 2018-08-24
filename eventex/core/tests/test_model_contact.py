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
