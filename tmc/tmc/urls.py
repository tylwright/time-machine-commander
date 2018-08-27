from django.conf.urls import url
from django.contrib import admin
from dashboard import views as dashboard_views
from users import views as user_views
from core import views as core_views


urlpatterns = [
    # Admin stuffs
    url(r'^admin/', admin.site.urls),

    # Dashboard
    url(r'^$', dashboard_views.index),
    url(r'^home/', dashboard_views.index),

    # Users
    url(r'^users/$', user_views.index),

    # Settings
    url(r'^settings/$', core_views.settings),
    url(r'^settings/share-permissions/', core_views.settings_share_permissions),
    url(r'^settings/backups/', core_views.settings_backups),
    url(r'^settings/configs/', core_views.settings_configs),

    # Downloads
    url(r'^downloads/(?P<file>[-\w.]+)/$', core_views.download_configs)
]
