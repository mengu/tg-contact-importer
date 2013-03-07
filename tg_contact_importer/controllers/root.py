# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController
from tg import expose, flash, require, url, lurl, request, redirect, validate, config
from tg.i18n import ugettext as _, lazy_ugettext as l_

from tg_contact_importer import model
from tg_contact_importer.model import DBSession
from contact_importer.providers import GoogleContactImporter, YahooContactImporter, LiveContactImporter


class RootController(TGController):
    @expose('tg_contact_importer.templates.index')
    def index(self, provider=None):
        if provider is not None:
            providers = {
                "google": GoogleContactImporter,
                "live": LiveContactImporter,
                "yahoo": YahooContactImporter
            }

            if provider not in providers:
                raise Exception("The provider %s is not supported." % provider)

            client_id = config.get("%s.client_id" % provider)
            client_secret = config.get("%s.client_secret" % provider)

            if not client_id:
                raise Exception("The provider %s is not supported." % provider)

            provider_class = providers[provider]
            provider_inst = provider_class(client_id, client_secret, url("/tg_contact_importer/invite?provider=%s" % provider)) 
            return redirect(provider_inst.request_authorization())

        return dict()

    @expose('tg_contact_importer.templates.invite')
    def invite(self, provider):
        pass
        
