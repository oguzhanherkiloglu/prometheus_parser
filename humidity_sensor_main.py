import datetime

import requests

import settings_humidity_sensor as settings

import collections

import logging

logger = logging.getLogger(__name__)


def get_data_from_prometheus():
    for prometheus_instance in settings.PROMETHEUS_INSTANCES:
        url = 'http://' + settings.PROMETHEUS_URL_AND_PORT + '/api/v1/query_range?query={instance=\"' + prometheus_instance + '\"}&start=' + settings.PROMETHEUS_START + '&end=' + settings.PROMETHEUS_END + '&step=' + settings.PROMETHEUS_STEP
        # print(url)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("GET", url, headers=headers)
        if response is not None:
            if response.status_code == 200:
                response_as_json = response.json()
                json_response, file_path = convert_json_to_proper_json_array(
                    response_as_json["data"]["result"])
                text_file = open(file_path, "w")
                write_data_to_txt(text_file, str(prometheus_instance) + " SERVER VALUES")
                logger.info(str(prometheus_instance) + " SERVER VALUES")
                result_dict = dict()
                for object_key, object_value in json_response.items():
                    result_dict[convert_epoch_time_to_datetime(object_key)] = object_value
                    write_data_to_txt(text_file, str(result_dict))
                    logger.info(result_dict)
                    logger.info('\n')
                    result_dict.clear()
                close_txt_file(text_file)


def convert_json_to_proper_json_array(json_response):
    object_dict = collections.defaultdict(list)
    file_path = settings.PROMETHEUS_TXT_FILE_PATH
    for object in json_response:
        if (object['metric'].get('__name__') is not None) and (
                object['metric'].get('__name__') == 'humiSensorValue'):
            if object['metric'].get('__name__') == 'humiSensorValue':
                for object_values in object['values']:
                    object_dict[object_values[0]].append({
                        settings.HUMIDITY_SENSOR_LABELS.get(object['metric'].get('humiSensorIndex')): round(
                            (int(object_values[1]) / 10), 2)
                    })

    return object_dict, file_path


def convert_epoch_time_to_datetime(epoch_time):
    datetime_time = datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
    return str(datetime_time)


def write_data_to_txt(text_file, string):
    text_file.write(string + "\n")
    print(string)
    print('\n')


def close_txt_file(text_file):
    text_file.close()


if __name__ == '__main__':
    get_data_from_prometheus()
