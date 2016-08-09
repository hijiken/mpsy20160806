# This file is part of "MPS Yokohama Deep Learning Series Day 08/06/2016"
#
# "MPS Yokohama Deep Learning Series Day 08/06/2016"
# is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# "MPS Yokohama Deep Learning Series Day 08/06/2016"
# is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
# (c) Junya Kaneko <jyuneko@hotmail.com>


import numpy as np


def ma(history, n):
    return np.array([0, ] * (n - 1) + [np.average(history[i - n: i]) for i in range(n, len(history) + 1)])
