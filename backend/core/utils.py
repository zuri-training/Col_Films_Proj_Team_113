from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def mk_paginator(request, items, num_items):
    """
    Create and return a paginator.
    Ex: items = mk_paginator(request, items, 2)
    """
    paginator = Paginator(items, num_items)
    page = request.GET.get('page', 1)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, return the first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range, return the last page of results.
        items = paginator.page(paginator.num_pages)
    return items
