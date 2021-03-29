from odoo import api, models, fields

class TeamsOrder(models.Model):
    _inherit = 'res.users'

    teams_id = fields.Many2one('teams.order', string="Teams")
    work_id = fields.Many2one('work.order', string="work Order")

class TeamsOrder(models.Model):
    _name = 'teams.order'
    
    name = fields.Char('Team Name')
    team_leader_id = fields.Many2one('res.users', string='Team Leader')
    employees_ids = fields.One2many('res.users', 'teams_id', string='Employees')
    equipments_ids = fields.One2many('serial.number', 'teams_id', string='Serial Number')
    sale_id = fields.Many2one('sale.order', string='Sales Order')

