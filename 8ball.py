#! /usr/bin/env python3

"""
Leif Gregory <leif@devtek.org>
8ball.py v0.1
Tested to Python v3.10.7

Description:
Returns a random choice of responses.

Changelog:
20230319 -  Initial code

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import random

responses = [
    "You will have bad luck today.",
    "Go back to bed, today is gonna suck!",
    "You will do well today.",
    "You will have great luck today.",
    "Everything will go your way today!"
]

print(f"8Ball sez: {random.choice(responses)}")