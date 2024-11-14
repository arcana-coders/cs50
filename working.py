import re

def main():
    print(convert(input("Hours: ")))

def convert(time):
    fullhr = r'(\d{1,2})(:[0-5][0-9])? (AM|PM) to (\d{1,2})(:[0-5][0-9])? (AM|PM)'
    match = re.match(fullhr, time)
    
    if match:
        start_hour = match.group(1)
        start_minute = match.group(2)[1:] if match.group(2) else "00" 
        start_period = match.group(3)
        end_hour = match.group(4)
        end_minute = match.group(5)[1:] if match.group(5) else "00"  
        end_period = match.group(6)
        
        if not (1 <= int(start_hour) <= 12) or not (1 <= int(end_hour) <= 12):
            raise ValueError("Hours must be between 1 and 12")
        
        start_24 = convert_to_24_hour_format(start_hour, start_minute, start_period)
        
        end_24 = convert_to_24_hour_format(end_hour, end_minute, end_period)
        
        return f"{start_24} to {end_24}"
    else:
        raise ValueError("Invalid time format")

def convert_to_24_hour_format(hour, minute, period):
    hour = int(hour)
    minute = int(minute)

    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0
    
    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()

