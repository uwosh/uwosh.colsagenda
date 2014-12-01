"""Definition of the Agenda content type
"""

from zope.interface import implements, directlyProvides

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from uwosh.colsagenda import colsagendaMessageFactory as _
from uwosh.colsagenda.interfaces import IAgenda
from uwosh.colsagenda.config import PROJECTNAME

AgendaSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    atapi.TextField('text',
        searchable=True,
        primary=True,
        default_output_type = 'text/x-html-safe',
        storage = atapi.AnnotationStorage(),
        widget=atapi.RichWidget(label=_(u"Text"),
                                description=_(u"Main agenda text"))
    ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

AgendaSchema['title'].storage = atapi.AnnotationStorage()
AgendaSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(AgendaSchema, folderish=True, moveDiscussion=False)

class Agenda(folder.ATFolder):
    """A rich text field that can contain files."""
    implements(IAgenda)

    portal_type = "Agenda"
    schema = AgendaSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')
    text = atapi.ATFieldProperty('text')

atapi.registerType(Agenda, PROJECTNAME)
