About tg_contact_importer
-------------------------

tg_contact_importer is a Pluggable application for TurboGears2.

Installing
-------------------------------

tg_contact_importer can be installed both from pypi or from bitbucket::

    easy_install tg_contact_importer

should just work for most of the users

Plugging tg_contact_importer
----------------------------

In your application *config/app_cfg.py* import **plug**::

    from tgext.pluggable import plug

Then at the *end of the file* call plug with tg_contact_importer::

    plug(base_config, 'tg_contact_importer')

You will be able to access the registration process at
*http://localhost:8080/tg_contact_importer*.

Available Hooks
----------------------

tg_contact_importer makes available a some hooks which will be
called during some actions to alter the default
behavior of the appplications:

Exposed Partials
----------------------

tg_contact_importer exposes a bunch of partials which can be used
to render pieces of the blogging system anywhere in your
application:

Exposed Templates
--------------------

The templates used by registration and that can be replaced with
*tgext.pluggable.replace_template* are:

