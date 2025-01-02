# Tupper's Formula Visualizer

An interactive Python implementation of Tupper's self-referential formula with a PyGame-based visualization tool. This project allows you to both visualize existing k-values and create new bitmap images that can be converted into their corresponding k-values.

![Tupper's Formula Interface](./images/interface_demo.png)

## About Tupper's Formula

Tupper's self-referential formula is a remarkable mathematical curiosity that, when plotted, can visually represent any bitmap image within a 106×17 pixel grid. The formula uses a specific number (k) to generate the image, and conversely, any 106×17 bitmap can be converted back into its corresponding k-value.

## Examples

Here are some examples of what you can create and visualize with this tool:

### Example 1: "FABLAB" Text
![FABLAB Example](./images/fablab_example.png)
```python
k = 4839804616377261396274084291097975584006211355337299053212959775126516568114007954556318202515699186677267721876170118812980641538458955070016764792191723669583173862780236893045798768843687756537200423675156017868767945316136068245963816122674631513592469265745832011443338641947808633470245363524455738117874273557756018464067952848548829234240228868247978794759412244789316937643159083908353992826320056216756488531212678880995576545472238662588770290645649507020974476681450793619946810044083740505511175591595902846716460942328916120533009
```

### Example 2: Simple Shape
![Simple Shape Example](./images/shape_example.png)
```python
k = 960939379918958884971672962127852754715004339660129306651505519271702802395266424689642842174350718121267153782770623355993237280874144307891325963941337723487857735749823926629715517173716995165232890538221612403238855866184013235585136048828693337902491454229288667081096184496091705183454067827731551705405381627380967602565625016981482083418783163849115590225610003652351370343874461848378737238198224849863465033159410054974700593138339226497249461751545728366702369745461014655997933798537483143786841806593422227898388722980000748404719
```

### Example 3: Drawing Interface
![Drawing Interface](./images/drawing_demo.gif)

## Features

- Visualize any valid k-value as a 106×17 bitmap image
- Interactive drawing interface to create custom images
- Real-time k-value calculation for drawn images
- Grid-based visualization with adjustable scale
- Save and load functionality for created images

## Requirements

- Python 3.6+
- NumPy
- PyGame

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mosvlad/tupper
cd tupper
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Visualizing an Existing K-value

```python
from tupper_visualizer import visualize_k

# Example k-value that displays "FABLAB"
k = 4839804616377261396274084291097975584006211355337299053212959775126516568114007954556318202515699186677267721876170118812980641538458955070016764792191723669583173862780236893045798768843687756537200423675156017868767945316136068245963816122674631513592469265745832011443338641947808633470245363524455738117874273557756018464067952848548829234240228868247978794759412244789316937643159083908353992826320056216756488531212678880995576545472238662588770290645649507020974476681450793619946810044083740505511175591595902846716460942328916120533009

visualize_k(k)
```

### Creating a New Image

```python
from tupper_visualizer import create_new_image

create_new_image()
```

## Interactive Controls

- Left mouse button: Toggle cells (black/white)
- Click and drag: Draw continuously
- Close window: Exit the program

The k-value for your drawing will be printed to the console whenever you release the mouse button.

## Project Structure

- `TupperFormula`: Core class implementing the formula's logic
- `VisualizerConfig`: Configuration class for visualization parameters
- `TupperVisualizer`: PyGame-based visualization interface
- Helper functions for quick usage (`visualize_k` and `create_new_image`)


## Customization

You can adjust the visualization parameters by modifying the `VisualizerConfig` class:

```python
config = VisualizerConfig(
    scale=2,  # Adjust window scale
    field_size_x=106,  # Width in cells
    field_size_y=17    # Height in cells
)
visualizer = TupperVisualizer(config)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Jeff Tupper for creating the original self-referential formula
- PyGame community for the excellent graphics library
- All contributors and users of this project

## Author

[Your Name]

## References

- [Tupper's Self-Referential Formula (Wikipedia)](https://en.wikipedia.org/wiki/Tupper%27s_self-referential_formula)
- [PyGame Documentation](https://www.pygame.org/docs/)