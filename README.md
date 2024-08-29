# IMSTA - Image Analyzer for Instagram Post Generation

This Python project allows you to analyze images in a directory, rename them sequentially, and generate Instagram post content (captions and hashtags) using the OpenAI API. The project includes functionalities for encoding images, sending them to the OpenAI API, and handling the responses to create engaging social media content.

## Features

- **Sequential Image Renaming**: Automatically renames images in a directory to a sequential format (`img_01.jpg`, `img_02.jpg`, etc.).
- **Base64 Image Encoding**: Encodes images in base64 format for API requests.
- **OpenAI API Integration**: Sends encoded images to the OpenAI API for content analysis and generation.
- **Terminal Visualization**: Outputs progress and results in a visually appealing format using colorized terminal output.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Install the Required Python Packages:**

    Install the necessary Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Your OpenAI API Key:**

    Replace the placeholder api_key in the script with your actual OpenAI API key. You can get your API key from OpenAI's platform.

## Usage

1. **Place Your Images in the images Directory:**

    Ensure that the images you want to analyze are placed in the images directory.

    ![](https://i.postimg.cc/gcn7wd92/gif-1.gif)

1. **Run the Script:**

    Execute the Python script to rename the images, encode them, and analyze them using the OpenAI API:

    ```bash
    python api-insta.py
    ```

    ![](https://i.postimg.cc/SxBSPVWW/Enregistrement-de-l-e-cran-2024-08-29-a-10-03-13.gif)

3. **View the Results:**

    The script will output the results in the terminal, showing the renamed files and the API responses for each image, including the generated captions and hashtags.

### Example of a generated caption:

    A breathtaking sunset over the mountains.
    Generated Hashtags: #sunset #mountains #nature #travel #photography

## Requirements

    Python 3.7+
    An OpenAI API key
    openai
    plaintext
    requests
    colorama

## License

*This project is licensed under the MIT License. See the LICENSE file for more details.*

*Мир - это единственная битва, которую стоит вести.*