#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def teach(self, knowledge):
              self.knowledge = knowledge

    knowledge = [
                 "str is a data type in Python",
                 "programming is hard, but it's worth it",
                 "JavaScript async web request",
                 "Python function call definition",
                 "object-oriented teacher instance",
                 "programming computers hacking learning terminal",
                 "pipenv install pipenv shell",
                 "pytest -x flag to fail fast",
                ]