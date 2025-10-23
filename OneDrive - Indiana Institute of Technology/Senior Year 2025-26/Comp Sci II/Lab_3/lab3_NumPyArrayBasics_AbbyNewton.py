# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
import time

# For regular Python, plots will open in separate windows
plt.style.use('seaborn-v0_8-darkgrid') # Make plots look nice!

# Set random seed for reproducibility
np.random.seed(42)

print("Lab environment ready!")
print(f"NumPy version: {np.__version__}")

def exercise_1_1():
    """
    Create arrays using different methods and visualize them.
    """
    print("="*50)
    print("Exercise 1.1: Array Creation Methods")
    print("="*50)
    # TODO: Create the following arrays
    # 1. An array of integers from 0 to 20
    array_range = None # Your code here
        # 2. An array of 50 evenly spaced points between 0 and 2π
    array_linear = None # Your code here
    # 3. A 5x5 identity matrix
    identity_matrix = None # Your code here
    # 4. A 3x3 matrix filled with random integers between 1 and 10
    random_matrix = None # Your code here
    # Visualization (provided)
    if array_range is not None and array_linear is not None:
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
        # Plot 1: Bar chart of range array
        axes[0, 0].bar(range(len(array_range)), array_range, color='skyblue')
        axes[0, 0].set_title('Array Range (0 to 20)')
        axes[0, 0].set_xlabel('Index')
        axes[0, 0].set_ylabel('Value')
        # Plot 2: Sine wave using linear space
        if array_linear is not None:
            sine_wave = np.sin(array_linear)
            axes[0, 1].plot(array_linear, sine_wave, 'b-', linewidth=2)
            axes[0, 1].set_title('Sine Wave')
            axes[0, 1].set_xlabel('Radians')
            axes[0, 1].set_ylabel('sin(x)')
            axes[0, 1].grid(True)
        # Plot 3: Identity matrix as heatmap
        if identity_matrix is not None:
            im = axes[1, 0].imshow(identity_matrix, cmap='RdBu', vmin=0, vmax=1)
            axes[1, 0].set_title('5x5 Identity Matrix')
            plt.colorbar(im, ax=axes[1, 0])
        # Plot 4: Random matrix as heatmap
        if random_matrix is not None:
            im = axes[1, 1].imshow(random_matrix, cmap='viridis')
            axes[1, 1].set_title('3x3 Random Matrix')
            for i in range(3):
                for j in range(3):
                    axes[1, 1].text(j, i, f'{random_matrix[i, j]}',
                        ha='center', va='center', color='white')
            plt.colorbar(im, ax=axes[1, 1])
        plt.tight_layout()
        plt.show()
    return array_range, array_linear, identity_matrix, random_matrix
# Run the exercise
arrays = exercise_1_1()

def exercise_1_2():
    """
    Explore array attributes with different dimensional arrays.
    """
    print("\n" + "="*50)
    print("Exercise 1.2: Array Attributes")
    print("="*50)
    # Create arrays of different dimensions
    arr_1d = np.array([1, 2, 3, 4, 5])
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    # TODO: Fill in the attributes for each array
    arrays = [
        ("1D Array", arr_1d),
        ("2D Array", arr_2d),
        ("3D Array", arr_3d)
    ]
    for name, arr in arrays:
        print(f"\n{name}:")
        print(f" Array: {arr}")
        # TODO: Print the following attributes
        # - ndim (number of dimensions)
        # - shape
        # - size (total elements)
        # - dtype
        # - itemsize (bytes per element)
        # - nbytes (total bytes)
        # Your code here
    # Bonus: Create a visualization showing memory usage
    # TODO: Create a bar chart comparing nbytes for each array
    return arr_1d, arr_2d, arr_3d
# Run the exercise
exercise_1_2()

