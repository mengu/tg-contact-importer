# -*- coding: utf-8 -*-
"""Setup the tg_contact_importer application"""

from tg_contact_importer import model
from tgext.pluggable import app_model

def bootstrap(command, conf, vars):
    print 'Bootstrapping tg_contact_importer...'

    s1 = model.Sample()
    s1.name = 'Test Sample'
    s1.user = model.DBSession.query(app_model.User).first()

    model.DBSession.add(s1)
    model.DBSession.flush()