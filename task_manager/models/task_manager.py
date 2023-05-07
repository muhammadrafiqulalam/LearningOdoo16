# -*- coding: utf-8 -*-
from odoo import api, fields, models

class TaskManager(models.Model):
    _name = 'task.manager'
    _description = 'Task Manager'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    

    name = fields.Char('Task Name', required=True)
    designation=fields.Many2one('hr.job',string='Designation Name')
    department = fields.Many2one('hr.department',string='Department Name')
    description = fields.Text('Description')
    date = fields.Date('Date')
    priority = fields.Selection([('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], required=True, default='low')
    status = fields.Selection([('new', 'New'), ('in_progress', 'In Progress'), ('done', 'Done')], required=True, default='new')
    assigned_to_id = fields.Many2one('hr.employee', string='Assigned to', default=lambda self: self.env.user)
    deadline_date = fields.Date(string='Deadline Date')
    currency_id = fields.Many2one('res.currency', string='Currency')
    task_duration_req = fields.Float(string='Task Required Duration')
    task_day_price = fields.Monetary('Task Per Day Price', default=0.00, currency_field='currency_id')
    publisher_id = fields.Many2one('res.partner', string='Publisher', ondelete='set null', context={}, domain=[],)
    author_ids = fields.Many2many('res.partner', string='Authors')
   
  
class ResPartner(models.Model):
    _inherit = 'res.partner'

    task_book_ids = fields.One2many('task.manager', 'publisher_id', string='Published Books')
    author_book_ids = fields.Many2many('task.manager',string='Authored Books')


class MyTest(models.Model):
    _name = 'my.test'
    _description = 'My Test'
    _inherit = 'task.manager'

    mytest_name = fields.Char('My Test Name', required=True)
    bd_id = fields.Char('BD ID', required=True)

