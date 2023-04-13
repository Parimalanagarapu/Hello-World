import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('172.17.12.66', username='pnagarapu', password='Miracle@345345')
# stdin, stdout, stderr = client.exec_command('ls -l')
sftp_client = client.open_sftp()
# print(dir(sftp_client))
sftp_client.get("Path",'remote path')
sftp_client.put("transfer_file.py", "/home/transfer_file.py")
sftp_client.close()
client.close()