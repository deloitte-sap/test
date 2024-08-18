sap.ui.define([
    "sap/ui/core/UIComponent",
    "sap/ui/model//JSONModel",
    "sap/ui/core/routing/Router"
], function (UIComponent, JSONModel, Router) {
    "use strict";

    return UIComponent.extend("copilot.Component", {
        metadata: {
            manifest: ""
        },

        init: function () {
            // call the init function of the parent
            UIComponent.prototype.init.apply(this, arguments);

            // set data model
            var oData = {
                recipient: {
                    name: "World"
                }
            };
            var oModel = new JSONModel(oData);
            this.setModel(oModel);

            // create the views based on the url/hash
            this.getRouter().initialize();
        }
    });
});