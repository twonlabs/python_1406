import matplotlib.pyplot as plt

plt.style.use('default')

# plt.plot([2, 4, 6, 8])

x = [2, 4, 6, 8]
y = [1, 3, 5, 7]
plt.plot(x, y)

# plt.show()

fig = plt.figure()
# (행개수, 열개수, 위치값)
fig.add_subplot(1, 2, 1)
fig.add_subplot(2, 2, 3)
# plt.show()

plt.close('all')

fig = plt.figure()

a1 = fig.add_subplot(1, 2, 1)
a2 = fig.add_subplot(1, 2, 1)

x = range(0, 10)
y = range(5, 15)
a1.plot(x, y)

plt.close('all')

x = range(0, 50)
y = range(0, 50)
a2.plot(x, y)

plt.show()

plt.style.use('ggplot')

a = fig.add_subplot(111)
x = [3, 4]
y = [1, 2]

labels = ['red', 'blue']
a.bar(x, y, tick_label=labels, color=color)
plt.show()

