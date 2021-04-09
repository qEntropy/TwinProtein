import pandas as pd
import numpy as np

from plotnine import *
from plotnine.data import *



d = {'xco': [4, 2, 1], 'yco': [165.803, 168.454, 167.864]}
df = pd.DataFrame(data=d)

XLIM = (0, 5)
YLIM = (130, 190)

x_axis = 'Executors'

db = "db-smaller.txt measurements"



428.594

print(df)

print(type(df))

x = ggplot(df, aes(x='xco', y='yco')) +\
  geom_line() +  geom_text(aes(label = "yco"), va = 'top', size = 10) + \
  labs(x=x_axis, y='Time Taken in Seconds') + \
  geom_point() + coord_cartesian(xlim = XLIM, ylim = YLIM) + \
  ggtitle(db)

print(x)


