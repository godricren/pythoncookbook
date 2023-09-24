import numpy as np

l1 = [1,2,3]
l2=[[1,2,3],[3,2,1],[-1,-3,-5]]
nd1 = np.array(l1)
nd2 = np.array(l2)

l3=['Hello',3.14,100]
nd3 = np.array(l3)

l4 = [3.1415, 102]
nd4 = np.array(l4)

nd5 = np.asarray(l1)

nd6 = np.ones((3,3))

nd7 = np.array(nd6)
nd8 = np.asarray(nd6)
nd6[1][1]=2

import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randint(0,150,size=(5,3)),
                  index=list('abcde'),
                  columns=['python','Math','English'])