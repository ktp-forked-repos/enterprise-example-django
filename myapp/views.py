from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from .client import *


def index(request):
    if request.method == 'POST':
        # you'll acquire an access token issued per user as POST parameter
        # after they have successfully uploaded their DNA data via popup window.
        token = request.POST.get('genomelinkToken')

        # for this example app, if token is valid,
        #
        # ```
        # {'detail': 'Hello GENOME LINK!'}
        # ```
        #
        # will be returnd as JSON.
        try:
            data = Report.fetch(client_secret=settings.GENOMELINK_CLIENT_SECRET, token=token)
            messages.success(request, data['detail'])
        except GenomeLinkError as e:
            messages.warning(request, e)

    return render(request, 'myapp/index.html', {'GENOMELINK_CLIENT_ID': settings.GENOMELINK_CLIENT_ID})
