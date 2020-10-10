# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CustomerServiceTicket(models.Model):

    _name = 'customer.service.ticket'
    _description = 'Customer Service Ticket'  # TODO

    name = fields.Char()
