using { copilot as db } from '../db/schema';

service ChatService {
  entity Chats as projection on db.Chat;

  @readonly
  action sendMessage(message: String) returns String;
}