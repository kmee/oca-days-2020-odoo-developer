# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CustomerServiceTicket(models.Model):

    _name = 'customer.service.ticket'
    _inherit = ['base.kanban.abstract', 'mail.thread']

    _description = 'Customer Service Ticket'  # TODO

    code = fields.Char(
        readonly=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('customer.service')
    )
    name = fields.Char()
    description = fields.Html(sanitize_style=True)
    user_id = fields.Many2one('res.users')
    partner_id = fields.Many2one('res.partner')
    partner_email = fields.Char(related='partner_id.email')

    def send_number_by_sms(self):
        for record in self:
            record._message_sms(
                'OCA days: Your ticket number is {}'.format(record.code),
                partner_ids=record.partner_id.ids
            )
