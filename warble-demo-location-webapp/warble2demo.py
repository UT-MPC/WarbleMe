#!/usr/bin/env python

# Copyright 2016 Google Inc.
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

# [START imports]
import os
import json
import logging

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

trajectory = {}
currentLocation = ""


# [START main_page]
class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('layouts/index.html')
        self.response.write(template.render(template_values))
# [END main_page]


class SaveTrajectory(webapp2.RequestHandler):
    def post(self):
        jsonTrajectoryString = self.request.body
        logging.info(jsonTrajectoryString)

        global trajectory
        trajectory = json.loads(jsonTrajectoryString)


class LoadTrajectory(webapp2.RequestHandler):
    def get(self):
        global trajectory
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(trajectory))


class SaveCurrentLocation(webapp2.RequestHandler):
    def post(self):
        global currentLocation
        currentLocation = self.request.body.strip("\"")
        logging.info(self.request.body)


class LoadCurrentLocation(webapp2.RequestHandler):
    def get(self):
        global currentLocation
        self.response.write(currentLocation)


# [START app]
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/saveTrajectory', SaveTrajectory),
    ('/loadTrajectory', LoadTrajectory),
    ('/saveCurrentLocation', SaveCurrentLocation),
    ('/loadCurrentLocation', LoadCurrentLocation),
], debug=True)
# [END app]
