# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import UserError


class ProductProduct(models.Model):
    _inherit = 'product.product'

    equipment_ok = fields.Boolean('Is an equipment')

class SerialNumber(models.Model):
    _name = 'serial.number'

    name =  fields.string('Name')
    teams_id = fields.Many2one('teams.order', string='Equipments')
    work_equipment_id = fields.Many2one('work.order', string="Work Order Equipments")


class EventRegistration(models.Model):
    _inherit = 'event.registration'

    equipment_attendee = fields.Many2one('serial.number', string='Serial Number')

    def check_booking_order(self):
    	if self.event_date != 'False':
    		raise UserError(_('Employee %s Employee %s and Equipment %s has an event on that day and time ')%
                (self.name, self.name, self.equipment_attendee.name))

    	if self.event_date == 'False':
    		raise UserError(_('Everyone is available for the booking'))


    def makebookingorder(self):
        registration = super(EventRegistration, self).create(vals)
        if registration._check_auto_confirmation():
            registration.sudo().confirm_registration()
        return registration