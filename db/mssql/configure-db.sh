#!/bin/bash
echo -e "\n>>> Setting up Data-Mart databases and permissions ...\n"
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -d master -i /mssql-init/setup.sql

echo -e "\n>>> Creating Tzdb schema for ${DM_SQLSVR_DATABASE} ...\n"
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -d ${DM_SQLSVR_DATABASE} -i /mssql-init/create_Tzdb_tables.sql
  #echo -e "\n>>> Parparing Tzdb data for ${DM_SQLSVR_DATABASE} ...\n"
  #/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -d ${DM_SQLSVR_DATABASE} -i /mssql-init/insert_Tzdb_data.sql

echo -e "\n>>> Creating Tzdb schema for ${LDM_SQLSVR_DATABASE} ...\n"
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -d ${LDM_SQLSVR_DATABASE} -i /mssql-init/create_Tzdb_tables.sql
  #echo -e "\n>>> Parparing Tzdb data for ${LDM_SQLSVR_DATABASE} ...\n"
  #/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -d ${LDM_SQLSVR_DATABASE} -i /mssql-init/insert_Tzdb_data.sql
