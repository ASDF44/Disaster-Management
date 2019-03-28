"""dis[0] = name of the disaster 
dis[1] = time to take the disaster back in control
dis[2] = rate of deaths per day
dis[3] = finance required per day
dis[4] = factor
dis[5] = waiting time or the NULL character
total deaths = tat*rate of deaths per day"""
import threading
import random

def enter(d,n): #Enter function to take names of disasters and their datas
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	for i in range(n):
		#d.append([str(input('Enter the name of disaster :: ')),int(input('Enter the time to take the disaster back in control :: ')),int(input('Enter the rate of deaths per day :: ')),int(input('Enter the money required to control the disaster :: '))])
		d.append([random.choice(alpha),random.randint(1,100),random.randint(1,100000),random.randint(1,100)])
	return(d)	

def display(d,n):
	for i in range(n):
		print(d[i][0],'\n')
		

	 		
		
def factor(d,m,n):
	for i in range(m,n):
		t = d[i][2] + d[i][1] + d[i][3]*d[i][1]
		deathrate = d[i][2]**(1/3) 
		time = d[i][1]**(1/3) 
		finance = (d[i][3]*d[i][1])**(1/3)
		factor1 = (deathrate**6)*(time**3)*(finance**(-3))
		d[i].append(factor1)
	
	
	
def sort(d,n):
	for i in range(n):
		for j in range(i,n):
			if(d[i][4] > d[j][4]):
				temp = d[i]
				d[i] = d[j]
				d[j] = temp
	return(dis)
	


def manage(dis,n,finance):
	temp = finance
	wt = [0]
	if(finance < dis[0][3]*dis[0][1]):
		wt[0] = 'NULL'
	else:
		finance -= dis[0][3]*dis[0][1]
		
	
	for i in range(n):
		j = i
		flag = 1
		while(j >= 0):
			if(wt[j] != 'NULL' and finance > dis[i][3]*dis[i][2]):
				wt.append(wt[j] + dis[i][1])
				finance = finance - dis[i][3]*dis[i][1]
				flag = 1
				break
			else:
				flag = 0
				j = j-1
		if(flag == 0 and j >= -1):
			wt.append('NULL')
	wt.pop()
	
	for i in range(n):
		dis[i].append(wt[i])
	

	print(finance,'\n\n\n\n')
	print(round((temp-finance)*100/temp,2),'\n\n\n\n')
	return(dis)
	

			
if __name__ == '__main__':
	n = int(input('Enter the number of disasters :: '))
	dis = []
	dis = enter(dis,n)
	#finance = int(input('Enter the finance we have :: '))33
	finance = random.randint(10000,1000000)
	a1 = threading.Thread(target = factor,args = (dis,0,n//2))
	a2 = threading.Thread(target = factor,args = (dis,n//2,n))
	
	a1.start()
	a2.start() 
	
	a1.join()
	a2.join()

	dis = sort(dis,n)
	
	print('finance = ',finance)
	#display(dis,n)
	manage(dis,n,finance)
	print('Disaster Name   Control time in days    death rate per day    finance require rate          waiting time\n')
	for i in range(n):
		print('        ',dis[i][0],'               ',dis[i][1],'                ',dis[i][2],'            ',dis[i][3],'                       ',dis[i][5])
	
