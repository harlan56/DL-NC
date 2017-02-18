import src
import numpy as np
import matplotlib.pyplot as plt


#-----------------simulation setting----------------
# define and generate the data
np.random.seed(108)
Data, cla = src.data.Simple(1,src.core.MAX_OPERATION_TIME,3).Tri_function()

test_data = Data[1][0][0:100]
test_cla = cla[1][0][0:100]

# define and initialize the liquid
Liquid = src.liquid.Liquid(Data, cla[2],'Input', 1, 1)
Liquid.initialization()
Liquid.pre_train_res()
Liquid.train_readout()
output = Liquid.test(test_data,test_cla)
print(output)