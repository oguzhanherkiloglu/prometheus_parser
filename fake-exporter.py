import datetime

import datetime

import requests

import settings

import collections

import logging

logger = logging.getLogger(__name__)


def get_data_from_prometheus():
    current_datetime = datetime.datetime.now()
    date_start = datetime.datetime.now() - datetime.timedelta(minutes=180)
    date_start = date_start.strftime('%Y-%m-%dT%H:%M:%S')
    modified_date_start = date_start + '.000Z'
    date_end = datetime.datetime.now() - datetime.timedelta(minutes=179)
    date_end = date_end.strftime('%Y-%m-%dT%H:%M:%S')
    modified_date_end = date_end + '.999Z'
    print(modified_date_start)
    print(modified_date_end)
    url = 'http://' + settings.PROMETHEUS_URL_AND_PORT + '/api/v1/query_range?query={instance=\"' + '192.168.10.50' + '\"}&start=' + modified_date_start + '&end=' + modified_date_end + '&step=' + settings.PROMETHEUS_STEP
    print(url)
    headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("GET", url, headers=headers)
    if response is not None:
        if response.status_code == 200:
            response_as_json = response.json()
            #print(type(response_as_json))
            #print(response_as_json)
            json_response = convert_json_to_proper_json_array(response_as_json["data"]["result"])
            print(type(json_response))
            print(json_response)


def convert_json_to_proper_json_array(json_response):
    object_dict = collections.defaultdict(list)
    for object in json_response:
        for object_values in object['values']:
            if (object['metric'].get('__name__') is not None) and (
                    object['metric'].get('name') == 'HSC Input Power'):
                    labels =
                    object_dict[object_values[0]].append({object['metric']['name']: object_values[1]})

    return object_dict



if __name__ == '__main__':
    get_data_from_prometheus()
