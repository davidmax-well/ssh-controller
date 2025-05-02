import paramiko
import json
import os
import curses

# Encapsulates the details and functionality related to an SSH server.

class Server:
    def __init__(self, name, host, username, key_file_path=None):
        self.name = name
        self.host = host
        self.username = username
        self._key_file_path = key_file_path # Private attribute

    @property
    def key_file_path(self):

        # Gives access to the private key path 
        return self.key_file_path                                   
    
    def connect(self):
        
        # Establish an SSH connection using the provided credentials
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            if self._key_file_path:
                key = paramiko.RSAKey.from_private_key_file(self._key_file_path)
                client.connect(self.host, username=self.username, pkey=key)
            else:
                raise ValueError("Private Key Path is not set!")
            return client
        except Exception as e:
            print(f"Connection failed! {e}")
            return None

    def set_key_path(self, path):

        # Set the private key path 
        if not path or not isinstance(path, str):
            raise ValueError("Invalid private key path!")
        self._key_file_path = path

    def get_server_info(self):

        #return basic info
        return {
            "name": self.name
            "host": self.host
            "username": self.username
        }