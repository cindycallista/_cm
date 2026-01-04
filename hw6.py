import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    def scale(self, sx, sy, center=None):
        cx, cy = (center.x, center.y) if center else (0, 0)
        return Point(cx + (self.x - cx) * sx, cy + (self.y - cy) * sy)

    def rotate(self, angle_rad, center=None):
        cx, cy = (center.x, center.y) if center else (0, 0)
        s, c = math.sin(angle_rad), math.cos(angle_rad)
        px, py = self.x - cx, self.y - cy
        return Point(px * c - py * s + cx, px * s + py * c + cy)

    def dist_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.a = p1.y - p2.y
        self.b = p2.x - p1.x
        self.c = p1.x * p2.y - p2.x * p1.y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]

    def transform(self, mode, **kwargs):
        new_pts = []
        for p in self.points:
            if mode == 'translate': new_pts.append(p.translate(kwargs['dx'], kwargs['dy']))
            elif mode == 'scale': new_pts.append(p.scale(kwargs['sx'], kwargs['sy'], kwargs.get('center')))
            elif mode == 'rotate': new_pts.append(p.rotate(kwargs['angle'], kwargs.get('center')))
        return Triangle(*new_pts)

def intersect_lines(l1, l2):
    det = l1.a * l2.b - l2.a * l1.b
    if abs(det) < 1e-9: return None
    return Point((l1.b * l2.c - l2.b * l1.c) / det, (l2.a * l1.c - l1.a * l2.c) / det)

def intersect_line_circle(line, circle):
    dx, dy = line.p2.x - line.p1.x, line.p2.y - line.p1.y
    fx, fy = line.p1.x - circle.center.x, line.p1.y - circle.center.y
    a, b = dx*dx + dy*dy, 2 * (fx*dx + fy*dy)
    c = (fx*fx + fy*fy) - circle.radius**2
    delta = b*b - 4*a*c
    if delta < 0: return []
    pts = []
    for s in ([1, -1] if delta > 0 else [1]):
        t = (-b + s * math.sqrt(delta)) / (2*a)
        pts.append(Point(line.p1.x + t*dx, line.p1.y + t*dy))
    return pts

def intersect_circles(c1, c2):
    d = c1.center.dist_to(c2.center)
    if d > c1.radius + c2.radius or d < abs(c1.radius - c2.radius) or d == 0: return []
    a = (c1.radius**2 - c2.radius**2 + d**2) / (2 * d)
    h = math.sqrt(max(0, c1.radius**2 - a**2))
    x2 = c1.center.x + a * (c2.center.x - c1.center.x) / d
    y2 = c1.center.y + a * (c2.center.y - c1.center.y) / d
    rx, ry = -(c2.center.y - c1.center.y) * (h / d), (c2.center.x - c1.center.x) * (h / d)
    return [Point(x2 + rx, y2 + ry), Point(x2 - rx, y2 - ry)]

def get_perpendicular_foot(p, line):
    dx, dy = line.p2.x - line.p1.x, line.p2.y - line.p1.y
    t = ((p.x - line.p1.x) * dx + (p.y - line.p1.y) * dy) / (dx*dx + dy*dy)
    return Point(line.p1.x + t * dx, line.p1.y + t * dy)

def verify_pythagoras(p_out, line):
    f = get_perpendicular_foot(p_out, line)
    a = line.p1
    sq_a = p_out.dist_to(f)**2
    sq_b = f.dist_to(a)**2
    sq_c = p_out.dist_to(a)**2
    return math.isclose(sq_a + sq_b, sq_c)
