from django.views.generic import View
from django.views.generic.base import ContextMixin
from django.http.response import HttpResponse
from .utils import _ERROR_CODES
from django.conf import settings
import json


class JSONResponse(HttpResponse):
    def __init__(self, context_data, status=200, mimetype='application/json',
                 content_type='application/json'):
        if settings.DEBUG is True:
            content = json.dumps(context_data, sort_keys=True, indent=4)
        else:
            content = json.dumps(context_data, separators=(',', ':'))
        super(JSONResponse, self).__init__(content, mimetype, status, mimetype)


class JSONMixin(object):

    response_class = JSONResponse

    def render_to_response(self, context, **response_kwargs):
        return self.render_response(context, **response_kwargs)

    def render_response(self, context, **response_kwargs):
        return self.response_class(context_data=context, **response_kwargs)

    def render_error(self, error_type='UNKNOWN', message=None):
        if error_type not in _ERROR_CODES:
            error_type = 'UNKNOWN'

        obj = {'status': 'error',
               'error_code': _ERROR_CODES[error_type][0],
               'error_message': _ERROR_CODES[error_type][1]}

        if message is not None:
            obj['error_message'] = message

        return self.render_response(obj, status=_ERROR_CODES[error_type][2])


class JSONView(JSONMixin, ContextMixin, View):

    def dispatch(self, request, *args, **kwargs):
        return super(JSONView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context = {'status': 'ok'}
        return self.render_response(context)
