import time

from django.shortcuts import redirect


# get_response gets the response from next middleware or view
def measure_time_middleware(get_response):

    def middleware(request, *args, **kwargs):
        start = time.time()

        response = get_response(request, *args, **kwargs)

        end = time.time()
        exec_time = end - start

        print(f"------------------ {exec_time:.3f} s ------------------")

        return response

    return middleware
