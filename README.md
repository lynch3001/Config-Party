# Config-Party

This is a very basic....very rudimentary....Config tool.

There are a few elements to this:

1. All config files to be placed in 'Configs'

2. place the name of the config file in config-list.csv with the location they are to be copied to in the second column

3. Place IP addresses in serverToConfig.csv, with optional Server name in column 2

4. Run script, It will ask you for your username and password that you use to ssh to these servers. 

5. Script will back up files to Dir "backups" with timedate stamp

6. Config files to pushed and over written. 



TO-DO: 
Add command after files have been pushed to restart service that it is associated with. 
