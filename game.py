import random
global ded
import os


def play():
	data={
	0:['https://starregistration.net/media/wysiwyg/Constellations/Orion.png','Орион'],
	1:['https://starregistration.net/media/wysiwyg/Constellations/Ursa_major.png','Большая медведица'],
	2:['https://starregistration.net/media/wysiwyg/Constellations/Hercules.png','Геркулес'],
	3:['https://starregistration.net/media/wysiwyg/Constellations/Cygnus.png','Лебедь'],
	4:['https://starregistration.net/media/wysiwyg/Constellations/Lyra.png','Лира'],
	5:['https://starregistration.net/media/wysiwyg/Constellations/Gemini.png','Близнецы'],
	6:['https://starregistration.net/media/wysiwyg/Constellations/Leo.png','Лев'],
	7:['https://starregistration.net/media/wysiwyg/Constellations/Bootes.png','Волопас'],
	8:['https://starregistration.net/media/wysiwyg/Constellations/Perseus.png','Персей'],
	9:['https://starregistration.net/media/wysiwyg/Constellations/Ursa_minor.png','Малая медведица'],
	}
	return data
'''
def shuffle():
	ded+=1
	ded=ded%10
	#b = [i for i in range(1, 10)]
	#random.shuffle(b)
	return ded

ded=0
'''
def create_random():
	out=[]
	data=play()
	number_play=random.randint(0,9)

	pic1=data[number_play]
	pic=pic1[0]
	answer1=data[number_play]
	answer2=answer1[1]

	r = [i for i in range(0,9)]
	if number_play in r:
		r.remove(number_play)
	a=random.choice(r)
	r.remove(a)
	b=random.choice(r)
	r.remove(b)
	c=random.choice(r)

	a1=data[a]
	b1=data[b]
	c1=data[c]

	out.append(a1[1])
	out.append(b1[1])
	out.append(answer2)
	out.append(c1[1])

	random.shuffle(out)
	answer=out.index(answer2)


	return pic, answer, out, number_play
'''
for i in range(10):
	print(create_random())
	print('\n\n')
os.system('pause')
'''