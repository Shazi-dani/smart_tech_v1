from django.shortcuts import render, redirect, reverse, HttpResponse


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.META.get('HTTP_REFERER', '/')
    color = None

    if 'product_color' in request.POST:
        color = request.POST['product_color']

    bag = request.session.get('bag', {})

    if color:
        if item_id in list(bag.keys()):
            if color in bag[item_id]['items_by_color'].keys():
                bag[item_id]['items_by_color'][color] += quantity
            else:
                bag[item_id]['items_by_color'][color] = quantity
        else:
            bag[item_id] = {'items_by_color': {color: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    color = None

    if 'product_color' in request.POST:
        color = request.POST['product_color']

    bag = request.session.get('bag', {})

    if color:  # Corrected this condition
        if quantity > 0:
            bag[item_id]['items_by_color'][color] = quantity  # Corrected from items_by_color to items_by_color
        else:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        color = None
        if 'product_color' in request.POST:
            color = request.POST['product_color']

        bag = request.session.get('bag', {})

        if color:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
