# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Document(models.Model):
    _name = "document.document"
    _description = 'Document'
    
    sequence = fields.Integer(default=0)
    name = fields.Char('Name', required=True)
    description = fields.Char('Description') 
    