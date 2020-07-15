import json
import logging

from django.http import JsonResponse, HttpResponse
from django.views import View
from datetime import datetime

logger = logging.getLogger("helloworld")
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_timestamp():
    """ Returns current date and time in a human-readable format.

     Returns:
         str: current date and time
     """
    return datetime.now().strftime(TIMESTAMP_FORMAT)


class LandingView(View):
    def get(self, request, *args, **kwargs):
        logger.debug("{}: Received a {} request at URL: {}"
                     .format(get_timestamp(), request.method, request.build_absolute_uri()))

        if request.headers and "Accept" in request.headers:
            if request.headers["Accept"] == "application/json":
                message = {"message": "Hello, World"}
                return HttpResponse(json.dumps(message), content_type="application/json")
            else:
                message = "Hello, World"
                return HttpResponse(message)
        else:
            message = "<p>Hello, World</p>"
            return HttpResponse(message, content_type="text/html")

    def post(self, request, *args, **kwargs):
        logger.debug("{}: Received a {} request at URL: {}"
                     .format(get_timestamp(), request.method, request.build_absolute_uri()))

        # Basic payload validations
        if not request.body:
            return JsonResponse({"error": "Data cannot be empty"}, status=400)
        try:
            data = json.loads(request.body)
        except ValueError as err:
            return JsonResponse({"error": str(err)}, status=400)

        # Implement posting the data

        return HttpResponse("Post successful!")
