# What is dbatools?
This is a tools that automate and simplify regular DBA tasks.


## Features
  - Myacc - to perform mass MySQL login deployment


### How to use this image
#### Myacc
|**Subject**|**Description**|
|:------------------------------------|:--------------------------------|
|**Upload deployment files page**  | http://localhost:8000/admin  |
|**Deployment page**  | http://localhost:8000/deploy  |
|**Default username password**  | root/Cc123456  |
|**Sample deployment files**  | under media/myacc-sample |

##### Deployment types
The deployment type are determine the keys inside the deployment yaml files.
- Databases file - It is yaml format, contains all the database host and login information
- Deployment file - It is yaml format, contains deployment content base on different deployment type.

  - role deployment (key: roles_deploy)- create roles and grants permissions
  - user deployment (key: users_deploy) - create users and grants permissions/roles
  - user removal (key: users_remove) - drop users
  - password deployment (key: passwd_deploy) - changing user password

##### Deployment Processes
  1. Upload database files and deployment files via upload page.
  2. Fill in the database file name and deployment file name; then click "Deploy" button.
  