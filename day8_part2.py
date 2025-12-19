
def parse_points(path: str) -> list[tuple[int, int, int]]:
    points: list[tuple[int, int, int]] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x_str, y_str, z_str = line.split(",")
            points.append((int(x_str), int(y_str), int(z_str)))
    return points


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        parent = self.parent
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True


def build_edges(points: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    n = len(points)
    edges: list[tuple[int, int, int]] = []
    for i in range(n - 1):
        xi, yi, zi = points[i]
        for j in range(i + 1, n):
            xj, yj, zj = points[j]
            dx = xi - xj
            dy = yi - yj
            dz = zi - zj
            d2 = dx * dx + dy * dy + dz * dz
            edges.append((d2, i, j))
    edges.sort(key=lambda t: t[0])
    return edges


def solve(path: str = "input.txt") -> int:
    points = parse_points(path)
    edges = build_edges(points)

    dsu = DSU(len(points))
    last_merge: tuple[int, int] | None = None

    for k, (_d2, i, j) in enumerate(edges):
        merged = dsu.union(i, j)

        if merged:
            last_merge = (i, j)
            if dsu.components == 1:
                break

    i, j = last_merge
    return points[i][0] * points[j][0]


print(solve("input.txt"))