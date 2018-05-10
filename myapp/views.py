from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
import genomelink


def index(request):
    if request.method == 'POST':
        # You'll acquire an access token issued per user as a POST parameter.
        token = request.POST.get('genomelinkToken')

        try:
            # Then, you can fetch reports by using the token and your GENOMELINK_CLIENT_SECRET.
            reports = genomelink.Report.fetch(name='example', population='european', token=token, client_secret=settings.GENOMELINK_CLIENT_SECRET)

            # Now you can display the reports.
            # In real applications, you should store report data into persistent storage.
            for report in reports:
                messages.success(request, '{}: {}'.format(report.phenotype['display_name'], report.summary['text']))

        except genomelink.errors.GenomeLinkError as e:
            # When something is wrong with API request, API client raise errors.
            # In real applications, you should not display direct error messages to users.
            messages.warning(request, e)

    return render(request, 'myapp/index.html', {'GENOMELINK_CLIENT_ID': settings.GENOMELINK_CLIENT_ID})