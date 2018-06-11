import numpy
from dxfwrite import DXFEngine as dxf
#dwg = dxf.drawing('D:\OneDrive\python\dxf\polyline.dxf')
class f:
    from math import sinh,cosh,tanh,sqrt
    eta=0.0001
    tacke=50
    @classmethod
    def f11(cls,a,h,l,s,g):
        return (l-f.sqrt(h**2+(2*(s+f.eta)*f.sinh(a*g/2/(s+f.eta))/g)**2))/f.eta-(l-f.sqrt(h**2+(2*s*f.sinh(a*g/2/s)/g)**2))/f.eta
    @classmethod
    def f12(cls,a,h,l,s,g):
        return (l-f.sqrt(h**2+(2*s*f.sinh((a+f.eta)*g/2/s)/g)**2))/f.eta-(l-f.sqrt(h**2+(2*s*f.sinh(a*g/2/s)/g)**2))/f.eta
    @classmethod
    def f21(cls,a,h,l,s,g,sf):
    #d/ll
        return  (sf-a*s/(2*(l+f.eta))-((l+f.eta)**2+h**2)*g/(4*(l+f.eta)*f.tanh(a*g/(2*s)))-(sf-a*s/(2*l)-(l**2+h**2)*g/(4*l*f.tanh(a*g/(2*s)))))/f.eta
    @classmethod
    def f22(cls,l,l0,t,t0,al,sf,sf0,e):
        return (l-(l0+f.eta)-(t-t0)*al*(l0+f.eta)-(sf-sf0)*(l0+f.eta)/e)/f.eta-(l-l0-(t-t0)*al*l0-(sf-sf0)*l0/e)/f.eta
    @classmethod
    def f23(cls,l,l0,t,t0,al,sf,sf0,e):
        return (l-l0-(t-t0)*al*l0-(sf-(sf0+f.eta))*l0/e)/f.eta-(l-l0-(t-t0)*al*l0-(sf-sf0)*l0/e)/f.eta
    @classmethod
    def f31(cls,a,h,l,s,g,sf):
    #d/sigma
        return (sf-a*(s+f.eta)/(2*l)-(l**2+h**2)*g/(4*l*f.tanh(a*g/(2*(s+f.eta))))-(sf-a*s/(2*l)-(l**2+h**2)*g/(4*l*f.tanh(a*g/(2*s)))))/f.eta
    @classmethod
    def f32(cls,a,h,l,s,g,sf):
    #d/a
        return ( sf-(a+f.eta)*s/(2*l)-(l**2+h**2)*g/(4*l*f.tanh((a+f.eta)*g/(2*s)))- (sf-a*s/(2*l)-(l**2+h**2)*g/(4*l*f.tanh(a*g/(2*s)))))/f.eta
    @classmethod
    def f33(cls,a,h,l,s,g,sf):
    #d/l
        return (sf-a*s/(2*(l+f.eta))-((l+f.eta)**2+h**2)*g/(4*(l+f.eta)*f.tanh(a*g/(2*s)))-(sf-a*s/(2*l)-(l**2+h**2)*g/(4*l*f.tanh(a*g/(2*s)))))/f.eta
    @classmethod
    def f41(cls,a,h,ad,s,g):
    #d/sigma
        return (h-(2*(s+f.eta)/g)*f.sinh(a*g/2/(s+f.eta))*f.sinh(ad*g/2/(s+f.eta))-(h-(2*s/g)*f.sinh(a*g/2/s)*f.sinh(ad*g/2/s)))/f.eta
    @classmethod
    def f42(cls,a,h,ad,s,g):
    #d/a
        return (h-(2*s/g)*f.sinh((a+f.eta)*g/2/s)*f.sinh(ad*g/2/s)-(h-(2*s/g)*f.sinh(a*g/2/s)*f.sinh(ad*g/2/s)))/f.eta
    @classmethod
    def f43(cls,a,h,ad,s,g):
    #d/ad
        return (h-(2*s/g)*f.sinh(a*g/2/s)*f.sinh((ad+f.eta)*g/2/s)-(h-(2*s/g)*f.sinh(a*g/2/s)*f.sinh(ad*g/2/s)))/f.eta
    @classmethod
    def f1(cls,a,h,l,s,g):
        return l-f.sqrt(h**2+(2*s*f.sinh(a*g/2/s)/g)**2)
    @classmethod
    def f2(cls,l,l0,t,t0,al,sf,sf0,e):
        return l-l0-(t-t0)*al*l0-(sf-sf0)*l0/e
    @classmethod
    def f3(cls,a,h,l,s,g,sf):
        return sf-a*s/(2*l)-(l**2+h**2)*g/(4*l*f.tanh(a*g/(2*s)))
    @classmethod
    def f4(cls,a,h,ad,s,g):
        return h-(2*s/g)*f.sinh(a*g/2/s)*f.sinh(ad*g/2/s)
    @classmethod
    def fl(cls,x,s,g):
        return (s/g)*f.cosh(x*g/s)	
		
