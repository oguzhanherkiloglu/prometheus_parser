import requests
import time
import random
from os import path

from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server


def get_data_from_api():
    url1 = 'https://visualizer.nestcloud.ch/Realtime/data/401130000_401130024_401130060_401130078_401191062_401130061_401130060_401130058_401130059_401130079_401130078_401130076_401130077_401130032_401130038_401130044_401130033'
    #print(url)
    headers1 = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response1 = requests.request("GET", url1, headers=headers1)
    url2 = 'https://visualizer.nestcloud.ch/Realtime/data/401130039_401130045_401130024_401130008_401130014_401130020_401130009_401130015_401130021_401130000_401191070_401191076_401191082_401191071_401191077_401191083_401191062_401190042'
    #print(url)
    headers2 = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response2 = requests.request("GET", url2, headers=headers2)
    if response1 and response2 is not None:
        if response1.status_code == 200 and response2.status_code ==200:
            # result_list=[]
            response_as_json1 = response1.json()
            response_as_json2 = response2.json()
            # print(type(response_as_json))
            # print(response_as_json)
            # print(len(response_as_json))
            # for element in range(len(response_as_json)):
            # print(response_as_json[element])
            # temp_dict = {}
            # temp_dict = response_as_json[element]
            # result_list.append(temp_dict['value'])
            # print(result_list)
    return response_as_json1, response_as_json2


