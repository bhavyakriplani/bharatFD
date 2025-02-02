from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
import time

class FAQ(models.Model):
    language_choices = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    ]
    
    question = models.TextField()
    answer = RichTextField()
    language = models.CharField(max_length=2, choices=language_choices, default='en')

    # Translated fields
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def translate_content(self):
        """Translate content and store in respective fields."""
        translator = Translator()
        print(f"🔵 Translating: {self.question}")

        try:
            if not self.question_hi:
                self.question_hi = translator.translate(self.question, src='en', dest='hi').text
                print(f"✅ Translated Question (hi): {self.question_hi}")
                time.sleep(1)

            if not self.question_bn:
                self.question_bn = translator.translate(self.question, src='en', dest='bn').text
                print(f"✅ Translated Question (bn): {self.question_bn}")
                time.sleep(1)

            if not self.answer_hi:
                self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text
                print(f"✅ Translated Answer (hi): {self.answer_hi}")
                time.sleep(1)

            if not self.answer_bn:
                self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text
                print(f"✅ Translated Answer (bn): {self.answer_bn}")
                time.sleep(1)

        except Exception as e:
            print(f"❌ Translation Error: {e}")

    def save(self, *args, **kwargs):
        """Automatically translate FAQ content when saved."""
        if not self.question_hi or not self.question_bn or not self.answer_hi or not self.answer_bn:
            self.translate_content()
        super().save(*args, **kwargs)