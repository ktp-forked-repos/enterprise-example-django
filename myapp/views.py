from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
import genomelink


def index(request):
    reports = None

    if request.method == 'POST':
        # You'll acquire an access token issued per user as a POST parameter.
        token = request.POST.get('genomelinkToken')

        try:
            # Then, you can fetch reports by using the token and your GENOMELINK_CLIENT_SECRET.
            # In real applications, you should store report data into persistent storage.
            reports = genomelink.Report.fetch(token=token,
                                              client_secret=settings.GENOMELINK_CLIENT_SECRET,
                                              name='foo',             # TODO: remove
                                              population='european')  # TODO: remove
            messages.success(request, 'Success!')
        except genomelink.errors.GenomeLinkError as e:
            # When something is wrong with API request, API client raise errors.
            # In real applications, you should not display direct error messages to users.
            messages.warning(request, e)

    context = {
        'GENOMELINK_CLIENT_ID': settings.GENOMELINK_CLIENT_ID,
        'reports': reports
    }
    return render(request, 'myapp/index.html', context)
