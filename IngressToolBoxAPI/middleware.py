# -*- coding:utf-8 -*-
import json
import logging

logger = logging.getLogger('file_log')


class LogMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        try:
            request_dict = {}
            try:
                request_dict = json.loads(request.body)
            except Exception as e:
                pass
            request_dict.update(request.GET.dict())
            request_dict.update(request.POST.dict())
            if 'json' in response._headers['content-type'][1]:
                log_str = f"{request.path} params: {str(request_dict)} " \
                          f"response {response.status_code} {response.content}"
            else:
                log_str = "{} params: {} response {} {}".format(
                    request.path, str(request_dict),
                    response.status_code, 'html_page'
                )
            logger.info(log_str)
        except Exception as e:
            logger.info("middleware log error {}".format(e.message))
        return response
