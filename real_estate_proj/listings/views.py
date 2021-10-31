from django.shortcuts import render
from django.core.paginator import EmptyPage,  PageNotAnInteger, Paginator

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
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')