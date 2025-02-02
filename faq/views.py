from rest_framework import generics
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer
import json
import os 
import sys

class FAQListCreateView(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        """Fetch FAQs based on requested language and apply caching."""
        lang = self.request.query_params.get('lang', 'en')  # Default to English
        cache_key = f'faqs_{lang}'
        
        print(f"🔍 Checking Cache for Key: {cache_key}")
        cached_faqs = cache.get(cache_key)

        if cached_faqs:
            print(f"✅ Serving from Redis Cache: {cache_key}")
            return json.loads(cached_faqs)  
        
        print(f"⚠️ Fetching from Database, Storing in Redis: {cache_key}")
        faqs = FAQ.objects.all()

        # 🔥 Apply language filter
        formatted_faqs = []
        for faq in faqs:
            if lang == 'hi':
                formatted_faqs.append({
                    "id": faq.id,
                    "question": faq.question_hi or faq.question, 
                    "answer": faq.answer_hi or faq.answer,
                    "language": "hi"
                })
            elif lang == 'bn':
                formatted_faqs.append({
                    "id": faq.id,
                    "question": faq.question_bn or faq.question, 
                    "answer": faq.answer_bn or faq.answer,
                    "language": "bn"
                })
            else:  # Default English
                formatted_faqs.append({
                    "id": faq.id,
                    "question": faq.question,
                    "answer": faq.answer,
                    "language": "en"
                })

        # Cache filtered FAQs
        cache.set(cache_key, json.dumps(formatted_faqs), timeout=86400)  # Cache for 1 day
        return formatted_faqs

class FAQDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer