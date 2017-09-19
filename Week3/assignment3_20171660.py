## 20171660 이건민
## Week3
import pickle

dbfilename = 'test3_4.dat'
scdb_total = []
def readScoreDB():
        try:
                fH = open(dbfilename, 'rb')
        except FileNotFoundError as e:
                print("New DB: ", dbfilename)
                return []
        try:
                scdb =  pickle.load(fH)
        except:
                print("Empty DB: ", dbfilename)
        else:
                print("Open DB: ", dbfilename)
        fH.close()
        for p in scdb:
                scdb_age=int(p['Age'])         #나이와 점수를 정수형으로 인식시키기 위해
                scdb_score=int(p['Score'])
                scdb_total.append({'Name': p['Name'], 'Age': scdb_age, 'Score': scdb_score})
        return scdb_total


# write the data into person db
def writeScoreDB(scdb_total):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb_total, fH)
    fH.close()

def doScoreDB(scdb_total):
	while(True):	
		inputstr = (input("Score DB > "))
		if inputstr == "": continue
		parse = inputstr.split(" ")
		
		if parse[0] == 'add':
			try:                           #미입력시 예외 처리
				record = {'Name' :parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])} #나이와 점수를 int로
				scdb_total += [record]
			except IndexError:
				print("이름과 나이, 점수를 입력하세요")
		elif parse[0] == 'del':
			try:                           #미입력시 예외 처리
				for p in scdb_total:         #같은 이름은 모두 삭제하기 위해 모두 소문자로 낮춤
					if p['Name'].lower() == parse[1].lower(): 
						scdb_total.remove(p)
			except IndexError:
				print("이름을 입력하세요")
		elif parse[0] == 'show':
			sortKey ='Name' if len(parse) == 1 else parse[1]
			showScoreDB(scdb_total, sortKey)
		elif parse[0] == 'quit':
			break
		elif parse[0] == 'find':
			try:        			#미입력시 예외처리
				for p in scdb_total:          
					if parse[1] in p['Name']:   #입력받은 이름을 찾고 
						for k,v in p.items():          
							if type(v) == int:  # 이름은 str으로 받고          
                                               			print(k + '=%d'%v, end=' ')
                                               			print()	
							else:               #나이, 점수는 정수로 받음
								print(k + '+' + v, end=' ')
								print()
						break				# 모든정보를 입력받은 후 종료	
					else:
						print("없음")  #이름이 없다면		
						break
			except IndexError:
				print("이름을 입력하세요")		
				
		elif parse[0] == 'inc':
			try:					#미입력시 예외 처리
				for p in scdb_total:
					if p['Name'] == parse[1]:           #입력받은 이름과 같은 이름이 있으면
						num = parse[2]		    #str을 int로 바꾸어준다
						intnum =int(num)
						p['Score'] += intnum
					else:
						print("똑바로 입력하세요")
			except IndexError:
				print("이름과 합할 점수를 입력하세요")				
				break							
		else:
			print("Invalid command: " + parse[0])


def showScoreDB(scdb_total, keyname):
	for p in sorted(scdb_total, key=lambda person: person[keyname]):
		
		for k,v in p.items():                    # p에서 key와 value를 나눠 이름은 str, 나이와 점수는 int로
			if type(v) == int:
				print(k + '=%d'%v, end=' ')
			else:
				print(k + '=' + v, end=' ')
		print()



scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

