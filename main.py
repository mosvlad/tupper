from typing import List, Tuple
import numpy as np
import pygame
from dataclasses import dataclass


class TupperFormula:
    def __init__(self, height: int = 17, width: int = 106):
        self.height = height
        self.width = width
        self.cells = [[False for _ in range(width)] for _ in range(height)]

    def evaluate(self, x: int, y: int, k: int) -> bool:
        return ((k + y) // 17 // 2 ** (17 * int(x) + int(y) % 17)) % 2 > 0.5

    def generate_from_k(self, k: int) -> List[List[bool]]:
        self.cells = [[self.evaluate(x, y, k) for x in range(self.width)]
                      for y in range(self.height)]
        return self.cells

    def calculate_k(self, cells: List[List[bool]]) -> int:
        binary = ''
        for i in range(self.width):
            for j in range(self.height - 1, -1, -1):
                binary += '1' if cells[j][i] else '0'
        k = int(binary, 2)
        return k * self.height

    def save_to_file(self, filename: str):
        np.save(filename, np.array(self.cells))

    def load_from_file(self, filename: str):
        self.cells = np.load(filename).tolist()


@dataclass
class VisualizerConfig:
    scale: int = 2
    field_size_x: int = 106
    field_size_y: int = 17

    @property
    def screen_w(self) -> int:
        return 742 * self.scale

    @property
    def screen_h(self) -> int:
        return 119 * self.scale

    @property
    def cell_size_x(self) -> int:
        return int(self.screen_w / self.field_size_x)

    @property
    def cell_size_y(self) -> int:
        return int(self.screen_h / self.field_size_y)


class TupperVisualizer:
    def __init__(self, config: VisualizerConfig = VisualizerConfig()):
        self.config = config
        pygame.init()
        self.screen = pygame.display.set_mode([config.screen_w, config.screen_h])
        self.drawing = False
        self.formula = TupperFormula()

    def get_cell_coordinates(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        x = int(pos[1] / self.config.cell_size_x)
        y = abs(int(pos[0] / self.config.cell_size_y) - (int(self.config.screen_w / self.config.cell_size_x) - 1)) # FIX IT
        print(x, y)
        return x, y

    def draw_grid(self):
        for i in range(self.config.field_size_x):
            for j in range(self.config.field_size_y):
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (i * self.config.screen_h / self.config.field_size_y, j),
                                 (i * self.config.screen_h / self.config.field_size_y, self.config.screen_w))
                pygame.draw.line(self.screen, (0, 0, 0),
                                 (i, j * self.config.screen_w / self.config.field_size_x),
                                 (self.config.screen_w, j * self.config.screen_w / self.config.field_size_x))

    def draw_cells(self):
        cells = [row[::-1] for row in self.formula.cells]
        for x in range(len(cells)):
            for y in range(len(cells[x])):
                if cells[x][y]:
                    pygame.draw.rect(
                        self.screen, (0, 0, 0),
                        pygame.Rect(
                            y * self.config.screen_w / self.config.field_size_x,
                            x * self.config.screen_h / self.config.field_size_y,
                            self.config.cell_size_x,
                            self.config.cell_size_y
                        )
                    )

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.drawing = True
                pos = pygame.mouse.get_pos()
                x, y = self.get_cell_coordinates(pos)
                self.formula.cells[x][y] = not self.formula.cells[x][y]

            elif event.type == pygame.MOUSEBUTTONUP:
                self.drawing = False
                k = self.formula.calculate_k(self.formula.cells)
                print(f"Generated k value: {k}")

            elif event.type == pygame.MOUSEMOTION and self.drawing:
                pos = pygame.mouse.get_pos()
                x, y = self.get_cell_coordinates(pos)
                self.formula.cells[x][y] = True

        return True

    def run(self):
        running = True
        while running:
            running = self.handle_events()

            self.screen.fill((255, 255, 255))
            self.draw_grid()
            self.draw_cells()
            pygame.display.flip()

        pygame.quit()


def visualize_k(k: int):
    formula = TupperFormula()
    formula.generate_from_k(k)

    visualizer = TupperVisualizer()
    visualizer.formula = formula
    visualizer.run()


def create_new_image():
    visualizer = TupperVisualizer()
    visualizer.run()


if __name__ == "__main__":
    # Example k value for "FABLAB"
    k = 4839804616377261396274084291097975584006211355337299053212959775126516568114007954556318202515699186677267721876170118812980641538458955070016764792191723669583173862780236893045798768843687756537200423675156017868767945316136068245963816122674631513592469265745832011443338641947808633470245363524455738117874273557756018464067952848548829234240228868247978794759412244789316937643159083908353992826320056216756488531212678880995576545472238662588770290645649507020974476681450793619946810044083740505511175591595902846716460942328916120533009

    visualize_k(k)  # Visualize existing k value
    #create_new_image()  # Create new image from scratch