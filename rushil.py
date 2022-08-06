from turtle import color
import matplotlib.pyplot as plt
import psutil as p
app_name=[]
percentage=[]
count=0
for process in p.process_iter():
    count=count+1
    if count<=8:
        name=process.name()
        cpu_usage=p.cpu_percent()
        print("name: ",name,"cpu usage : ",cpu_usage)
        app_name.append(name)
        percentage.append(cpu_usage)
plt.figure(figsize=(15,7)) 
plt.xlabel(app_name)
plt.ylabel(percentage)
plt.bar(app_name,percentage,width=0.8,color=("red","blue","green","yellow","orange","purple","pink","brown"))
plt.plt.show       
