# -*- coding: utf-8 -*-

from odoo import models, fields, api

class conta_move(models.Model):
    
    _inherit = 'account.move'

    conta_ids = fields.Integer(index="True")

class asiento(models.Model):
    _inherit = 'account.move.line'

    asiente = fields.Many2one('account.move')
    asiento = fields.Char(compute='index')

    def index(self):
        for record in self:
            record.asiento = record.move_id.id

   
            
   

#     _name = 'journales.journales'
#     _description = 'journales.journales)

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
