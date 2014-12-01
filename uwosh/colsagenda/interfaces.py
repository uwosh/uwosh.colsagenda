from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from uwosh.colsagenda import colsagendaMessageFactory as _

# -*- extra stuff goes here -*-

class IAgenda(Interface):
    """A rich text field that can contain files."""

    contains('Products.ATContentTypes.interfaces.IATFile',)

    text = schema.Text(title=_(u"Text"),
                       description=_(u"Main agenda text"),
                       required=True)