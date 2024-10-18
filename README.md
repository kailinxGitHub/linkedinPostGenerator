# linkedinPostGenerator
### Files and Directories

- **contentGenerationForm/**: Contains the logic for querying GPT to generate content.
  - `queryGPT.py`: Contains the `query` function used to generate content.
- **modelForm/**: Contains the logic for model content retrieval and generation.
  - `modelContentRetrieval.py`: Handles retrieval of model content.
  - `modelGeneration.py`: Handles generation of model content.
- **ui.py**: The main application file that sets up the Streamlit interface.
- **environment.yml**: Conda environment configuration file.
- **.env**: Environment variables file.
- **.gitignore**: Git ignore file.
- **README.md**: Project documentation.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd linkedinPostGenerator
    ```

2. Create and activate a Conda environment:
    ```sh
    conda env create -f environment.yml
    conda activate linkedinPostGenerator
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run ui.py
    ```

2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

3. Use the sidebar forms to input the necessary information:
    - **Model Form**: Specify the model influencer.
    - **Content Generation Form**: Provide the temperature, max tokens, context, and content for the post.

4. Click the "Write" button to generate the LinkedIn post.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License.