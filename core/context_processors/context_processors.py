from core.models import Settings,Logo

def settings(requests):
    context= {
        'x':Settings.objects.first(),
        'y':Logo.objects.first()

}
    return context