# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import timedelta

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
    task_day_price = fields.Monetary('Task Per Day Price', default=0.00, currency_field='currency_id')
    publisher_id = fields.Many2one('res.partner', string='Publisher', ondelete='set null', context={}, domain=[],)
    author_ids = fields.Many2many('res.partner', string='Authors')
    task_remaining_days = fields.Float(string='Task Remaining Days',compute='_compute_r_days',store=False)
    task_total_price = fields.Float(string='Task Total price',compute='_compute_t_total_price',store=False)
   
    
    @api.depends('deadline_date')
    
    def _compute_r_days(self):
        today = fields.Date.today()
        for book in self:
            if book.deadline_date:
                delta = book.deadline_date - today
                book.task_remaining_days = delta.days
            else:
                book.task_remaining_days = 0
    
    @api.depends('deadline_date','task_day_price')
    def _compute_t_total_price(self):
        for b in self:
            total_price = b.task_day_price * b.task_remaining_days
            b.task_total_price = total_price

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


class EmployeeTask(models.Model):
    _name = 'employee.task'
    _inherit = 'task.manager'

    show_load = fields.Float(string='Show Load' ,compute='_compute_show_load',store=False)

    @api.depends('status')

    def _compute_show_load(self):
        for book in self:
            if book.status:
                if book.status == 'new':
                    book.show_load = 0.0
                elif book.status == 'in_progress':
                    book.show_load = 0.5
                elif book.status == 'done':
                    book.show_load = 1.0
            else:
                book.show_load = 0.0