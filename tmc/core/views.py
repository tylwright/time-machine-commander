from django.shortcuts import render_to_response


def settings(request):
    return render_to_response('settings.html', locals())


def settings_share_permissions(request):
    return render_to_response('settings_share_permissions.html', locals())


def settings_backups(request):
    return render_to_response('settings_backups.html', locals())


def settings_configs(request):
    return render_to_response('settings_configs.html', locals())