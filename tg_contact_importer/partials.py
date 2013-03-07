from tg import expose

@expose('tg_contact_importer.templates.little_partial')
def something(name):
    return dict(name=name)