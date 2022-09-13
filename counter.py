#clocking time


def minutes():								#first function for only minutes
	minutes = [0]
	for i in minutes:						#cycle for minutes
		try:
			i = int(input('input minutes: '))	#try to input user data
		except ValueError:					#if user data is not 
			print('{} hours and {} minutes'.format(sum(minutes)//60, (sum(minutes)%60)))
			break
		else:
			if i <= 60:
				minutes.append(i)
			else:
				print('put numbers less then 60')
def seconds_and_minutes():					#second function for both of minutes and seconds
	minutes = [0]
	seconds = [0]
	for i in minutes:						#cycle for minutes
		try:
			i = int(input('input minutes: '))
		except ValueError:
			break
		else:
			if i <= 60:
				minutes.append(i)
			else:
				print('put numbers less then 60')
	for i in seconds:						#cycle for seconds
		try:
			i = int(input('input seconds: '))
		except ValueError:
			secsum = sum(seconds)
			secsumreal = secsum//60
			print('{} hours , {} minutes and {} seconds'.format(sum(minutes)//60, sum(minutes)%60 +  secsumreal, secsum%60))
			break
		else:
			if i <= 60:
				seconds.append(i)
			else:
				print('put numbers less then 60')
	try:
		speed = float(input('do you like take into speed(x1.25 , x1.50 , x1.75 , x2, n): '))
	except ValueError:
		print('sure!')
	except KeyboardInterrupt:
		print('sure!')
	else:
		newsum = sum(minutes) + sum(seconds)//60
		seconds1 = (sum(seconds)%60)//speed
		newsumwithspeed = newsum//speed
		adding = newsumwithspeed%speed
		hours = newsumwithspeed//60
		minutes1 = newsumwithspeed%60

		print('{} hours , {} minutes and {} seconds'.format(int(hours), int(minutes1), int(seconds1)))
		
var = input('put y/n to set seconds or not: ')
assert var == 'y' or var == 'n'
if var == 'y':
	seconds_and_minutes()
elif var == 'n':
	minutes()



