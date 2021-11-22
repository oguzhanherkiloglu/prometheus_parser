import main
import dewpoint_sensor_main
import temp_sensor_main
import humidity_sensor_main

if __name__ == '__main__':
    main.get_data_from_prometheus()
    dewpoint_sensor_main.get_data_from_prometheus()
    temp_sensor_main.get_data_from_prometheus()
    humidity_sensor_main.get_data_from_prometheus()