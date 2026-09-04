import math
from textual.app import App, ComposeResult
from textual.widgets import Static

LUMINANCE = ".,-~:;=!*#$@"

# theta/phi tables don't depend on A or B (the spin angles), so there's no
# reason to recompute cos/sin for them 20 times a second -- build once.
THETA_STEP = 0.07
PHI_STEP = 0.02
THETA_TABLE = [(math.cos(i * THETA_STEP), math.sin(i * THETA_STEP))
               for i in range(int(2 * math.pi / THETA_STEP))]
PHI_TABLE = [(math.cos(i * PHI_STEP), math.sin(i * PHI_STEP))
             for i in range(int(2 * math.pi / PHI_STEP))]


def render_donut(A: float, B: float, width: int, height: int) -> str:
    output = [" "] * (width * height)
    zbuffer = [0.0] * (width * height)

    cosA, sinA = math.cos(A), math.sin(A)
    cosB, sinB = math.cos(B), math.sin(B)

    half_w, half_h = width / 2, height / 2
    xscale, yscale = width * 0.4, height * 0.42

    for costheta, sintheta in THETA_TABLE:
        circlex = costheta + 2
        circley = sintheta

        for cosphi, sinphi in PHI_TABLE:
            x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
            y = circlex * (sinB * cosphi - sinA * cosB * sinphi) + circley * cosA * cosB
            z = 5 + cosA * circlex * sinphi + circley * sinA
            ooz = 1 / z

            xp = int(half_w + xscale * ooz * x)
            yp = int(half_h - yscale * ooz * y)

            L = (cosphi * costheta * sinB - cosA * costheta * sinphi
                 - sinA * sintheta + cosB * (cosA * sintheta - costheta * sinA * sinphi))

            if L > 0 and 0 <= xp < width and 0 <= yp < height:
                idx = xp + yp * width
                if ooz > zbuffer[idx]:
                    zbuffer[idx] = ooz
                    output[idx] = LUMINANCE[max(0, min(int(L * 8), len(LUMINANCE) - 1))]

    rows = ["".join(output[r * width:(r + 1) * width]) for r in range(height)]
    return "\n".join(rows)


class Donut(Static):
    WIDTH = 60
    HEIGHT = 30

    def __init__(self, *args, **kwargs) -> None:
        # markup=False: this is plain ASCII with no [style] tags, so skip
        # Rich's markup parsing on every single update() call.
        super().__init__(*args, markup=False, **kwargs)
        self.angle_a = 0.0
        self.angle_b = 0.0

    def on_mount(self) -> None:
        self.set_interval(1 / 20, self.spin)

    def spin(self) -> None:
        self.angle_a += 0.08
        self.angle_b += 0.03
        self.update(render_donut(self.angle_a, self.angle_b, self.WIDTH, self.HEIGHT))


class DonutApp(App):
    def compose(self) -> ComposeResult:
        yield Donut()


if __name__ == "__main__":
    DonutApp().run()
