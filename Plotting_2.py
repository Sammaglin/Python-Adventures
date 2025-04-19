import statistics
import matplotlib.pyplot as plt
lst=[130, 134, 230, 627, 694, 650, 207, 344, 683, 206, 170, 430, 408, 674, 162, 421, 686, 207, 664, 435, 189, 367, 204, 699, 185, 173, 443, 122, 371, 130, 144, 614, 134, 364, 652, 290, 619, 156, 461, 118, 405, 162, 414, 430, 498, 248, 469, 397, 615, 616, 344, 263, 691, 559, 409, 197, 199, 695, 402, 501, 126, 218, 454, 422, 459, 480, 362, 609, 679, 409, 694, 255, 605, 686, 456]
y=[]

lst.sort()
tv=int(0.1*(len(lst)))
lst=lst[tv:]
lst=lst[:len(lst)-tv]
for i in range(len(lst)):
    y.append(5)
plt.plot(lst, y,'r--')
plt.plot([statistics.mean(lst)],[5],'ro')
plt.plot([statistics.median(lst)],[5],'bs')
plt.plot([375],[5],'g^')
plt.ylabel("Numbers")
plt.xlabel("Speed")