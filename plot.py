import matplotlib.pyplot as plt
import numpy as np


UBr = [1320,1200,880,640,460,268,128,94.4,70.4,44,21.6,13.6,30,52,78,96,118,208,296,400,472,536,584,640]
Quotient1 = [1320,1200,880,640,460,268,128,94.4,70.4,44,21.6,13.6,30,52,78,96,118,208,296,400,472,536,584,640]


for x in range(24):
    #Quotient1[x] = (UBr[x])/(2500)
    Quotient1[x] = (UBr[x])/(2500*np.sqrt(2))
    print(Quotient1[x])

v = [30,80,130,180,230,280,330,340,350,360,370,380,390,400,410,420,430,480,530,580,630,680,730,780]
Quotient2 = [30,80,130,180,230,280,330,340,350,360,370,380,390,400,410,420,430,480,530,580,630,680,730,780]


for x in range(24):
    Quotient2[x] = (v[x])/(380) 
    print(Quotient2[x])



plt.plot(Quotient2, Quotient1,'r.', label='Messwerte')
plt.xscale('log')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

#########################################################################################################################
#Teil 2: Theoriekurve

w_0 = 1/(1000*(420*10e-9))
omega = np.linspace(30/380,800/380,100000)
 


plt.plot(omega, np.sqrt(    (1/9) * ((( (omega)**2 - 1)**2)/( (1-(omega)**2)**2 + 9*(omega)**2  )    ) ) , label = 'Theoriekurve')
plt.xscale('log')
plt.xlabel(r'$\Omega = \frac{\nu}{\nu_{0}}$')
plt.ylabel(r'$\Bigl|frac{U_{Br}}{U_{S}}\Bigl|$')
plt.legend()
plt.tight_layout()


plt.savefig('plot.pdf')