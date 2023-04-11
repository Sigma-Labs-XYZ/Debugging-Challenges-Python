# This is a function that will send a get request to a URL and time how long it takes the url to respoond (ping)
# Do not edit this code, the aim is to debug!

from typing import List

def send_pings(url: str = "https://www.google.com", n: int) -> List[int]: 
    """
    Sends n HTTP GET requests to the specified URL and returns a list of response times in milliseconds.
    
    Args:
    - url: A string representing the URL of the website to ping
    - n: An integer representing the number of pings to send
    
    Returns:
    - A list of integers representing the response times of each ping in milliseconds
    """
    response_times = "" 
    for i in range(n):
        try:
            response = requests.get(url)
            response_time = round(response.elapsed.total_seconds() * 1000)
            response_times.append(response_time)
            print("Ping {i+1}: {response_time} ms")
        except requests.exceptions.RequestException as e:
            print(f"Ping {i+1}: Failed ({e})")
            response_times.append(None)
    return response_times

if __name__ == "__main__":
    # Example usage
    ping_times = send_pings("https://www.google.com", 5)
    print(ping_times)
