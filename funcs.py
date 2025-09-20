def gradient(x, y, func, h: float = 0.001):
    dx = func(x + h, y) - func(x - h, y) / 2*h
    dy = func(x, y + h) - func(x, y + h) / 2*h
    return dx, dy