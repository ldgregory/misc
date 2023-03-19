#! /usr/bin/env python3

"""
Leif Gregory <leif@devtek.org>
dieroller.py v0.1
Tested to Python v3.10.7

Description:


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
import re


def roll(sets):
    pattern = '^(\d+)d(\d+)([+-]\d+)?$'  # (2)d(10)(+5)
    rolled_values = []
    total_rolls_value = []

    for set in sets.split(','):
        rolls = re.search(pattern, set)
        num_of_rolls = rolls.group(1)
        die = rolls.group(2)
        modifier = rolls.group(3) if rolls.group(3) is not None else 0

        for x in range(int(num_of_rolls)):
            rolled = random.randint(1, int(die)) + int(modifier)
            total_rolls_value.append(rolled if rolled > 0 else 0)  # no negative numbers
            rolled_values.append(f'd{die}{"" if modifier == 0 else modifier}: {str(rolled)}')

    return rolled_values, total_rolls_value


def main():
    sets = input('Input rolls in form of 1d20, 5d12 etc.: ').lower().replace(' ', '')
    rolled_values, total_rolls_value = roll(sets)
    
    print(f'Rolls: {", ".join(str(x) for x in rolled_values)}')
    print(f'\nTotal: {sum(total_rolls_value)}')


if __name__ == '__main__':
    main()
