odoo.define('module_name.BasicView', function (require) {
    "use strict";
    var session = require('web.session');
    var BasicView = require('web.BasicView');
    BasicView.include({
        init: function(viewInfo, params) {
            var self = this;
            this._super.apply(this, arguments);
            var model = self.controllerParams.modelName === 'project.project' ? 'True' : 'False';
            if(model) {
                session.user_has_group('project.group_project_manager').then(function(has_group) {
                    if(!has_group) {
                        self.controllerParams.archiveEnabled = 'False' in viewInfo.fields;
                    }
                });
                session.user_has_group('project_extend.group_project_team_manager').then(function(has_group) {
                    if(!has_group) {
                        self.controllerParams.archiveEnabled = 'False' in viewInfo.fields;
                    }
                });
            }
        },
    });
});
