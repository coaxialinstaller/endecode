import base64
import random

## Encode base16
def encode16(message):
    encoded_message = base64.b16encode(message)
    return encoded_message

## Encode base32
def encode32(message):
    encoded_message = base64.b32encode(message)
    return encoded_message

## Encode base64
def encode64(message):
    encoded_message = base64.b64encode(message)
    return encoded_message

def random_encoding(message, turns):
    message_bytes = message
    for x in range(turns):
        choises_list = ["encode16", "encode32", "encode64"]
        choises_dict = {"encode16": encode16(message_bytes), "encode32": encode32(message_bytes), "encode64": encode64(message_bytes)}
        message_bytes = choises_dict[random.choice(choises_list)]
        print(f"\r{x+1}/{turns}", end="\r")
    
    return message_bytes.decode("utf-8")

def encode(message, base, turns):
    encoded_message = message
    if base == "16":
        for x in range(turns):
            last = encoded_message
            encoded_message = encode16(last)
            print(f"\r{x+1}/{turns}", end="\r")

    elif base == "32":
        for x in range(turns):
            last = encoded_message
            encoded_message = encode32(last)
            print(f"\r{x+1}/{turns}", end="\r")

    elif base == "64":
        for x in range(turns):
            last = encoded_message
            encoded_message = encode64(last)
            print(f"\r{x+1}/{turns}", end="\r")

    return(last.decode("utf-8"))

def interface(message):
    print("What base encoding to choose?")
    print("base16(1), base32(2), base64(3), random(4)")
    encoded_type = input()
    while encoded_type not in ["1", "2", "3", "4"]:
        print("You need to type in 1,2,3 or 4")
        encoded_type = input()
    
    print("Who many times do you want to encode it? (1-1000 times)")
    encode_turns = int(input())
    while encode_turns not in range(1,1001):
        print("It needs to be between 1 and 1000 times")
        encode_turns = int(input())

    if encoded_type == "1":
        encoded_message = encode(message, "16", encode_turns)
    elif encoded_type == "2":
        encoded_message = encode(message, "32", encode_turns)
    elif encoded_type == "3":
        encoded_message = encode(message, "64", encode_turns)
    elif encoded_type == "4":
        encoded_message = random_encoding(message, encode_turns)

    return encoded_message

def main():
    while True:
        print("What would you like to encode?")
        print("File(1)")
        print("String(2)")
        to_encode = input().lower()
        
        while to_encode not in ["1", "2", "file", "string"]:
            print("You need to choose: File(1) or String (2)")
            to_encode = input().lower()

        if to_encode == "file":
            to_encode = "1"
        elif to_encode == "string":
            to_encode = "2"
        
        if to_encode == "1":
            while True:
                print("Input file path:")
                input_path = input()
                try:
                    print("Output file path: ")
                    output_path = input()
                    with open(input_path) as file:
                        message  = file.read()
                        encoded_message = interface(bytes(message, "utf-8"))
                    
                    with open(output_path, "w") as out:
                        out.write(encoded_message)
                    print("Done!")
                    return 1
                except:
                    print("Path does not exist")
                

        elif to_encode == "2":
            print("Inster string: ")
            string = input()
            print("Output file path: ")
            output_path = input()
            encoded_message = interface(bytes(string, "utf-8"))
            with open(output_path, "w") as out:
                out.write(encoded_message)
            print("Done!")
            return 1
            

if __name__ == "__main__":
    main()