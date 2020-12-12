
in_file = open('input_12.txt', 'r')
# in_file = open('test_12.txt', 'r')

def route(cmds):
	def perform_cmd(cmd):
		c, val = cmd[0], int(cmd[1:])
		def N(v): waypoint[0] += v
		def E(v): waypoint[1] += v
		def W(v): waypoint[1] -= v
		def S(v): waypoint[0] -= v
		def L(v):
			if v == 90:
				waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
			elif v == 180:
				waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
			elif v == 270:
				R(90)
		def R(v):
			if v == 90:
				waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
			elif v == 180:
				waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
			elif v == 270:
				L(90)
		def F(v):
			for i, w in enumerate(waypoint):
				pos[i] += w*v
		cs = {
			'N': N,
			'E': E,
			'W': W,
			'S': S,
			'F': F,
			'L': L,
			'R': R,
		}
		return cs[c](val)
		
	waypoint = [1, 10]
	direction = 'E'
	dir_enum = list('NESW')
	pos = [0,0]
	for cmd in cmds:
		perform_cmd(cmd)
	return sum(map(lambda x: abs(x), pos))

cmds = list(map(lambda x: x.rstrip(), in_file.readlines()))
print(route(cmds))