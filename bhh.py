#İBRAHİM TUNÇ 
#29.01.2023

#Necessary Modules
import numpy as np
from matplotlib import pyplot as plt
from celluloid import Camera
from numpy import sin,sqrt,cos,pi 
from matplotlib.animation import PillowWriter

writer = PillowWriter(fps=60)    #for saving animations to gif
plt.style.use("dark_background") #Theme

class BHM:
    g = 9.81 #Gravitiy

    def __init__(self,r,l,m,sensetive,interval) -> None:

        self.r = r #amplitude
        self.l = l #Rope lenght
        self.m = m #mass

        self.sensetive = sensetive #Sensetive of time variable (linspace) rec:240
        self.interval = interval #interval of animate function rec: 40

        self.T = 2 * pi * sqrt(self.l / self.g) #Period
        self.f = 1 / self.T #Freuquency
        self.w = 2 * pi * self.f #Omega
        
        self.fig = plt.figure(figsize=(10,8)) #Create a figure
        self.camera = Camera(self.fig) #Create a camera to snapping

        #Axes
        self.ax1 = plt.subplot2grid((4, 5), (0, 0), colspan=4)
        self.ax2 = plt.subplot2grid((4, 5), (1, 0), colspan=4)
        self.ax3 = plt.subplot2grid((4, 5), (2, 0),colspan=4)
        self.ax4 = plt.subplot2grid((4,5),  (3,0),colspan=4)
        self.ax5 = plt.subplot2grid((4, 5), (0, 4), rowspan=4)

        #Time variable 
        self.t = np.linspace(0, 2 * self.T, self.sensetive, endpoint=True) #sensetive of time  

        #Equations
        self.x = self.r * sin(self.w * self.t) # instant  postion
        self.v = self.r * self.w * cos(self.w * self.t) # instant velocity
        self.a = self.x * (self.w)**2   # instant acceleration 
    
    def animater(self):
        
        for i,j in zip(self.t,self.x):
            self.fig.suptitle("BASIC HARMONIC MOTION")

            #Basic Harmonic Motion Modelling
            self.ax1.scatter(self.r*sin(self.w* i),0,color="r",s=150) #interactive scatter plot for tracking 
            self.ax1.grid(True,alpha=0.2)
            self.ax1.axvline(-10,color="green",ls="--",lw=0.5)
            self.ax1.axvline(0,color="green",ls="--",lw=0.5)
            self.ax1.axvline(10,color="green",ls="--",lw=0.5)
            self.ax1.axhline(0,color="green",ls="-.",lw=0.5)
            self.ax1.set_ylim(-14.9,14.9)

            #Instant Position Graph
            self.ax2.set_title("x/t")
            self.ax2.set_xlabel("t")
            self.ax2.set_ylabel("x(t)")
            self.ax2.plot(self.t,self.x,"r")
            self.ax2.scatter(i,self.r*sin(self.w* i),color="g",s=100)
            self.ax2.grid(True,alpha=0.4)
            self.ax2.set_ylim(-14.9,14.9)

            #Instant Velocity Graph
            self.ax3.set_title("v/t")
            self.ax3.set_xlabel("t")
            self.ax3.set_ylabel("v(t)")
            self.ax3.plot(self.t,self.v,"r")
            self.ax3.scatter(i,self.r*self.w*cos(self.w*i),color="g",s=100)
            self.ax3.grid(True,alpha=0.4)
            self.ax3.set_ylim(-14.9,14.9)

            #Instant Acceleration Graph            
            self.ax4.set_title("a/t")
            self.ax4.set_xlabel("t")
            self.ax4.set_ylabel("a(t)")
            self.ax4.plot(self.t,self.a,"r")
            self.ax4.scatter(i,j*self.w**2,color="g",s=100)
            self.ax4.grid(True,alpha=0.4) 
            self.ax4.set_ylim(-14.9,14.9)

            #Instant Force Graph            
            self.ax5.bar(0,self.m * (self.w**2) * self.r * sin(self.w * -i),color="red")
            self.ax5.grid(True,alpha=0.25)
            self.ax5.set_title("Force")
            self.ax5.set_xticklabels(" ")

            #Snapping to moment of graph to visualize
            self.camera.snap()
        #Animate all snapped positions

        self.animate = self.camera.animate(interval=self.interval,repeat=True)
        plt.tight_layout()
        plt.show()

    def saveAnimate(self):
        name = "animater1.gif"
        self.animate.save(name,writer=writer) #Save fig by using PillowWriter
        print(f"{name} saved!")  
    
    def printAllVariables(self):
        #Print All Variables and Constants
        print(
            f"* Amplitutde: {self.r}",
            f"* Rope Length: {self.l}",
            f"* Gravitiy: {self.g}",
            f"* Mass: {self.m}",
            f"* Sensetive of time: {self.sensetive}",
            f"* Interval func: {self.interval}",
            f"* Period: {self.T}",
            f"* Frequency: {self.f}",
            f"* Omega: {self.w}",
            sep="\n")
