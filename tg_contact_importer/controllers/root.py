# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate, config
from tg.i18n import ugettext as _, lazy_ugettext as l_

from tg_contact_importer import model
from tg_contact_importer.model import DBSession
from contact_importer.providers import GoogleContactImporter, YahooContactImporter, LiveContactImporter
from tgext.pluggable.utils import plug_url

providers = {
    "google": GoogleContactImporter,
    "live": LiveContactImporter,
    "yahoo": YahooContactImporter
}

class RootController(TGController):

    def _get_redirect_url(self):
        redirect_url = "%s://%s%s" % (request.scheme, request.host, 
                                    plug_url("tg_contact_importer", "/invite?provider=%s" % request.GET.get('provider')))
        return redirect_url

    @expose('tg_contact_importer.templates.index')
    def index(self, provider=None):
        if provider is not None:
            provider_inst = get_provider_instance(provider, self._get_redirect_url()) 
            return redirect(provider_inst.request_authorization())

        return dict(url_func=plug_url)

    @expose('tg_contact_importer.templates.invite')
    def invite(self, provider, code):
        redirect_url = self._get_redirect_url()
        provider_instance = get_provider_instance(provider, redirect_url)
        access_token = provider_instance.request_access_token(code)

        print access_token

        if not access_token:
            return redirect(plug_url("tg_contact_importer", "/"))

        contacts = provider_instance.import_contacts(access_token)
        return dict(contacts=contacts)


def get_provider_instance(provider, redirect_url):
    if provider not in providers:
        raise Exception("The provider %s is not supported." % provider)

    client_id = config.get("%s.client_id" % provider)
    client_secret = config.get("%s.client_secret" % provider)

    if not client_id:
        raise Exception("The provider %s is not supported." % provider)

    provider_class = providers[provider]
    return provider_class(client_id, client_secret, redirect_url)

