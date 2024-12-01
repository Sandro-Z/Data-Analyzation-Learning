import matplotlib.pyplot as plt
qc={
	'A':1,
	'b':2,
	'c':3
}
a=plt.pie(qc.values(),labels=qc.keys())
plt.show()
print(a)