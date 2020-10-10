# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from base64 import b64encode
from pkg_resources import Requirement, resource_string
from anthem.lyrics.records import create_or_update


def setup_company(ctx, req):
    """ Setup company """
    company = ctx.env.ref('base.main_company')
    company.name = 'OCA Days 2020'

    # load logo on company
    logo_content = resource_string(req, 'data/images/logo.png')
    logo = b64encode(logo_content)
    company.logo = logo

def main(ctx):
    """ Create demo data """
    req = Requirement.parse('dev-oca-days')
    setup_company(ctx, req)
