# Facebook Comments Retrieval Script

This script retrieves comments from a Facebook post and saves them into an Excel file.

## Prerequisites

- Python installed on your system.
- Required packages installed. You can install them by running:
    ```bash
    pip install requests pandas
    ```

## Usage

1. Obtain your Facebook API credentials:
    - **Page ID**: Your Facebook Page ID.
    - **Post ID**: The ID of the post from which you want to retrieve comments.
    - **Access Token**: Your access token generated from [Facebook for Developers](https://developers.facebook.com/tools/explorer/).

2. Add your API credentials to the script:
    ```python
    page_id = 'your_page_id_here'
    post_id = 'your_post_id_here'
    access_token = 'your_access_token_here'
    ```

3. Run the script:
    ```bash
    python retrieve_comments.py
    ```

4. The comments will be saved to an Excel file named `comments.xlsx`.

## Credits

This script was developed by [Rob Williams](https://github.com/robwilliams18).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
