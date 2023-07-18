# Cloud Computing Introduction

## Client Server Computing
### Basic Architecture of a Computer
<p align="center"><img width="800" alt="Screenshot 2023-07-19 at 06 42 31" src="https://github.com/CodexploreRepo/aws/assets/64508435/b9f93e94-1c0e-4cc6-9f69-f03d5d7f67bb"></p>

- Type of devices:
  - Client device: laptop, desktop, mobile
  - Server device: many users can connect to it over a network
<p align="center"><img width="800" alt="Screenshot 2023-07-19 at 06 42 31" src="https://github.com/CodexploreRepo/aws/assets/64508435/1c65ee36-ee8e-407a-b3d3-d8957cf3e38b"></p>

### Client & Server Communication
#### Client connecting to Server
- The client application finds the server by **IP address** via specific
  - **Protocol**: HTTP, SMB (Service Message Block), SMTP (to send email) 
  - **Port** (like a door of the server)
<p align="center"><img width="600" alt="Screenshot 2023-07-19 at 06 42 31" src="https://github.com/CodexploreRepo/aws/assets/64508435/b0d47c29-3214-4eec-a100-3d8f33b894aa">
<br><br><img width="600" alt="Screenshot 2023-07-19 at 06 42 31" src="https://github.com/CodexploreRepo/aws/assets/64508435/f95314f2-2631-4172-8faa-8f74bf1516e8">
</p>

#### Server connecting to another server
- Application Server can connect to Database Server via MySQL **protocol** via **Port** 3306
<p align="center"><img width="800" alt="Screenshot 2023-07-19 at 06 42 31" src="https://github.com/CodexploreRepo/aws/assets/64508435/e1f56f1f-6b34-4dd0-a989-4ef67d832437"></p>

### Storage
- Hard-drives: block-based storage systems
  - File System: Fat32 & NTFS (Windows)
- Network Attached Storage (NAS): file-based storage system (mounted to OS using a network share)
- Object Storage Systems: upload objects (file, video, image) using a web broswer to *Object Storage container* via **HTTP protocol** with a **REST API** (GET, PUT, POST, SELECT, DELETE)
  -  Object Storage container: there is no hierachy of objects in the container

### IP address
- IP address are to the address computers use to communicate
- DNS: to map IP address with the domain

#### What is IPv4 address
- `192.168.0.1`
