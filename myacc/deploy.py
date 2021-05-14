import sys
import os.path
from os import path
import yaml
import datetime
from sqlalchemy import *
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from user import *
from role import *
from db import *
from log import log


def conf_read(conf_file, option=None):
    try:
        with open(conf_file, 'r') as stream:
          documents = yaml.safe_load(stream)
        if option == 'databases': opt = 'db'
        elif option == 'users_deploy': opt = 'user'
        elif option == 'roles_deploy': opt = 'role'
        elif option == 'users_remove': opt = 'user'
        elif option == 'passwd_deploy': opt = 'user'
        docs=documents[option]
        confs=[]
        for _doc in docs:
          doc=_doc[opt]
          confs.append(doc)
        return confs
    except yaml.YAMLError as exc:
      log("--")

def conf_type_read(conf_file):
    try:
      log(conf_file + ' file exits? ' + str(path.exists(conf_file)) + '\n' )
      if path.exists(conf_file) :
        with open(conf_file, 'r') as stream:
          documents = yaml.safe_load(stream)
        if 'users_deploy' in documents.keys(): return 'users_deploy'
        if 'roles_deploy' in documents.keys(): return 'roles_deploy'
        if 'users_remove' in documents.keys(): return 'users_remove'
        if 'passwd_deploy' in documents.keys(): return 'passwd_deploy'
    except yaml.YAMLError as exc:
      log("--")


def deployment(configs, deploy_type):
    for user_conf in configs:
      log("_" * 30)
      user_exists_result=User.exists(user_conf, engine)

      if len(user_exists_result) == 0 and deploy_type == 'users_deploy':
        User.create(user_conf, engine)
        if 'roles' in user_conf: User.grant_roles(user_conf, engine)
        if 'grants' in user_conf: User.grant_permissions(user_conf, engine)

      elif len(user_exists_result) == 0 and deploy_type == 'roles_deploy':
        Role.create(user_conf, engine)
        if 'roles' in user_conf: User.grant_roles(user_conf, engine)
        if 'grants' in user_conf: User.grant_permissions(user_conf, engine)

      elif len(user_exists_result) > 0 and deploy_type in ['users_deploy', 'roles_deploy']:
        user_show_grants_result_set = User.show_grants(user_conf, engine)
        User.revoke(user_show_grants_result_set, engine)
        if 'roles' in user_conf: User.grant_roles(user_conf, engine)
        if 'grants' in user_conf: User.grant_permissions(user_conf, engine)

      elif len(user_exists_result) > 0 and deploy_type == 'users_remove':
        User.drop(user_conf, engine)

      elif len(user_exists_result) > 0 and deploy_type == 'passwd_deploy':
        User.passwd(user_conf, engine)


   
######################
###  MAIN  ###########
######################
os.system('clear')
dbfile = sys.argv[1]
db_configs=conf_read(dbfile, 'databases')

deployment_file = sys.argv[2]
deployment_type = conf_type_read(deployment_file)
deployment_configs = conf_read(deployment_file, deployment_type)

log(f"Deployment Method: {deployment_type}")

SQL_TRACE=True

#log(db_configs)
for db_conf in db_configs:
  log("_" * 100)
  engine = Db.dbconn(db_conf,SQL_TRACE)
  session=Session(engine)
  log(engine)
  metadata = MetaData()
  #metadata.reflect(engine, only=['sys_config'])
  Base = automap_base(metadata=metadata)
  Base.prepare()
  
  if len(deployment_configs) > 0: deployment(deployment_configs, deployment_type)

