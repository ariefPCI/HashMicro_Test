# -*- coding: utf-8 -*-

from odoo import api, models, fields

class BookingOrder(models.Model):
    _name = 'booking.order'
    work_order_ids = fields.One2many('work.order', 'team_id', string='Booking Order')


class SaleOrder(models.Model):
    _inherit = "sale.order"

    is_booking = fields.Boolean("Is a Booking", default=False)
    teams_order_ids = fields.One2many('teams.order', 'sale_id', string='Teams Order')

    @api.onchange('is_booking')
    def is_booking(self):
        if self.is_booking == 'True':
        	self.teams_order_ids.name = self.team_id.name
            