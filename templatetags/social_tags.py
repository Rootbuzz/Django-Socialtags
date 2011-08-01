from django.template import Library
from django.conf import settings

if "django.contrib.sites" in settings.INSTALLED_APPS:
    from django.contrib.sites.models import Site
    current_domain = lambda: Site.objects.get_current().domain

elif getattr(settings, "SITE_DOMAIN", None):
    current_domain = lambda: settings.SITE_DOMAIN

else:
    current_domain = lambda: "example.com"
    

register = Library()

def fully_qualified(url):
    # if it's not a string the rest of this fn will bomb
    if not isinstance(url, basestring): return ""
    
    if url.startswith('http'):
        return url
    elif url.startswith("/"):
        return 'http://%s%s' % (current_domain(), url)
    else:
        return 'http://%s' % url
    
    
@register.inclusion_tag('social_tags/default/twitter.html')
def twitter_share(url=None):
    url = fully_qualified(url)
    return locals()


@register.inclusion_tag('social_tags/default/facebook.html')
def facebook_share(url=None):
    url = fully_qualified(url)
    return locals()


@register.inclusion_tag('social_tags/default/linkedin.html')
def linkedin_share(url=None):
    url = fully_qualified(url)
    return locals()


@register.inclusion_tag('social_tags/default/email.html')
def email_share(url=None):
    url = fully_qualified(url)
    return locals()


@register.inclusion_tag('social_tags/default/google.html')
def google_plus(url=None):
    url = fully_qualified(url)
    return locals()