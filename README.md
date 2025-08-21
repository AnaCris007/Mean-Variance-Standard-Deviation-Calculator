# Mean, Variance, and Standard Deviation Calculator

This project consists of a Python function that calculates the mean, variance, standard deviation, maximum, minimum, and sum of a list of nine numbers. The function uses the NumPy library to efficiently perform calculations on a 3x3 matrix.

## Features

The `calculate()` function takes a list of 9 numbers and returns a dictionary containing:

-   **Mean**: Mean along axes 0 and 1, and of the entire matrix.
-   **Variance**: Variance along axes 0 and 1, and of the entire matrix.
-   **Standard Deviation**: Standard deviation along axes 0 and 1, and of the entire matrix.
-   **Maximum**: Maximum value along axes 0 and 1, and of the entire matrix.
-   **Minimum**: Minimum value along axes 0 and 1, and of the entire matrix.
-   **Sum**: Total sum along axes 0 and 1, and of the entire matrix.

## How to Use

### Prerequisites

-   Python 3.x
-   NumPy

You can install the necessary dependency with:

```bash
pip install numpy
```

### Running

1.  Import the `calculate` function from the `mean_var_std.py` file.
2.  Call the function, passing a list of 9 numbers.

**Example:**

```python
import mean_var_std

# Call the function with a list of 9 numbers
result = mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

# Print the result
print(result)
```

### Expected Output

The output will be a dictionary formatted as follows:

```json
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## ⚠️ Error Handling

If the provided list does not contain exactly 9 numbers, the function will raise a `ValueError` with the message: "List must contain nine numbers."
