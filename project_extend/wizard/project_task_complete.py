# -*- coding: utf-8 -*-
from odoo import fields, models, _


class ProjectTaskCompleteWizard(models.TransientModel):
    _name = 'project.task.complete.wizard'
    _description = 'Project task complete'

    reason = fields.Text(string="Reason")

    def action_complete(self):
        self.ensure_one()
        task_id = self.env.context.get('active_id')
        task = self.env['project.task'].browse(task_id)
        project_stage_list = task.project_id.type_ids.filtered(lambda line: line.code == 'review')
        task.write({'stage_id': project_stage_list[0].id})
        task._compute_is_in_progress()
        message = _("Complete Task: {reason}".format(reason=self.reason))
        task.message_post(body=message, subject='Complete Task')
