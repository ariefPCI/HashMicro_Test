# -*- coding: utf-8 -*-
from odoo import api, models, fields

class WorkOrder(models.Model):
    _name = 'work.order'
    
    work_booking_ok = fields.Boolean("Is a Booking", default=False)
    scheduled_start = fields.Datetime(string='Scheduled Start')
    scheduled_end = fields.Datetime(string='Scheduled End')

    actual_start = fields.Datetime(string='Actual Start')
    actual_end = fields.Datetime(string='Actual End')
    team_id = fields.Many2one('booking.order', string="Team")
    team_leader =  fields.Char(string="Team Leader")
    employees_id = fields.One2many('res.users','work.order', string="Employees")
    equipmenet_ids = fields.One2many('serial.number','work_equipment_id', string="Equipmenets")


class StockMove(models.Model):
	_inherit = 'stock.move'

	def check_work_order(self):
		if self.date != 'False':
    		raise UserError(_('Employee %s Employee %s and Equipment %s has an event on that day and time ')%
                (self.name, self.name, self.equipment_attendee.name))

    	if self.date == 'False':
    		raise UserError(_('Everyone is available for the booking'))

    #create function makeworkorder
    def makeworkorder(self):
    	print(".....")