def exercise_2_1():
    """
    Compare performance between NumPy arrays and Python lists.
    Create visualizations showing the speed difference.
    """
    print("\n" + "="*50)
    print("Exercise 2.1: The Great Performance Race!")
    print("="*50)
    # Test different sizes
    sizes = [100, 1000, 10000, 100000]
    python_times = []
    numpy_times = []
    for size in sizes:
        # Create data
        python_list = list(range(size))
        numpy_array = np.arange(size)
        # TODO: Time Python list operation (squaring each element)
        start = time.time()
        # Your code here: Square each element using list comprehension
        python_result = None # Replace with your code
        python_time = time.time() - start
        python_times.append(python_time)
        # TODO: Time NumPy array operation (squaring each element)
        start = time.time()
        # Your code here: Square each element using NumPy
        numpy_result = None # Replace with your code
        numpy_time = time.time() - start
        numpy_times.append(numpy_time)
        # Calculate speedup
        speedup = python_time / numpy_time if numpy_time > 0 else 0
        print(f"Size {size:6}: Python: {python_time:.4f}s, NumPy: {numpy_time:.4f}s, Speedup: {speedup:.1f}x")
    # Create visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    # Plot 1: Time comparison
    x = np.arange(len(sizes))
    width = 0.35
    ax1.bar(x - width/2, python_times, width, label='Python List', color='coral')
    ax1.bar(x + width/2, numpy_times, width, label='NumPy Array', color='skyblue')
    ax1.set_xlabel('Array Size')
    ax1.set_ylabel('Time (seconds)')
    ax1.set_title('Performance Comparison: Python vs NumPy')
    ax1.set_xticks(x)
    ax1.set_xticklabels(sizes)
    ax1.legend()
    ax1.set_yscale('log') # Log scale for better visibility
    # Plot 2: Speedup factor
    speedups = [p/n if n > 0 else 0 for p, n in zip(python_times, numpy_times)]
    ax2.plot(sizes, speedups, 'go-', linewidth=2, markersize=10)
    ax2.set_xlabel('Array Size')
    ax2.set_ylabel('Speedup Factor')
    ax2.set_title('NumPy Speedup Over Python Lists')
    ax2.grid(True, alpha=0.3)
    ax2.set_xscale('log')
    plt.tight_layout()
    plt.show()
    return python_times, numpy_times
# Run the performance comparison
exercise_2_1()

def exercise_3_1():
    """
    Create pixel art using NumPy arrays and matplotlib!
    """
    print("\n" + "="*50)
    print("Exercise 3.1: NumPy Pixel Art")
    print("="*50)
    # TODO: Create a simple smiley face using a 10x10 grid
    # Use 0 for background, 1 for yellow (face), 2 for black (eyes, mouth)
    smiley = np.zeros((10, 10))
    # TODO: Fill in the face (hint: use array slicing)
    # Make a circular-ish face by setting appropriate pixels to 1
    # TODO: Add eyes (set appropriate pixels to 2)
    # TODO: Add a smile (set appropriate pixels to 2)
    # Display the pixel art
    plt.figure(figsize=(6, 6))
    plt.imshow(smiley, cmap='YlOrBr', interpolation='nearest')
    plt.title('NumPy Pixel Art: Smiley Face')
    plt.axis('off')
    plt.show()
    # Bonus: Create your own pixel art design!
    # TODO: Create a 15x15 array with your own design
    my_art = np.zeros((15, 15))
    # Your creative design here!
    return smiley, my_art
# Create pixel art
exercise_3_1()

def exercise_3_2():
    """
    Use broadcasting to create beautiful color gradients.
    """
    print("\n" + "="*50)
    print("Exercise 3.2: Color Gradients with Broadcasting")
    print("="*50)
    # Create coordinate arrays
    width, height = 256, 256
    # TODO: Create x and y coordinate arrays using broadcasting
    # Hint: Create a column vector and row vector, then use broadcasting
    x = None # Your code here - should be shape (256, 1)
    y = None # Your code here - should be shape (1, 256)
    # Create different gradient patterns using broadcasting
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    # Gradient 1: Linear horizontal
    gradient1 = None # TODO: Create using x
    # Gradient 2: Linear vertical
    gradient2 = None # TODO: Create using y
    # Gradient 3: Diagonal
    gradient3 = None # TODO: Create using x + y
    # Gradient 4: Circular (distance from center)
    # TODO: Calculate distance from center (128, 128)
    center_x, center_y = 128, 128
    gradient4 = None # Hint: use np.sqrt((x - center_x)**2 + (y - center_y)**2)
    # Gradient 5: Sine wave pattern
    gradient5 = None # TODO: Create using np.sin(x * 0.1) * np.cos(y * 0.1)
    # Gradient 6: Your creative pattern!
    gradient6 = None # TODO: Create your own pattern
    # Display all gradients
    gradients = [gradient1, gradient2, gradient3, gradient4, gradient5, gradient6]
    titles = ['Horizontal', 'Vertical', 'Diagonal', 'Circular', 'Sine Wave', 'Creative']
    for ax, grad, title in zip(axes.flat, gradients, titles):
        if grad is not None:
            ax.imshow(grad, cmap='viridis')
        ax.set_title(title)
        ax.axis('off')
    plt.tight_layout()
    plt.show()
    return gradients
