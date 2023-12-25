import os
import settings_empa_kubernetes as settings
import socket

def get_cpu_info_from_prometheus(ip_addess_of_host):
    url = 'http://' + settings.PROMETHEUS_URL_AND_PORT + '/api/v1/query?query=(count(node_cpu_seconds_total{mode="idle", instance=\"' + ip_addess_of_host + '\"}) without (cpu,mode))&time=' + settings.PROMETHEUS_START
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("GET", url, headers=headers)
    if response is not None:
        if response.status_code == 200:
            response_as_json = response.json()
            print(response_as_json['data']['result'])
            sample_list = []
            sample_list = response_as_json['data']['result']
            sample_dict = {}
            print(sample_list[0])
            print(type(sample_list[0]))
            sample_dict = sample_list[0]
            print(sample_dict['value'][1])
            print(type(response_as_json['data']['result']))

        return sample_dict['value'][1]


def get_servers_current_stats():
    for prometheus_instance in settings.SLAVE_NODES:
        response = os.system("ping -c 1 " + prometheus_instance)
        if response == 0:
            # temp_list = []
            print(f"{prometheus_instance} is up!")
            ip_address_of_host = socket.gethostbyname(prometheus_instance)
            print(ip_address_of_host)
            server_status.setdefault(f"{prometheus_instance}", []).append('UP')
            num_of_core = get_cpu_info_from_prometheus(f"ip_address_of_host")
            print(num_of_core)
            server_status.setdefault(f"{prometheus_instance}", []).append(56)
            server_status.setdefault(f"{prometheus_instance}", []).append(f"{ip_address_of_host}")

            # temp_list.append('UP')
            # temp_list.append('abc')
            # temp_list.append(56)
            # server_status[f"{prometheus_instance}"] = temp_list()
            # del temp_list[:]
        else:
            print(f"{prometheus_instance} is down!")
            server_status[f"{prometheus_instance}"] = 'DOWN'

        print(server_status)
