from django.http import JsonResponse
from .models import FAQ
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json


def FAQViewSet(request):
    lang = request.GET.get('lang', 'en')
    faqs = [faq.get_translation(lang) for faq in FAQ.objects.all()]
    return JsonResponse(faqs, safe=False)


def faq_list(request):
    lang = request.GET.get('lang', 'en')
    faqs = [faq.get_translation(lang) for faq in FAQ.objects.all()]
    return JsonResponse(faqs, safe=False)


def faq_detail(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    lang = request.GET.get('lang', 'en')
    return JsonResponse(faq.get_translation(lang))


@csrf_exempt
def faq_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question = data.get('question')
        answer = data.get('answer')

        if not question or not answer:
            return JsonResponse(
                                {"error": "Both question and answer are required."},
                                status=400
                                )

        faq = FAQ.objects.create(question=question, answer=answer)
        return JsonResponse({"message": "FAQ created successfully!", "qid": faq.qid},
                            status=201)


@csrf_exempt
def faq_update(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)

    if request.method == 'PUT':
        data = json.loads(request.body)
        faq.question = data.get("question", faq.question)
        faq.answer = data.get("answer", faq.answer)
        faq.save()
        return JsonResponse({"message": "FAQ updated successfully!"},
                            status=200)


@csrf_exempt
def faq_delete(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)

    if request.method == 'DELETE':
        faq.delete()
        return JsonResponse({"message": "FAQ deleted successfully!"},
                            status=204)
