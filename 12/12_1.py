
in_file = open('input_12.txt', 'r')
# in_file = open('test_12.txt', 'r')

def route(cmds):
	def perform_cmd(cmd):
		c, val = cmd[0], int(cmd[1:])
		def N(v): pos[0] += v
		def E(v): pos[1] += v
		def W(v): pos[1] -= v
		def S(v): pos[0] -= v
		def L(v):
			nonlocal direction
			direction = dir_enum[(dir_enum.index(direction) - int(v / 90))%4]
		def R(v):
			nonlocal direction 
			direction = dir_enum[(dir_enum.index(direction) + int(v / 90))%4]
		def F(v): cs[direction](v)
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
		
	direction = 'E'
	dir_enum = list('NESW')
	pos = [0,0]

	for cmd in cmds:
		perform_cmd(cmd)
	return sum(map(lambda x: abs(x), pos))

cmds = list(map(lambda x: x.rstrip(), in_file.readlines()))
print(route(cmds))