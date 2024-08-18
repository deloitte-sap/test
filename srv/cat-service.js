const cds = require('@sap/cds');

module.exports = function () {
  this.on('sendMessage', async (req) => {
    const { message } = req.data;
    const response = await callExternalChatService(message);
    return response;
  });

  async function callExternalChatService(message) {
    // Simulate a call to an external service
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(`Echo: ${message}`);
      }, 1000);
    });
  }
};