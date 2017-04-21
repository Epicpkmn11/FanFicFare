# -*- coding: utf-8 -*-

# Copyright 2011 Fanficdownloader team, 2015 FanFicFare team
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
#

from ..htmlcleanup import stripHTML

# Software: eFiction
from base_efiction_adapter import BaseEfictionAdapter

class TheDelphicExpanseComAdapter(BaseEfictionAdapter):
    ''' This adapter will download stories from the
       'Taste of Poison, the Fanfiction of Arsenic Jade' site '''

    @staticmethod
    def getSiteDomain():
        return 'www.thedelphicexpanse.com'

    @classmethod
    def getPathToArchive(self):
        return '/archive'

    @classmethod
    def getSiteAbbrev(self):
        return 'tdec'

    @classmethod
    def getDateFormat(self):
        return "%B %d, %Y"

def getClass():
    return TheDelphicExpanseComAdapter