# -*- coding: utf-8 -*-
from Products.PortalTransforms.interfaces import ITransform
from Products.PortalTransforms.libtransforms.utils import bodyfinder
from zope.interface import implementer


@implementer(ITransform)
class HTMLRemoveInlineData(object):
    """Simple transform which extracts the content of the body tag"""

    __name__ = "html_remove_inline_data"
    inputs = ('text/html',)
    output = "text/html"

    def __init__(self, name=None):
        self.config_metadata = {
            'inputs':
                ('list',
                 'Inputs',
                 'Input(s) MIME type. Change with care.'),
        }
        if name:
            self.__name__ = name

    def name(self):
        return self.__name__

    def __getattr__(self, attr):
        if attr == 'inputs':
            return self.config['inputs']
        if attr == 'output':
            return self.config['output']
        raise AttributeError(attr)

    def convert(self, orig, data, **kwargs):
        if orig.find('src="data:"'):
            # do remove
            modified = orig
            data.setData(modified)
        else:
            data.setData(orig)
        return data


def register():
    return HTMLRemoveInlineData()
