# -*- coding: utf-8 -*-
{
    'name': 'Task Manager',
    'summary': """For Practicing my first app""",
    'description': """
Task Management App
========
Something about the App.
    """,
    'version': '16.0.1.0',
    'author': 'Daffodil',
    'website': 'http://www.daffodil.com',
    'category': 'Human Resources',
    'sequence': 1,
    'depends': [
        'base',
        'web',
        'hr',
        'mail'
        
        ],
    'data': [
    
        # Security
        'security/ir.model.access.csv',
        'security/task_manager_security.xml',
        
         # ## View
        'views/task_manager_views.xml',
        'views/my_test_view.xml',
        'views/employee_task_view.xml',
    ],
    'qweb': [],
    'assets': {},
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'OPL-1',
}
