# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    k = int(input())
    room_number_list = list(map(int, input().split(" ")))
    room_number_list = sorted(room_number_list)
    
    captain_room = 0;
    for i in range(1, len(room_number_list)):
        if(i != len(room_number_list) - 1):
            if(room_number_list[i] != room_number_list[i+1] and room_number_list[i] != room_number_list[i-1]):
                captain_room = room_number_list[i]
                break
        else:
            captain_room = room_number_list[i]
            
    print(captain_room)