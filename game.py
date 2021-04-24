import random
global ded
import os



def description():
	desc={
	0:['Главные сокровища зимнего неба находятся именно в созвездии *Орион*. Задуманный как небесный охотник, силуэт Ориона действительно напоминает человека с характерным поясом из трех звезд.'],
	1:['Знаменитый ковш созвездия *Большая медведица* всем нам знаком с детства. Но важно помнить, что помимо ковша у "медведицы" также имеются протяженные лапы и морда.'],
	2:['Еще один герой древнегреческих мифов *Геркулес* - сын бога Зевса является обладателем потрясающего шарового скопления М13. Созвездие легко запомнить благодаря квадратному телу героя с расходящимися руками.'],
	3:['Еще один странник - небесный *Лебедь* летит прямо по направлению проекции Млечного пути. Контур созвездия действительно напоминает птицу с крыльями, продолговатой шеей и хвостом.'],
	4:['Знаменитый музыкальный инструмент времен Античности также представлен на небе и вместе с Лебедем и Орлом составляет летне-осенний треугольник. Созвездие *Лира* выглядит как ромб с яркой звездой Вега с краю.'],
	5:['Известные мифологические близнецы Кастор и Поллукс неразлучны даже на небосводе. Созвездие *Близнецы* можно определить по двум ярким, близко расположенным звездам, названным в честь самих братьев.'],
	6:['Могучий *Лев* вынужден вечно рыскать по небу в поисках добычи. Это созвездие выглядит как утюг; так его проще найти на ночном небе.'],
	7:['Этот древнегреческий персонаж по ошибке на охоте застрелил собственную мать, а позже в его часть назвали созвездие *Волопас*. Из-за его очертаний, созвездие часто называют парашютистом.'],
	8:['Небесный спутник прекрасной Андромеды *Персей* не оставляет и тут свою супругу. Главная его достоприимечательность - звезда Алголь, которую важно не путать с алкоголем.'],
	9:['Это весьма неприметное созвездие играет важнейшую роль в навигации: именно в нем расположена Полярная звезда, указывающая направление на север. *Малая медведица* как и Большая имеет форму ковша.']
	}
	return desc

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