from django.apps import AppConfig
from django.conf.urls import url
from django.urls import include
from oscar import app


class Shop(app.Shop):
    def get_urls(self):
        urlpatterns = [
            url(r'^cart/', include(self.basket_app.urls)),
            # ...
            # Remianing urls here
        ]
        return urlpatterns


application = Shop()


class CmsConfig(AppConfig):
    name = 'cms'
