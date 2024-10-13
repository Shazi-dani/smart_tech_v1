from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.META.get('HTTP_REFERER', '/')
    color = request.POST.get('product_color')

    # Initialize the shopping bag from the session
    bag = request.session.get('bag', {})

    # Check if color is provided
    if color:
        if item_id in bag.keys():
            if color in bag[item_id]['items_by_color']:
                bag[item_id]['items_by_color'][color] += quantity
                messages.success(request,
                                 f'Updated color {color.upper()} '
                                 f'{product.name} quantity to '
                                 f'{bag[item_id]["items_by_color"][color]}')
            else:
                bag[item_id]['items_by_color'][color] = quantity
                messages.success(request,
                                 f'Added color {color.upper()} '
                                 f'{product.name} to your bag')
        else:
            bag[item_id] = {'items_by_color': {color: quantity}}
            messages.success(request,
                             f'Added color {color.upper()} '
                             f'{product.name} to your bag')
    else:
        if item_id in bag.keys():
            bag[item_id] += quantity
            messages.success(request,
                             f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    # Save the updated bag to the session
    request.session['bag'] = bag
    
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    color = None

    if 'product_color' in request.POST:
        color = request.POST['product_color']

    bag = request.session.get('bag', {})

    if color:  # Corrected this condition
        if quantity > 0:
            bag[item_id]['items_by_color'][color] = quantity  # Corrected from items_by_color to items_by_color
            messages.success(request,
                             (f'Updated color {color.upper()} '
                              f'{product.name} quantity to '
                              f'{bag[item_id]["items_by_color"][color]}'))
        else:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
                messages.success(request,
                             (f'Removed color {color.upper()} '
                              f'{product.name} from your bag'))
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {bag[item_id]}'))
        else:
            bag.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} '
                              f'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    try:
        color = None
        if 'product_color' in request.POST:
            color = request.POST['product_color']

        bag = request.session.get('bag', {})

        if color:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
                messages.success(request,
                             (f'Removed color {color.upper()} '
                              f'{product.name} from your bag'))
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
