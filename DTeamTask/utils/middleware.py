
class HelloWorldMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        comment = '<!--Hello, World!-->'
        request.comment = comment
        response = self.get_response(request)
        return response