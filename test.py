from __future__ import division
import numpy as np
np.seterr(invalid='raise')
from matplotlib import pyplot as plt

import models, observations

blah = models.Mixture(alpha_0=3,components=[observations.Gaussian(mu_0=np.zeros(2),sigma_0=np.eye(2),kappa_0=0.1,nu_0=4) for itr in range(20)])

blah.generate(200) # starts blah at truth, cheating!

blah.plot()
plt.title('initial zs')

for itr in range(200):
    blah.meanfield_coordinate_descent_step()

blah.plot()
plt.title('final badness')
plt.show()