# -*- encoding: utf-8 -*-
{
    "name": "Project Extend",
    "summary": "This Module allow add new features to project module",
    "description": "This Module allow add new features to project module",
    "version": "15.0.1.0.1",
    "category": "Project",
    "depends": ['sale', 'project', 'hr_timesheet', 'project_task_default_stage', 'sale_timesheet'],
    "data": [
        'security/project_security.xml',
        'security/ir.model.access.csv',
        'data/project_data.xml',
        'views/project_views.xml',
        'views/project_form2.xml',
        'views/project_tag.xml',
        'wizard/project_date_change_wizard_views.xml',
        'wizard/project_task_date_change_wizard_views.xml',
        'wizard/project_task_return_wizard.xml',
        'wizard/project_task_complete.xml',
        'wizard/project_task_approve.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'project_extend/static/src/js/basic_view.js',
        ],
    },
    "installable": True,
    "license": "OPL-1",
}
