import logging
logger = logging.getLogger('uowsh.colsagenda: setuphandlers')

from Products.CMFCore.utils import getToolByName

def makeAgendaLinkable(context):
    if context.readDataFile('uwosh.colsagenda.txt') is None:
        return

    kupuTool = getToolByName(context.getSite(), 'kupu_library_tool')
    
    linkable = list(kupuTool.getPortalTypesForResourceType('linkable'))
    
    if 'Agenda' not in linkable:
        linkable.append('Agenda')
        
    kupuTool.updateResourceTypes(({'resource_type' : 'linkable',
                                   'old_type'      : 'linkable',
                                   'portal_types'  :  linkable},))
                                   