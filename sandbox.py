import os
import django


os.environ.update({'DJANGO_SETTINGS_MODULE': 'config.settings',
                   'AUTH_USER_MODEL': 'users.User'
                   })
django.setup()


from newsletter_app.services import newsletter

newsletter()
