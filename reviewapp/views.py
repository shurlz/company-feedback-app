from django.shortcuts import render
from django.http import HttpResponse
from .models import Tags , companyReview
from django.core.cache import cache
from .forms import TagsForm , companyReviewForm
# Create your views here.


def index(request):
    company_filter = request.GET.get('company')
    tag_filter = request.GET.get('tag')

    all_reviews = companyReview.objects.all()
    all_tags = Tags.objects.all()

    if company_filter :
        all_reviews = companyReview.objects.filter(company_name__icontains=company_filter)

    if tag_filter:
        all_reviews = companyReview.objects.filter(tag=tag_filter)

    context = {'all_reviews':all_reviews,'all_tags':all_tags}
    return render(request,'index.html',context)


def specificReview(request,primary_key):
    if cache.get(primary_key):
        review = cache.get(primary_key)
        source = 'This is a cached review'
    else:
        review = companyReview.objects.get(id=primary_key)
        cache.set(primary_key , review)
        source = 'This review isnt cached'
    context = {'review':review , 'source':source}
    return render(request,'review.html',context)


