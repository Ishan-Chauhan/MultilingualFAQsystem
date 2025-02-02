from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from bs4 import BeautifulSoup
from django.core.cache import cache


class FAQ(models.Model):
    qid = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = RichTextField()

    def get_translation(self, lang):
        cache_key_question = f"qfaq_{self.qid}_lang_{lang}"
        cache_key_answer = f"afaq_{self.qid}_lang_{lang}"
        cached_translation_question = cache.get(cache_key_question)
        cached_translation_answer = cache.get(cache_key_answer)

        if cached_translation_question and cached_translation_answer:
            # print("from cache")
            return {"question": cached_translation_question,
                    "answer": cached_translation_answer}

        if lang == "en":
            return {"question": self.question, "answer": self.answer}

        def translate_html(html):
            soup = BeautifulSoup(html, "html.parser")

            for text_node in soup.find_all(text=True):
                if text_node.strip():
                    try:
                        translated_text = translator.translate(text_node, dest=lang).text
                        text_node.replace_with(translated_text)
                    except Exception:
                        return html

            return str(soup)

        translator = Translator()
        try:
            translated_question = translator.translate(self.question, dest=lang).text
        except Exception:
            translated_question = self.question
        translated_answer = translate_html(self.answer)

        cache.set(cache_key_question, translated_question, timeout=60*60)
        cache.set(cache_key_answer, translated_answer, timeout=60*60)

        return {"question": translated_question, "answer": translated_answer}

    def __str__(self):
        return self.question
