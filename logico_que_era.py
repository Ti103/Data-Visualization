import matplotlib.pyplot as plt

l_y = [20,16,16]
l_x = [2,2,4]

o_y = [18, 20, 18, 16, 18]
o_x = [5, 6, 7, 6, 5]

g_y = [19, 20, 18, 16, 18, 18]
g_x = [9.5, 9, 8, 9, 10, 9]

i_y = [16, 17, 18, 19, 20]
i_x = [11]*5

c_y = [20, 18, 16]
c_x = [14, 12, 14]

o2_y = o_y
o2_x = [15, 16, 17, 16, 15]

q_y = [14, 12, 10, 12, 14]
q_x = [9.5, 8.5, 9.5, 10.5, 9.5]

traco_y = [12, 10.5]
traco_x = [9.5, 10.5]

e_y = [8, 8, 6, 6, 6, 4, 4]
e_x = [8, 6, 6, 8, 6, 6, 8]

r_y = [4, 8, 7, 6, 4]
r_x = [9, 9, 11, 9, 11]

a_y = [4, 8, 4, 6, 6]
a_x = [12, 13, 14, 13.5, 12.5]

plt.scatter(l_x, l_y)
plt.scatter(o_x, o_y)
plt.scatter(g_x, g_y)
plt.scatter(i_x, i_y)
plt.scatter(c_x, c_y)
plt.scatter(o2_x, o2_y)
plt.scatter(q_x, q_y)
plt.scatter(e_x, e_y)
plt.scatter(r_x, r_y)
plt.scatter(a_x, a_y)
plt.scatter(traco_x, traco_y)
plt.plot(l_x, l_y)
plt.plot(o_x, o_y)
plt.plot(g_x, g_y)
plt.plot(i_x, i_y)
plt.plot(c_x, c_y)
plt.plot(o2_x, o2_y)
plt.plot(q_x, q_y)
plt.plot(e_x, e_y)
plt.plot(r_x, r_y)
plt.plot(a_x, a_y)
plt.plot(traco_x, traco_y)
plt.show()
