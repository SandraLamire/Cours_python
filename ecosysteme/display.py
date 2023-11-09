import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("TkAgg")


def display_ecosystem(
            ecosystem,
            update_ecosystem_callback,
            number_of_steps=100,
        ):
    """
        Display an ecosystem in a grid with Matplotlib
        :param ecosystem: the ecosystem to display
        :param update_ecosystem_callback: a function that takes an ecosystem as parameter and returns an updated ecosystem
        :param number_of_steps: the number of steps to display
    """
    assert callable(update_ecosystem_callback), "update_ecosystem_callback must be a function"
    assert isinstance(number_of_steps, int), "number_of_steps must be an integer"
    assert number_of_steps > 0, "number_of_steps must be greater than 0"
    assert isinstance(ecosystem, list), "ecosystem must be a list"
    assert len(ecosystem) > 0, "ecosystem must not be empty"
    assert isinstance(ecosystem[0], list), "ecosystem must be a list of lists"
    assert len(ecosystem[0]) > 0, "ecosystem must not be a list of empty lists"
    assert isinstance(ecosystem[0][0], int), "ecosystem must be a list of lists of integers"
    assert len(ecosystem) == len(ecosystem[0]), "ecosystem must be a square matrix"

    # Create figure and axes for grid display
    fig, ax = plt.subplots()

    # Display the color grid with imshow()
    im = ax.imshow(ecosystem, cmap='viridis')  # cmap is an optional parameter to define the colormap (viridis is a default colormap of Matplotlib)
    # Refresh the figure at each iteration
    for _ in range(number_of_steps):
        # Update grid data with set_data()
        im.set_data(ecosystem)

        ecosystem = update_ecosystem_callback(ecosystem)

        # Update display
        plt.draw()
        plt.pause(1)  # Add a pause to give the impression of dynamism

    plt.show()
