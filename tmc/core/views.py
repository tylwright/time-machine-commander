from django.shortcuts import render_to_response, HttpResponse, Http404
import logging


def settings(request):
    return render_to_response('settings.html', locals())


def settings_share_permissions(request):
    return render_to_response('settings_share_permissions.html', locals())


def settings_backups(request):
    return render_to_response('settings_backups.html', locals())


def settings_configs(request):
    return render_to_response('settings_configs.html', locals())


def download_configs(request, file):
    if "avahi-daemon" in file:
        path = "/etc/avahi/avahi-daemon.conf"
    elif "afpd" in file:
        path = "/etc/netatalk/afpd.conf"
    elif "afp" in file:
        path = "/etc/netatalk/afp.conf"
    elif "AppleVolumes" in file:
        path = "/etc/netatalk/AppleVolumes.default"
    else:
        raise Http404()
    response = HttpResponse(open(path, 'rb').read())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename={}'.format(file)
    return response