h=[10,15,-26,12,-36,-21.1,32,23,65,45,23,12,36,25,14,23,56,36,21,15,12,36,54,33.3,65,32]
a=numpy.array([339.5,300,306,450,324,123,452,554,325,456,254,665,369,258,177,456,789,123,351,426,536,452,125,326,364,526])
uze=[15.85,83.8,0.004646,0.0168453,9630,0.0000164]
n=5;t0=-5;t=0
#dodter=1
size=n*6+1
m1=numpy.zeros((n,size))
m2=numpy.zeros((n,size))
m3=numpy.zeros((n,size))
m4=numpy.zeros((1,size))
m5=numpy.zeros((n,size))
m6=numpy.zeros((n,size))
m7=numpy.zeros((n,size))
mx=numpy.zeros((size,1))
mf=numpy.zeros((size,1))
#VEKTOR PROMENLJIVE pocetne vrednosti
for x in range(len(mx)):
    if x in range(0,n):
        mx[x+3*n+1]=mx[x,0]=f.sqrt(a[x]**2+h[x]**2); mx[x+5*n+1]=a[x]/2
    else:
        if x in range (n,2*n):
            mx[x+3*n+1]=mx[x,0]=uze[0]/2
        else:
            if x in range (2*n,2*n+1):
                mx[x,0]=uze[0]/2
            else:
                if x in range (2*n+1,3*n+1):
                   mx[x,0]=a[x-2*n-1]
mp=mx
#print(mx)
#JAKOBIJAN
delta=1
#print(dodter)
while abs(delta)>f.eta:
    prir=mx[2*n,0]
    #print(mf)
    for x in range(0, n):
        #if x==dodter:
        #    kt=3
        #else:
        kt=2
        #print(kt)
        m1[x,x]=1
        m1[x,2*n]=f.f11((mx[2*n+1+x,0]),(h[x]),(mx[x,0]),(mx[2*n,0]),(uze[kt]))
        m1[x,2*n+x+1]=f.f12((mx[2*n+1+x,0]),(h[x]),(mx[x,0]),(mx[2*n,0]),(uze[kt]))
        m2[x,x]=1.0
        m2[x,x+n]=-1*(mx[3*n+1+x,0])/uze[4]
        #l,l0,t,t0,al,sf,sf0,e
        #print("l %s  l0 %s t %s t0 %s al %s sf %s sf0 %s e %s " % ((mx[x,0]),(mx[3*n+1+x,0]),t,t0,uze[5],(mx[n+x,0]),(mx[4*n+1+x,0]),uze[4]))
        m2[x,x+3*n+1]=f.f22((mx[x,0]),(mx[3*n+1+x,0]),t,t0,uze[5],(mx[n+x,0]),(mx[4*n+1+x,0]),uze[4])
        m2[x,x+4*n+1]=f.f23((mx[x,0]),(mx[3*n+1+x,0]),t,t0,uze[5],(mx[n+x,0]),(mx[4*n+1+x,0]),uze[4])
        m3[x,x]=f.f21((mx[2*n+1+x,0]),(h[x]),(mx[x,0]),(mx[2*n,0]),(uze[kt]),(mx[n+x,0]))
        m3[x,x+n]=1.0
        m3[x,2*n]=f.f31((mx[2*n+1+x,0]),(h[x]),(mx[x,0]),(mx[2*n,0]),(uze[kt]),(mx[n+x,0]))
        m3[x,2*n+x+1]=f.f32((mx[2*n+1+x,0]),(h[x]),(mx[x,0]),(mx[2*n,0]),(uze[kt]),(mx[n+x,0]))
        m4[0,x+2*n+1]=-1.0
        m5[x,3*n+1+x]=1.0
        m6[x,4*n+1+x]=1.0
        #a,h,l,s,g,sf
        m6[x,3*n+1+x]=f.f21((mp[2*n+1+x,0]),(h[x]),(mp[x,0]),(uze[0]),(uze[3]),(mp[n+x,0]))
		#a,h,ad,s,g
        #print("f4-- a %s  h %s ad %s sigma %s g %s " % (mx[2*n+1+x,0],h[x],mx[5*n+1+x,0],mx[2*n,0],uze[kt]))
        m7[x,2*n]=f.f41(mx[2*n+1+x,0],h[x],mx[5*n+1+x,0],mx[2*n,0],uze[kt])
        m7[x,2*n+x+1]=f.f42(mx[2*n+1+x,0],h[x],mx[5*n+1+x,0],mx[2*n,0],uze[kt])
        m7[x,5*n+x+1]=f.f43(mx[2*n+1+x,0],h[x],mx[5*n+1+x,0],mx[2*n,0],uze[kt]) 
		