class EmpaEnergyCollector(object):
    def __init__(self):
        pass

    def collect(self):
        queried_data1, queried_data2 = get_data_from_api()
        gauge1 = GaugeMetricFamily("power_thermal_and_electricity_power_datacenter_emergency_grid",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge2 = GaugeMetricFamily("power_thermal_and_electricity_power_cooling_system_emergency_grid",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge3 = GaugeMetricFamily("power_thermal_and_electricity_power_cooling_system_thermal",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge4 = GaugeMetricFamily("power_thermal_and_electricity_power_heating_system_thermal",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge5 = GaugeMetricFamily("power_thermal_and_electricity_power_datacenter_normal_grid",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge6 = GaugeMetricFamily("thermal_cooling_low_temperature_grid_flow",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge7 = GaugeMetricFamily("thermal_cooling_low_temperature_grid_power",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge8 = GaugeMetricFamily("thermal_cooling_low_temperature_grid_outlet_temperature",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge9 = GaugeMetricFamily("thermal_cooling_low_temperature_grid_inlet_temperature",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge10 = GaugeMetricFamily("thermal_heating_medium_temperature_grid_flow",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge11 = GaugeMetricFamily("thermal_heating_medium_temperature_grid_power",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge12 = GaugeMetricFamily("thermal_heating_medium_temperature_grid_outlet_temperature",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge13 = GaugeMetricFamily("thermal_heating_medium_temperature_grid_inlet_temperature",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge14 = GaugeMetricFamily("electricity_cooling_system_emergency_grid_current_l1",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge15 = GaugeMetricFamily("electricity_cooling_system_emergency_grid_current_l2",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge16 = GaugeMetricFamily("electricity_cooling_system_emergency_grid_current_l3",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge17 = GaugeMetricFamily("electricity_cooling_system_emergency_grid_voltage_l1",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge18 = GaugeMetricFamily("electricity_cooling_system_emergency_grid_voltage_l2",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge19 = GaugeMetricFamily("electricity_cooling_system_emergency_grid_voltage_l3",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge20 = GaugeMetricFamily("electricity_cooling_system_emergency_grid_active_power_total",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge21 = GaugeMetricFamily("electricity_datacenter_emergency_grid_current_l1",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge22 = GaugeMetricFamily("electricity_datacenter_emergency_grid_current_l2",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge23 = GaugeMetricFamily("electricity_datacenter_emergency_grid_current_l3",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge24 = GaugeMetricFamily("electricity_datacenter_emergency_grid_voltage_l1",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge25 = GaugeMetricFamily("electricity_datacenter_emergency_grid_voltage_l2",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge26 = GaugeMetricFamily("electricity_datacenter_emergency_grid_voltage_l3",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge27 = GaugeMetricFamily("electricity_datacenter_emergency_grid_active_power_total",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge28 = GaugeMetricFamily("electricity_datacenter_normal_grid_current_l1",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge29 = GaugeMetricFamily("electricity_datacenter_normal_grid_current_l2",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge30 = GaugeMetricFamily("electricity_datacenter_normal_grid_current_l3",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge31 = GaugeMetricFamily("electricity_datacenter_normal_grid_voltage_l1",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge32 = GaugeMetricFamily("electricity_datacenter_normal_grid_voltage_l2",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge33 = GaugeMetricFamily("electricity_datacenter_normal_grid_voltage_l3",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge34 = GaugeMetricFamily("electricity_datacenter_normal_grid_active_power_total",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])
        gauge35 = GaugeMetricFamily("battery_nest_active_power_total",
                                   "Data coming from Empa DC measurements",
                                   labels=['Sensor_ID', 'DataInfo', 'DataPoint_Unit'])

        gauge1.add_metric(['65NT_ELM04_P822_M00', 'el. active power total', 'kW'], queried_data1[0]['value'])
        yield gauge1
        gauge2.add_metric(['65NT_ELM04_P820_M00', 'th. active power total', 'kW'], queried_data1[1]['value'])
        yield gauge2
        gauge3.add_metric(['65NT_ULK02_P890_M00', 'th. power total', 'kW'], queried_data1[2]['value'])
        yield gauge3
        gauge4.add_metric(['65NT_ULK02_P891_M00', 'th. power total', 'kW'], queried_data1[3]['value'])
        yield gauge4
        gauge5.add_metric(['65NT_ELM01_P827_M00', 'el. active power total', 'kW'], queried_data1[4]['value'])
        yield gauge5
        gauge6.add_metric(['65NT_ULK02_B840_M00', 'flow', 'm3/h'], queried_data1[5]['value'])
        yield gauge6
        gauge7.add_metric(['65NT_ULK02_P890_M00', 'th. power total', 'kW'], queried_data1[6]['value'])
        yield gauge7
        gauge8.add_metric(['65NT_ULK02_B800_M00', 'forward temperature', 'Celcius'], queried_data1[7]['value'])
        yield gauge8
        gauge9.add_metric(['65NT_ULK02_B804_M00', 'return temperature', 'Celcius'], queried_data1[8]['value'])
        yield gauge9
        gauge10.add_metric(['65NT_ULK02_B841_M00', 'flow', 'm3/h'], queried_data1[9]['value'])
        yield gauge10
        gauge11.add_metric(['65NT_ULK02_P891_M00', 'th. power total', 'kW'], queried_data1[10]['value'])
        yield gauge11
        gauge12.add_metric(['65NT_ULK02_B801_M00', 'forward temperature', 'Celcius'], queried_data1[11]['value'])
        yield gauge12
        gauge13.add_metric(['65NT_ULK02_B805_M00', 'return temperature', 'Celcius'], queried_data1[12]['value'])
        yield gauge13
        gauge14.add_metric(['65NT_ELM04_P820_M02', 'el. current l1', 'A'], queried_data1[13]['value'])
        yield gauge14
        gauge15.add_metric(['65NT_ELM04_P820_M03', 'el. current l2', 'A'], queried_data1[14]['value'])
        yield gauge15
        gauge16.add_metric(['65NT_ELM04_P820_M04', 'el. current l3', 'A'], queried_data1[15]['value'])
        yield gauge16
        gauge17.add_metric(['65NT_ELM04_P820_M17', 'el. voltage l1', 'V'], queried_data1[16]['value'])
        yield gauge17
        gauge18.add_metric(['65NT_ELM04_P820_M21', 'el. voltage l2', 'V'], queried_data2[0]['value'])
        yield gauge18
        gauge19.add_metric(['65NT_ELM04_P820_M25', 'el. voltage l3', 'V'], queried_data2[1]['value'])
        yield gauge19
        gauge20.add_metric(['65NT_ELM04_P820_M00', 'el. active power total', 'kW'], queried_data2[2]['value'])
        yield gauge20
        gauge21.add_metric(['65NT_ELM04_P822_M02', 'el. current l1', 'A'], queried_data2[3]['value'])
        yield gauge21
        gauge22.add_metric(['65NT_ELM04_P822_M03', 'el. current l2', 'A'], queried_data2[4]['value'])
        yield gauge22
        gauge23.add_metric(['65NT_ELM04_P822_M04', 'el. current l3', 'A'], queried_data2[5]['value'])
        yield gauge23
        gauge24.add_metric(['65NT_ELM04_P822_M17', 'el. voltage l1', 'V'], queried_data2[6]['value'])
        yield gauge24
        gauge25.add_metric(['65NT_ELM04_P822_M21', 'el. voltage l2', 'V'], queried_data2[7]['value'])
        yield gauge25
        gauge26.add_metric(['65NT_ELM04_P822_M25', 'el. voltage l3', 'V'], queried_data2[8]['value'])
        yield gauge26
        gauge27.add_metric(['65NT_ELM04_P822_M00', 'el. active power total', 'kW'], queried_data2[9]['value'])
        yield gauge27
        gauge28.add_metric(['65NT_ELM01_P827_M02', 'el. current l1', 'A'], queried_data2[10]['value'])
        yield gauge28
        gauge29.add_metric(['65NT_ELM01_P827_M03', 'el. current l2', 'A'], queried_data2[11]['value'])
        yield gauge29
        gauge30.add_metric(['65NT_ELM01_P827_M04', 'el. current l3', 'A'], queried_data2[12]['value'])
        yield gauge30
        gauge31.add_metric(['65NT_ELM01_P827_M17', 'el. voltage l1', 'V'], queried_data2[13]['value'])
        yield gauge31
        gauge32.add_metric(['65NT_ELM01_P827_M21', 'el. voltage l2', 'V'], queried_data2[14]['value'])
        yield gauge32
        gauge33.add_metric(['65NT_ELM01_P827_M25', 'el. voltage l3', 'V'], queried_data2[15]['value'])
        yield gauge33
        gauge34.add_metric(['65NT_ELM01_P827_M00', 'el. active power total', 'kW'], queried_data2[16]['value'])
        yield gauge34
        gauge35.add_metric(['65NT_ELM01_P801_M00', 'main supply el. active power total', 'kW'], queried_data2[17]['value'])
        yield gauge35


def prepare_data_for_prometheus():
    print(queried_data)
    for element in range(len(queried_data)):
        print(element)
        print(queried_data[element]['value'])


if __name__ == '__main__':
    start_http_server(9001)
    REGISTRY.register(EmpaEnergyCollector())
    while True:
        #prepare_data_for_prometheus()
        time.sleep(40)