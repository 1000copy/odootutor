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
    

    
    def name_get(self):
        if self.env.context.get('display_full_name', False):
            pass
        else:
            return super(Document, self).name_get()
        def get_names(record):
            res = []
            while record:
                res.append(record.name or '')
                record = record.parent_id
            return res
        return [(record.id, " / ".join(reversed(get_names(record)))) for record in self]

    
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        default.update(name=_("%s (copy)") % (self.name or ''))
        return super(Document, self).copy(default)

    def action(self):
        self.ensure_one()
        context = self.env.context
        action_id = context.get('module_action_id')
        if action_id:
            action_dict = self.env.ref(action_id).read([
                "type", "res_model", "view_mode", "domain"
            ])[0]
            action_dict["name"] = self.name
        return action_dict
