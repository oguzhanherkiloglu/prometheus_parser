import datetime

import pandas as pd
import requests

import settings


def get_data_from_prometheus():
    url = 'http://' + settings.PROMETHEUS_URL_AND_PORT + '/api/v1/query_range?query=tempSensorValue&tempSensorIndex=' + settings.TEMP_SENSOR_INDEX + '&start=' + settings.PROMETHEUS_START + '&end=' + settings.PROMETHEUS_END + '&step=' + settings.PROMETHEUS_STEP

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("GET", url, headers=headers)
    if response is not None:
        # print(response.text)
        if response.status_code == 200:
            response_as_json = response.json()
            intended_json = convert_json_to_proper_json_array(response_as_json["data"]["result"])
            return intended_json
        return None
    return None


def convert_json_to_proper_json_array(json_response):
    final_list = []
    for object in json_response:
        for object_values in object['values']:
            if object['metric'].get('tempSensorIndex') is not None:
                single_json_object = {
                    "tempSensorIndex": object['metric']['tempSensorIndex'],
                    "timestamp": convert_epoch_time_to_datetime(object_values[0]),
                    "value": object_values[1],
                }
                final_list.append(single_json_object)

    return final_list


def convert_epoch_time_to_datetime(epoch_time):
    datetime_time = datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
    return str(datetime_time)


def write_csv(data):
    try:
        df = pd.DataFrame.from_dict(data)
        df['timestamp'] = pd.to_datetime(df.timestamp, format='%Y-%m-%d %H:%M:%S')
        df['timestamp'] = df['timestamp'].dt.strftime('%d-%m-%Y %H:%M:%S')
        df = df.sort_values(["timestamp"], ascending=True)
        df.to_csv(settings.PROMETHEUS_CSV_PATH_TEMP, index=False)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    rectified_json = get_data_from_prometheus()
    if rectified_json is not None:
        write_csv(rectified_json)
