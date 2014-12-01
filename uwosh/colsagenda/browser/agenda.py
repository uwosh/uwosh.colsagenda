from Acquisition import aq_inner

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.memoize.instance import memoize

class AgendaView(BrowserView):
    """Default view of anAgenda
    """
    
    __call__ = ViewPageTemplateFile('agenda.pt')