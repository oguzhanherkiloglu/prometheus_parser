import requests
import time
import random
from os import path

from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server


def get_data_from_api():
    url = 'https://visualizer.nestcloud.ch/Realtime/data/3200000_3200001_3200002_3200003_3200004_3200005_3200006_3200008_3200009_3200010_3200011_3200012_3200013_3200014_3200016_3200017'
    #print(url)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("GET", url, headers=headers)
    if response is not None:
        if response.status_code == 200:
            # result_list=[]
            response_as_json = response.json()
            # print(type(response_as_json))
            # print(response_as_json)
            # print(len(response_as_json))
            # for element in range(len(response_as_json)):
            # print(response_as_json[element])
            # temp_dict = {}
            # temp_dict = response_as_json[element]
            # result_list.append(temp_dict['value'])
            # print(result_list)
    return response_as_json


class MeteorologyCollector(object):
    def __init__(self):
        pass

    def collect(self):
        queried_data = get_data_from_api()
        gauge1 = GaugeMetricFamily("empa_building_outside_temperature",
                                   "Ambient Temperature of Empa from rooftop Whether Station",
                                   labels=['Sensor_ID', 'DataPoint_Unit'])

        gauge2 = GaugeMetricFamily("empa_building_outside_humidity",
                                   "Ambient Humidity of Empa from rooftop Whether Station",
                                   labels=['Sensor_ID', 'DataPoint_Unit'])

        gauge3 = GaugeMetricFamily("empa_building_outside_relative_humidity",
                                   "Ambient Relative Humidity of Empa from rooftop Whether Station",
                                   labels=['Sensor_ID' , 'DataPoint_Unit'])

        gauge4 = GaugeMetricFamily("empa_building_outside_absolute_air_pressure",
                                   "Ambient Air Pressure of Empa from rooftop Whether Station",
                                   labels=['Sensor_ID', 'DataPoint_Unit'])

        gauge5 = GaugeMetricFamily("empa_building_outside_wind_speed",
                                   "Ambient Wind speed of Empa from rooftop Whether Station",
                                   labels=['Sensor_ID', 'DataPoint_Unit'])

        gauge6 = GaugeMetricFamily("empa_building_outside_wind_speed_avarage",
                                   "Ambient Wind Speed Avarage of Empa from rooftop Whether Station",
                                   labels=['Sensor_ID', 'DataPoint_Unit'])

        gauge7 = GaugeMetricFamily("empa_building_outside_wind_direction",
                                   "Ambient Wind Direction of Empa from rooftop Whether Station",
                                   labels=['Sensor_ID', 'DataPoint_Unit'])

        gauge8 = GaugeMetricFamily("empa_building_outside_global_solar_radiation",
                                   "Ambient Global Solar Radiation of Empa from rooftop Whether Station",
                                   labels=['Sensor_ID', 'DataPoint_Unit'])

        gauge9 = GaugeMetricFamily("empa_building_outside_brightness_north",
                                   "Ambient Brightness North of Empa from rooftop Whether Station",
                                   labels=['Sensor_ID', 'DataPoint_Unit'])

        gauge10 = GaugeMetricFamily("empa_building_outside_brightness_east",
                                    "Ambient Brightness East of Empa from rooftop Whether Station",
                                    labels=['Sensor_ID', 'DataPoint_Unit'])

        gauge11 = GaugeMetricFamily("empa_building_outside_brightness_south",
                                    "Ambient Brightness South of Empa from rooftop Whether Station",
                                    labels=['Sensor_ID', 'DataPoint_Unit'])

        gauge12 = GaugeMetricFamily("empa_building_outside_brightness_west",
                                    "Ambient Brightness West of Empa from rooftop Whether Station",
                                    labels=['Sensor_ID', 'DataPoint_Unit'])

        gauge13 = GaugeMetricFamily("empa_building_outside_dusk",
                                    "Ambient Dusk of Empa from rooftop Whether Station",
                                    labels=['Sensor_ID', 'DataPoint_Unit'])

        gauge14 = GaugeMetricFamily("empa_building_outside_height_above_NN",
                                    "Ambient Height above NN of Empa from rooftop Whether Station",
                                    labels=['Sensor_ID', 'DataPoint_Unit'])

        gauge15 = GaugeMetricFamily("empa_building_outside_dev_point_temperature",
                                    "Ambient Dev Point Temperature of Empa from rooftop Whether Station",
                                    labels=['Sensor_ID', 'DataPoint_Unit'])

        gauge16 = GaugeMetricFamily("empa_building_outside_relative_air_pressure",
                                    "Ambient Relative Air Pressure of Empa from rooftop Whether Station",
                                    labels=['Sensor_ID', 'DataPoint_Unit'])
        gauge1.add_metric(['65NT_MET51_B870_M00', 'Celcius'], queried_data[0]['value'])
        yield gauge1
        gauge2.add_metric(['65NT_MET51_B870_M01', 'g/m3'], queried_data[1]['value'])
        yield gauge2
        gauge3.add_metric(['65NT_MET51_B870_M02','%'], queried_data[2]['value'])
        yield gauge3
        gauge4.add_metric(['65NT_MET51_B870_M03', 'h/Pa'], queried_data[3]['value'])
        yield gauge4
        gauge5.add_metric(['65NT_MET51_B870_M04', 'm/s'], queried_data[4]['value'])
        yield gauge5
        gauge6.add_metric(['65NT_MET51_B870_M05','m/s'], queried_data[5]['value'])
        yield gauge6
        gauge7.add_metric(['65NT_MET51_B870_M06', 'angle'], queried_data[6]['value'])
        yield gauge7
        gauge8.add_metric(['65NT_MET51_B870_M08', 'W/m2'], queried_data[7]['value'])
        yield gauge8
        gauge9.add_metric(['65NT_MET51_B870_M09', 'kLux'], queried_data[8]['value'])
        yield gauge9
        gauge10.add_metric(['65NT_MET51_B870_M10', 'kLux'], queried_data[9]['value'])
        yield gauge10
        gauge11.add_metric(['65NT_MET51_B870_M11', 'kLux'], queried_data[10]['value'])
        yield gauge11
        gauge12.add_metric(['65NT_MET51_B870_M12', 'kLux'], queried_data[11]['value'])
        yield gauge12
        gauge13.add_metric(['65NT_MET51_B870_M13', 'lux'], queried_data[12]['value'])
        yield gauge13
        gauge14.add_metric(['65NT_MET51_B870_M14', 'm'], queried_data[13]['value'])
        yield gauge14
        gauge15.add_metric(['65NT_MET51_B870_M16', 'Celcius'], queried_data[14]['value'])
        yield gauge15
        gauge16.add_metric(['65NT_MET51_B870_M17', 'hPa'], queried_data[15]['value'])
        yield gauge16


def prepare_data_for_prometheus():
    print(queried_data)
    for element in range(len(queried_data)):
        print(element)
        print(queried_data[element]['value'])


if __name__ == '__main__':
    start_http_server(9000)
    REGISTRY.register(MeteorologyCollector())
    while True:
        #prepare_data_for_prometheus()
        time.sleep(40)