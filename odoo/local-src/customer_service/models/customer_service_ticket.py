# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CustomerServiceTicket(models.Model):

    _name = 'customer.service.ticket'
    _inherit = 'base.kanban.abstract'

    _description = 'Customer Service Ticket'  # TODO

    name = fields.Char()
    description = fields.Html(sanitize_style=True)
    user_id = fields.Many2one('res.users')
    partner_id = fields.Many2one('res.partner')
    partner_email = fields.Char(related='partner_id.email')