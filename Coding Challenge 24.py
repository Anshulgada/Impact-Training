from typing import List


def scan_disk_schedule(head_position: int, requests: List[int]) -> List[int]: 

    requests.sort()

    i = 0
    while (i < len(requests) and head_position >= requests[i]):
        i += 1
        
    requests = requests[:i][::-1] + requests[i:]

    print("Order of serviced requests:", requests)


head_position = int(input())
requests = list(map(int, input().split(' ')))
scan_disk_schedule(head_position, requests)