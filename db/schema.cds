namespace copilot;

entity Chat {
  key ID : UUID;
  sender : String;
  message : String;
  timestamp : Timestamp;
}