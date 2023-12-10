import requests
import pandas as pd

def get_comments(page_id, post_id, access_token):
    url = f'https://graph.facebook.com/v16.0/{page_id}_{post_id}/comments?access_token={access_token}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for unsuccessful HTTP requests
        data = response.json()

        if 'data' in data:
            comments = data['data']
            excel_data = [{
                'name': comment['from']['name'],
                'time': comment['created_time'],
                'message': comment['message']
            } for comment in comments]

            df = pd.DataFrame(excel_data)
            df.to_excel('comments.xlsx', index=False)
            print("Comments saved to 'comments.xlsx'")
        else:
            print("No comments found.")

    except requests.RequestException as e:
        print(f"Request Exception: {e}")
    except KeyError as ke:
        print(f"KeyError: {ke} - Possibly missing data in the response")
    except Exception as ex:
        print(f"An error occurred: {ex}")

# Input your page_id, post_id, and access_token here
page_id = 'your_page_id_here'
post_id = 'your_post_id_here'
access_token = 'your_access_token_here'

get_comments(page_id, post_id, access_token)
