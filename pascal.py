def pascalPlane(n, prevPlane):
	plane =[]
	for row in range(n):
		created_row = []
		for col in range(row + 1):
			s = 0
			for pos in ((col,row), (col, row-1), (col-1, row-1)):
				if pos[0] > -1 and pos[1] > -1 and pos[1] < len(prevPlane) and pos[0] < len(prevPlane[pos[1]]):
					s += prevPlane[pos[1]][pos[0]]
			created_row.append(s)
		plane.append(created_row)
	return plane


def pascal3D(rows):
	return list(yieldPlanes(rows))

def yieldPlanes(rows):
	prev = [[1]]
	for e in range(rows):
		prev = pascalPlane(e + 1, prev)
		yield prev

def getPlaneAt(row):
	return list(yieldPlanes(row))[-1]