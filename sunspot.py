from numpy import loadtxt, zeros
from pylab import plot, show, xlabel, xlim, ylim, ylabel
a=loadtxt("sunspots.txt",float)
plot(a[:,0],a[:,1])
y=[]
x=[]
for k in range(5,1000):
    ykm=0
    for m in range(k-5,k+5):
        d=a[m,1]
        ykm=ykm+d
    y.append(ykm/11)
    x.append(k)
plot(x,y)
xlim(0,1000)
xlabel("meses")
ylabel("manchas solares")
show()
