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
    def index(self):
        sample = DBSession.query(model.Sample).first()
        return dict(sample=sample)

    @expose('tg_contact_importer.templates.import')
    def contacts(self):
        return dict()

    @expose('tg_contact_importer.templates.contacts')
    def invite(self, provider):
        providers = {
            "google": GoogleContactImporter,
            "live": LiveContactImporter,
            "yahoo": YahooContactImporter
        }

        if provider not in providers:
            raise Exception("Unsupported Provider")

        provider_class = providers[provider]
        provider_inst = provider_class()
