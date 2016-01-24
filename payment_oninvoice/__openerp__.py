# -*- coding: utf-8 -*-

###############################################################################
#
#   payment_oninvoice for Odoo/OpenERP
#   Copyright (C) 2016 Emmanuel SCIARA
#   @author: Emmanuel SCIARA <emmanuel.sciara@gmail.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': 'On Invoice Payment Acquirer',
    'category': 'Hidden',
    'license': 'LGPL-3',
    'summary': 'Payment Acquirer: On Invoice Implementation',
    'version': '1.0',
    'description': """On Invoice Payment Acquirer""",
    'author': "Emmanuel SCIARA",
    'depends': ['payment'],
    'data': [
        'views/oninvoice.xml',
        'data/oninvoice.xml',
    ],
    'installable': True,
    'auto_install': False,
}