#FUNKCIJE a,h,l,s,g
    for x in range(len(mf)):
        if x in range(0,n):
            #print("f1-- a %s  h %s l %s s %s g %s " % (mx[2*n+1+x,0],h[x],mx[x,0],mx[2*n,0],uze[2]))
            #if x==dodter:
            #    kt=3
            #else:
            kt=2
            mf[x]=f.f1(mx[2*n+1+x,0],h[x],mx[x,0],mx[2*n,0],uze[kt])
        else:
            #l,l0,t,t0,al,sf,sf0,e
            if x in range (n,2*n):

                #print("l %s  l0 %s t %s t0 %s al %s sf %s sf0 %s e %s " % (mx[x-n,0],mx[x+2*n+1,0],t,t0,uze[5],mx[x],mx[x+3*n+1,0],uze[4]))
                mf[x]=f.f2(mx[x-n,0],mx[x+2*n+1,0],t,t0,uze[5],mx[x],mx[x+3*n+1,0],uze[4])
            else:
                if x in range (2*n,3*n):
                    #if x==dodter:
                    #    kt=3
                    #else:
                    kt=2
                    #a,h,l,s,g,sf
                    #print("a %s  h %s l %s s %s g %s sf %s " % (mx[1+x,0],h[x-2*n],mx[x-2*n,0],mx[2*n,0],uze[2],mx[x-n,0]))
                    mf[x]=f.f3(mx[1+x,0],h[x-2*n],mx[x-2*n,0],mx[2*n,0],uze[kt],mx[x-n,0])
                else:
                    if x in range (3*n,3*n+1):
                        #print(a[range(0,n)])
                        #print(mp[range(2*n+1,3*n+1)])
                        mf[x]=numpy.sum(a[range(0,n)])-numpy.sum(mx[range(2*n+1,3*n+1)])
                    else:
                        if x in range (3*n+1,4*n+1):
                            #a,h,l,s,g
                            #print("a %s  h %s l %s s %s g %s " % (mp[x-n,0],h[x-3*n-1],mx[x,0],mp[2*n,0],uze[3]))
                            mf[x]=f.f1(mp[x-n,0],h[x-3*n-1],mx[x,0],mp[2*n,0]*2,uze[3])
                        else:
                            if x in range (4*n+1,5*n+1):
                            #a,h,l,s,g,sf
                                #print("a %s  h %s l %s s %s g %s sf %s " % (mp[x-2*n,0],h[x-4*n-1],mp[x-4*n-1,0],mp[2*n,0],uze[3],mx[x,0]))
                                mf[x]=f.f3(mp[x-2*n,0],h[x-4*n-1],mp[x-4*n-1,0],mp[2*n,0]*2,uze[3],mx[x,0])
                            else:
                                if x in range (5*n+1,6*n+1):
								#a,h,ad,s,g
                                    #print(mx[x-3*n,0],h[x-5*n-1],mx[x,0],mx[2*n,0],uze[kt])
                                    mf[x]=f.f4(mx[x-3*n,0],h[x-5*n-1],mx[x,0],mx[2*n,0],uze[kt])
    m=numpy.concatenate((m1,m2,m3,m4,m5,m6,m7))
    #print(mx)
    #print(m)
    minv = numpy.linalg.inv(m)
    mx=numpy.subtract(mx,minv.dot(mf))
    delta=mx[2*n,0]-prir

print(mx)
#l=[]
#for i in range(0, n):
    #print(mx[5*n+1+i])
    #x1=(mx[5*n+1+i]-mx[2*n+1+i])/2
    #x2=(mx[5*n+1+i]+mx[2*n+1+i])/2
    #print(x1,x2)
    #step=mx[2*n+1+i]/f.tacke
    #print(step)
    #l=numpy.linspace(x1,x2,f.tacke)
    #yy=numpy.zeros(range(l))
    #print(l)
    #for x in l:
        #yy[y]=f.fl(l[x],mx[2*n],uze[2])
    #fx=numpy.array(l,y)
    #polyline = dxf.polyline(fx)
    #polyline.close()
    #dwg.add(polyline)
    #l.append((x1+step,fl(x1+step,mx[2*n])))
    #fl(cls,x,s,g)
    
    
    #print(x1,x2)
    


