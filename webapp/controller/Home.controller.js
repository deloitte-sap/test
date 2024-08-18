sap.ui.define([
    "sap/ui/core/mvc/Controller",
    "sap/ui/model//JSONModel",
    "sap/m/MessageToast"
], function (Controller, JSONModel, MessageToast) {
    "use strict";

    return Controller.extend("copilot.controller.Home", {

        onInit: function () {
            var oModel = new JSONModel({
                chat: []
            });
            this.getView().setModel(oModel);
        },

        onSend: function () {
            var oView = this.getView();
            var oModel = oView.getModel();
            var aChat = oModel.getProperty("/chat");
            var sMessage = oView.byId("chatInput").getValue();

            // Clear input field
            oView.byId("chatInput").setValue("");

            if (sMessage.trim()) {
                var oMessage = {
                    sender: "User",
                    message: sMessage
                };
                aChat.push(oMessage);
                oModel.setProperty("/chat", aChat);

                // Call backend service
                this._callBackendService(sMessage);
            } else {
                MessageToast.show("Please enter a message.");
            }
        },

        _callBackendService: function (sMessage) {
            var oView = this.getView();
            var oModel = oView.getModel();

            // Make an API call to the backend service
            $.ajax({
                url: "/backend/chat",
                method: "POST",
                contentType: "application/",
                data: JSON.stringify({ message: sMessage }),
                success: function (oResponse) {
                    var aChat = oModel.getProperty("/chat");
                    var oMessage = {
                        sender: "Bot",
                        message: oResponse.reply
                    };
                    aChat.push(oMessage);
                    oModel.setProperty("/chat", aChat);
                },
                error: function () {
                    MessageToast.show("Failed to get response from backend.");
                }
            });
        }
    });
});