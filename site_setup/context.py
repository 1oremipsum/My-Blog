from site_setup.models import SiteSetup

# Context Processors

def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()
    return {
        'site_setup': setup,
    }