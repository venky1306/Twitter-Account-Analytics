import requests


bearer_token = "AAAAAAAAAAAAAAAAAAAAAJiDlAEAAAAAiws20TtnnDRl%2F6i0ONDAKogh7cY%3Deee6F58LpWuDRPzYKpDodWB8tErvhXzvhlv9Z4vWFbJFcFCUn9"

users = ["BarackObama","elonmusk",'justinbieber','katyperry','rihanna','Cristiano','taylorswift13',
            'realDonaldTrump','narendramodi','ladygaga','YouTube','EllenDeGeneres','KimKardashian','NASA',
            'selenagomez','Twitter','cnnbrk','jtimberlake','BillGates','CNN']


def create_url():
    people = ','.join(users)
    usernames = "usernames={}".format(people)
    data_requried = 'id,name,profile_image_url,public_metrics,username,withheld'
    user_fields = "user.fields={}".format(data_requried)
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def get_users():
    url = create_url()
    return(connect_to_endpoint(url))



