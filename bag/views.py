from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """
    View that renders bag contents page
    """
    return render(request, 'bag/bag.html')
