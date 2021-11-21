import datetime
import json
from collections import defaultdict

import pandas as pd
import requests

import settings


def get_data_from_prometheus():
    for prometheus_instance in settings.PROMETHEUS_INSTANCES:
        url = 'http://' + settings.PROMETHEUS_URL_AND_PORT + '/api/v1/query_range?query={instance=\"' + prometheus_instance + '\"}&start=' + settings.PROMETHEUS_START + '&end=' + settings.PROMETHEUS_END + '&step=' + settings.PROMETHEUS_STEP

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.request("GET", url, headers=headers)
        if response is not None:
            # print(response.text)
            if response.status_code == 200:
                response_as_json = response.json()
                convert_json_to_proper_json_array(
                    response_as_json["data"]["result"])
                # if intended_json is not None:
                #     write_csv(intended_json, intended_file_name)


def convert_json_to_proper_json_array(json_response):
    final_list = []
    intendedfilename = "test.csv"
    i = 0
    for object in json_response:
        required_json_object = {convert_epoch_time_to_datetime(object['values'][i][0]): ""}
        required_json_object_values_list = []
        required_json_object_values_dict = dict()
        # required_json_object = {convert_epoch_time_to_datetime(object['values'][i][0]): ""}
        for object_values in object['values']:
            intendedfilename = "Rack" + object['metric']['Rack_Cabinet'] + "firstrow" + object['metric'][
                'First_Row'] + "height" + object['metric']['Height'] + ".csv"
            if (object['metric'].get('name') is not None) and (
                    object['metric'].get('__name__') == 'ipmi_current_amperes') or (
                    object['metric'].get('__name__') == 'ipmi_fan_speed_rpm') or (
                    object['metric'].get('__name__') == 'ipmi_power_watts') or (
                    object['metric'].get('__name__') == 'ipmi_temperature_celsius') or (
                    object['metric'].get('__name__') == 'ipmi_sensor_value' and object['metric'].get(
                'name') == 'SYS Usage'):
                # {“12-09-2021 15:30:00” :{ “CPUTemp”: “50 C”, “inletTemp”: “17 C”, “pwrConsumption”: “500 Watts”, “systemUsage”: “70 percent”, “exhaustTemp”: “32” }}
                if object['metric'].get('__name__') == 'ipmi_current_amperes':
                    if object['metric']['name'] + "[Amper]" not in required_json_object_values_dict.keys():
                        required_json_object_values_list.append({
                            object['metric']['name'] + "[Amper]": object_values[1]
                        })
                        required_json_object_values_dict[object['metric']['name'] + "[Amper]"] = 'processed'

                elif object['metric'].get('__name__') == 'ipmi_fan_speed_rpm':
                    if object['metric']['name'] + "[RPM]" not in required_json_object_values_dict.keys():
                        required_json_object_values_list.append({
                            object['metric']['name'] + "[RPM]": object_values[1]
                        })
                        required_json_object_values_dict[object['metric']['name'] + "[RPM]"] = 'processed'

                elif object['metric'].get('__name__') == 'ipmi_power_watts':
                    if object['metric']['name'] + "[Watts]" not in required_json_object_values_dict.keys():
                        required_json_object_values_list.append({
                            object['metric']['name'] + "[Watts]": object_values[1]
                        })
                        required_json_object_values_dict[object['metric']['name'] + "[Watts]"] = 'processed'

                elif object['metric'].get('__name__') == 'ipmi_temperature_celsius':
                    if object['metric']['instance'] == '192.168.105.153' and object['metric']['id'] == '151':
                        if "CPU1" + object['metric']['name'] + "[C]" not in required_json_object_values_dict.keys():
                            required_json_object_values_list.append({
                                "CPU1" + object['metric']['name'] + "[C]": object_values[1]
                            })
                            required_json_object_values_dict[object['metric']['name'] + "[C]"] = 'processed'

                    else:
                        if object['metric']['name'] + "[C]" not in required_json_object_values_dict.keys():
                            required_json_object_values_list.append(
                                {
                                    object['metric']['name'] + "[C]": object_values[1]

                                })
                            required_json_object_values_dict[object['metric']['name'] + "[C]"] = 'processed'

                elif object['metric'].get('__name__') == 'ipmi_sensor_value' and object['metric'].get(
                        'name') == 'SYS Usage':
                    if object['metric']['name'] + "[%]" not in required_json_object_values_dict.keys():
                        required_json_object_values_list.append({
                            object['metric']['name'] + "[%]": object_values[1]
                        })
                        required_json_object_values_dict[object['metric']['name'] + "[%]"] = 'processed'
            required_json_object_values_dict.clear()
        if len(required_json_object_values_list) > 0:
            try:
                required_json_object[
                    convert_epoch_time_to_datetime(object['values'][i][0])] = required_json_object_values_list
                # print(required_json_object)
                # print('\n')
                final_list.append(required_json_object)
            except Exception as e:
                print('')

        i = i + 1
    print(final_list)
    print('\n')
    # return final_list, intendedfilename


def convert_epoch_time_to_datetime(epoch_time):
    datetime_time = datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
    return str(datetime_time)


def write_csv(data, intendedfilename):
    try:
        df = pd.DataFrame.from_dict(data)
        df['timestamp'] = pd.to_datetime(df.timestamp, format='%Y-%m-%d %H:%M:%S')
        df['timestamp'] = df['timestamp'].dt.strftime('%d-%m-%Y %H:%M:%S')
        df = df.sort_values(["timestamp"], ascending=True)
        df = df.drop(columns="id")
        df.to_csv(settings.PROMETHEUS_CSV_PATH_NAMED + intendedfilename, index=False)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_data_from_prometheus()
