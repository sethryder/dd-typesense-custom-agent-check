import urllib.request
import json

from checks import AgentCheck

class TypesenseCheck(AgentCheck):

  def check(self, instance):

    host = instance['host']
    protocol = instance['protocol']
    api_key = instance['api_key']

    headers = {'X-TYPESENSE-API-KEY': api_key}

    #metrics
    req = urllib.request.Request(protocol + '://' + host + '/metrics.json', headers=headers)
    with urllib.request.urlopen(req) as response:
        metrics = json.loads(response.read().decode())

    for metric_name, metric in metrics.items():
        if 'system' in metric_name:
          self.gauge('typesense.system.' + metric_name.replace('system_', ''), metric, tags=['typesense_host:' + host])
        else:
          self.gauge('typesense.' + metric_name.replace('typesense_', ''), metric, tags=['typesense_host:' + host])

    #stats
    req = urllib.request.Request(protocol + '://' + host + '/stats.json', headers=headers)
    with urllib.request.urlopen(req) as response:
        stats = json.loads(response.read().decode())

    for stat_name, stat in stats.items():
        if stat_name == 'latency_ms':
          for r, latency in stat.items():
            r_split = r.split(' ')
            method = r_split[0]
            resource = r_split[1]
            self.gauge('typesense.latency', latency, tags=['method:' + method, 'resource:' + resource, 'typesense_host:' + host])
        elif stat_name == 'requests_per_second':
          for r, request_per_second in stat.items():
            r_split = r.split(' ')
            method = r_split[0]
            resource = r_split[1]
            self.gauge('typesense.requests_per_second', request_per_second, tags=['method:' + method, 'resource:' + resource, 'typesense_host:' + host])
        else:
          self.gauge('typesense.' + stat_name, stat, tags=['typesense_host:' + host])

    #health
    req = urllib.request.Request(protocol + '://' + host + '/health', headers=headers)
    with urllib.request.urlopen(req) as response:
        health = json.loads(response.read().decode())

    health_status = 0

    if health['ok'] == True:
      health_status = 1

    self.gauge('typesense.health', health_status, tags=['typesense_host:' + host])
