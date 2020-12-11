from copy import deepcopy as dc
in_file = open('input_11.txt', 'r')
# in_file = open('test_11.txt', 'r')

toCheck = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1,0), (1,1)]

def countSeat(s):
	counter = 0
	for row in s:
		counter += row.count('#')
	return counter

def changeSeat(oldSeats):
	newSeats = dc(oldSeats)
	for row, seatRow in enumerate(oldSeats):
		for col, seat in enumerate(seatRow):
			if seat == 'L':
				counter = 0
				for offset in toCheck:
					if 0 <= row + offset[0] < len(oldSeats) and 0 <= col + offset[1] < len(seatRow):
						if oldSeats[row+offset[0]][col+offset[1]] == '#':
							counter += 1
				if counter == 0:
					newSeats[row][col] = '#'
			elif seat == '#':
				counter = 0
				for offset in toCheck:
					if 0 <= row + offset[0] < len(oldSeats) and 0 <= col + offset[1] < len(seatRow):
						if oldSeats[row+offset[0]][col+offset[1]] == '#':
							counter += 1
				if counter >= 4:
					newSeats[row][col] = 'L'
	return newSeats

raw = list(map(lambda x: x.rstrip(), in_file.readlines()))
raw = list(map(lambda x: [c for c in x], raw))
seats = dc(raw)
prevSeats = []
i = 1; limit = 6
while seats != prevSeats:
	prevSeats = dc(seats)	
	seats = changeSeat(seats)
res = countSeat(seats)
print(res)
