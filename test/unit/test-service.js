const cds = require('@sap/cds');
const { expect } = require('chai');
const { GET, POST } = cds.test(__dirname + '/../..');

describe('ChatService', () => {
  it('should return echo message', async () => {
    const response = await POST('/sendMessage', { message: 'Hello' });
    expect(response.data).to.equal('Echo: Hello');
  });
});