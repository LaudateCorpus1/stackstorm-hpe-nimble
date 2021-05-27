# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0.

# Unless required by applicable law. or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"

# A python script for getting a dictionary of switches

import pymongo
from lib.actions import MongoBaseAction


class loadDb(MongoBaseAction):
    def run(self, alarms):

        mydb = self.dbclient["app_db"]
        known = mydb["nimblealarms"]

        new_alarm={}

        for alarm in alarms:
            myquery = { "u_id" : alarm[4] }
            records = known.find(myquery).count()
            if records == 0:
                new_alarm['u_category']=alarm[3]
                new_alarm['u_severity']=alarm[2]
                new_alarm['u_time']=alarm[1]
                new_alarm['u_status']=alarm[0]
                new_alarm['u_id']=alarm[4]
                new_alarm['_id']=alarm[4]
                new_alarm['u_process']='no'
                write_record = known.insert_one(new_alarm)
                new_alarm={}

            else:
                records='Fail to write mongo record, possible duplicate'
                # write_record = process.insert_one(alarm)
        return (records)
