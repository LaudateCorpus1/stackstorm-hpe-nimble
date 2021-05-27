# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"


from lib.actions import HpeNimbleBaseAction
from datetime import datetime

class Alarms(HpeNimbleBaseAction):
    def run(self):
        # Connect to the system
        api = self.client
        # Setup some variables
        alarm_data = []
        # Get the arrays
        alarms = api.alarms.list()

        for a in alarms:

            entry = api.alarms.get(a.attrs['id']).attrs

            time = datetime.fromtimestamp(entry['onset_time']).strftime('%d-%m-%y, %H:%M:%S')

            alarmz = [
                    entry['status'],
                    time,
                    entry['severity'],
                    entry['category'],
                    entry['id']
                    ]

            alarm_data.append(alarmz)
        return alarm_data
