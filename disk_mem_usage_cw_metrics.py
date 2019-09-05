#! /usr/bin/env python
import sys
import re
from datetime import datetime
import boto3
import os
import requests

def collect_memory_usage():
    meminfo = {}
    pattern = re.compile('([\w\(\)]+):\s*(\d+)(:?\s*(\w+))?')
    with open('/proc/meminfo') as f:
        for line in f:
            match = pattern.match(line)
            if match:
                # For now we don't care about units (match.group(3))
                meminfo[match.group(1)] = float(match.group(2))
    return meminfo

def collect_disk_usage():
    return os.statvfs("/")

def send_multi_metrics(instance_id, instance_type, metrics, session):
    '''
    Send multiple metrics to CloudWatch
    metrics is expected to be a map of key -> value pairs of metrics
    '''

    client = session.client('cloudwatch', region_name=session.region_name)
    now = datetime.utcnow()
    response = client.put_metric_data(
        Namespace='EC2/Health',
        MetricData=[
            {
                'MetricName': 'DiskUsage',
                'Dimensions': [
                    {
                        'Name': 'ENV',
                        'Value': os.environ['ENV']
                    },
                    {
                        'Name': 'InstanceId',
                        'Value': instance_id
                    },
                    {
                        'Name': 'InstanceType',
                        'Value': instance_type
                    },
                ],
                'Timestamp': now,
                'Value': metrics['DiskUsage'],
                'Unit': 'Percent'
            },
            {
                'MetricName': 'MemoryUsage',
                'Dimensions': [
                    {
                        'Name': 'ENV',
                        'Value': os.environ['ENV']
                    },
                    {
                        'Name': 'InstanceId',
                        'Value': instance_id
                    },
                    {
                        'Name': 'InstanceType',
                        'Value': instance_type
                    },
                ],
                'Timestamp': now,
                'Value': metrics['MemUsage'],
                'Unit': 'Percent'
            },
        ]
    )

if __name__ == '__main__':
    instance_id = requests.get("http://169.254.169.254/latest/meta-data/instance-id").text
    instance_type = requests.get("http://169.254.169.254/latest/meta-data/instance-type").text
    mem_usage = collect_memory_usage()
    disk_usage = collect_disk_usage()

    mem_free = mem_usage['MemFree'] + mem_usage['Buffers'] + mem_usage['Cached']
    mem_used = mem_usage['MemTotal'] - mem_free

    metrics = {
        'MemUsage': mem_used / mem_usage['MemTotal'] * 100,
        'DiskUsage': 100 - ((disk_usage.f_frsize * disk_usage.f_bfree) / (disk_usage.f_frsize * disk_usage.f_blocks ) * 100)
    }

    session = boto3.session.Session()
    send_multi_metrics(instance_id, instance_type, metrics, session)
