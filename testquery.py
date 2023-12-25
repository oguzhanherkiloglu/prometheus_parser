import datetime

import requests

import test_settings as settings

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