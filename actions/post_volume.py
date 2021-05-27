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
# __license__ = "Apache2.0""
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"


from lib.actions import HpeNimbleBaseAction

class Volumes(HpeNimbleBaseAction):
    def run(self,name=None,size=None,limit_iops=None):
        vol = 'fail'
        volz = self.client.volumes.get(name=name)
        if volz is None:
            #
            vol = self.client.volumes.create(name=name, size=size, limit_iops=limit_iops)
        return (vol)
