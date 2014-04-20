from django.conf import settings
import datetime
today = datetime.date.today()

JSON_MIME_TYPE = getattr(settings, 'JSON_MIME_TYPE', 'application/json')


_ERROR_CODES = {
    'BAD_REQUEST': (400, 'Bad request: missing or invalid body', 400),
    'UNAUTHORIZED': (401, 'Authentication credential are invalid', 401),
    'FORBIDDEN': (403, 'Api key is invalid or missing', 403),
    'NOT_FOUND': (404, 'Object or resource was not found', 404),
    'CONFLICT': (409, 'Missing parameter', 409),
    'UNKNOWN': (500, 'server error', 500),
}


def clear_cart(request, cart):
    modify = False
    for key, item in cart.items():
        start_date = datetime.datetime.strptime(item['start_date'], '%m/%d/%Y').date()
        today = datetime.date.today()
        if (start_date - today).days < 0:
            modify = True
            del cart[key]

    # remove late items
    if modify:
        if self.request.user.is_authenticated():
            user_profile = request.user.get_profile()
            user_profile.cart = json.dumps(cart)
            user_profile.save()
        else:
            self.request.session['cart'] = cart
    return cart