# Create gradients
exercise_3_2()

def exercise_4_1():
    """
    Analyze temperature data from multiple weather stations.
    """
    print("\n" + "="*50)
    print("Exercise 4.1: Weather Station Analysis")
    print("="*50)
    # Simulate temperature data for 5 stations over 30 days
    # Each row is a station, each column is a day
    np.random.seed(42)
    base_temps = np.array([20, 22, 18, 25, 15]) # Base temperature for each station
    # TODO: Generate temperature data with daily variations
    # Add random variations between -5 and +5 degrees
    daily_variations = None # Your code here - shape should be (5, 30)
    temperatures = None # Your code here - add base_temps to variations
    # TODO: Calculate statistics for each station
    # 1. Mean temperature per station
    mean_temps = None # Your code here
    # 2. Max temperature per station
    max_temps = None # Your code here
    # 3. Min temperature per station
    min_temps = None # Your code here
    # 4. Temperature range per station
    temp_ranges = None # Your code here
    # TODO: Find the hottest day across all stations
    hottest_day_index = None # Your code here
    hottest_temp = None # Your code here
    # TODO: Find the coldest day across all stations
    coldest_day_index = None # Your code here
    coldest_temp = None # Your code here
    # Print results
    station_names = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E']
    print("\n Weather Station Statistics:")
    for i, name in enumerate(station_names):
        if mean_temps is not None:
            print(f"{name}: Mean={mean_temps[i]:.1f}°C, "
                f"Max={max_temps[i]:.1f}°C, "
                f"Min={min_temps[i]:.1f}°C, "
                f"Range={temp_ranges[i]:.1f}°C")
    if hottest_day_index is not None:
        print(f"\n Hottest day: Day {hottest_day_index + 1} with {hottest_temp:.1f}°C")
    if coldest_day_index is not None:
        print(f" Coldest day: Day {coldest_day_index + 1} with {coldest_temp:.1f}°C")
    # Create visualizations
    if temperatures is not None:
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        # Plot 1: Temperature heatmap
        im = axes[0, 0].imshow(temperatures, cmap='coolwarm', aspect='auto')
        axes[0, 0].set_title('Temperature Heatmap (°C)')
        axes[0, 0].set_xlabel('Day')
        axes[0, 0].set_ylabel('Station')
        axes[0, 0].set_yticks(range(5))
        axes[0, 0].set_yticklabels(station_names)
        plt.colorbar(im, ax=axes[0, 0])
        # Plot 2: Daily temperature trends
        days = np.arange(1, 31)
        for i, name in enumerate(station_names):
            axes[0, 1].plot(days, temperatures[i], label=name, linewidth=2)
            axes[0, 1].set_title('Daily Temperature Trends')
            axes[0, 1].set_xlabel('Day')
            axes[0, 1].set_ylabel('Temperature (°C)')
            axes[0, 1].legend(loc='best')
            axes[0, 1].grid(True, alpha=0.3)
    # Plot 3: Station comparison (box plot style)
    if mean_temps is not None:
        x_pos = np.arange(len(station_names))
        axes[1, 0].bar(x_pos, mean_temps, color='skyblue', label='Mean')
        axes[1, 0].errorbar(x_pos, mean_temps,
            yerr=[(mean_temps - min_temps), (max_temps - mean_temps)],
            fmt='none', color='black', capsize=5, label='Range')
        axes[1, 0].set_title('Station Temperature Comparison')
        axes[1, 0].set_xlabel('Station')
        axes[1, 0].set_ylabel('Temperature (°C)')
        axes[1, 0].set_xticks(x_pos)
        axes[1, 0].set_xticklabels(station_names)
        axes[1, 0].legend()
        # Plot 4: Daily average across all stations
        daily_avg = temperatures.mean(axis=0)
        axes[1, 1].fill_between(days, daily_avg, alpha=0.3, color='green')
        axes[1, 1].plot(days, daily_avg, 'g-', linewidth=2)
        axes[1, 1].set_title('Daily Average Temperature (All Stations)')
        axes[1, 1].set_xlabel('Day')
        axes[1, 1].set_ylabel('Temperature (°C)')
        axes[1, 1].grid(True, alpha=0.3)
        # Mark hottest and coldest days
        if hottest_day_index is not None:
            axes[1, 1].plot(hottest_day_index + 1, daily_avg[hottest_day_index],
                'ro', markersize=10, label=f'Hottest: Day {hottest_day_index + 1}')
        if coldest_day_index is not None:
            axes[1, 1].plot(coldest_day_index + 1, daily_avg[coldest_day_index],
                'bo', markersize=10, label=f'Coldest: Day {coldest_day_index + 1}')
        axes[1, 1].legend()
        plt.tight_layout()
        plt.show()
    return temperatures, mean_temps, max_temps, min_temps
