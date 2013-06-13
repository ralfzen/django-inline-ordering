from django.conf import settings

# path to inline_ordering.js
INLINE_ORDERING_JS_URL = getattr(settings, 'INLINE_ORDERING_JS_URL', settings.STATIC_URL + 'inline_ordering.js')


JQUERY_PREAMBLE_JS_URL = INLINE_ORDERING_JS_URL.replace('inline_ordering.js', 'inline_ordering_preamble.js')
JQUERY_UI_JS_URL = INLINE_ORDERING_JS_URL.replace('inline_ordering.js', 'jquery-ui.min.js')
