import requests

bearer_token = "AAAAAAAAAAAAAAAAAAAAAJiDlAEAAAAAiws20TtnnDRl%2F6i0ONDAKogh7cY%3Deee6F58LpWuDRPzYKpDodWB8tErvhXzvhlv9Z4vWFbJFcFCUn9"


def create_url(user_id):
    # Replace with user ID below
    return "https://api.twitter.com/2/users/{}/tweets?max_results=6&expansions=author_id&tweet.fields=created_at,geo,id,lang,public_metrics,source,text&user.fields=created_at,description,id,location,name,profile_image_url,public_metrics,url,username".format(user_id)


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def info(user_id):
    url = create_url(user_id)
    return(connect_to_endpoint(url))