# Run weather analysis
exercise_4_1()

def challenge_1():
    """
    Create a magic square where all rows, columns, and diagonals sum to the same value.
    """
    print("\n" + "="*50)
    print("Challenge 1: Magic Square")
    print("="*50)
    # A 3x3 magic square
    magic = np.array([[2, 7, 6],
            [9, 5, 1],
            [4, 3, 8]])
    # TODO: Verify it's a magic square by checking:
    # 1. All row sums are equal
    # 2. All column sums are equal
    # 3. Both diagonal sums are equal
    row_sums = None # Your code here
    col_sums = None # Your code here
    diag1_sum = None # Your code here (main diagonal)
    diag2_sum = None # Your code here (anti-diagonal)
    # Print your results
    print(f"Row sums: {row_sums}")
    print(f"Column sums: {col_sums}")
    print(f"Main diagonal sum: {diag1_sum}")
    print(f"Anti-diagonal sum: {diag2_sum}")
    # TODO: Create your own 4x4 magic square
    # Hint: One approach is to use a pattern or look up magic square algorithms
    magic_4x4 = None # Your code here
    return magic, magic_4x4
# Try the challenge
challenge_1()

def challenge_2():
    """
    Create and transform a simple image using NumPy operations.
    """
    print("\n" + "="*50)
    print("Challenge 2: Image Transformations")
    print("="*50)
    # Create a simple 20x20 checkerboard pattern
    size = 20
    checkerboard = np.zeros((size, size))
    # TODO: Create checkerboard pattern
    # Hint: Use slicing with step size
    # Make alternating 2x2 squares of 0s and 1s
    # TODO: Apply transformations
    # 1. Rotate 90 degrees (hint: use np.rot90)
    rotated = None
    # 2. Flip horizontally (hint: use np.fliplr or slicing)
    flipped_h = None
    # 3. Flip vertically (hint: use np.flipud or slicing)
    flipped_v = None
    # 4. Invert colors (1s become 0s, 0s become 1s)
    inverted = None
    # 5. Create your own transformation!
    your_transform = None
    # Display all transformations
    fig, axes = plt.subplots(2, 3, figsize=(10, 7))
    images = [checkerboard, rotated, flipped_h, flipped_v, inverted, your_transform]
    titles = ['Original', 'Rotated 90°', 'Flipped H', 'Flipped V', 'Inverted', 'Your Transform']
    for ax, img, title in zip(axes.flat, images, titles):
        if img is not None:
            ax.imshow(img, cmap='gray', interpolation='nearest')
            ax.set_title(title)
            ax.axis('off')
    plt.tight_layout()
    plt.show()
    return checkerboard, rotated, flipped_h, flipped_v, inverted
# Try the challenge
challenge_2()

def test_submission():
    """
    Test that all exercises run without errors.
    """
    print("Testing your submission...")
    try:
        # Test each exercise
        print("Testing Exercise 1.1...")
        exercise_1_1()
        print("Testing Exercise 1.2...")
        exercise_1_2()
        print("Testing Exercise 2.1...")
        exercise_2_1()
        print("Testing Exercise 3.1...")
        exercise_3_1()
        print("Testing Exercise 3.2...")
        exercise_3_2()
        print("Testing Exercise 4.1...")
        exercise_4_1()
        print("Testing Challenge 1...")
        challenge_1()
        print("Testing Challenge 2...")
        challenge_2()
        print("\n All tests passed! Ready to submit.")
    except Exception as e:
        print(f"\n Error found: {e}")
        print("Please fix the error before submitting.")
# Run the test
test_submission()

def bonus_animation():
    """
    Create an animated sine wave using NumPy and matplotlib.
    Note: This creates multiple plots to simulate animation.
    """
    print("\n" + "="*50)
    print("BONUS: Animated Sine Wave")
    print("="*50)
    # TODO: Create an animation that shows a wave moving
    # Hint: Use a loop to create multiple frames with different phases
    # Your creative animation code here!
    pass
# Uncomment to run the animation
# bonus_animation()
