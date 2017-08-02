config = {
    "192.168.22.0/24": {"host": "192.168.22.231",
                        "interface": "br0"},
    "192.168.23.0/24": {"host": "192.168.23.180",
                        "interface": "br0"},
    "172.18.30.0/24": {"host": "172.18.30.11",
                       "interface": "br0"}
}
dbconfig = {
    "db_host": "192.168.23.206",
    "db_port": 3306,
    "db_username": "query_falcon",
    "db_password": "falcon_zewei",
    "db_default_db": "falcon_portal"
}
exclude_ip = ['172.18.30.3', '172.18.30.2', '172.18.30.1', '192.168.23.178', '192.168.23.179', '192.168.22.230',
              '192.168.22.228', '192.168.22.229']

error_ip_log = '/error.log'

current_host_file = 'current_host.log'
