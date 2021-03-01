# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Creates a Container VM with the provided Container manifest."""

import container_man
import common

def GenerateConfig(context):
  """Generate configuration."""

  res = []
  base_name = (context.env['deployment'] + '-selenium-vm')    
          
  # Properties for the container-based instance.
  instance = {
      'zone': context.properties['zone'],
      'machineType': common.ZonalComputeUrl(context.env['project'],
                                     context.properties['zone'],
                                     'machineTypes',
                                     context.properties['machine']),
      'metadata': {
          'items': [{
              'key': 'gce-container-declaration',
              'value': container_man.selenium()
              },{
              'key': 'google-logging-enabled',
              'value': 'true'
          }]
      },
      'disks': [{
          'deviceName': 'boot',
          'type': 'PERSISTENT',
          'autoDelete': True,
          'boot': True,
          'initializeParams': {
              'diskName': base_name + '-disk',
              'sourceImage': common.GlobalComputeUrl('cos-cloud',
                                              'images',
                                              'family/cos-stable')
              },
      }],
      'networkInterfaces': [{
          'accessConfigs': [{
              'name': 'external-nat',
              'type': 'ONE_TO_ONE_NAT'
              }],
          'network': common.GlobalComputeUrl(context.env['project'],
                                      'networks',
                                      'default')
      }],
      'serviceAccounts': [{
          'email': 'default',
          'scopes': [
            "https://www.googleapis.com/auth/logging.write",
            "https://www.googleapis.com/auth/monitoring.write"
          ]
      }]
  }
  
  res.append({
      'name': base_name,
      'type': 'compute.v1.instance',
      'properties': instance
  })
  
  # Resources to return.
  
  resources = {
      'resources': res,
  }

  return resources
