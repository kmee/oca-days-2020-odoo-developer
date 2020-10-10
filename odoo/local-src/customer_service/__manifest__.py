# Copyright 2020 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Customer Service',
    'description': """
        ACME Customer Service""",
    'version': '13.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'KMEE',
    'website': 'www.kmee.com.br',
    'depends': [
    ],
    'data': [
        'security/customer_service_ticket.xml',

        'views/customer_service_menu.xml',
        'views/customer_service_ticket.xml',
    ],
    'demo': [
        'demo/customer_service_ticket.xml',
    ],
}
