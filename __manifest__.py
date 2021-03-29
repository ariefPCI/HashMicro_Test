# coding: utf-8
##############################################################################
#
# This module is developed by Portcities Indonesia
# Copyright (C) 2017 Portcities Indonesia (<http://idealisconsulting.com>).
# All Rights Reserved
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'Booking Service',
    'version' : '10.0.2.0',
    'summary': 'Create Module Booking Service to Hiring HashMicro',
    'description': """ 
    To allow users to create bookings for employees and equipments
     """,
    'author' : 'Arief Afandy',
    'category': 'HashMicro Hiring Employee',
    'depends' : ['sale','stock','web_calender','event'],
    'data': [
        'views/product_view.xml',
        'views/booking_order_view.xml',
        'views/work_order_view.xml',
        'views/teams_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

