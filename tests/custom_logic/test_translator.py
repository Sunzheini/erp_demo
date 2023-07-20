from django.test import TestCase
from erp_demo.custom_logic.custom_logic import translate_to_maimunica

class TranslateToMaimunicaTest(TestCase):
    def test_translate_only_letters(self):
        cyrillic_string = "АБВГД"
        expected_translation = "ABVGD"

        translated_string = translate_to_maimunica(cyrillic_string)

        self.assertEqual(translated_string, expected_translation)

    def test_translate_mixed_string(self):
        mixed_string = "Даниел123"
        expected_translation = "Daniel123"

        translated_string = translate_to_maimunica(mixed_string)

        self.assertEqual(translated_string, expected_translation)
