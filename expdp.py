#EXPORT USER
 
import os
import subprocess
import sys
 
'''Setting database environment'''
def set_db_env(dbenv):
	# set up some environment variables
	dbenv["PATH"] = os.environ["PATH"]
	dbenv["ORACLE_HOME"] = os.getenv("ORACLE_HOME")
	dbenv["TNS_ADMIN"] = os.getenv("TNS_ADMIN")
	dbenv["LD_LIBRARY_PATH"] = os.getenv("LD_LIBRARY_PATH")
 
'''DB export'''
def db_export(dbenv):
	db_user = sys.argv[1]
	db_pass = sys.argv[2]
	db_alias = sys.argv[3]
	schema = sys.argv[4]
	dump_file = sys.argv[5]
	expdp_args = db_user + '/' + db_pass + '@' + db_alias + ' SCHEMAS=' + 
			schema + ' DUMPFILE=' + dump_file + 
			' DIRECTORY=DATA_PUMP_DIR'
	db_exp_work = subprocess.Popen(["expdp", expdp_args], 
				stdout=subprocess.PIPE, env=dbenv)
	if db_exp_work.wait() != 0:
		print "db_export() failed!"
		raise Exception("db_export() failed!")
	print "db_export() end!"
 
'''Printing help function'''
def help():
	print "Usage : %s db_user db_pass db_alias schema_to_export dump_file" 
		%(sys.argv[0])
 
if __name__=='__main__':
	if len(sys.argv) != 6:
		help()
		sys.exit(1)
	dbenv = {}
	set_db_env(dbenv)
	db_export(dbenv)
And you can run it like this :

Shell

tarek@tarek-ubuntu-server:~ ./oracle_export.py pm media ORCLUBUNTU pm pmdb_20160306.dmp

Export: Release 11.2.0.2.0 - Production on Sun Mar 6 00:24:41 2016

Copyright (c) 1982, 2009, Oracle and/or its affiliates. All rights reserved.

Connected to: Oracle Database 11g Enterprise Edition Release 11.2.0.1.0 - 64bit Production
With the Partitioning, OLAP, Data Mining and Real Application Testing options
Starting "PM"."SYS_EXPORT_SCHEMA_01": pm/********@ORCLUBUNTU SCHEMAS=pm DUMPFILE=pmdb_20160306.dmp DIRECTORY=DATA_PUMP_DIR
Estimate in progress using BLOCKS method...
Processing object type SCHEMA_EXPORT/TABLE/TABLE_DATA
Total estimation using BLOCKS method: 10.68 MB
Processing object type SCHEMA_EXPORT/PRE_SCHEMA/PROCACT_SCHEMA
Processing object type SCHEMA_EXPORT/TYPE/TYPE_SPEC
Processing object type SCHEMA_EXPORT/TABLE/TABLE
Processing object type SCHEMA_EXPORT/TABLE/INDEX/INDEX
Processing object type SCHEMA_EXPORT/TABLE/CONSTRAINT/CONSTRAINT
Processing object type SCHEMA_EXPORT/TABLE/INDEX/STATISTICS/INDEX_STATISTICS
Processing object type SCHEMA_EXPORT/TABLE/COMMENT
Processing object type SCHEMA_EXPORT/TABLE/CONSTRAINT/REF_CONSTRAINT
Processing object type SCHEMA_EXPORT/TABLE/STATISTICS/TABLE_STATISTICS
. . exported "PM"."ONLINE_MEDIA" 7.854 MB 9 rows
. . exported "PM"."PRINT_MEDIA" 190.2 KB 4 rows
. . exported "PM"."TEXTDOCS_NESTEDTAB" 87.74 KB 12 rows
Master table "PM"."SYS_EXPORT_SCHEMA_01" successfully loaded/unloaded
******************************************************************************
Dump file set for PM.SYS_EXPORT_SCHEMA_01 is:
/u01/app/oracle/product/11.2.0/db_1/rdbms/log/pmdb_20160306.dmp
Job "PM"."SYS_EXPORT_SCHEMA_01" successfully completed at 00:25:17

db_export() end!
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
tarek@tarek-ubuntu-server:~ ./oracle_export.py pm media ORCLUBUNTU pm pmdb_20160306.dmp
 
Export: Release 11.2.0.2.0 - Production on Sun Mar 6 00:24:41 2016