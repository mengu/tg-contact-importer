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

    plug(base_config, 'tg_contact_importer', 'contacts')

You will be able to access the registration process at
*http://localhost:8080/contacts*.

Configuring your application
----------------------------
In order to import contacts from Gmail, Live and Yahoo accounts you should follow these steps.

1. Obtain a client id and client secret from providers above.
2. Set your API credentials in your *.ini config files.

Following is a sample configuration:

.. code:: bash

    [app:main]
    # other configurations..
    google.client_id = my_google_client_id
    google.client_secret = my_google_client_secret
    live.client_id = my_live_client_id
    live.client_secret = my_live_client_secret
    yahoo.client_id = my_yahoo_client_id
    yahoo.client_secret = my_yahoo_client_secret


Exposed Templates
--------------------

The templates used by registration and that can be replaced with
*tgext.pluggable.replace_template* are:

    templates/invite.jinja

