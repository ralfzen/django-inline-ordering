from django.conf import settings
import os


# path to inline_ordering.js
INLINE_ORDERING_JS_URL = getattr(settings, 'INLINE_ORDERING_JS_URL', 
    os.path.join(settings.STATIC_URL, 'js', 'inline_ordering.js'))

JQUERY_PREAMBLE_JS_URL = INLINE_ORDERING_JS_URL.replace('inline_ordering.js',
    'inline_ordering_preamble.js')
JQUERY_UI_JS_URL = INLINE_ORDERING_JS_URL.replace('inline_ordering.js', 
    'jquery-ui.min.js')
