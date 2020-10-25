
'''
This is Class for ycn agent libvirt Guest Monitoring

Author : Dhanasekara Pandian
Email  : sekar5in@gmail.com
CopyRights : All Rights are Reserved
'''

import os
from coreutils import domconn, domaction
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError
from coreutils.dataformat import dict_to_json
import json
import pickle


def main():
    while True:
        from datetime import datetime
        startTime = datetime.now()

        print("Current Working Directory :", os.getcwd())

        # Ensure read write call is running with administrator privileges
        conn = domconn.DomainStatus('ro')

        # Connection
        conn_obj, conn_return = conn.connection()
        action_obj = domaction.DomainAction(conn_return)

        # list all registered domains count by status
        #print(action_obj.domain_status()+action_obj.resource_status()+ time.asctime(time.localtime(time.time())))

        monitor_parameters = {"domainStatus": action_obj.domain_status(),
                              "nodeStatus": action_obj.resource_status(),
                              "vmStatus": action_obj.stats(),
                              "created At": time.asctime(time.localtime(time.time()))
                              }

        # disconnection
        conn.disconnection(conn_obj)

        producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                 bootstrap_servers=['kafka1:9092', 'kafka2:9092', 'kafka3:9092'], linger_ms=10)

        # print(monitor_parameters)
        data = dict_to_json(monitor_parameters)
        # data = json.dumps(monitor_parameters)
        print(data)
        producer.send('kvm-monitor', json.loads(data))
        producer.flush()
        print("Data Pushed and Waiting for 30 secs")
        print(datetime.now() - startTime)
        time.sleep(30)


# Boiler Plate
if __name__ == '__main__':
    main()

 