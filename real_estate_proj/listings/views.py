from django.db.models import query
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage,  PageNotAnInteger, Paginator

from listings.choices import price_choices, state_choices, bedroom_choices
from .models import Listing

# Create your views here.
def index(request):
    """
    Gets the data from the Listings model in the db.The data is then
    ordered by list date in descending order and filtred by 'is published'
    value.
    Pagination (var 'paginator') is set to 6 listings to be displayed
    per page. 
    var 'page' gets the page number.
    var 'paged_listings' passes 'page as an object in get page method. 
    Context is then set to paged_listings via a dictionary. 

    """
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page =  request.GET.get('page')
    paged_listings = paginator.get_page(page)


    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    # get selected object from listings
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing':listing
    }


    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # search for keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # search for city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)


    # search for state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    
    # search for bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) # lte=LessThan or Equalto


    # search for price       
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)



    context = {
        'price_choices':price_choices,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'listings':queryset_list,
        'values':request.GET

    }

    return render(request, 'listings/search.html', context)